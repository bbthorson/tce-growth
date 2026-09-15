---
title: "Real Options Under Irreversibility"
layer: theory
status: active
operationalizes: [axiom-2, axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# Real Options Under Irreversibility

**Sources:**
- Dixit, A.K. & Pindyck, R.S. (1994). *Investment under Uncertainty*. Princeton University Press.
- McDonald, R. & Siegel, D. (1986). "The Value of Waiting to Invest." *Quarterly Journal of Economics*, 101(4), 707–728.
- Trigeorgis, L. (1996). *Real Options: Managerial Flexibility and Strategy in Resource Allocation*. MIT Press.

**Abstract.** Net present value analysis assumes an investment is either reversible or a one-time take-it-or-leave-it choice. Dixit and Pindyck showed that when an investment is irreversible and the environment is uncertain, neither assumption holds, and the ability to wait carries real economic value. Committing capital destroys the option to learn first. That destroyed option is a genuine cost that NPV omits, which is why firms rationally decline investments with positive expected value. The corollary matters more for TCG than the theorem: an investment restructured into stages, each contingent on resolved uncertainty, is worth more than the same investment committed at once, because staging preserves the option to stop.

**Key claims:**
- Under irreversibility and uncertainty, the option to defer has positive value, and exercising it early forfeits that value.
- A positive-NPV project can still be correctly rejected when the option value of waiting exceeds the net present value.
- Higher uncertainty raises the value of waiting, so uncertainty delays commitment rather than merely discounting it.
- Staging converts one irreversible decision into a sequence of smaller ones, each taken with more information than the last.
- An abandonment option bounds maximum downside, which raises the value of the whole sequence independent of any change in expected return.
- Option value is destroyed by contract structures that force full commitment before uncertainty resolves.

**Supports in TCG:**
- **Staged Commitment** (Axiom II corollary, with Axiom III) — direct theoretical basis. Phase gating is option construction.
- **Axiom III — Law of Uncertainty Inflation** — explains a mechanism the Constitution otherwise leaves implicit. Buyer uncertainty does not only inflate cost, it also raises the value of doing nothing. This is the formal account of why the Safe No beats the Logical Yes.
- **The MIP** — operationalizes both the staging option and the abandonment option. Gate-contingent payments with defined acceptance criteria give the buyer a priced right to stop.
- **Milestone Valuation Model** — applies staged uncertainty decay to gate design. See [milestone-valuation-model.md](../../practice/milestone-valuation-model.md).
- **Akerlof Exit Threshold** (clarifying concept) — real options supplies the complementary explanation. The buyer may exit not because signals failed but because waiting dominates acting.

**Notable quotes:**
- The status quo is not inertia. It is an option the buyer currently holds and the seller is asking them to give up.
- A buyer who says "not yet" is often pricing the option to wait correctly. The counter is to make waiting cost something.
- Staging does not reduce the work. It reduces how much of the work must be committed before the buyer knows whether it will succeed.

**Notable statistics:**
- None. This source contributes structure rather than measurement. Implementation failure rates that justify the abandonment option live in [fear-of-failure.md](./fear-of-failure.md).
