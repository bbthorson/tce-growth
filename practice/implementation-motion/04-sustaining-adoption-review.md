---
title: "The Sustaining Adoption Review (The Proof)"
layer: practice
kind: instrument
status: active
version: 1.1
operationalizes: [axiom-2, axiom-3]
canonical_source: theory/canon/constitution.md
---

# The Sustaining Adoption Review (The Proof)

**Version:** 1.1

**Motion:** **Implementation-led**. Fourth of four artifacts, after the MIP.

**Goal:** To keep the surplus the MIP locked in, by transferring what the seller learned, measuring whether value landed, and re-earning the right to renew.

| | |
|---|---|
| **Inputs** | Signed [MIP](./03-closing-mutual-implementation-plan.md), the filled [Blueprint](./01-discovery-contextual-blueprint.md), and the [Red Team](./02-validation-red-team-protocol.md) risk register. |
| **Outputs** | A receipted handoff packet, a completed RE-AIM review per cycle, and a renewal posture backed by evidence rather than relationship. |
| **Next step** | Renewal, expansion, or a documented decision to let the account lapse. |
| **Owner** | CS or Implementation Lead. The AE stays accountable through the first review under vested compensation ([governance-forms.md](../../theory/arguments/governance-forms.md) section 5). |
| **Reduces** | Post-signature defection and drift (Axiom II). Prevents $\Delta_A$ from resetting at the handoff boundary. |

---

## Why this artifact exists

Axiom II's governance corollary decides whether a deal persists, and Axiom III's second clause, that verified uncertainty rebuilds unless it is maintained, states the mechanism this artifact exists to run. The Handoff Rule below is that clause applied at the seam between sales and Customer Success. The asymmetry assessment the seller produced must transfer intact to Customer Success, or the bilateral asymmetry gap ($\Delta_A$, the combined ignorance on both sides of the relationship) resets to near maximum on the receiving side. The Blueprint is the institutional memory that prevents the **Fumbled Handoff** failure mode.

The first three artifacts drive $\Delta_A$ toward zero before signature. Nothing keeps it there. This document is the maintenance. It is a fill-in template rather than a scored instrument, so it carries no formulas and adds nothing to the uncalibrated-parameter backlog.

---

## Section 1: The Handoff Packet (T-0 to T+14)

*The deal team knows things that exist nowhere in the CRM. Move them, or the customer explains their own business to a stranger and concludes nobody was listening.*

### 1.1 What transfers

The receiving lead confirms each item arrived, in writing. An unchecked box is a known blind spot.

**From the [Blueprint](./01-discovery-contextual-blueprint.md):**

- [ ] **The Economic Event.** The trigger, the quantified cost of inaction, and why it had to be now.
- [ ] **The Political Capital Map.** Sponsor, Beneficiary, Casualty.
- [ ] **The Sacred Cows.** Which workflow or team is politically protected, and why.
- [ ] **The Graveyard.** What they tried before and how it failed.
- [ ] **Stakeholder DNA.** Champion, Sponsor, and the Skeptic who was invited to the Red Team.
- [ ] **The Negative Capability Declaration.** Every limitation the seller stated before signature. CS must know what was promised NOT to work.

**From the [Red Team](./02-validation-red-team-protocol.md):**

- [ ] **The surfaced failure modes**, and which remain open at signature.
- [ ] **Skeptic versus adversary classification**, plus the containment strategy for any adversary.

**From the [MIP](./03-closing-mutual-implementation-plan.md):**

- [ ] **The North Star metric** and the date it comes due.
- [ ] **Both sides' resource commitments**, including the buyer's named admin and committed hours.
- [ ] **The Resource Expiry Clause** terms and the date they bite.
- [ ] **Go / No-Go launch criteria.**

### 1.2 The receipt and the transfer test

- **Handoff meeting held:** ______ (date). **Attended by:** AE ______, CS lead ______, SE ______.
- **Packet received and reviewed by:** ______________
- **Open risks explicitly accepted by CS:** ______________________________

Before the AE steps back, the receiving lead answers from memory: who is the Casualty on this account and what are they likely to do, what did we promise this customer we could NOT do, and what killed their last attempt at solving this. If they cannot, the packet moved but the knowledge did not.

> [!WARNING]
> **The failure this prevents.** A customer who repeats their entire context to the new team reads the repetition as evidence that the seller's diligence was theater. The Red Team's costly signal is retroactively devalued, which is worse than never having run it. See [Axiom III](../../theory/canon/constitution.md) on why a signal that turns out to be cheap talk does more damage than silence.

---

## Section 2: The Adoption Review (RE-AIM)

*The MIP promised success metrics via RE-AIM and supplied no instrument. This is the instrument.*

RE-AIM (Reach, Effectiveness, Adoption, Implementation, Maintenance) comes from public-health intervention evaluation, where the gap between "works in a trial" and "works in the world" is the whole problem. See [re-aim-framework.md](../../theory/evidence/re-aim-framework.md). Run this at every review cycle.

**Review date:** ______  **Cycle:** [ ] T+90  [ ] T+180  [ ] Annual  [ ] Pre-renewal

| Dimension | What it means here | Evidence to record | Status |
|---|---|---|---|
| **Reach** | License utilization. Are the seats we sold in the hands of people who log in. | Provisioned vs. active seats: ______ / ______ | [ ] Green [ ] Watch [ ] Red |
| **Effectiveness** | Movement on the North Star metric, in the customer's own numbers. | Baseline ______ → current ______ | [ ] Green [ ] Watch [ ] Red |
| **Adoption** | Feature consumption depth. Whether users reach the features that carry the value. | Value-carrying features in real use: ______ | [ ] Green [ ] Watch [ ] Red |
| **Implementation** | Configuration fidelity. How far the deployment drifted from the supportable path. | Custom branches or workarounds in place: ______ | [ ] Green [ ] Watch [ ] Red |
| **Maintenance** | Whether value is still being captured, and whether the relationship is compounding. | NRR trajectory, expansion signals, renewal posture: ______ | [ ] Green [ ] Watch [ ] Red |

**Reading the pattern.** The dimensions fail in a specific order and the order names the intervention. Reach red with everything else untested is a stalled deployment, and the MIP's resource commitments are the lever. Reach green and Adoption red is shallow use, a training and workflow-design problem rather than a product problem. Adoption green and Effectiveness red means the metric or the theory of value was wrong at signature, and it escalates to the executive sponsor because it does not resolve at the practitioner level. Implementation red is customization accumulating into a branch nobody can maintain, which quietly builds the case for replacement. Everything green and Maintenance red is reputation depreciation rather than delivery failure, and Section 4 governs it.

### 2.1 The count re-take

*The [Deal Triage Calculator](../deal-triage-calculator.md) counted three things before the deal was scored. By the first review cycle, all three are known rather than estimated.* Run this once, at the first cycle where deployment is far enough along to know.

| Counted at triage | Scored | Actual | Variance |
|---|---|---|---|
| Integration points | ______ | ______ | ______ |
| Workflows that change | ______ | ______ | ______ |
| Undocumented exception paths | ______ | ______ | ______ |
| **Total** | ______ | ______ | ______ |

The variance is read across a book rather than on this account. One deal scored at 3 against 11 actual is a hard deal. A scorer whose variance runs one direction across five deals is a scoring problem, and the direction says which: consistently under is routing deals away from apparatus, consistently over is routing them toward it. No band and no threshold apply, because a variance of 4 on a deal counting 30 items is not the same finding as a variance of 4 on a deal counting 5. This is the only audit the counting instrument has on itself.

---

## Section 3: The QBR Protocol

*The [MIP](./03-closing-mutual-implementation-plan.md) already requires a QBR and does not define one. This does.*

**Attendance.** The customer executive sponsor, whom the MIP commits and whose absence is the earliest reliable churn signal. The customer champion, who owns the operational truth. The CS or Implementation Lead, who owns the review. The AE at the first review, who carries the pre-signature context. And the Casualty from the Blueprint, invited by name, because the stakeholder whose position worsened is the one most able to withdraw cooperation quietly, and the invitation converts a silent adversary into a visible one.

**Cadence.** T+90 first, which coincides with the Resource Expiry Clause and is the highest-stakes review in the sequence. Quarterly thereafter through the initial term. Then the renewal review at minus 120 days, which Section 4 governs.

**Agenda.** The RE-AIM review, evidence first. Open risks from the Red Team register: which closed, which remain, and which materialized that nobody predicted, the last being the category worth the meeting. A commitment audit in both directions, naming the seller's own misses out loud in front of the sponsor. Decisions. Next-cycle commitments, dated and named.

**What a QBR can decide.** Reallocate committed resources on either side. Trigger or waive the Resource Expiry Clause. Escalate a red dimension to both executive sponsors. Revise the North Star metric, with both sponsors signing. Open an expansion conversation, but only from green Effectiveness.

> [!IMPORTANT]
> **Do not open expansion from a yellow account.** Expanding scope while the original promise is unproven is the seller's version of the buyer's hold-up. It converts a recoverable delivery problem into a credibility problem.

---

## Section 4: Renewal and Reputation Refresh

*Axiom III's second clause after signature: reputation depreciates. What was earned at signature does not carry to renewal without intervening evidence of delivery.*

The Constitution prescribes **demurrage on credibility**, a standing charge against reputation that forces it to be re-earned rather than accumulated. The trust that closed the deal has been spending down since T-0, and the renewal conversation prices what has been delivered since, not what was promised before.

### 4.1 The renewal evidence pack (minus 120 days)

- [ ] **RE-AIM trend across all cycles**, not the latest snapshot. Direction matters more than level.
- [ ] **The North Star metric** against the number written in the MIP, with the variance stated plainly.
- [ ] **Commitment ledger.** What each side committed and delivered across the term.
- [ ] **Risk register outcome.** Which Red Team predictions proved true. Being right about a risk you named and mitigated is the strongest costly signal available at renewal, because a vendor who could not do the work could not have predicted it.
- [ ] **Value delivered in the customer's language**, tied to the original Economic Event.

### 4.2 Reputation tripwires

Each of these means credibility is depreciating faster than delivery is refreshing it. Any one changes the renewal from a conversation into a campaign.

| Tripwire | What it signals | Response |
|---|---|---|
| Champion leaves or changes role | Institutional memory of why they bought just walked out | Re-run the handoff packet with the successor. Treat it as a new $\Delta_A$ to close. |
| Exec sponsor misses two consecutive QBRs | The initiative lost its executive patron | Escalate through the AE. Do not let CS absorb it quietly. |
| Support tickets rise while usage falls | Users are struggling and then giving up | Adoption intervention, not a support intervention. |
| Customer stops asking for anything | Usually disengagement, read as satisfaction | Proactive review. Silence is not a green signal. |
| A competitor is evaluated mid-term | Delivered value no longer visibly exceeds the switching cost | Return to the Effectiveness evidence. Price the switch honestly. |

### 4.3 Renewal posture

- **Green across RE-AIM, commitments met both ways.** Renew and open expansion. The evidence pack does the selling.
- **Mixed, with the variance named by you before the customer names it.** Renew on the strength of the disclosure. Volunteering a miss is itself a costly signal, because a vendor hiding a problem cannot afford to raise one.
- **Red on Effectiveness at renewal.** Do not discount to hold the logo. Price addresses the direct cost term ($c$) and this is a value-delivery failure, so the lever does not fit the problem. Either commit to a governed remediation with new gates, or let it lapse honestly and keep the reference.

---

## Related

- **Theory:** [TCG Constitution, Axiom II (Law of Asset Specificity), governance corollary, and Axiom III's second clause](../../theory/canon/constitution.md). This artifact operationalizes the Handoff Rule and reputation depreciation, both Axiom III's second clause applied after signature.
- **Academic backing:** [re-aim-framework.md](../../theory/evidence/re-aim-framework.md) for the five dimensions, and [game-theory-and-nrr.md](../../theory/evidence/game-theory-and-nrr.md) for why sustained cooperation requires re-earned trust.
- **CFIR mapping:** [cfir-field-mapping.md](../cfir-field-mapping.md). Round 5 (Churn) maps to the Maintenance dimension.
- **Prerequisite:** A signed [MIP](./03-closing-mutual-implementation-plan.md). This artifact audits commitments the MIP created.
- **Comp alignment:** [governance-forms.md](../../theory/arguments/governance-forms.md) section 5. The T+90 review is the natural clawback checkpoint, and the first QBR is where an expansion bonus would vest.
- **Cohort view:** [friction-efficiency-index.md](../friction-efficiency-index.md) aggregates post-signature effort across closed deals. This artifact governs one account. That one scores the book.
