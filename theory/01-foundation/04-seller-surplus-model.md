---
title: "Seller Surplus and the Implementation Investment"
layer: theory
status: active
version: 1.0
operationalizes: [axiom-2]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# Seller Surplus and the Implementation Investment

**Version:** 1.0
**Purpose:** To specify the seller's side of the transaction, so that "should we invest engineering in this deal, and how much" becomes a question the framework can express.

The [Constitution](./00-tcg-constitution.md) models one party. Its Surplus equation describes what the *buyer* gains and what the *buyer* pays. The seller appears throughout as the agent who reduces the buyer's friction, and nowhere as a party with costs of its own.

That omission is invisible while the motion is advisory. It becomes binding the moment the seller deploys engineers into a buyer's environment before signature, because the seller is then sinking capital that no term of the buyer's equation accounts for.

This document adds the second equation. Axiom II names which party bears the asset specificity, which is the claim section 3 depends on.

---

## 1. Why the Surplus equation cannot answer the question

Part III of the Constitution gives:

$$S = \left(V_{effective}(t) - V_{next\_best}\right) - F_{effective}$$

Every term describes the buyer. $F_{effective}$ is the friction the buyer bears. $\Delta_A$ inflates the buyer's perceived cost. $c$ is the price the buyer pays, which is the seller's revenue rather than the seller's cost.

A seller reading this equation learns whether the deal *can* close. It cannot tell them whether the deal is *worth closing*, because nothing in it moves when the seller spends more or less to close it. Asking "should I invest in implementation" of the Surplus equation is asking a question in a language that has no word for it.

---

## 2. The seller's surplus

*Before signature. Sections 2 through 5 govern the single transaction up to signature.*

$$S_{seller} = p_{close} \cdot \left(V_{contract} - C_{deliver}\right) - C_{invest}$$

| Term | Meaning |
|---|---|
| $p_{close}$ | Probability the deal closes, given the investment made |
| $V_{contract}$ | Contract value the seller receives |
| $C_{deliver}$ | Post-signature cost to deliver what was sold |
| $C_{invest}$ | Pre-signature, deal-specific engineering. Spent whether or not the deal closes |

The structure of the asymmetry sits in the last two rows. $C_{deliver}$ is contingent: it is incurred only against revenue. $C_{invest}$ is not. It leaves the building before anyone signs, and it leaves whether $p_{close}$ resolves to one or to zero.

**Both parties are subject to a boundary, and both must clear it.** The Constitution's condition $S > 0$ governs whether the buyer will transact. $S_{seller} > 0$ governs whether the seller should want them to. A deal sitting comfortably inside the buyer's potential well can sit outside the seller's, and the seller who closes it has done accretive work for the customer and dilutive work for their own firm.

---

## 3. What is actually at risk

$C_{invest}$ overstates the exposure. The correct measure is the appropriable quasi-rent:

$$Q = C_{invest} - R_{redeploy}$$

Where $R_{redeploy}$ is the value of that work redeployed elsewhere: reusable connectors, a reference architecture, domain knowledge that transfers to the next deal in the segment. Research backing is in [klein-crawford-alchian.md](../02-research/klein-crawford-alchian.md).

$Q$ is the amount a buyer can extract by threatening to walk after the engineering is spent, and it is the number that belongs in a risk review. Two engagements consuming identical hours carry different exposure when one produces a connector the seller ships to every subsequent customer and the other produces a mapping to a schema that exists in exactly one hospital.

**This inverts the axiom's usual direction.** Axiom II treats asset specificity as the buyer's problem, solved by governance the seller supplies. In a forward-deployed motion the seller sinks the specific investment first, so the seller holds the exposure and needs the governance. The Mutual Implementation Plan already provides it. Its stated rationale covers only one direction.

---

## 4. The investment decision

Differentiating $S_{seller}$ with respect to $C_{invest}$ gives the marginal rule:

$$\frac{\partial p_{close}}{\partial C_{invest}} \cdot \left(V_{contract} - C_{deliver}\right) > 1$$

Spend the next increment while a unit of pre-signature engineering raises the close probability enough that the expected gross margin gain exceeds the unit spent. Stop when it does not.

**Why the left side is ever large enough to justify the spend.** $C_{invest}$ enters the buyer's equation by two routes at once. It reduces $\Delta_A$, because deployed engineering is a demonstration a weak competitor cannot afford to imitate, which is the Single Crossing Property from Axiom III. It also reduces the buyer's $F_{implementation}$ directly, because work the seller performs is work the buyer does not. Both raise $S_{buyer}$, and $p_{close}$ rises with $S_{buyer}$.

This is the only lever that appears on both sides of the transaction, which is what makes it worth modeling separately from price. Discounting moves $c$ and leaves $\Delta_A$ untouched.

**The exposure constraint runs alongside the marginal rule.** Unprotected quasi-rent at any moment must stay inside what a failed deal can cost the firm. A deal can satisfy the marginal rule at every increment and still be wrong to pursue, when the accumulated $Q$ before the buyer commits anything exceeds what the seller can absorb. Sequencing is what reconciles the two, which is section 5.

---

## 5. Staged investment: the mirror of the milestone model

The [Milestone Valuation Model](../../practice/milestone-valuation-model.md) stages the buyer's payments so the buyer never carries more committed cost than the stage has de-risked. The seller's engineering spend needs the same treatment in the other direction: each tranche of $C_{invest}$ gates on a buyer commitment that reduces the seller's unprotected $Q$.

The buyer-side rule "payment follows proof, not calendar" has a seller-side twin: **engineering follows commitment, not optimism.** A tranche released against a date, a verbal assurance, or a forecast category converts a staged investment back into an unconditional one, which removes the protection the staging existed to provide.

Rule 3 of the milestone model already requires symmetric consequence when a stage fails on seller execution. The symmetric obligation is unwritten: what the buyer forfeits when a stage fails on buyer execution, whether that is data access never granted, stakeholders never convened, or an environment never provisioned.

---

## 6. Calibration status

> [!IMPORTANT]
> **Nothing here is fitted.** $p_{close}$ is not directly observable, and $\partial p_{close} / \partial C_{invest}$ cannot be estimated without a record of deals carrying both the investment made and the outcome. No such record exists in this repository. Treat these forms as a way to structure the decision and to name what a reviewer should ask for, not as a way to forecast a number. The same caution governs [02-mathematical-models.md](./02-mathematical-models.md) and applies here with more force, because this model has no parameter anchored in published literature at all.

The practical consequence: a manager can use section 4 to ask "what would have to be true about $\partial p_{close} / \partial C_{invest}$ for this spend to make sense," and can compare that answer against experience. That is a real use. Producing a number and calling it a probability is not.

The same caution governs section 7, where $r_t$ is no better observed than $p_{close}$ and the discount rate is a policy choice rather than a measurement.

---

## 7. The repeated game

*After signature.*

Sections 2 through 4 describe a single transaction. Subscription businesses do not have those. The contract renews, the seller keeps spending on the relationship, and Net Revenue Retention is the outcome of a sequence rather than of a close.

$$S_{seller} = \sum_{t=1}^{T} \frac{r_t \left(V_t - C_{deliver,t} - C_{sustain,t}\right)}{(1+\rho)^t} - C_{invest}$$

| Term | Meaning |
|---|---|
| $r_t$ | Probability the relationship is live in period $t$. $r_1$ is $p_{close}$ |
| $C_{sustain,t}$ | Ongoing relationship investment in period $t$. Distinct from delivery |
| $\rho$ | Discount rate applied to future periods |

The single-shot form in section 2 is this expression with $T = 1$ and $C_{sustain} = 0$. Two consequences follow immediately, and the first is a correction.

**$C_{invest}$ amortizes across the stream, not against the first contract.** The marginal rule in section 4 used first-year gross margin. That is the right test only when $r_t$ collapses quickly. The [Deal Triage Calculator](../../practice/deal-triage-calculator.md) once ruled the implementation-led region out whenever pre-sale cost exceeded first-year gross margin. Read literally that is a single-shot test, and it disqualifies deals that a durable relationship would justify, which is why its decline conditions now state the test as level against frequency.

**$C_{sustain}$ is not overhead.** It is the spend that holds $r_t$ up, and section 7.2 says what it actually buys.

### 7.1 Two mechanisms with opposite signs

A forward-deployed engagement is often defended on the grounds that it raises the buyer's switching cost. That defence has a problem inside this framework.

Switching cost is a **lock-in** mechanism, and lock-in raises the seller's temptation payoff $T$ in the cooperation condition $\delta_{discount} > (T - R)/(T - P)$. A buyer who cannot leave can be repriced and under-served. Raising $T$ raises the threshold the seller's own discount factor must clear, so the arrangement becomes harder to sustain exactly as the seller's position strengthens. This is the extraction drift Axiom II describes for channels and adjudicators, arriving at the deal level.

The buyer prices this at signature. A buyer who anticipates lock-in is losing the option to exit, and [real-options.md](../02-research/real-options.md) says that option carries real value. So switching cost raises $\Delta_A$ and $y$ before the seller has delivered anything.

**Switching cost is a liability at signature and an asset at renewal.** Any account of it that carries only one sign is describing half the mechanism.

### 7.2 What actually defends the position

The durable asset is not lock-in. It is **asymmetric $\Delta_A$**.

After a forward-deployed engagement the incumbent's $I_{seller}$ approaches zero, because the environment has been mapped. Every challenger begins at close to maximum. The buyer's renewal decision compares $y$ with the incumbent against $y$ with a challenger, and the challenger's figure carries a full $F_{implementation}$ amplified by an asymmetry gap nobody has closed yet.

That is an information asset rather than a hostage. The buyer is not trapped, the alternative is genuinely more expensive, and the buyer can verify the comparison themselves. It also produces the renewal behaviour the lock-in story predicts, without raising $T$.

**It decays at a rate the Constitution already names.** $\hat{\Delta}_k(t) = \hat{\Delta}_k(0) + \gamma_k t$ absent maintenance. The rate that runs on staff turnover, workflow change, and systems the seller never saw installed is $\gamma_{implementation}$ specifically, which is the component an incumbent's advantage actually sits in. $C_{sustain}$ is the spend that holds it down. Net Revenue Retention is therefore not a separate mechanism. It is the asymmetry drift equation run past signature, on one component of three.

The erosion is invisible until a challenger appears, which is the same structure as Reputation Depreciation under Axiom II. A seller who stops paying $C_{sustain}$ keeps the revenue and loses the moat, and learns which happened at the renewal after next.

### 7.3 Why $Q$ appears twice

Section 3 defines $Q = C_{invest} - R_{redeploy}$ as the seller's exposure: work that cannot be redeployed is what a buyer can appropriate by threatening to walk.

In the repeated game the same quantity does the opposite job. Work that cannot be redeployed means the seller loses badly if the relationship ends, which is a credible bond rather than a liability. Mutual specific investment is the joint-ownership remedy in [klein-crawford-alchian.md](../02-research/klein-crawford-alchian.md): neither party defects when both have sunk something they cannot recover.

So a forward-deployed motion raises the seller's temptation $T$ and the seller's bond $Q$ at the same time. **The relationship is healthy while $Q$ grows at least as fast as $T$.** That is the condition to watch, and it is why the defensible account of the motion is not that the buyer is locked in but that both parties now have more to lose.

### 7.4 The leading indicator

[game-theory-and-nrr.md](../02-research/game-theory-and-nrr.md) states that Net Revenue Retention is a lagging indicator, and it lags by a full renewal cycle. Section 7.2 supplies a leading one: the incumbent's asymmetry gap, which erodes continuously and is measurable at any point.

The instrument already exists. The [Asymmetry Scorecard](../../practice/asymmetry-scorecard.md) measures $\Delta_A$, and nothing currently runs it after signature. Re-running it each QBR would report moat erosion while it is still cheap to reverse. Section 4 of the [Adoption Review](../../practice/implementation-motion/04-sustaining-adoption-review.md) is the natural home, since it already governs what depreciates and must be re-earned.

---

## Open questions

- **Resolved in the Constitution.** Axiom II names the party bearing the specificity and sets the level, and Axiom I separates composition, which selects the motion, from that level. Both were open questions raised by this document.
- **$p_{close}$ needs an estimator.** The nearest available approach is retrospective scoring of closed deals, which carries hindsight bias and would be recorded with that status rather than presented as clean.
- **The first-year margin disqualifier assumes a single-shot game.** Section 7 shows the test is too strict when $r_t$ holds up. Correcting it means editing a disqualification rule reps rely on, so it waits for review.
- **$C_{sustain}$ has no budget owner.** The framework assigns no department to it, and a variable with no owner drifts.
- **$R_{redeploy}$ needs a scoring method.** Redeployability is the term that separates a good forward-deployed engagement from an expensive one, and nothing in the repository measures it yet.

---

## Related

- **Research:** [klein-crawford-alchian.md](../02-research/klein-crawford-alchian.md) for quasi-rents and supplier exposure, [real-options.md](../02-research/real-options.md) for staging under irreversibility, [process-misfit.md](../02-research/process-misfit.md) for what drives $C_{deliver}$.
- **Buyer-side model:** [00-tcg-constitution.md](./00-tcg-constitution.md) Part III.
- **Functional forms:** [02-mathematical-models.md](./02-mathematical-models.md).
- **Staging in practice:** [milestone-valuation-model.md](../../practice/milestone-valuation-model.md).
