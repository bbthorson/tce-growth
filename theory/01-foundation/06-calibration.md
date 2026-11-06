---
title: "The Calibration Layer"
layer: theory
status: active
version: 1.0
operationalizes: [axiom-1, axiom-2, axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# The Calibration Layer

**Version:** 1.0
**Purpose:** To hold every number in this framework in one place, so that the structural claims can be read, argued with, and accepted or rejected without any of them.

---

## 1. Why the numbers are quarantined

The framework makes two kinds of claim and they carry very different weight.

**Structural claims** say what depends on what. Using the market costs three things, and any one of them can keep the buyer out. The sale starts at the cost nearest its own threshold. Each party goes ahead only when its own share of today's investment is covered by its own return, and price cancels between the two conditions. What a party sinks exposes it to what it cannot verify or enforce, and the gaps rebuild unless maintained. The costs are non-compensatory, and each has a cost floor set outside the deal. Specificity and frequency select the governance form. These are the framework, they are argued from mechanism, and they are what a reader is being asked to accept.

**Parameters** say how much. Every one of them is a reasoned starting value. None is fitted to booked deal data.

Mixing the two makes the framework weaker than it is. A reader who doubts where a band edge sits should be able to doubt that without doubting that any one cost can keep a buyer out, because the second claim does not depend on the first. Keeping the numbers here is what makes those two positions separable.

> [!IMPORTANT]
> **No value on this page is a measurement.** Read the provenance column before quoting any of them outside this repository, and do not present any of them as an empirical estimate of anything. The framework is currently coherent rather than confirmed, and section 4 says what would change that.

---

## 2. Provenance vocabulary

| Status | What it means |
|---|---|
| **Structurally motivated** | The *shape* follows from a stated argument. A published result constrains the direction or the sign. The specific value does not follow and is chosen inside whatever range the argument allows. |
| **Anchored by analogy** | The magnitude is borrowed from a measured quantity in another domain, as an order-of-magnitude justification. The borrowing does not transfer the original's provenance. |
| **Convention** | A normalizing choice with no empirical content. Setting it to something else rescales the output and changes nothing about the model. |
| **Chosen** | No source. A reasoned starting value and nothing more. |
| **Named, not valued** | The parameter exists in the model and no default is offered, because offering one would read as an estimate. |

---

## 3. Every parameter in the framework

### 3.1 The two conditions, the gaps and future loss ([02-mathematical-models.md](./02-mathematical-models.md))

| Parameter | Symbol | Value | Provenance |
|---|---|---|---|
| Self-serve threshold, per cost | $\tau^{self}_k$ | — | **Named, not valued.** The theory states the threshold exists. The field instrument places it as an edge on each count, section 3.2. |
| Participation threshold, per cost | $\tau^{part}_k$ | — | **Named, not valued.** As above. It marks the buyer's capacity to get through the cost and does not move with value, per section 6 of the math file. |
| Floor on the chance of loss | $\pi_0$ | — | **Named, not valued.** That a floor above zero exists is structurally motivated by the return-variance floor in section 2.3 of the math file. No value is offered. |
| Shape of the chance of loss | — | straight line | **Chosen.** A placeholder between floor and ceiling. No curvature is claimed. |
| How a party's gaps combine | — | arithmetic mean | **Chosen.** No source. |
| Renegotiation split | $\omega$ | 0.5 | **Chosen.** `OMEGA_RENEGOTIATION`. The symmetric split Grossman and Hart (1986) use, with nothing allocated in advance. Section 5.5 of the math file. |
| Future stake at a boundary | $F_{-p}$ | — | **Named, not valued.** What forcing a renegotiation costs the side that forces it. |
| How hold-up and a failed fit combine | — | independent | **Chosen.** Hold-up counts only where the fit did not fail. |
| Shape of discovery cost | — | quadratic | **Chosen.** Diminishing returns to discovery before sinking. Section 5.6 of the math file. |
| Discovery cost scale | $c$ | — | **Named, not valued.** |
| Share of the gap only use reveals | $\rho$ | — | **Named, not valued.** Near zero for a static specification. |
| Drift ceiling | — | 1 | **Convention.** The top of the range every count-based gap is defined on. |
| Component drift rates | $\gamma_{search}$, $\gamma_{consensus}$, $\gamma_{implementation}$ | — | **Named, not valued.** |
| Shape of maintenance | — | proportional to the gap | **Chosen.** Section 5.3 of the math file. |
| Maintenance rate | $\eta_k$ | — | **Named, not valued.** The seller's choice, section 5.7. |
| Cost per unit of maintenance | $c_\eta$ | — | **Named, not valued.** Linear in $\eta$ is chosen. |
| How the chance of non-renewal follows the held gap | — | straight line, as section 5.2 | **Chosen.** |
| Fit drift rates | $\psi_b$, $\psi_s$ | — | **Named, not valued.** Divergent steps opened per period by each side's changes. |
| Technical weight | $w_t$ | 0.6 | **Chosen.** No source. |
| Process weight | $w_p$ | 0.4 | **Chosen.** Fixed by $w_t + w_p = 1$. |
| Tech acceleration exponent | $\phi_t$ | 1.2 | **Structurally motivated.** Convexity follows from Williamson's asset specificity argument. The value does not. |
| Process acceleration exponent | $\phi_p$ | 1.1 | **Chosen.** No source. |
| Return uncertainty sensitivity | $\mu$ | 1.0 | **Convention.** |
| Unvalidated vendor doubt | $\nu$ | 2.0 | **Chosen.** No source. |
| Vendor proof decay | $\kappa$ | 0.5 | **Structurally motivated.** Diminishing returns follow from Spence (1973). The rate does not. |
| Coordination overhead | $\alpha$ | 1.0 | **Convention.** Also the conversion of the bargaining cost into contract value, which nobody has measured. |
| Committee complexity exponent | $\beta$ | 1.35 | **Structurally motivated.** $\beta > 1$ follows from $N(N-1)/2$ channel growth (Cyert and March 1963; Webster and Wind 1972). The value inside $[1.2, 2.0]$ is chosen. |
| Technical overlap weight | $\gamma_{TO}$ | 0.20 | **Chosen.** Field refinement, not core theory. |
| Responsiveness factor | $\gamma_r$ | 0.5 | **Chosen.** Staging logic follows from Dixit and Pindyck (1994). The value does not. |

**Retired in Constitution 4.0.** The reduced form $y = a\hat{\Delta}_A^2 + c$ took three parameters with it: the coefficient $a = 2.25$, anchored by analogy to loss aversion, the convexity exponent, and the base friction growth rate $b$. The Deal Triage Calculator's score bands, level range, Structural boundary, addends, divergence modifier and dominance threshold went when the calculator was rebuilt on positions. [02-mathematical-models.md](./02-mathematical-models.md) section 7 records why. None of them is in the model.

### 3.2 The triage instrument ([Deal Triage Calculator](../../practice/deal-triage-calculator.md))

Every input to this instrument is a count of a named thing, and each count is read against two edges of its own. The edges are where the arbitrariness that counting removed comes back. Each is placed on a boundary of the score bands earlier versions used, so that a reader comparing old and new readings can see where the line moved, and that placement is the only argument behind any of them.

| Cost | Self-serve edge | Participation edge | Provenance |
|---|---|---|---|
| Search, alternatives to rule out | 4 | 8 | **Chosen.** The top of the old 3-to-4 band and the bottom of the old 8-or-more band. |
| Consensus, decision roles that can say no plus any formal body | 1 | 7 | **Chosen.** The old single-veto band and the bottom of the old 7-or-more band. |
| Implementation, integration points plus changed workflows plus undocumented exceptions | 2 | 11 | **Chosen.** The top of the old 0-to-2 band and the bottom of the old 11-or-more band. |

| Parameter | Value | Provenance |
|---|---|---|
| Unnamed category, or no channel | Keeps the buyer out | **Structurally motivated.** An unbounded alternative set and an unreachable seller are argued in step 1a. Neither is a count, so neither has an edge. |
| Expected count | Read against the measured count's edges | **Convention.** The buyer decides on what it expects under Axiom I, and one pair of edges keeps the two readings comparable. |
| Formal body | Counts as one veto | **Convention.** A body holds a veto and is not a person, so it joins the position count and not the evidence denominator. |
| Search evidence items | 4 | **Chosen.** The four questions are argued; the count of them is an artifact of that argument. |

### 3.2a The market reading ([The Market Reading](../../practice/00-market-reading.md))

The reading reuses every edge in section 3.2 and adds one structural count of its own.

| Parameter | Value | Provenance |
|---|---|---|
| Ledger rows | 12 | **Chosen.** The rows are argued from the three components and frequency. The count of them is an artifact of that argument, and the unfilled fraction is a share of it. |
| Unfilled-fraction threshold | none | **Named, not valued.** The fraction is reported. A line needs data from populations entered and populations declined. |
| Missing-capability range | 0 to 4 per component | **Convention.** The four activities below Read in the activity grid. |

### 3.3 The asymmetry scorecard ([Bilateral Asymmetry Scorecard](../../practice/asymmetry-scorecard.md))

| Parameter | Value | Provenance |
|---|---|---|
| Raw gap range | $[2, 10]$ | **Convention.** Two halves each on $[1, 5]$. |
| Normalization | $(\Delta_A - 2) / 8$ | **Convention.** Maps the raw range onto $[0, 1]$, which every equation that takes a gap requires. |
| Dimension mapping | $f \cdot 4 + 1$ | **Convention.** Puts an unevidenced fraction onto the presentation scale. Carries no information the fraction does not. |
| Risk band edges | 4.0, 7.0 | **Chosen.** No source. |
| Commercial hold threshold | 7.0 | **Chosen.** No source. |

### 3.4 Staged commitment ([Milestone Valuation Model](../../practice/milestone-valuation-model.md))

| Parameter | Value | Provenance |
|---|---|---|
| Reference resolution profile | $\mu$ = 0.25, 0.50, 0.80 | **Chosen.** The shape is the argument and the values are illustrative. |
| Reference payment schedule | 0.25, 0.35, 0.40 of annual contract value | **Chosen.** Illustrative. The constraint that matters is that committed payment stays below value realized at every row. |
| Reference sunk amounts | 0.10, 0.25, 0.50 of annual contract value | **Chosen.** Illustrative. The shape, small commitments early and large late, is the argument. |
| Illustrative floor on the chance of loss | 0.05 | **Chosen.** Used only in the worked table. The theory names the floor and does not value it, and nothing in the model ships it as a default. |

### 3.5 Retrospective measures ([Friction Efficiency Index](../../practice/friction-efficiency-index.md))

Weakest layer in the framework, and the only one whose parameters have no argument behind them at all.

| Parameter | Value | Provenance |
|---|---|---|
| Composite weights | 0.35, 0.25, 0.25, 0.15 | **Chosen.** No source. In order ACR, BCV, RMS, SVI. Allocation coverage inherited the weight the effort ratio carried. |
| What makes an allocation | Risk bearer, gate and right to stop, all three | **Chosen.** Mirrors what a Mutual Implementation Plan gate writes down. |
| Committee-size correction | $N^{0.5}$ | **Structurally motivated.** Direction follows from the bargaining cost rising in $N$. The exponent is chosen. |
| Provisioning guard | +1 | **Convention.** Prevents division by zero. |
| Change-order weight | 0.25 | **Chosen.** No source. |
| Buyer commitment reference | 0.5 | **Convention** until twenty closed deals with specific exposure exist, then a trailing median. |
| Minimum credible edge cases | 8 | **Chosen.** No source. |

---

## 4. What would make any of this empirical

The framework becomes predictive rather than organizing when deals are instrumented. Five things, in rough order of how much each one buys.

1. **The three component gaps logged separately** at deal open and at every artifact boundary. This makes the drift rates estimable and tests the framework's central dynamic claim, that discovery moves where the sale starts rather than only lowering every cost. A book of deals whose largest position at close sits on the same cost as at open falsifies it.
2. **Each party's investment and specific exposure logged in contract value** at signature, with the outcome at each renewal. That makes the chance of loss estimable against the gaps, and it is the estimation problem with a stated unit on both sides.
3. **Committee size and stakeholder alignment recorded as structured fields** rather than narrative notes, which makes $\beta$ estimable.
4. **Triggering events dated**, which makes the decay rate observable as the fall in buyer-reported urgency between the event and close.
5. **Count Variance recorded at every Adoption Review**, which is the only check the counting instrument has on itself and the fastest way to learn whether the bands in section 3.2 are the right shape.

Until then, treat every output as a structured comparison between deals inside one book. A deal whose largest position is 1.4 is meaningfully further from closing than one at 0.8. Neither number predicts a close date.

### 4.1 Predictions waiting on data

These were open questions in [07-open-questions.md](./07-open-questions.md). Each is a claim the framework makes, or an objection to one, that only evidence settles, so each stays here until the deals or public records above exist to test it. They keep their numbers because other files cite them by number.

**Axiom I, composition.**

**52. Turnkey erosion may be ordinary diffusion.** The Turnkey falsifier predicts rising vendor counts before falling trial-to-paid conversion and the arrival of sales-assist teams. Diffusion predicts the same sequence for another reason: later adopters are larger organizations with higher bargaining costs, and vendors move upmarket on their own. A test has to hold the adopter's size fixed. Raised by the 6.1 adversarial review.

**55. Hostages should raise close rates at equal verification.** The hold-up wedge in [02-mathematical-models.md](./02-mathematical-models.md) section 1.3 says a deal that creates value can fail where one side fears more hold-up than the other plans, and that a bond, staged fees or an allocated right closes the gap. If deals with those terms close no more often than matched deals without them, at equal verification, the wedge is doing no work. Raised by the 6.1 convergence check.

**53. Sellers who publish their costs choose to.** Axiom I predicts that sellers who publish checkable evidence of their bargaining and policing costs bring more buyers into discovery than matched sellers with the same costs. By the framework's own single-crossing argument, the sellers who publish are the ones whose costs are low, so "matched sellers with the same costs" may not exist. A test needs a publication the seller did not choose, such as a disclosure a regulator required. Raised by the 6.1 adversarial review.

**37. Whether a transaction-cost cutoff is a wall or a penalty.** Axiom I says ease on one cost never buys back another above its threshold. Two-stage choice research supports a screen followed by trade-offs (Gensch 1987, Gilbride and Allenby 2004), but Swait (2001) estimates stated cutoffs as penalties and finds respondents breach them when another attribute compensates. If buyers breach a cost threshold the same way, the gate becomes a steep penalty and the non-compensatory rule weakens. *Settled by:* stated cost thresholds elicited before a decision, then a constrained choice model of the kind Swait fits, estimated on what the same buyers did. A public first pass, proposed by the review: federal (FPDS) and EU (TED) award records note whether a tender used a lowest-price-acceptable rule or a best-value trade-off. If policing cost works as a wall, cancellations should rise with how hard quality is to verify. If it works as a penalty, buyers should switch to trade-off rules and award at a premium instead. Nobody has checked that the records code complexity well enough. [adversarial-review-2026-11.md](../02-research/adversarial-review-2026-11.md).

**3. Whether exposure adds vetoes, and whether a discovered misfit lowers the category's standing.** [02-mathematical-models.md](./02-mathematical-models.md) section 3.5 predicts that the decision roles a deal ends with exceed those mapped at open by the roles its impositions fall on and the approvers its exposure triggers, and that deficiencies add none. The cost floor corollary predicts that a buyer who discovered a misrepresented fit asks more of the next seller in the category. *Settled by:* the veto count logged at open and at each artifact boundary beside the divergent steps found, split into impositions and deficiencies, and, for the second, time to decision and approvers on repeat purchases in a category from a different seller, against buyers with no failed implementation there.

**27. Whether maintenance, fit drift and separation behave as section 5 states.** [02-mathematical-models.md](./02-mathematical-models.md) sections 5.3, 5.7 and 5.8 predict four things. Accounts whose renewal margin is small against the cost of keeping pace get no dedicated account management, and one-shot deals get none at all. Divergent steps found at renewal rise with the changes either side made since go-live, whatever the account's re-verification, and fall where notice of change and an allocated change process were in place. Categories that pool re-separate, through a costlier signal or a shared institution, unless the premium cannot pay for one. And the Turnkey corollary's falsifier: in categories where self-serve selling dominated, a rising vendor count comes before falling trial-to-paid conversion and the arrival of sales-assist teams. *Settled by:* account management coverage against contract value and term, divergent steps logged at go-live and at renewal beside each side's change log, and category histories of vendor count, conversion and the arrival of certifications or standards.

**43. Buyer-side lock-in may hold a Turnkey market without any of the four named protections.** The Turnkey corollary says a standard, a network effect, a dominant brand or a staked channel holds the search cost down as entrants arrive. Procedural switching costs (Burnham, Frels and Mahajan 2003) are specific investment users sink after adoption, so "nothing specific sunk" holds at entry and fails later, and Axiom III then protects the incumbent. Interactive decision aids and AI buying agents may also move the cost of entry onto the seller's discoverability rather than the buyer's search (Häubl and Trifts 2000), which item 35 already asks. *Settled by:* incumbent self-serve retention and trial conversion against entrant density across software categories, split by how much configuration a user sinks. [adversarial-review-2026-11.md](../02-research/adversarial-review-2026-11.md).

**Axiom II, investment.**

**36. Whether markets whose floor keeps buyers out are opened by the dominant seller or an outsider.** [01-motions.md](./01-motions.md) section 6 predicts that a market whose cost floor sits above the participation threshold opens only when someone whose return comes from many deals pays to lower the floor, and rarely through a seller in the middle of the market. Where only the category prior sits above it, a single seller showing its own cost should open it. *Settled by:* category histories that date when buyers began buying at all, against what preceded it: a certification, a standard, a mandate, a marketplace, a contract vehicle, or a dominant seller's investment. The Cures Act certification dates in item 34 are one such record.

**38. The bargaining cost floor mixes statute with internal policy.** The cost floor corollary puts the buyer's institutions under bargaining and decision. Statute fits: state privacy law cut hospital EMR adoption and network effects in a way no single deal could undo (Miller and Tucker 2009, Adjerid et al. 2016). Internal procurement policy may not: private buyers set aside competitive bidding for complex projects (Bajari, McMillan and Tadelis 2009), and suppliers work around a buyer's internal barriers inside one deal (Tuli, Kohli and Bharadwaj 2007). *Settled by:* splitting the floor into external rules and internal policy, then testing whether sponsors waive internal policy as project complexity rises, and whether any seller ever moves the external part within one deal. Item 34's (g)(10) test is the external half. [adversarial-review-2026-11.md](../02-research/adversarial-review-2026-11.md).

**39. Seller absorption of the buyer's investment may have a ceiling.** Axiom II's falsifier assumes that the more of the buyer's investment the seller absorbs, the more often a deal closes. Three findings point the other way past some share: labor raises the builder's valuation (Norton, Mochon and Ariely 2012), sunk effort raises the commitment to finish (Arkes and Blumer 1985), and user participation drives later system use (Sabherwal, Jeyaraj and Chowa 2006). Under Axiom III the buyer's own investment is also its hostage, so full absorption removes it. Allocated rights, the corollary's other remedy, could stand in for that hostage: a buyer that sinks nothing can still be held by a priced right to stop. Such a right protects the seller against the buyer walking away and does nothing for the commitment and use effects above, so if those effects are real the ceiling holds even when the seller is protected. *Settled by:* close rate and twelve-month use by absorption share, comparing a fully seller-funded pilot, a co-invested pilot and buyer-borne implementation. [adversarial-review-2026-11.md](../02-research/adversarial-review-2026-11.md).

**Axiom III, future cost.**

**7. Whether allocation and advance work follow section 5.6.** [02-mathematical-models.md](./02-mathematical-models.md) section 5.6 derives the allocation required from the bond condition and gives the work done in advance a placeholder form. *Settled by:* the test three reviews proposed, extended by the imbalance. Stratify deals by the exposure count and by the imbalance between the parties' sunk investments, randomize front-loaded against modular protocols, and read win rate, deployment and retention together, so that decision paralysis and emergent misfit each have a signature. The forms predict that modular protocols win where much of the misfit surfaces only in use and lose little where the specification is static, and that a deal sunk with its allocation requirement uncovered drifts whatever the protocol. [incomplete-contracts.md](../02-research/incomplete-contracts.md) carries the evidence.

**15. The drift rates are asserted, not derived.** $\gamma_{search}$, $\gamma_{consensus}$ and $\gamma_{implementation}$ are named and not valued. Only the bargaining rate has a discrete field event attached, a departed champion. The other two are asserted continuous. *Settled by:* logging the three gaps at every artifact boundary, which is item 1 above.

**17. Reputation depreciation has no rate.** Axiom III's rebuild clause applied after signature has tripwires and no instrument. The [Asymmetry Scorecard](../../practice/asymmetry-scorecard.md) could be re-run at each review and is not. *Settled by:* running it, which section 7.4 of the seller surplus model already proposes.

**19. Axiom III's uncertainty half inherits the weakest empirical result in transaction cost economics.** Meta-analyses of the record (David and Han 2004, Carter and Hodgson 2006, Geyskens, Steenkamp and Kumar 2006) find that specificity predicts governance reliably, that uncertainty predicts it weakly and inconsistently, with trust and joint problem-solving often substituting for formal safeguards, and that specificity is usually measured with subjective scales. Axiom III now carries both results: its specificity half sits on the strong one and its uncertainty half on the weak one. The counting instruments were built against the measurement critique. *Settled by:* counts validated against outcomes across a book of deals, and a stated account of when relational norms substitute for the instruments. [tce-empirical-record.md](../02-research/tce-empirical-record.md).

**33. Who drifts first after signature.** The enforcement corollary runs in both directions and makes no claim about which party's incentives move first, buyer or seller, or whether it depends on which side sank more. *Settled by:* a book of post-signature relationships coded for which party's conduct changed first, against each side's sunk specific investment.

**40. Which enforcement remedy works in software deals.** Renegotiation design (Aghion, Dewatripont and Rey 1994) and simple option contracts (Nöldeke and Schmidt 1995) induce efficient specific investment when information is observable to both parties and unverifiable to a court, which is the corollary's own setting. The enforcement corollary therefore names two remedies, hostages and rights allocated in advance, where it first named hostages alone. What stays open is which works better where. Two results complicate both: when investment is cooperative, ex ante contracts may be worth nothing (Che and Hausch 1999), and fixed-price software contracts are often renegotiated after the fact (Banerjee and Duflo 2000), which bears on item 7. *Settled by:* comparing dispute and termination rates for option, hostage, fixed-price and time-and-materials contracts in high-specificity software deals. The review proposes two public sources: the material contracts companies file as Exhibit 10 to SEC filings, and federal IT contract records in FPDS, coded by governance form and joined to dispute and termination records. Nobody has checked that either records what the coding needs. [adversarial-review-2026-11.md](../02-research/adversarial-review-2026-11.md).

**41. Liability may do what the framework credits to verification.** The levers table in [02-mathematical-models.md](./02-mathematical-models.md) section 1.3 says verification raises the joint surplus by lowering $\pi_p$. In a laboratory credence-goods market, liability drove efficiency and verifiability had a minor effect (Dulleck, Kerschbamer and Sutter 2011). If enterprise software behaves the same way, hostages and outcome liability carry more weight than verification. *Settled by:* deals matched on specificity, comparing outcome-liability terms with verification pilots on realized value and renewal. [adversarial-review-2026-11.md](../02-research/adversarial-review-2026-11.md).

**Standing assumptions.**

**22. Opportunism as a design premise may be self-fulfilling.** Ghoshal and Moran (1996) argue that governance designed around the assumption of opportunism produces the opportunism it assumes. The third standing assumption is marked descriptive, and the decision-role ledger records each occupant's reservation and the arrangement's answer rather than a verdict, which is the cooperative reading built into an instrument. Nothing tests that the cooperative reading holds in use. *Settled by:* whether reservation-based ledgers outperform defensive safeguards on comparable deals. [tce-empirical-record.md](../02-research/tce-empirical-record.md). Arikan (2020) adds that parties judge the intent behind a governance act, so a probe of private vulnerability reads as opportunism however it is framed, which is why the bargaining ledger's diagnosis is private and only the arrangement is shared.

**32. Preferences may be constructed during evaluation.** Constitution 5.0 splits value into realizable, recognized and realized, and says the seller moves only the recognized estimate for a given offer. The strongest objection is that preferences for unfamiliar, complex purchases are built during the evaluation itself (Payne, Bettman and Schkade 1999), so realizable value may have no stable referent before the sale, and a reframe changes both the estimate and, through adoption effort, the value. The adoption channel is priced as buyer investment under Axiom II, and post-sale disconfirmation measures preferences experience reveals, but neither reply settles it. The falsifier in that file also has a selection problem. A buyer shares its own data mostly with a seller it already buys from, so in any running seller's sample the claims verified on the buyer's own data come mostly from the seller's existing accounts, and the asserted claims mostly from new ones. The comparison has to be made within each group, new accounts against new accounts and existing against existing. *Settled by:* evidence on whether anchoring and framing move the realized value of enterprise purchases, not only stated estimates and prices. [value-and-persuasion.md](../02-research/value-and-persuasion.md).

**Cross-cutting.**

**28. Whether occupants will state reservations one to one at the rate the metric needs.** An external review established, against corporate sociology and bargaining theory, that occupants will not write personal exposure on a seller-held document, and the bargaining ledger split into a private decision-role map and a shared arrangement record in response. *Settled by:* running the decision-role map on live deals and counting the decision roles whose occupant stated a reservation privately against those the seller inferred, and the share of arrangement records the buyer ratified.

**35. Whether AI buying agents break the link between entry and the search cost floor.** The Turnkey corollary says entry raises the search cost. Agents that search, negotiate and transact for a buyer could screen vendors so that more entrants need no more buyer effort (Shahidi et al. 2025). Turnkey erosion would then run through pooled policing signals rather than search. *Settled by:* buyer search effort per purchase tracked against vendor count in categories where agent-mediated buying is common and where it is not.

**42. Health tech may be a biased home case.** Health tech has statutory cost floors, a buyer split across clinicians, patients, administrators, payers and regulators (Herzlinger 2006), and outcomes that are hard to attribute. Under fee-for-service a tool that removes duplicate tests cuts the hospital's billed revenue, which is a negative $V_{switch}$ and not a cost above its threshold, and EMR adoption raised hospital costs for years outside IT-intensive labor markets (Dranove, Forman, Goldfarb and Greenstein 2014). A framework calibrated there may read value problems as bargaining thresholds and overstate cost floors elsewhere. *Settled by:* a triage step that separates $V_{switch} \le 0$ from $r_k > 1$, and the same readings taken in a commercial B2B software market without statutory floors. [adversarial-review-2026-11.md](../02-research/adversarial-review-2026-11.md).

---

## 5. Known defects in this layer

Recorded rather than fixed, because each fix means choosing a shape and that is a decision rather than a repair.

**The edges reintroduce what counting removed.** The instrument counts named things, which fixes the ordinal problem at the input, and since Constitution 4.0 it no longer converts them to scores. Each count is still read against two chosen edges, so a position is only as defensible as the edges behind it. The step functions are gone and the edges remain.

**The zone edges are cliffs.** A count one below an edge and a count one above it land in different zones. The dominance threshold carried the same defect and is gone. The zone edges carry it in a weaker form, because where the sale starts is read from positions, which are continuous, and only the zone label jumps.

**The shape of the chance of loss is not identified.** The straight line between floor and ceiling is a placeholder, and nothing in the framework distinguishes it from any other increasing form. Constitution 3.0 carried the same defect as an unidentified convexity exponent on the retired reduced form.

**The Friction Efficiency Index composite carries two open defects of its own**, recorded in section 6 of that file. They are defects in the measure rather than in its parameters, so they are not repeated here.

---

## Related

- [00-tcg-constitution.md](./00-tcg-constitution.md) — The structural claims, which are stated without reference to any value on this page.
- [02-mathematical-models.md](./02-mathematical-models.md) — The functional forms these parameters sit inside.
- [citation-provenance-audit.md](../02-research/audits/citation-provenance-audit.md) — The companion for headline statistics, on the same discipline. That file traces numbers cited from outside; this one traces numbers chosen inside.
- [models/README.md](../../models/README.md) — Why nothing here is fitted, and what fitting to synthetic data would cost.
