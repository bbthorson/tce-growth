# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A knowledge base for **Transaction Cost Growth (TCG)**, a theory of go-to-market built on transaction cost economics: what a deal costs a buyer beyond the price determines how it can be sold. Search-led, consensus-led and implementation-led are motions inside it, each named after the cost the sale starts at. Turnkey is the market condition where every cost is low enough for the buyer to pay down alone. `theory/01-foundation/01-motions.md` maps them onto PLG and SLG. Almost all content is Markdown.

| Directory | Function |
|---|---|
| `theory/` | Develop and pressure-test the framework. Axioms, equations, academic backing. |
| `practice/` | Operationalize theory. The instruments the axioms name and the measurement tools the tests assert. |
| `publishing/` | Turn the framework into public writing. Voice guide, writing protocols, content generators. |
| `models/` | Executable forms of the equations, the tests that check the worked examples, and the figure generator. Python, no dependencies. |
| `tools/` | The two linters and the Vale style that keep the other directories consistent. |

## Conceptual architecture

**The source of truth is `theory/01-foundation/00-tcg-constitution.md`**: three standing assumptions and three axioms. Each axiom answers one decision, in time order, with a falsifier:

- **I, Composition. Should I use the market?** Using it costs the buyer three things beyond price: search and information, bargaining and decision, policing and enforcement. Any one can keep the buyer out, and the sale starts at the cost nearest its own threshold.
- **II, Transaction Investment. What will it cost me today?** Each cost is paid down by the buyer, the seller or both, and each party goes ahead only when its own share is covered by its own return.
- **III, Future Cost. What might it cost me later?** Whatever a party sinks that is worth less outside the relationship exposes it to what it cannot verify, and who carries that has to be settled before the investment is sunk. Specificity, the gate, and the governance forms live here.

The dependency chain runs one way: `theory/` → `practice/` → `publishing/`. Changes to theory propagate downstream. Changes to practice or publishing never modify theory.

Read before editing:
- **Any `practice/` file**: `practice/cfir-field-mapping.md`, which says which research construct each section operationalizes. The Deal Triage Calculator (`practice/deal-triage-calculator.md`) is referenced by nearly every instrument. It emits each cost's position and zone, where the sale starts, and an exposure reading, and it never sums the costs.
- **Any research file**: `theory/02-research/00-reading-guide.md`, which maps each paper to the axiom it backs.
- **Before extending the theory**: `theory/01-foundation/07-open-questions.md`. An extension should land on a recorded gap or add one.

<!-- vale TCG.RetiredTerms = NO -->
Older analyses and git history use readings Constitution 4.0 retired: the friction vector, the summed 0-to-30 level, the Structural deal class, the coefficient 2.25, and the market states. `01-motions.md` and the Constitution's version history record what replaced them.
<!-- vale TCG.RetiredTerms = YES -->

## The two conditions

All framework claims trace to two conditions, one per party, and a participation test:

$$S_b = V_{switch}(t) - P - \sum_k I^b_k - L_b > 0 \qquad S_s = P - C_{deliver} - \sum_k I^s_k - L_s > 0 \qquad r_k \le 1 \;\; \forall k$$

- **All terms are fractions of annual contract value** (`02-mathematical-models.md` section 1.2), not percentage points.
- **$P$** is a transfer, so it cancels when the conditions are added. A discount moves the split. Verification lowers a loss both sides carry.
- **$I^b_k$, $I^s_k$** = what each party invests today against cost $k$ (Axiom II).
- **$L_p = Q_p \cdot \pi_p$** = each party's expected future loss (Axiom III). The gaps behind $\pi_p$ are normalized to $[0, 1]$. The Asymmetry Scorecard emits a raw gap on $[2, 10]$, so normalize first.
- **$r_k$** = cost $k$'s position between its self-serve and participation thresholds (Axiom I). Above 1 the buyer stays out. The sale starts at the largest. The costs are never summed.

When diagnosing a stall or editing a prescription, identify which term it addresses.

## Content conventions

Apply the voice rules in `publishing/02-tools/voice-guide.md`. Vale enforces most of them.

- **Component names**: Dahlman's names are canonical in theory prose. *Search*, *consensus* and *implementation* are the field names and the notation subscripts. Introduce the field name at first use in a theory file. A position in the buyer's coalition is a *decision role*.
- **Translate every technical term** in plain English right after first use.
- **Em dashes and semicolons**: at most 30 per file for reference material, 3 for prose written for publication. Restructure into periods rather than raising either limit.
- **Active voice with named actors.** No "It's not X, it's Y" constructions. No hype words, no emojis.
- **The Constitution is axioms-first.** A claim that cannot be traced to an axiom does not belong in it. Operational content belongs in `practice/`.
- **Frontmatter**: every file in `theory/` and `practice/` opens with `title` (matching the H1), `layer`, `status`, optional `version`, `operationalizes` and `canonical_source`. `check_frontmatter.py` enforces the schema. `grep -rl "axiom-1" theory/ practice/` lists everything that claims to derive from an axiom.

## Drift rules

Each of these has a check behind it. Do the step in the same commit as the change.

- **New headline statistic in `theory/`**: add a row to `theory/02-research/audits/citation-provenance-audit.md` with an honest verification status. When two files disagree on a number, record it there first, then fix both against the primary source.
- **New coefficient, threshold or band edge**: declare it in `theory/01-foundation/06-calibration.md` with its provenance. Every parameter is unfitted and must say so. Do not fit to synthetic data. The test suite fails on an undeclared constant.
- **Changing an equation**: the document is the specification and the code is the bug. Edit the document, then `models/tcg_models.py`, then rerun `make_figures.py` if the Constitution plots it, then fix any worked example whose result moved. `models/README.md` has the detail.
- **Renaming anything canonical**: grep the whole repo for the old term, add it to `swap:` in `tools/linting/styles/TCG/RetiredTerms.yml`, and bump the Constitution version and the root README footer together. Then check descriptions, not just names: a paragraph can use every current term and still describe a superseded axiom. `tools/linting/README.md` has the detail.

## Checking your work

Run all five before finishing an edit:

```bash
python3 tools/linting/check_playbook.py && \
python3 tools/linting/check_frontmatter.py && \
python3 models/test_tcg_models.py && \
python3 models/make_figures.py --check && vale .
```

They also run in `.githooks/pre-commit`, which is active only after `git config core.hooksPath .githooks`.

## Publishing workflow

```
publishing/README.md (content pillars) → voice-guide.md → writing-protocols.md (context check) → {long-form | short-form}-generator.md → style-references/
```

`writing-protocols.md` also holds the AI persona for deal-analysis writing and the trenches protocol for analyzing a specific deal. Style references are published text kept verbatim, so Vale exempts them.
