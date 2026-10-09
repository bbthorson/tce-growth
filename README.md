# Transaction Cost Growth (TCG) Knowledge Base

**A theory of go-to-market built on transaction cost economics: what a deal costs a buyer beyond the price determines how it can be sold, and often whether it can be sold at all.**

---

## What is TCG?

Buying costs more than money. Finding a solution, getting your own organization to agree, and installing the thing without breaking something are three separate bills, and a buyer pays all three before they see any value. **Transaction Cost Growth is the claim that those three costs, not the product and not the pitch, determine which go-to-market motion a deal can support.**

Each cost is read on its own, never summed with the others.

> **Any one cost can keep a buyer out of the market. Among the costs a buyer will bear, the one nearest that limit is where the sale starts.**

The named motions are named after the cost a seller pays down first, and they are not competing philosophies. A sale that starts at finding and comparing is search-led. One that starts at getting the buyer's own people to decide is consensus-led. One that starts at whether the seller will deliver and the product will work here is implementation-led. Where every cost is low enough for the buyer to pay down alone, and nothing specific is sunk, the market is Turnkey, and Turnkey does not last on its own: the low investment that defines it invites entrants, and entrants raise the search cost. The familiar labels only partly line up. Sales-Led Growth is narrower than search-led, Product-Led Growth overlaps Turnkey without equaling it, and consensus-led has no established name at all, which is a finding rather than an omission. [01-motions.md section 10](./theory/01-foundation/01-motions.md) carries the map. Choosing between these motions as though they were strategies is choosing a label before measuring the thing the label is supposed to describe.

Three axioms carry the argument, each answering one decision in time order. Should I use the market: using it costs the buyer three things beyond price, search and information, bargaining and decision, and policing and enforcement. What will it cost me today: each cost is paid down by the buyer, the seller or both, and each party goes ahead only when its own share is covered by its own return. What might it cost me later: whatever a party sinks that is worth less outside the relationship exposes it to what it cannot verify, and who carries that exposure has to be settled before the investment is sunk.

Everything in this repository derives from those three, and the derivation is checked rather than asserted: every equation has an implementation in [`models/`](./models/), every worked example is tested against it, and every headline statistic carries a provenance row.

**The numbers are held separately from the claims.** Every coefficient, threshold and band edge sits in [the calibration layer](./theory/01-foundation/06-calibration.md) with an honest provenance status, and none of them is fitted to booked deal data. The framework is coherent rather than confirmed, it says what would confirm it, and it is built so that doubting a number does not require doubting the structure the number sits in.

---

## How this repo is organized

The repo serves **three functions**, each in its own top-level directory, plus two directories holding the equations in code and the checkers.

| Function | Where | What it is |
|---|---|---|
| **[theory/](./theory/)** | `theory/01-foundation/` + `theory/02-research/` | Develop and pressure-test the TCG framework. Academic papers, axioms, definitions. |
| **[practice/](./practice/)** | `practice/` + `practice/implementation-motion/` | Operationalize the theory. The instruments the axioms name, and the measurement tools the tests assert. |
| **[publishing/](./publishing/)** | `publishing/01-cases/` + `publishing/02-tools/` | Turn the framework into public writing. Case analyses, voice guides, content generators. |
| **[models/](./models/)** | `models/` | Executable forms of the equations, so a worked example cannot drift from its formula. Python, no dependencies. |
| **[tools/](./tools/)** | `tools/linting/` | The link, frontmatter and style checkers. |

Each has a README listing what is inside it. For `tools/` it is [tools/linting/README.md](./tools/linting/README.md).

---

## Start here: which decision are you making

The framework indexes on **decision**. Each axiom answers one, and the three run in time order. They are stated in [Constitution Part I](./theory/01-foundation/00-tcg-constitution.md).

| Decision | What it settles | Axiom | Go here |
|---|---|---|---|
| **Should I use the market?** | Whether any cost keeps the buyer out, and which cost the sale starts with | I | [Deal Triage Calculator](./practice/deal-triage-calculator.md), then [01-motions.md](./theory/01-foundation/01-motions.md) |
| **What will it cost me today?** | Who invests against each cost, and whether each party's share fits its return | II | [Contextual Blueprint](./practice/implementation-motion/01-discovery-contextual-blueprint.md), [04-seller-surplus-model.md](./theory/01-foundation/04-seller-surplus-model.md) |
| **What might it cost me later?** | What each party sinks that is specific, what it cannot verify, what arrangement holds it, and what to re-prove at renewal | III | [Red Team](./practice/implementation-motion/02-validation-red-team-protocol.md), [MIP](./practice/implementation-motion/03-closing-mutual-implementation-plan.md), [05-governance-forms.md](./theory/01-foundation/05-governance-forms.md), [Sustaining Adoption Review](./practice/implementation-motion/04-sustaining-adoption-review.md) |

Where nothing specific is sunk and a trial verifies fit, the future cost is near zero and market terms hold. That is the gate, and it sits under Axiom III.

## Looking for something specific

| If you want to... | Go here |
|---|---|
| Understand the theory cold | [theory/01-foundation/](./theory/01-foundation/) |
| Look up a symbol or term | [03-glossary-and-notation.md](./theory/01-foundation/03-glossary-and-notation.md) |
| See the evidence behind a claim | [theory/02-research/00-reading-guide.md](./theory/02-research/00-reading-guide.md) |
| Decide whether to invest engineering in a deal | [04-seller-surplus-model.md](./theory/01-foundation/04-seller-surplus-model.md) |
| Compute a formula, or check one still holds | [models/](./models/) |
| Write about TCG publicly | [publishing/02-tools/](./publishing/02-tools/) |

**Orientation lives in two places only:** this file, and [the research reading guide](./theory/02-research/00-reading-guide.md). Every other README is a local index of its own directory.

---

## Core concepts at a glance

### The two conditions

$$S_b = V_{switch}(t) - P - \sum_k I^b_k - L_b > 0 \qquad S_s = P - C_{deliver} - \sum_k I^s_k - L_s > 0 \qquad r_k \le 1 \;\; \forall k$$

- **$S_b$, $S_s$** = the buyer's and the seller's surplus. A deal closes only when both are positive. All terms are fractions of annual contract value.
- **$V_{switch}(t)$** = $V_{solution} \cdot e^{-\delta t} - V_{next\_best}$, the buyer's opportunity cost of staying put, decaying at rate $\delta$ after the triggering event
- **$P$** = price over the relationship. It appears in both conditions and cancels when they are added, because price is a transfer and not a transaction cost.
- **$I^b_k$, $I^s_k$** = what the buyer and the seller invest today against cost $k \in \{search, consensus, implementation\}$ (Axiom II)
- **$L_b$, $L_s$** = each party's expected future loss, its specific exposure times the chance the exposure does not come back (Axiom III)
- **$r_k$** = where cost $k$ sits between the level the buyer can pay down alone and the level that keeps the buyer out. Above 1, the buyer does not enter the market. The sale starts at the largest (Axiom I).

The equations are in [Constitution Part III](./theory/01-foundation/00-tcg-constitution.md). Every threshold behind them is chosen rather than fitted, and [the calibration layer](./theory/01-foundation/06-calibration.md) says so.

### The Three Axioms

Statements below are canonical. If this table and the [Constitution](./theory/01-foundation/00-tcg-constitution.md) ever disagree, the Constitution wins.

| Axiom | Decision | Statement |
|---|---|---|
| **I. Law of Transaction Cost Composition** | Should I use the market? | Using the market costs the buyer three things beyond price: search and information, bargaining and decision, and policing and enforcement. A buyer will not use the market while any one of them exceeds what it will bear, and among costs it will bear, their relative size is where the sale starts. |
| **II. Law of Transaction Investment** | What will it cost me today? | Each of those costs is paid down by an investment from the buyer, the seller or both, and each party goes ahead only when its own share is covered by its own return. |
| **III. Law of Future Cost** | What might it cost me later? | Whatever a party sinks that is worth less outside this relationship exposes it to what it cannot verify later. That exposure is a future cost, it rebuilds unless maintained, and its allocation must be settled before the investment is sunk. |

The field calls the three costs *search*, *consensus* and *implementation*, and the notation keeps those subscripts.

### Turnkey, and routing outside it

Turnkey is a market condition, not a deal class: every cost low enough for the buyer to pay down alone, and nothing specific sunk. Outside it, a deal routes on two readings.

| | **Nothing specific sunk** | **Something specific sunk** |
|---|---|---|
| **Every cost self-serve** | Turnkey. Self-serve and standard terms | Light sale, heavy contract. Staging and stop rights agreed before the investment is sunk |
| **Some cost needs seller investment** | Heavy sale, light contract. The seller pays down search or decision costs, then standard terms hold | The full implementation chain |

---

## Contributing

This is a living document. As you work:
- Add new applied analyses to [publishing/01-cases/](./publishing/01-cases/) using the trenches protocol.
- Refine field assets in [practice/](./practice/) based on what works.
- Update research with new evidence; the [provenance audit](./theory/02-research/audits/citation-provenance-audit.md) tracks source quality.

---

**Version:** 4.0 (tracks the [Constitution](./theory/01-foundation/00-tcg-constitution.md) version; bump both together)
**Last updated:** 2026-10-09
