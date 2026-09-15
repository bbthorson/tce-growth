---
title: "Friction Efficiency Index"
layer: practice
status: active
operationalizes: [axiom-2]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# Friction Efficiency Index

**Purpose:** To measure whether an organization is spending its implementation effort before signature or after it, and to benchmark that allocation across a book of Structural deals.

**Use when:** Reviewing a closed cohort of Structural deals quarterly. This is a retrospective management instrument, not a per-deal gate.

**Operationalizes:** Axiom II's scaling requirement ($F_{deployed} \sim k$) and Friction Allocation Principle 3 (friction scales with stakes). It measures execution of the motion rather than a term in the Surplus equation.

> [!IMPORTANT]
> **Why this lives in `practice/` and not `theory/`.** Every model in [02-mathematical-models.md](../theory/01-foundation/02-mathematical-models.md) supplies a functional form for a variable the Constitution already names, and that file states it introduces no new claims. The measures below do something different: they score how well an organization ran the motion. They are observations about execution, not derivations from the axioms, and placing them in the foundation would break the axioms-first rule.

> [!WARNING]
> **Calibration status: none.** Every threshold, weight, and coefficient on this page is a reasoned starting value. None is fitted to booked deal data. Use these numbers to compare deals within your own book. Do not quote them externally as benchmarks, and do not report the composite index to a board as a performance figure until Section 7 conditions are met. Section 6 records three defects in the composite that are known and unfixed.

---

## 1. Friction Allocation Ratio (FAR)

The share of total implementation effort spent before signature.

$$\text{FAR} = \frac{H_{pre}}{H_{pre} + H_{post}}$$

Where $H_{pre}$ is solutions-engineering and implementation hours logged before contract signature, and $H_{post}$ is the same functions' hours from signature through go-live.

**Reference band: 0.60 to 0.75.** Below 0.60, the organization is discovering the buyer's environment after it has committed to a delivery date, which is the under-frictioned Structural failure mode. Above 0.75, either the deal was a Turnkey deal that received implementation-chain treatment, or pre-sale work is being performed that the buyer never asked for.

**FAR is blind to scale.** An engagement spending 10 pre-sale and 5 post-sale hours scores identically to one spending 1,000 and 500. Always report FAR alongside $H_{pre} + H_{post}$, because the ratio only becomes meaningful once total effort is proportional to the deal's asset specificity. A high FAR on a trivial hour count means the deal was small, not that the motion was well run.

---

## 2. Buyer Commitment Velocity (BCV)

How quickly the buyer mobilizes internal resources once asked.

$$\text{BCV} = \frac{S_{dept}}{(D_{prov} + 1) \cdot N^{0.5}}$$

Where $S_{dept}$ is the count of departments that supplied a named participant to Blueprint or Red Team sessions, $D_{prov}$ is calendar days from the request to the first delivered artifact or confirmed attendee, and $N$ is total committee size.

**The $N^{0.5}$ denominator is a correction, not decoration.** The canvas form of this metric was $S_{dept} / (D_{prov} + 1)$, which rewards engaging more departments. That inverts Axiom III. The consensus model treats stakeholder count as a cost driver, where $F_{consensus} = \alpha N^{\beta}(1 + \text{Var})$ rises with $N$. Uncorrected, an organization could raise its score by dragging more people into rooms, which the [Consensus Friction Calculator](./consensus-friction-calculator.md) correctly scores as worse. Dividing by $\sqrt{N}$ measures mobilization speed per unit of coordination burden rather than raw breadth.

**What BCV actually detects.** Speed of resource commitment is a costly signal in Spence's sense. A buyer who convenes four departments in three days has spent real internal capital and cannot cheaply fake it. A buyer who takes six weeks to produce one attendee is signalling that this project sits below the line on their priority list, whatever they say on calls.

$D_{prov} + 1$ guards against division by zero on same-day response. It is a convention, not a modelled quantity.

---

## 3. Risk Mitigation Score (RMS)

The share of discovered edge cases that were closed before signature.

$$\text{RMS} = 1 - \frac{N_{unresolved}}{N_{identified}}$$

**This corrects an arithmetic error in the canvas form.** That version read $N_{edge} / (N_{edge} + N_{unresolved})$, which double-counts. Unresolved cases are a subset of identified cases, so they appear in both numerator and denominator. A Red Team that identified ten edge cases and resolved none scored 10/20 = 0.50, reporting half the risk mitigated when in fact none was. The corrected form returns 0.

**RMS rewards shallow discovery, and must never be read alone.** A Red Team that surfaces two edge cases and closes both scores 1.00. One that surfaces forty and closes thirty-five scores 0.875. The lazier workshop wins. This is the superficial Red Team failure the [Red Team Protocol](./implementation-motion/02-validation-red-team-protocol.md) exists to prevent, and a metric that rewards it will produce it.

Report $N_{identified}$ next to RMS every time, and treat a low count as the finding. Below roughly eight identified edge cases on a genuine Structural deal, the workshop did not do its job, and the RMS figure carries no information regardless of how high it is.

---

## 4. Scope Variance Index (SVI)

Divergence between scoped and delivered implementation, where lower is better.

$$\text{SVI} = \frac{|T_{actual} - T_{scoped}|}{T_{scoped}} + 0.25 \cdot C_{orders}$$

Where $T$ is implementation duration and $C_{orders}$ is the count of post-signature change orders.

Two properties to hold in mind when reading it. The absolute value penalizes early delivery as heavily as late delivery, which is deliberate: finishing in half the scoped time means the estimate was wrong, and a wrong estimate on the optimistic side produces the same buyer-facing credibility loss as one on the pessimistic side. The 0.25 coefficient on change orders is chosen, with no source. It encodes a judgment that one change order is worth about as much scope instability as a 25 percent schedule miss.

---

## 5. The composite index

$$\text{FEI} = 100 \cdot \left(0.35 \cdot \text{FAR} + 0.25 \cdot \widehat{\text{BCV}} + 0.25 \cdot \text{RMS} + 0.15 \cdot (1 - \widehat{\text{SVI}})\right)$$

The weights sum to 1.00, so FEI is bounded on $[0, 100]$ once both normalizations are applied. The canvas specified this formula without defining them, which left it uncomputable. Both are supplied here:

$$\widehat{\text{BCV}} = \min\left(\frac{\text{BCV}}{\text{BCV}_{ref}}, 1\right) \qquad \widehat{\text{SVI}} = \min(\text{SVI}, 1)$$

$\text{BCV}_{ref}$ is the trailing median BCV across your last twenty closed Structural deals. Until twenty deals exist, set $\text{BCV}_{ref} = 0.5$ and mark every reported figure as provisional. SVI caps at 1 because a 100 percent schedule overrun is already a total scoping failure, and allowing the term to run higher would let one catastrophic project dominate a cohort average.

| FEI | Reading | Action |
|---|---|---|
| **Above 75** | Friction is front-loaded and discovery is closing risk before signature. | Maintain. Check that $H_{pre} + H_{post}$ is proportional to deal size. |
| **50 to 75** | Mixed. Usually strong FAR with weak RMS, meaning hours are spent early but not on finding failure modes. | Audit Red Team facilitation before adding pre-sale hours. |
| **Below 50** | Effort is landing after signature. Expect clawbacks and post-signature scope fights. | Treat as a motion-compliance problem, not a rep-skill problem. |

**Read the four components before the composite.** Any weighted index can hide an offsetting pair, and the common one here is a high FAR carrying a low RMS: the organization spends heavily before signature and still fails to surface failure modes, which produces a respectable FEI on top of an expensive, shallow process. The composite is for tracking one organization's direction over time. The components are what tell you where to intervene.

---

## 6. Three defects in the composite, recorded

Each was found by evaluating the formulas in [`models/tcg_models.py`](../models/tcg_models.py) rather than by reading them. None is fixed here, because each fix requires choosing a shape or a weight rather than correcting arithmetic, and that is a decision rather than a repair.

**The composite is monotonic in FAR, and section 1 says it should not be.** Section 1 states that above 0.75 the organization is either treating a Turnkey deal as Structural or performing pre-sale work nobody asked for. Section 5 then weights FAR at 0.35 with no band. Holding the other three components fixed, a FAR of 0.70 scores 81.50 and a FAR of 1.00 scores 92.00. The composite rewards the state section 1 names as a failure. A fix means giving FAR a band-shaped contribution, which requires choosing how steeply to penalize each side of the band.

**Red Team credibility is ungated in the composite.** Section 3 states that below roughly eight identified edge cases the score carries no information however high it is. Section 5 consumes RMS anyway. A workshop finding two cases and closing both scores 1.000 and reaches a composite of 86.50. One finding forty and closing thirty-five scores 0.875 and reaches 83.38. The shallower workshop wins by three points, which is the failure section 3 predicts and section 5 builds.

**Half of any book caps out on Buyer Commitment Velocity.** $\text{BCV}_{ref}$ is the trailing median across the last twenty closed Structural deals, and $\widehat{\text{BCV}} = \min(\text{BCV}/\text{BCV}_{ref}, 1)$. A median splits its own population in half by definition, so half of all deals sit at exactly 1.000 on a component weighted 0.25. The component discriminates across one half of the book and not at all across the other.

---

## 7. What would make this empirical

The same three conditions that govern [02-mathematical-models.md](../theory/01-foundation/02-mathematical-models.md) Section 6 apply, plus one specific to this instrument:

1. **Hours are logged by phase** in the professional services system, split at signature rather than reconstructed afterward.
2. **Edge cases are recorded as structured Red Team output** rather than narrative notes, which is what makes $N_{identified}$ countable at all.
3. **Change orders are dated and attributed** to a root cause: unmapped environment, buyer-initiated expansion, or seller estimation error. Only the first two are scope variance in the sense modelled here.
4. **The 0.60 to 0.75 FAR band is tested against realized outcomes.** Regress FAR against 90-day launch success across a cohort. If the band is real, it appears as a plateau. If it does not appear, the band was an assumption and should be removed rather than defended.

Until then, treat every output as a structured comparison between deals in your own book. A cohort scoring 71 is meaningfully better run than one scoring 46. Neither number is a benchmark against another company.

---

## Parameter reference

| Parameter | Symbol | Default | Provenance |
|---|---|---|---|
| FAR target band | — | 0.60–0.75 | **Chosen.** No source. Test per Section 7.4. |
| Committee-size correction | $N^{0.5}$ | 0.5 exponent | **Structurally motivated.** Direction follows from $F_{consensus}$ rising in $N$. The exponent is chosen. |
| Provisioning guard | $D_{prov} + 1$ | 1 | **Convention.** Prevents division by zero. |
| Change-order weight | — | 0.25 | **Chosen.** No source. |
| FEI component weights | — | 0.35 / 0.25 / 0.25 / 0.15 | **Chosen.** Sum to 1.00 by construction. No empirical basis for the split. |
| BCV reference | $\text{BCV}_{ref}$ | trailing median, or 0.5 | **Convention.** Self-referential to your own book by design. |
| Minimum credible edge-case count | $N_{identified}$ | 8 | **Chosen.** Field heuristic for detecting a shallow Red Team. |

Read the provenance column before quoting any figure outside this repository. No parameter on this page carries literature support for its value.

---

## Related

- [02-mathematical-models.md](../theory/01-foundation/02-mathematical-models.md) — The axiom-derived models. This file deliberately sits downstream of them.
- [Consensus Friction Calculator](./consensus-friction-calculator.md) — Source of the $N$ correction applied to BCV.
- [Bilateral Asymmetry Scorecard](./asymmetry-scorecard.md) — Pre-close companion. The scorecard predicts; this index scores the result.
- [Red Team Protocol](./implementation-motion/02-validation-red-team-protocol.md) — Where $N_{identified}$ originates.
