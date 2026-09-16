---
title: "The Constitution of Transaction Cost Growth (TCG)"
layer: theory
status: active
version: 2.3
---

# The Constitution of Transaction Cost Growth (TCG)

**Version:** 2.3
**Purpose:** To state the three claims from which everything else in this repository derives, each at the level where a seller meets it, each producing a decision, and each falsifiable on its own.

Version history is at the end of this document.

> [!IMPORTANT]
> **This document states structure. It states no measured quantity.** Every claim below says what depends on what, and each is argued from a mechanism. The coefficients, thresholds and band edges that turn those claims into numbers live in [06-calibration.md](./06-calibration.md), none of them is fitted, and a reader can reject any number there without rejecting the claim it sits inside.

---

## Standing assumptions

Three premises sit above the axioms. They are inherited rather than argued, and each is named here so a reader who rejects one knows what falls with it.

1. **Bounded rationality and opportunism** (Williamson 1985). No party can foresee every state the relationship will reach, so every contract is incomplete. And a party will exploit a gap once the other side's position is exposed. The first is why uncertainty has a price. The second is why safeguards exist.
2. **Value is exogenous to the seller, and it decays.** Willingness to pay is a property of the product and the buyer's situation. The seller's levers are the cost of transacting and the buyer's perception of it. Where value moves during a cycle it moves down, from the triggering event: $V_{effective}(t) = V_{solution} \cdot e^{-\delta t}$. This is a modeling assumption, stated in [02-mathematical-models.md](./02-mathematical-models.md) section 4, and the one term in $\delta$ a seller can touch is whether an external catalyst has been named.
3. **Every actor acts on their own payoff** (Jensen and Meckling 1976). That includes the seller's own representatives and every intermediary standing between the two parties. An actor whose payoff does not depend on the outcome behaves as though the outcome does not matter, whatever their intent.

![Two exponential decay curves falling toward a floor at the value of the next best alternative. Organizational inertia alone reaches the floor in the second month. A named external catalyst holds value above it until the eleventh.](./assets/value-decay.svg)

---

## Definitions

Four words the axioms use, each naming the unit at which one axiom is read. They are definitions rather than claims. A claim that follows from one is stated under its axiom.

- **Market.** The buyers who call a problem by one name. Axiom I is read here, and coarsely on purpose: which of the three costs dominates across that population, and so which motion a seller must build to serve it. The reading is a property of the buyers and not of any seller. Two sellers with different organizations read the same market and reach different answers on whether to pursue it, because what each pays to serve the vector differs.
- **Workflow.** The procedure a product changes. A product is an encoded reference workflow, and Axiom II is read here: how far the buyer's version sits from the reference is the specificity of the investment.
- **Seat.** A position in the buying coalition, defined by its relation to the workflow rather than by its occupant: who runs it, who owns it, who pays for it, who polices it. A seat holds a veto or an evaluation, is measured on something the change touches, and survives the person in it. The bargaining cost counts seats. A champion leaving is an occupant change on a stable seat, which is why the gap reopens without the cost changing.
- **Deal.** One buyer's divergence from the reference workflow, with the seats their version carries. Axiom III is read here: what each party to each cost cannot verify about their own outcome, at signature and again at renewal.

A market's name says how its buyers search and nothing about what they are buying. Which of those buyers a product can serve is decided one level down, at the workflow.

---

## Part I: The Three Axioms

Each axiom is stated at the level where a seller meets it, and each produces one decision.

| Axiom | Level | Statement | Decision it produces |
|---|---|---|---|
| **I. Law of Transaction Cost Composition** | **Market** | Every deal carries three costs beyond price, search, bargaining and enforcement, and the one that binds selects the motion. | Which instruments to run |
| **II. Law of Asset Specificity** | **Workflow** | The more specific the investment, the more a deal costs to transact, and the more of that cost must be paid before signature. | How much apparatus, when to spend it, what arrangement holds it, whether to decline |
| **III. Law of Uncertainty Inflation** | **Deal** | Each cost is inflated by what the parties to it cannot verify about their own outcome, and the inflation rebuilds over time unless it is maintained. | What to prove, in what order, and what to re-prove at renewal |

**The axioms are numbered in the order a seller meets them, and the second is the gate.** A seller encounters a market before a buyer's workflow and a workflow before a deal, so the numbering follows that path. Williamson's result is that specificity is the master variable: when the investment is not specific, the buyer can verify by trying and walk away at no cost, market terms hold, and the other two readings barely matter. Uncertainty and frequency start to bite only once specificity is present. Read the three in order, and treat Axiom II as the test that decides whether the rest applies.

**On the component names.** The three costs carry Coase's names in this document and throughout the theory. The field calls the second one *consensus* and the third *implementation*, and the notation keeps those subscripts, because the field names say what a seller experiences and Coase's names say why. [03-glossary-and-notation.md](./03-glossary-and-notation.md) carries the mapping.

---

### Axiom I — The Law of Transaction Cost Composition

> **Every deal carries three costs beyond price, search, bargaining and enforcement, and the one that binds selects the motion.**

*Plain English: buying costs more than money. Finding it, agreeing on it, and making it work are three separate bills. The largest bill tells you how to sell.*

*Origin: Coase (1937). Using the price mechanism is itself costly, and the cost comes in kinds.*

**Mechanism.** Coase identified three costs of using a market: discovering what is available and at what price, bargaining to an agreement, and policing performance after it. B2B software enlarges each in a specific way, and the enlargements are this framework's own rather than Coase's.

| Coase's cost | What B2B adds | Field name |
|---|---|---|
| **Search** | Reachability. A buyer can know the category and name five vendors and still be structurally unable to reach the seller without a channel. | Search |
| **Bargaining** | The buyer is a coalition, not an agent. The bargain is n-party and mostly internal, before any term is negotiated with the seller (Webster and Wind 1972). | Consensus |
| **Enforcement** | Specificity. The buyer's own sunk adaptation, workflow rewiring and integration work, which no remedy against the seller recovers. | Implementation |

The three are separately addressable rather than separately caused. A workflow the product must fit but does not raises the enforcement cost and generates a bargaining cost at the same time, because an imposition creates a stakeholder whose objectives worsen.

**Mathematical content.** Treat the three components as one object:

$$\mathbf{F} = (F_{search},\; F_{consensus},\; F_{implementation})$$

Two properties of that object carry the decision. Its **direction**, $\hat{\mathbf{F}} = \mathbf{F} / \lVert \mathbf{F} \rVert_1$, is which component dominates and by how much, and it selects the motion. Its **level**, $\lVert \mathbf{F} \rVert_1$, is how much cost there is in total, and Axiom II governs it. Direction is read from the components after Axiom III's amplification, because the cost that binds is the cost as the buyer perceives it. Do not read the total as a motion selector. Two deals of identical total, one sitting in search and one in enforcement, take different motions.

**Corollaries.**

- **A motion is a region, not a list entry.** The named motions are regions of the space $\mathbf{F}$ spans, and Product-Led, Sales-Led and Implementation-Led name the seller rather than the cost. Read by cost, the argument between them splits into two measurable questions. [01-motions.md](./01-motions.md) carries the derivation.
- **A sales organization is a division of labor over the three costs.** Business development reduces search, account executives reduce bargaining, solutions engineers reduce enforcement uncertainty. The standard org meets the costs in that fixed order, so a deal whose binding cost is enforcement gets its engineer last, at the demo, when it needed one first. And each handoff between roles is a seam where a cost gets paid twice, because what one role learned does not travel.
- **Cost to serve is directional.** The seller pays the mirror of each cost: reaching buyers, working the coalition, proving and delivering. Two markets with the same cost of sale can demand it in different components, so a motion is a decision about which cost an organization is built to pay, and an organization built to pay the wrong one is mis-composed before its first deal.
- **Addressable market is a property of the motion.** A seller who runs only short-vector instruments can transact only with short-vector buyers. The rest were never reachable. [05-governance-forms.md](./05-governance-forms.md) section 4.

**What would falsify it.** A deal whose binding cost is search closing reliably under enforcement instruments, or the reverse. The prediction is that a motion aimed at a cost that is not binding leaves the deal where it was, and that is observable in stage-to-stage conversion by dominant component.

**Failure mode.** Mis-composed. The collected table is in Part III.
---

### Axiom II — The Law of Asset Specificity

> **The more specific the investment, the more a deal costs to transact, and the more of that cost must be paid before signature.**

*Plain English: when the thing being bought only works here, for this buyer, the deal is expensive, and whoever is left holding it if the deal dies needs to see the risk resolved before they sign.*

*Origin: Williamson (1979, 1985). Specificity creates exposure, and exposure demands safeguards written before the investment is sunk.*

**Mechanism.** An investment is specific when it loses value outside this relationship. Once it is sunk, the party who made it can be held up, because the other side can extract the difference between what the investment is worth here and what it is worth anywhere else. Klein, Crawford and Alchian (1978) named that difference the appropriable quasi-rent and established that the exposure follows the investment rather than the invoice: whoever sinks the specific capital is the exposed party, buyer or seller.

In a software deal the buyer's post-signature cost has two halves, and the axiom's second clause rests on the distinction. One half is policing the seller's performance, which is enforcement in Coase's sense, and a contract can remedy it. The other half is the buyer's own adaptation, the workflows rewired and the integration built, and no clause against the seller recovers it because the buyer's investment is already gone. That second half is the fear that kills specific deals. It is not a fear that the seller will fail to perform. It is a fear of being left holding the investment, and the only thing that assuages it before signature is a process the buyer can inspect and a commitment that stages the exposure. Williamson (1983) calls these credible commitments, and they are ex ante by construction.

What governance allocates is residual control (Grossman and Hart 1986, Hart and Moore 1990). Contracts on specific transactions are incomplete as a structural matter, so states arise that nobody specified. What governs those states is the pre-agreed allocation of the right to decide, and a party who expects to be held up in them declines to sink the investment at all. That is why more legal review does not move a stalled specific deal.

**Mathematical content.** The level of the friction vector is the deal's specificity, read on base cost before any amplification, because specificity is a property of the deal and not of what anyone currently knows about it:

$$k = \lVert \mathbf{F} \rVert_1 = F_{search} + F_{consensus} + F_{implementation}$$

The boundary condition is $k > k_{threshold}$, separating Structural deals from Turnkey ones, and $F_{deployed} \sim k$, requiring the friction the seller deploys to scale with the specificity it manages. The threshold is chosen and [06-calibration.md](./06-calibration.md) says so.

The second clause, that the pre-signature share of the cost rises with $k$, is stated here in prose. The equation in Part III is a snapshot at signature and does not carry time, and the claim is deliberately left as a derivation beneath the axiom rather than a term inside the model until there is a reason to fit one. The [Friction Efficiency Index](../../practice/friction-efficiency-index.md) measures it in retrospect.

**Corollaries.**

- **Governance form.** With frequency, specificity selects the arrangement that holds the deal after signature. Below the boundary, market terms at any frequency. Above it, a one-shot transaction takes a third-party safeguard because neither side will build relational machinery for a single event, a recurring one takes bilateral governance where each repetition safeguards the next, and a continuous relationship of rising specificity eventually takes integration, which for the seller means the buyer builds it. The Mutual Implementation Plan is the bilateral form's instrument. [05-governance-forms.md](./05-governance-forms.md).
- **Frequency is partly the seller's choice.** Restructuring a one-shot sale as a subscription converts a single-play game into a repeated one, which brings the cooperation condition $\delta_{discount} > (T - R)/(T - P)$ within reach (Axelrod 1984) and lets a specific transaction be governed bilaterally rather than through an arbitrator. This is the framework's account of why subscription changed what could be sold, not only when it was paid for. [05-governance-forms.md](./05-governance-forms.md) section 5.
- **Commitment must be staged.** When an investment is irreversible and the environment uncertain, the right to wait has value, and a contract demanding full commitment at once asks the buyer to destroy it (Dixit and Pindyck 1994). Gating the commitment converts one irreversible decision into a sequence, each taken with more information, and preserves a priced right to stop. Hold-up explains why commitments must be mutual. Option value explains why they must be staged. The [Milestone Valuation Model](../../practice/milestone-valuation-model.md) is the instrument.
- **Every party holding exposed rent, or adjudicating it, needs a stake.** By the third standing assumption, a representative paid in full at signature plays the seller's side of a repeated game with a one-shot payoff, and a channel with no exposure to the outcome drifts from adjudication toward extraction. Vesting compensation on outcomes that survive signature is the seller's own safeguard. [05-governance-forms.md](./05-governance-forms.md) section 5.
- **Who bears the specificity decides who needs the safeguard.** In a forward-deployed motion the seller sinks the specific investment before signature, and the exposure is the seller's. [04-seller-surplus-model.md](./04-seller-surplus-model.md) carries that side of the transaction.
- **A product that cannot name its workflow has not chosen its market.** Specificity is read as divergence from the reference workflow the product encodes. A product that claims a category and names no workflow has no reference to read divergence against, so neither its specificity nor the apparatus it needs can be known. The gate applies to the seller before it applies to any buyer.
- **Pursuit is amortizability at market level.** Whether a market is worth entering is the deal question asked of a population: can the buyers' contract value and frequency recover the spend their vector demands from this seller. A seller that cannot recover it declines the market rather than running the motion lighter, for the same reason a Structural one-shot deal is declined rather than under-frictioned. [04-seller-surplus-model.md](./04-seller-surplus-model.md).

**What would falsify it.** A population of highly specific deals that closed on light pre-signature work and kept their surplus through renewal. The prediction is that such deals close and then fail to deploy, so the failure lands in retention rather than in win rate, and it is observable in churn by specificity at signature.

**Failure modes.** Under-frictioned before and after signature, over-frictioned, mis-governed, and defection. The collected table is in Part III.
---

### Axiom III — The Law of Uncertainty Inflation

> **Each cost is inflated by what the parties to it cannot verify about their own outcome, and the inflation rebuilds over time unless it is maintained.**

*Plain English: what nobody in the room can verify, they price as risk, and the risk multiplies the bill it attaches to. Three bills, three rooms, three separate things nobody can verify. And what was verified last quarter is not verified now.*

*Origin: Akerlof (1970) and Spence (1973). Unverifiable quality drives buyers out of a market, and a signal separates quality only when it costs something to send.*

**Mechanism.** Each of the three costs runs between its own pair of parties, and what inflates it is each party's uncertainty about what the transaction does to *them*.

| Component | Whose uncertainty, about what | What resolves it |
|---|---|---|
| Search | The buyer's, about the market. Which alternatives exist and whether this one fits. | Artifacts that travel without the seller: category definition, reference architectures, verifiable proof, a channel with a stake |
| Bargaining | Each stakeholder's, about their own outcome. What the change does to their budget, headcount and standing. | Mapping who loses what, and surfacing the objections in a room built to hear them |
| Enforcement | Bilateral. The seller's, about the buyer's environment. The buyer's, about the seller's capability. | Discovery that maps the environment, and demonstrations the seller pays to produce |

Only the third pair is buyer against seller, which is why an instrument built for that pair does not move the other two. The second pair is not an information gap between stakeholders that proof could close. Two stakeholders with perfect knowledge of each other and opposed interests still disagree. What proof can close is each stakeholder's uncertainty about their own exposure, and that is the inflation this axiom names on the bargaining cost.

A signal resolves uncertainty only when it costs the sender something a low-quality sender could not afford. This is Spence's single crossing property, and it is why volume is not verification: a message that costs nothing to send carries no information, and a channel full of them degrades for the costly signals too. How heavily the remaining uncertainty is weighed is a question of loss aversion (Kahneman and Tversky 1979). The framework anchors the weighting on their coefficient by analogy, and [06-calibration.md](./06-calibration.md) records how far the analogy stretches.

**Mathematical content.** Each component is amplified by its own pair's normalized gap:

$$F_{effective} = \sum_{k} F_k \,(1 + \hat{\Delta}_k), \qquad \hat{\Delta}_k \in [0, 1]$$

The sum factors exactly into $F_{base}(1 + \hat{\Delta}_A)$ when $\hat{\Delta}_A$ is the friction-weighted mean of the three, so the single-multiplier form is a shorthand and not a rival. What the single multiplier cannot do is rotate the vector: scaling every component by one factor changes its length and leaves its direction untouched, so under that form no amount of discovery could change which motion a deal needs. Per-component amplification is what lets a Blueprint change the shape of a deal and not only its size.

Collapsed to a scalar, the buyer's perceived cost is

$$y = a\hat{\Delta}_A^2 + c$$

with $y$, $a$ and $c$ all in annual contract values, so that at a fully open gap the uncertainty term is $a$ contract values against a price of $c$. The square is the simplest convex shape and nothing here depends on it being a square. The reduced form explains and does not diagnose, because it has discarded direction.

Absent maintenance, each gap rebuilds at its own rate:

$$\hat{\Delta}_k(t) = \hat{\Delta}_k(0) + \gamma_k t$$

Discovery and drift are one mechanism with opposite signs. A champion leaving is $\gamma_{consensus}$ arriving all at once, and a deal can leave the viable zone with no change in product, price or technical work.

![A convex cost curve rising steeply as the asymmetry gap widens, a discounted curve shifted down by a constant amount without changing shape, and a straight line showing what a linear cost of uncertainty would look like instead.](./assets/axiom-3-cost-convexity.svg)

![Two rising lines from a near-zero implementation gap at go-live, against a horizontal line marking where a challenger begins. The unmaintained line approaches the challenger within three years. The maintained line stays well below it.](./assets/axiom-3-asymmetry-drift.svg)

**Corollaries.**

- **The Friction Allocation Principles.** A mechanism reduces a gap only if its cost cannot be automated away, is borne by the claimant rather than the receiver, scales with the size of the claim, and is adjudicated by someone who loses when a bad signal passes. Violate any one and the mechanism is cheap talk. The [Friction Allocation Diagnostic](../../practice/friction-allocation-diagnostic.md) tests them.
- **Three levers, and a conjecture about their order.** The seller can lower $c$ by discounting, lower $a$ by taking risk back through hostages such as guarantees and clawbacks, or lower $\hat{\Delta}_k$ in whichever component binds. The framework conjectures that the third lever moves more surplus than raising value would, because the cost curve is convex and a constant cannot offset a squared term. That conjecture rests on the anchored coefficient, and its falsifier is a discount closing a deal that a resolved gap could not.
- **Reputation depreciates.** What was verified at $t_0$ is not verified at $t_1$. Credibility carries demurrage, and it must be re-earned with evidence of continued delivery at every level: the seller's, the channel's, the adjudicator's. This is the second clause of the axiom applied after signature, and the [Sustaining Adoption Review](../../practice/implementation-motion/04-sustaining-adoption-review.md) is where the re-earning happens.
- **The Decay Clock.** Value decays from the trigger by the second standing assumption while the gaps rebuild by this axiom. Both push $S$ toward zero on a cycle, and a deal viable at $t_0$ is not necessarily viable at $t_1$ without intervention. [02-mathematical-models.md](./02-mathematical-models.md) section 4.

**What would falsify it.** A component whose gap was closed by verifiable evidence and whose effective cost did not fall, or a channel that saturated with unverifiable claims and kept its response rate. The second is already observable in outbound email.

**Failure modes.** Cheap talk, misallocated friction, Akerlof saturation, the wrong gap closed, Jevons collapse, and reputation hoarding. The collected table is in Part III.
---

## Part II: Derivations

Everything the repository claims beyond the three axioms is derived from them, and this table says where. A concept missing from it is either a standing assumption, a research file elaborating a source, or a mistake.

| Derivation | From | Stated in |
|---|---|---|
| A motion is a region of the friction space | I, with III supplying the direction reading | [01-motions.md](./01-motions.md) |
| Division of sales labor over the three costs | I | Part I above |
| Cost to serve is directional | I | Part I above |
| Addressable market is a property of the motion | I | [05-governance-forms.md](./05-governance-forms.md) §4 |
| Boundary condition, $k > k_{threshold}$ and $F_{deployed} \sim k$ | II | [01-motions.md](./01-motions.md) §3, [Deal Triage Calculator](../../practice/deal-triage-calculator.md) |
| Governance form from specificity and frequency | II | [05-governance-forms.md](./05-governance-forms.md) §2 |
| Frequency as a commercial choice | II | [05-governance-forms.md](./05-governance-forms.md) §5 |
| Staged commitment | II, with III | [Milestone Valuation Model](../../practice/milestone-valuation-model.md), [real-options.md](../02-research/real-options.md) |
| Stakes for agents and adjudicators | II, with the third standing assumption | [05-governance-forms.md](./05-governance-forms.md) §5 |
| Seller surplus and who bears the specificity | II | [04-seller-surplus-model.md](./04-seller-surplus-model.md) |
| A product must name its workflow | II | Part I above |
| Pursuit as amortizability at market level | II, with I | Part I above, [04-seller-surplus-model.md](./04-seller-surplus-model.md) |
| Per-component amplification and its factorization | III | [02-mathematical-models.md](./02-mathematical-models.md) §1, §2 |
| Friction Allocation Principles | III | [Friction Allocation Diagnostic](../../practice/friction-allocation-diagnostic.md) |
| Three sales levers | III | [02-mathematical-models.md](./02-mathematical-models.md) §1 |
| Reputation depreciation and demurrage | III | [Sustaining Adoption Review](../../practice/implementation-motion/04-sustaining-adoption-review.md) §4 |
| Decay Clock | III, with the second standing assumption | [02-mathematical-models.md](./02-mathematical-models.md) §4 |
| The Surplus equation | All three | Part III below |

---

## Part III: The Surplus Equation

The three axioms are what the terms of one equation mean.

$$S = \left(V_{solution} \cdot e^{-\delta t} - V_{next\_best}\right) - \sum_{k} F_k \,(1 + \hat{\Delta}_k(t)) = OC_{\text{switching}} - y$$

- The value bracket, $OC_{\text{switching}}$, is the buyer's opportunity cost of staying where they are, decaying by the second standing assumption.
- The sum runs over three components because of **Axiom I**, and its direction selects the motion.
- The size of each $F_k$, and the level they sum to, is set by specificity under **Axiom II**, which also decides how much of the sum must be paid before signature and what arrangement holds it afterward.
- The multiplier on each component is **Axiom III**, and $\hat{\Delta}_k(t)$ carries its second clause.
- $y = a\hat{\Delta}_A^2 + c$ is the same cost collapsed to a scalar, in annual contract values.

A deal closes when $S > 0$ at the moment of decision. It persists when the governance form selected under Axiom II holds every party's weight on the future above the cooperation threshold, and when the gaps are maintained under Axiom III faster than they rebuild.

**Reading a stall.** Walk the terms in axiom order.

1. **Is the investment specific?** If not, stop applying apparatus. Market terms, and let the buyer verify by trying. (Axiom II, the gate.)
2. **If it is, which cost binds after amplification?** Aim the motion there and nowhere else. A component that dominated at open may not dominate now. (Axiom I.)
3. **How much of the cost has been paid before signature, and what will hold the deal after?** A specific one-shot deal is the case to escalate or restructure, not to run lighter. (Axiom II.)
4. **Which pair cannot verify what, and is it rebuilding faster than discovery closes it?** A departed champion lands in the bargaining gap and no amount of technical proof reaches it. (Axiom III.)
5. **Does the buyer accept the case and still defer?** They are pricing the right to wait. Stage the commitment rather than re-arguing the return. (Axiom II with III.)
6. **Is value decaying faster than the gaps close?** Name a catalyst or close faster. (Second standing assumption.)
7. **Has any party's stake fallen below the threshold, or has any party stopped re-earning credibility?** The relationship decays regardless of the deal's economics. (Axiom II corollary, Axiom III corollary.)

**Failure modes, collected.**

| Axiom | Failure | Signal |
|---|---|---|
| I | Mis-composed | Direction misread, motion attacks a cost that is not binding |
| I | Mis-composed, organization | Motion adopted by imitation, seller built to pay a cost its market's buyers do not carry |
| II | Under-frictioned, pre-signature | Specific deal on a velocity motion, buyer builds internally |
| II | Under-frictioned, post-signature | Specific deal on an easy commercial path, buyer signs, fails to deploy, churns |
| II | Over-frictioned | Turnkey deal under heavy apparatus, buyer chooses a lighter competitor |
| II | Mis-governed | Frequency ignored, wrong arrangement for the repetition pattern |
| II | Defection | A party's weight on the future below threshold, hold-up on either side |
| III | Cheap talk | Signal fails single crossing, no gap moves |
| III | Misallocated friction | Receiver bears the filtering cost |
| III | Akerlof saturation | Gap past what any affordable signal can close, buyer exits |
| III | Wrong gap closed | Effort on a component whose gap was already low |
| III | Jevons collapse | Channel friction was production cost and fell to zero |
| III | Reputation hoarding | Past signals unrefreshed, incumbent coasts |
| II with III | Option value dominates | Case accepted, commitment deferred, full commitment demanded before uncertainty resolves |

Each mode names one axiom and one place to intervene. A stall matching none of them means the table is incomplete, which is itself worth recording.

---

## Version History

**Current version: 2.3.** The framework's version tracks this document's, and the root README footer must agree, which `check_frontmatter.py` enforces.

| Version | Date | Change |
|---|---|---|
| 2.3 | 2026-09 | Definitions added for market, workflow, seat and deal, the units at which the three axioms are read. Three corollaries added: cost to serve is directional (I), a product must name its workflow (II), pursuit is amortizability at market level (II). An organization-level mis-composed failure mode. Two register entries opened: the market reading has no instrument, and the components have no equilibrium statement. 08-from-axioms-to-instruments.md opened as the derivation of what a reader must be able to do, and integration-touchpoints.md added to the research. No axiom changed. |
| 2.2 | 2026-09 | Restructure, step 6. Reference trim. The research files stop carrying quotes and statistics, which move to publishing and the provenance audit. The glossary term index loses every single-file term. The math file's argument about units is compressed. The retired derivation tiers are removed from every support line. No axiom changed. |
| 2.1 | 2026-09 | Restructure, step 5. Coase's component names swept through theory prose, fit verification moved out of the search component and under specificity, the motions and governance files trimmed of material the Constitution now carries, and 07-open-questions.md opened as the register of under-developed areas. No axiom changed. |
| 2.0 | 2026-09 | The axioms are rewritten. Governance stops being an axiom and becomes a corollary of specificity, where Williamson put it. Specificity becomes Axiom II with its own law. Uncertainty Inflation moves from II to III and gains its second clause. Each axiom is stated at the level where a seller meets it, in one sentence, with a falsifier. Three standing assumptions are named above the axioms. The components take Coase's names in theory, with consensus and implementation kept as the field translations. Part II becomes a table. No equation changed. |
| 1.2 | 2026-09 | Restructure, step 3. Three motion files merged into 01-motions.md, the foundation files renumbered, this history reduced to a pointer, the reading guide and glossary trimmed. |
| 1.1 | 2026-09 | Restructure, step 2. Practice flattened to one directory and ten operating-procedure files removed. The vesting claim moved to 05-governance-forms.md section 5. |
| 1.0 | 2026-09 | First release under the name Transaction Cost Growth. The framework was renamed from Implementation-Led Growth, every motion was named after the cost it reduces, and the count restarted. |

The nineteen revisions made under the earlier name, and the prose entry for each, are in the git history: `git log -- theory/01-foundation/00-tcg-constitution.md`, then `git show <commit>:theory/01-foundation/00-tcg-constitution.md`. `RetiredTerms.yml` cites those version numbers when it records what each one retired.

---

## Related

**Sibling theory:**
- [01-motions.md](./01-motions.md) — Motion selection derived from the friction vector, the four regions and what each deploys, and the map onto the incumbent vocabulary.
- [02-mathematical-models.md](./02-mathematical-models.md) — Functional forms behind the variables named here, and the derivation reconciling the two cost representations.
- [03-glossary-and-notation.md](./03-glossary-and-notation.md) — Canonical index of every symbol and term, including the Coase-to-field name mapping.
- [04-seller-surplus-model.md](./04-seller-surplus-model.md) — The seller's side of Axiom II.
- [05-governance-forms.md](./05-governance-forms.md) — Axiom II's governance corollaries in full.
- [06-calibration.md](./06-calibration.md) — Every number, with its provenance.
- [07-open-questions.md](./07-open-questions.md) — Where the theory is under-developed, by axiom, and what would settle each gap.
- [08-from-axioms-to-instruments.md](./08-from-axioms-to-instruments.md) — What a reader must be able to do, derived from the axioms: the two-level reading, the activity grid, the three ledgers and the plan.

**Academic backing** (per axiom):
- Axiom I (Composition) → [transaction-cost-economics.md](../02-research/transaction-cost-economics.md), [buying-center-dynamics.md](../02-research/buying-center-dynamics.md), [channel-collapse.md](../02-research/channel-collapse.md), [integration-touchpoints.md](../02-research/integration-touchpoints.md)
- Axiom II (Specificity) → [transaction-cost-economics.md](../02-research/transaction-cost-economics.md), [klein-crawford-alchian.md](../02-research/klein-crawford-alchian.md), [incomplete-contracts.md](../02-research/incomplete-contracts.md), [process-misfit.md](../02-research/process-misfit.md), [game-theory-and-nrr.md](../02-research/game-theory-and-nrr.md), [real-options.md](../02-research/real-options.md), [fear-of-failure.md](../02-research/fear-of-failure.md), [integration-touchpoints.md](../02-research/integration-touchpoints.md)
- Axiom III (Inflation) → [costly-signals.md](../02-research/costly-signals.md), [prospect-theory.md](../02-research/prospect-theory.md), [cfir.md](../02-research/cfir.md), [re-aim-framework.md](../02-research/re-aim-framework.md), [fear-of-failure.md](../02-research/fear-of-failure.md)

**Field operationalization:**
- Level, direction and frequency → [deal-triage-calculator.md](../../practice/deal-triage-calculator.md)
- Blueprint → [01-discovery-contextual-blueprint.md](../../practice/implementation-motion/01-discovery-contextual-blueprint.md)
- Red Team → [02-validation-red-team-protocol.md](../../practice/implementation-motion/02-validation-red-team-protocol.md)
- MIP → [03-closing-mutual-implementation-plan.md](../../practice/implementation-motion/03-closing-mutual-implementation-plan.md)
- Handoff and reputation refresh → [04-sustaining-adoption-review.md](../../practice/implementation-motion/04-sustaining-adoption-review.md)
