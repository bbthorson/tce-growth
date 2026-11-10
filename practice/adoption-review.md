---
title: "The Sustaining Adoption Review"
layer: practice
status: active
version: 2.0
operationalizes: [axiom-2, axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# The Sustaining Adoption Review

Version: 2.0
Goal: After signature, keep the gaps the two deal ledgers closed from reopening, catch the fit drifting apart before the renewal finds it, and earn the renewal on delivered evidence. It runs the Maintain stage of the [Enforcement Ledger](./enforcement-ledger.md) and the [Bargaining Ledger](./bargaining-ledger.md), and the standing review the Enforcement Ledger's Stage agreed before anything was sunk.

**Canonical reference:** [Constitution 6.4](../theory/01-foundation/00-tcg-constitution.md), Axiom III's drift and enforcement corollaries. The derivation is [08-from-axioms-to-instruments.md](../theory/01-foundation/08-from-axioms-to-instruments.md) sections 4 and 5, and the functional forms are [02-mathematical-models.md](../theory/01-foundation/02-mathematical-models.md) sections 5.3, 5.5 and 5.7.

| | |
|---|---|
| **Inputs** | The signed Enforcement Ledger: its deal record, rows, gates, outcome measure and the standing review's terms. The Bargaining Ledger's private map and shared arrangement record. |
| **Outputs** | A receipted handoff, a review record per cycle with each finding coded by cause and the right it invoked, and a renewal posture with its forecast call. |
| **Next step** | Renewal, a remediation under new gates, or a lapse decided in writing. The counts re-taken at renewal go to the [Deal Triage Calculator](./deal-triage-calculator.md)'s audit. An expansion that reaches new roles or steps opens there as a new deal. |
| **Owner** | The account manager, whose pay carries a stake at the renewal it maintains ([05-governance-forms.md](../theory/01-foundation/05-governance-forms.md) section 5). The account executive stays accountable through the first review. |

**When to run it, and how deep.** The seller funds maintenance only while the margin it holds at the next renewal covers keeping pace with the rebuild ([02-mathematical-models.md](../theory/01-foundation/02-mathematical-models.md) section 5.7).

- **One-shot deal.** No renewal follows, so the seller has nothing to protect. Do not run it.
- **A plug-in purchase,** where nothing was built and a trial verified fit. The renewal is the review: read use and the outcome measure, and re-take the triage's counts for its audit.
- **Recurring, with specific exposure.** Compare the hours a dedicated cycle takes, at the seller's cost, with the renewal's margin, counting only where a review can still change the renewal. Where the hours cover only some accounts, give the dedicated cycle to those where a review can still change the renewal most, which are not necessarily those the forecast call marks at risk (Constitution, drift corollary). Where the margin covers them, run all of it. Otherwise run it **pooled**: use and the outcome measure from telemetry, release notices sent automatically to every account whose mapped touchpoints a release touches, and the out-of-cycle triggers in section 2.4 routed to a pooled account manager who runs one review when a trigger fires. A pooled review reads stale rows and divergences from the two sides' change logs, so it still counts.

---

## 1. The handoff

A handoff is an occupant change on the seller's side. If what the account executive knows does not cross, the seller's half of the policing gap reopens at once.

**What transfers.** The receiving account manager checks each item in writing.

- [ ] **From the Enforcement Ledger:** the deal record (the economic event, the sponsor, champion and skeptic, the declared limits), every row with its evidence and the date of that evidence, the rows open at signature and those marked as surfacing in use with their risk carrier, the gates with their hostages and allocated rights, the outcome measure, the standing review's terms, and any previous attempt with why it failed.
- [ ] **From the Bargaining Ledger:** the arrangement record, the bond each exposed role holds, and any written overrule. The private map moves to a restricted document with a named access list: the account team that inherits the relationship, and no one else.

**The transfer test.** The account executive's manager asks the account manager, without notes, which roles read −1 and what answers each, what the seller declared it could not do, and what killed the buyer's last attempt, and checks the answers against the ledgers. On a fail the receipt stays unsigned, and the account executive stays on the account through the first review.

---

## 2. The standing review

This is Axiom III's plan for what nobody could foresee. A review that reads neither ledger and can invoke no right is a sales meeting, and it does not count.

### 2.1 What it reads

| Reading | Source | What to read |
|---|---|---|
| **Stale evidence** | What was verified goes stale | Each Enforcement Ledger row whose touchpoint, system, data or performing role a release, staff change or system change has touched since its evidence was dated. Age alone does not make a row stale. Each decision role whose occupant, budget or mandate has changed. |
| **Fit drift** | The fit moves as either side changes | Each divergent step opened since the last review, whose change opened it, and whether notice came first. Each row marked as surfacing in use that has now surfaced. |
| **Value** | Realized value falls short of realizable | The value reading in section 2.2 |

**Then record three readings against the last review.**

- **The policing rows, as counts:** rows stale, rows without evidence, and rows added. A fraction can move because rows were added. Report $f_{seller}$ and $f_{buyer}$ beside the counts only where one verdict cannot swing them ([07-open-questions.md](../theory/01-foundation/07-open-questions.md) item 57).
- **The bargaining gap:** the share of roles whose current occupant has not stated and received the answer.
- **The balance of what each side has sunk since signature.** Whichever side re-adapted to a divergence raised its own quasi-rent, whoever chose the divergence. The buyer stays bonded while $\omega Q_b \le (1-\omega)Q_s + F_s$: what the seller could take at a renegotiation stays below what forcing one would cost it ([02-mathematical-models.md](../theory/01-foundation/02-mathematical-models.md) section 5.5). A divergence that breaks the condition is a hold-up hazard, however it began.

### 2.2 The value reading

Three of the five [RE-AIM](../theory/02-research/re-aim-framework.md) dimensions. The other two, implementation fidelity and maintenance, are the fit-drift and stale-evidence readings above.

| Dimension | Reads | Evidence |
|---|---|---|
| **Reach** | Whether the people the deal was for use it | Provisioned against active |
| **Adoption** | Whether use reaches the steps that carry the value | The value-carrying steps in real use |
| **Effectiveness** | Movement on the signed outcome measure, in the buyer's numbers | Baseline, current, and the number the gate reads |

**The order they fail in names the intervention.** Reach red is a stalled deployment, and the resource rows are the lever. Reach green and Adoption red is shallow use, a workflow and training problem. Adoption green and Effectiveness red means the measure or the value case was wrong at signature, which only both sponsors can re-scope.

### 2.3 What each finding can invoke

Each finding invokes a right agreed in Stage. A finding with no right to invoke is an allocation Stage missed: settle it before any work on it begins, or raise it at renewal.

| Finding | Right either side can invoke | Who pays |
|---|---|---|
| A row's evidence has gone stale | Re-verification of the row before the next gate or renewal | The party whose half of the gap the row closes: the seller for its Map evidence, with the buyer giving access, and the buyer for re-checking what the seller showed in Test |
| A new divergence | The change process agreed in Stage, at its rate card | Whoever the process names. Where Stage agreed notice and the change came without it, the party that changed. A change neither side made, such as a regulation or an upstream vendor's, splits evenly unless the process says otherwise. |
| The outcome measure missed at a gate | The gate's consequence | Credits if the seller's execution missed, the stop price if the buyer stops for another reason |
| The balance breaks the bond condition | The step-up agreed in Stage: a hostage or a renewal-price cap that takes effect at that point | As agreed |

### 2.4 How it runs

- **Two meetings.** A working review, of the row owners on each side and the account manager, covers sections 2.1 and 2.3 on the cycle below, in a meeting or in writing. A sponsor review, half an hour with both sponsors, hears only the value reading and the findings that invoked a right. The seller names its own misses first in both.
- **Roles, one to one.** Re-read a role whose direction reads −1 when its occupant changes, when a finding touches the term that answered it, and once before renewal. A new occupant states their reservation before the next review, and the term written against the role carries to them. A dissolved mandate re-maps the coalition in the Bargaining Ledger. Neither meeting hears a reservation, only the arrangement.
- **Cadence.** The first working review sits at the first gate after go-live, then on the cycle agreed in Stage, quarterly by default. Shorten it when a review finds a divergence that came without notice or a stale row that failed re-verification, and only while the renewal margin covers the extra reviews. Where findings keep outrunning the cycle, lower the rate instead: stability and deprecation commitments on the seller's side, configuration the buyer owns on the other ([02-mathematical-models.md](../theory/01-foundation/02-mathematical-models.md) section 5.3). Lengthen it after two reviews in a row find neither. Count findings from the change logs and the triggers below, not from the account manager's report.
- **Out of cycle.** Any of these calls a working review before its date: the champion or sponsor leaves or changes role, the sponsor misses two sponsor reviews in a row, use falls, support requests rise, the buyer stops asking for anything, the buyer evaluates a challenger mid-term, or either side announces a change that touches a mapped row.
- **Code each finding by cause the day it is found,** from the dated change logs: stale evidence, fit drift and whose change, hold-up in plain view (one side forcing a renegotiation or refusing to adapt where it could), value the offer cannot deliver here, or an event outside the relationship dated in a public record: the buyer's own failure, a budget cut across its market, an acquirer replacing the product, a failed payment. A divergence a change preceded is fit drift, and stale applies only where no divergence was found. The owner on each side signs each code, and a code they dispute is recorded as disputed. A churn or contraction with no coded finding before it is recorded as uncoded and is never assigned a cause after the fact ([07-open-questions.md](../theory/01-foundation/07-open-questions.md) item 51).

---

## 3. Renewal

**Start it** the length of a remediation under new gates, plus the procurement lead time the Bargaining Ledger recorded, before the date.

**The forecast call.** At risk if any of these holds: Effectiveness red, Reach or Adoption falling across two reviews, scope or licenses reduced, the bargaining gap open at a role that can veto the renewal, or a challenger evaluated. Otherwise forecast on the posture below. Never sum the readings into a health score, for the reason the triage never sums the costs.

**The evidence pack.**

- [ ] **The review record across the term,** read as a trend.
- [ ] **The outcome measure** against the number signed in Stage, with the variance stated plainly.
- [ ] **The commitments** each side made and delivered.
- [ ] **The risks that materialized,** and which of them the seller named in Test.
- [ ] **The rows a challenger would have to map** that this seller has already evidenced.

**The buyer's alternatives.** Record a challenger it has evaluated, its own team on the adjacent function, and its own build estimate where it has one. Past the bond condition, price at or under what those alternatives allow and offer a cap on the renewal price. Taking more teaches the buyer to build ([05-governance-forms.md](../theory/01-foundation/05-governance-forms.md) section 3).

**Posture.**

- **Outcome met, commitments met both ways.** Renew, true up on Reach, and price within the buyer's alternatives where it is past the bond condition.
- **Mixed.** Renew flat, with a remediation gate the seller's own disclosure scopes.
- **Outcome missed.** Do not discount to cover it. Propose a remediation under new gates, built by the Enforcement Ledger's four rules, or let the account lapse in writing.

**Expansion.** Scope that reaches the same roles and steps opens only from a met outcome measure. Scope that reaches a new budget owner or new steps is a new deal: run it through the Deal Triage Calculator and add its roles to the Bargaining Ledger ([07-open-questions.md](../theory/01-foundation/07-open-questions.md) item 47).

---

## Review record

| Field | Value |
|---|---|
| Depth: full, pooled, or at renewal only, and the hours against the margin | |
| Handoff: date, received by, transfer test passed (yes / no) and graded by | |
| Review: working or sponsor, in cycle or called out of cycle and by what | |
| Rows stale, rows without evidence, rows added; $f_{seller}$ and $f_{buyer}$ where they can be read | |
| Roles re-read, and the bargaining gap | |
| Balance since signature, and any step-up taken | |
| Reach, Adoption, Effectiveness, and the pattern | |
| Findings: cause, signed or disputed, and the right invoked | |
| Next review date, and why the cycle moved | |
| Renewal: forecast call, evidence pack, the buyer's alternatives, posture | |
| Counts re-taken at renewal, sent to the triage's audit | |
| Date, and by whom | |

---

## Related

- **Theory:** [05-governance-forms.md](../theory/01-foundation/05-governance-forms.md) sections 1, 3 and 5.
- **The repeated game:** [04-seller-surplus-model.md](../theory/01-foundation/04-seller-surplus-model.md) section 7.
- **Research:** [re-aim-framework.md](../theory/02-research/re-aim-framework.md), [game-theory-and-nrr.md](../theory/02-research/game-theory-and-nrr.md), [incomplete-contracts.md](../theory/02-research/incomplete-contracts.md).
- **Before it:** the [Enforcement Ledger](./enforcement-ledger.md) and the [Bargaining Ledger](./bargaining-ledger.md). **Beside it:** the [Deal Triage Calculator](./deal-triage-calculator.md)'s count audit.
