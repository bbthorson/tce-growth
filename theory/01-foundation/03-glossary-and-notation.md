---
title: "Glossary and Notation"
layer: theory
status: active
version: 1.0
---

# Glossary and Notation

**Version:** 1.0
**Purpose:** To supply one place to look up any symbol or term used in this repo, and to say where its canonical definition lives.

## How to use this file

Two rules govern what is written here, and they differ by section.

**The term index is an index, not a source of truth.** Every entry carries a one-line identifier and a link to where the concept is actually defined. The identifier exists so you can confirm you found the right entry, not so you can skip reading the source. If an entry and its linked source disagree, **the source wins** and the entry is a bug. Report it or fix it.

**The notation index is canonical.** Symbols had no home before this file. Several are reused across documents with different meanings, and one collision was serious enough that [02-mathematical-models.md](./02-mathematical-models.md) had to stop mid-derivation to disambiguate it by hand. That is the gap this section closes. When a document introduces a new symbol, add it here in the same commit.

---

## Notation index

### The Surplus equation

| Symbol | Meaning | Defined in |
|---|---|---|
| $S$ | Deal Surplus. Must exceed 0 for a deal to close. | [Constitution, Part III](./00-tcg-constitution.md) |
| $OC_{switching}$ | Opportunity cost of staying with the status quo. Equals $V_{effective}(t) - V_{next\_best}$. | [Constitution, Part III](./00-tcg-constitution.md) |
| $y$ | Total perceived transaction cost, reduced form. Equals $a\hat{\Delta}_A^2 + c$, in annual contract values. | [Constitution, Axiom III](./00-tcg-constitution.md) |
| $D(t)$ | A deal's trajectory through time, $TC(t) - OC(t)$. Stays below the ceiling only while Axiom II holds. Carries a direction, since its cost term is the friction vector. | [Constitution, Axiom II](./00-tcg-constitution.md) |

### Seller-side terms

| Symbol | Meaning | Defined in |
|---|---|---|
| $S_{seller}$ | Seller surplus. Must exceed 0 for the deal to be worth pursuing, independently of $S$. | [04-seller-surplus-model.md §2](./04-seller-surplus-model.md) |
| $C_{invest}$ | Pre-signature, deal-specific engineering. Sunk whether or not the deal closes. | [04-seller-surplus-model.md §2](./04-seller-surplus-model.md) |
| $C_{deliver}$ | Post-signature cost to deliver what was sold. Contingent on revenue. | [04-seller-surplus-model.md §2](./04-seller-surplus-model.md) |
| $V_{contract}$ | Contract value the seller receives. **Seller revenue, not buyer cost.** | [04-seller-surplus-model.md §2](./04-seller-surplus-model.md) |
| $p_{close}$ | Probability the deal closes given the investment made. Not the same as $p_m$. | [04-seller-surplus-model.md §2](./04-seller-surplus-model.md) |
| $Q$ | Appropriable quasi-rent. The seller's unprotected exposure, $C_{invest} - R_{redeploy}$. | [04-seller-surplus-model.md §3](./04-seller-surplus-model.md) |
| $R_{redeploy}$ | Value of pre-signature work redeployed to other deals. **Not $R$, the reward payoff.** | [04-seller-surplus-model.md §3](./04-seller-surplus-model.md) |
| $p_m$ | Probability of achieving milestone stage $m$. | [Milestone Valuation Model](../../practice/milestone-valuation-model.md) |
| $S_m$ | Expected surplus at milestone stage $m$. A buyer-side quantity. | [Milestone Valuation Model](../../practice/milestone-valuation-model.md) |
| $r_t$ | Probability the relationship is live in period $t$. $r_1$ equals $p_{close}$. | [04-seller-surplus-model.md §7](./04-seller-surplus-model.md) |
| $C_{sustain}$ | Ongoing relationship investment per period. Holds $\gamma$ down; distinct from $C_{deliver}$. | [04-seller-surplus-model.md §7](./04-seller-surplus-model.md) |
| $\rho$ | Discount rate on future periods. **A policy choice, not $\delta_{discount}$.** | [04-seller-surplus-model.md §7](./04-seller-surplus-model.md) |

### Value terms (second standing assumption)

| Symbol | Meaning | Defined in |
|---|---|---|
| $V_{solution}$ | Peak perceived value at the triggering event. | [Constitution, standing assumptions](./00-tcg-constitution.md) |
| $V_{effective}(t)$ | Value after decay. Equals $V_{solution} \cdot e^{-\delta t}$. | [Constitution, standing assumptions](./00-tcg-constitution.md) |
| $V_{next\_best}$ | Value of the buyer's next best alternative, including building it themselves. This is the make-or-buy boundary. | [Constitution, standing assumptions](./00-tcg-constitution.md) |
| $k$ | Asset specificity of the deal. | [Constitution, Axiom II](./00-tcg-constitution.md) |
| $k_{threshold}$ | The Structural / Turnkey boundary ($k = 15$ on a 0 to 30 level). Above it, direction selects the motion. | [Deal Triage Calculator](../../practice/deal-triage-calculator.md) |
| $F_{deployed}$ | The friction structure the seller actually deploys. Must scale with $k$. | [Constitution, Axiom II](./00-tcg-constitution.md) |

### Friction terms (Axioms I and III)

| Symbol | Meaning | Defined in |
|---|---|---|
| $\mathbf{F}$ | The friction vector. The three components treated as one object. | [01-motions.md §1](./01-motions.md) |
| $\hat{\mathbf{F}}$ | Direction. Each component's share of effective cost, summing to 1. Selects the motion. | [01-motions.md §1](./01-motions.md) |
| $\lVert \mathbf{F} \rVert_1$ | Level. Base friction summed. Sets the Turnkey and Structural boundary. Equals $F_{base}$. | [01-motions.md §1](./01-motions.md) |
| $F_{base}$ | The three cost components summed, before amplification. | [Constitution, Axiom III](./00-tcg-constitution.md) |
| $F_{effective}$ | Friction after amplification. Equals $\sum_k F_k (1 + \hat{\Delta}_k)$, which factors into $F_{base}(1 + \hat{\Delta}_A)$. | [Constitution, Axiom III](./00-tcg-constitution.md) |
| $F_{search}$ | Cost of locating the category and viable vendors. Splits into category search and vendor evaluation. | [01-motions.md](./01-motions.md) |
| $F_{consensus}$ | Internal buyer alignment plus external bargaining. | [02-mathematical-models.md](./02-mathematical-models.md) |
| $F_{implementation}$ | Deployment plus sustained change. | [Constitution, Axiom III](./00-tcg-constitution.md) |

### Asymmetry terms (Axiom III)

| Symbol | Meaning | Defined in |
|---|---|---|
| $\Delta_A$ | Bilateral Asymmetry Gap. A **sum**, not a difference: $I_{seller} + I_{buyer}$. | [02-mathematical-models.md §2.1](./02-mathematical-models.md) |
| $\hat{\Delta}_A$ | The deal-level gap on $[0, 1]$. The friction-weighted mean of the three component gaps. **Required before substituting into either cost equation.** | [02-mathematical-models.md §1.1](./02-mathematical-models.md) |
| $\hat{\Delta}_k$ | A component's own gap on $[0, 1]$, for $k$ in search, consensus, implementation. Three different pairs of parties. | [02-mathematical-models.md §2.4](./02-mathematical-models.md) |
| $\Delta_A^*$ | Akerlof Exit Threshold. Above it the buyer leaves the market entirely. | [costly-signals.md](../02-research/costly-signals.md) |
| $I_{seller}$ | Seller Ignorance. What the seller has not mapped about the buyer's environment. | [02-mathematical-models.md §2.2](./02-mathematical-models.md) |
| $I_{buyer}$ | Buyer Uncertainty. Doubt about return variance and vendor capability. | [02-mathematical-models.md §2.3](./02-mathematical-models.md) |
| $x_m$ | Residual uncertainty **entering** milestone stage $m$, already normalized. Not a separate quantity from $\hat{\Delta}_{implementation}$, which is where the chain starts. | [Milestone Valuation Model](../../practice/milestone-valuation-model.md) |

### Coefficients and parameters

| Symbol | Meaning | Default | Defined in |
|---|---|---|---|
| $a$ | Friction-asymmetry coupling. Anchored at 2.25 by analogy, not measurement. | 2.25 | [02-mathematical-models.md §1.6](./02-mathematical-models.md) |
| $b$ | Rate at which base friction grows per unit of asymmetry. The derivation identifies $a$ with $b$. | measured | [02-mathematical-models.md §1.3](./02-mathematical-models.md) |
| $c$ | Direct cost. The irreducible floor of licence fees and unavoidable deployment work. | measured | [Constitution, Axiom III](./00-tcg-constitution.md) |
| $\lambda$ | Loss aversion coefficient from prospect theory. **Not the same quantity as $a$.** | 2.25 | [prospect-theory.md](../02-research/prospect-theory.md) |
| $\alpha$ | Baseline coordination overhead in the consensus model. | 1.0 | [02-mathematical-models.md §3.1](./02-mathematical-models.md) |
| $\beta$ | Organizational complexity exponent. Above 1 because channels grow as $N(N-1)/2$. | 1.35 | [02-mathematical-models.md §3.1](./02-mathematical-models.md) |
| $N$ | Stakeholders holding veto power or evaluation responsibility. | measured | [02-mathematical-models.md §3.1](./02-mathematical-models.md) |
| $I_i$ | Stakeholder $i$'s utility from the initiative, on $[-1, 1]$. | measured | [02-mathematical-models.md §3.2](./02-mathematical-models.md) |
| $\text{Var}(I_i)$ | Variance in stakeholder incentive alignment, bounded above by 1. | measured | [02-mathematical-models.md §3.2](./02-mathematical-models.md) |
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
| $\delta_{discount}$ | A party's discount factor. The weight it places on future payoffs. | [Constitution, Axiom II](./00-tcg-constitution.md) |
| $\gamma_k$ | Rate at which component $k$'s gap rebuilds per unit time, absent maintenance. Three rates with different drivers. | [Constitution, Axiom III](./00-tcg-constitution.md) |
| $\gamma$ | The deal-level drift rate. The friction-weighted mean of the three $\gamma_k$, and an average rather than a mechanism. | [Constitution, Axiom III](./00-tcg-constitution.md) |
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

---

## Symbol disambiguation

Seven groups look alike and mean different things. Each has produced a documented error, required an inline correction somewhere in this repo, or was caught during drafting before it could.

**1. $\gamma$ carries three unrelated meanings, and one of them has three subscripts of its own.** In the Constitution, $\gamma$ is the rate at which an asymmetry gap rebuilds over time, and there is one rate per component: $\gamma_{search}$, $\gamma_{consensus}$, $\gamma_{implementation}$. In the mathematical models the letter appears twice more, as $\gamma_r$ (responsiveness to an external catalyst) and $\gamma_{TO}$ (the technical overlap weight). The subscripts are load-bearing, and the two families are told apart by what the subscript names: a component, or a mechanism. A bare $\gamma$ always means deal-level asymmetry drift.

**2. $\delta$ and $\delta_{discount}$ are unrelated.** Bare $\delta$ is the urgency decay rate, and it belongs to the value-decay half of the Decay Clock, a standing assumption. $\delta_{discount}$ is a party's weight on future payoffs, and it belongs to Axiom II's cooperation condition. They share a letter and nothing else. A rising $\delta$ is bad for the deal, and a rising $\delta_{discount}$ is good for it. A third rate joins them in [04-seller-surplus-model.md §7](./04-seller-surplus-model.md): $\rho$ discounts the seller's future cash flows and is set by finance policy, where $\delta_{discount}$ describes how much a party actually weighs its future and is a behavioural fact about them.

**3. $\Delta_A$ and $\hat{\Delta}_A$ differ by an order of magnitude, and $\hat{\Delta}_A$ and $\hat{\Delta}_{implementation}$ differ by scope.** The [Asymmetry Scorecard](../../practice/asymmetry-scorecard.md) produces a raw score on $[2, 10]$ that must be normalized before either cost equation accepts it. Raw scores drive the scorecard's field triage bands, and normalized values go into equations. The normalization and its rationale live in [02-mathematical-models.md §1.5](./02-mathematical-models.md). Separately, what the scorecard measures is the implementation component's gap alone, because that is the only component whose pair is buyer against seller. $\hat{\Delta}_A$ is the friction-weighted mean across all three. Substituting the scorecard's output for $\hat{\Delta}_A$ treats one pair's gap as though it governed the deal.

**4. $a$, $b$, and $\lambda$ are three different quantities that all sit near 2.25, and only two of them carry units.** $\lambda$ is measured (prospect theory) and dimensionless, $b$ is the rate at which base friction grows per unit of asymmetry, and the derivation identifies $a$ with $b$, borrowing $\lambda$'s magnitude as justification rather than measurement. $a$ and $b$ are in annual contract values, per [02-mathematical-models.md §1.7](./02-mathematical-models.md). Do not cite $a$ as though prospect theory established it, and do not add it to a figure quoted in percentage points. The full account is [§1.6](./02-mathematical-models.md).

**5. $F_{base}$ and $F_{effective}$ differ by the multiplier, and level and direction are read off different ones.** $F_{base}$ is the three components summed. $F_{effective}$ is $\sum_k F_k (1 + \hat{\Delta}_k)$, which factors exactly into $F_{base}(1 + \hat{\Delta}_A)$. A third form appears inside the derivation, where base friction is written as a function of the gap, $F_{base}(\hat{\Delta}_A) = c + b\hat{\Delta}_A$. Level is the $L^1$ norm of base friction and direction is the share of effective cost, which is why discovery rotates a deal without reclassifying it. Quoting a friction figure without saying which form it is makes the number unusable.

**6. $c$ is a buyer cost and the $C$ terms are seller costs.** Lowercase $c$ is the direct cost the buyer pays, which is the seller's revenue. $C_{invest}$ and $C_{deliver}$ are what the seller spends. They sit on opposite sides of the transaction and a figure quoted without its case is unreadable. $V_{contract}$ has the same hazard: it is seller revenue, not a value the buyer receives.

**7. Three surpluses and two probabilities share letters.** Bare $S$ is the buyer's Deal Surplus from Part III. $S_{seller}$ is the seller's, and the two are independent conditions that must both hold. $S_m$ is neither: it is the buyer's expected surplus at one milestone stage. Likewise $p_{close}$ is the probability a deal closes and $p_m$ is the probability a stage completes. This pair was caught while drafting [04-seller-surplus-model.md](./04-seller-surplus-model.md) rather than in use.

---

## Term index

One line each, then the canonical source. The line identifies the term. The source defines it.

### The three levels

| Term | Identifier | Canonical source |
|---|---|---|
| **Market level** | Where a seller meets the category. Which cost binds, and therefore which motion. Axiom I. | [Constitution, Part I](./00-tcg-constitution.md) |
| **Workflow level** | Where a seller meets the buyer's operation. How specific the investment is, how much apparatus that needs, and when it must be spent. Axiom II. | [Constitution, Part I](./00-tcg-constitution.md) |
| **Deal level** | Where a seller meets the parties. What each cannot verify about their own outcome, before signature and again at renewal. Axiom III. | [Constitution, Part I](./00-tcg-constitution.md) |

### Component names

| Coase's name (canonical in theory) | Field name (notation subscript) | What B2B adds |
|---|---|---|
| **Search** | search | Reachability. |
| **Bargaining** | consensus | The buyer is a coalition, so the bargain is n-party and internal. |
| **Enforcement** | implementation | Specificity. The buyer's own sunk adaptation. |

### Deal classification

| Term | Identifier | Canonical source |
|---|---|---|
| **Structural Deal** | A deal whose level reaches the boundary. Level 15 to 30. | [Deal Triage Calculator](../../practice/deal-triage-calculator.md) |
| **Turnkey Deal** | A low-specificity deal that a velocity motion serves better. Level below 15. | [Deal Triage Calculator](../../practice/deal-triage-calculator.md) |
| **Chaos Trap** | A buyer with no documented workflow, in any market. Route to consulting, not to a motion. | [Deal Triage Calculator, Step 0](../../practice/deal-triage-calculator.md) |
| **Level** | The friction vector's $L^1$ length, on base friction. Sets the Turnkey and Structural boundary. | [01-motions.md](./01-motions.md) |
| **Frequency** | How often the same two parties transact. One-shot, recurrent, or continuous. Selects the governance form. | [05-governance-forms.md](./05-governance-forms.md) |
| **Governance Form** | The shape of the arrangement after signature. Market, trilateral, bilateral, or unified. | [05-governance-forms.md](./05-governance-forms.md) |
| **Make-or-buy boundary** | $V_{next\_best}$ read as Coase's founding question. A deal closes only when buying beats integrating, net of transaction cost. | [05-governance-forms.md](./05-governance-forms.md) |
| **Direction** | Each component's share of effective cost. Selects the instruments. Dominant at 0.50. | [01-motions.md](./01-motions.md) |
| **Count Variance** | Scored count against actual count, taken at the Adoption Review. The instrument's audit on itself. | [Deal Triage Calculator](../../practice/deal-triage-calculator.md) |
| **Boundary Condition** | The test every deal passes before heavy apparatus is justified. | [Constitution, Part I corollaries](./00-tcg-constitution.md) |

### Axiom III concepts

| Term | Identifier | Canonical source |
|---|---|---|
| **Friction Allocation Principles** | The four conditions a signal mechanism must satisfy to reduce $\Delta_A$. | [Constitution, Part I corollaries](./00-tcg-constitution.md) |
| **Single Crossing Property** | A signal informs only when it costs the high-quality actor proportionally less. | [costly-signals.md](../02-research/costly-signals.md) |
| **Costly Signal** | A demonstration a low-quality competitor could not afford to replicate. | [costly-signals.md](../02-research/costly-signals.md) |
| **Cheap Talk** | A signal that fails the Single Crossing Property and therefore carries no information. | [Constitution, Axiom III](./00-tcg-constitution.md) |
| **Safe No / Logical Yes** | The buyer's refusal to change, which risks nothing for the decider, versus the positive business case it defeats. | [Constitution, Axiom III](./00-tcg-constitution.md) |
| **Akerlof Exit Threshold** | The asymmetry level beyond which the buyer stops participating in the market. | [costly-signals.md](../02-research/costly-signals.md) |
| **Jevons Vulnerability** | A channel whose binding constraint is production cost, and which therefore collapses when that cost falls. | [channel-collapse.md](../02-research/channel-collapse.md) |
| **Buying Center** | The set of people in a purchase decision, each judging it against a different objective. | [buying-center-dynamics.md](../02-research/buying-center-dynamics.md) |
| **Decay Clock** | The two time dynamics that erode deal viability before close. | [Constitution, Part I corollaries](./00-tcg-constitution.md) |
| **Reputation Depreciation** | Past signals lose value without intervening evidence of continued delivery. Axiom III's second clause after signature. | [Constitution, Part I corollaries](./00-tcg-constitution.md) |

### Axiom II concepts

| Term | Identifier | Canonical source |
|---|---|---|
| **Recursive Cooperation** | The cooperation condition must hold for every party holding exposed rent or adjudicating it. Axiom II's stakes corollary. | [Constitution, Part I corollaries](./00-tcg-constitution.md) |
| **Demurrage on Credibility** | The prescription following from depreciation. Reputation must be re-earned to retain signal value. | [Constitution, Part I corollaries](./00-tcg-constitution.md) |
| **Williamson Hold-Up** | Once asset-specific investment is sunk, either party can extract its value. | [transaction-cost-economics.md](../02-research/transaction-cost-economics.md) |
| **Residual Control Rights** | The pre-agreed authority to decide in states no contract specified. | [incomplete-contracts.md](../02-research/incomplete-contracts.md) |
| **Staged Commitment** | Why bilateral commitments must be staged rather than merely mutual. | [Constitution, Part I corollaries](./00-tcg-constitution.md) |
| **Real Option** | The economic value of being able to defer an irreversible decision under uncertainty. | [real-options.md](../02-research/real-options.md) |
| **Handoff Rule** | The Blueprint must reach Customer Success intact, or $\Delta_A$ resets on the receiving side. | [04-sustaining-adoption-review.md](../../practice/implementation-motion/04-sustaining-adoption-review.md) |

### Artifact vocabulary

| Term | Identifier | Canonical source |
|---|---|---|
| **Contextual Blueprint** | Discovery artifact that reduces Seller Ignorance. | [01-discovery-contextual-blueprint.md](../../practice/implementation-motion/01-discovery-contextual-blueprint.md) |
| **Red Team** | Pre-mortem workshop that reduces Buyer Uncertainty. | [02-validation-red-team-protocol.md](../../practice/implementation-motion/02-validation-red-team-protocol.md) |
| **Mutual Implementation Plan (MIP)** | The governance instrument that distributes decision authority and stages commitment. | [03-closing-mutual-implementation-plan.md](../../practice/implementation-motion/03-closing-mutual-implementation-plan.md) |
| **Sustaining Adoption Review** | The post-signature artifact. Handoff packet, RE-AIM review, QBR protocol, and renewal evidence. | [04-sustaining-adoption-review.md](../../practice/implementation-motion/04-sustaining-adoption-review.md) |
| **Reciprocity Gate** | The artifacts a buyer must supply before discovery advances. | [01-discovery-contextual-blueprint.md](../../practice/implementation-motion/01-discovery-contextual-blueprint.md) |
| **Sacred Cow** | A politically protected workflow, tool, or team. | [01-discovery-contextual-blueprint.md](../../practice/implementation-motion/01-discovery-contextual-blueprint.md) |
| **The Casualty** | The stakeholder who loses power, budget, or status if the initiative succeeds. | [01-discovery-contextual-blueprint.md](../../practice/implementation-motion/01-discovery-contextual-blueprint.md) |
| **Negative Capability Declaration** | Stating platform limitations before signature, as a costly signal. | [01-discovery-contextual-blueprint.md](../../practice/implementation-motion/01-discovery-contextual-blueprint.md) |
| **Resource Expiry Clause** | The buyer-side hostage that makes buyer delay costly. | [03-closing-mutual-implementation-plan.md](../../practice/implementation-motion/03-closing-mutual-implementation-plan.md) |
| **Vested Commission** | Comp structure tying rep payout to outcomes rather than signature. | [05-governance-forms.md](./05-governance-forms.md) section 5 |

### External frameworks

| Term | Identifier | Canonical source |
|---|---|---|
| **CFIR** | Implementation-science framework for reading a buyer's organization pre-sale. | [cfir.md](../02-research/cfir.md), mapped in [cfir-field-mapping.md](../../practice/cfir-field-mapping.md) |
| **RE-AIM** | Five-dimension framework for post-sale success measurement. | [re-aim-framework.md](../02-research/re-aim-framework.md) |
| **NRR** | Net Revenue Retention. The lagging indicator of the four upstream RE-AIM dimensions. | [re-aim-framework.md](../02-research/re-aim-framework.md) |
| **JOLT Effect** | Research on buyer indecision, and why urgency tactics backfire on indecisive buyers. | [fear-of-failure.md](../02-research/fear-of-failure.md) |

---

## Maintaining this file

- **New symbol introduced anywhere:** add a row to the notation index in the same commit.
- **New concept that two or more directories reference:** add a row to the term index, pointing at its canonical home. Do not define it here.
- **A term is renamed or retired:** update the row, and add the old name to the retired-terms lint rule if this repo has one, so the rename cannot drift back.
- **An entry disagrees with its source:** the source wins. Fix the entry.

## Related

- [00-tcg-constitution.md](./00-tcg-constitution.md) supplies the axioms and the clarifying concepts most term entries point to.
- [02-mathematical-models.md](./02-mathematical-models.md) supplies the functional forms. [06-calibration.md](./06-calibration.md) carries every parameter and its provenance.
- [01-motions.md](./01-motions.md) derives the motions and carries the incumbent-vocabulary map in section 10.
