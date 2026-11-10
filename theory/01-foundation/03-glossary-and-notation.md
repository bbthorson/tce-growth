---
title: "Glossary and Notation"
layer: theory
status: active
version: 2.0
---

# Glossary and Notation

**Version:** 2.0
**Purpose:** To supply one place to look up any term used in this repo, and to say where its canonical definition lives.

## How to use this file

**The term index is an index, not a source of truth.** Every entry carries a one-line identifier and a link to where the concept is defined. The identifier exists so you can confirm you found the right entry, not so you can skip reading the source. If an entry and its linked source disagree, **the source wins** and the entry is a bug. Report it or fix it.

The term index matches Constitution 7.0. The notation index below it is older and is marked as such.

---

## Term index

One line each, then the canonical source. The line identifies the term. The source defines it.

### The three axioms and their times

| Term | Identifier | Canonical source |
|---|---|---|
| **Axiom I, Law of Transaction Cost Composition** | Time0, the market. The buyer asks whether to buy, build or do nothing, and the seller whether it can serve these buyers at a profit. Claims 1 to 5. | [Constitution, Part I](./00-tcg-constitution.md) |
| **Axiom II, Law of Transaction Investment** | Time1, contracting. The buyer asks whether its organization can agree and what the purchase will take, and the seller whether the deal is worth what it takes. Claims 6 to 9. | [Constitution, Part I](./00-tcg-constitution.md) |
| **Axiom III, Law of Future Cost** | Time2, renewal. The buyer asks whether it worked here and whether it is free to leave, and the seller whether the relationship pays. Claims 10 to 12. | [Constitution, Part I](./00-tcg-constitution.md) |
| **Time0, Time1, Time2** | The market, contracting and renewal. Written without a space. Each cost has a home time. | [Constitution, Part I](./00-tcg-constitution.md) |
| **Claim** | One of the twelve numbered statements in the Constitution, each with a test that could fail. The numbers are stable, so cite a claim by its number. | [Constitution, Part I](./00-tcg-constitution.md) |

### The three costs

| Term | Identifier | Canonical source |
|---|---|---|
| **Search** | Finding a seller to trust, telling whether a solution fits, and reaching the seller at all. Home time Time0. Descends from Dahlman's search and information. | [Constitution, premise](./00-tcg-constitution.md) |
| **Consensus** | The buyer's own decision roles reaching agreement. Home time Time1. One half of Dahlman's bargaining and decision. | [Constitution, premise](./00-tcg-constitution.md) |
| **Implementation** | Making the product work in the buyer's environment, and checking that the seller delivered. Home time Time2. Wider than Dahlman's policing and enforcement. It is a fear at Time1 and work at Time2. | [Constitution, premise](./00-tcg-constitution.md) |

### Definitions

*Market* and *deal* keep their ordinary meanings.

| Term | Identifier | Canonical source |
|---|---|---|
| **Workflow** | The procedure a product changes. Read for how settled and how entangled it is. | [Constitution, Definitions](./00-tcg-constitution.md) |
| **Settled** | Written down, followed, with its exceptions known. | [01-motions.md](./01-motions.md) section 2 |
| **Entangled** | How much else changes when the workflow changes. | [01-motions.md](./01-motions.md) section 2 |
| **Decision role** | A position in the buyer's organization that can stop or must approve the purchase, defined by its relation to the workflow and not by its occupant. | [Constitution, Definitions](./00-tcg-constitution.md) |
| **Plug-in purchase** | Works on arrival. The buyer can try it on its own work and walk away having stranded nothing. | [Constitution, claim 6](./00-tcg-constitution.md) |
| **Built-in purchase** | The buyer, the seller or both build something that is worth less anywhere else. | [Constitution, claim 6](./00-tcg-constitution.md) |
| **Specific investment** | The economists' word for what a built-in purchase builds. The research files use it. | [transaction-cost-economics.md](../02-research/transaction-cost-economics.md) |
| **Motion** | What a seller does, and is organized to do, to carry part of a buyer's cost. | [01-motions.md](./01-motions.md) |
| **Turnkey** | A market where buyers can carry every cost alone and the purchase is plug-in. It does not stay that way on its own. | [Constitution, claim 3](./00-tcg-constitution.md), [01-motions.md](./01-motions.md) section 4 |

### Time0 terms

| Term | Identifier | Canonical source |
|---|---|---|
| **Search-led, consensus-led, implementation-led** | The three motions, each named for the cost it carries. Two costs in the way are run together. | [01-motions.md](./01-motions.md) section 3 |
| **Relay model** | One role per funnel stage, each with a fixed playbook, and pay on bookings. The right motion for a Turnkey market. | [01-motions.md](./01-motions.md) section 6 |
| **Floor** | The part of a cost set outside any deal, which falls only through something shared across deals. | [Constitution, claim 4](./00-tcg-constitution.md), [information-environment.md](../02-research/information-environment.md) |
| **Costly signal** | A commitment that costs a weak seller more than a strong one, so it tells them apart. | [costly-signals.md](../02-research/costly-signals.md) |
| **Cheap talk** | A claim any seller could make at no cost. It carries no information and adds to the buyer's work. | [costly-signals.md](../02-research/costly-signals.md) |
| **Friction Allocation Principles** | The four tests a signal must pass to count as evidence. | [Friction Allocation Diagnostic](../../practice/friction-allocation-diagnostic.md) |
| **Channel collapse** | A channel whose filtering ran on the cost of producing a message, and which fails when that cost falls. | [channel-collapse.md](../02-research/channel-collapse.md) |
| **Chaos Trap** | A buyer with no documented workflow, where the product automates the process. Route to consulting, not to a motion. | [Deal Triage Calculator, Step 0](../../practice/deal-triage-calculator.md) |

### Time1 terms

| Term | Identifier | Canonical source |
|---|---|---|
| **Price as a transfer** | What leaves the buyer arrives at the seller, so a discount changes the split and leaves the work of buying the same size. | [Constitution, claim 8](./00-tcg-constitution.md), [02-mathematical-models.md](./02-mathematical-models.md) sections 1.1 to 1.4 |
| **Spend threshold** | The contract value above which the buyer's rules add an approver. The one case where price changes a cost. | [Constitution, claim 8](./00-tcg-constitution.md) |
| **Commitment** | Something a seller would not offer if it expected to fail, such as capped overages or a guarantee tied to the buyer's environment. | [Constitution, claim 8](./00-tcg-constitution.md) |
| **Discovery** | The seller learning the buyer's environment before either side builds. | [Enforcement Ledger, Map](../../practice/enforcement-ledger.md) |
| **Pre-mortem** | Walking the buyer through how the project would fail before anyone signs. | [Enforcement Ledger, Test](../../practice/enforcement-ledger.md) |
| **Real option** | The value of being able to defer a decision that cannot be undone. | [real-options.md](../02-research/real-options.md) |

### Time2 terms

| Term | Identifier | Canonical source |
|---|---|---|
| **Hold-up** | One side squeezing the other once it cannot leave. | [Constitution, claim 11](./00-tcg-constitution.md), [klein-crawford-alchian.md](../02-research/klein-crawford-alchian.md) |
| **Earned lock-in, and lock-in by control** | A buyer stays because of what the two sides built, or because it cannot take its data or leave its terms. | [Constitution, claim 11](./00-tcg-constitution.md) |
| **Staged plan** | Who carries which risk, in stages, with a point at each where either side can stop at a known price. Agreed before either side builds. | [Constitution, claim 12](./00-tcg-constitution.md), [Enforcement Ledger, Stage](../../practice/enforcement-ledger.md) |
| **Standing review** | A review agreed before signature for what nobody can foresee, held before the renewal reads it. | [Constitution, claims 10 and 12](./00-tcg-constitution.md), [Sustaining Adoption Review](../../practice/adoption-review.md) |
| **Account management** | The seller carrying a buyer's cost after signature. | [Constitution, claim 10](./00-tcg-constitution.md) |
| **Residual control rights** | The agreed authority to decide where the contract is silent. | [incomplete-contracts.md](../02-research/incomplete-contracts.md) |
| **Handoff Rule** | Both deal ledgers must reach the account manager intact, or what the seller learned is lost on the receiving side. | [Sustaining Adoption Review](../../practice/adoption-review.md) |

### Artifact vocabulary

| Term | Identifier | Canonical source |
|---|---|---|
| **Contextual Blueprint** | The discovery artifact: what the seller learned of the buyer's environment, in writing. | [Enforcement Ledger, Map](../../practice/enforcement-ledger.md) |
| **Red Team** | The pre-mortem workshop. | [Enforcement Ledger, Test](../../practice/enforcement-ledger.md) |
| **Mutual Implementation Plan (MIP)** | The staged plan both sides agree before either builds. | [Enforcement Ledger, Stage](../../practice/enforcement-ledger.md) |
| **Sustaining Adoption Review** | The handoff, the standing review and renewal, after signature. | [Sustaining Adoption Review](../../practice/adoption-review.md) |
| **Vested Commission** | Pay that waits on what happens after signature. Claim 5 says when it applies. | [Constitution, claim 5](./00-tcg-constitution.md) |

### External frameworks

| Term | Identifier | Canonical source |
|---|---|---|
| **CFIR** | Implementation-science framework for reading a buyer's organization before the sale. | [cfir.md](../02-research/cfir.md), which says where each construct is read |
| **RE-AIM** | Five-dimension framework for measuring success after the sale. | [re-aim-framework.md](../02-research/re-aim-framework.md) |
| **NRR** | Net Revenue Retention. The lagging indicator of the four upstream RE-AIM dimensions. | [re-aim-framework.md](../02-research/re-aim-framework.md) |

### Retired terms

Kept so older analyses stay readable. Do not use these in new writing. Files that have not yet had their pass in the trim still use the 7.0 retirements.

<!-- vale TCG.RetiredTerms = NO -->
**Retired in Constitution 7.0**

| Retired term | Use instead |
|---|---|
| Time 0 for the deal, time 1 for the relationship | Time1 and Time2. Time0 is the market |
| Position, zone, self-serve threshold, participation threshold, default edges | Nothing. A cost is in the way or it is not, read from the workflow and the organization (claim 2) |
| The gate | The three plug-in tests in claim 6. The rule that one cost keeps a buyer out whatever else is true has no replacement, because value trades against cost |
| Where the sale starts, the tightest cost | The cost in the way |
| Specific exposure, read as none or specific | Plug-in or built-in |
| Toaster and bridge | Plug-in and built-in |
| Realizable, recognized and realized value | Value, set outside the sale |
| Recognized cost, category prior, Unshown | What the buyer expects, and showing a cost with evidence the buyer can check |
| The two conditions, as the Constitution's content | Price as a transfer (claim 8). The equations are in 02-mathematical-models.md sections 1.1 to 1.4 |
| Three levers | Claim 8: a discount, against a commitment the seller would not make if it expected to fail |
| Governance form, frequency | Standard terms for a plug-in purchase, and a staged plan with a standing review for a built-in one (claim 12) |
| Stakes corollary | Claim 5, on pay |
| Hold-up wedge, bond condition, drift rates, Decay Clock, Reputation Depreciation | Nothing in the Constitution. Claims 10 to 12 state what they defended |
| Dahlman's names as the canonical names | Search, consensus and implementation. Dahlman is cited as their origin |

**Retired earlier.** Some replacements in this table were themselves retired in 7.0. Follow them into the table above.

| Retired term | Use instead |
|---|---|
| Law of Asset Specificity (Axiom II until 4.0) | Axiom III, Law of Future Cost. Axiom II is now the Law of Transaction Investment |
| Law of Uncertainty Inflation (Axiom III until 4.0) | Axiom III, Law of Future Cost |
| Market level, workflow level, deal level | The three times |
| Seat, seat map, seat ledger | Decision role, decision-role map, decision-role ledger |
| Coase's names: search, bargaining, enforcement | Search, consensus and implementation |
| Structural deal | A built-in purchase, or a deal outside Turnkey, by meaning |
| Turnkey deal, as a level below 15 | Turnkey, a market condition |
| Level, magnitude, the 0 to 30 sum | Nothing |
| Direction, shares, dominant component, dominance threshold, Composed | The cost in the way. Two are run together |
| The cost that binds, the cost nearest its own threshold | The cost in the way |
| Boundary Condition | The three plug-in tests in claim 6 |
| Amplification, the per-component multiplier | Nothing |
| The Surplus equation | Price as a transfer |
| Under-frictioned | Unallocated |
| Mis-composed | Imitation |
<!-- vale TCG.RetiredTerms = YES -->

---

## Notation index

> [!NOTE]
> **This index and the symbol disambiguation after it describe [02-mathematical-models.md](./02-mathematical-models.md) as it stood at Constitution 6.4.** Constitution 7.0 holds no equation, so where a row gives the Constitution as a symbol's source, read that file. Both sections retire with the math in pass 5 of the trim ([TRIM-PROPOSAL.md](../../TRIM-PROPOSAL.md)).

### The two conditions (Axiom II, with Axiom III's losses)

Every term is a fraction of annual contract value, per [02-mathematical-models.md](./02-mathematical-models.md) section 1.2, except the gate's demands and thresholds below.

| Symbol | Meaning | Defined in |
|---|---|---|
| $S_b$ | The buyer's condition. $V_{switch}(t) - P - \sum_k I^b_k - L_b$. Must exceed 0 for the buyer to go ahead. | [Constitution, Axiom II](./00-tcg-constitution.md) |
| $S_s$ | The seller's condition. $P - C_{deliver} - \sum_k I^s_k - L_s$. Must exceed 0 for the seller to go ahead. | [Constitution, Axiom II](./00-tcg-constitution.md) |
| $S_b + S_s$ | The joint surplus. Price cancels from it, because price is a transfer. | [02-mathematical-models.md §1.3](./02-mathematical-models.md) |
| $V_{switch}(t)$ | The buyer's opportunity cost of staying where they are. Equals $\tilde{V}_{solution} \cdot e^{-\delta t} - V_{next\_best}$, read on recognized value. | [Constitution, Axiom II](./00-tcg-constitution.md) |
| $P$ | Price over the relationship. Appears in both conditions and in neither party's cost of transacting. **Not the punishment payoff.** | [Constitution, Axiom II](./00-tcg-constitution.md) |
| $C_{deliver}$ | The seller's cost of delivering against that price. Contingent on revenue. | [Constitution, Axiom II](./00-tcg-constitution.md), [04-seller-surplus-model.md §2](./04-seller-surplus-model.md) |
| $I^b_k$ | What the buyer invests today against cost $k$. Includes the buyer's adaptation work: integrations built, workflows rewired. | [Constitution, Axiom II](./00-tcg-constitution.md) |
| $I^s_k$ | What the seller invests today against cost $k$. The seller's cost of acquiring customers lives here. | [Constitution, Axiom II](./00-tcg-constitution.md) |
| $L_b$, $L_s$ | Each party's expected future loss, from Axiom III. | [Constitution, Axiom III](./00-tcg-constitution.md) |
| $W_k$ | The work against cost $k$, before it is assigned to either party. | [02-mathematical-models.md §1.4](./02-mathematical-models.md) |
| $\theta^b_k$, $\theta^s_k$ | Each party's cost of doing one unit of $W_k$. | [02-mathematical-models.md §1.4](./02-mathematical-models.md) |
| $w$ | The share of $W_k$ moved from buyer to seller. | [02-mathematical-models.md §1.4](./02-mathematical-models.md) |

### Seller-side terms

| Symbol | Meaning | Defined in |
|---|---|---|
| $S_{seller}$ | Seller surplus in the seller surplus model. $S_s$ is the same condition read on a close, with $C_{invest}$ split by cost and the future loss written out. | [04-seller-surplus-model.md §2](./04-seller-surplus-model.md) |
| $C_{invest}$ | The seller's pre-signature, deal-specific engineering. Sunk whether or not the deal closes. The seller's case of $C^{p}_{invest}$. | [04-seller-surplus-model.md §2](./04-seller-surplus-model.md) |
| $V_{contract}$ | Contract value the seller receives. **Seller revenue, not buyer cost.** | [04-seller-surplus-model.md §2](./04-seller-surplus-model.md) |
| $p_{close}$ | Probability the deal closes given the investment made. Not the same as $p_m$ or $\pi_p$. | [04-seller-surplus-model.md §2](./04-seller-surplus-model.md) |
| $R_{redeploy}$ | Value of the seller's pre-signature work redeployed to other deals. The seller's case of $R^{p}_{redeploy}$. **Not $R$, the reward payoff.** | [04-seller-surplus-model.md §3](./04-seller-surplus-model.md) |
| $p_m$ | Probability of achieving milestone stage $m$. | [02-mathematical-models.md §5.4](./02-mathematical-models.md) |
| $S_m$ | Expected surplus at milestone stage $m$. A buyer-side quantity. | [02-mathematical-models.md §5.4](./02-mathematical-models.md) |
| $r_t$ | Probability the relationship is live in period $t$. $r_1$ equals $p_{close}$. **Not $r_k$, a cost's position.** | [04-seller-surplus-model.md §7](./04-seller-surplus-model.md) |
| $C_{sustain}$ | Ongoing relationship investment per period. Holds the gaps down, and is distinct from $C_{deliver}$. | [04-seller-surplus-model.md §7](./04-seller-surplus-model.md) |
| $\rho$ | Discount rate on future periods. **A policy choice, not $\delta_{discount}$.** | [04-seller-surplus-model.md §7](./04-seller-surplus-model.md) |

### Value terms (second standing assumption)

| Symbol | Meaning | Defined in |
|---|---|---|
| $V_{solution}$ | Realizable value: what the change can be worth to this buyer for a given offer, set by the product and the buyer's situation. Exogenous to the sale. | [Constitution, standing assumptions](./00-tcg-constitution.md) |
| $\tilde{V}_{solution}$ | Recognized value: the buyer's estimate of realizable value, usually held as a range, at its peak at the triggering event. The seller moves it, and the buyer decides on it. | [Constitution, standing assumptions](./00-tcg-constitution.md) |
| $V_{effective}(t)$ | Value after decay. Equals $\tilde{V}_{solution} \cdot e^{-\delta t}$. | [Constitution, standing assumptions](./00-tcg-constitution.md) |
| $V_{next\_best}$ | Value of the buyer's next best alternative, including building it themselves. This is the make-or-buy boundary. | [Constitution, Axiom II](./00-tcg-constitution.md) |

### Costs, thresholds and positions (Axiom I)

| Symbol | Meaning | Defined in |
|---|---|---|
| $F_k$ | Cost $k$, for $k$ in search, consensus, implementation: what the work on its demand costs, in fractions of annual contract value, $c^b_k(n_k - a_k) + c^s_k a_k$. Non-compensatory, with a cost floor set outside the deal. | [Constitution, Axiom I](./00-tcg-constitution.md), [02-mathematical-models.md §6](./02-mathematical-models.md) |
| $F_{search}$ | The search and information cost. Which solutions exist, whether this one fits, and whether the buyer can reach the seller at all. | [Constitution, Axiom I](./00-tcg-constitution.md) |
| $F_{consensus}$ | The bargaining and decision cost. Mostly internal, among the decision roles, before any term is negotiated with the seller. | [Constitution, Axiom I](./00-tcg-constitution.md), [02-mathematical-models.md §3](./02-mathematical-models.md) |
| $F_{implementation}$ | The policing and enforcement cost. Whether the seller will deliver what was promised, and whether it will work here. | [Constitution, Axiom I](./00-tcg-constitution.md) |
| $n_k$ | Cost $k$'s demand on its payer, in the payer's own units. The gate reads it. | [Constitution, Axiom I](./00-tcg-constitution.md), [02-mathematical-models.md §6](./02-mathematical-models.md) |
| $\kappa_k$, $\bar{A}_k$, $a_k$ | The payer's capacity for cost $k$'s work, the most demand others can move off it within the deal, and the amount moved. | [Constitution, Axiom I](./00-tcg-constitution.md), [02-mathematical-models.md §6](./02-mathematical-models.md) |
| $c^b_k$, $c^s_k$ | What a unit of cost $k$'s work costs each side. Named, not valued. | [02-mathematical-models.md §6](./02-mathematical-models.md) |
| $G_k$, $h_k$, $\chi_k$ | The seller's belief about cost $k$'s capacity, that belief's hazard, and the share of a gain on cost $k$ the seller keeps against rivals. The next seller dollar goes to the largest $\chi_k h_k / c^s_k$. Named, not valued. | [02-mathematical-models.md §1.5](./02-mathematical-models.md) |
| $\tau^{self}_k$, $\tau^{part}_k$ | The thresholds, $\kappa_k$ and $\kappa_k + \bar{A}_k$. Chosen default edges stand in until read, and a position on them is evidence neither way. | [Constitution, Axiom I](./00-tcg-constitution.md), [02-mathematical-models.md §6](./02-mathematical-models.md) |
| $r_k$ | Cost $k$'s position, $(n_k - \tau^{self}_k)/(\tau^{part}_k - \tau^{self}_k)$: the share of the movable demand that has to be moved. The largest is the tightest cost, where the sale starts. | [Constitution, Axioms I and II](./00-tcg-constitution.md), [02-mathematical-models.md §6](./02-mathematical-models.md) |
| $\tilde{n}_k$, $\tilde{r}_k$ | Recognized cost and its position: the demand the buyer expects, on which it decides to enter discovery. Before any seller is met it is the category prior. | [Constitution, Axiom I](./00-tcg-constitution.md) |
| $n_{search}$, $n_{consensus}$, $n_{impl}$ | The calculator's three counts: the demand $n_k$ for each cost. | [Deal Triage Calculator](../../practice/deal-triage-calculator.md) |
| $n_{exposure}$ | Integration points, changed workflows and divergent steps. Read only where the gate fails, and never added to a cost. | [Deal Triage Calculator](../../practice/deal-triage-calculator.md) |

### Gap terms (Axiom III)

| Symbol | Meaning | Defined in |
|---|---|---|
| $\hat{\Delta}_k$ | Cost $k$'s own gap on $[0, 1]$. Three different pairs of parties. Feeds the chance of future loss and multiplies no cost. | [02-mathematical-models.md §2.4](./02-mathematical-models.md) |
| $e_k$, $m_k$ | Items with evidence attached, and items in scope, for the count-based gaps $\hat{\Delta}_{search}$ and $\hat{\Delta}_{consensus}$. | [02-mathematical-models.md §2.4](./02-mathematical-models.md) |
| $\Delta_A$ | The implementation gap, the one bilateral pair. A **sum**, not a difference: $I_{seller} + I_{buyer}$. | [02-mathematical-models.md §2.1](./02-mathematical-models.md) |
| $\Delta_A^{raw}$ | The scorecard's raw implementation gap on $[2, 10]$. Normalize to $\hat{\Delta}_{implementation}$ before any equation takes it. | [02-mathematical-models.md §2.5](./02-mathematical-models.md) |
| $I_{seller}$ | Seller Ignorance. What the seller has not mapped about the buyer's environment. The seller's loss runs on it. | [02-mathematical-models.md §2.2](./02-mathematical-models.md) |
| $I_{buyer}$ | Buyer Uncertainty. Doubt about return variance and vendor capability. The buyer's loss runs on it. | [02-mathematical-models.md §2.3](./02-mathematical-models.md) |
| $\Delta_A^*$ | Akerlof Exit Threshold, the research concept. In the framework, buyer exit is Axiom I's participation threshold. | [costly-signals.md](../02-research/costly-signals.md) |
| $x_m$ | Residual uncertainty **entering** milestone stage $m$, already normalized. Not a separate quantity from $\hat{\Delta}_{implementation}$, which is where the chain starts. | [02-mathematical-models.md §5.4](./02-mathematical-models.md) |

### Future loss (Axiom III)

| Symbol | Meaning | Defined in |
|---|---|---|
| $L_p$ | Party $p$'s expected future loss, $Q_p \cdot \pi_p$, for $p$ in $b$ (buyer) and $s$ (seller). A shortfall in expected return, not a second charge for the investment. | [Constitution, Axiom III](./00-tcg-constitution.md) |
| $Q_p$ | Appropriable quasi-rent. What party $p$ has sunk that is worth less outside this relationship, $C^{p}_{invest} - R^{p}_{redeploy}$. Bounds $L_p$. | [Constitution, Axiom III](./00-tcg-constitution.md) |
| $C^{p}_{invest}$ | What party $p$ has sunk in this relationship. | [Constitution, Axiom III](./00-tcg-constitution.md) |
| $R^{p}_{redeploy}$ | What party $p$ could recover by redeploying it elsewhere. | [Constitution, Axiom III](./00-tcg-constitution.md) |
| $\pi_p$ | The expected share of party $p$'s exposure lost, through a failed fit or through what the other side takes. Rises with the gaps $p$ cannot close, and with $H_p$ where the bond condition fails. Placeholder form for the gap part $\pi_0 + (1 - \pi_0)\, g_p$. | [02-mathematical-models.md §5.2, §5.5](./02-mathematical-models.md) |
| $\pi_0$ | Floor on the chance of loss, above zero because some risk survives any amount of proof. Named, not valued. | [02-mathematical-models.md §5.2](./02-mathematical-models.md) |
| $g_p$ | Mean of the normalized gaps in party $p$'s row: its own half of the implementation gap and the bargaining gap. | [02-mathematical-models.md §5.2](./02-mathematical-models.md) |
| $Q_m$ | Quasi-rent sunk at milestone gate $m$. The staged loss is $\sum_m Q_m \, \pi(x_m)$. | [02-mathematical-models.md §5.4](./02-mathematical-models.md) |

### Coefficients and parameters

Every default below is unfitted. [06-calibration.md](./06-calibration.md) carries each value's provenance.

| Symbol | Meaning | Default | Defined in |
|---|---|---|---|
| $\lambda$ | Loss aversion coefficient from prospect theory. Measured and dimensionless. No live equation in this framework takes it. | 2.25 | [prospect-theory.md](../02-research/prospect-theory.md) |
| $\alpha$ | Baseline coordination overhead in the consensus model, the conversion into contract value. | 1.0 | [02-mathematical-models.md §3.1](./02-mathematical-models.md) |
| $\beta$ | Organizational complexity exponent. Above 1 because channels grow as $N(N-1)/2$. | 1.35 | [02-mathematical-models.md §3.1](./02-mathematical-models.md) |
| $N$ | Decision roles holding veto power or evaluation responsibility. | measured | [02-mathematical-models.md §3.1](./02-mathematical-models.md) |
| $I_i$ | Decision role $i$'s utility from the initiative, on $[-1, 1]$. | measured | [02-mathematical-models.md §3.2](./02-mathematical-models.md) |
| $\text{Var}(I_i)$ | Variance in decision-role incentive alignment, bounded above by 1. | measured | [02-mathematical-models.md §3.2](./02-mathematical-models.md) |
| $TO$ | Technical overlap score on $[1, 5]$. Architectural alignment among technical evaluators. | measured | [02-mathematical-models.md §3.4](./02-mathematical-models.md) |
| $U_{tech}$, $U_{process}$ | Unmapped technical complexity and unmapped operational variance. | measured | [02-mathematical-models.md §2.2](./02-mathematical-models.md) |
| $w_t$, $w_p$ | Weights on the two ignorance terms, summing to 1. | 0.6, 0.4 | [02-mathematical-models.md §2.2](./02-mathematical-models.md) |
| $\phi_t$, $\phi_p$ | Risk acceleration exponents. | 1.2, 1.1 | [02-mathematical-models.md §2.2](./02-mathematical-models.md) |
| $\sigma_{ROI} / \bar{R}$ | Coefficient of variation of projected return. | measured | [02-mathematical-models.md §2.3](./02-mathematical-models.md) |
| $K_{vendor}$ | Demonstrated vendor proof. Blueprints, reference architectures, validated benchmarks. | measured | [02-mathematical-models.md §2.3](./02-mathematical-models.md) |
| $\mu$, $\nu$, $\kappa$ | Sensitivity to return uncertainty, baseline doubt for an unvalidated vendor, decay of doubt per unit of proof. | 1.0, 2.0, 0.5 | [02-mathematical-models.md §2.3](./02-mathematical-models.md) |
| $\lambda_{inertia}$ | Organizational inertia. Bureaucracy, competing projects, status quo preference. | measured | [02-mathematical-models.md §4.2](./02-mathematical-models.md) |
| $E_{external}$ | Magnitude of the external catalyst. The only term in $\delta$ a seller can move. | measured | [02-mathematical-models.md §4.2](./02-mathematical-models.md) |

### Time and governance terms

| Symbol | Meaning | Defined in |
|---|---|---|
| $\delta$ | Decay rate of urgency after the triggering event. | [02-mathematical-models.md §4](./02-mathematical-models.md) |
| $\delta_{discount}$ | A party's discount factor. The weight it places on future payoffs. | [Constitution, Axiom III](./00-tcg-constitution.md) |
| $\gamma_k$ | Rate at which cost $k$'s gap rebuilds toward its ceiling, absent maintenance. Three rates with different drivers. Named, not valued. | [Constitution, Axiom III](./00-tcg-constitution.md) |
| $\eta_k$ | Rate at which maintenance pulls cost $k$'s gap down, in proportion to its size. Account management is the seller's. Named, not valued. | [02-mathematical-models.md §5.3, §5.7](./02-mathematical-models.md) |
| $\psi_b$, $\psi_s$ | Rates at which the buyer's and the seller's changes open divergent steps after go-live. Fit drift, apart from stale verification. Named, not valued. | [02-mathematical-models.md §5.3](./02-mathematical-models.md) |
| $\gamma_r$ | Responsiveness converting external pressure into internal action. | [02-mathematical-models.md §4.2](./02-mathematical-models.md) |
| $\gamma_{TO}$ | Weight on the technical overlap term. | 0.20, [02-mathematical-models.md §3.4](./02-mathematical-models.md) |
| $T$, $R$, $P$ | Temptation, reward, and punishment payoffs in the cooperation condition. | [game-theory-and-nrr.md](../02-research/game-theory-and-nrr.md) |

### Allocation coverage

| Symbol | Meaning | Defined in |
|---|---|---|
| ACR | Allocation Coverage Ratio. Share of a deal's specific investment sunk only after a signed Stage row covering it was agreed. | [Enforcement Ledger](../../practice/enforcement-ledger.md) |

### Retired in Constitution 4.0

None of these survives in `models/tcg_models.py`. [02-mathematical-models.md](./02-mathematical-models.md) section 7 records why each went.

<!-- vale TCG.RetiredTerms = NO -->
| Symbol | What it was | What replaced it |
|---|---|---|
| $S$, $OC_{switching}$ | The single Deal Surplus and its opportunity-cost term | $S_b$ and $S_s$, and $V_{switch}(t)$ |
| $y$ | Reduced-form perceived transaction cost, $a\hat{\Delta}_A^2 + c$ | Nothing. A discount moves $P$, which cancels, and verification lowers $\pi_p$, so only verification can rescue a deal whose joint surplus is negative. It adds surplus only when it lowers the loss by more than it costs |
| $a$, $b$, $c$ | The coupling anchored at 2.25, the base friction growth rate, and direct cost | Nothing for $a$ and $b$. What $c$ held is price, now $P$ |
| $D(t)$ | A deal's trajectory, transaction cost against opportunity cost | The two conditions over time |
| $k$, $k_{threshold}$ | Specificity as a level, and its boundary at 15 of 30 | Specific exposure, read under Axiom III |
| $F_{deployed}$ | Friction deployed, required to scale with $k$ | The seller's investment $I^s_k$ (Axiom II), and governance only where something specific is sunk (Axiom III) |
| $\mathbf{F}$, $\hat{\mathbf{F}}$, $\lVert \mathbf{F} \rVert_1$ | The friction vector, its direction shares and its summed level | The positions $r_k$. The sale starts at the largest |
| $F_{base}$, $F_{effective}$ | Summed cost, and cost after the per-component multiplier $(1 + \hat{\Delta}_k)$ | Nothing. No single summed level is read, the costs are non-compensatory, and the gaps multiply nothing |
| $\hat{\Delta}_A$ | The deal-level gap, the friction-weighted mean of the three | Nothing. Each gap is read in its own pair, and $\hat{\Delta}_{implementation}$ is the normalized $\Delta_A$ |
| $\gamma$ (bare) | Deal-level drift, the friction-weighted mean of the $\gamma_k$ | $\gamma_k$ |
| $\hat{\Delta}_k(0) + \gamma_k t$ | Linear drift, unbounded | Bounded drift toward a ceiling |
<!-- vale TCG.RetiredTerms = YES -->

---

## Symbol disambiguation

Seven groups look alike and mean different things. Each has produced a documented error, required an inline correction somewhere in this repo, or was caught during drafting before it could.

**1. $\gamma$ carries three unrelated meanings, and one of them has three subscripts of its own.** In the Constitution, $\gamma_k$ is the rate at which a gap rebuilds over time, one rate per cost: $\gamma_{search}$, $\gamma_{consensus}$, $\gamma_{implementation}$. In the mathematical models the letter appears twice more, as $\gamma_r$ (responsiveness to an external catalyst) and $\gamma_{TO}$ (the technical overlap weight). The subscripts are load-bearing, and the two families are told apart by what the subscript names: a cost, or a mechanism. Bare $\gamma$, the deal-level average, retired with the deal-level gap.

**2. $\delta$ and $\delta_{discount}$ are unrelated.** Bare $\delta$ is the urgency decay rate, and it belongs to the value-decay half of the Decay Clock, a standing assumption. $\delta_{discount}$ is a party's weight on future payoffs, and it belongs to the cooperation condition in Axiom III's frequency corollary. They share a letter and nothing else. A rising $\delta$ is bad for the deal, and a rising $\delta_{discount}$ is good for it. A third rate joins them in [04-seller-surplus-model.md §7](./04-seller-surplus-model.md): $\rho$ discounts the seller's future cash flows and is set by finance policy, where $\delta_{discount}$ describes how much a party actually weighs its future and is a behavioural fact about them.

**3. $\Delta_A$ and $\hat{\Delta}_{implementation}$ differ by an order of magnitude, and neither is the deal's gap.** The model's scorecard form produces a raw score on $[2, 10]$ that must be normalized before any equation accepts it. The [Enforcement Ledger](../../practice/enforcement-ledger.md) reports the normalized value directly. The normalization and its rationale live in [02-mathematical-models.md §2.5](./02-mathematical-models.md). Separately, what the scorecard measures is the policing and enforcement cost's gap alone, the implementation gap in field terms, because that is the only pair that is buyer against seller. Constitution 4.0 retired the deal-level mean $\hat{\Delta}_A$, so there is no single deal gap to substitute the scorecard's output for. Each party's loss reads its own half.

**4. Five quantities are written with $I$.** $I^b_k$ and $I^s_k$ are investments today, in contract value, under Axiom II. $I_{buyer}$ and $I_{seller}$ are the two halves of the implementation gap under Axiom III. $I_i$ is one decision role's utility from the initiative, on $[-1, 1]$. A superscript party and a subscript cost mark an investment. A subscript party marks uncertainty. A subscript index marks a role.

**5. $P$, $r$ and $Q$ each carry two meanings.** $P$ is price in the two conditions and the punishment payoff in the cooperation condition. $r_k$ is a cost's position between its thresholds, and $r_t$ is the probability the relationship is live in period $t$. $Q_p$ is party $p$'s whole quasi-rent and $Q_m$ is the part sunk at gate $m$, while bare $Q$ in the seller surplus model is the seller's $Q_s$. Read the subscript before the letter.

**6. The $C$ terms carry their party.** $C_{deliver}$ and bare $C_{invest}$ are what the seller spends. $C^{p}_{invest}$ is what either party sinks, and for the buyer it is the integration built and the workflows rewired. $V_{contract}$ is seller revenue, the price $P$ seen from the seller's side, and not a value the buyer receives. A figure quoted without its party is unreadable.

**7. Four surpluses and three probabilities share letters.** $S_b$ and $S_s$ are the two conditions of Part II, and both must hold. $S_{seller}$ is the seller surplus model's form of $S_s$. $S_m$ is neither: it is the buyer's expected surplus at one milestone stage. Likewise $p_{close}$ is the probability a deal closes, $p_m$ is the probability a stage completes, and $\pi_p$ is the chance a party's exposure does not come back. The $p_{close}$ and $p_m$ pair was caught while drafting [04-seller-surplus-model.md](./04-seller-surplus-model.md) rather than in use.

---

## Maintaining this file

- **New concept that two or more directories reference:** add a row to the term index, pointing at its canonical home. Do not define it here. A term used in one file belongs in that file and not here.
- **A term is renamed or retired:** move the row to the retired table, and add the old name to the retired-terms lint rule, so the rename cannot drift back.
- **An entry disagrees with its source:** the source wins. Fix the entry.
- **New symbol:** do not add one. The notation index retires with the math.

## Related

- [00-tcg-constitution.md](./00-tcg-constitution.md) states the twelve claims most entries point to.
- [01-motions.md](./01-motions.md) carries the motions and the incumbent-vocabulary map.
- [02-mathematical-models.md](./02-mathematical-models.md) holds the symbols the notation index lists.
