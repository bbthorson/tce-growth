---
title: "Practice"
layer: practice
status: under-review
---

# Practice

> [!NOTE]
> **Being rebuilt for Constitution 6.1.** The [Market Reading](./00-market-reading.md) and the [Deal Triage Calculator](./deal-triage-calculator.md) are rebuilt and active. Every other file derives from Constitution 4.1 and stays as written until its turn. [The practice rebuild proposal](../PRACTICE-REBUILD-PROPOSAL.md) says which files are rebuilt, merged or archived, and in what order.

**Function:** operationalize the theory. Every file here is an instrument one of the three axioms names, or a measurement tool whose worked example the model tests assert. Nothing here is operating procedure for a sales organization. That material was removed in the 2026-09 restructure, and the version history in the [Constitution](../theory/01-foundation/00-tcg-constitution.md) records what went.

Each document carries its own header table stating its inputs, outputs, next step, and owner. This README points at them and does not restate them.

---

## By decision

The Constitution's axioms answer three questions: whether a market can exist, what has to be paid down at time 0, and what prevents churn and contraction at time 1. The instruments meet those questions at different moments. Name the question, then open the instrument.

| Moment | Your question | Instrument |
|---|---|---|
| **Before any buyer** | Where does the sale start across this buyer population, and are we built to pay down that cost? | [00. The Market Reading](./00-market-reading.md) |
| **Deal** | Can this buyer enter, where does the sale start and what must the seller's spending do, and what must be settled before anything specific is sunk? | [Deal Triage Calculator](./deal-triage-calculator.md) |
| **Deal, specific exposure** | What does each side not know about the other, how does this fail, and who commits what before anything is sunk? | [Enforcement Ledger](./enforcement-ledger.md): Map, Test and Stage |
| **Deal, after signature** | Did value land, and have we re-earned the renewal? | [04. Sustaining Adoption Review](./implementation-motion/04-sustaining-adoption-review.md) |

The Market Reading, the Deal Triage Calculator and the Enforcement Ledger are built from [08-from-axioms-to-instruments.md](../theory/01-foundation/08-from-axioms-to-instruments.md) for Constitution 6.1. The Enforcement Ledger replaces the Blueprint, Red Team and Mutual Implementation Plan, which are now its three stages, and the Adoption Review in [`implementation-motion/`](./implementation-motion/) runs after it. The Deal Triage Calculator decides whether the sale starts at the implementation cost. The search and consensus regions have no instrument files, and the calculator says so when a deal routes to them.

---

## Quantitative instruments

Three instruments convert deal observations into comparable numbers. Two measure a quantity the axioms name and the third scores how the motion was run. Each ranks deals against each other, and none predicts a close date. Every parameter they use is declared in [06-calibration.md](../theory/01-foundation/06-calibration.md), and every worked example is asserted in [`models/`](../models/).

| Instrument | Measures | Run it when |
|---|---|---|
| [Enforcement Ledger](./enforcement-ledger.md) | The policing gap, the mean of the seller's and the buyer's unevidenced fractions, which feeds the chance of future loss | At each stage, from Map onward |
| [Consensus Friction Calculator](./consensus-friction-calculator.md) | $F_{consensus}$ | After the buying committee is mapped |
| [Friction Efficiency Index](./friction-efficiency-index.md) | Whether specific investment was allocated before it was sunk, and where the effort went, across a closed cohort | Quarterly, in retrospect. The one instrument that could test Axiom III's allocation clause after the fact. |

---

## Design references

| Document | What it does |
|---|---|
| [CFIR Field Mapping](./cfir-field-mapping.md) | Which research construct each section of each artifact operationalizes. Read it before modifying any artifact here. |
| [Friction Allocation Diagnostic](./friction-allocation-diagnostic.md) | Tests whether a signal mechanism satisfies the four Friction Allocation Principles from Axiom III. Use when designing an artifact or diagnosing a failing signal. |

---

## Related

- **Theory:** [00-tcg-constitution.md](../theory/01-foundation/00-tcg-constitution.md) for the axioms, [01-motions.md](../theory/01-foundation/01-motions.md) for why where the sale starts selects the instrument, [05-governance-forms.md](../theory/01-foundation/05-governance-forms.md) for what shape the arrangement takes after signature.
- **Checks:** [`tools/linting/`](../tools/linting/) for the link, frontmatter and style checkers.
