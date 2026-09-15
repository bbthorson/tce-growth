---
title: "Foundation"
layer: theory
status: active
---

# Foundation

**Start here.** These documents form the canonical theoretical basis for everything else in the repo. Read in numerical order.

Parent: [theory/](../) · Sibling: [02-research/](../02-research/)

The three states (Market, Deal at T0, Relationship at T1+) are the framework's primary index. They are defined in [00-tcg-constitution.md](./00-tcg-constitution.md) Part I and used as the front door in the [root README](../../README.md).

## Reading order

1. **[01-motion-taxonomy.md](./01-motion-taxonomy.md)** — *(start here if you're new)* The four motions, each named after the cost it spends to reduce, and what each one contains. Gives you the lay of the land before you dive into theory.
2. **[00-tcg-constitution.md](./00-tcg-constitution.md)** — The full economic and behavioral framework, structured as a deductive system. Four parts:
   - **Part I:** The Three Axioms — Law of Transaction Cost Composition, Law of Uncertainty Inflation, Law of Governance
   - **Part II:** Derived Concepts — primary derivations from each axiom (Boundary Condition, Friction Allocation Principles, Three Sales Levers, Recursive Cooperation, Reputation Depreciation), bridge concepts (Decay Clock, Effective Cost, Staged Commitment, Surplus)
   - **Part III:** Synthesis — the full integrated Surplus equation and the failure-modes summary. Part I carries one figure per axiom, generated from [`models/`](../../models/README.md).
4. **[03-mathematical-models.md](./03-mathematical-models.md)** — *(reference)* Functional forms, parameter specifications, and the derivation connecting the structural and reduced forms of transaction cost.
5. **[04-glossary-and-notation.md](./04-glossary-and-notation.md)** — *(reference, read as needed)* Every symbol and term in one place, with a pointer to where each is canonically defined. The notation index is itself canonical, since symbols had no home before it. Includes a disambiguation section for the five symbol pairs that look alike and mean different things.
6. **[05-seller-surplus-model.md](./05-seller-surplus-model.md)** — The seller's side of the transaction. The Constitution models what the buyer gains and pays; this specifies what the seller spends before signature, what portion of it is exposed, and when the spend is worth making. Read it before designing a forward-deployed or implementation-heavy engagement.

7. **[06-friction-vector.md](./06-friction-vector.md)** — Derives motion selection from the direction and length of the three-component cost vector, which is where Axiom I's composition claim and Axiom II's per-component amplification come from. Section 9 records what it does not settle.
8. **[07-governance-forms.md](./07-governance-forms.md)** — What shape the arrangement should take once the deal closes. Adds frequency as Axiom I's third property, derives Williamson's four governance forms from level and frequency, and names the make-or-buy boundary that sits in the Surplus equation. Read it for the strategy layer rather than the deal layer.
9. **[08-calibration.md](./08-calibration.md)** — *(reference)* Every coefficient, threshold and band in the framework, in one place, with an honest provenance status on each. Nothing in it is measured. Read it before quoting any number outside this repository.
10. **[09-motion-vocabulary.md](./09-motion-vocabulary.md)** — *(reference)* How the motion names map onto Product-Led, Sales-Led and the rest of the incumbent vocabulary, and where the older terms mislead. Read it if you arrived holding those terms, or before writing anything public.

## What goes here vs. elsewhere

| Type of content | Where it lives |
|---|---|
| Theoretical framework, axioms, equations | **`theory/01-foundation/`** (this directory) |
| Academic papers and evidence | [`../02-research/`](../02-research/) |
| Templates reps actually use | [`../../practice/`](../../practice/) |
| Comp plans, calibration, governance | [`../../practice/`](../../practice/) |

If a concept is invoked in two or more directories, its canonical definition lives **here**.
