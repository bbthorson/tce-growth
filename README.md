# Transaction Cost Growth (TCG) Knowledge Base

**A theory of go-to-market built on transaction cost economics: what a deal costs a buyer beyond the price determines how it can be sold, and often whether it can be sold at all.**

---

## What is TCG?

Buying costs more than money. Finding a solution, getting your own organization to agree, and installing the thing without breaking something are three separate bills, and a buyer pays all three before they see any value. **Transaction Cost Growth is the claim that those three costs, not the product and not the pitch, determine which go-to-market motion a deal can support.**

Two properties of that cost structure carry the decision.

> **How much cost there is decides how much apparatus the deal can carry. Which cost dominates decides what that apparatus should be.**

The named motions are regions of that space rather than competing philosophies. A deal whose cost sits in finding and comparing is a Sales-Led deal. One whose cost is small on every axis is Product-Led. One whose cost sits in installation is Implementation-Led. One whose cost sits in getting the buyer's own people to agree has no established playbook at all, which is a finding rather than an omission. Choosing between Turnkey, search-led and implementation-led as though they were strategies is choosing a label before measuring the thing the label is supposed to describe.

Three axioms carry the argument. Costs decompose and their composition selects the motion. Uncertainty inflates each cost by whatever the parties to it cannot verify, which is why unverifiable claims are expensive rather than merely unconvincing. And whether the arrangement survives depends on who holds a stake in the outcome, including the channels and platforms standing between the two sides.

Everything in this repository derives from those three, and the derivation is checked rather than asserted: every equation has an implementation in [`models/`](models/), every worked example is tested against it, and every headline statistic carries a provenance row.

**The numbers are held separately from the claims.** Every coefficient, threshold and band edge sits in [the calibration layer](theory/01-foundation/08-calibration.md) with an honest provenance status, and none of them is fitted to booked deal data. The framework is coherent rather than confirmed, it says what would confirm it, and it is built so that doubting a number does not require doubting the structure the number sits in.

---

## How this repo is organized

The repo serves **three functions**, each in its own top-level directory, plus a fourth directory holding the equations in code.

| Function | Where | What it is |
|---|---|---|
| **[theory/](theory/)** | `theory/01-foundation/` + `theory/02-research/` | Develop and pressure-test the TCG framework. Academic papers, axioms, definitions. |
| **[practice/](practice/)** | `practice/01-field-assets/` + `practice/02-internal-ops/` | Help sellers and managers actually run the motions. Templates and governance. |
| **[publishing/](publishing/)** | `publishing/01-cases/` + `publishing/02-tools/` | Turn the framework into public writing. Case analyses, voice guides, content generators. |
| **[models/](models/)** | `models/` | Executable forms of the equations, so a worked example cannot drift from its formula. Python, no dependencies. |

Each group has its own README listing what is inside it.

---

## Start here: which state are you in

The framework indexes on **state**, not on document. Name where the deal is, and the state names what governs it. The three states are defined in [Constitution Part I](theory/01-foundation/00-tcg-constitution.md).

| State | The question | Governed by | Go here |
|---|---|---|---|
| **Market** | Which motion is viable at all? | Axiom I | [Deal Triage Calculator](practice/01-field-assets/deal-triage-calculator.md), then [01-motion-taxonomy.md](theory/01-foundation/01-motion-taxonomy.md) |
| **Deal** (T0) | What must the seller supply before signature? | Axiom II | [practice/01-field-assets/](practice/01-field-assets/) — Blueprint, Red Team, MIP in order |
| **Relationship** (T1+) | Does the surplus survive, and who can displace it? | Axiom III | [Sustaining Adoption Review](practice/01-field-assets/implementation-motion/04-sustaining-adoption-review.md), [05-seller-surplus-model.md](theory/01-foundation/05-seller-surplus-model.md) §7 |

Each axiom has a home state and none is confined to it. Part I explains where the mapping holds and where it does not.

## Looking for something specific

| If you want to... | Go here |
|---|---|
| Understand the theory cold | [theory/01-foundation/](theory/01-foundation/) |
| Look up a symbol or term | [04-glossary-and-notation.md](theory/01-foundation/04-glossary-and-notation.md) |
| See the evidence behind a claim | [theory/02-research/00-reading-guide.md](theory/02-research/00-reading-guide.md) |
| Decide whether to invest engineering in a deal | [05-seller-surplus-model.md](theory/01-foundation/05-seller-surplus-model.md) |
| Set up your org for TCG | [practice/02-internal-ops/](practice/02-internal-ops/) |
| Compute a formula, or check one still holds | [models/](models/) |
| Write about TCG publicly | [publishing/02-tools/](publishing/02-tools/) |

**Orientation lives in two places only:** this file, and [the research reading guide](theory/02-research/00-reading-guide.md). Every other README is a local index of its own directory.

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

Names, scope, and taglines below are canonical. If this table and the [Constitution](theory/01-foundation/00-tcg-constitution.md) ever disagree, the Constitution wins.

| Axiom | Governs | Tagline | What it says |
|---|---|---|---|
| **I. Law of Transaction Cost Composition** | Whether a deal can happen | *"Costs determine the deal"* | Search, consensus, and implementation costs decompose. Their composition selects the motion and their combined level sets the Turnkey and Structural boundary. Exposure to asset specificity belongs to whichever party sinks the specific investment. |
| **II. Law of Uncertainty Inflation** | What the deal costs when it happens | *"Fear > Value"* | Base friction is amplified by the bilateral asymmetry gap between buyer and seller. Reducing risk moves more surplus than increasing ROI. |
| **III. Law of Governance** | Whether the deal persists | *"Structure determines behavior"* | Every party whose decisions affect outcomes needs skin in the game tied to those outcomes, including the channels and adjudicators between them. |

### Turnkey vs. Structural Deals

| | **Turnkey Deal** | **Structural Deal** |
|---|---|---|
| Level | Below 15 on the [Deal Triage Calculator](practice/01-field-assets/deal-triage-calculator.md) | 15 to 30 |
| Motion | Turnkey. Optimize for velocity | Search-led, consensus-led or implementation-led, by direction |
| Example | Standalone SaaS tools, modular utilities | Enterprise platforms, deep workflow rewiring |

---

## Contributing

This is a living document. As you work:
- Add new applied analyses to [publishing/01-cases/](publishing/01-cases/) using the trenches protocol.
- Refine field assets in [practice/01-field-assets/](practice/01-field-assets/) based on what works.
- Update research with new evidence; the [provenance audit](theory/02-research/audits/citation-provenance-audit.md) tracks source quality.

---

**Version:** 1.0 (tracks the [Constitution](theory/01-foundation/00-tcg-constitution.md) version; bump both together)
**Last updated:** 2026-09-10
