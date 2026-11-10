---
title: "Practice"
layer: practice
status: active
---

# Practice

**Function:** operationalize the theory. Every file here is an instrument one of the three axioms names, or a measurement tool whose worked example the model tests assert. A section stays only if it passes three questions: it changes a decision the person using the instrument makes, it is said in one place, and the person can act on it when they use the instrument. Nothing here is operating procedure for a sales organization. That material was removed in the 2026-09 restructure, and the version history in the [Constitution](../theory/01-foundation/00-tcg-constitution.md) records what went.

Each document carries its own header table stating its inputs, outputs, next step, and owner. This README points at them and does not restate them.

---

## By decision

The Constitution's axioms answer three questions: whether a market can exist, what has to be paid down at Time1, and what prevents churn and contraction at Time2. The instruments meet those questions at different moments. Name the question, then open the instrument.

| Moment | Your question | Instrument |
|---|---|---|
| **Before any buyer** | Where does the sale start across this buyer population, and are we built to pay down that cost? | [00. The Market Reading](./00-market-reading.md) |
| **Deal** | Can this buyer enter, where does the sale start and what must the seller's spending do, and what must be settled before anything specific is sunk? | [Deal Triage Calculator](./deal-triage-calculator.md) |
| **Deal, a coalition** | Whose measure does this change, what does each role need answered, and who inside the buyer holds the decision together? | [Bargaining Ledger](./bargaining-ledger.md) |
| **Deal, specific exposure** | What does each side not know about the other, how does this fail, and who commits what before anything is sunk? | [Enforcement Ledger](./enforcement-ledger.md): Map, Test and Stage |
| **Deal, after signature** | Did value land, and have we re-earned the renewal? | [Sustaining Adoption Review](./adoption-review.md) |

Every instrument here is built from [08-from-axioms-to-instruments.md](../theory/01-foundation/08-from-axioms-to-instruments.md) for Constitution 6.1. The Enforcement Ledger replaces the Blueprint, Red Team and Mutual Implementation Plan, which are now its three stages, and the Adoption Review runs the Maintain stage of both deal ledgers after signature, with the standing review agreed in Stage. The Deal Triage Calculator decides where the sale starts. Search runs on the Market Reading's search ledger, bargaining on the Bargaining Ledger, and implementation on the Enforcement Ledger.

---

## Quantitative instruments

Two instruments convert deal observations into comparable numbers, each a quantity the axioms name. Each ranks deals against each other, and none predicts a close date. Every parameter they use is declared in [06-calibration.md](../theory/01-foundation/06-calibration.md), and every worked example is asserted in [`models/`](../models/).

| Instrument | Measures | Run it when |
|---|---|---|
| [Enforcement Ledger](./enforcement-ledger.md) | The policing gap, the mean of the seller's and the buyer's unevidenced fractions, which feeds the chance of future loss. Its allocation coverage reads whether specific investment was allocated before it was sunk. | At each stage, from Map onward, and coverage at go-live |
| [Bargaining Ledger](./bargaining-ledger.md) | The bargaining gap, and $F_{consensus}$ with its band | Whenever the triage reads bargaining as needing investment, and on every deal with specific exposure |

---

## The signal check

[The Friction Allocation Diagnostic](./friction-allocation-diagnostic.md) decides whether one piece of evidence counts, against the four Friction Allocation Principles. The Enforcement Ledger's Test rows and the Market Reading's search ledger run every evidence cell through it.

---

## Archived in the 6.1 rebuild

Each file below is in git history. What it carried that the axioms still need now lives here:

| Archived | Now in |
|---|---|
| Contextual Blueprint, Red Team Protocol, Mutual Implementation Plan, Milestone Valuation Model, Bilateral Asymmetry Scorecard | The [Enforcement Ledger](./enforcement-ledger.md)'s Map, Test and Stage, and its policing gap |
| Consensus Friction Calculator, and the Blueprint's and Red Team's stakeholder sections | The [Bargaining Ledger](./bargaining-ledger.md) |
| Friction Efficiency Index | Its allocation coverage ratio, in the Enforcement Ledger, and its test of Axiom III's allocation clause, in [06-calibration.md](../theory/01-foundation/06-calibration.md) section 4. The other three measures and the composite changed no decision on a deal. |
| CFIR Field Mapping | [cfir.md](../theory/02-research/cfir.md), section "Where each construct is read" |

---

## Related

- **Theory:** [00-tcg-constitution.md](../theory/01-foundation/00-tcg-constitution.md) for the axioms, [01-motions.md](../theory/01-foundation/01-motions.md) for why where the sale starts selects the instrument, [05-governance-forms.md](../theory/01-foundation/05-governance-forms.md) for what shape the arrangement takes after signature.
- **Checks:** [`tools/linting/`](../tools/linting/) for the link, frontmatter and style checkers.
