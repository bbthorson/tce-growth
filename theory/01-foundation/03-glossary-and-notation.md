---
title: "Glossary and Notation"
layer: theory
status: active
version: 1.1
---

# Glossary and Notation

**Version:** 1.1
**Purpose:** To supply one place to look up any symbol or term used in this repo, and to say where its canonical definition lives.

## How to use this file

Two rules govern what is written here, and they differ by section.

**The term index is an index, not a source of truth.** Every entry carries a one-line identifier and a link to where the concept is actually defined. The identifier exists so you can confirm you found the right entry, not so you can skip reading the source. If an entry and its linked source disagree, **the source wins** and the entry is a bug. Report it or fix it.

**The notation index is canonical.** Symbols had no home before this file. Several are reused across documents with different meanings, and one collision was serious enough that [02-mathematical-models.md](./02-mathematical-models.md) had to stop mid-derivation to disambiguate it by hand. That is the gap this section closes. When a document introduces a new symbol, add it here in the same commit.

Every symbol below matches Constitution 4.0. Symbols that 4.0 retired are collected at the end of the notation index, so a reader meeting them in an older analysis can find what replaced them.

---

## Notation index

### The two conditions (Axiom II, with Axiom III's losses)

Every term is a fraction of annual contract value, per [02-mathematical-models.md](./02-mathematical-models.md) section 1.2.

| Symbol | Meaning | Defined in |
|---|---|---|
| $S_b$ | The buyer's condition. $V_{switch}(t) - P - \sum_k I^b_k - L_b$. Must exceed 0 for the buyer to go ahead. | [Constitution, Axiom II](./00-tcg-constitution.md) |
| $S_s$ | The seller's condition. $P - C_{deliver} - \sum_k I^s_k - L_s$. Must exceed 0 for the seller to go ahead. | [Constitution, Axiom II](./00-tcg-constitution.md) |
| $S_b + S_s$ | The joint surplus. Price cancels from it, because price is a transfer. | [02-mathematical-models.md §1.3](./02-mathematical-models.md) |
| $V_{switch}(t)$ | The buyer's opportunity cost of staying where they are. Equals $V_{solution} \cdot e^{-\delta t} - V_{next\_best}$. | [Constitution, Axiom II](./00-tcg-constitution.md) |
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
| $p_m$ | Probability of achieving milestone stage $m$. | [Milestone Valuation Model](../../practice/milestone-valuation-model.md) |
| $S_m$ | Expected surplus at milestone stage $m$. A buyer-side quantity. | [Milestone Valuation Model](../../practice/milestone-valuation-model.md) |
| $r_t$ | Probability the relationship is live in period $t$. $r_1$ equals $p_{close}$. **Not $r_k$, a cost's position.** | [04-seller-surplus-model.md §7](./04-seller-surplus-model.md) |
| $C_{sustain}$ | Ongoing relationship investment per period. Holds the gaps down, and is distinct from $C_{deliver}$. | [04-seller-surplus-model.md §7](./04-seller-surplus-model.md) |
| $\rho$ | Discount rate on future periods. **A policy choice, not $\delta_{discount}$.** | [04-seller-surplus-model.md §7](./04-seller-surplus-model.md) |

### Value terms (second standing assumption)

| Symbol | Meaning | Defined in |
|---|---|---|
| $V_{solution}$ | Peak perceived value at the triggering event. | [Constitution, standing assumptions](./00-tcg-constitution.md) |
| $V_{effective}(t)$ | Value after decay. Equals $V_{solution} \cdot e^{-\delta t}$. | [Constitution, standing assumptions](./00-tcg-constitution.md) |
| $V_{next\_best}$ | Value of the buyer's next best alternative, including building it themselves. This is the make-or-buy boundary. | [Constitution, Axiom II](./00-tcg-constitution.md) |

### Costs, thresholds and positions (Axiom I)

| Symbol | Meaning | Defined in |
|---|---|---|
| $F_k$ | Cost $k$ to the buyer, for $k$ in search, consensus, implementation. The three are never summed. | [Constitution, Axiom I](./00-tcg-constitution.md) |
| $F_{search}$ | The search and information cost. Which solutions exist, whether this one fits, and whether the buyer can reach the seller at all. | [Constitution, Axiom I](./00-tcg-constitution.md) |
| $F_{consensus}$ | The bargaining and decision cost. Mostly internal, among the decision roles, before any term is negotiated with the seller. | [Constitution, Axiom I](./00-tcg-constitution.md), [02-mathematical-models.md §3](./02-mathematical-models.md) |
| $F_{implementation}$ | The policing and enforcement cost. Whether the seller will deliver what was promised, and whether it will work here. | [Constitution, Axiom I](./00-tcg-constitution.md) |
| $\tau^{self}_k$ | Self-serve threshold for cost $k$. Below it the buyer pays the cost down alone. Named, not valued. | [Constitution, Axiom I](./00-tcg-constitution.md) |
| $\tau^{part}_k$ | Participation threshold for cost $k$. Above it the buyer does not enter the market. Named, not valued. | [Constitution, Axiom I](./00-tcg-constitution.md) |
| $r_k$ | Cost $k$'s position between its own two thresholds, $(F_k - \tau^{self}_k)/(\tau^{part}_k - \tau^{self}_k)$. Dimensionless. The sale starts at the largest. | [Constitution, Axiom I](./00-tcg-constitution.md), [02-mathematical-models.md §6](./02-mathematical-models.md) |
| $n_{search}$, $n_{consensus}$, $n_{impl}$ | The calculator's three counts, each read as $F_k$ against its own two edges. | [Deal Triage Calculator](../../practice/deal-triage-calculator.md) |
| $n_{exposure}$ | Integration points, changed workflows and divergent steps. Read only where the gate fails, and never added to a cost. | [Deal Triage Calculator](../../practice/deal-triage-calculator.md) |

### Gap terms (Axiom III)

| Symbol | Meaning | Defined in |
|---|---|---|
| $\hat{\Delta}_k$ | Cost $k$'s own gap on $[0, 1]$. Three different pairs of parties. Feeds the chance of future loss and multiplies no cost. | [02-mathematical-models.md §2.4](./02-mathematical-models.md) |
| $e_k$, $n_k$ | Items with evidence attached, and items in scope, for the count-based gaps $\hat{\Delta}_{search}$ and $\hat{\Delta}_{consensus}$. | [02-mathematical-models.md §2.4](./02-mathematical-models.md) |
| $\Delta_A$ | The implementation gap, the one bilateral pair. A **sum**, not a difference: $I_{seller} + I_{buyer}$. | [02-mathematical-models.md §2.1](./02-mathematical-models.md) |
| $\Delta_A^{raw}$ | The scorecard's raw implementation gap on $[2, 10]$. Normalize to $\hat{\Delta}_{implementation}$ before any equation takes it. | [02-mathematical-models.md §2.5](./02-mathematical-models.md) |
| $I_{seller}$ | Seller Ignorance. What the seller has not mapped about the buyer's environment. The seller's loss runs on it. | [02-mathematical-models.md §2.2](./02-mathematical-models.md) |
| $I_{buyer}$ | Buyer Uncertainty. Doubt about return variance and vendor capability. The buyer's loss runs on it. | [02-mathematical-models.md §2.3](./02-mathematical-models.md) |
| $\Delta_A^*$ | Akerlof Exit Threshold, the research concept. In the framework, buyer exit is Axiom I's participation threshold. | [costly-signals.md](../02-research/costly-signals.md) |
| $x_m$ | Residual uncertainty **entering** milestone stage $m$, already normalized. Not a separate quantity from $\hat{\Delta}_{implementation}$, which is where the chain starts. | [Milestone Valuation Model](../../practice/milestone-valuation-model.md) |

### Future loss (Axiom III)

| Symbol | Meaning | Defined in |
|---|---|---|
| $L_p$ | Party $p$'s expected future loss, $Q_p \cdot \pi_p$, for $p$ in $b$ (buyer) and $s$ (seller). A shortfall in expected return, not a second charge for the investment. | [Constitution, Axiom III](./00-tcg-constitution.md) |
| $Q_p$ | Appropriable quasi-rent. What party $p$ has sunk that is worth less outside this relationship, $C^{p}_{invest} - R^{p}_{redeploy}$. Bounds $L_p$. | [Constitution, Axiom III](./00-tcg-constitution.md) |
| $C^{p}_{invest}$ | What party $p$ has sunk in this relationship. | [Constitution, Axiom III](./00-tcg-constitution.md) |
| $R^{p}_{redeploy}$ | What party $p$ could recover by redeploying it elsewhere. | [Constitution, Axiom III](./00-tcg-constitution.md) |
| $\pi_p$ | The chance party $p$'s exposure does not come back. Rises with the gaps $p$ cannot close. Placeholder form $\pi_0 + (1 - \pi_0)\, g_p$. | [02-mathematical-models.md §5.2](./02-mathematical-models.md) |
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
| $\gamma_r$ | Responsiveness converting external pressure into internal action. | [02-mathematical-models.md §4.2](./02-mathematical-models.md) |
| $\gamma_{TO}$ | Weight on the technical overlap term. | 0.20, [02-mathematical-models.md §3.4](./02-mathematical-models.md) |
| $T$, $R$, $P$ | Temptation, reward, and punishment payoffs in the cooperation condition. | [game-theory-and-nrr.md](../02-research/game-theory-and-nrr.md) |

### Retrospective measures

| Symbol | Meaning | Defined in |
|---|---|---|
| FAR | Friction Allocation Ratio. Share of implementation effort spent before signature. | [Friction Efficiency Index](../../practice/friction-efficiency-index.md) |
| BCV | Buyer Commitment Velocity. How fast the buyer mobilized. | [Friction Efficiency Index](../../practice/friction-efficiency-index.md) |
| RMS | Risk Mitigation Score. Share of discovered risk closed before signature. | [Friction Efficiency Index](../../practice/friction-efficiency-index.md) |
| SVI | Scope Variance Index. Scope stability through delivery. | [Friction Efficiency Index](../../practice/friction-efficiency-index.md) |
| $H_{pre}$, $H_{post}$ | Solutions-engineering and implementation hours before and after signature. | [Friction Efficiency Index](../../practice/friction-efficiency-index.md) |

### Retired in Constitution 4.0

None of these survives in `models/tcg_models.py`. [02-mathematical-models.md](./02-mathematical-models.md) section 7 records why each went.

<!-- vale TCG.RetiredTerms = NO -->
| Symbol | What it was | What replaced it |
|---|---|---|
| $S$, $OC_{switching}$ | The single Deal Surplus and its opportunity-cost term | $S_b$ and $S_s$, and $V_{switch}(t)$ |
| $y$ | Reduced-form perceived transaction cost, $a\hat{\Delta}_A^2 + c$ | Nothing. Verification now beats discounting because a discount moves $P$, which cancels, and verification lowers $\pi_p$ |
| $a$, $b$, $c$ | The coupling anchored at 2.25, the base friction growth rate, and direct cost | Nothing for $a$ and $b$. What $c$ held is price, now $P$ |
| $D(t)$ | A deal's trajectory, transaction cost against opportunity cost | The two conditions over time |
| $k$, $k_{threshold}$ | Specificity as a level, and its boundary at 15 of 30 | Specific exposure, read under Axiom III |
| $F_{deployed}$ | Friction deployed, required to scale with $k$ | The seller's investment $I^s_k$ (Axiom II), and governance only where something specific is sunk (Axiom III) |
| $\mathbf{F}$, $\hat{\mathbf{F}}$, $\lVert \mathbf{F} \rVert_1$ | The friction vector, its direction shares and its summed level | The positions $r_k$. The sale starts at the largest |
| $F_{base}$, $F_{effective}$ | Summed cost, and cost after the per-component multiplier $(1 + \hat{\Delta}_k)$ | Nothing. The costs are never summed and the gaps multiply nothing |
| $\hat{\Delta}_A$ | The deal-level gap, the friction-weighted mean of the three | Nothing. Each gap is read in its own pair, and $\hat{\Delta}_{implementation}$ is the normalized $\Delta_A$ |
| $\gamma$ (bare) | Deal-level drift, the friction-weighted mean of the $\gamma_k$ | $\gamma_k$ |
| $\hat{\Delta}_k(0) + \gamma_k t$ | Linear drift, unbounded | Bounded drift toward a ceiling |
<!-- vale TCG.RetiredTerms = YES -->

---

## Symbol disambiguation

Seven groups look alike and mean different things. Each has produced a documented error, required an inline correction somewhere in this repo, or was caught during drafting before it could.

**1. $\gamma$ carries three unrelated meanings, and one of them has three subscripts of its own.** In the Constitution, $\gamma_k$ is the rate at which a gap rebuilds over time, one rate per cost: $\gamma_{search}$, $\gamma_{consensus}$, $\gamma_{implementation}$. In the mathematical models the letter appears twice more, as $\gamma_r$ (responsiveness to an external catalyst) and $\gamma_{TO}$ (the technical overlap weight). The subscripts are load-bearing, and the two families are told apart by what the subscript names: a cost, or a mechanism. Bare $\gamma$, the deal-level average, retired with the deal-level gap.

**2. $\delta$ and $\delta_{discount}$ are unrelated.** Bare $\delta$ is the urgency decay rate, and it belongs to the value-decay half of the Decay Clock, a standing assumption. $\delta_{discount}$ is a party's weight on future payoffs, and it belongs to the cooperation condition in Axiom III's frequency corollary. They share a letter and nothing else. A rising $\delta$ is bad for the deal, and a rising $\delta_{discount}$ is good for it. A third rate joins them in [04-seller-surplus-model.md §7](./04-seller-surplus-model.md): $\rho$ discounts the seller's future cash flows and is set by finance policy, where $\delta_{discount}$ describes how much a party actually weighs its future and is a behavioural fact about them.

**3. $\Delta_A$ and $\hat{\Delta}_{implementation}$ differ by an order of magnitude, and neither is the deal's gap.** The [Asymmetry Scorecard](../../practice/asymmetry-scorecard.md) produces a raw score on $[2, 10]$ that must be normalized before any equation accepts it. Raw scores drive the scorecard's field triage bands, and normalized values go into equations. The normalization and its rationale live in [02-mathematical-models.md §2.5](./02-mathematical-models.md). Separately, what the scorecard measures is the policing and enforcement cost's gap alone, the implementation gap in field terms, because that is the only pair that is buyer against seller. Constitution 4.0 retired the deal-level mean $\hat{\Delta}_A$, so there is no single deal gap to substitute the scorecard's output for. Each party's loss reads its own half.

**4. Five quantities are written with $I$.** $I^b_k$ and $I^s_k$ are investments today, in contract value, under Axiom II. $I_{buyer}$ and $I_{seller}$ are the two halves of the implementation gap under Axiom III. $I_i$ is one decision role's utility from the initiative, on $[-1, 1]$. A superscript party and a subscript cost mark an investment. A subscript party marks uncertainty. A subscript index marks a role.

**5. $P$, $r$ and $Q$ each carry two meanings.** $P$ is price in the two conditions and the punishment payoff in the cooperation condition. $r_k$ is a cost's position between its thresholds, and $r_t$ is the probability the relationship is live in period $t$. $Q_p$ is party $p$'s whole quasi-rent and $Q_m$ is the part sunk at gate $m$, while bare $Q$ in the seller surplus model is the seller's $Q_s$. Read the subscript before the letter.

**6. The $C$ terms carry their party.** $C_{deliver}$ and bare $C_{invest}$ are what the seller spends. $C^{p}_{invest}$ is what either party sinks, and for the buyer it is the integration built and the workflows rewired. $V_{contract}$ is seller revenue, the price $P$ seen from the seller's side, and not a value the buyer receives. A figure quoted without its party is unreadable.

**7. Four surpluses and three probabilities share letters.** $S_b$ and $S_s$ are the two conditions of Part III, and both must hold. $S_{seller}$ is the seller surplus model's form of $S_s$. $S_m$ is neither: it is the buyer's expected surplus at one milestone stage. Likewise $p_{close}$ is the probability a deal closes, $p_m$ is the probability a stage completes, and $\pi_p$ is the chance a party's exposure does not come back. The $p_{close}$ and $p_m$ pair was caught while drafting [04-seller-surplus-model.md](./04-seller-surplus-model.md) rather than in use.

---

## Term index

One line each, then the canonical source. The line identifies the term. The source defines it.

### The three decisions

| Term | Identifier | Canonical source |
|---|---|---|
| **Axiom I, Law of Transaction Cost Composition** | Should I use the market? The buyer's three costs beyond price, a participation threshold for each, and where the sale starts. | [Constitution, Part I](./00-tcg-constitution.md) |
| **Axiom II, Law of Transaction Investment** | What will it cost me today? Each cost is paid down by investment from either party, and each goes ahead only when its own share is covered. | [Constitution, Part I](./00-tcg-constitution.md) |
| **Axiom III, Law of Future Cost** | What might it cost me later? Specific investment exposes a party to what it cannot verify, and the allocation is settled before the investment is sunk. | [Constitution, Part I](./00-tcg-constitution.md) |

### Definitions

*Market* and *deal* keep their ordinary meanings and are not Definitions.

| Term | Identifier | Canonical source |
|---|---|---|
| **Workflow** | The procedure a product changes. A product is an encoded reference workflow, and the buyer's distance from it is what makes an investment specific under Axiom III. | [Constitution, Definitions](./00-tcg-constitution.md) |
| **Decision role** | A position in the buyer's organization holding a veto or an evaluation over the purchase, defined by its relation to the workflow and not by its occupant. An occupant change reopens a gap. A role dissolving changes the coalition. | [Constitution, Definitions](./00-tcg-constitution.md) |

### Component names

Coase (1937) owns the question, whether to use the market at all. Dahlman (1979) supplied the three names, which are canonical in theory prose. The field names stay, and so do the notation subscripts.

| Dahlman's name (canonical in theory) | Field name (notation subscript) | What B2B adds |
|---|---|---|
| **Search and information** | search | Reachability. |
| **Bargaining and decision** | consensus | The buyer is a coalition, so most of the bargain is internal, among the decision roles. |
| **Policing and enforcement** | implementation | The buyer cannot police performance until the product is adapted to its environment, so the question becomes whether it will work here. The buyer's adaptation work is an Axiom II investment against this cost, not the cost itself. |

### Axiom I concepts

| Term | Identifier | Canonical source |
|---|---|---|
| **Participation threshold** | The point on one cost above which the buyer does not enter the market, whatever the other two read. | [Constitution, Axiom I](./00-tcg-constitution.md) |
| **Self-serve threshold** | The point on one cost below which the buyer pays it down alone. | [Constitution, Axiom I](./00-tcg-constitution.md) |
| **Position and zone** | Where a cost sits between its own two thresholds, read as self-serve, needs investment, or keeps the buyer out. | [Deal Triage Calculator](../../practice/deal-triage-calculator.md) |
| **Where the sale starts** | The cost nearest its own participation threshold, the largest position. Two at the same position are run together. Names the motion. | [Constitution, Axiom I](./00-tcg-constitution.md), [01-motions.md](./01-motions.md) |
| **Turnkey** | A market condition: every cost self-serve and nothing specific sunk. It erodes through entry. | [Constitution, Axiom I corollaries](./00-tcg-constitution.md) |
| **Chaos Trap** | A buyer with no documented workflow, where the product automates the process. Route to consulting, not to a motion. | [Deal Triage Calculator, Step 0](../../practice/deal-triage-calculator.md) |
| **Akerlof Exit Threshold** | The research form of buyer exit under adverse selection. The framework states exit as the participation threshold. | [costly-signals.md](../02-research/costly-signals.md) |
| **Jevons Vulnerability** | A channel whose filtering ran on production cost, and which therefore collapses when that cost falls. | [channel-collapse.md](../02-research/channel-collapse.md) |

### Axiom II concepts

| Term | Identifier | Canonical source |
|---|---|---|
| **The two conditions** | One per party, $S_b$ and $S_s$. A deal happens when both are positive and no cost keeps the buyer out. | [Constitution, Part III](./00-tcg-constitution.md) |
| **Price as a transfer** | Price cancels when the two conditions are added, so it is not a transaction cost. | [Constitution, Axiom II corollaries](./00-tcg-constitution.md) |
| **Make-or-buy boundary** | $V_{next\_best}$ read as Coase's founding question. A deal closes only when buying beats integrating, net of what transacting costs. | [05-governance-forms.md](./05-governance-forms.md) |
| **Cost to serve is directional** | The seller's investment falls on whichever cost it pays down, so two markets with the same cost of sale can demand it in different places. | [Constitution, Axiom II corollaries](./00-tcg-constitution.md) |
| **Pursuit** | The seller's condition asked of a population: whether buyers' contract value and frequency can recover the investment their costs demand. | [04-seller-surplus-model.md](./04-seller-surplus-model.md) |

### Axiom III concepts

| Term | Identifier | Canonical source |
|---|---|---|
| **Specific exposure** | Whether a deal sinks anything worth less outside this relationship. The calculator reads it as none or specific. | [Constitution, Axiom III](./00-tcg-constitution.md), [Deal Triage Calculator, Step 2](../../practice/deal-triage-calculator.md) |
| **Appropriable quasi-rent** | What a party has sunk less what it could recover elsewhere. Whoever sinks it is the exposed party. | [klein-crawford-alchian.md](../02-research/klein-crawford-alchian.md) |
| **The gate** | Where nothing specific is sunk and a trial verifies fit, market terms hold. Apparatus below it is over-frictioning. | [Constitution, Axiom III corollaries](./00-tcg-constitution.md) |
| **Frequency** | How often the same two parties transact. One-shot, recurrent, or continuous. With specific exposure, selects the governance form. | [05-governance-forms.md](./05-governance-forms.md) |
| **Governance Form** | The shape of the arrangement that holds the deal. Market, trilateral, bilateral, or unified. | [05-governance-forms.md](./05-governance-forms.md) |
| **Stakes corollary** | Every party holding exposed rent, or adjudicating it, needs a stake, including the seller's own agents and the channel. | [Constitution, Axiom III corollaries](./00-tcg-constitution.md) |
| **Williamson Hold-Up** | Once asset-specific investment is sunk, the other party can extract its value. | [transaction-cost-economics.md](../02-research/transaction-cost-economics.md) |
| **Residual Control Rights** | The pre-agreed authority to decide in states no contract specified. | [incomplete-contracts.md](../02-research/incomplete-contracts.md) |
| **Staged Commitment** | Why commitment to a specific investment must be staged, with a right to stop at each gate. | [Constitution, Axiom III corollaries](./00-tcg-constitution.md) |
| **Real Option** | The economic value of being able to defer an irreversible decision under uncertainty. | [real-options.md](../02-research/real-options.md) |
| **Three levers** | Discount, take risk back, or verify. A discount never raises the joint surplus. Taking risk back raises it only by what it changes in the seller's conduct and what it reveals about which seller it is, both of which lower the chance of loss. | [Constitution, Axiom III corollaries](./00-tcg-constitution.md) |
| **Friction Allocation Principles** | The four conditions a signal mechanism must satisfy to reduce a gap. | [Constitution, Axiom III corollaries](./00-tcg-constitution.md) |
| **Single Crossing Property** | A signal informs only when it costs the high-quality actor proportionally less. | [costly-signals.md](../02-research/costly-signals.md) |
| **Cheap Talk** | A signal that fails the Single Crossing Property and therefore carries no information. | [Constitution, Axiom III](./00-tcg-constitution.md) |
| **Reputation Depreciation** | Past signals lose value without intervening evidence of continued delivery, so credibility must be re-earned. The rebuild clause after signature. | [Constitution, Axiom III corollaries](./00-tcg-constitution.md) |
| **Decay Clock** | Value decaying from the trigger while the gaps rebuild, both pushing the conditions toward zero. | [Constitution, Axiom III corollaries](./00-tcg-constitution.md) |
| **Handoff Rule** | The Blueprint must reach Customer Success intact, or the implementation gap $\Delta_A$ resets on the receiving side. | [04-sustaining-adoption-review.md](../../practice/implementation-motion/04-sustaining-adoption-review.md) |

### Artifact vocabulary

| Term | Identifier | Canonical source |
|---|---|---|
| **Contextual Blueprint** | Discovery artifact that reduces Seller Ignorance. | [01-discovery-contextual-blueprint.md](../../practice/implementation-motion/01-discovery-contextual-blueprint.md) |
| **Red Team** | Pre-mortem workshop that reduces Buyer Uncertainty. | [02-validation-red-team-protocol.md](../../practice/implementation-motion/02-validation-red-team-protocol.md) |
| **Mutual Implementation Plan (MIP)** | The bilateral governance instrument that distributes decision authority and stages commitment. | [03-closing-mutual-implementation-plan.md](../../practice/implementation-motion/03-closing-mutual-implementation-plan.md) |
| **Sustaining Adoption Review** | The post-signature artifact. Handoff packet, RE-AIM review, QBR protocol, and renewal evidence. | [04-sustaining-adoption-review.md](../../practice/implementation-motion/04-sustaining-adoption-review.md) |
| **Count Variance** | The triage counts re-taken at the Adoption Review against the counts taken at triage. The instrument's audit on itself. | [Deal Triage Calculator](../../practice/deal-triage-calculator.md) |
| **Vested Commission** | Comp structure tying rep payout to outcomes rather than signature. | [05-governance-forms.md](./05-governance-forms.md) section 5 |

### External frameworks

| Term | Identifier | Canonical source |
|---|---|---|
| **CFIR** | Implementation-science framework for reading a buyer's organization pre-sale. | [cfir.md](../02-research/cfir.md), mapped in [cfir-field-mapping.md](../../practice/cfir-field-mapping.md) |
| **RE-AIM** | Five-dimension framework for post-sale success measurement. | [re-aim-framework.md](../02-research/re-aim-framework.md) |
| **NRR** | Net Revenue Retention. The lagging indicator of the four upstream RE-AIM dimensions. | [re-aim-framework.md](../02-research/re-aim-framework.md) |

### Retired terms

Kept so older analyses stay readable. Do not use these in new writing.

<!-- vale TCG.RetiredTerms = NO -->
| Retired term | Use instead |
|---|---|
| Law of Asset Specificity (Axiom II until 4.0) | Axiom III, Law of Future Cost. Axiom II is now the Law of Transaction Investment |
| Law of Uncertainty Inflation (Axiom III until 4.0) | Axiom III, Law of Future Cost |
| Market level, workflow level, deal level | The three decisions, in time order |
| Market and deal as Definitions | Ordinary words. Only workflow and decision role are Definitions |
| Seat, seat map, seat ledger | Decision role, decision-role map, decision-role ledger |
| Coase's names: search, bargaining, enforcement | Dahlman's names: search and information, bargaining and decision, policing and enforcement |
| Structural deal | A deal with specific exposure, or a deal outside Turnkey, by meaning |
| Turnkey deal, as a level below 15 | Turnkey, a market condition |
| Level, magnitude, the 0 to 30 sum | How much seller investment the deal needs (Axiom II), or specific exposure (Axiom III), by meaning |
| Direction, shares, dominant component, dominance threshold, Composed | Where the sale starts. Ties are run together |
| The cost that binds | The cost nearest its own participation threshold |
| Boundary Condition | The gate |
| Amplification, the per-component multiplier | Nothing. Gaps feed the chance of future loss |
| The Surplus equation | The two conditions |
| Under-frictioned | Unallocated |
| Mis-composed | Mis-sequenced (a deal) or imitation (an organization) |
<!-- vale TCG.RetiredTerms = YES -->

---

## Maintaining this file

- **New symbol introduced anywhere:** add a row to the notation index in the same commit.
- **New concept that two or more directories reference:** add a row to the term index, pointing at its canonical home. Do not define it here. A term used in one file belongs in that file and not here.
- **A term is renamed or retired:** move the row to the retired table, and add the old name to the retired-terms lint rule, so the rename cannot drift back.
- **An entry disagrees with its source:** the source wins. Fix the entry.

## Related

- [00-tcg-constitution.md](./00-tcg-constitution.md) supplies the axioms and the corollaries most term entries point to.
- [02-mathematical-models.md](./02-mathematical-models.md) supplies the functional forms. [06-calibration.md](./06-calibration.md) carries every parameter and its provenance.
- [01-motions.md](./01-motions.md) derives the motions from where the sale starts and carries the incumbent-vocabulary map.
