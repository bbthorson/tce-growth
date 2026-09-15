---
title: "The Mutual Implementation Plan (The Execution)"
layer: practice
status: active
version: 2.0
operationalizes: [axiom-2]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# The Mutual Implementation Plan (The Execution)

Version: 2.0  
Motion: **Implementation-led**. Third of four artifacts, after the Red Team.  
Audience: Project Managers / Procurement / Legal  
Goal: To contractualize the outcome and lock in the "Infinite Game."

| | |
|---|---|
| **Inputs** | [Blueprint](./01-discovery-contextual-blueprint.md) + [Red Team](./02-validation-red-team-protocol.md) outputs. Identified risks, mitigations, and bilateral resource commitments. |
| **Outputs** | Signed MIP with North Star metric, Governance Structure, Go/No-Go Protocol. Resource plan attached to contract. |
| **Next step** | [Sustaining Adoption Review](./04-sustaining-adoption-review.md) (handoff packet, then RE-AIM reviews); vested compensation terms activate ([05-governance-forms.md](../../theory/01-foundation/05-governance-forms.md) section 5). |
| **Owner** | AE + Customer PM + Procurement + Legal. |
| **Reduces** | Defection risk via mutual skin in the game (Axiom II — Governance). |

## Rep Compliance: The Ratio Check

*Before the close, verify your content density:*

- \[ \] **10% Business (Why):** The North Star Metric (The Anchor).  
- \[ \] **20% Product (What):** Final Scope Definition.  
- \[ \] **70% Technical (How):** Dates, Dollars, and Data.

## Section 1: The North Star (The Business Why)

*We are doing this work to achieve ONE thing.*

### 1.1 The Success Metric (Vested Interest)

- **The Goal:** Achieve \[X\]% Adoption / $\[Y\] ROI by \[Date\].  
- **The Stake:** If we hit this, we unlock \[Phase 2 / Renewal\].  
- **The Clawback Trigger:** (Internal Note) If this metric is missed due to our failure, credits are issued.

## Section 2: The Governance Structure (The Technical How)

*Who does what, and when?*

### 2.1 The Timeline

- **T-0 (Signature):** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
- **T-30 (Technical Integration):** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
- **T-60 (User Onboarding):** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
- **T-90 (First Value Delivered):** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 2.2 Resource Commitments (Skin in the Game)

- **Buyer Commitments:**  
  * \[ \] Dedicated Admin (10 hrs/week).  
  * \[ \] Data Clean-up Team (One-time sprint).  
  * \[ \] Executive Sponsor presence at QBR.  
- **Vendor Commitments:**  
  * \[ \] Solutions Engineer (5 hrs/week).  
  * \[ \] Custom Training Session.

### 2.3 Resource Expiry Clause (Buyer Hostage / "Use It or Lose It")

*Goal: Prevent buyer opportunism by creating accountability for timely implementation. This clause acts as "Skin in the Game" for the buyer.*

**Theory:** Without a forcing function, buyers can internalize their coordination costs onto the vendor by stalling indefinitely. This clause creates Loss Aversion by making the buyer's inaction costly.

**The Clause:**

> Implementation resources (Solutions Engineering, Training, Support Hours) are reserved for **[DEFINE TIMEFRAME]** from contract signature (T-0).  
>
> If buyer-caused delays (e.g., delayed data access, unavailable stakeholders, postponed training sessions) cause the project to stall beyond **T+[TIMEFRAME]**, the following occurs:
>
> - \[ \] **Option A:** Implementation resources expire. Restart requires a **Restart Fee** of $\_\_\_\_\_\_.
> - \[ \] **Option B:** Resource reservation extends for an additional **[TIMEFRAME]** at a **Holding Fee** of $\_\_\_\_\_/month.
> - \[ \] **Option C:** *(Custom arrangement based on your business model)*

**Defining the Timeframe:** 

> [!WARNING]
> **Calibration Required:** The timeframe must be defensible and aligned with typical implementation cycles in your industry. Use the following exercise:

**Exercise: How to Set [TIMEFRAME]**

1. **Review Historical Data:** What is the median time-to-value for successful implementations? (e.g., 90 days, 120 days)
2. **Add Buffer:** Add 25-50% buffer for buyer coordination delays. (e.g., 90 days × 1.5 = 135 days)
3. **Round to Milestone:** Align to a natural milestone (e.g., 90 days, 120 days, 6 months).
4. **Test with Champion:** "If we can't get this live within [X] days due to delays on your side, should we pause and restart later?" (Gauge their reaction)

**Safe Harbor Exceptions:** Resource expiry is waived for delays caused by:
- Vendor-side technical failures
- Force majeure events (M&A, leadership changes, regulatory changes)
- Mutually agreed scope changes

**Rationale:** This prevents the buyer from treating your implementation team as infinite, free labor. It internalizes their coordination costs and creates urgency.

## Section 3: The "Go / No-Go" Protocol

*We do not launch until we are safe.*

### 3.1 The Launch Criteria

- \[ \] Integration Passed Stress Test.  
- \[ \] 80% of Users Trained.  
- \[ \] Executive Sign-off Received.

Signature Block:
"By signing, we agree not just to the software, but to the work required to make it successful."

---

**Prerequisites:** This document builds on the outputs of [The Contextual Blueprint](./01-discovery-contextual-blueprint.md) (Phase 01) and [The Red Team Protocol](./02-validation-red-team-protocol.md) (Phase 02). The MIP should incorporate the risks and mitigations identified in those prior phases.

---

## Related

- **Theory:** [TCG Constitution, Axiom II (Governance)](../../theory/01-foundation/00-tcg-constitution.md) — The MIP operationalizes the deal-level case of recursive cooperation; bilateral skin in the game between buyer and seller.
- **Academic backing:** [game-theory-and-nrr.md](../../theory/02-research/game-theory-and-nrr.md) — Shadow of the Future; why mutual skin in the game shifts the Nash equilibrium.
- **CFIR mapping:** [cfir-field-mapping.md](../cfir-field-mapping.md) — Implementation Process constructs (Planning, Executing, Reflecting & Evaluating).
- **Comp alignment:** [05-governance-forms.md](../../theory/01-foundation/05-governance-forms.md) section 5. Rep compensation must follow MIP outcomes, not signature.
