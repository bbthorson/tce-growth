# Practice Rebuild Proposal

**Status:** Accepted 2026-11-06, with choices P1 to P4 taken as proposed. Being applied in the section 5 sequence: steps 1 and 2 are done, and the files they retired are named here without links.
**Date:** 2026-11-06

The 5.0 proposal decided that after the axioms settle, the instrument set is derived fresh from them, at the smallest size they require, and whatever is not derived is archived. The [Deal Triage Calculator](./practice/deal-triage-calculator.md) was rebuilt first, as 9.0. This file sorts the other ten practice files against the same test, and against the instrument set [08-from-axioms-to-instruments.md](./theory/01-foundation/08-from-axioms-to-instruments.md) derives. Archived means removed from the tree and kept in git history, with a line in the practice README saying where each part went.

---

## 1. The test

A section of an instrument stays only if it passes all three.

1. **It changes a decision** the person using the instrument makes.
2. **It is said in one place.** Theory explains, and an instrument applies.
3. **The person can act on it when they use the instrument.**

---

## 2. What 08 derives, and what exists

| Derived instrument | 08 | Exists today as |
|---|---|---|
| Market reading | Section 2.1 | [00-market-reading.md](./practice/00-market-reading.md), built from 08 under 5.x |
| Deal reading | Section 2.2 | [deal-triage-calculator.md](./practice/deal-triage-calculator.md) 9.0, done |
| Search ledger: alternatives, the evidence that compares them, the path to the buyer | Section 5, market level | Nothing. The market reading's ledger holds part of it |
| Bargaining ledger: the private decision-role map and the shared arrangement record | Section 5, deal level | Nothing. Pieces sit in the Consensus Friction Calculator, the Blueprint's Stakeholder DNA, and the Red Team's Stakeholder Diagnosis. Open question 2 says it is owed |
| Enforcement ledger: one row per workflow step, a column per verb (Map, Test, Stage, Maintain) | Section 5, deal level | The four implementation-motion artifacts, one per column, plus the Asymmetry Scorecard (its gap), the Milestone Valuation Model (its Stage column) and the allocation coverage ratio (its book-level readout) |
| The plan | Section 6 | Not a document. It is the empty cells across the ledgers, ordered by where the sale starts |
| A check on any signal | Constitution, Friction Allocation Principles | [friction-allocation-diagnostic.md](./practice/friction-allocation-diagnostic.md) |

---

## 3. The sort

| File | Words | What it does | Where it sits in 08 | Call | Note |
|---|---|---|---|---|---|
| [00-market-reading.md](./practice/00-market-reading.md) | 2,914 | Reads a buyer population before any buyer is met, ending in pursue, restructure or decline | Market reading | **Rebuild** | Light. The seller's limit becomes what the seller builds before any deal, the motion moves under Axiom II, and the search ledger becomes a section of it, since both live at the market and are written once. |
| `asymmetry-scorecard.md` | 1,833 | Scores the two halves of the policing gap | The enforcement ledger's gap, read from its Map and Test columns | **Merge** into the enforcement ledger | The two halves are counts of empty cells in the ledger's buyer and seller columns. Its scoring functions stay in the model. |
| [consensus-friction-calculator.md](./practice/consensus-friction-calculator.md) | 1,339 | Sizes the bargaining cost with $\alpha N^{\beta}(1 + \text{Var})$ and picks an intervention band | The bargaining ledger | **Merge** into the new bargaining ledger | The triage already reads the bargaining position from the count. What this file adds is variance, which needs each occupant's stated position, which is what the decision-role map records. Its three bands become the ledger's routing. The equation stays in the math file. |
| [friction-allocation-diagnostic.md](./practice/friction-allocation-diagnostic.md) | 1,768 | Tests whether a signal is cheap talk against the four principles | A check on every Test cell, and on the job "lets a deal go ahead" | **Rebuild**, shorter | It passes all three questions: it decides whether an artifact counts as evidence the buyer can check. Most of its length argues why the four principles are the only four, which is theory, and that argument goes to [costly-signals.md](./theory/02-research/costly-signals.md). |
| [friction-efficiency-index.md](./practice/friction-efficiency-index.md) | 2,346 | Four book-level measures and a composite, with the composite's defects recorded | The allocation coverage ratio is the enforcement ledger's Stage column, counted across a book | **Merge** the coverage ratio into the enforcement ledger. **Archive** the rest | 08 already names the coverage ratio as Axiom III's allocation clause made countable. Velocity, risk mitigation and scope variance change no decision on a deal, and the composite carries recorded defects. Their calibration rows and tests go with them. |
| `milestone-valuation-model.md` | 1,812 | Designs gates so each one retires a tranche of uncertainty | The enforcement ledger's Stage column | **Merge** into the enforcement ledger's Stage stage | Its three design rules and reference gates are how the Stage column is filled. The stage equation stays in the math file, section 5.4. The Constitution links it as the staging instrument, so that link moves. |
| [cfir-field-mapping.md](./practice/cfir-field-mapping.md) | 1,705 | Maps implementation-research constructs onto the field artifacts | None. It is a crosswalk, not an instrument | **Archive** to [cfir.md](./theory/02-research/cfir.md) | It fails the first question. The construct table moves to the research file, as one table keyed to the rebuilt instruments. `CLAUDE.md`'s rule to read it before editing practice points there instead. |
| `01-discovery-contextual-blueprint.md` | 1,082 | Discovery: the catalyst, the complexity map, the stakeholders, the reciprocity gate, the declared limits | Map column of the enforcement ledger, and the first column of the decision-role map | **Rebuild** as the enforcement ledger's Map stage | Its Stakeholder DNA moves to the bargaining ledger, and the catalyst is a value reading under the second standing assumption. |
| `02-validation-red-team-protocol.md` | 1,532 | Pre-mortem workshop, the skeptic, the signed gap analysis of product limits | Test column of the enforcement ledger | **Rebuild** as the enforcement ledger's Test stage | Its Stakeholder Diagnosis moves to the bargaining ledger. |
| `03-closing-mutual-implementation-plan.md` | 902 | Contracts the outcome: the north star, the governance structure, go and no-go | Stage column of the enforcement ledger, and the arrangement record | **Rebuild** as the enforcement ledger's Stage stage, absorbing the Milestone Valuation Model | Adds what 6.1 requires at contract: staged gates with a priced right to stop, a hostage or allocated right where one side sinks far more, and the standing review with what each side can invoke. |
| [04-sustaining-adoption-review.md](./practice/implementation-motion/04-sustaining-adoption-review.md) | 2,224 | Handoff, the adoption review, the business review, renewal | Maintain column, and the standing review | **Rebuild**, kept separate | Different owner and different time: it runs after signature, by customer success. It is where open question 46, the review's specification, gets settled. |

**Result.** Thirteen practice files become six:
1. the market reading, with the search ledger
2. the deal reading (the Triage Calculator)
3. the bargaining ledger, new
4. the enforcement ledger, with its Map, Test and Stage stages
5. the adoption review
6. the signal check

The practice layer is about 24,000 words today. A rough target is 12,000 to 14,000. That is an estimate, and each rebuild will be held to the three questions instead of to a number.

---

## 4. Choices still open

- **P1. One enforcement ledger file, or four.** The four artifacts are the four columns of one ledger, and 08 says it is one document that grows to the right. Proposed: one file with three stages (Map, Test, Stage), with Maintain in the adoption review. The alternative keeps three files that each fill their column of a shared ledger, which is closer to how a sales team runs the meetings.
- **P2. Build the bargaining ledger now or later.** It is the largest gap in the practice layer, and open question 2 has said so since 4.0. Proposed: build it third, from the Consensus Friction Calculator's bands, the Blueprint's Stakeholder DNA and the Red Team's Stakeholder Diagnosis, so those three can be cut.
- **P3. The Friction Efficiency Index.** Proposed: keep only the coverage ratio, inside the enforcement ledger, and archive the other three measures and the composite with their tests and calibration rows. The alternative keeps the file as a book-level report.
- **P4. The CFIR mapping.** Proposed: archive it to the research file and change `CLAUDE.md`'s read-before-editing rule to point there.

---

## 5. Sequence

One PR each, in the order 08's phases run, so no instrument is rebuilt before the one it reads from.

1. **The market reading,** with the search ledger.
2. **The enforcement ledger,** absorbing the Blueprint, the Red Team, the Mutual Implementation Plan, the Milestone Valuation Model, the Asymmetry Scorecard and the coverage ratio.
3. **The bargaining ledger,** absorbing the Consensus Friction Calculator and the stakeholder sections.
4. **The adoption review,** with the standing review's specification.
5. **The signal check,** shortened, and the archive: the rest of the Friction Efficiency Index and the CFIR mapping.

Each PR moves the inbound links, test headers and calibration rows for what it merges or archives, and runs the five checks. This file retires to git history when the last PR merges, along with the 5.0 and 6.0 proposals.
