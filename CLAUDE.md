# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A knowledge base for **Transaction Cost Growth (TCG)** — a theory of go-to-market built on transaction cost economics, holding that what a deal costs a buyer beyond the price determines how it can be sold. Turnkey, search-led, consensus-led and implementation-led are motions inside it rather than rivals to it, each named after the cost it spends to reduce. `theory/01-foundation/01-motions.md` maps them onto the incumbent PLG and SLG vocabulary. Almost all content is Markdown. The repo is organized into four groups, each with its own README:

| Directory | Function |
|---|---|
| `theory/` | Develop and pressure-test the TCG framework. Axioms, equations, academic backing. |
| `practice/` | Operationalize theory. The instruments the axioms name and the measurement tools the tests assert. |
| `publishing/` | Turn the framework into public writing. Voice guide, content generators, case analyses. |
| `models/` | Executable forms of the equations, the tests that check the worked examples, and the figure generator. Python, no dependencies. |
| `tools/` | The two linters and the Vale style that keep the other directories consistent. |

## Conceptual architecture

**The canonical source of truth is `theory/01-foundation/00-tcg-constitution.md`** — three axioms from which all other concepts derive. Everything in `practice/` and `publishing/` traces back to it.

The dependency chain runs one way: `theory/` → `practice/` → `publishing/`. Changes to theory should propagate downstream. Changes to practice or publishing never modify theory.

Key cross-file dependencies to know:
- The **Deal Triage Calculator** (`practice/deal-triage-calculator.md`) operationalizes both of Axiom I's quantities: it emits a level and a direction, not a motion label. It is referenced by nearly every field asset.
- The **CFIR field mapping** (`practice/cfir-field-mapping.md`) explains which research construct each artifact section operationalizes — read it before modifying any `practice/` document.
- The **Friction Allocation Diagnostic** (`practice/friction-allocation-diagnostic.md`) operationalizes the four Friction Allocation Principles from Axiom II.
- The **three implementation artifacts** (Blueprint → Red Team → MIP) in `practice/implementation-motion/` run sequentially; each artifact gates the next. They are the implementation component's instruments. The directory keeps the motion's name because the motion keeps its name.

The **research files** in `theory/02-research/` back specific axioms:
- Axiom I → `transaction-cost-economics.md`
- Axiom II → `costly-signals.md`, `prospect-theory.md`, `fear-of-failure.md`, `cfir.md`
- Axiom III → `game-theory-and-nrr.md`, `re-aim-framework.md`

Start with `theory/02-research/00-reading-guide.md` before modifying any research file.

**A motion is a region, not a list entry.** `theory/01-foundation/01-motions.md` carries the derivation, adopted in Constitution v17.0 as the friction vector and merged with the motion taxonomy and vocabulary in the 2026-09 restructure: motion selection follows from the direction and length of the three-component cost vector, and its section 9 records what it leaves unsettled. The retired names are worth knowing because they still appear in older analyses: Nascent, Efficient, Saturated, Transitional and Mature market states are all gone, along with the reading of a summed score as a motion selector. `RetiredTerms.yml` catches the instrument's old name and the superseded Axiom II description, not the market states, because those were never load-bearing outside the two files that carried them.

## Frontmatter

Every document in `theory/` and `practice/` opens with YAML frontmatter. `publishing/` is out of scope, because the style references are verbatim records of published text and `.vale.ini` already exempts them for that reason.

```yaml
---
title: "The Deal Triage Calculator"   # must match the H1
layer: practice                        # theory | practice, must match the directory
status: active                         # active | under-review | superseded
version: 4.2                           # only where the document tracks one
operationalizes: [axiom-1]             # which axioms it derives from
canonical_source: theory/01-foundation/00-tcg-constitution.md
---
```

`operationalizes` is the field that earns the schema. It makes the theory-to-practice trace machine-readable, so revising an axiom can list every document claiming to derive from it:

```bash
grep -rl "axiom-1" --include=*.md theory/ practice/
```

## Content conventions

When writing or editing any document in this repo, apply the voice rules from `publishing/02-tools/voice-guide.md`:

- **Translate every technical term** immediately after first use — never drop "Asset Specificity" or "Single Crossing Property" without a plain-English follow-up.
<!-- vale TCG.AntiHype = NO -->
- **Anti-hype vocabulary**: banned words include *synergy*, *revolutionize*, *disruptive*, *cutting-edge*, *seamlessly*, *unlock potential*. See voice guide for replacements.
<!-- vale TCG.AntiHype = YES -->
- **Em dashes and semicolons**: at most 30 per file for reference and operational material, which is the repo-wide default, and at most 3 for prose written for publication. `.vale.ini` sets which rule applies where. Restructure into periods rather than raising either limit.
- **Anti-antithesis filter**: avoid "It's not X, it's Y" constructions.
- **Active voice**: name actors. "HTD will map the workflow" over "the workflow will be mapped."
- **No emojis.**
- The Constitution is **axioms-first** (v11+): if a claim cannot be traced to one of the three axioms, it does not belong in `theory/01-foundation/00-tcg-constitution.md`. Operational content belongs in `practice/`.
- **New headline statistics need a provenance row.** Any quantitative claim added to `theory/` gets a row in `theory/02-research/audits/citation-provenance-audit.md` in the same commit, with an honest verification status. When two files disagree on a number, record the discrepancy there first, then fix both against the primary source. This is what stops stat drift, the way `RetiredTerms.yml` stops rename drift.

### Checking your work

Most of the rules above are machine-checked. Run all five before finishing an edit. `tools/linting/README.md` covers the two linters and `models/README.md` covers the two model checks:

```bash
python3 tools/linting/check_playbook.py && \
python3 tools/linting/check_frontmatter.py && \
python3 models/test_tcg_models.py && \
python3 models/make_figures.py --check && vale .
```

`check_playbook.py` needs no dependencies and validates links plus LaTeX delimiters. `check_frontmatter.py` needs none either and validates the frontmatter schema across `theory/` and `practice/`, including that every `operationalizes` entry names a real axiom and that the Constitution version matches the root README footer. `test_tcg_models.py` checks that every worked example in `theory/` and `practice/` still reproduces from [`models/tcg_models.py`](./models/tcg_models.py). `make_figures.py --check` regenerates the Constitution's axiom figures and fails if any has drifted from the equation that generates it. Vale (`brew install vale`) enforces the banned-word list, the emoji ban, the punctuation limit, and retired vocabulary.

All four Python checks run in `.githooks/pre-commit` alongside Vale.

### Renaming anything canonical

The dependency chain runs `theory/` → `practice/` → `publishing/`, and nothing enforces it automatically. When you rename an axiom, retire an equation variable, or renumber a directory:

1. Grep the whole repo for the old term before assuming the rename is local. Stale names hide inside links whose hrefs are still correct, so the link checker will not catch them.
2. Add the old term to `swap:` in `tools/linting/styles/TCG/RetiredTerms.yml` in the same commit. That is what stops the rename from drifting back.
3. Bump the version in `theory/01-foundation/00-tcg-constitution.md` (both the frontmatter and the body) and the matching version footer in the root `README.md` together. `check_frontmatter.py` enforces that they agree.
4. Check the *descriptions*, not just the names. A paragraph can use every current term and still describe a superseded version of an axiom.

## How documents relate to the Fundamental Equation

All framework claims trace to:

$$S = \left(V_{solution} \cdot e^{-\delta t} - V_{next\_best}\right) - \sum_{k} F_k \cdot (1 + \hat{\Delta}_k) = OC_{\text{switching}} - y$$

- **S** = Deal Surplus, which must exceed 0 for the deal to close
- **$\hat{\Delta}_k$** = the gap inside component $k$'s own pair of parties, normalized to $[0, 1]$. Three components, three different pairs, and only the implementation pair is buyer against seller. Per `02-mathematical-models.md` section 2.4.
- **$\hat{\Delta}_A$** = the deal-level gap, which is the friction-weighted mean of the three. The sum above factors into $F_{base}(1 + \hat{\Delta}_A)$ exactly, so both forms are the same quantity. The Asymmetry Scorecard emits a raw score on $[2, 10]$, it measures the implementation pair alone, and **neither cost equation accepts a raw value**. Normalize first, per section 1.5. `models/tcg_models.py` refuses a raw value at the type level.
- **y** = Total Perceived Transaction Cost = $a\hat{\Delta}_A^2 + c$, where $a = 2.25$ is anchored by analogy to loss aversion and $c$ is direct cost. **All three are fractions of annual contract value**, per section 1.7. Reading them as percentage points inverts the argument the equation exists to make.
- **Level** = the Deal Triage Calculator's summed component scores, on base friction, range 0–30. 15 and above is a Structural deal. It sets how much apparatus the deal can carry and discovery does not move it.
- **Direction** = each component's share of *effective* cost, $F_k(1 + \hat{\Delta}_k)$ over the total. It selects the instruments, it moves every time an artifact closes a gap, and the level does not settle it. Axiom I is explicit: do not read the total as a motion selector.

When diagnosing a stall or editing a prescription, identify which term in the equation it addresses.

### Changing an equation or a coefficient

Every live formula has an implementation in [`models/tcg_models.py`](./models/tcg_models.py), and every worked example in `theory/` and `practice/` is asserted against it. **The document is the specification: where the two disagree, the code is the bug.** So the order is fixed.

1. Edit the document first. The test then fails against the old code, which is the point of having it.
2. Update `tcg_models.py` and rerun `python3 models/test_tcg_models.py`.
3. Rerun `python3 models/make_figures.py` if the change touches a curve the Constitution plots. The Constitution's three axiom figures are sampled from the module, so a retuned coefficient moves the picture instead of leaving it quietly asserting the old value.
4. Update the worked example itself if the change moves its result. A worked example that no longer follows from its own formula is the failure this catches.

This is what stops formula drift, the way `RetiredTerms.yml` stops rename drift and the provenance audit stops stat drift.

**Parameters in this repo are unfitted, and every new one must say so.** [`theory/01-foundation/06-calibration.md`](./theory/01-foundation/06-calibration.md) is the single home for every coefficient, threshold and band edge in the framework. Any new one needs a row there with an honest provenance status, in the same commit, and anything that reads as an empirical estimate is wrong. `test_tcg_models.py` asserts that every numeric constant in the module is declared on that page, so adding a constant without declaring it fails the suite.

The separation earns its keep: the theory states structure, the calibration layer states quantity, and a reader can reject any number without rejecting the claim it sits inside. Keep it that way. A coefficient quoted in `theory/` prose without a pointer to the calibration layer is how the two collapse back together. Do not fit these to synthetic data: it produces parameters that look measured and are not. `models/README.md` records why.

## Publishing workflow

New content in `publishing/` follows the multi-phase workflow in the relevant generator file:

```
publishing/README.md (content pillars) → voice-guide.md → writing-protocols.md (context check) → {long-form | short-form}-generator.md → style-references/
```

Case analyses go in `publishing/01-cases/` following the trenches analysis protocol in `publishing/02-tools/writing-protocols.md`. If a case becomes a polished published piece, the final version moves to `publishing/02-tools/style-references/`.

The AI persona config for deal-analysis writing is the first section of the same file.
