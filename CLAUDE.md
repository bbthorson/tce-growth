# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A knowledge base for **Transaction Cost Growth (TCG)** — a theory of go-to-market built on transaction cost economics, holding that what a deal costs a buyer beyond the price determines how it can be sold. Search-led, consensus-led and implementation-led are motions inside it rather than rivals to it, each named after the cost the sale starts at, and Turnkey is the market condition where every cost is low enough for the buyer to pay down alone. `theory/01-foundation/01-motions.md` maps them onto the incumbent PLG and SLG vocabulary. Almost all content is Markdown. The repo is organized into five directories:

| Directory | Function |
|---|---|
| `theory/` | Develop and pressure-test the TCG framework. Axioms, equations, academic backing. |
| `practice/` | Operationalize theory. The instruments the axioms name and the measurement tools the tests assert. |
| `publishing/` | Turn the framework into public writing. Voice guide, content generators, case analyses. |
| `models/` | Executable forms of the equations, the tests that check the worked examples, and the figure generator. Python, no dependencies. |
| `tools/` | The two linters and the Vale style that keep the other directories consistent. |

## Conceptual architecture

**The canonical source of truth is `theory/01-foundation/00-tcg-constitution.md`** — three standing assumptions and three axioms from which all other concepts derive. Since version 4.0 each axiom answers one decision, in time order, in one sentence, with a falsifier:

- **I, Composition. Should I use the market?** Using it costs the buyer three things beyond price: search and information, bargaining and decision, policing and enforcement. Any one can keep the buyer out, and the sale starts at the cost nearest its own threshold.
- **II, Transaction Investment. What will it cost me today?** Each cost is paid down by the buyer, the seller or both, and each party goes ahead only when its own share is covered by its own return.
- **III, Future Cost. What might it cost me later?** Whatever a party sinks that is worth less outside the relationship exposes it to what it cannot verify, and who carries that has to be settled before the investment is sunk. Specificity, the gate, and the governance forms live here.

Everything in `practice/` and `publishing/` traces back to it.

The dependency chain runs one way: `theory/` → `practice/` → `publishing/`. Changes to theory should propagate downstream. Changes to practice or publishing never modify theory.

Key cross-file dependencies to know:
- The **Deal Triage Calculator** (`practice/deal-triage-calculator.md`) operationalizes Axiom I's thresholds and Axiom III's specific exposure: it emits each cost's position and zone, where the sale starts, and an exposure reading, not a motion label. It never sums the costs. It is referenced by nearly every field asset.
- The **CFIR field mapping** (`practice/cfir-field-mapping.md`) explains which research construct each artifact section operationalizes — read it before modifying any `practice/` document.
- The **Friction Allocation Diagnostic** (`practice/friction-allocation-diagnostic.md`) operationalizes the four Friction Allocation Principles from Axiom III.
- The **three implementation artifacts** (Blueprint → Red Team → MIP) in `practice/implementation-motion/` run sequentially; each artifact gates the next. They are the implementation component's instruments. The directory keeps the motion's name because the motion keeps its name.

The **research files** in `theory/02-research/` back specific axioms:
- Axiom I (Composition) → `transaction-cost-economics.md`, `buying-center-dynamics.md`, `channel-collapse.md`, `fear-of-failure.md`, `integration-touchpoints.md`
- Axiom II (Investment) → `transaction-cost-economics.md`, `integration-touchpoints.md`, `process-misfit.md`
- Axiom III (Future Cost) → `transaction-cost-economics.md`, `klein-crawford-alchian.md`, `incomplete-contracts.md`, `process-misfit.md`, `game-theory-and-nrr.md`, `real-options.md`, `costly-signals.md`, `prospect-theory.md`, `fear-of-failure.md`, `cfir.md`, `re-aim-framework.md`, `tce-empirical-record.md`

Start with `theory/02-research/00-reading-guide.md` before modifying any research file. Before extending the theory, read `theory/01-foundation/07-open-questions.md`, which records where it is under-developed by axiom; an extension should land on a recorded gap or add one.

<!-- vale TCG.RetiredTerms = NO -->
**The motion is where the sale starts.** `theory/01-foundation/01-motions.md` carries the derivation and its section 9 records what it leaves unsettled. The retired readings are worth knowing because they still appear in older analyses and in git history:
- The friction vector's direction and length, the summed 0-to-30 level, and the Structural deal class went in Constitution 4.0.
- The per-component multiplier, the reduced form $y = a\hat{\Delta}^2 + c$ and its coefficient 2.25 went at the same time.
- The Nascent, Efficient, Saturated, Transitional and Mature market states went earlier.

`RetiredTerms.yml` catches the retired axiom names, the instrument's old name, Structural and seat. It does not catch the market states, because those were never load-bearing outside the two files that carried them. `AXIOM-REVISION-PROPOSAL.md` in git history records why 4.0 happened.
<!-- vale TCG.RetiredTerms = YES -->

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

- **Component names**: Dahlman's names, *search and information*, *bargaining and decision* and *policing and enforcement*, are canonical in theory prose. *Search*, *consensus* and *implementation* are the field names and the notation subscripts (`F_consensus`, `F_implementation`). Introduce the field name at first use in a theory file, and do not retire either. A position in the buyer's coalition is a *decision role*, and `RetiredTerms.yml` flags the old word.
- **Translate every technical term** immediately after first use — never drop "Asset Specificity" or "Single Crossing Property" without a plain-English follow-up.
<!-- vale TCG.AntiHype = NO -->
- **Anti-hype vocabulary**: banned words include *synergy*, *revolutionize*, *disruptive*, *cutting-edge*, *seamlessly*, *unlock potential*. See voice guide for replacements.
<!-- vale TCG.AntiHype = YES -->
- **Em dashes and semicolons**: at most 30 per file for reference and operational material, which is the repo-wide default, and at most 3 for prose written for publication. `.vale.ini` sets which rule applies where. Restructure into periods rather than raising either limit.
- **Anti-antithesis filter**: avoid "It's not X, it's Y" constructions.
- **Active voice**: name actors. "HTD will map the workflow" over "the workflow will be mapped."
- **No emojis.**
- The Constitution is **axioms-first**: if a claim cannot be traced to one of the three axioms, it does not belong in `theory/01-foundation/00-tcg-constitution.md`. Operational content belongs in `practice/`.
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

## How documents relate to the two conditions

All framework claims trace to two conditions, one per party, and a participation test:

$$S_b = V_{switch}(t) - P - \sum_k I^b_k - L_b > 0 \qquad S_s = P - C_{deliver} - \sum_k I^s_k - L_s > 0 \qquad r_k \le 1 \;\; \forall k$$

- **All terms are fractions of annual contract value**, per `02-mathematical-models.md` section 1.2. Reading them as percentage points is a unit error.
- **$V_{switch}(t)$** = $V_{solution} e^{-\delta t} - V_{next\_best}$, the buyer's opportunity cost of staying put.
- **$P$** = price. It cancels when the two conditions are added, because price is a transfer and not a transaction cost. That is the whole argument for verification over discounting: a discount moves the split, and verification lowers a loss both sides carry.
- **$I^b_k$, $I^s_k$** = what each party invests today against cost $k$ (Axiom II). Moving investment between parties changes the joint surplus only when the party taking it on is cheaper or the move lowers a future loss.
- **$L_p = Q_p \cdot \pi_p$** = each party's expected future loss (Axiom III): its quasi-rent times the chance it does not come back. $\pi_p$ rises with the gaps party $p$ cannot close. The gaps are normalized to $[0, 1]$ and never multiply a cost. The Asymmetry Scorecard emits a raw implementation gap on $[2, 10]$, so normalize first, per section 2.5. `models/tcg_models.py` refuses a raw value at the type level.
- **$r_k$** = cost $k$'s position between its own self-serve and participation thresholds (Axiom I). Above 1 the buyer stays out. The sale starts at the largest. The costs are never summed.
- **Exposure** = the Deal Triage Calculator's reading of whether the deal sinks anything specific. With frequency it selects the governance form.

When diagnosing a stall or editing a prescription, identify which term it addresses.

### Changing an equation or a coefficient

Every live formula has an implementation in [`models/tcg_models.py`](./models/tcg_models.py), and every worked example in `theory/` and `practice/` is asserted against it. **The document is the specification: where the two disagree, the code is the bug.** So the order is fixed.

1. Edit the document first. The test then fails against the old code, which is the point of having it.
2. Update `tcg_models.py` and rerun `python3 models/test_tcg_models.py`.
3. Rerun `python3 models/make_figures.py` if the change touches a curve the Constitution plots. The Constitution's figures are sampled from the module, so a retuned coefficient moves the picture instead of leaving it quietly asserting the old value.
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
