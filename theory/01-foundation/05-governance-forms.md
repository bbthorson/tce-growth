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

**What the readings read.** The three readings are field proxies for one quantity: each party's stake at the next boundary. That is the surplus a party expects from the relationship's remaining repetitions, which it puts at risk by forcing a renegotiation or letting the relationship lapse. It is $F_p$ in [02-mathematical-models.md](./02-mathematical-models.md) section 5.5, and it does both of frequency's jobs. Governance machinery amortizes against the same stream, and the stream is what each side forfeits if it defects. Read against the two quasi-rents, it gives the readings real boundaries.

- **One-shot** is a deal with no next boundary at which both sides have something to forfeit, $\min(F_b, F_s) = 0$. A sanction needs a stake on both sides, so a one-shot deal is bonded only by the quasi-rents themselves or by a third party.
- **Recurrent** is a deal with a stake on both sides where the buyer stays bonded, $\omega Q_b \le (1 - \omega) Q_s + F_s$. The buyer's non-renewal is a credible sanction, because the seller could not take more from the buyer at a boundary than forcing the renegotiation would cost the seller.
- **Continuous** is the same deal once the buyer fails that condition. Its quasi-rent, the integration built and the workflows rewired, has outgrown what the next boundary puts at risk for the seller, so stopping is a project and non-renewal stops being a sanction. More repetitions move a deal away from this line, because they raise the seller's stake. A rising buyer investment moves it toward the line.

The seller can fail the same condition in the other direction, early in a forward-deployed engagement. That is not a frequency reading. It is the seller's exposure, and Axiom III governs it by settling the allocation before the seller spends.

Two consequences follow. The variable Constitution 2.4 proposed and 3.0 withdrew, the buyer's cost of exit, survives inside $Q_b$. It is now read against the seller's quasi-rent and stake rather than alone, and reading it alone was the reason for the withdrawal. And the fourth row's loss condition in section 2 begins where the buyer fails the bond condition. It becomes rational once the buyer's build alternative beats the renegotiated terms, which is what open question 12 still has to read.

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

**What each form safeguards, and where the sale starts.** All four forms govern one pair: the buyer and the seller. Market governance leaves each free to walk. Trilateral governance puts a third party between them, bilateral governance has each sanction the other at the boundary, and unified governance merges them. The Constitution's gap table in Axiom III says each cost runs between its own pair of parties, so a form protects a deal only against the hazard that runs between the pair it governs.

- **Policing and enforcement** runs between the buyer and the seller: the seller's uncertainty about the buyer's environment, and the buyer's about the seller's capability in it. That is the pair the forms govern, so a deal whose sale starts here takes the form section 2 selects, and nothing more.
- **Bargaining and decision** has an external part, the buyer's bargain with the seller over terms, which the forms reach. Its internal part runs between the decision roles inside the buyer. The future loss it feeds is whether the coalition holds once the investment is sunk, and the party that defects there is a decision role, not the buyer firm. No buyer-seller form reaches it. Non-renewal sanctions the wrong party, and a Mutual Implementation Plan binds the signatory, not the role whose budget the change cuts. So a deal whose sale starts here needs the form section 2 selects and a safeguard inside the buyer as well.
- **Search and information** runs between the buyer and the market. Once the buyer has chosen, it stops mattering to what anyone loses later (Axiom III), so where a sale starts at search the form follows the exposure the other two costs leave. A channel or marketplace that stands between the buyer and the market is an adjudicator that needs a stake under Axiom III, and not a governance form for the transaction.

**The safeguard inside the buyer.** It applies Axiom III's rule that every party holding exposed rent needs a stake, with the decision roles as the parties. It has three parts.

1. **An adjudicator with authority over the roles, holding a stake.** The buyer's own hierarchy settles disputes between its decision roles by fiat, which makes the sponsor the third party in a trilateral structure inside the buyer. A sponsor with nothing riding on the outcome is the adjudicator with no exposure that the corollary warns against. Whether the mandate still stands is what open question 29 asks the deal reading to track.
2. **An arrangement each exposed role ratifies.** Each role's reservation is answered in the arrangement record and accepted by the role's occupant, which is the shared half of the bargaining instrument open question 2 still owes.
3. **Commitments written against roles, not people.** A departed champion reopens the bargaining gap at once. A safeguard tied to the role survives an occupant change and is re-ratified by the successor. One tied to the person leaves with them.

The bond logic carries over. A role that bears the change's cost in budget or headcount stays bonded when what it gains from the change, staged with adoption, covers what it loses, and it defects when the change only costs it.

*Falsifier.* At equal specific exposure and frequency, deals whose sale started at bargaining and were governed only between buyer and seller should drift after signature more than those with a staked sponsor and role-level ratification, and deals whose sale started at policing should show no such difference. If the bargaining-start deals governed by a Mutual Implementation Plan alone drift no more than the policing-start deals, the forms need no addition.

---

## 3. The make-or-buy boundary was already in the equation

The buyer's condition subtracts the buyer's next best alternative inside $V_{switch}(t) = V_{effective}(t) - V_{next\_best}$:

$$S_b = V_{switch}(t) - P - \sum_k I^b_k - L_b$$

$V_{next\_best}$ has always included building it internally. Which means the buyer's condition has carried Coase's founding question since it was written, without naming it: **the deal closes only when buying beats integrating, net of what transacting costs.**

Reading it that way makes two things visible that the deal-level reading hides.

**Every reduction in transaction cost widens the market for buying rather than making.** It is not only this deal that moves. A seller who lowers $F_{implementation}$ across a category shifts the make-or-buy boundary for every buyer in it, which is why the instrument sets in [`practice/`](../../practice/) are a market-making investment and not only a deal-closing one.

**A buyer's build alternative gets cheaper over time on its own.** Their internal capability compounds, tooling improves, and the specificity that made building expensive erodes as patterns standardize. A seller whose only argument is that building is hard is on a losing schedule, and the Decay Clock is the deal-level version of the same pressure.

**When the buyer builds.** The fourth row in section 2 now has a condition. At a renewal the buyer chooses between staying on renegotiated terms and building. Write the build margin, in contract value per year, as

$$M_{build} = C^{b}_{run} + k_{build} + \left(\tilde{V}_{solution} - V_{build}\right) - P$$

$C^{b}_{run}$ is what running the function in-house would cost the buyer each year. $k_{build}$ is the build and the migration, annualized over the buyer's horizon. The bracket is whatever value the buyer's own version would lack. A positive margin means paying the seller is cheaper than building before any hold-up. A buyer whose margin has fallen to zero builds whatever the governance, which is ordinary make-or-buy and the schedule the paragraph above describes.

While the buyer stays bonded, in section 1's recurrent reading, the seller can take nothing in plain view and the margin alone decides. Once the buyer fails the bond condition, in the continuous reading, the seller can take up to $H_b$ at each boundary ([02-mathematical-models.md](./02-mathematical-models.md) section 5.5). The buyer builds when what it stands to lose that way exceeds the margin:

$$H_b > M_{build}$$

- **The build margin caps the seller's take.** A seller that takes less keeps the account, and one that takes more teaches the buyer to build. The seller does not see the buyer's build alternative, so it usually finds the line by crossing it, which is the platform-team announcement section 7 describes.
- **This is the latest the buyer builds, not the earliest.** Refusing to adapt, or moving the best people to a newer account, costs the buyer more than it saves the seller, and $H_b$ counts only what the seller gains. The buyer's loss can cross the margin first.
- **Rising specificity works against the seller on both sides.** It raises $Q_b$ and with it $H_b$. As patterns standardize it also lowers $k_{build}$. That is the fourth row's "specific, and rising" stated as two terms.
- **The seller's defences are the bond terms.** It can raise its own stake and quasi-rent, allocate a right that limits what renegotiation can take, such as a cap on the renewal price, or keep its price under the margin.

*Falsifier.* Among bonded accounts, a move in-house should follow a build alternative becoming cheaper than the price. Among accounts past the bond condition, it should also follow forced renegotiations and refusals to adapt. If both groups go in-house at the same rate and after the same triggers, the bond condition adds nothing to make-or-buy.

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

**What follows for compensation: the safeguard inside the seller.** The seller is a coalition too, and its representative holds one of its decision roles: the one that reads the deal, picks the motion and makes the promises the rest of the seller delivers. The seller sinks its specific investment on that reading, the pre-sale engineering, the delivery capacity and the forward-deployed team, and so meets both exposures Axiom III names. It cannot verify what the representative knows about the deal's fit, which is hidden information. And once the representative is paid at signature, it can see that attention move to the next deal and cannot stop it, which is lock-in. A representative paid in full at signature holds no stake in whether the relationship reaches its second repetition, so the seller's side of the repeated game is played by someone with a one-shot payoff.

The enforcement corollary's two remedies, applied with the representative as the party, are the vesting plan. A clawback when the customer fails to launch is a hostage. A safe harbor for risks nobody could have seen is a right allocated before the investment is sunk, settling in advance who carries what neither could read. A share of expansion revenue for the ones who did the job is the representative's stake at the next boundary, $F$ in the bond condition of [02-mathematical-models.md](./02-mathematical-models.md) section 5.5. That condition carries over in form, with its terms not valued here: the representative sinks little of its own, so the stake required rises with what the seller sinks on the representative's reading, and it is zero where the seller sinks nothing specific. This is sharper than the third standing assumption alone, which says only that an actor with no stake ignores the outcome. Below the gate a representative paid on bookings costs the seller nothing it can lose later, and vesting there buys no governance. This matters beyond the specific deal it protects, because the person choosing the motion is otherwise an adjudicator with no exposure to the churn a misread deal produces. The framework carried this as a comp plan template until 2026-09. The template is gone and the claim stays.

**What follows for channels.** A channel, marketplace or analyst that recommends a seller adjudicates the buyer's search gap, and the fourth Friction Allocation Principle already says its signal separates only if it loses when a bad signal passes. A channel paid on referral is cheap talk by that principle, and it drifts from adjudication toward extraction for the same reason. Its stake is a share of what survives signature, or its own reputation staked on the recommendation, which depreciates by Axiom III's reputation corollary unless it is re-earned.

**What the derivation leaves standing.** It treats a decision role as a party to Axiom III, and that is a premise about who the parties are, not a result. The bargaining cost rests on the same premise, because the buyer is a coalition whose roles bargain over their own budgets and standing. So the third standing assumption stays, narrowed. It no longer carries the stakes. It says the parties are the roles on each side and the intermediaries between them, each acting on its own payoff.

*Falsifier.* At equal contract value, vesting and clawbacks should predict retention after signature in deals where the seller sank specific investment before signature, more strongly the more it sank, and predict nothing in deals below the gate. If compensation structure moves retention as much below the gate as above it, the stake is doing something other than governing the seller's exposure, and the third standing assumption is carrying the claim after all.

**Enforcement governs what verification cannot.** Mutual sanction at each boundary is one kind of hostage, renewed. Constitution 5.0 makes the wider claim an Axiom III corollary. Wathne and Heide (2000) separate opportunism that depends on hidden information from opportunism that exploits lock-in. Verification reaches only the first. A party that can see the other side refuse to adapt, force a renegotiation or move its best people to a newer account, and cannot stop it, is exposed under full information. Two things govern that. One is a hostage, something the defecting party loses: a bond, a reciprocal specific investment, fees staged against delivery, or the seller's referenceability. The other is a right allocated before the investment is sunk, which fixes where a renegotiation starts and who controls it: an option to renew at a preset price, a priced right to stop, or the right to make the last offer. Aghion, Dewatripont and Rey (1994) and Nöldeke and Schmidt (1995) show such rights can induce efficient specific investment without any hostage, and open question 40 asks which works better in software deals. Both remedies run in both directions, and the framework makes no claim about which party drifts first (open question 33). Each party is entitled to ask what the other loses if it stops trying. A seller offering only proof, or only a discount, to a buyer worried about drift has answered the wrong question, which is the unhostaged failure. A discount changes the price once. A hostage or an allocated right changes what defection costs at every later boundary. [02-mathematical-models.md](./02-mathematical-models.md) section 5.5 states the bond condition both remedies serve. [incomplete-contracts.md](../02-research/incomplete-contracts.md) carries the evidence.

**What would falsify this.** If categories that moved from one-shot to recurring terms showed no change in the specificity of deals they could close, only in revenue timing, the claim is wrong. The prediction is that the specificity a seller could govern widened where both parties carried a stake at each boundary, and did not widen where the buyer alone could walk. For enforcement: at equal verification, deals where both parties hold something to lose, or where the right to renew or stop was allocated in advance, should drift less after signature than deals where only one side has sunk investment and nothing was allocated.

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

- **Where the continuous boundary sits.** Section 3 now states it: the buyer builds once what the seller can take at a boundary exceeds the buyer's build margin. No instrument reads the margin yet. A seller currently learns it crossed the line when the buyer announces a platform team.
- **How to measure the stake at a boundary.** Section 1 now reads the three readings as regions of each party's stake at the next boundary against the two quasi-rents, which settled open question 11 on 2026-11-04. The stake $F_p$ is named and not valued, so the field still classifies from the evidence column. Constitution 2.4 proposed the buyer's cost of exit at the next boundary and 3.0 withdrew it: contractual exit is a thin layer over procedural, technical and human switching cost (Burnham, Frels and Mahajan 2003), and lowering it one-sidedly hands the seller's sunk investment to the buyer (MacLeod and Malcomson 1989).
- **Whether the recurrence claim survives a category that never had a one-shot form.** Software sold as a subscription from the beginning offers no before-and-after, so the test in section 5 runs only on categories that made the transition, or has to vary the mutual stake inside one.
- **What two restatements gave up.** Until 2.4 this section claimed that subscription won because it made specific software governable. Until 3.0 it claimed the buyer's cheap exit was the governing variable. The first fell to software economics and the second to relational-contracting theory, and [tce-empirical-record.md](../02-research/tce-empirical-record.md) records both.
- **How large the representative's stake has to be.** Section 5 now derives the stakes for the seller's representatives and for channels from Axiom III with the roles as parties, which settled open question 21 on 2026-11-04. The stake required rises with what the seller sinks on the representative's reading and is zero below the gate, and neither term is valued.
- **How the safeguard inside the buyer is read.** Section 2 now says a deal whose sale starts at bargaining needs a safeguard inside the buyer beside the buyer-seller form, which settled open question 10 on 2026-11-04. No instrument yet reads whether a deal has one. The decision-role ledger owed under open question 2 is its home.

---

## Related

- [00-tcg-constitution.md](./00-tcg-constitution.md) — Axiom III supplies specificity, frequency and the cooperation condition section 5 turns on. Axiom I supplies where the sale starts.
- [01-motions.md](./01-motions.md) — The motions, named by where the sale starts.
- [04-seller-surplus-model.md](./04-seller-surplus-model.md) — What the seller spends before signature, which is what a one-shot deal has to recover in one transaction.
- [transaction-cost-economics.md](../02-research/transaction-cost-economics.md) — Williamson (1979) is the source of the four forms and the frequency dimension.
- [game-theory-and-nrr.md](../02-research/game-theory-and-nrr.md) — Axelrod, and why a repeated game safeguards itself.
- [Mutual Implementation Plan](../../practice/implementation-motion/03-closing-mutual-implementation-plan.md) — The bilateral form's instrument.
- [Deal Triage Calculator](../../practice/deal-triage-calculator.md) — Emits the positions, where the sale starts, the specific exposure, the frequency and the governance form.
