---
title: "CFIR-to-Field Asset Mapping"
layer: practice
status: active
version: 1.0
operationalizes: [axiom-2, axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# CFIR-to-Field Asset Mapping

**Purpose:** This document maps the Consolidated Framework for Implementation Research (CFIR) constructs to the TCG field assets. CFIR is the "engineering spec" behind the tools reps use — the academic rigor lives here so the templates stay simple.

**Audience:** Framework designers, sales enablement, anyone updating or creating field assets.

**Canonical Reference:** [CFIR Research Paper](../theory/02-research/cfir.md)

**Scope:** CFIR is the spine of this document. Two companion frameworks appear where the artifacts actually use them: RE-AIM supplies the Red Team's five failure dimensions, and Frame Alignment Processes supply the cross-asset consensus tactics. Both are documented in [cfir.md](../theory/02-research/cfir.md) and [re-aim-framework.md](../theory/02-research/re-aim-framework.md). Where a section maps something other than a CFIR construct, it names the source.

---

## How to Read This Document

Each CFIR construct is mapped to the specific field asset section it powers. When updating a field asset, consult this mapping to ensure you're not accidentally removing a construct's coverage. When creating new assets, use this to identify which constructs still need operationalization.

---

## Inner Setting → Contextual Blueprint

The Blueprint's primary job is to diagnose the buyer's Inner Setting. Here's how each section maps:

| Blueprint Section | CFIR Construct | What It Captures | Rep Sees It As |
|---|---|---|---|
| **1.1 The Economic Event** | Tension for Change | Is the status quo intolerable? Is there a forcing function? | "The Bleeding Neck" |
| **1.2 Political Capital Map** | Networks & Communications, Structural Characteristics | Who has power? How does influence flow? Where are the silos? | "Sponsor / Beneficiary / Casualty" |
| **Sacred Cow Scan** | Culture, Compatibility | What norms, habits, or values will the solution violate? | "We've always done it this way" |
| **Graveyard of Previous Attempts** | Implementation Climate (Learning-Centeredness) | Has the org tried and failed before? Is there psychological safety to try again? | "Why it failed last time" |
| **Stakeholder DNA** | Characteristics of Individuals (Self-Efficacy, Knowledge & Beliefs, Org Identification) | Who will champion? Who will resist? What's driving their behavior? | "Driver / Sponsor / Skeptic" |
| **Reciprocity Gate** | Available Resources, Relative Priority | Does the org have capacity? Is this a real priority or a tire kick? | "Willingness to do the work" |

---

## Inner Setting + Characteristics of Individuals → Red Team Protocol

The Red Team's job is to stress-test the Blueprint findings using Prospective Hindsight (Inverted RE-AIM), which means imagining the project has already failed and working backward to the cause. The workshop itself operationalizes one Process construct directly: putting the buyer's skeptic in the room and asking them to attack the plan is CFIR's Engaging construct. The rounds inside the workshop then diagnose Inner Setting and Individuals risks.

Each failure round maps to a CFIR risk:

| Red Team Round | RE-AIM Dimension | CFIR Construct at Risk | What Failure Looks Like |
|---|---|---|---|
| **Round 1: Ghost Town** | Reach | Networks & Communications | Users don't know the tool exists — communication failure |
| **Round 2: Rebellion** | Adoption | Culture, Compatibility, Self-Efficacy | Users refuse to log in — cultural or competence resistance |
| **Round 3: Crash** | Implementation | Structural Characteristics, Available Resources | Technical integration fails — infrastructure or capacity gap |
| **Round 4: So What?** | Effectiveness | Tension for Change, Relative Priority | ROI not demonstrated — wrong KPIs or insufficient tension |
| **Round 5: Churn** | Maintenance | Individual Identification, Implementation Climate | Usage drops off — champion left, leadership changed, fatigue |
| **Round 6: Automation Trap** | N/A (Pre-qualification) | Compatibility (Workflow Maturity) | Workflow is undefined — the Chaos Trap |

### The Saboteur Matrix (CFIR-Based)

The Red Team also classifies resistance using CFIR constructs. This is the mapping between stakeholder behavior and root cause:

| Saboteur Type | Primary CFIR Driver | What They Say | What They Mean | Management Strategy |
|---|---|---|---|---|
| **Structural Skeptic** | Structural Characteristics / Available Resources | "We don't have the budget/staff" | The org lacks absorptive capacity | Co-design a resource plan; focus on Adaptability |
| **Cultural Defender** | Culture / Compatibility | "That's not how we do things" | The innovation threatens group identity | Frame Alignment — connect to existing values |
| **Insecure Traditionalist** | Self-Efficacy / Knowledge & Beliefs | "This is too complex/risky" | Fear of incompetence or status loss | Education, trialability, "sandbox" environments |
| **Political Cynic** | Networks & Communications / Org Identification | "Management always pushes these fads" | Disconnected from the network; low org identification | Peer pressure via Opinion Leaders, not management |
| **Priority Pragmatist** | Relative Priority / Tension for Change | "We have bigger fires to fight" | Tension for Change is too low | Frame Amplification — quantify the cost of inaction |

---

## Implementation Process → Mutual Implementation Plan (MIP)

The MIP is where CFIR's Process domain (Planning, Executing, Reflecting & Evaluating) becomes contractual. It also carries the Readiness constructs past signature, because the Inner Setting conditions the Blueprint diagnosed do not hold themselves in place. At the framework level this is the deal-level case of Axiom II's stakes corollary, meaning bilateral skin in the game between buyer and seller.

| MIP Section | CFIR Construct | What It Ensures |
|---|---|---|
| **Timeline** | Planning | Both parties agree the sequence before work starts, not after |
| **North Star Metric** | Reflecting & Evaluating, Tension for Change (sustained) | The "why" doesn't evaporate post-signature, and one agreed number says whether it held |
| **Resource Commitments** | Executing, Available Resources | Both parties have skin in the game |
| **Resource Expiry Clause** | Relative Priority (forcing function) | Buyer can't stall indefinitely, which creates urgency |
| **Go/No-Go Protocol** | Implementation Climate (Readiness) | We don't launch until the Inner Setting can absorb the change |

---

## Frame Alignment Processes → Cross-Asset Application

Frame Alignment Processes are the four ways to connect an initiative to what a stakeholder already believes. They come from Snow et al. (1986) rather than from CFIR. They sit in this document because CFIR names what is blocking a stakeholder and these are the moves that shift the stakeholder once named, and because all three assets use them:

| Frame Process | When to Use | Asset | Example |
|---|---|---|---|
| **Frame Bridging** | Stakeholder cares about a different outcome than you're selling | Blueprint (Political Capital Map) | "This innovation IS risk mitigation" — bridge your solution to Legal's concern |
| **Frame Amplification** | Tension for Change is too low | Blueprint (Cost of Inaction) | "2 hrs/week × 50 reps = $250K/year in lost productivity" |
| **Frame Extension** | A department feels excluded from the value prop | Red Team (Stakeholder Diagnosis) | "This isn't just about sales efficiency — it's about data governance" (brings IT on board) |
| **Frame Transformation** | A stakeholder holds a fundamentally incorrect belief | Red Team (Gap Analysis) | "Automation doesn't kill creativity — it liberates you from drudgery" |

---

## Intervention Characteristics → Deal Triage Calculator

Two CFIR constructs govern deal triage rather than any single artifact. Both live in the [Deal Triage Calculator](./deal-triage-calculator.md), which routes the deal before an artifact is chosen.

| Calculator Section | CFIR Construct | What It Captures | Rep Sees It As |
|---|---|---|---|
| **Step 0: Workflow Maturity Gate** | Compatibility (maturity sense) | Has the buyer defined this process at all? | "Is there an SOP?" |
| **Step 2 Gate A** | Compatibility (workflow sense) | Is there an encoded workflow for the product to fit, or does the product create the practice? | "Are we replacing something or starting something?" |
| **Step 2 Gate B** | Trialability | Can the buyer verify fit themselves, cheaply, and walk away? | "Can they just try it?" |
| **Step 2 divergence count** | Compatibility (workflow sense) | How many steps in the buyer's workflow have no counterpart in the product's | "How weird is their setup?" |

Gate B is where Trialability does its work, and the reason it belongs in triage rather than in an artifact: a buyer who can measure fit for themselves does not need the seller to prove it, which removes the condition the implementation artifacts exist to satisfy.

The divergence count enters as a multiplier on the implementation component rather than as a parallel score read alongside the total. A high-divergence deal therefore reads as implementation-dominant rather than needing a routing exception, which makes Compatibility's effect on the motion arithmetic rather than a table row. Research backing sits in [process-misfit.md](../theory/02-research/process-misfit.md).

---

## Coverage Gaps

The following CFIR constructs are **not yet operationalized** in any field asset:

| CFIR Construct | Domain | Gap Description | Suggested Action |
|---|---|---|---|
| **Cosmopolitanism** | Outer Setting | How networked is the org with external peers? Insular orgs resist outside ideas. | Add to Blueprint: "How does your org evaluate new technology? Internal review only, or do you benchmark against peers?" |
| **Learning-Centeredness** | Culture | Is there psychological safety to fail? Critical for adoption but not directly asked. | Add to Blueprint Sacred Cow Scan or Red Team Round 2 probes |

---

## Related

- [00-tcg-constitution.md](../theory/01-foundation/00-tcg-constitution.md) — The axioms the mapped artifacts serve. The artifacts themselves are field assets, linked below.
- [cfir.md](../theory/02-research/cfir.md) — Canonical CFIR reference; the academic basis for this mapping.
- [re-aim-framework.md](../theory/02-research/re-aim-framework.md) — Companion framework for post-sale measurement.
- Field artifacts being mapped:
  - [01-discovery-contextual-blueprint.md](./implementation-motion/01-discovery-contextual-blueprint.md)
  - [02-validation-red-team-protocol.md](./implementation-motion/02-validation-red-team-protocol.md)
  - [03-closing-mutual-implementation-plan.md](./implementation-motion/03-closing-mutual-implementation-plan.md)
  - [04-sustaining-adoption-review.md](./implementation-motion/04-sustaining-adoption-review.md) — post-signature; reuses the Round 5 (Churn) mapping to the Maintenance dimension above.

---

**Version:** 1.0
**Last Updated:** 2026-08-28
