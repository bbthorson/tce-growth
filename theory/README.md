---
title: "Theory"
layer: theory
kind: reference
status: active
---

# Theory

**Function:** develop and pressure-test the TCG framework. This is where the ideas live before they get operationalized in [`practice/`](../practice/) or published in [`publishing/`](../publishing/).

## How this directory is organized

**By document contract, not by topic.** What a file promises a reader decides how long it may be and what it may contain, and the directory it sits in declares that promise. This is the rule that keeps a claim from acquiring a second home, which is how the framework reached 99,000 words the first time.

| Directory | Promises | Rule it lives under |
|---|---|---|
| [`canon/`](./canon/) | The claims, and only the claims | One statement, one mechanism, one falsifier, one pointer. No derivations, no worked examples, no parameter defaults. Word-capped. |
| [`reference/`](./reference/) | Exhaustive lookup | Never read front to back, so length does not matter. States, and does not argue. |
| [`arguments/`](./arguments/) | Extensions that stand on their own | Downstream of canon, explicitly not part of it, free to be wrong on their own terms. |
| [`evidence/`](./evidence/) | Where a claim came from | Sources, abstracts, and what each one backs. No synthesis, and no number without a provenance row. |

`check_frontmatter.py` enforces the first two columns: every file declares a `kind`, it must match its directory, and a `canon` file over the word cap fails. It also reports when a canon file grows a parameter table, which belongs in the calibration layer.

## Reading order

Two files are the framework. Everything else is looked up, argued separately, or cited.

1. **[canon/constitution.md](./canon/constitution.md)** — three standing assumptions, the three axioms stated at the level where a seller meets them, the derivations table, and the Surplus equation. Part II names every derivation and the file that argues it. Everything in the repo traces here.
2. **[canon/motions.md](./canon/motions.md)** — motion selection derived from the direction and length of the three-component cost vector, the four regions and what each deploys, and the map onto Product-Led, Sales-Led and the rest of the incumbent vocabulary.

Then, as needed:

| File | What it is for |
|---|---|
| [reference/models.md](./reference/models.md) | Functional forms behind every variable the Constitution names, and the derivation reconciling the two cost representations. |
| [reference/notation.md](./reference/notation.md) | Every symbol and term, with where each is canonically defined. The notation index is itself canonical. |
| [reference/calibration.md](./reference/calibration.md) | Every coefficient, threshold and band, with an honest provenance status. Nothing in it is measured. Read it before quoting any number outside this repository. |
| [reference/open-questions.md](./reference/open-questions.md) | The single register of where the theory is under-developed, grouped by the axiom each gap weakens. Read it before extending the theory, so the extension lands on a recorded gap or adds one. |
| [arguments/seller-surplus.md](./arguments/seller-surplus.md) | The seller's side of the transaction: what the seller spends before signature, what portion is exposed, and when the spend is worth making. |
| [arguments/governance-forms.md](./arguments/governance-forms.md) | What shape the arrangement takes after signature. Adds frequency as Axiom II's second selector and derives Williamson's four forms from level and frequency. |

## [evidence/](./evidence/)

The academic backing for each axiom, plus the provenance audit that makes any quantitative claim traceable. Start with [reading-guide.md](./evidence/reading-guide.md), which owns the reading order, says which axiom each paper backs, and carries the scope boundary for the whole directory.

[citation-provenance-audit.md](./evidence/citation-provenance-audit.md) is the provenance table for every headline statistic: the claim, its primary source, and a verification status. Check a statistic's status there before quoting it anywhere outside this repository.

## What goes here vs. elsewhere

| Type of content | Where it lives |
|---|---|
| Axioms, equations, the theory's own claims | **this directory** |
| Instruments and artifacts | [`../practice/`](../practice/) |
| Public writing, cases, style references | [`../publishing/`](../publishing/) |
| Executable forms of the equations and their tests | [`../models/`](../models/) |

If a concept is invoked in two or more directories, its canonical definition lives here, and [reference/notation.md](./reference/notation.md) says which file holds it.
