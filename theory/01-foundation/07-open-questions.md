---
title: "Open Questions"
layer: theory
status: active
version: 1.1
operationalizes: [axiom-1, axiom-2, axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# Open Questions

**Version:** 1.1
**Purpose:** To record, in one place, where the theory is under-developed now that the axioms are fixed. Each entry says what the framework claims, what it lacks, and what would settle it. Entries are grouped by the axiom they weaken.

This register consolidates. Where a file already carries its own "what this does not settle" section, the entry here points at it rather than restating it. An entry leaves this file when the work is done or when the claim is withdrawn, and either exit is recorded in the Constitution's version history. Item numbers are stable, because other files cite them, so a closed number is not reused. The items Constitution 4.0 closed are listed at the end.

---

## Axiom I, composition

**1. Why three costs and not four.** The decomposition is Dahlman's three costs, each enlarged for B2B. Nothing tests whether a candidate fourth cost is separately addressable. The two candidates a reader will raise are contracting cost proper (legal, procurement, security review, currently folded into bargaining as a formal-body addend) and exit cost (the cost of leaving the incumbent, currently folded into $V_{next\_best}$). *Settled by:* a stated test for separateness. A cost earns its own place only if a seller investment reduces it without moving the other two.

**2. The bargaining cost has no instrument set.** The framework measures it, the [Consensus Friction Calculator](../../practice/consensus-friction-calculator.md), and supplies nothing to pay it down. The incumbent practice, qualification frameworks and multithreading, lives outside the repository. This is the largest gap in the framework and [01-motions.md](./01-motions.md) says so. *Settled by:* an instrument derived from Axiom III's per-decision-role reading of the bargaining gap, which would map each decision role's exposure and supply the evidence that resolves it. [08-from-axioms-to-instruments.md](./08-from-axioms-to-instruments.md) sections 4 and 5 derive what the instrument must do and the decision-role ledger it runs on. The instrument itself is still owed.

**3. The costs are causally coupled and the coupling is unmodeled.** Misfit raises the policing cost and creates a bargaining cost at the same time, so where the sale starts partly depends on when the reading is taken. The Constitution states the coupling and nothing quantifies it. *Settled by:* a term linking the divergence count to the veto count, or a stated reason to leave them independent. Until then, the Constitution's falsifier for Axiom I, that deals whose first seller investment went to the cost with the largest position convert no faster than matched deals, is read on positions taken at one stated moment.

**4. The division-of-labor corollary predicts an org design it does not describe.** If the standard sales organization meets the three costs in a fixed order, an organization that meets each deal at the cost where its sale starts would look different, and the framework does not say how. *Settled by:* a short derivation of what it means to staff by where the sale starts rather than by funnel stage. [08-from-axioms-to-instruments.md](./08-from-axioms-to-instruments.md) section 2.1 derives half of it from Axiom II's cost-to-serve corollary: a motion is a decision about which cost an organization is built to pay down. The staffing consequence is still owed.

**5. Reachability has research and no measurement.** The search cost's second blocker, a buyer the seller cannot reach, is backed by [channel-collapse.md](../02-research/channel-collapse.md) and read in the [Deal Triage Calculator](../../practice/deal-triage-calculator.md) as a yes or no: a missing channel puts search in the keeps-out zone whatever the count. *Settled by:* a count-based reading of reachability that survives the same scrutiny as the other counts.

**6. The market reading has a draft and no worked case.** Axiom I's motion is chosen across a buyer population, and Axiom II's pursuit corollary decides whether to enter it, which are organizational decisions. Without a reading of the population, the choice of motion is made by imitation, the organization-level failure the Constitution names. [08-from-axioms-to-instruments.md](./08-from-axioms-to-instruments.md) section 2.1 derives what the reading must contain, and [The Market Reading](../../practice/00-market-reading.md) is its first draft: each cost's position across the population, where the sale starts, the exposure reading, the seller's cost to serve by cost, and pursue, restructure or decline. *Settled by:* a worked scenario on two anonymized EHR-integration populations, and a book of deal readings checked against the market reading they sit under.

---

## Axiom II, investment

Constitution 4.0 made investment an axiom of its own, and no entry has been filed against it yet. Items 7 to 13 were filed here when Axiom II carried specificity, and they now sit under Axiom III with their numbers unchanged.

---

## Axiom III, future cost

**7. The allocation clause has no formula.** Axiom III says the allocation of a specific deal must be settled before the investment is sunk, and that the share of the arrangement settled in advance rises with specificity. Staging has a formula, the expected loss summed over gates in [02-mathematical-models.md](./02-mathematical-models.md) section 5.4. The rising share does not. It is stated in prose and tested by one retrospective instrument, the [Friction Efficiency Index](../../practice/friction-efficiency-index.md), which measures spend rather than allocation. Three reviews established the moderator: what can be done in advance falls as uncertainty rises, because misfits in roles, controls and culture surface only in use, while what can be allocated does not, and front-end definition pays directly only where the specification is static (Merrow, Gibson). *Settled by:* a time split of each investment into the part made before the specific investment is sunk and the part made after, with the allocated share as a function of the quasi-rent and the spent share as a function of the quasi-rent and uncertainty, a model update and a calibration row, when there is a reason to fit one. The decisive test stratifies deals by the exposure count, randomizes front-loaded against modular protocols, and reads win rate, deployment and retention together, so that decision paralysis and emergent misfit each have a signature. [incomplete-contracts.md](../02-research/incomplete-contracts.md) carries the evidence.

**9. Joint exposure has a form and no bond condition.** The two conditions now carry each party's own future loss, $L_b = Q_b \pi_b$ and $L_s = Q_s \pi_s$, so a deal where both sink specific investment, the ordinary forward-deployed case, can be written down. What is missing is the condition under which mutual exposure is a bond rather than a liability, which section 7.3 of [04-seller-surplus-model.md](./04-seller-surplus-model.md) sketches and does not derive. *Settled by:* that condition, stated in terms of the two quasi-rents.

**10. Governance form and where the sale starts may interact.** The forms are selected by specificity and frequency. Whether a deal whose sale starts at bargaining wants a different safeguard structure from one that starts at policing, with the same specific exposure, is untested, and [05-governance-forms.md](./05-governance-forms.md) section 7 says there is reason to think it does. *Settled by:* stating what each form safeguards and checking it against each cost's pair of parties.

**11. Frequency is three readings by convention.** One-shot, recurring, continuous. Nothing argues the boundaries are real rather than convenient. *Settled by:* a stated variable underneath the readings, such as expected repetitions or the buyer's cost of exit, and the thresholds on it. Constitution 2.4 proposed the buyer's cost of exit at the next boundary and 3.0 withdrew it, for the reasons [05-governance-forms.md](./05-governance-forms.md) section 7 records. 4.0 keeps mutual sanction as what frequency buys, so the mutual stake at each boundary is the next candidate for the variable underneath.

**12. The unified-governance boundary has no instrument.** The fourth governance row says the buyer eventually builds it. Nothing reads when. *Settled by:* an instrument that reads the buyer's build alternative, which is $V_{next\_best}$ made observable.

**14. The bargaining gap the instrument measures is not the one the axiom names.** Axiom III says the bargaining gap is each decision role's uncertainty about its own outcome. The [Deal Triage Calculator](../../practice/deal-triage-calculator.md) measures how many decision roles have a documented objective the seller can read, which is the seller's uncertainty about them. [02-mathematical-models.md](./02-mathematical-models.md) section 2.4 records the proxy. *Settled by:* redesigning the consensus block to read each decision role's own exposure, or restating the axiom's bargaining row to match what can be observed. [08-from-axioms-to-instruments.md](./08-from-axioms-to-instruments.md) section 2.2 states the gap at the level of the claim, as the share of decision roles whose occupant has stated their own exposure, so the instrument follows the axiom. The instrument is still owed.

**15. The drift rates are asserted, not derived.** $\gamma_{search}$, $\gamma_{consensus}$ and $\gamma_{implementation}$ are named and not valued. Only the bargaining rate has a discrete field event attached, a departed champion. The other two are asserted continuous. *Settled by:* logging the three gaps at every artifact boundary, which is item 1 of [06-calibration.md](./06-calibration.md) section 4.

**17. Reputation depreciation has no rate.** Axiom III's rebuild clause applied after signature has tripwires and no instrument. The [Asymmetry Scorecard](../../practice/asymmetry-scorecard.md) could be re-run at each review and is not. *Settled by:* running it, which section 7.4 of the seller surplus model already proposes.

**18. Two quantities, one instrument, on bargaining.** Incentive variance measures how far apart the decision roles' interests sit, and it sets the size of today's bargaining cost. The bargaining gap measures how much of their own exposure each role can see, and it feeds the chance of future loss. They enter different terms of the two conditions, and the field instrument reads one of them. *Settled by:* the same redesign as item 14. [08-from-axioms-to-instruments.md](./08-from-axioms-to-instruments.md) section 2.2 carries the statement both readings follow.

**19. Axiom III's uncertainty half inherits the weakest empirical result in transaction cost economics.** Meta-analyses of the record (David and Han 2004, Carter and Hodgson 2006, Geyskens, Steenkamp and Kumar 2006) find that specificity predicts governance reliably, that uncertainty predicts it weakly and inconsistently, with trust and joint problem-solving often substituting for formal safeguards, and that specificity is usually measured with subjective scales. Axiom III now carries both results: its specificity half sits on the strong one and its uncertainty half on the weak one. The counting instruments were built against the measurement critique. *Settled by:* counts validated against outcomes across a book of deals, and a stated account of when relational norms substitute for the instruments. [tce-empirical-record.md](../02-research/tce-empirical-record.md).

**31. The Friction Efficiency Index rewards work done before signature.** Its reference band for the friction allocation ratio, 0.60 to 0.75, scores an organization by the share of implementation effort spent before signature. Axiom III asks only that the *allocation* of a specific investment be settled before it is sunk, and says the work done in advance can fall as uncertainty rises, because misfit surfaces in use. A band that rewards pre-signature work may reward forcing discovery that only use can do. *Settled by:* re-deriving the ratio's target from the allocation clause, or measuring allocation directly, in the [Friction Efficiency Index](../../practice/friction-efficiency-index.md).

---

## Standing assumptions

**20. Value exogeneity is strong.** The second standing assumption says the seller cannot move willingness to pay. Positioning and category creation do move perceived value, and the framework absorbs that by calling category definition a search instrument. *Settled by:* a stated boundary between moving $V$ and lowering $F_{search}$, or a weakening of the assumption to "the value lever is weaker than the cost lever."

**21. Agency is assumed where it could be derived.** The third standing assumption houses vesting and channel stakes. The neater route, that the seller is also a buying center with its own bargaining cost and the representative holds one of its decision roles, would derive them from Axioms I and III instead. The route is sketched in conversation and nowhere in the repository. *Settled by:* writing the derivation and testing whether it survives.

**22. Opportunism as a design premise may be self-fulfilling.** Ghoshal and Moran (1996) argue that governance designed around the assumption of opportunism produces the opportunism it assumes. The third standing assumption is marked descriptive, and the decision-role ledger records each occupant's reservation and the arrangement's answer rather than a verdict, which is the cooperative reading built into an instrument. Nothing tests that the cooperative reading holds in use. *Settled by:* whether reservation-based ledgers outperform defensive safeguards on comparable deals. [tce-empirical-record.md](../02-research/tce-empirical-record.md). Arikan (2020) adds that parties judge the intent behind a governance act, so a probe of private vulnerability reads as opportunism however it is framed, which is why the bargaining ledger's diagnosis is private and only the arrangement is shared.

---

## Cross-cutting

**23. Axioms I and II have no figure.** The Constitution plots value decay under the second standing assumption and drift under Axiom III. Where the sale starts has no picture, and neither do the two conditions. *Settled by:* a figure sampled from `threshold_position()` in the model for Axiom I, showing three costs each against its own two thresholds, and one sampled from the two conditions for Axiom II.

**24. Nothing is instrumented.** Every parameter is a reasoned starting value. [06-calibration.md](./06-calibration.md) section 4 lists the five things that would change that, in order.

**27. The gaps have drift rates and no equilibrium.** Each gap rebuilds toward its ceiling at $\gamma_k$, and the Constitution draws a maintained curve and an unmaintained one without stating the condition between them. Two equilibria are implied and neither is written. Per deal, a steady state where the seller's maintenance spend matches the rebuild. Per market, Spence's separating equilibrium, where the marginal costly signal just separates. Constitution 4.0 now names the mechanism that moves a market off it: the Turnkey corollary says entry raises the search cost, because every entrant is another alternative to rule out, and raises the policing cost through pooling, because free trials and identical claims stop separating good sellers from bad. That is the slide back to pooling this entry recorded as missing. What is still unwritten is the condition itself, and the split of the search cost's response to information by verifiability: falling in verifiable information, rising in unverifiable. *Settled by:* a stated equilibrium condition in the drift section, and the entry corollary's falsifier tested: in categories where self-serve selling dominated, a rising vendor count comes before falling trial-to-paid conversion and the arrival of sales-assist teams.

**28. Whether occupants will state reservations one to one at the rate the metric needs.** An external review established, against corporate sociology and bargaining theory, that occupants will not write personal exposure on a seller-held document, and the bargaining ledger split into a private decision-role map and a shared arrangement record in response. *Settled by:* running the decision-role map on live deals and counting the decision roles whose occupant stated a reservation privately against those the seller inferred, and the share of arrangement records the buyer ratified.

**29. The deal reading has no mandate variable.** Implementation research finds that setting-level variables, sponsorship, capital and absorptive capacity, predict adoption better than individual characteristics, and a purchase stalls when the mandate dissolves whatever the decision roles say. The Constitution's definition of a decision role now separates an occupant change from the dissolution of a role when the mandate leaves with the person, and the framework reads the catalyst under the second standing assumption. Nothing reads whether the mandate still stands between them. *Settled by:* a mandate reading in the deal instrument, taken apart from the decision roles and re-taken at every occupant change.

---

## Closed since 4.0

- **8. The level conflated specificity with size.** The summed level retired, and specific exposure is now read on its own count, in Step 2 of the [Deal Triage Calculator](../../practice/deal-triage-calculator.md).
- **16. The coefficient $a$ crossed three boundaries by analogy.** It retired with the reduced form it sat in, and the case for verification over discounting now follows from price cancelling between the two conditions.
- **25. The equation stopped at signature.** The two conditions carry each party's expected future loss, its rebuild and its staging over gates, and recurrence enters through price and delivery cost summed over renewals. What remains of the time index is item 7.
- **26. The notation carried the field names.** 4.0 decided to keep the field subscripts, and the Constitution states why: the field names say what a seller experiences and Dahlman's say what the cost is.
- **13. The research file presented the decomposition as inherited.** [transaction-cost-economics.md](../02-research/transaction-cost-economics.md) now credits Coase with the question, Dahlman with the three costs and Williamson with the split by time, and names what the framework adds.
- **30. Whether the participation threshold rises with the value at stake.** Settled after 4.0, on 2026-10-09: it does not. The threshold marks the buyer's capacity to get through a cost, and value lives in the buyer's condition, where a bigger prize funds the investment that pulls a cost back under the threshold. [02-mathematical-models.md](./02-mathematical-models.md) section 6 carries the argument and its falsifier.

---

## Related

- [00-tcg-constitution.md](./00-tcg-constitution.md) — The claims these questions weaken, and the version history that records each exit.
- [01-motions.md](./01-motions.md), [05-governance-forms.md](./05-governance-forms.md) section 7, [04-seller-surplus-model.md](./04-seller-surplus-model.md) open questions, [06-calibration.md](./06-calibration.md) section 5 — The file-local registers this one points at.
