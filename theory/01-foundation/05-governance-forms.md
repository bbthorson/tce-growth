---
title: "Governance Forms"
layer: theory
status: active
version: 1.3
operationalizes: [axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# Governance Forms

**Version:** 1.3
**Purpose:** To say what shape a commercial relationship should take, given what it costs to transact. Where the sale starts says which instruments a deal needs. This says what kind of arrangement should hold the two parties together once something specific is sunk, and when no arrangement will. The forms are corollaries of Axiom III, the Law of Future Cost.

---

## 1. The dimension the framework had lost

Williamson selects a governance form from three properties of a transaction: how specific the investment is, how uncertain the environment is, and **how often the transaction recurs between the same two parties**.

Specificity is the specific exposure under Axiom III. Uncertainty is the gaps that decide the chance of future loss, under the same axiom. Frequency is the third reading, and it is not a cost. It is what decides whether machinery built to govern a relationship can be amortized at all, because machinery amortizes over repetitions and a single transaction has nothing to amortize over.

**Frequency is a separate axis with three readings.**

| Reading | Condition | Field evidence |
|---|---|---|
| **One-shot** | The transaction completes and the parties have no structural reason to meet again. A migration, a perpetual licence, a fixed-scope build. | No renewal date exists. Nobody can name what the second purchase would be. |
| **Recurrent** | The transaction renews on a cycle, and either party can decline at the boundary. An annual contract. | A renewal date exists and a named person owns it on each side. |
| **Continuous** | The product is inside the buyer's operations and stopping is itself a project. A platform the buyer has built on. | Ask what a migration away would cost them. If nobody can answer, it is continuous. |

---

## 2. Four forms, selected by specific exposure and frequency

Williamson's result is that specificity and frequency together select the governance structure, and that using the wrong one is expensive in a predictable direction. This is Axiom III's governance corollary. Since Constitution 4.0 the specificity reading is the [Deal Triage Calculator](../../practice/deal-triage-calculator.md)'s exposure: whether the deal sinks anything that only works here.

| Specific exposure | Frequency | Governance form | What it looks like commercially |
|---|---|---|---|
| None | Any | **Market** | Standard terms, published pricing, no relationship apparatus. Classical contracting: the document is complete and the parties are strangers. |
| Specific | One-shot | **Trilateral** | Neither side will build relational machinery for a transaction that happens once, so safeguards come from outside the pair. Fixed scope, external acceptance criteria, escrow, arbitration, a named third party who adjudicates. |
| Specific | Recurrent | **Bilateral** | The parties safeguard each other directly and both keep their autonomy. Mutual commitments, staged gates, symmetric consequence. The [Mutual Implementation Plan](../../practice/implementation-motion/03-closing-mutual-implementation-plan.md) is an instrument of this form. |
| Specific, and rising | Continuous | **Unified** | One party absorbs the other's function. The buyer builds it internally, or the seller acquires the delivery capability. The transaction stops being a transaction. |

**The MIP is bilateral governance.** Its stated purpose is protection against hold-up, which is true and incomplete. Structurally it is a relational contract: it leaves both parties autonomous, it safeguards the relationship rather than the transaction, and its gates are the mechanism by which each repetition earns the next. That is why it works on recurring deals and reads as overhead on one-shot ones.

**The fourth row is a loss condition.** When specificity keeps rising on a continuous relationship, unified governance eventually beats any contract the two parties can write. For the seller, that means the buyer builds it. Axiom III's unallocated failure mode describes the symptom. This row describes when it becomes rational rather than merely likely.

---

## 3. The make-or-buy boundary was already in the equation

The buyer's condition subtracts the buyer's next best alternative inside $V_{switch}(t) = V_{effective}(t) - V_{next\_best}$:

$$S_b = V_{switch}(t) - P - \sum_k I^b_k - L_b$$

$V_{next\_best}$ has always included building it internally. Which means the buyer's condition has carried Coase's founding question since it was written, without naming it: **the deal closes only when buying beats integrating, net of what transacting costs.**

Reading it that way makes two things visible that the deal-level reading hides.

**Every reduction in transaction cost widens the market for buying rather than making.** It is not only this deal that moves. A seller who lowers $F_{implementation}$ across a category shifts the make-or-buy boundary for every buyer in it, which is why the instrument sets in [`practice/`](../../practice/) are a market-making investment and not only a deal-closing one.

**A buyer's build alternative gets cheaper over time on its own.** Their internal capability compounds, tooling improves, and the specificity that made building expensive erodes as patterns standardize. A seller whose only argument is that building is hard is on a losing schedule, and the Decay Clock is the deal-level version of the same pressure.

---

## 4. Addressable market is a property of the motion

Addressable market is normally treated as a property of the product. Under Axiom I it is a property of the motion, because the motion decides which costs a seller can pay down, and buyers whose sale starts at a cost the seller cannot pay down are never reached. Three consequences follow.

**A market sizing exercise conducted without naming the motion is not measuring anything stable.** It is measuring the intersection of who needs the product with who the current motion can reach, and reporting the first number.

**A funnel conversion rate is a statement about motion coverage as much as about execution.** Deals that die at the same stage for the same reason, repeatedly, are usually not being lost. They start at a cost the motion does not pay down, and coaching reps harder on them is spending against a structural constraint.

**Reaching buyers whose sale starts elsewhere is a capability decision, not a campaign.** Serving buyers whose sale starts at consensus requires consensus instruments, which this repository does not have. A seller cannot decide to reach those buyers next quarter any more than they can decide to ship a feature by announcing it.

---

## 5. Recurrence is a choice, and what it buys is mutual sanction

This is the strategic claim the rest of the file assembles, and it is the framework's own rather than Williamson's. Constitution 2.4 restated it around the buyer's cost of exit and 3.0 withdrew that restatement. Section 7 records why.

A one-shot high-specificity transaction sits in trilateral governance, where safeguards have to come from outside the pair because neither party will build machinery for a single event. Third-party safeguards are expensive, slow, and adversarial by construction.

A recurrent transaction of identical specificity sits in bilateral governance, where the safeguard is the next repetition. The repetition safeguards because each party can sanction the other at the boundary, and the sanction is credible only when both hold exposure there. The buyer's is non-renewal, credible where their real cost of leaving is bounded. The seller's is the delivery commitment, the price cap and the penalty a lapse would forfeit. Williamson's term is the hostage: credible commitments are mutual or they are not commitments. A one-sided cheap exit for the buyer is not governance. It hands the seller's sunk investment to the buyer to hold up (MacLeod and Malcomson 1989, Baker, Gibbons and Murphy 2002), which is why enterprise buyers above the small-deal tier seek multi-year terms with price caps rather than short ones, and why sellers who grant termination for convenience price it or refuse it.

$$\delta_{discount} > \frac{T - R}{T - P}$$

**So the frequency of a transaction is not only a fact about the market. It is partly a decision by the seller, and it changes what the same deal costs to govern.** Restructuring a one-shot sale as a recurring one brings the cooperation condition within reach when two things hold. The seller can amortize the governance apparatus across repetitions, which is Williamson's frequency argument. And both sides carry a stake at each boundary. Where exit is operationally impossible whatever the contract says, as in core systems, the buyer's sanction is not credible, and governance falls back to the trilateral row with system integrators and multi-year terms whatever the pricing model.

**What subscription did, and what it did not.** Subscription was one vehicle for recurrence. The framework does not claim it as the reason subscription won: multi-tenant hosting, revenue smoothing and operating-expense treatment explain most of that adoption (Choudhary 2007). Nor did it make cheap exit normal above the small-deal tier, where multi-year terms and auto-renewal are the norm. The claim kept is narrower: recurrence with a stake on both sides widened the specificity a seller could govern without an arbitrator. [tce-empirical-record.md](../02-research/tce-empirical-record.md) records both corrections.

**What follows operationally.** Where a deal reads specific and one-shot, the highest-leverage move is often not a better safeguard. It is to find a structure that makes the relationship recurrent with a stake on both sides at each boundary, because that changes which governance form applies rather than making an expensive form cheaper. Staging the commitment, per Axiom III's corollary, is how the two stakes grow together.

**What follows for compensation.** The cooperation condition applies to the seller's own agents as well as the seller. A representative paid in full at signature holds no stake in whether the relationship reaches its second repetition, so the seller's side of the repeated game is being played by someone with a one-shot payoff. Vesting commission on outcomes that survive signature brings that agent's $\delta_{discount}$ above the threshold: a clawback when the customer fails to launch, a safe harbor for risks nobody could have seen, and a share of expansion revenue for the ones who did the job. This matters beyond the specific deal it protects, because the person choosing the motion is otherwise an adjudicator with no exposure to the churn a misread deal produces. The framework carried this as a comp plan template until 2026-09. The template is gone and the claim stays.

**What would falsify this.** If categories that moved from one-shot to recurring terms showed no change in the specificity of deals they could close, only in revenue timing, the claim is wrong. The prediction is that the specificity a seller could govern widened where both parties carried a stake at each boundary, and did not widen where the buyer alone could walk.

---

## 6. Which output answers which question

The [Deal Triage Calculator](../../practice/deal-triage-calculator.md) emits four readings about a deal, and they are routinely confused.

| Output | Question it answers | What moves it |
|---|---|---|
| **Where the sale starts** | Which cost does the seller pay down first, and with which instruments? (Axiom I) | Discovery and seller investment. The counts are re-taken at every artifact boundary, and a cost that started nearest its threshold may not stay there. |
| **The three gaps** | What can each pair of parties not yet verify? (Axiom III) | Discovery steps them down. Absent maintenance they rebuild. They move the chance of future loss, never the positions. |
| **Specific exposure** | Does the deal sink anything worth less outside this relationship, and so need governance at all? (Axiom III) | What the deal sinks. A trial that lets the buyer verify fit and walk away passes the gate and leaves nothing specific. |
| **Governance form** | What shape should the arrangement take, and can the seller's investment be paid back? (Axiom III) | Frequency, which is partly a commercial choice rather than a finding, and which buys governance only when both parties hold a stake at each boundary. |

**Exposure says whether the deal needs governance and frequency says whether it can be afforded.** A specific one-shot deal needs a safeguard and cannot amortize the seller's investment over anything. That is the second decline condition in the [Deal Triage Calculator](../../practice/deal-triage-calculator.md), stated in its proper terms, and it is the case where declining or restructuring as recurrent is correct and running a lighter version is not.

---

## 7. What this does not settle

- **Where the continuous boundary sits.** The fourth row says unified governance eventually wins on rising specificity in a continuous relationship. It does not say at what degree of specificity, and there is no instrument that reads it. A seller currently learns they crossed it when the buyer announces a platform team.
- **Whether frequency is three readings or a continuum.** The three readings are chosen for field use, and nothing argues the boundaries are real rather than convenient. The variable underneath is open. Constitution 2.4 proposed the buyer's cost of exit at the next boundary and 3.0 withdrew it: contractual exit is a thin layer over procedural, technical and human switching cost (Burnham, Frels and Mahajan 2003), and lowering it one-sidedly hands the seller's sunk investment to the buyer (MacLeod and Malcomson 1989).
- **Whether the recurrence claim survives a category that never had a one-shot form.** Software sold as a subscription from the beginning offers no before-and-after, so the test in section 5 runs only on categories that made the transition, or has to vary the mutual stake inside one.
- **What two restatements gave up.** Until 2.4 this section claimed that subscription won because it made specific software governable. Until 3.0 it claimed the buyer's cheap exit was the governing variable. The first fell to software economics and the second to relational-contracting theory, and [tce-empirical-record.md](../02-research/tce-empirical-record.md) records both.
- **How governance form interacts with where the sale starts.** The forms are selected by specific exposure and frequency. Whether a deal that starts at consensus wants a different safeguard structure from one that starts at implementation, at identical exposure, is untested, and there is reason to think it does: the parties who need safeguarding are not the same parties.

---

## Related

- [00-tcg-constitution.md](./00-tcg-constitution.md) — Axiom III supplies specificity, frequency and the cooperation condition section 5 turns on. Axiom I supplies where the sale starts.
- [01-motions.md](./01-motions.md) — The motions, named by where the sale starts.
- [04-seller-surplus-model.md](./04-seller-surplus-model.md) — What the seller spends before signature, which is what a one-shot deal has to recover in one transaction.
- [transaction-cost-economics.md](../02-research/transaction-cost-economics.md) — Williamson (1979) is the source of the four forms and the frequency dimension.
- [game-theory-and-nrr.md](../02-research/game-theory-and-nrr.md) — Axelrod, and why a repeated game safeguards itself.
- [Mutual Implementation Plan](../../practice/implementation-motion/03-closing-mutual-implementation-plan.md) — The bilateral form's instrument.
- [Deal Triage Calculator](../../practice/deal-triage-calculator.md) — Emits the positions, where the sale starts, the specific exposure, the frequency and the governance form.
