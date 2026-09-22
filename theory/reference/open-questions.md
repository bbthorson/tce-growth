---
title: "Open Questions"
layer: theory
kind: reference
status: active
version: 1.0
operationalizes: [axiom-1, axiom-2, axiom-3]
canonical_source: theory/canon/constitution.md
---

# Open Questions

**Version:** 1.0
**Purpose:** To record, in one place, where the theory is under-developed now that the axioms are fixed. Each entry says what the framework claims, what it lacks, and what would settle it. Entries are grouped by the axiom they weaken.

This register consolidates, and it is the only place a gap is written out. A file that had its own "what this does not settle" section now points here instead, because two registers drift apart and these already had. An entry leaves this file when the work is done or when the claim is withdrawn, and either exit is recorded in the Constitution's version history.

**The numbers are identifiers, not positions.** Other files cite entries by number, so a new entry takes the next free number inside its axiom group rather than renumbering what is already there. Expect gaps and expect the order inside a group to be arbitrary.

---

## Axiom I, composition

**1. Why three components and not four.** The decomposition is Coase's three costs, each enlarged for B2B. Nothing tests whether a candidate fourth cost is separately addressable. The two candidates a reader will raise are contracting cost proper (legal, procurement, security review, currently folded into bargaining as a formal-body addend) and exit cost (the cost of leaving the incumbent, currently folded into $V_{next\_best}$). *Settled by:* a stated test for separateness. A cost earns its own component only if a seller instrument reduces it without moving the other three.

**2. The bargaining component has no instrument set.** The framework measures it, the [Consensus Friction Calculator](../../practice/consensus-friction-calculator.md), and supplies nothing to reduce it. The incumbent practice, qualification frameworks and multithreading, lives outside the repository. This is the largest gap in the framework and [motions.md](../canon/motions.md) section 2.2 says so. *Settled by:* an instrument derived from Axiom III's per-seat reading of the bargaining cost, which would map each stakeholder's exposure and supply the evidence that resolves it.

**3. The components are causally coupled and the coupling is unmodeled.** Misfit raises the enforcement cost and generates a bargaining cost at the same time, so "which component binds" partly depends on when the reading is taken. The Constitution states the coupling and nothing quantifies it. *Settled by:* a term linking the divergence count to the veto count, or a stated reason to leave them independent.

**4. The division-of-labor corollary predicts an org design it does not describe.** If the standard sales organization is a fixed-direction instrument set, a direction-following organization would look different, and the framework does not say how. *Settled by:* a short derivation of what it means to staff by direction rather than by funnel stage.

**5. Reachability has research and no measurement.** The search component's second blocker, a buyer the seller cannot reach, is backed by [channel-collapse.md](../evidence/channel-collapse.md) and measured by a single addend in the calculator. *Settled by:* a count-based reading of reachability that survives the same scrutiny as the other counts.

**24. Whether direction is vendor-relative.** An incumbent defending a renewal and a challenger attacking it face the same opportunity with different vectors, because the incumbent's enforcement cost is already sunk. The [Deal Triage Calculator](../../practice/deal-triage-calculator.md) scores the deal rather than a seat, which is a decision rather than an oversight: a seat-scored instrument owes the reader an account of how each seat wins, and that account does not exist. Until it does, an incumbent scoring a renewal reads implementation-light for a reason the counts cannot see. *Settled by:* either that account, or a stated rule that the instrument is challenger-relative and a renewal is scored differently.

**25. The count bands are chosen, and nothing tests their shape.** The instrument counts named things, which fixes the ordinal problem the ratings had, and then converts counts to component scores through bands. The counts are observations. The bands are not, and [calibration.md](./calibration.md) records them as chosen. *Settled by:* the same cohort logging that settles item 14, read against realized routing outcomes rather than against close dates.

---

## Axiom II, specificity

**6. The timing claim has no formula.** The second clause, that the pre-signature share of the cost rises with specificity, is stated in prose and tested by one retrospective instrument, the [Friction Efficiency Index](../../practice/friction-efficiency-index.md). The Surplus equation is a snapshot at signature and cannot express it. This was a deliberate choice. *Settled by:* a time split, $F_k = F_k^{pre} + F_k^{post}$, with the pre-signature share as a function of $k$, a model update and a calibration row, when there is a reason to fit one.

**7. The level proxies specificity and conflates it with size.** $k = \lVert \mathbf{F} \rVert_1$ sums all three base costs, but only the enforcement component is specificity in Williamson's sense. A deal with a large search cost and a redeployable product reads as specific when it is merely large. The divergence modifier partly corrects this on the enforcement component alone. *Settled by:* either a specificity reading separate from the level, or an argument that the sum is the right proxy.

**8. Mixed specificity has no joint model.** [seller-surplus.md](../arguments/seller-surplus.md) covers the case where the seller sinks the specific investment. The Constitution covers the buyer. Deals where both sink specific investment, which is the ordinary forward-deployed case, have no model of the joint exposure. *Settled by:* a two-party quasi-rent model and the condition under which mutual exposure is a bond rather than a liability, which section 7.3 of the seller surplus model sketches and does not derive.

**9. Governance form and direction may interact.** The forms are selected by level and frequency. Whether a bargaining-dominant deal wants a different safeguard structure from an enforcement-dominant one of identical level is untested, and [governance-forms.md](../arguments/governance-forms.md) section 7 says there is reason to think it does. *Settled by:* stating what each form safeguards and checking it against each component's pair of parties.

**10. Frequency is three readings by convention.** One-shot, recurring, continuous. Nothing argues the boundaries are real rather than convenient. *Settled by:* a stated variable underneath the readings, such as expected repetitions or the buyer's cost of exit, and the thresholds on it.

**11. The unified-governance boundary has no instrument.** The fourth governance row says the buyer eventually builds it. Nothing reads when. *Settled by:* an instrument that reads the buyer's build alternative, which is $V_{next\_best}$ made observable.

**12. Own the decomposition or cite it.** The Constitution says the B2B enlargements of Coase's three costs are the framework's own. The research files still present the decomposition as inherited. *Settled by:* one pass through [transaction-cost-economics.md](../evidence/transaction-cost-economics.md) to separate what Coase said from what the framework added.

**26. Where the boundary between short and long sits.** $k_{threshold} = 15$ sits at half the instrument's range and nothing but convention puts it there. *Settled by:* a cohort split at several candidate thresholds, checked for whether apparatus deployed above the line earns its cost and apparatus below it does not.

**27. The recurrence claim cannot be falsified on a category that never had a one-shot form.** Section 5 of [governance-forms.md](../arguments/governance-forms.md) predicts that moving a category from perpetual licence to subscription widened the reachable region of the friction space. Software sold as a subscription from the beginning offers no before-and-after, so the test only runs on categories that made the transition. *Settled by:* naming the categories that did, which bounds the claim to a testable population rather than weakening it.

**28. $p_{close}$ has no estimator.** The seller's marginal rule in [seller-surplus.md](../arguments/seller-surplus.md) section 4 turns on $\partial p_{close} / \partial C_{invest}$, and neither term is observed. The nearest available approach is retrospective scoring of closed deals, which carries hindsight bias and would have to be recorded with that status rather than presented as clean. *Settled by:* a deal-record schema that logs the investment made against the outcome, which is a decision about what the organization logs rather than a modelling choice.

**29. $C_{sustain}$ has no budget owner.** The post-signature relationship spend is what holds the incumbent's asymmetry advantage down, per section 7.2 of the seller surplus model, and the framework assigns it to no department. A variable with no owner drifts. *Settled by:* naming the owner, which is an organizational claim the framework has so far avoided making.

**30. $R_{redeploy}$ has no scoring method.** Redeployability is the term separating a good forward-deployed engagement from an expensive one, and `quasi_rent()` in the module takes it as a caller-supplied input for exactly that reason. Inventing a rubric would put a number into a risk review that no document backs. *Settled by:* a scoring method argued from what actually transfers between deals, or a stated decision to keep it a judgment input.

---

## Axiom III, inflation

**13. The bargaining gap the instrument measures is not the one the axiom names.** Axiom III says the bargaining cost is inflated by each stakeholder's uncertainty about their own outcome. The [Deal Triage Calculator](../../practice/deal-triage-calculator.md) measures how many stakeholders have a documented objective the seller can read, which is the seller's uncertainty about them. [models.md](./models.md) section 2.4 records the proxy. *Settled by:* redesigning the consensus block to read each seat's own exposure, or restating the axiom's bargaining row to match what can be observed.

**14. The drift rates are asserted, not derived.** $\gamma_{search}$, $\gamma_{consensus}$ and $\gamma_{implementation}$ are named and not valued. Only the bargaining rate has a discrete field event attached, a departed champion. The other two are asserted continuous. *Settled by:* logging the three gaps at every artifact boundary, which is item 1 of [calibration.md](./calibration.md) section 4.

**15. The coefficient $a$ crosses three boundaries by analogy.** Individual to organizational, laboratory to procurement, dimensionless to annual contract value. The verification-beats-value conjecture rests on it. *Settled by:* item 2 of the calibration page, which is the one estimation problem in the framework with a stated unit.

**16. Reputation depreciation has no rate.** The second clause of the axiom applied after signature has tripwires and no instrument. The [Asymmetry Scorecard](../../practice/asymmetry-scorecard.md) could be re-run at each review and is not. *Settled by:* running it, which section 7.4 of the seller surplus model already proposes.

**17. Two quantities, one instrument, on bargaining.** Incentive variance measures how far apart the stakeholders' interests sit. The bargaining gap measures how much of that can be seen. They enter the cost at different places and the field instrument reads one of them. *Settled by:* the same redesign as item 13.

---

## Standing assumptions

**18. Value exogeneity is strong.** The second standing assumption says the seller cannot move willingness to pay. Positioning and category creation do move perceived value, and the framework absorbs that by calling category definition a search instrument. *Settled by:* a stated boundary between moving $V$ and lowering $F_{search}$, or a weakening of the assumption to "the value lever is weaker than the cost lever," which is what the reduced form argues.

**19. Agency is assumed where it could be derived.** The third standing assumption houses vesting and channel stakes. The neater route, that the seller is also a buying center with its own bargaining cost and the representative is one of its seats, would derive them from Axioms I and III instead. The route is sketched in conversation and nowhere in the repository. *Settled by:* writing the derivation and testing whether it survives.

---

## Cross-cutting

**20. Axioms I and II have no figure.** The model plots value decay and two Axiom III curves. Composition has no picture and neither does the pre-signature share. *Settled by:* a figure sampled from `direction()` in the model for Axiom I, and nothing for Axiom II until item 6 gives it an equation.

**21. Nothing is instrumented.** Every parameter is a reasoned starting value. [calibration.md](./calibration.md) section 4 lists the five things that would change that, in order.

**22. The equation stops at signature.** Drift, renewal and the repeated game are prose in [seller-surplus.md](../arguments/seller-surplus.md) section 7 and the Constitution's Axiom III corollaries. *Settled by:* item 6, since the same time index that carries the pre-signature share would carry the post-signature dynamics.

**23. The notation carries the field names.** Coase's names are canonical in theory and the subscripts read `consensus` and `implementation`. This is a rule rather than a defect, stated in the Constitution, and it will read as a wart to a careful reader. *Settled by:* a decision to rename the subscripts, which is mechanical and touches the model, the tests and every worked example.

---

## Related

- [constitution.md](../canon/constitution.md) — The claims these questions weaken.
- [motions.md](../canon/motions.md) section 9, [governance-forms.md](../arguments/governance-forms.md) section 7 and [seller-surplus.md](../arguments/seller-surplus.md) — Their gaps were folded in here and those sections now point back, so this file is the only prose home.
- [calibration.md](./calibration.md) sections 4 and 5, and [friction-efficiency-index.md](../../practice/friction-efficiency-index.md) sections 6 and 7 — Not folded in. Those record what would make a number empirical and what is wrong inside one instrument's composite, which is narrower than a gap in the theory.
