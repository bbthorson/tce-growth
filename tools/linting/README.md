# Linting

**Automated enforcement of the repo's content conventions.** Two independent checkers cover different failure classes. Run both before opening a PR.

Parent: [tools/](../) · Rules they enforce: [voice-guide.md](../../publishing/02-tools/voice-guide.md) and [CLAUDE.md](../../CLAUDE.md)

## check_frontmatter.py

Validates the YAML frontmatter block on every document in `theory/` and `practice/`. No dependencies. `publishing/` is out of scope on purpose: the style references are verbatim records of what was published, which is the same reason `.vale.ini` exempts them.

It checks six things:

| Check | Why it exists |
|---|---|
| `title` matches the H1 | So a generated index cannot drift from the page it indexes. The old field-asset README drifted exactly this way. |
| `layer` matches the directory | Catches a file moved between groups without its metadata following. |
| `status` is one of active, under-review, superseded | `under-review` is real: it marks a rule still in force whose replacement is being argued. |
| `operationalizes` names real axioms | Makes the theory-to-practice trace machine-readable. Revising an axiom can now list every document claiming to derive from it. |
| `canonical_source` resolves | A dead pointer to a canonical home is worse than none. |
| Constitution version equals the root README footer | CLAUDE.md has required these to move together since v13. Nothing enforced it until now, and it was done by hand. |

The YAML parser is deliberately small. It handles the flat key/value and inline-list shapes this repo uses and rejects anything else rather than guessing, so a malformed block fails loudly instead of parsing into something surprising.

## The two checkers

| Checker | Catches | Needs installing |
|---|---|---|
| `check_playbook.py` | Broken relative links, malformed LaTeX delimiters | No. Python 3, no dependencies. |
| Vale + the `TCG` style | Banned vocabulary, emojis, punctuation density, retired terms | Yes. See below. |

### check_playbook.py

Walks every `.md` file outside `.git`, `.claude`, `node_modules`, and `.gemini`. Reports two error classes and exits non-zero if either fires.

```bash
python3 tools/linting/check_playbook.py
```

1. **LaTeX integrity.** Unclosed inline or block math delimiters, and delimiters nested inside each other. The script knows the difference between math and a dollar sign, so currency amounts and template placeholders are not treated as opening a math block.
2. **Link validity.** Every relative link resolves to a file that exists. Web URLs, `mailto:`, and `#` anchors are skipped.

> [!NOTE]
> The script scans raw text and does not skip fenced code blocks. A math delimiter or a relative link inside an example will be validated as though it were real. Describe such examples in prose, or point them at a path that actually resolves from the file you are editing.

### Vale

```bash
brew install vale
vale .
```

Configuration lives in [`.vale.ini`](../../.vale.ini) at the repo root, which points `StylesPath` here and applies the `TCG` style to all `*.md`. `MinAlertLevel` is `warning`, so warnings surface alongside errors.

## The TCG style rules

| Rule | Level | Enforces |
|---|---|---|
<!-- vale TCG.AntiHype = NO -->
| [`AntiHype.yml`](./styles/TCG/AntiHype.yml) | error | The banned-word list (*synergy*, *revolutionize*, *disruptive*, *cutting-edge*, *seamlessly*, *unlock potential*). Case-insensitive. |
| [`NoEmoji.yml`](./styles/TCG/NoEmoji.yml) | error | No emoji anywhere, across nine Unicode ranges including the variation selector. |
| [`Punctuation.yml`](./styles/TCG/Punctuation.yml) | warning | At most 3 em dashes plus semicolons combined. Applies to prose written for publication. |
| [`PunctuationReference.yml`](./styles/TCG/PunctuationReference.yml) | warning | At most 30, for reference and operational material. The repo-wide default. |
| [`RetiredTerms.yml`](./styles/TCG/RetiredTerms.yml) | error | Vocabulary the framework has replaced. Reports the current term to use. |
<!-- vale TCG.AntiHype = YES -->

This file quotes retired terms and banned words in order to document them, so it fences the relevant blocks with the mechanism described under [naming a retired term on purpose](#naming-a-retired-term-on-purpose). Read the raw source to see the fences.

### Why RetiredTerms exists

The link checker validates hrefs. It cannot see the prose around them. In August 2026 the repo carried 40 references to retired vocabulary, and every one of them sat inside a *correctly resolving* link:

<!-- vale TCG.RetiredTerms = NO -->
```markdown
[TCG Constitution - Axiom III (Law of Friction)](../../theory/canon/constitution.md)
```

The href was right. The name had been retired two Constitution versions earlier. Same pattern for directory numbering: link text said `04-internal-ops/` while the href pointed at the real `02-internal-ops/`. Both classes are invisible to a link checker and to a reader who trusts the link. `RetiredTerms.yml` is the rule that sees them.
<!-- vale TCG.RetiredTerms = YES -->

Neither class shows up in a `git diff` review either, because each one was correct when it was written.

### Adding a retired term

Whenever you rename an axiom, retire an equation variable, or renumber a directory, add a row to `swap:` in [`RetiredTerms.yml`](./styles/TCG/RetiredTerms.yml) **in the same commit as the rename**. That is the whole maintenance ritual.

<!-- vale TCG.RetiredTerms = NO -->
```yaml
swap:
  Law of Friction: Law of Uncertainty Inflation
```
<!-- vale TCG.RetiredTerms = YES -->

Keys are regexes and the match is case-sensitive. The `message` template fills `%s` with the retired term and then the replacement, so the fix is in the error output and nobody has to go looking for it.

### Building the list from history, not from the working tree

A rule built by scanning the current repo only catches drift that happens to still be visible. Names purged before the rule existed leave no trace in the tree, and they come back the moment someone reopens an old branch. Mine the history instead:

```bash
git log -p --all --format="" -- '*.md' | grep -oE 'Law of [A-Z][a-zA-Z]*( [A-Z][a-zA-Z]*)*' | sort | uniq -c | sort -rn
```

Adapt the pattern to whatever is being renamed. Read every hit before adding it, because the pattern will also catch legitimate prose. "Law of Conservation" appears in a published style reference as Tesler's Law and is not a retired axiom, so it stays out of the rule.

### Naming a retired term on purpose

Version-history notes sometimes need to name the old term. Fence the passage:

```markdown
<!-- vale TCG.RetiredTerms = NO -->
Renamed in v12 from the previous axiom name.
<!-- vale TCG.RetiredTerms = YES -->
```

The same form works for any rule in the table, for example `<!-- vale TCG.AntiHype = NO -->`.

Prefer this over deleting the row. An unenforced rule catches nothing.

## Pre-commit hook

A ready-to-use pre-commit hook is provided in [`.githooks/pre-commit`](../../.githooks/pre-commit). It runs `check_playbook.py` and `vale .` automatically before every commit.

To activate it for your local clone:

```bash
git config core.hooksPath .githooks
```

## Current state of the repo

Both checkers pass cleanly across all files in the repository:

| Rule | State |
|---|---|
| `check_playbook.py` | Clean. Zero broken links or LaTeX errors across 78 scanned markdown files. |
| `RetiredTerms` | Clean. Zero hits repo-wide. Covers retired axioms, old directory numbers, and retired deal analogies ("Bridge" / "Toaster" -> Structural / Turnkey). |
| `NoEmoji` | Clean. |
| `AntiHype` | Clean, with documented suppressions in style-references and self-documenting files. |
| `Punctuation` / `PunctuationReference` | Clean. |

### The three AntiHype suppressions

Two are self-referential: [`CLAUDE.md`](../../CLAUDE.md) and [`voice-guide.md`](../../publishing/02-tools/voice-guide.md) have to print the banned-word list in order to document it, so both are fenced. This README's own rule table is fenced for the same reason.

The third is a scope exclusion in `.vale.ini` for `publishing/02-tools/style-references/`. Those files are published posts kept verbatim as a record of what went out, and two of them predate the anti-hype list. Editing published text to satisfy a later rule would make this repo disagree with what readers can actually see.

The cost of that exclusion is real: a future post moved into `style-references/` carries its hype language in unchecked. The check that matters happens while authoring the piece.

### Why there are two punctuation rules

Vale's `occurrence` rule counts absolute instances and cannot be parameterized per directory, so a 480-line Constitution was held to the same budget as a 20-line LinkedIn post. Measuring the repo showed the limit of 3 was calibrated for short-form posts, where it still works: those files sit at a median of 3. It had simply been applied to everything.

Reference and operational material now carries a budget of 30 and is the repo-wide default. Prose written for publication opts back into 3, in `.vale.ini`:

- `publishing/02-tools/style-references/`

The limit of 30 was chosen so that all of `theory/` passes (the Constitution is the ceiling at 29) while genuine outliers still report. A limit set so nothing ever fires is not a relaxed rule, it is a deleted one.

**Do not raise either limit further to silence a warning.** Both encode house style. If a document legitimately needs more, that is a conversation about the document.

## Known limitations

- **Neither checker validates claims against the Constitution.** They catch stale vocabulary, not stale reasoning. A description can use every current term and still describe a superseded version of an axiom, which is what happened to the root README's axiom list. That still needs a human reading both files side by side.
- **`Punctuation.yml` counts per file, not per section.** A long document at the limit will flag on the next legitimate em dash. Restructure into periods rather than raising the limit.

