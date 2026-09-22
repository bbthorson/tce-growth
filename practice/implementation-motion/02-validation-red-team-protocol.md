---
title: "The Red Team Protocol (The Validator)"
layer: practice
status: active
version: 2.0
operationalizes: [axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# The Red Team Protocol (The Validator)

Version: 2.0  
Motion: **Implementation-led**. Second of four artifacts, after the Blueprint.  
Audience: Technical Evaluators / End Users / Skeptics  
Goal: To convert "Rational Fear" into "Confidence" and identify the Saboteur.

| | |
|---|---|
| **Inputs** | Completed [Blueprint](./01-discovery-contextual-blueprint.md) with Catalyst, Stakeholder DNA, and Sacred Cows mapped. Skeptic and Adversary identified. |
| **Outputs** | Pre-mortem failure mode list; mitigation map; Skeptic-vs-Adversary classification; signed "Gap Analysis" of product limits. |
| **Next step** | [Mutual Implementation Plan](./03-closing-mutual-implementation-plan.md) — contractualize the mitigations. |
| **Owner** | AE + Solutions Engineer (with workshop facilitator). |
| **Reduces** | Buyer Uncertainty (I_buyer) via costly signals. |

## Rep Compliance: The Ratio Check

*Before the workshop, verify your content density:*

- \[ \] **20% Business (Why):** Re-state the North Star (briefly).  
- \[ \] **50% Product (What):** Stress-test the failure modes.  
- \[ \] **30% Technical (How):** Preview the resource cost of the fix.

## Section 1: The Pre-Mortem (The Product What)

*Assume it is 12 months from now, and the project has failed. Why?*

### 1.1 The Failure Modes (Inverted RE-AIM)

- **Adoption Failure:** Users didn't log in because... (e.g., "Too many clicks")  
- **Technical Failure:** The integration broke because... (e.g., "Bad data quality")  
- **Political Failure:** The project was killed because... (e.g., "Sponsor left")

### 1.2 The Gap Analysis (Honesty Hour)

*Where does the product struggle in your specific environment?*

- **Gap Identified:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
- **Proposed Workaround:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
- **Buyer Sign-off:** "We accept this workaround." \[Yes/No\]

## Section 2: The Resource Preview (The Technical How)

*If these failures happen, what is the cost to fix them?*

### 2.1 The Crisis Response Team

- **When X breaks, who fixes it?**  
- **Buyer Owner:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
- **Vendor Owner:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## Section 3: The Stakeholder Diagnosis (Internal Only)

*Map the room during the session.*

### 3.1 The Resistance Profile

- **The Skeptic:** Asked hard questions about data/features. (Action: **Co-opt** with answers).  
- **The Saboteur:** Asked vague questions about "culture" or "timing"; blocked access. (Action: **Contain** via Political Map).

**Decision Gate:** Do we have a credible path to technical victory? If Yes \-\> Proceed to MIP.

---

# The Red Team Facilitator Guide

Internal Name: The Pre-Mortem / Red Team Workshop

External Name: Implementation Feasibility & Risk Assessment

Time: 60 Minutes

Required Attendees: Your Champion \+ The Skeptic (Technical/Operational Lead)

*Frame the session as 'Protecting the Champion's Reputation,' not just 'Finding Failure.' Add a 'Fast Track' option if no risks are found.*

---

## Phase I: The Rules of Engagement (5 Minutes)

*Set the stage. You must disarm the "Sales Resistance" immediately.*

**The Script (Read Verbatim):**

"Thanks for joining. I want to be clear: **This is not a sales pitch.**

We are here because large IT projects deliver 56% less value than predicted, on average, across more than 5,400 projects over $15 million (McKinsey with the University of Oxford, 2012), and the usual cause is implementation friction nobody mapped in advance. We refuse to let that happen to our partners.

Today, we are going to use a method called **'Prospective Hindsight.'** We are going to fast-forward 6 months and imagine this project has **failed**. Then, we will work backward to figure out why.

**To the Technical Team:** Your job today is to be the 'Red Team.' I want you to poke holes in our plan. If you see a technical blocker, a security risk, or a workflow issue, put it on the table. We can't fix what we don't acknowledge."

---

## Phase II: The "Failure Rounds" (Inverted RE-AIM) (35 Minutes)

*The Rep leads 5 rapid-fire rounds. Do not argue with the risks raised. Validate them and write them down.*

### Round 1: Reach Failure (The "Ghost Town" Risk)

**The Prompt:**

"Imagine it is Launch Day \+ 30\. The system is live, but **50% of your target users don't even know it exists.** Why did that happen?"

- **Facilitator Probes:**  
  * Did the email training get caught in spam?  
  * Are remote employees excluded from the network?  
  * Did we rely on a "Intranet post" that nobody reads?

### Round 2: Adoption Failure (The "Rebellion" Risk)

**The Prompt:**

"Everyone knows about the tool, but a specific department or location **refuses to log in**. They are sticking to their spreadsheets. Who is it, and why?"

- **Facilitator Probes:**  
  * Is it the \[Department identified in Blueprint\] because of the "Sacred Cow"?  
  * Is the Union blocking it?  
  * Is the new workflow actually *slower* for them than the old one?

### Round 3: Implementation Failure (The "Crash" Risk)

**The Prompt:**

"We flip the switch, and the system breaks immediately. Or, it breaks a downstream system (like your ERP). **What broke first?**"

- **Facilitator Probes:**  
  * Did the API token expire?  
  * Did the firewall block the data sync?  
  * Did we accidentally corrupt the data migration?

### Round 4: Effectiveness Failure (The "So What?" Risk)

**The Prompt:**

"People are using it, the tech is stable, but 6 months from now the CFO says **'This was a waste of money.'** Why are we failing to show ROI?"

- **Facilitator Probes:**  
  * Are we measuring the wrong KPI?  
  * Is the data "clean" enough to trust the reports?  
  * Did we save time but fail to cut costs?

### Round 5: Maintenance Failure (The "Churn" Risk)

**The Prompt:**

"It is one year from now. The project started well, but usage has dropped off a cliff, and you are cancelling the contract. **What changed?**"

- **Facilitator Probes:**  
  * Did the Champion (you) leave the company?  
  * Did a new Executive come in with a different agenda?  
  * Did we stop training new hires?

### Round 6: Workflow Chaos (The "Automation Trap" Risk)

**The Prompt:**

"Imagine we automate your current process **exactly as it is today**, without changing anything. Does it break? Does it expose problems that were previously hidden by manual workarounds?"

- **Facilitator Probes:**  
  * Is your current process actually broken, but people work around it?  
  * Are there manual "judgment calls" that can't be automated?  
  * Do different teams follow different versions of the process?  
  * Is the process actually undefined (ad-hoc, varies by person)?

**Critical Decision:** If the answer reveals that the workflow is undefined or fundamentally broken, **STOP.**  

**Action:** This is **Quadrant III: The Chaos Trap.** Redirect to Consulting to define the SOP before attempting to sell software.

---

## Phase III: The Mitigation Map (20 Minutes)

*This is where you turn "Complaints" into "Contracts." You categorize every risk identified.*

The Activity:

Share your screen. Categorize the risks raised into the Traffic Light Protocol.

| Risk Status | Definition | Action Required |
| :---- | :---- | :---- |
| **Solvable** | Standard friction. We have a playbook for this. | **Add to Mutual Implementation Plan (MIP).** |
| **Constraint** | A real barrier, but we can work around it. | **Assign Owner (Buyer/Seller) to fix by \[Date\].** |
| **Showstopper** | A fundamental incompatibility (Technical or Cultural). | **PAUSE THE DEAL.** |

**The "Costly Signal" Script (If a Red Risk is found):**

"This risk regarding \[Legacy Database Access\] is a Showstopper. Based on what you've told me, if we can't solve this, this software will become shelf-ware.

**I recommend we pause the commercial discussion right now.**

My Solutions Architect needs 48 hours to investigate if we can build a custom bridge for this. If we can't, I will tell you, and we won't proceed to a Proposal. Is that fair?"

---

### Facilitator Notes (Internal Training)

1. **Silence is Data:** If you ask "Who will refuse to use this?" and the room is silent, **call on the Saboteur**. "John, from an IT perspective, who usually complains the loudest about new tools?"  
2. **Don't defend the Product:** If they say "Your UI looks confusing," do not say "Actually, it's very intuitive." Say: "Noted. UI complexity is an Adoption Risk. Let's write that down." Validation lowers defenses.  
3. **The "Go/No-Go" Hook:** You must be willing to kill the deal in Phase III. The moment you say "We should pause," the buyer's trust in you skyrockets. This paradoxically makes them want to buy more.

---

### Next Step

This covers the **Stress Test**. We have identified the risks.

Now we need the final document that legally and operationally solves them.

Ready to draft Asset \#3: The Mutual Implementation Plan (MIP)?

---

## Related

- **Theory:** [TCG Constitution, Axiom III](../../theory/01-foundation/00-tcg-constitution.md) — The Red Team primarily addresses $F_{implementation}$ forecasting and reduces Buyer Uncertainty ($I_{buyer}$) through costly signals satisfying the Single Crossing Property.
- **CFIR mapping:** [cfir-field-mapping.md](../cfir-field-mapping.md) — Implementation Process / Engaging constructs.
- **Academic backing:** [costly-signals.md](../../theory/02-research/costly-signals.md), [re-aim-framework.md](../../theory/02-research/re-aim-framework.md) (inverted RE-AIM is the workshop's structure).
- **Prerequisite:** [01-discovery-contextual-blueprint.md](./01-discovery-contextual-blueprint.md) — You stress-test what discovery surfaced.
- **Next step:** [03-closing-mutual-implementation-plan.md](./03-closing-mutual-implementation-plan.md) — Contractualize the mitigations.
