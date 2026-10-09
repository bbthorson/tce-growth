---
title: "Friction Efficiency Index"
layer: practice
status: active
operationalizes: [axiom-2, axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# Friction Efficiency Index

**Purpose:** To measure whether an organization settles the allocation of each specific investment before it is sunk, and how its effort and its buyers' commitment ran, across a book of deals with specific exposure.

**Use when:** Reviewing a closed cohort of deals with specific exposure quarterly. This is a retrospective management instrument, not a per-deal gate.

**Operationalizes:** Axiom II's split of investment between the parties, Axiom III's clause that allocation is settled before the specific investment is sunk, and Friction Allocation Principle 3 (friction scales with stakes). It measures execution of the motion rather than a term in the two conditions.

> [!IMPORTANT]
> **Why this lives in `practice/` and not `theory/`.** Every model in [02-mathematical-models.md](../theory/01-foundation/02-mathematical-models.md) supplies a functional form for a variable the Constitution already names, and that file states it introduces no new claims. The measures below do something different: they score how well an organization ran the motion. They are observations about execution, not derivations from the axioms, and placing them in the foundation would break the axioms-first rule.

> [!WARNING]
> **Calibration status: none.** Every threshold, weight, and coefficient on this page is a reasoned starting value. None is fitted to booked deal data. Use these numbers to compare deals within your own book. Do not quote them externally as benchmarks, and do not report the composite index to a board as a performance figure until Section 7 conditions are met. Section 6 records two defects in the composite that are known and unfixed, and one that allocation coverage resolved.

---

## 1. Allocation Coverage Ratio (ACR)

The share of a deal's specific investment that was sunk only after an allocation covering it had been agreed.

$$\text{ACR} = \frac{n_{allocated}}{n_{exposure}}$$

Where $n_{exposure}$ is the deal's exposure count from Step 2 of the [Deal Triage Calculator](./deal-triage-calculator.md), integration points plus workflows that change plus divergent steps, re-taken at the [Adoption Review](./implementation-motion/04-sustaining-adoption-review.md). $n_{allocated}$ counts the items whose work began only after a written allocation covered them. **An allocation covers an item when it names all three:** who bears that item's adaptation risk, the gate the item sits behind, and a right to stop at that gate. Two of the three is not an allocation. These are the three things a [Mutual Implementation Plan](./implementation-motion/03-closing-mutual-implementation-plan.md) gate writes down, so the plan is where the count is read.

**Higher is better, and there is no band.** An ACR of 1.0 means nothing specific was sunk before someone agreed who carries it. Axiom III asks for exactly that, so no point short of 1.0 is a target to stop at.

**ACR is undefined when nothing specific was sunk.** A deal with an exposure count of zero, or one where the buyer could trial and walk away, has nothing to allocate, and it belongs outside the cohort this index reads.

**Why this is the target and effort is not.** Earlier versions scored the share of implementation effort spent before signature, with a reference band of 0.60 to 0.75. Constitution 3.0 established that what must come before the investment is sunk is the *allocation*: who bears which adaptation risk, staged how, with what right to stop. The work done in advance can rightly fall as uncertainty rises, because misfits in roles, controls and culture surface only in use. A target on pre-signature effort rewarded forcing discovery that only use can do.

### 1.1 Friction Allocation Ratio (FAR), as description

The share of total implementation effort spent before signature.

$$\text{FAR} = \frac{H_{pre}}{H_{pre} + H_{post}}$$

Where $H_{pre}$ is solutions-engineering and implementation hours logged before contract signature, and $H_{post}$ is the same functions' hours from signature through go-live.

**FAR has no target and no weight in the composite.** It says where the effort went, which is worth knowing beside ACR: a high ACR on a low FAR is a deal that allocated well and did its discovery in use, which Axiom III permits, and a low ACR on a high FAR is a deal that worked hard in advance and still sank investment nobody had agreed to carry.

**FAR is blind to scale.** An engagement spending 10 pre-sale and 5 post-sale hours scores identically to one spending 1,000 and 500. Always report FAR alongside $H_{pre} + H_{post}$. A high FAR on a trivial hour count means the deal was small, not that the motion was well run.

---

## 2. Buyer Commitment Velocity (BCV)

How quickly the buyer mobilizes internal resources once asked.

$$\text{BCV} = \frac{S_{dept}}{(D_{prov} + 1) \cdot N^{0.5}}$$

Where $S_{dept}$ is the count of departments that supplied a named participant to Blueprint or Red Team sessions, $D_{prov}$ is calendar days from the request to the first delivered artifact or confirmed attendee, and $N$ is total committee size.

**The $N^{0.5}$ denominator is a correction, not decoration.** The canvas form of this metric was $S_{dept} / (D_{prov} + 1)$, which rewards engaging more departments. That inverts Axiom I. The consensus model treats the count of decision roles as a cost driver, where $F_{consensus} = \alpha N^{\beta}(1 + \text{Var})$ rises with $N$. Uncorrected, an organization could raise its score by dragging more people into rooms, which the [Consensus Friction Calculator](./consensus-friction-calculator.md) correctly scores as worse. Dividing by $\sqrt{N}$ measures mobilization speed per unit of coordination burden rather than raw breadth.

**What BCV actually detects.** Speed of resource commitment is a costly signal in Spence's sense. A buyer who convenes four departments in three days has spent real internal capital and cannot cheaply fake it. A buyer who takes six weeks to produce one attendee is signalling that this project sits below the line on their priority list, whatever they say on calls.

$D_{prov} + 1$ guards against division by zero on same-day response. It is a convention, not a modelled quantity.

---

## 3. Risk Mitigation Score (RMS)

The share of discovered edge cases that were closed before signature.

$$\text{RMS} = 1 - \frac{N_{unresolved}}{N_{identified}}$$

**This corrects an arithmetic error in the canvas form.** That version read $N_{edge} / (N_{edge} + N_{unresolved})$, which double-counts. Unresolved cases are a subset of identified cases, so they appear in both numerator and denominator. A Red Team that identified ten edge cases and resolved none scored 10/20 = 0.50, reporting half the risk mitigated when in fact none was. The corrected form returns 0.

**RMS rewards shallow discovery, and must never be read alone.** A Red Team that surfaces two edge cases and closes both scores 1.00. One that surfaces forty and closes thirty-five scores 0.875. The lazier workshop wins. This is the superficial Red Team failure the [Red Team Protocol](./implementation-motion/02-validation-red-team-protocol.md) exists to prevent, and a metric that rewards it will produce it.

Report $N_{identified}$ next to RMS every time, and treat a low count as the finding. Below roughly eight identified edge cases on a genuine deal with specific exposure, the workshop did not do its job, and the RMS figure carries no information regardless of how high it is.

---

## 4. Scope Variance Index (SVI)

Divergence between scoped and delivered implementation, where lower is better.

$$\text{SVI} = \frac{|T_{actual} - T_{scoped}|}{T_{scoped}} + 0.25 \cdot C_{orders}$$

Where $T$ is implementation duration and $C_{orders}$ is the count of post-signature change orders.

Two properties to hold in mind when reading it. The absolute value penalizes early delivery as heavily as late delivery, which is deliberate: finishing in half the scoped time means the estimate was wrong, and a wrong estimate on the optimistic side produces the same buyer-facing credibility loss as one on the pessimistic side. The 0.25 coefficient on change orders is chosen, with no source. It encodes a judgment that one change order is worth about as much scope instability as a 25 percent schedule miss.

---

## 5. The composite index

$$\text{FEI} = 100 \cdot \left(0.35 \cdot \text{ACR} + 0.25 \cdot \widehat{\text{BCV}} + 0.25 \cdot \text{RMS} + 0.15 \cdot (1 - \widehat{\text{SVI}})\right)$$

The weights sum to 1.00, so FEI is bounded on $[0, 100]$ once both normalizations are applied. The canvas specified this formula without defining them, which left it uncomputable. Both are supplied here:

$$\widehat{\text{BCV}} = \min\left(\frac{\text{BCV}}{\text{BCV}_{ref}}, 1\right) \qquad \widehat{\text{SVI}} = \min(\text{SVI}, 1)$$

$\text{BCV}_{ref}$ is the trailing median BCV across your last twenty closed deals with specific exposure. Until twenty deals exist, set $\text{BCV}_{ref} = 0.5$ and mark every reported figure as provisional. SVI caps at 1 because a 100 percent schedule overrun is already a total scoping failure, and allowing the term to run higher would let one catastrophic project dominate a cohort average.

| FEI | Reading | Action |
|---|---|---|
| **Above 75** | Specific investment is allocated before it is sunk, and discovery is closing risk. | Maintain. Check that $H_{pre} + H_{post}$ is proportional to deal size. |
| **50 to 75** | Mixed. Usually strong ACR with weak RMS, meaning the allocation is written but the Red Team is not finding failure modes. | Audit Red Team facilitation before adding pre-sale hours. |
| **Below 50** | Specific investment is being sunk before anyone agreed who carries it. Expect clawbacks and post-signature scope fights. | Treat as a motion-compliance problem, not a rep-skill problem. |

**Read the four components before the composite.** Any weighted index can hide an offsetting pair, and the common one here is a high ACR carrying a low RMS: every gate is written down and the workshop still fails to surface failure modes, which produces a respectable FEI on top of a well-documented, shallow process. The composite is for tracking one organization's direction over time. The components are what tell you where to intervene.

---

## 6. Defects in the composite, recorded

Each was found by evaluating the formulas in [`models/tcg_models.py`](../models/tcg_models.py) rather than by reading them. The two still open are not fixed here, because each fix requires choosing a shape or a weight rather than correcting arithmetic, and that is a decision rather than a repair.

**Resolved: the composite was monotonic in FAR.** Earlier versions weighted FAR at 0.35 with no band while naming a FAR above 0.75 as a failure, so the composite rewarded the state it warned against. ACR took FAR's weight. More allocation is better all the way to 1.0, so a monotonic weight is now the right shape, and FAR carries no weight at all.

**Red Team credibility is ungated in the composite.** Section 3 states that below roughly eight identified edge cases the score carries no information however high it is. Section 5 consumes RMS anyway. A workshop finding two cases and closing both scores 1.000 and reaches a composite of 86.50. One finding forty and closing thirty-five scores 0.875 and reaches 83.38. The shallower workshop wins by three points, which is the failure section 3 predicts and section 5 builds.

**Half of any book caps out on Buyer Commitment Velocity.** $\text{BCV}_{ref}$ is the trailing median across the last twenty closed deals with specific exposure, and $\widehat{\text{BCV}} = \min(\text{BCV}/\text{BCV}_{ref}, 1)$. A median splits its own population in half by definition, so half of all deals sit at exactly 1.000 on a component weighted 0.25. The component discriminates across one half of the book and not at all across the other.

---

## 7. What would make this empirical

The conditions in [06-calibration.md](../theory/01-foundation/06-calibration.md) section 4 that govern the theory's models apply here too. This instrument also needs four of its own:

1. **Hours are logged by phase** in the professional services system, split at signature rather than reconstructed afterward.
2. **Edge cases are recorded as structured Red Team output** rather than narrative notes, which is what makes $N_{identified}$ countable at all.
3. **Change orders are dated and attributed** to a root cause: unmapped environment, buyer-initiated expansion, or seller estimation error. Only the first two are scope variance in the sense modelled here.
4. **ACR is tested against realized outcomes.** Regress 90-day launch success and first-renewal retention on ACR, stratified by the exposure count. If allocation is what Axiom III says it is, ACR predicts both better than FAR does at equal exposure. If FAR predicts better, the theory's allocation clause is in trouble, and [07-open-questions.md](../theory/01-foundation/07-open-questions.md) item 7 is where to record it.

Until then, treat every output as a structured comparison between deals in your own book. A cohort scoring 71 is meaningfully better run than one scoring 46. Neither number is a benchmark against another company.

---

## Parameter reference

| Parameter | Symbol | Default | Provenance |
|---|---|---|---|
| What makes an allocation | — | Risk bearer, gate and right to stop, all three | **Chosen.** Mirrors what a Mutual Implementation Plan gate writes down. Test per Section 7.4. |
| Committee-size correction | $N^{0.5}$ | 0.5 exponent | **Structurally motivated.** Direction follows from $F_{consensus}$ rising in $N$. The exponent is chosen. |
| Provisioning guard | $D_{prov} + 1$ | 1 | **Convention.** Prevents division by zero. |
| Change-order weight | — | 0.25 | **Chosen.** No source. |
| FEI component weights | — | 0.35 / 0.25 / 0.25 / 0.15, for ACR, BCV, RMS and SVI | **Chosen.** Sum to 1.00 by construction. No empirical basis for the split. ACR inherited FAR's weight. |
| BCV reference | $\text{BCV}_{ref}$ | trailing median, or 0.5 | **Convention.** Self-referential to your own book by design. |
| Minimum credible edge-case count | $N_{identified}$ | 8 | **Chosen.** Field heuristic for detecting a shallow Red Team. |

Read the provenance column before quoting any figure outside this repository. No parameter on this page carries literature support for its value.

---

## Related

- [02-mathematical-models.md](../theory/01-foundation/02-mathematical-models.md) — The axiom-derived models. This file deliberately sits downstream of them.
- [Consensus Friction Calculator](./consensus-friction-calculator.md) — Source of the $N$ correction applied to BCV.
- [Bilateral Asymmetry Scorecard](./asymmetry-scorecard.md) — Pre-close companion. The scorecard predicts; this index scores the result.
- [Red Team Protocol](./implementation-motion/02-validation-red-team-protocol.md) — Where $N_{identified}$ originates.
