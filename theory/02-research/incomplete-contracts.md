---
title: "Incomplete Contracts and Residual Control Rights"
layer: theory
status: active
operationalizes: [axiom-2, axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# Incomplete Contracts and Residual Control Rights

**Sources:**
- Grossman, S.J. & Hart, O.D. (1986). "The Costs and Benefits of Ownership: A Theory of Vertical and Lateral Integration." *Journal of Political Economy*, 94(4), 691–719.
- Hart, O. & Moore, J. (1988). "Incomplete Contracts and Renegotiation." *Econometrica*, 56(4), 755–785. (not yet read here)
- Hart, O. & Moore, J. (1990). "Property Rights and the Nature of the Firm." *Journal of Political Economy*, 98(6), 1119–1158.
- Hart, O. (2016). Nobel Prize Lecture: "Incomplete Contracts and Control."
- Crocker, K.J. & Reynolds, K.J. (1993). "The Efficiency of Incomplete Contracts: An Empirical Analysis of Air Force Engine Procurement." *RAND Journal of Economics*, 24(1), 126–146.
- Bajari, P. & Tadelis, S. (2001). "Incentives versus Transaction Costs: A Theory of Procurement Contracts." *RAND Journal of Economics*, 32(3), 387–407.
- MacCormack, A., Verganti, R. & Iansiti, M. (2001). "Developing Products on 'Internet Time': The Anatomy of a Flexible Development Process." *Management Science*, 47(1), 133–150.
- Merrow, E.W. (2011). *Industrial Megaprojects: Concepts, Strategies, and Practices for Success.* Wiley.
- Gibson, G.E. & Dumont, P.R. (1996). *Project Definition Rating Index (PDRI) for Industrial Projects.* Construction Industry Institute, Research Report 113-11.
- Flyvbjerg, B. & Budzier, A. (2011). "Why Your IT Project May Be Riskier Than You Think." *Harvard Business Review*, 89(9), 23–25.
- Wathne, K.H. & Heide, J.B. (2000). "Opportunism in Interfirm Relationships: Forms, Outcomes, and Solutions." *Journal of Marketing*, 64(4), 36–51. doi:10.1509/jmkg.64.4.36.18070.

Crocker and Reynolds through Flyvbjerg and Budzier reached the repository through an external review in 2026-09. Wathne and Heide was added in 2026-11 for Constitution 5.0, read in full. Page ranges are to be verified against the journal record before any is quoted.

**Abstract.** Complete contracting models assume parties can foresee every future state, assign probabilities, and write verifiable obligations for each one. Grossman and Hart showed that under bounded rationality and transaction complexity, contracts are necessarily incomplete: states arise that no one specified and no court can verify. What governs the relationship in those states is not the contract but the allocation of *residual control rights*, meaning the right to decide how an asset gets used when the contract is silent. Hart and Moore extended this to show that ownership structure is precisely the allocation of those residual rights, and that misallocating them destroys the incentive to make relationship-specific investments in the first place.

This is the theoretical layer beneath Williamson's hold-up problem. Williamson explained why asset specificity creates exposure. Grossman-Hart-Moore explained what actually determines the outcome once exposure exists.

**Key claims:**
- Contracts covering complex transactions are incomplete as a structural matter, not as a drafting failure. More lawyering does not close the gap.
- What governs unspecified states is the allocation of residual control rights, decided in advance.
- Under high asset specificity, incomplete contracts expose whichever party sunk the specific investment to opportunistic renegotiation.
- Anticipated hold-up suppresses specific investment before it happens. The buyer under-invests in integration precisely because they foresee the exposure.
- Efficiency depends on giving residual control to the party whose investment matters most at the margin.
- Reducing the space of unspecified states is itself a governance intervention, distinct from reallocating control within that space.

**Supports in TCG:**
- **Claim 12.** Direct basis. No contract foresees everything, so the two sides settle who decides where it is silent: who carries which risk, in stages, with a point at each where either can stop. A Mutual Implementation Plan is that allocation written down. Joint sign-off at each stage splits the right to decide, so neither side can impose an outcome when something unmapped appears.
- **Claim 11.** Hold-up that a party expects suppresses its investment before it happens. That is why a buyer that sees lock-in coming prices it before it signs, and builds less.
- **Claim 9.** Shrinking the set of states nobody specified is a separate act from deciding who controls them. Discovery does the first, and the Contextual Blueprint records it.
- **Claim 6.** None of this applies to a plug-in purchase, where nothing is built that the price mechanism cannot govern.

---

## Extension: allocation before the investment is sunk, adaptation after (2026-09)

This is the evidence behind claim 12's sentence that the two sides settle who carries which risk before either builds. Item 7 in [06-calibration.md](../01-foundation/06-calibration.md) is the test it still owes.

**The empirical record on contract completeness.** Crocker and Reynolds found that Air Force engine procurement contracts were written more incompletely as technological uncertainty rose, deliberately, because drafting contingencies that would be obsolete by execution cost more than resolving them later. Bajari and Tadelis formalized the trade-off: fixed-price contracts on complete ex-ante specifications invite opportunistic change orders once adaptation is needed, and cost-plus contracts with deliberately incomplete specifications govern adaptation more cheaply when complexity is high. MacCormack, Verganti and Iansiti found that in fast-moving software environments, early specification freezes correlated negatively with product quality, and teams that deferred the freeze and iterated on feedback outperformed.

**Where front-end definition pays.** Merrow's benchmarks across industrial capital projects, and the Construction Industry Institute's Project Definition Rating Index, show that scope definition before sanction is the strongest predictor of cost and schedule performance where the specification is static and the cost of change steep. Flyvbjerg and Budzier's work on IT projects adds that duration itself compounds tail risk, so lengthening definition cycles in uncertain projects raises exposure rather than lowering it.

**What follows for claims 9 and 12.** Under uncertainty, what can be settled before the investment is sunk is the allocation of adaptation risk, who bears it, staged how, with what right to stop, which is residual control in Grossman-Hart-Moore's sense. The adaptation itself follows, and Strong and Volkoff's finding that misfits in roles, controls and culture surface only in use says why it must. So the allocation is settled in advance, and the share of the work done in advance can fall as uncertainty rises. Where specification is static, the two coincide and front-end loading pays directly. The [Enforcement Ledger](../../practice/enforcement-ledger.md)'s Map and Stage divide along this line: the first shrinks the set of unspecified states as far as discovery can reach, the second allocates control over the states it cannot.

---

## Extension: hold-up under full information (2026-11)

This is the evidence behind claim 12's sentence that proof before signature shows what a seller can do without binding what either side does once the other cannot easily leave.

**Two conditions, not one.** Wathne and Heide sort opportunism by whether it is passive or active and whether it happens under existing or new circumstances. That gives four forms: evasion, refusal to adapt, violation and forced renegotiation. They name two separate conditions that make opportunism possible. One is information asymmetry, where one party cannot see what the other does. The other is lock-in, where one party has sunk an investment that ties it to the relationship.

**Monitoring reaches only the first.** Their treatment of governance pairs each condition with a remedy. Monitoring works only against opportunism that depends on hidden information. A party exploiting the other's lock-in, by refusing to adapt or by forcing a renegotiation, can do it in plain view, so watching more closely does not stop it. What governs lock-in is incentives, including hostages: something the defecting party loses, such as a bond, a reciprocal specific investment or fees staged against delivery. Selection and socialization are their other two remedies.

**What follows for claims 11 and 12.** Proof, references and maintained evidence answer the hidden-information half. The lock-in half is exposure to what a party can see and cannot stop, and most drift after signature looks like it. Nobody hides anything. The sponsor leaves, a priority changes, or the seller moves its best people to a newer account, and both sides can see it happen. What answers it is something each side loses by defecting: fees staged against delivery, engineering staged against the buyer's commitment, and a renewal either side can decline. Option contracts and renegotiation design are a second remedy. They settle in advance who controls a renegotiation (Aghion, Dewatripont and Rey 1994, Nöldeke and Schmidt 1995). Section 4 of [06-calibration.md](../01-foundation/06-calibration.md) lists those sources, and item 40 there asks which remedy works where.

**Quotes and statistics.** Citable passages from this source are collected in [source-quotes.md](../../publishing/02-tools/source-quotes.md). Its numbers are recorded, with provenance, in the [citation audit](./audits/citation-provenance-audit.md).
