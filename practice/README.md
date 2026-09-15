---
title: "Practice"
layer: practice
status: active
---

# Practice

**Function:** operationalize the theory. Every file here is an instrument one of the three axioms names, or a measurement tool whose worked example the model tests assert. Nothing here is operating procedure for a sales organization. That material was removed in the 2026-09 restructure, and the version history in the [Constitution](../theory/01-foundation/00-tcg-constitution.md) records what went.

Each document carries its own header table stating its inputs, outputs, next step, and owner. This README points at them and does not restate them.

---

## By level

The three levels are the Constitution's index: each axiom is stated at the level where a seller meets it. Name the level, then open the instrument.

| Level | Your question | Instrument |
|---|---|---|
| **Market** | How long is this deal's friction vector, and where does it point? | [Deal Triage Calculator](./deal-triage-calculator.md) |
| **Workflow** | What do I not yet know about their environment, and how specific is the investment? | [01. Contextual Blueprint](./implementation-motion/01-discovery-contextual-blueprint.md) |
| **Deal** | How does this implementation fail? | [02. Red Team Protocol](./implementation-motion/02-validation-red-team-protocol.md) |
| **Deal** | Who commits what, and what happens when a stage fails? | [03. Mutual Implementation Plan](./implementation-motion/03-closing-mutual-implementation-plan.md) |
| **Deal, after signature** | Did value land, and have we re-earned the renewal? | [04. Sustaining Adoption Review](./implementation-motion/04-sustaining-adoption-review.md) |

The four artifacts in [`implementation-motion/`](./implementation-motion/) run in order and each gates the next. They are the implementation component's instruments. The Deal Triage Calculator decides whether the implementation component is what this deal is paying for. The search and consensus regions have no instrument files, and the calculator says so when a deal routes to them.

---

## Quantitative instruments

Four instruments convert deal observations into comparable numbers. Each measures one term in the Surplus equation, each ranks deals against each other, and none predicts a close date. Every parameter they use is declared in [06-calibration.md](../theory/01-foundation/06-calibration.md), and every worked example is asserted in [`models/`](../models/).

| Instrument | Measures | Run it when |
|---|---|---|
| [Bilateral Asymmetry Scorecard](./asymmetry-scorecard.md) | $\Delta_A = I_{seller} + I_{buyer}$, on the implementation pair | Weekly, from first qualification onward |
| [Consensus Friction Calculator](./consensus-friction-calculator.md) | $F_{consensus}$ | After the Blueprint maps the buying committee |
| [Milestone Valuation Model](./milestone-valuation-model.md) | Staged uncertainty decay and gate payment structure | While drafting the MIP timeline and commercial terms |
| [Friction Efficiency Index](./friction-efficiency-index.md) | Whether implementation effort landed before or after signature, across a closed cohort | Quarterly, in retrospect. The one instrument that could falsify Axiom II after the fact. |

---

## Design references

| Document | What it does |
|---|---|
| [CFIR Field Mapping](./cfir-field-mapping.md) | Which research construct each section of each artifact operationalizes. Read it before modifying any artifact here. |
| [Friction Allocation Diagnostic](./friction-allocation-diagnostic.md) | Tests whether a signal mechanism satisfies the four Friction Allocation Principles from Axiom III. Use when designing an artifact or diagnosing a failing signal. |

---

## Related

- **Theory:** [00-tcg-constitution.md](../theory/01-foundation/00-tcg-constitution.md) for the axioms, [01-motions.md](../theory/01-foundation/01-motions.md) for why direction selects the instrument, [05-governance-forms.md](../theory/01-foundation/05-governance-forms.md) for what shape the arrangement takes after signature.
- **Checks:** [`tools/linting/`](../tools/linting/) for the link, frontmatter and style checkers.
