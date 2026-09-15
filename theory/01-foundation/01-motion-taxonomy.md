---
title: "The Motion Taxonomy"
layer: theory
status: active
version: 1.1
operationalizes: [axiom-1, axiom-2]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# The Motion Taxonomy

**Version:** 1.1
**Purpose:** To name the motions and specify what each one deploys.

A sales motion is the instrument set deployed to reduce a buyer's transaction friction. Because a seller cannot alter intrinsic willingness to pay, transaction enablement operates entirely by reducing transaction costs across three components:

* **$F_{search}$:** Inability to discover, compare, or reach a viable solution at acceptable cost.
* **$F_{consensus}$:** Inability of internal buyer stakeholders to reconcile competing priorities and operational risk.
* **$F_{implementation}$:** Inability to verify that post-signature technical and operational execution will succeed without destructive disruption.

The three are separately addressable rather than separately caused. A workflow the product must fit but does not raises $F_{implementation}$ and generates $F_{consensus}$ at the same time, because an imposition creates a stakeholder whose objectives worsen. Treat them as three bills the buyer pays, not as three independent variables.

---

## 1. Triage Architecture: Level and Direction

Every opportunity routes through two sequential measurements emitted by Axiom I:

1. **Level ($\lVert \mathbf{F} \rVert_1$):** Evaluates aggregate transaction friction against the apparatus boundary of 15. Deals below 15 do not generate enough transaction surplus to repay dedicated enablement instruments.
2. **Direction:** Evaluates which friction component accounts for 50 percent or more of effective cost on structural deals. If no single component reaches 50 percent, the deal is **Composed**.

| Level | Component Condition | Motion Routing | Primary Operational Mechanism |
|---|---|---|---|
| **Turnkey** (level below 15) | Ignored | **Turnkey** | Friction elimination. Fit verification transferred entirely to the buyer via self-service. |
| **Structural** (15 and above) | $\hat{F}_{search} \ge 0.50$ | **Search-led** | Portable evaluation artifacts, market education, and reachability infrastructure. |
| **Structural** | $\hat{F}_{consensus} \ge 0.50$ | **Consensus-led** | Stakeholder objective reconciliation matrices and internal political risk containment. |
| **Structural** | $\hat{F}_{implementation} \ge 0.50$ | **Implementation-led** | Bilateral technical discovery, prospective failure stress-testing, and mutual governance. |
| **Structural** | None reaches 0.50 | **Composed** | Top two instruments deployed in direct proportion to relative component weights. |

Level is read from base friction and direction from the amplified components, which is why discovery rotates a deal without reclassifying it. The [Deal Triage Calculator](../../practice/deal-triage-calculator.md) emits both, and the five values in the Motion Routing column are the words it returns.

---

## 2. Motion Specifications

### Turnkey

* **Deal Profile:** Minimal integration surface, singular sign-off authority, and immediate native workflow alignment.
* **Seller Instruments:** Automated provisioning, published pricing, self-service trial environments, and zero-touch onboarding. No instrument file: a short vector needs none.
* **Primary Failure Mode:** Misclassifying structural friction as turnkey. Low initial seat counts within complex enterprise architectures mask downstream integration barriers.

### Search-led

* **Deal Profile:** High buyer uncertainty regarding category boundaries, vendor landscape, or baseline technical viability.
* **Blocker Decomposition:**
  * *Category Unnamed:* Deploys commercial teaching, reference architectures, and diagnostic frameworks.
  * *Vendor Unreachable:* Deploys marketplace agreements, system integrator distribution, and purchasing vehicles. This blocker falls largely on the seller, and neither education nor a trial reduces it. Research is in [channel-collapse.md](../02-research/channel-collapse.md).
  * *Fit Unverified:* Deploys sandboxes, standardized proofs-of-concept, and self-serve evaluation suites.
* **Seller Instruments:** Commercial teaching, reference architectures, sandboxes and channel agreements. No instrument file in this repository.
* **Primary Failure Mode:** Mid-cycle category commoditization. As educational instruments succeed, search costs drop, and the buyer transitions to price-based vendor comparisons.

### Consensus-led

* **Deal Profile:** Technical viability is established, but misaligned cross-functional stakeholder incentives block internal transaction approval.
* **Seller Instruments:** Cross-department objective mapping, champion-enablement collateral, and bilateral decision-criteria frameworks.
* **Operational Rule:** Identified as an active theoretical gap in this repository. Routing to this motion flags an uninstrumented deal boundary during forecast triage. No dedicated instrument exists in this repository, and the incumbent practice (economic-buyer access, written decision criteria, champion development) lives outside the framework. Research on why the component resists the other two motions' instruments is in [buying-center-dynamics.md](../02-research/buying-center-dynamics.md).

### Implementation-led

* **Deal Profile:** Category is established, but high operational risk, deep legacy dependencies, or architectural integration complexity threatens delivery viability.
* **Seller Instruments:** Four sequenced pre-signature governance artifacts:
  1. *[Contextual Blueprint](../../practice/implementation-motion/01-discovery-contextual-blueprint.md):* Rigorous baseline mapping of operational and technical workflows.
  2. *[Red Team Protocol](../../practice/implementation-motion/02-validation-red-team-protocol.md):* Structured prospective hindsight sessions to expose latent failure modes.
  3. *[Mutual Implementation Plan](../../practice/implementation-motion/03-closing-mutual-implementation-plan.md):* Formal bilateral resource and decision-authority allocation.
  4. *[Adoption Review](../../practice/implementation-motion/04-sustaining-adoption-review.md):* Post-signature metric verification confirming target value realization.
* **Primary Failure Mode:** Applying implementation governance to search-dominant deals, forcing operational rigor onto an uncommitted prospect.

---

## 3. Structural Vector Dynamics and Category Drift

Classification represents a dynamic vector position, not an immutable deal attribute:

* **Expansion Rotation (Turnkey to Implementation-led):** Departmental adoption expands into an enterprise-wide rollout, introducing compliance, security, and architectural friction that carries the level above 15.
* **Category Maturation (Search-led to Implementation-led):** Industry-wide education completes, eliminating search friction and concentrating buyer risk on technical deployment.
* **Discovery Reclassification (Search-led to Implementation-led):** Discovery surfaces unmapped integration dependencies, requiring immediate rotation from educational collateral to implementation governance.

```
Category Evolution Lifecycle:
Emerging Category      -> High F_search + High F_implementation -> Search-led / Composed
Consolidating Category -> F_search collapses; F_implementation remains -> Implementation-led
Commoditized Category  -> All components fall below 15 -> Turnkey (apparatus retired)
```

The second and third transitions are the pair reps miss, and they miss the third more often, because nothing external changes to prompt a re-score.

---

## 4. Implementation-led Exclusion Criteria

Deploying the implementation chain when transaction surplus cannot support enablement overhead destroys deal margin. When any condition below is met, decline the transaction or route away from the implementation-led motion.

* **1. No Operational Baseline Exists**
  * *Failure:* Mapping a nonexistent workflow produces fabricated alignment. Red Team sessions then stress-test fictional parameters.
  * *Prescribed Route:* Decline the implementation-led motion. Direct the buyer to advisory engagements to establish processes, then re-qualify.
* **2. Transaction Value Cannot Support Enablement Overhead**
  * *Failure:* Solutions-engineering resource expenditure exceeds first-year gross margin contribution.
  * *Prescribed Route:* Route to Turnkey self-service evaluation, or decline.
  * *Under review.* First-year gross margin is a single-shot test. [05-seller-surplus-model.md](./05-seller-surplus-model.md) section 7 shows pre-sale investment amortizes across the renewal stream, so this criterion is correct where retention is weak and too strict where it holds. [07-governance-forms.md](./07-governance-forms.md) section 6 gives the level-and-frequency split that replaces it.
* **3. Category Has Commoditized**
  * *Failure:* Standardized integrations and reduced switching costs drive transaction friction below the apparatus boundary.
  * *Prescribed Route:* Re-score the deal, migrate to Turnkey instruments, and retire pre-sale engineering workflows.
* **4. Specification Is Externally Fixed**
  * *Failure:* Regulatory mandates or rigid requests for proposal fix delivery parameters, eliminating discovery surplus.
  * *Prescribed Route:* Compete strictly on unit economics, service level guarantees, and delivery credibility.
* **5. Buyer Lacks Operational Implementation Capacity**
  * *Failure:* The MIP assigns mandatory tasks to nonexistent buyer engineering personnel, guaranteeing deployment failure.
  * *Prescribed Route:* Defer the cycle until internal buyer capacity is hired, or contract as a fully managed service.
* **6. Seller Lacks Delivery Depth**
  * *Failure:* Executing superficial Red Team reviews without technical competence generates false operational confidence and downstream delivery failure.
  * *Prescribed Route:* Discontinue the motion until internal delivery and technical capabilities are operational.

The first three are properties of the deal. The last three are properties of the environment or the seller, and they are the ones teams skip when auditing their own boundary.

---

## 5. Operational Failure Mode Checklist

* **Under-Scoping Structural Deals:** Deploying Turnkey instruments on a deal at level 15 or above induces procurement gridlock and post-signature churn.
* **Over-Scoping Turnkey Deals:** Deploying pre-sale engineering protocols on low-friction transactions inflates acquisition cost and drives prospects to lower-overhead alternatives.
* **Conflating Unnamed Categories with Absence of Competition:** Treating an unnamed category as a narrow vendor set artificially deflates $F_{search}$. Absence of established market vocabulary represents maximum search friction.
* **Forcing Monolithic Motions on Composed Deals:** Forcing an individual motion when no component exceeds 50 percent leaves a secondary binding friction point unaddressed.
* **Unilateral MIP Commitment:** Executing pre-sale engineering without mandatory, reciprocal buyer resource investments results in uncommitted pipeline and deal drift.
* **Superficial Red Team Validation:** Failing to aggressively surface prospective systemic failures creates false security and shifts execution breakdowns past signature.

---

## Related Files

* [00-tcg-constitution.md](./00-tcg-constitution.md) — Formal derivation of Axioms I and II.
* [06-friction-vector.md](./06-friction-vector.md) — Vector space geometry and apparatus boundary derivations.
* [07-governance-forms.md](./07-governance-forms.md) — Post-signature governance structures and transaction frequency.
* [09-motion-vocabulary.md](./09-motion-vocabulary.md) — Translation mappings for legacy go-to-market frameworks.
* [deal-triage-calculator.md](../../practice/deal-triage-calculator.md) — Algorithmic quantification of level and direction.
