---
title: "Reading Guide"
layer: theory
kind: evidence
status: active
---

# Reading Guide

**How to navigate the research, in what order, for which audience.** This guide tells you where to start, what to read in what sequence, and what's safe to skip — given who you are and what you need.

The theoretical synthesis of these papers lives in the [Constitution](../canon/constitution.md). This guide tells you which papers back the Constitution's claims and how to read them efficiently.

---

## How the research builds

The papers in this directory depend on each other in a specific order. Lower-level papers establish foundations the higher-level papers build on, and the numbered list below is that order.

This section carries reading order only. Which axiom each paper backs is in the [Constitution](../canon/constitution.md) under Related, which is the canonical mapping, and repeating it here would give it a second home to drift from.

**Order of dependency:**

1. **[Transaction Cost Economics](./transaction-cost-economics.md)** — Start here. Establishes why friction exists and why it's necessary.
2. **[Costly Signals](./costly-signals.md)** — Builds on TCE: how friction resolves information asymmetry.
3. **[Prospect Theory](./prospect-theory.md)** — Explains *why* buyers fear change at the neurobiological level (λ ≈ 2.25).
4. **[Game Theory and NRR](./game-theory-and-nrr.md)** — Shows how incentives must be structured to sustain cooperation across the repeated game.
5. **[Fear of Failure](./fear-of-failure.md)** — Empirical evidence: Standish CHAOS, Gartner regret data, the JOLT Effect.
6. **[CFIR](./cfir.md)** — Pre-sale diagnostic methodology.
7. **[RE-AIM](./re-aim-framework.md)** — Post-sale measurement methodology.

Plus the channel-level layer:

8. **[Channel Collapse](./channel-collapse.md)** — Jevons' Paradox applied to outbound. Governance solutions for the channel-level externality problem.

Plus three sources that each deepen an axiom already in place, so read them after the paper they extend rather than in sequence:

9. **[Incomplete Contracts](./incomplete-contracts.md)** — Read after Transaction Cost Economics. Williamson explains why asset specificity creates exposure. Grossman-Hart-Moore explain what determines the outcome once exposure exists, which is the allocation of residual control rights. This is the theory beneath the MIP.
10. **[Buying Center Dynamics](./buying-center-dynamics.md)** — Read before CFIR. Establishes that the buyer is a coalition rather than an agent, which is the premise CFIR's Inner Setting analysis depends on. Supplies the structure of $F_{consensus}$.
11. **[Real Options](./real-options.md)** — Read after Prospect Theory. Loss aversion explains why the buyer fears the downside. Real options explains why waiting is a rationally priced alternative rather than mere inertia, and why staged commitment is the counter.

Plus the implementation layer:

12. **[Process Misfit](./process-misfit.md)** — Read after Transaction Cost Economics and before CFIR. Williamson establishes that asset specificity raises governance cost. The misfit literature says what that specificity is made of in a software deal, and names the six domains a seller can inspect before signature. Supplies the structure of $F_{implementation}$, the way Buying Center Dynamics supplies the structure of $F_{consensus}$.

Plus the seller-side layer:

13. **[Appropriable Quasi-Rents and Supplier-Side Hold-Up](./klein-crawford-alchian.md)** — Read after Transaction Cost Economics and alongside Incomplete Contracts. Williamson says specificity creates exposure. Klein, Crawford and Alchian name the quantity at stake and establish that it belongs to whichever party sank the investment, which in a forward-deployed motion is the seller. Backs [seller-surplus.md](../arguments/seller-surplus.md).

---

## The shape of an entry

Each file in this directory follows one form, so a reader knows where to look before opening it.

- **Sources** — authors, year, paper title, journal or publisher, link to the primary source.
- **Abstract** — three or four sentences carrying the core finding.
- **Key claims** — what the work establishes, as statements.
- **Supports in TCG** — which axiom or derivation this source backs, with a one-line connection.
- **Quotes and statistics** — a pointer, never the thing itself. Citable passages live in [`source-quotes.md`](../../publishing/02-tools/source-quotes.md) and every number lives in [citation-provenance-audit.md](./citation-provenance-audit.md) with its verification status, so a research file carries argument only.

---

## What you won't find here

This is a citation index, not a theoretical synthesis, and this section is the directory's scope boundary in both directions.

| Content | Where it lives |
|---|---|
| Canonical citations, abstracts, source links | **this directory** |
| Three axioms and their derivations | [Constitution](../canon/constitution.md), Parts I and II |
| Surplus equation and failure modes | Constitution Part III. The per-axiom figures are in Part I, generated from [`models/`](../../models) |
| Instruments and artifacts | [`practice/`](../../practice) |
| Applied analysis of a specific deal or event | [`publishing/01-cases/`](../../publishing/01-cases) |
| Published or polished commentary | [`publishing/02-tools/style-references/`](../../publishing/02-tools/style-references) |
| Citable passages, and every statistic with its status | [`source-quotes.md`](../../publishing/02-tools/source-quotes.md), [citation-provenance-audit.md](./citation-provenance-audit.md) |
