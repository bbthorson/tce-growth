# Transaction Cost Growth (TCG) Knowledge Base

**A theory of go-to-market built on transaction cost economics: what a deal costs a buyer beyond the price determines how it can be sold, and often whether it can be sold at all.**

---

## What is TCG?

Buying costs more than money. Finding a solution, getting your own organization to agree, and installing the thing without breaking something are three separate bills, and a buyer pays all three before they see any value. **Transaction Cost Growth is the claim that those three costs, not the product and not the pitch, determine which go-to-market motion a deal can support.**

Two properties of that cost structure carry the decision.

> **How much cost there is decides how much apparatus the deal can carry. Which cost dominates decides what that apparatus should be.**

The named motions are regions of that space rather than competing philosophies. A deal whose cost sits in finding and comparing is a Sales-Led deal. One whose cost is small on every axis is Product-Led. One whose cost sits in installation is Implementation-Led. One whose cost sits in getting the buyer's own people to agree has no established playbook at all, which is a finding rather than an omission. Choosing between Turnkey, search-led and implementation-led as though they were strategies is choosing a label before measuring the thing the label is supposed to describe.

Three axioms carry the argument, each stated at the level where a seller meets it. At the market level, every deal carries three costs beyond price, search, bargaining and enforcement, and the one that binds selects the motion. At the workflow level, the more specific the investment, the more a deal costs to transact and the more of that cost must be paid before signature. At the deal level, each cost is inflated by what the parties to it cannot verify about their own outcome, and the inflation rebuilds unless it is maintained.

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

Each group has its own README listing what is inside it.

---

## Start here: which level are you at

The framework indexes on **level**. Each axiom is stated where a seller meets it, and each produces a decision. The three levels are defined in [Constitution Part I](./theory/01-foundation/00-tcg-constitution.md).

| Level | The decision | Axiom | Go here |
|---|---|---|---|
| **Market** | Which cost binds, and therefore which instruments to run | I | [Deal Triage Calculator](./practice/deal-triage-calculator.md), then [01-motions.md](./theory/01-foundation/01-motions.md) |
| **Workflow** | How specific the investment is, how much apparatus it needs, when to spend it, what arrangement holds it | II | [Contextual Blueprint](./practice/implementation-motion/01-discovery-contextual-blueprint.md), [05-governance-forms.md](./theory/01-foundation/05-governance-forms.md) |
| **Deal** | What each party cannot verify about their own outcome, what to prove, and what to re-prove at renewal | III | [Red Team](./practice/implementation-motion/02-validation-red-team-protocol.md), [MIP](./practice/implementation-motion/03-closing-mutual-implementation-plan.md), [Sustaining Adoption Review](./practice/implementation-motion/04-sustaining-adoption-review.md) |

Axiom II is the gate. When the investment is not specific, market terms hold and the other two readings barely matter.

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

### The Fundamental Equation

$$S = \left(V_{solution} \cdot e^{-\delta t} - V_{next\_best}\right) - (F_{search} + F_{consensus} + F_{implementation}) \cdot (1 + \Delta_A) = OC_{\text{switching}} - y$$

- **S** = Deal Surplus (must be > 0 for a deal to close)
- **Δ_A** = Bilateral Asymmetry Gap = Seller Ignorance + Buyer Uncertainty
- **y** = Total Perceived Transaction Cost = $a\hat{\Delta}_A^2 + c$ (where $a = 2.25$ is risk aversion, $\hat{\Delta}_A$ is the normalized deal-level asymmetry gap, and $c$ is direct cost, all as fractions of annual contract value)
- **δ** = Decay Rate of urgency after the triggering event
- Applies when **k > k_threshold** (the deal is Structural, not Turnkey) AND **F_deployed ~ k** (the friction deployed matches the specificity)

### The Three Axioms

Statements below are canonical. If this table and the [Constitution](./theory/01-foundation/00-tcg-constitution.md) ever disagree, the Constitution wins.

| Axiom | Level | Statement |
|---|---|---|
| **I. Law of Transaction Cost Composition** | Market | Every deal carries three costs beyond price, search, bargaining and enforcement, and the one that binds selects the motion. |
| **II. Law of Asset Specificity** | Workflow | The more specific the investment, the more a deal costs to transact, and the more of that cost must be paid before signature. |
| **III. Law of Uncertainty Inflation** | Deal | Each cost is inflated by what the parties to it cannot verify about their own outcome, and the inflation rebuilds over time unless it is maintained. |

The field calls the bargaining cost *consensus* and the enforcement cost *implementation*, and the notation keeps those subscripts.

### Turnkey vs. Structural Deals

| | **Turnkey Deal** | **Structural Deal** |
|---|---|---|
| Level | Below 15 on the [Deal Triage Calculator](./practice/deal-triage-calculator.md) | 15 to 30 |
| Motion | Turnkey. Optimize for velocity | Search-led, consensus-led or implementation-led, by direction |
| Example | Standalone SaaS tools, modular utilities | Enterprise platforms, deep workflow rewiring |

---

## Contributing

This is a living document. As you work:
- Add new applied analyses to [publishing/01-cases/](./publishing/01-cases/) using the trenches protocol.
- Refine field assets in [practice/](./practice/) based on what works.
- Update research with new evidence; the [provenance audit](./theory/02-research/audits/citation-provenance-audit.md) tracks source quality.

---

**Version:** 2.4 (tracks the [Constitution](./theory/01-foundation/00-tcg-constitution.md) version; bump both together)
**Last updated:** 2026-09-22
