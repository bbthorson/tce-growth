---
title: "The Sustaining Adoption Review (The Proof)"
layer: practice
status: active
version: 1.0
operationalizes: [axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# The Sustaining Adoption Review (The Proof)

**Version:** 1.0

**Motion:** **Implementation-led**. Fourth of four artifacts, after the MIP.

**Audience:** Customer Success / Implementation Lead / AE / Customer Executive Sponsor

**Goal:** To keep the surplus the MIP locked in, by transferring what the seller learned, measuring whether value actually landed, and re-earning the right to renew.

| | |
|---|---|
| **Inputs** | Signed [MIP](./03-closing-mutual-implementation-plan.md), the filled [Blueprint](./01-discovery-contextual-blueprint.md), and the [Red Team](./02-validation-red-team-protocol.md) risk register. |
| **Outputs** | A receipted handoff packet, a completed RE-AIM review per cycle, and a renewal posture backed by evidence rather than relationship. |
| **Next step** | Renewal, expansion, or a documented decision to let the account lapse. |
| **Owner** | CS or Implementation Lead. The AE stays accountable through the first review under vested compensation ([07-governance-forms.md](../../theory/01-foundation/07-governance-forms.md) section 5). |
| **Reduces** | Post-signature defection and drift (Axiom III). Prevents $\Delta_A$ from resetting at the handoff boundary. |

---

## Why this artifact exists

Axiom III governs whether a deal persists, and the [Constitution's Handoff Rule](../../theory/01-foundation/00-tcg-constitution.md) states the mechanism plainly. The asymmetry assessment the seller produced must transfer intact to Customer Success, or the bilateral asymmetry gap ($\Delta_A$, meaning the combined ignorance on both sides of the relationship) resets to near maximum on the receiving side. The Blueprint is the institutional memory that prevents the **Fumbled Handoff** failure mode.

The first three artifacts drive $\Delta_A$ toward zero before signature. Nothing keeps it there. This document is the maintenance.

> [!NOTE]
> **Genre.** This is a fill-in template in the same family as the Blueprint and the MIP, not a scored instrument like the [Asymmetry Scorecard](../asymmetry-scorecard.md) or the [Friction Efficiency Index](../friction-efficiency-index.md). It deliberately carries no formulas and no reference bands, so it adds nothing to the repo's uncalibrated-parameter backlog. Judgment, evidenced.

---

## Section 1: The Handoff Packet (T-0 to T+14)

*The deal team knows things that exist nowhere in the CRM. Move them, or the customer explains their own business to a stranger and concludes nobody was listening.*

### 1.1 What transfers

The receiving CS or Implementation Lead confirms each item arrived, in writing. An unchecked box is not a formality, it is a known blind spot.

**From the [Blueprint](./01-discovery-contextual-blueprint.md):**

- [ ] **The Economic Event.** The trigger, the quantified cost of inaction, and why it had to be now.
- [ ] **The Political Capital Map.** Sponsor (writes the check), Beneficiary (looks good if it works), Casualty (loses power, budget, or status if it succeeds).
- [ ] **The Sacred Cows.** Which workflow or team is politically protected, and why.
- [ ] **The Graveyard.** What they tried before and how it failed. Adoption failure is the most common answer and predicts the same risk here.
- [ ] **Stakeholder DNA.** Champion, Sponsor, and the Skeptic who was invited to the Red Team.
- [ ] **The Negative Capability Declaration.** Every limitation the seller stated out loud before signature. CS must know what was promised NOT to work.

**From the [Red Team](./02-validation-red-team-protocol.md):**

- [ ] **The surfaced failure modes**, and which ones remain open at signature.
- [ ] **Skeptic versus adversary classification**, plus the containment strategy for anyone classified as an adversary.

**From the [MIP](./03-closing-mutual-implementation-plan.md):**

- [ ] **The North Star metric** and the date it comes due.
- [ ] **Both sides' resource commitments**, including the buyer's named admin and the hours they committed.
- [ ] **The Resource Expiry Clause** terms and the date they bite.
- [ ] **Go / No-Go launch criteria.**

### 1.2 The receipt

- **Handoff meeting held:** ______ (date). **Attended by:** AE ______, CS lead ______, SE ______.
- **Packet received and reviewed by:** ______________ (signature or written confirmation).
- **Open risks explicitly accepted by CS:** ______________________________

### 1.3 The transfer test

Before the AE steps back, the receiving CS lead answers these from memory. If they cannot, the packet moved but the knowledge did not.

1. Who is the Casualty on this account, and what are they likely to do?
2. What did we promise this customer we could NOT do?
3. What killed their last attempt at solving this?

> [!WARNING]
> **The failure this prevents.** A customer who repeats their entire context to the new team reads the repetition as evidence that the seller's diligence was theater. The Red Team's costly signal is retroactively devalued, which is worse than never having run it. See [Axiom II](../../theory/01-foundation/00-tcg-constitution.md) on why a signal that turns out to be cheap talk does more damage than silence.

---

## Section 2: The Adoption Review (RE-AIM)

*The MIP promised success metrics via RE-AIM and supplied no instrument. This is the instrument.*

RE-AIM (Reach, Effectiveness, Adoption, Implementation, Maintenance) comes from public-health intervention evaluation, where the gap between "works in a trial" and "works in the world" is the whole problem. See [re-aim-framework.md](../../theory/02-research/re-aim-framework.md) for sourcing. Run this at every review cycle.

**Review date:** ______  **Cycle:** [ ] T+90  [ ] T+180  [ ] Annual  [ ] Pre-renewal

| Dimension | What it means here | Evidence to record | Status |
|---|---|---|---|
| **Reach** | License utilization. Are the seats we sold in the hands of people who log in. | Provisioned vs. active seats: ______ / ______ | [ ] Green [ ] Watch [ ] Red |
| **Effectiveness** | Movement on the North Star metric from the MIP, in the customer's own numbers. | Baseline ______ → current ______ | [ ] Green [ ] Watch [ ] Red |
| **Adoption** | Feature consumption depth. Whether users reach the features that carry the value, not just the login screen. | Which value-carrying features are in real use: ______ | [ ] Green [ ] Watch [ ] Red |
| **Implementation** | Configuration fidelity. How far the deployment drifted from the supportable path. | Custom branches or workarounds in place: ______ | [ ] Green [ ] Watch [ ] Red |
| **Maintenance** | Whether value is still being captured, and whether the relationship is compounding. | NRR trajectory, expansion signals, renewal posture: ______ | [ ] Green [ ] Watch [ ] Red |

**Reading the pattern.** The dimensions fail in a specific order and the order tells you the intervention.

- **Reach red, everything else untested.** Deployment stalled. This is a project management problem and the MIP's resource commitments are the lever.
- **Reach green, Adoption red.** Users log in and stay shallow. The value-carrying features are not being reached, which is a training and workflow-design problem rather than a product problem.
- **Adoption green, Effectiveness red.** People use it properly and the North Star has not moved. Either the metric was wrong at signature or the theory of value was. Escalate to the exec sponsor, because this one does not resolve at the practitioner level.
- **Implementation red.** Customization is accumulating into a branch nobody can maintain. Every additional deviation raises the cost of the next upgrade and quietly builds the case for replacement.
- **Everything green, Maintenance red.** Value landed and the relationship still decayed. Go to Section 4, because this is reputation depreciation rather than a delivery failure.

### 2.1 The count re-take

*The [Deal Triage Calculator](../deal-triage-calculator.md) counted three things before the deal was scored. By the first review cycle, all three are known rather than estimated. Record what they turned out to be.*

Run this once, at the first cycle where deployment is far enough along to know. It is not repeated at later cycles.

| Counted at triage | Scored | Actual | Variance |
|---|---|---|---|
| Integration points | ______ | ______ | ______ |
| Workflows that change | ______ | ______ | ______ |
| Undocumented exception paths | ______ | ______ | ______ |
| **Total** | ______ | ______ | ______ |

**Who reads this, and what for.** Not this account. The variance is recorded here and read by the manager across a book, which is the only level at which it means anything. One deal scored at 3 against 11 actual is a hard deal. A rep whose variance runs one direction across five deals is a scoring problem, and the direction says which one: consistently under is a rep routing deals away from apparatus, and consistently over is a rep routing them toward it.

**No band and no threshold.** A variance of 4 on a deal counting 30 items is not the same finding as a variance of 4 on a deal counting 5, and this document does not carry the formula that would tell them apart. Record the numbers. The comparison is the manager's.

This is the only audit the counting instrument has on itself. Counts are checkable where ratings are not, and this is where the check happens.

---

## Section 3: The QBR Protocol

*The [MIP](./03-closing-mutual-implementation-plan.md) already requires a QBR and does not define one. This does.*

### 3.1 Attendance

| Role | Required | Why |
|---|---|---|
| Customer Executive Sponsor | Yes. The MIP commits them. | Sponsor absence is the earliest reliable churn signal. Record it when it happens. |
| Customer Champion | Yes | Runs it daily. Owns the operational truth. |
| CS or Implementation Lead | Yes | Owns the account and the review. |
| AE | First review mandatory | Required for the NRR bonus under vested commission, and the AE carries the pre-signature context. |
| The Casualty from the Blueprint | Invite by name | The stakeholder whose position worsened is the one most able to quietly withdraw cooperation. Inviting them converts a silent adversary into a visible one. |

### 3.2 Cadence

- **T+90.** First review. Coincides with the vested commission clawback window and the Resource Expiry Clause, which makes it the highest-stakes review in the sequence.
- **T+180 and thereafter.** Quarterly through the initial term.
- **Minus 120 days from renewal.** The renewal review. Section 4 governs it.

### 3.3 Agenda

1. **RE-AIM review** from Section 2. Evidence first, narrative second.
2. **Open risks from the Red Team register.** Which closed, which remain, which materialized that nobody predicted. The last category is the one worth the meeting.
3. **Commitment audit, both directions.** Did the buyer supply the admin hours and the data access they committed. Did the vendor supply the SE hours and the training. Name both, including your own misses, out loud and in front of the sponsor.
4. **Decisions.** See below.
5. **Next-cycle commitments**, dated and named.

### 3.4 What a QBR can decide

A review that cannot decide anything is a status meeting with a better name. This one can:

- Reallocate committed resources on either side
- Trigger or waive the Resource Expiry Clause
- Escalate a red RE-AIM dimension to the executive sponsors on both sides
- Revise the North Star metric, with both sponsors signing the revision
- Open an expansion conversation, but only from a position of green Effectiveness

> [!IMPORTANT]
> **Do not open expansion from a yellow account.** Expanding scope while the original promise is unproven is the seller's version of the buyer's hold-up. It converts a recoverable delivery problem into a credibility problem, and it is how a merely disappointed customer becomes a reference against you.

---

## Section 4: Renewal and Reputation Refresh

*Axiom III's second primary derivation: reputation depreciates. What was earned at signature does not carry to renewal without intervening evidence of delivery.*

The Constitution prescribes **demurrage on credibility**, meaning a standing charge against reputation that forces it to be re-earned rather than accumulated. Applied to an account: the trust that closed the deal has been spending down since T-0, and the renewal conversation prices what you have actually delivered since, not what you promised before.

### 4.1 The renewal evidence pack (minus 120 days)

- [ ] **RE-AIM trend across all cycles**, not the latest snapshot. Direction matters more than level.
- [ ] **The North Star metric**, against the number written in the MIP. State the variance plainly, including when it is unflattering.
- [ ] **Commitment ledger.** What each side committed and delivered across the term, both columns.
- [ ] **Risk register outcome.** Which Red Team predictions proved true. Being right about a risk you named and mitigated is the strongest costly signal available at renewal, because a vendor who could not do the work could not have predicted it.
- [ ] **Value delivered in the customer's language**, tied to the original Economic Event.

### 4.2 Reputation tripwires

Each of these means credibility is depreciating faster than delivery is refreshing it. Any one of them changes the renewal from a conversation into a campaign.

| Tripwire | What it signals | Response |
|---|---|---|
| Champion leaves the company or changes role | Institutional memory of why they bought just walked out | Re-run the handoff packet with their successor. Treat it as a new $\Delta_A$ to close. |
| Exec sponsor misses two consecutive QBRs | The initiative lost its executive patron | Escalate through the AE. Do not let CS absorb this quietly. |
| Support tickets rise while usage falls | Users are struggling and then giving up rather than complaining | Adoption intervention, not a support intervention. |
| Customer stops asking for anything | Read as satisfaction, usually disengagement | Proactive review. Silence is not a green signal. |
| A new competitor is evaluated mid-term | Your delivered value no longer visibly exceeds the switching cost | Return to the Effectiveness evidence. Price the switch honestly. |

### 4.3 Renewal posture

- **Green across RE-AIM, commitments met both ways.** Renew and open expansion. The evidence pack does the selling.
- **Mixed, with the variance named by you before the customer names it.** Renew on the strength of the disclosure. Volunteering a miss is itself a costly signal, because a vendor hiding a problem cannot afford to raise one.
- **Red on Effectiveness at renewal.** Do not discount to hold the logo. Price reduction addresses the direct cost term ($c$) and this is a value-delivery failure, so the lever does not fit the problem. Either commit to a governed remediation with new gates, or let it lapse honestly and keep the reference.

---

## Related

- **Theory:** [TCG Constitution, Axiom III (Law of Governance)](../../theory/01-foundation/00-tcg-constitution.md). This artifact operationalizes the Handoff Rule and the Reputation Depreciation derivation.
- **Academic backing:** [re-aim-framework.md](../../theory/02-research/re-aim-framework.md) for the five dimensions, and [game-theory-and-nrr.md](../../theory/02-research/game-theory-and-nrr.md) for why sustained cooperation requires re-earned trust.
- **CFIR mapping:** [cfir-field-mapping.md](../cfir-field-mapping.md). Round 5 (Churn) maps to the Maintenance dimension and names the same failure signals.
- **Prerequisite:** A signed [MIP](./03-closing-mutual-implementation-plan.md). This artifact has no meaning without one, because it audits commitments the MIP created.
- **Comp alignment:** [07-governance-forms.md](../../theory/01-foundation/07-governance-forms.md) section 5. The T+90 review is the natural clawback checkpoint, and the first QBR is where an expansion bonus would vest.
- **Cohort view:** [friction-efficiency-index.md](../friction-efficiency-index.md) aggregates post-signature effort across closed deals. This artifact governs one account. That one scores the book.
