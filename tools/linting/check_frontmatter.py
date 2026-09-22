#!/usr/bin/env python3
"""Validate YAML frontmatter across theory/ and practice/.

Also enforces the document contract: kind must match the directory where the
directory names one, and a canon file has a word cap. See theory/README.md.

No dependencies: the parser handles only the flat key/value and inline-list
shapes this repo uses, and rejects anything more complicated rather than
guessing. Run alongside check_playbook.py.

Scope is theory/ and practice/, excluding the linting directory. publishing/
is deliberately out of scope: style-references are verbatim records of what was
published, and .vale.ini already exempts them for the same reason.
"""
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SCOPE = ("theory", "practice")
EXCLUDE_DIRS = {".git", ".claude", "linting", "node_modules"}

REQUIRED = ("title", "layer", "kind", "status")
OPTIONAL = ("version", "operationalizes", "canonical_source")
LAYERS = {"theory", "practice"}
STATUSES = {"active", "under-review", "superseded"}
AXIOMS = {"axiom-1", "axiom-2", "axiom-3"}

# The document contract. What a file promises a reader decides how long it may
# be and what it may contain, which is the distinction the directory tree under
# theory/ is built on. See theory/README.md.
KINDS = {"canon", "reference", "argument", "evidence", "instrument"}

# Where the directory names the contract, the two must agree. practice/ is
# deliberately absent: it is flat on purpose and holds both instruments and
# references, so kind is declared there and not constrained by the path.
DIR_KIND = {
    "theory/canon/": "canon",
    "theory/reference/": "reference",
    "theory/arguments/": "argument",
    "theory/evidence/": "evidence",
}

# A ratchet, not a measurement. Canon states claims and sends the argument
# elsewhere, and the target is 3,000 words a file. The cap sits just above the
# largest canon file so that it cannot grow, and it is lowered as material
# moves out. Never raise it: raising it is how the cap stops meaning anything.
CANON_WORD_CAP = 4750


def parse_frontmatter(text, path):
    """Return (dict, errors). A missing block is an error, not an empty dict."""
    errors = []
    if not text.startswith("---\n"):
        return None, [f"{path}: no frontmatter block (file must open with '---')"]
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, [f"{path}: frontmatter block is never closed"]
    data = {}
    for i, line in enumerate(text[4:end].splitlines(), start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            errors.append(f"{path}:{i}: not a key/value line: {line!r}")
            continue
        key, _, raw = line.partition(":")
        key, raw = key.strip(), raw.strip()
        if key in data:
            errors.append(f"{path}:{i}: duplicate key {key!r}")
        if raw.startswith("[") and raw.endswith("]"):
            value = [v.strip() for v in raw[1:-1].split(",") if v.strip()]
        elif len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
            # Strip one matching pair only. Stripping characters piecemeal
            # mangles a title that legitimately ends in a quotation mark.
            value = raw[1:-1]
        else:
            value = raw
        data[key] = value
    return data, errors


def check_file(path, rel):
    errors = []
    text = open(path, encoding="utf-8").read()
    data, errors = parse_frontmatter(text, rel)
    if data is None:
        return errors

    for key in REQUIRED:
        if key not in data or data[key] == "":
            errors.append(f"{rel}: missing required key {key!r}")
    for key in data:
        if key not in REQUIRED + OPTIONAL:
            errors.append(f"{rel}: unknown key {key!r} (allowed: {', '.join(REQUIRED + OPTIONAL)})")

    layer = data.get("layer")
    if layer and layer not in LAYERS:
        errors.append(f"{rel}: layer {layer!r} not one of {sorted(LAYERS)}")
    elif layer and not rel.startswith(layer + "/"):
        errors.append(f"{rel}: layer {layer!r} does not match its directory")

    kind = data.get("kind")
    if kind and kind not in KINDS:
        errors.append(f"{rel}: kind {kind!r} not one of {sorted(KINDS)}")
    else:
        for prefix, required in DIR_KIND.items():
            if rel.startswith(prefix) and kind != required:
                errors.append(f"{rel}: kind {kind!r} does not match its directory, which requires {required!r}")

    status = data.get("status")
    if status and status not in STATUSES:
        errors.append(f"{rel}: status {status!r} not one of {sorted(STATUSES)}")

    ops = data.get("operationalizes")
    if ops is not None:
        if not isinstance(ops, list):
            errors.append(f"{rel}: operationalizes must be an inline list, e.g. [axiom-1, axiom-2]")
        else:
            for a in ops:
                if a not in AXIOMS:
                    errors.append(f"{rel}: operationalizes has {a!r}, not one of {sorted(AXIOMS)}")

    src = data.get("canonical_source")
    if src and not os.path.exists(os.path.join(ROOT, src)):
        errors.append(f"{rel}: canonical_source {src!r} does not resolve")

    if kind == "canon":
        words = len(text.split())
        if words > CANON_WORD_CAP:
            errors.append(f"{rel}: canon file is {words} words, over the {CANON_WORD_CAP} cap. "
                          f"Move an argument to the file that owns it rather than raising the cap")

    # The title should match the H1 so a generated index cannot drift from the page.
    body = text[text.find("\n---\n") + 5:]
    h1 = next((l[2:].strip() for l in body.splitlines() if l.startswith("# ")), None)
    if h1 and data.get("title") and h1 != data["title"]:
        errors.append(f"{rel}: title {data['title']!r} does not match H1 {h1!r}")
    return errors


def check_version_parity(docs):
    """CLAUDE.md requires the Constitution version and the README footer to move
    together. Nothing enforced it before this check."""
    const = docs.get("theory/canon/constitution.md", {}).get("version")
    if not const:
        return ["theory/canon/constitution.md: no version in frontmatter"]
    readme = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read()
    m = re.search(r"\*\*Version:\*\*\s*([0-9.]+)", readme)
    if not m:
        return ["README.md: no version footer found"]
    if m.group(1) != const:
        return [f"README.md version footer is {m.group(1)} but the Constitution is {const}; "
                f"CLAUDE.md requires them to move together"]
    return []


def canon_warnings(path, rel, data):
    """Not errors. A canon file carrying a parameter table is the drift the
    contract exists to catch, but the heuristic is narrow and can be wrong, so
    it reports and does not fail. Calibration is the home for a default."""
    if data.get("kind") != "canon":
        return []
    out = []
    for i, line in enumerate(open(path, encoding="utf-8").read().splitlines(), start=1):
        if line.startswith("|") and re.search(r"\|\s*(Default|Range)\s*\|", line):
            out.append(f"{rel}:{i}: canon file has a parameter table column "
                       f"({line.strip()[:60]}...). Defaults belong in theory/reference/calibration.md")
    return out


def main():
    errors, warnings, docs = [], [], {}
    for base in SCOPE:
        for root, dirs, files in os.walk(os.path.join(ROOT, base)):
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
            for f in sorted(files):
                if not f.endswith(".md"):
                    continue
                path = os.path.join(root, f)
                rel = os.path.relpath(path, ROOT)
                errors.extend(check_file(path, rel))
                data, _ = parse_frontmatter(open(path, encoding="utf-8").read(), rel)
                docs[rel] = data or {}
                warnings.extend(canon_warnings(path, rel, docs[rel]))
    errors.extend(check_version_parity(docs))

    print("=" * 60)
    print(f"Frontmatter validator: {len(docs)} files in {', '.join(SCOPE)}")
    print("=" * 60)
    for w in warnings:
        print(f"   ? {w}")
    if errors:
        for e in errors:
            print(f"   - {e}")
        print(f"\n{len(errors)} error(s)")
        sys.exit(1)
    print("All frontmatter valid, and the Constitution and README versions agree.")
    if warnings:
        print(f"{len(warnings)} warning(s), which do not fail the check.")
    sys.exit(0)


if __name__ == "__main__":
    main()
