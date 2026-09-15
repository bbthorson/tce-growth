---
title: "Governance Forms"
layer: theory
status: active
version: 1.0
operationalizes: [axiom-1, axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# Governance Forms

**Version:** 1.0
**Purpose:** To say what shape a commercial relationship should take, given what it costs to transact. The friction vector says which instruments a deal needs. This says what kind of arrangement should hold the two parties together once it closes, and when no arrangement will.

---

## 1. The dimension the framework had lost

Williamson selects a governance form from three properties of a transaction: how specific the investment is, how uncertain the environment is, and **how often the transaction recurs between the same two parties**.

Two of those three have been in this framework since the beginning. Asset specificity is the level, $\lVert \mathbf{F} \rVert_1$. Uncertainty is the three component gaps. Frequency was present once, as a scoring factor called Retention Horizon, and it was folded into the implementation count as though a long relationship were a kind of installation cost.

That was a category error and it cost the framework its entire strategy layer. Frequency is not a cost. It is the property that decides whether building machinery to govern a relationship is worth building at all, because machinery amortizes over repetitions and a single transaction has nothing to amortize over.

**Frequency is a separate axis with three readings.**

| Reading | Condition | Field evidence |
|---|---|---|
| **One-shot** | The transaction completes and the parties have no structural reason to meet again. A migration, a perpetual licence, a fixed-scope build. | No renewal date exists. Nobody can name what the second purchase would be. |
| **Recurrent** | The transaction renews on a cycle, and either party can decline at the boundary. An annual contract. | A renewal date exists and a named person owns it on each side. |
| **Continuous** | The product is inside the buyer's operations and stopping is itself a project. A platform the buyer has built on. | Ask what a migration away would cost them. If nobody can answer, it is continuous. |

---

## 2. Four forms, selected by level and frequency

Williamson's result is that specificity and frequency together select the governance structure, and that using the wrong one is expensive in a predictable direction.

| Level | Frequency | Governance form | What it looks like commercially |
|---|---|---|---|
| Below the boundary | Any | **Market** | Standard terms, published pricing, no relationship apparatus. Classical contracting: the document is complete and the parties are strangers. |
| At or above | One-shot | **Trilateral** | Neither side will build relational machinery for a transaction that happens once, so safeguards come from outside the pair. Fixed scope, external acceptance criteria, escrow, arbitration, a named third party who adjudicates. |
| At or above | Recurrent | **Bilateral** | The parties safeguard each other directly and both keep their autonomy. Mutual commitments, staged gates, symmetric consequence. The [Mutual Implementation Plan](../../practice/implementation-motion/03-closing-mutual-implementation-plan.md) is an instrument of this form. |
| Far above, and rising | Continuous | **Unified** | One party absorbs the other's function. The buyer builds it internally, or the seller acquires the delivery capability. The transaction stops being a transaction. |

**The MIP has always been bilateral governance and was justified as something narrower.** Its stated purpose is protection against hold-up, which is true and incomplete. What it actually is, structurally, is a relational contract: it leaves both parties autonomous, it safeguards the relationship rather than the transaction, and its gates are the mechanism by which each repetition earns the next. That is why it works on recurrent deals and reads as bureaucratic overhead on one-shot ones.

**The fourth row is a loss condition, and the framework has never named it.** When specificity keeps rising on a continuous relationship, unified governance eventually beats any contract the two parties can write. For the seller, that means the buyer builds it. Axiom I's under-frictioned failure mode describes the symptom. This row describes when it becomes rational rather than merely likely.

---

## 3. The make-or-buy boundary was already in the equation

The Surplus equation subtracts the buyer's next best alternative:

$$S = \left(V_{effective}(t) - V_{next\_best}\right) - F_{effective}$$

$V_{next\_best}$ has always included building it internally. Which means the framework's master equation has carried Coase's founding question since it was written, without naming it: **the deal closes only when buying beats integrating, net of what transacting costs.**

Reading it that way makes two things visible that the deal-level reading hides.

**Every reduction in transaction cost widens the market for buying rather than making.** It is not only this deal that moves. A seller who lowers $F_{implementation}$ across a category shifts the make-or-buy boundary for every buyer in it, which is why the instrument sets in [`practice/`](../../practice/) are a market-making investment and not only a deal-closing one.

**A buyer's build alternative gets cheaper over time on its own.** Their internal capability compounds, tooling improves, and the specificity that made building expensive erodes as patterns standardize. A seller whose only argument is that building is hard is on a losing schedule, and the Decay Clock is the deal-level version of the same pressure.

---

## 4. Addressable market is a property of the motion

A seller who runs only Turnkey instruments can transact only with short-vector buyers. Buyers whose deals carry a long vector are not lost somewhere in the funnel. They were never reachable, because the motion offered no instrument for the cost that was blocking them.

**This inverts the usual reading.** Addressable market is normally treated as a property of the product, fixed by what it does and who needs it. Under Axiom I it is a property of the motion, because the motion decides which regions of the friction space a seller can serve at all. Changing the motion changes the market, and no product change is required for that to happen.

Three consequences follow, and the first two are uncomfortable.

**A market sizing exercise conducted without naming the motion is not measuring anything stable.** It is measuring the intersection of who needs the product with who the current motion can reach, and reporting the first number.

**A funnel conversion rate is a statement about motion coverage as much as about execution.** Deals that die at the same stage for the same reason, repeatedly, are usually not being lost. They are outside the region the motion serves, and coaching reps harder on them is spending against a structural constraint.

**Entering a new region is a capability decision, not a campaign.** Serving consensus-dominant deals requires consensus instruments, which this repository does not have. A seller cannot decide to reach those buyers next quarter any more than they can decide to ship a feature by announcing it.

---

## 5. Recurrence is a choice, and choosing it lowers the cost of governing specificity

This is the strategic claim the rest of the file assembles, and it is the framework's own rather than Williamson's.

A one-shot high-specificity transaction sits in trilateral governance, where safeguards have to come from outside the pair because neither party will build machinery for a single event. Third-party safeguards are expensive, slow, and adversarial by construction.

A recurrent transaction of identical specificity sits in bilateral governance, where the safeguard is the next repetition. That is Axiom III's cooperation condition doing the work that an arbitrator would otherwise have to do, and it costs nothing per transaction once the relationship exists.

**So the frequency of a transaction is not only a fact about the market. It is partly a decision by the seller, and it changes what the same deal costs to govern.**

$$\delta_{discount} > \frac{T - R}{T - P}$$

Restructuring a one-shot sale as a subscription converts a single-play game into a repeated one, which raises both parties' weight on the future and brings the cooperation condition within reach. The usual account of why subscription pricing won is about revenue predictability and cash flow. Those are real and they are effects on the seller's income statement. This is a claim about the transaction itself: **subscription made high-specificity software governable without third-party machinery, and that is why it could be sold to buyers who would not have signed a fixed-scope build.**

**What follows operationally.** Where a deal reads high-level and one-shot, the highest-leverage move is often not a better safeguard. It is to find a structure that makes the relationship recurrent, because that changes which governance form applies rather than making an expensive form cheaper.

**What follows for compensation.** The cooperation condition binds the seller's own agents as well as the seller. A representative paid in full at signature holds no stake in whether the relationship reaches its second repetition, so the seller's side of the repeated game is being played by someone with a one-shot payoff. Vesting commission on outcomes that survive signature brings that agent's $\delta_{discount}$ above the threshold: a clawback when the customer fails to launch, a safe harbor for risks nobody could have seen, and a share of expansion revenue for the ones who did the job. This matters beyond the Structural deal it protects, because the person choosing the motion is otherwise an adjudicator with no exposure to the churn a misread vector produces. The framework carried this as a comp plan template until 2026-09. The template is gone and the claim stays.

**What would falsify this.** If categories that moved from perpetual licence to subscription showed no change in the specificity of deals they could close, only in revenue timing, the claim is wrong. The prediction is that the reachable region of the friction space widened, and that is observable in the deals that became closeable rather than in the income statement.

---

## 6. Which output answers which question

The framework now emits three things about a deal and they are routinely confused.

| Quantity | Question it answers | What moves it |
|---|---|---|
| **Level** | How much apparatus does this deal need? | Nothing during the cycle. It is a property of the deal. |
| **Direction** | Which instruments, of the apparatus it needs? | Discovery. Every closed gap rotates it. |
| **Governance form** | What shape should the arrangement take after signature, and can the apparatus be paid for? | Frequency, which is partly a commercial choice rather than a finding. |

**Level says what the deal needs and frequency says whether it can be afforded.** A one-shot deal at level 22 needs the full implementation chain and cannot amortize it over anything. That is the second exclusion criterion in [01-motion-taxonomy.md](./01-motion-taxonomy.md) section 4, stated in its proper terms, and it is the case where declining is correct and running a lighter version is not.

---

## 7. What this does not settle

- **Where the continuous boundary sits.** The fourth row says unified governance eventually wins on rising specificity in a continuous relationship. It does not say at what level, and there is no instrument that reads it. A seller currently learns they crossed it when the buyer announces a platform team.
- **Whether frequency is three readings or a continuum.** The three readings are chosen for field use. Nothing argues that the boundaries between them are real rather than convenient.
- **Whether the recurrence claim survives contact with a category that never had a one-shot form.** Software sold as a subscription from the beginning offers no before-and-after, so the falsification test in section 5 only runs on categories that made the transition.
- **How governance form interacts with direction.** The forms are selected by level and frequency. Whether a consensus-dominant deal wants a different safeguard structure from an implementation-dominant one of identical level is untested, and there is reason to think it does: the parties who need safeguarding are not the same parties.

---

## Related

- [00-tcg-constitution.md](./00-tcg-constitution.md) — Axiom I supplies level and frequency. Axiom III supplies the cooperation condition section 5 turns on.
- [06-friction-vector.md](./06-friction-vector.md) — Direction and level, the other two outputs.
- [01-motion-taxonomy.md](./01-motion-taxonomy.md) — Section 4's six exclusion criteria, of which the second is section 6's affordability case.
- [05-seller-surplus-model.md](./05-seller-surplus-model.md) — What the seller spends before signature, which is what a one-shot deal has to recover in one transaction.
- [transaction-cost-economics.md](../02-research/transaction-cost-economics.md) — Williamson (1979) is the source of the four forms and the frequency dimension.
- [game-theory-and-nrr.md](../02-research/game-theory-and-nrr.md) — Axelrod, and why a repeated game safeguards itself.
- [Mutual Implementation Plan](../../practice/implementation-motion/03-closing-mutual-implementation-plan.md) — The bilateral form's instrument.
- [Deal Triage Calculator](../../practice/deal-triage-calculator.md) — Emits level, direction and frequency.
