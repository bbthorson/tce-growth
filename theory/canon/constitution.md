---
title: "The Constitution of Transaction Cost Growth (TCG)"
layer: theory
kind: canon
status: active
version: 2.5
---

# The Constitution of Transaction Cost Growth (TCG)

**Version:** 2.4
**Purpose:** To state the three claims from which everything else in this repository derives, each at the level where a seller meets it, each producing a decision, and each falsifiable on its own.

Version history is at the end of this document.

> [!IMPORTANT]
> **This document states structure. It states no measured quantity.** Every claim below says what depends on what, and each is argued from a mechanism. The coefficients, thresholds and band edges that turn those claims into numbers live in [calibration.md](../reference/calibration.md), none of them is fitted, and a reader can reject any number there without rejecting the claim it sits inside.

---

## Standing assumptions

Three premises sit above the axioms. They are inherited rather than argued, and each is named here so a reader who rejects one knows what falls with it.

1. **Bounded rationality and opportunism** (Williamson 1985). No party can foresee every state the relationship will reach, so every contract is incomplete. And a party will exploit a gap once the other side's position is exposed. The first is why uncertainty has a price. The second is why safeguards exist.
2. **Value is exogenous to the seller, and it decays.** Willingness to pay is a property of the product and the buyer's situation. The seller's levers are the cost of transacting and the buyer's perception of it. Where value moves during a cycle it moves down, from the triggering event: $V_{effective}(t) = V_{solution} \cdot e^{-\delta t}$. This is a modeling assumption, stated in [models.md](../reference/models.md) section 4, and the one term in $\delta$ a seller can touch is whether an external catalyst has been named.
3. **Every actor acts on their own payoff** (Jensen and Meckling 1976). That includes the seller's own representatives and every intermediary standing between the two parties. An actor whose payoff does not depend on the outcome behaves as though the outcome does not matter, whatever their intent.

![Two exponential decay curves falling toward a floor at the value of the next best alternative. Organizational inertia alone reaches the floor in the second month. A named external catalyst holds value above it until the eleventh.](./assets/value-decay.svg)

---

## Part I: The Three Axioms

Each axiom is stated at the level where a seller meets it, and each produces one decision.

| Axiom | Level | Statement | Decision it produces |
|---|---|---|---|
| **I. Law of Transaction Cost Composition** | **Market** | Every deal carries three costs beyond price, search, bargaining and enforcement, and the one that binds selects the motion. | Which instruments to run |
| **II. Law of Asset Specificity** | **Workflow** | The more specific the investment, the more a deal costs to transact, and the more of that cost must be paid before signature. | How much apparatus, when to spend it, what arrangement holds it, whether to decline |
| **III. Law of Uncertainty Inflation** | **Deal** | Each cost is inflated by what the parties to it cannot verify about their own outcome, and the inflation rebuilds over time unless it is maintained. | What to prove, in what order, and what to re-prove at renewal |

**The axioms are numbered in the order a seller meets them, and the second is the gate.** A seller encounters a market before a buyer's workflow and a workflow before a deal, so the numbering follows that path. Williamson's result is that specificity is the master variable: when the investment is not specific, the buyer can verify by trying and walk away at no cost, market terms hold, and the other two readings barely matter. Uncertainty and frequency start to bite only once specificity is present. Read the three in order, and treat Axiom II as the test that decides whether the rest applies.

**On the component names.** The three costs carry Coase's names in this document and throughout the theory. The field calls the second one *consensus* and the third *implementation*, and the notation keeps those subscripts, because the field names say what a seller experiences and Coase's names say why. [notation.md](../reference/notation.md) carries the mapping.

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

The boundary condition is $k > k_{threshold}$, separating Structural deals from Turnkey ones, and $F_{deployed} \sim k$, requiring the friction the seller deploys to scale with the specificity it manages. The threshold is chosen and [calibration.md](../reference/calibration.md) says so.

The second clause, that the pre-signature share of the cost rises with $k$, is stated here in prose. The equation in Part III is a snapshot at signature and does not carry time, and the claim is deliberately left as a derivation beneath the axiom rather than a term inside the model until there is a reason to fit one. The [Friction Efficiency Index](../../practice/friction-efficiency-index.md) measures it in retrospect.

**What would falsify it.** A population of highly specific deals that closed on light pre-signature work and kept their surplus through renewal. The prediction is that such deals close and then fail to deploy, so the failure lands in retention rather than in win rate, and it is observable in churn by specificity at signature.

**Failure modes.** Under-frictioned before and after signature, over-frictioned, mis-governed, and defection. The collected table is in Part III.
---

### Axiom III — The Law of Uncertainty Inflation

> **Each cost is inflated by what the parties to it cannot verify about their own outcome, and the inflation rebuilds over time unless it is maintained.**

*Plain English: what nobody in the room can verify, they price as risk, and the risk multiplies the bill it attaches to. Three bills, three rooms, three separate things nobody can verify. And what was verified last quarter is not verified now.*

*Origin: Akerlof (1970) and Spence (1973). Unverifiable quality drives buyers out of a market, and a signal separates quality only when it costs something to send.*

**Mechanism.** Each of the three costs runs between its own pair of parties, and what inflates it is each party's uncertainty about what the transaction does to *them*.

| Component | Whose uncertainty, about what |
|---|---|
| Search | The buyer's, about the market. Which alternatives exist and whether this one fits. |
| Bargaining | Each stakeholder's, about their own outcome. What the change does to their budget, headcount and standing. |
| Enforcement | Bilateral. The seller's, about the buyer's environment. The buyer's, about the seller's capability. |

What closes each gap is an instrument rather than an axiom, and [models.md](../reference/models.md) section 2.4 tabulates the three with theirs.

Only the third pair is buyer against seller, which is why an instrument built for that pair does not move the other two. The second pair is not an information gap between stakeholders that proof could close. Two stakeholders with perfect knowledge of each other and opposed interests still disagree. What proof can close is each stakeholder's uncertainty about their own exposure, and that is the inflation this axiom names on the bargaining cost.

A signal resolves uncertainty only when it costs the sender something a low-quality sender could not afford. This is Spence's single crossing property, and it is why volume is not verification: a message that costs nothing to send carries no information, and a channel full of them degrades for the costly signals too. How heavily the remaining uncertainty is weighed is a question of loss aversion (Kahneman and Tversky 1979). The framework anchors the weighting on their coefficient by analogy, and [calibration.md](../reference/calibration.md) records how far the analogy stretches.

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

**What would falsify it.** A component whose gap was closed by verifiable evidence and whose effective cost did not fall, or a channel that saturated with unverifiable claims and kept its response rate. The second is already observable in outbound email.

**Failure modes.** Cheap talk, misallocated friction, Akerlof saturation, the wrong gap closed, Jevons collapse, and reputation hoarding. The collected table is in Part III.
---

## Part II: Derivations

Everything the repository claims beyond the three axioms is derived from them, and this table is the complete list. Each row states what follows in one sentence and names the file that argues it. **The argument lives in that file and not here**, because a claim with two prose homes has to be maintained in both, and this document is the one that must stay short enough to be held to. A concept missing from this table is either a standing assumption, a research file elaborating a source, or a mistake.

| Derivation | What follows | From | Argued in |
|---|---|---|---|
| A motion is a region | The named motions are regions of the space $\mathbf{F}$ spans, so a motion is read off a deal rather than chosen as a philosophy. | I, with III supplying the direction reading | [motions.md](./motions.md) |
| Division of sales labor | The standard sales organization is an instrument set with a fixed direction, so it meets the three costs in an order the deal did not choose, and every handoff is a seam where a cost is paid twice. | I | [motions.md](./motions.md) §2.3 |
| Addressable market | A seller who runs only short-vector instruments can transact only with short-vector buyers, so reach is a property of the motion rather than of the product. | I | [governance-forms.md](../arguments/governance-forms.md) §4 |
| Boundary condition | $k > k_{threshold}$ separates Structural deals from Turnkey ones, and $F_{deployed} \sim k$ requires deployed friction to scale with the specificity it manages. | II | [motions.md](./motions.md) §3, [Deal Triage Calculator](../../practice/deal-triage-calculator.md) |
| Governance form | Specificity and frequency together select market, trilateral, bilateral or unified governance, and the Mutual Implementation Plan is the bilateral form's instrument. | II | [governance-forms.md](../arguments/governance-forms.md) §2 |
| Frequency as a commercial choice | Restructuring a one-shot sale as a recurring one brings the cooperation condition within reach, which changes what can be governed without a third party. | II | [governance-forms.md](../arguments/governance-forms.md) §5 |
| Staged commitment | Hold-up is why commitments must be mutual and option value is why they must be staged, so a mutual commitment taken all at once still fails. | II, with III | [Milestone Valuation Model](../../practice/milestone-valuation-model.md), [real-options.md](../evidence/real-options.md) |
| Stakes for agents and adjudicators | A party paid in full at signature plays a repeated game with a one-shot payoff, and an adjudicator with no exposure drifts toward extraction, so both need a vested stake. | II, with the third standing assumption | [governance-forms.md](../arguments/governance-forms.md) §5 |
| Who bears the specificity | Whoever sinks the specific investment holds the exposure, which in a forward-deployed motion is the seller rather than the buyer. | II | [seller-surplus.md](../arguments/seller-surplus.md) |
| Per-component amplification | Each component is amplified by its own pair's gap, and the sum factors exactly into a single friction-weighted multiplier, which is why the two cost forms are one quantity. | III | [models.md](../reference/models.md) §1, §2 |
| Friction Allocation Principles | A mechanism reduces a gap only if its cost is non-automatable, borne by the claimant, scaled to the claim and adjudicated by someone who loses when a bad signal passes. Violate one and it is cheap talk. | III | [Friction Allocation Diagnostic](../../practice/friction-allocation-diagnostic.md) |
| Three levers, and their order | The seller can lower $c$, lower $a$, or lower $\hat{\Delta}_k$ where it binds, and the framework conjectures the third beats raising value because a constant cannot offset a squared term. | III | [models.md](../reference/models.md) §1.8 |
| Reputation depreciation | Credibility carries demurrage and must be re-earned with evidence of continued delivery, at the seller's level, the channel's and the adjudicator's. | III | [Sustaining Adoption Review](../../practice/implementation-motion/04-sustaining-adoption-review.md) §4 |
| Decay Clock | Value decays from the trigger while the gaps rebuild, so a deal viable at $t_0$ is not necessarily viable at $t_1$ without intervention. | III, with the second standing assumption | [models.md](../reference/models.md) §4 |
| The Surplus equation | The three axioms are what the terms of one equation mean. | All three | Part III below |

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

<!-- vale TCG.RetiredTerms = NO -->
<!--
  The retired-term rule is off for this section. A history entry names a file
  as it was called when the change happened, which is the same trade
  RetiredTerms.yml makes with its own version citations. Renaming them here
  would make the history describe a past that did not occur.
-->

**Current version: 2.5.** The framework's version tracks this document's, and the root README footer must agree, which `check_frontmatter.py` enforces.

| Version | Date | Change |
|---|---|---|
| 2.5 | 2026-09 | Segmentation audit, step 5. `theory/` is re-split by document contract into canon, reference, arguments and evidence, and this document moves to `theory/canon/constitution.md`. Every file declares a `kind` in its frontmatter, `check_frontmatter.py` requires it to match the directory, and a canon file now carries a word cap it cannot grow past. No axiom, equation or derivation changed: this version moves files and adds a check. |
| 2.4 | 2026-09 | Segmentation audit, step 4. The twelve corollary bullets are gone and Part II carries each derivation as one sentence naming the file that argues it. No axiom, equation or derivation changed, and nothing was dropped: four claims had no home outside these bullets and were moved first. The division of sales labour went to 01-motions.md §2.3, the hold-up against option-value distinction to the Milestone Valuation Model, the three levers and their conjecture to 02-mathematical-models.md §1.8, and the Decay Clock's second half to its section 4. Axiom III's pair table loses its prescription column to the same file's section 2.4. |
| 2.3 | 2026-09 | Segmentation audit, step 3. Deduplication, and no claim in this document changed. The "what this does not settle" sections in the motions, governance and seller surplus files fold into 07-open-questions.md, which gains seven entries and is now the only register. The three-pairs table, the addressable-market argument and the vesting claim each drop to a single prose home. The research README's scope table merges into the reading guide. |
| 2.2 | 2026-09 | Restructure, step 6. Reference trim. The research files stop carrying quotes and statistics, which move to publishing and the provenance audit. The glossary term index loses every single-file term. The math file's argument about units is compressed. The retired derivation tiers are removed from every support line. No axiom changed. |
| 2.1 | 2026-09 | Restructure, step 5. Coase's component names swept through theory prose, fit verification moved out of the search component and under specificity, the motions and governance files trimmed of material the Constitution now carries, and 07-open-questions.md opened as the register of under-developed areas. No axiom changed. |
| 2.0 | 2026-09 | The axioms are rewritten. Governance stops being an axiom and becomes a corollary of specificity, where Williamson put it. Specificity becomes Axiom II with its own law. Uncertainty Inflation moves from II to III and gains its second clause. Each axiom is stated at the level where a seller meets it, in one sentence, with a falsifier. Three standing assumptions are named above the axioms. The components take Coase's names in theory, with consensus and implementation kept as the field translations. Part II becomes a table. No equation changed. |
| 1.2 | 2026-09 | Restructure, step 3. Three motion files merged into 01-motions.md, the foundation files renumbered, this history reduced to a pointer, the reading guide and glossary trimmed. |
| 1.1 | 2026-09 | Restructure, step 2. Practice flattened to one directory and ten operating-procedure files removed. The vesting claim moved to 05-governance-forms.md section 5. |
| 1.0 | 2026-09 | First release under the name Transaction Cost Growth. The framework was renamed from Implementation-Led Growth, every motion was named after the cost it reduces, and the count restarted. |

The nineteen revisions made under the earlier name, and the prose entry for each, are in the git history: `git log -- theory/01-foundation/00-tcg-constitution.md`, then `git show <commit>:theory/01-foundation/00-tcg-constitution.md`. `RetiredTerms.yml` cites those version numbers when it records what each one retired.

<!-- vale TCG.RetiredTerms = YES -->

---

## Related

**Sibling theory:**
- [motions.md](./motions.md) — Motion selection derived from the friction vector, the four regions and what each deploys, and the map onto the incumbent vocabulary.
- [models.md](../reference/models.md) — Functional forms behind the variables named here, and the derivation reconciling the two cost representations.
- [notation.md](../reference/notation.md) — Canonical index of every symbol and term, including the Coase-to-field name mapping.
- [seller-surplus.md](../arguments/seller-surplus.md) — The seller's side of Axiom II.
- [governance-forms.md](../arguments/governance-forms.md) — Axiom II's governance corollaries in full.
- [calibration.md](../reference/calibration.md) — Every number, with its provenance.
- [open-questions.md](../reference/open-questions.md) — Where the theory is under-developed, by axiom, and what would settle each gap.

**Academic backing** (per axiom):
- Axiom I (Composition) → [transaction-cost-economics.md](../evidence/transaction-cost-economics.md), [buying-center-dynamics.md](../evidence/buying-center-dynamics.md), [channel-collapse.md](../evidence/channel-collapse.md)
- Axiom II (Specificity) → [transaction-cost-economics.md](../evidence/transaction-cost-economics.md), [klein-crawford-alchian.md](../evidence/klein-crawford-alchian.md), [incomplete-contracts.md](../evidence/incomplete-contracts.md), [process-misfit.md](../evidence/process-misfit.md), [game-theory-and-nrr.md](../evidence/game-theory-and-nrr.md), [real-options.md](../evidence/real-options.md), [fear-of-failure.md](../evidence/fear-of-failure.md)
- Axiom III (Inflation) → [costly-signals.md](../evidence/costly-signals.md), [prospect-theory.md](../evidence/prospect-theory.md), [cfir.md](../evidence/cfir.md), [re-aim-framework.md](../evidence/re-aim-framework.md), [fear-of-failure.md](../evidence/fear-of-failure.md)

**Field operationalization:**
- Level, direction and frequency → [deal-triage-calculator.md](../../practice/deal-triage-calculator.md)
- Blueprint → [01-discovery-contextual-blueprint.md](../../practice/implementation-motion/01-discovery-contextual-blueprint.md)
- Red Team → [02-validation-red-team-protocol.md](../../practice/implementation-motion/02-validation-red-team-protocol.md)
- MIP → [03-closing-mutual-implementation-plan.md](../../practice/implementation-motion/03-closing-mutual-implementation-plan.md)
- Handoff and reputation refresh → [04-sustaining-adoption-review.md](../../practice/implementation-motion/04-sustaining-adoption-review.md)
