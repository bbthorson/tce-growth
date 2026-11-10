---
title: "The Enforcement Ledger"
layer: practice
status: active
version: 1.0
operationalizes: [axiom-2, axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# The Enforcement Ledger

Version: 1.0
Goal: On one deal, close the policing gap from both sides and settle the allocation before anything specific is sunk. One ledger, one row per workflow step, shared in full with the buyer. It grows a column at each of three stages: **Map**, which the field calls the Blueprint, **Test**, the Red Team, and **Stage**, the Mutual Implementation Plan. Maintain runs after signature in the [Sustaining Adoption Review](./adoption-review.md).

**Canonical reference:** [Constitution 6.1](../theory/01-foundation/00-tcg-constitution.md), Axiom III: specificity, who cannot check what, contracting what can be foreseen, enforcement, staged commitment and the gate. Axiom II for discovery as spending that lowers the cost at Time2.

| | |
|---|---|
| **Inputs** | A [Deal Triage Calculator](./deal-triage-calculator.md) reading of a built-in purchase, or a pilot request. The workflow from the [Market Reading](./00-market-reading.md), Step 1. |
| **Outputs** | The ledger, the policing gap by half and the stage it sends the deal to, signed gates, and the allocation coverage at go-live. |
| **Next step** | The [Sustaining Adoption Review](./adoption-review.md), which runs Maintain and the standing review agreed in Stage. |
| **Owner** | The account executive and solutions engineer, with the buyer's technical lead. The buyer's skeptic judges Test. |

> [!IMPORTANT]
> **The ledger is the buyer's as much as the seller's,** and a buyer column the seller filled alone is a map of the seller's guesses. The empty cells are the seller's ignorance shown rather than hidden. What the change does to a person's budget, headcount or standing does not go here. It belongs in the private decision-role map of the [Bargaining Ledger](./bargaining-ledger.md), which this ledger's rows seed.

**Do not run it on a plug-in purchase.** A *plug-in* purchase works on arrival, and a *built-in* one has either side build something that is worth less anywhere else. Where the triage's three plug-in tests hold, the buyer verifies by trying, and running this ledger is the over-built failure.

---

## The deal record

Three entries above the rows, written before Map and carried to the Adoption Review:

- **The economic event:** the trigger, dated, and the cost of inaction sized in the buyer's own words. If the seller said it to the buyer, it is not evidenced.
- **The named roles:** the sponsor, the champion, and the skeptic who judges Test, named before Test: the person whose own work or budget the integration lands on. Names only. What the change does to each of them belongs in the [Bargaining Ledger](./bargaining-ledger.md).
- **The declared limits** (below).

## The rows

Start from the reference workflow, one row per step, with the columns the seller writes once before any deal: the step, its touchpoint type, the role that performs it, the system it touches, and the data it moves. Append a row for each integration point, procedure or exception path this buyer has that the reference does not, and a **resource row** for each commitment the buyer must make: the people, their hours and the owner.

**Declare the limits first.** Before Map, the seller writes what the product cannot do in an environment like this one, specifically enough that the buyer can test it. Each limit flags the rows it touches.

---

## Stage 1: Map (the Blueprint)

**Closes the seller's half:** what the seller does not know about the buyer's environment.

| Column | Filled with |
|---|---|
| Buyer's version | Matches, diverges or missing, against the reference step |
| Exception paths | Each branch with no written handling, with its volume |
| System | The system and its schema |
| Evidence | A schema, an API document, a procedure with volumes, or a security policy. A verbal assurance is not evidence. |

**The buyer invests first.** Before Test, the buyer supplies a current-state map of the workflow and a data sample, de-identified or under a paid discovery agreement. A buyer that will not invest in Map will not invest in Stage, so the deal pauses until it does.

**Previous attempts.** If the buyer has tried to solve this before, record why it failed: the technology, the people, or the budget.

**What Map cannot reach.** Misfits in roles, controls and culture surface only in use. Leave those rows marked "surfaces in use" rather than guessing, and the Adoption Review fills them.

**Done when** every row carries the buyer's version with evidence, or is marked as surfacing in use.

---

## Stage 2: Test (the Red Team)

**Closes the buyer's half:** what the buyer does not know about the seller's capability in its environment.

**Find the failures.** Collect each attendee's failure list in writing before the session, because a room suppresses what only one member knows. Then run the pre-mortem with the champion and the skeptic, who must attend. Assume the project failed a year from now and walk five ways it failed, the RE-AIM dimensions inverted ([implementation-science.md](../theory/02-research/implementation-science.md)): nobody knew it existed, a group refused it, the integration broke, it delivered no measurable value, and use decayed. Attach each failure to its row, or add a row.

| Column | Filled with |
|---|---|
| Scenario | What was run against the divergence or limit, in the buyer's environment, at the seller's cost |
| Result | What happened |
| Verdict | The skeptic's: resolved, mitigated with evidence that the mitigation works, or a product limit acknowledged in writing |

**Evidence counts only if it passes the [Friction Allocation Diagnostic](./friction-allocation-diagnostic.md).** A sales claim nobody challenged counts against, and a matching row needs the skeptic's confirmation that the product handles it as the buyer assumed.

**Classify what is not resolved.**

| Status | Meaning | Action |
|---|---|---|
| **Solvable** | Standard friction with a known remedy | Goes to Stage with an owner |
| **Constraint** | A real barrier with a workaround | Goes to Stage with an owner on one side and a date |
| **Showstopper** | A fundamental incompatibility | Pause the commercial discussion. Investigate, and if it cannot be solved, propose only the scope that excludes it, or nothing. |

**Done when** every row carries the skeptic's verdict.

---

## The policing gap: which stage next

The gap has two halves, read from the ledger itself.

$$f_{seller} = \frac{\text{rows without Map evidence}}{\text{rows in scope}} \qquad f_{buyer} = \frac{\text{rows without the skeptic's verdict}}{\text{rows in scope}}$$

$$\hat{\Delta}_{implementation} = \frac{f_{seller} + f_{buyer}}{2}$$

Both halves run over the same rows, so the seller cannot shrink the buyer's half by classifying generously. Rows marked as surfacing in use stay out of both, are reported as a share beside the gap, and go to Stage with a risk carrier and a change process. The buyer half is the starting uncertainty $x_0$ for the buyer's staging, and the seller half feeds the seller's loss.

**The balance says which stage is next.**

| Reading | Next |
|---|---|
| $f_{seller}$ exceeds $f_{buyer}$ by 0.25 or more | Back to Map. A Test run on an unmapped environment surfaces the seller's ignorance, not the buyer's risk. |
| $f_{buyer}$ exceeds $f_{seller}$ by 0.25 or more | Back to Test. The buyer is working from an imagined product, and pricing into that produces a signature followed by churn. |
| Within 0.25 of each other and both high | The most dangerous state: both sides are guessing. Map, then Test, before any forecast. |

**The level says how far to go before terms.**

| $\hat{\Delta}_{implementation}$ | Reading | Action |
|---|---|---|
| 0.25 or below | Low | Proceed to Stage. |
| Above 0.25, up to 0.625 | Moderate | Hold final pricing until the system and resource rows are evidenced. |
| Above 0.625 | High | Commercial hold. No terms until Map and Test have run again. |

**A writeback row without Map evidence holds the level at Moderate or above,** whatever the fraction, because one unmapped write into the buyer's record outweighs any number of evidenced setup rows. The edges are chosen and unmeasured.

---

## Stage 3: Stage (the Mutual Implementation Plan)

**Contracts what can be foreseen, before anything specific is sunk.** For every row not resolved in Test:

| Column | Filled with |
|---|---|
| Action | What retires the risk |
| Owners | One on each side |
| Date | When |
| Gate | The contract gate the row sits behind |
| Risk carried by | Which party bears the row's adaptation risk |
| Right to stop | What either side can do at that gate, and at what price |

**Design the gates by four rules.** [02-mathematical-models.md](../theory/01-foundation/02-mathematical-models.md) section 5.4 has the arithmetic.

1. **Low commitment before validation.** The first gate is the minimum viable integration: the smallest set of touchpoints that lets the buyer verify value. The buyer must be able to exit it having spent what it would not need to defend.
2. **Payment follows proof, not the calendar.** Payments trigger on sign-off against written acceptance criteria, and each criterion must be able to fail, or the gate resolves nothing. A date-triggered payment turns the right to stop back into a commitment. Book it the same way: the representative's credit vests at the gate, or no representative will propose it.
3. **Symmetric consequence.** If a gate fails on the seller's execution, unused fees are credited and remediation is not billed. If the buyer stops for any other reason, or withholds sign-off on criteria that were met, it pays the stop price, set to cover what the seller has sunk and cannot redeploy. Map and Test run at the seller's cost, so without a stop price the buyer holds a free exit from the seller's sunk investment, which is the one-sided exit the Constitution's governance corollary forbids.
4. **Small commitments early, large ones late.** Walk the gates in order and check that committed payment to date never exceeds value realized to date.

**Where one side sinks far more than the other, add a hostage or an allocated right.**
- On the buyer's side, a hostage is something the buyer loses if it stalls, such as a committed fee forfeited or a stop price owed, triggered by a dated buyer deliverable missed rather than by a finding of fault.
- On the seller's side, it is credits or a clawback if the agreed outcome is missed through the seller's failure.
- An allocated right fixes in advance a renewal price, a price to stop, or who owns the integration and the data.

**One outcome measure** both sides sign, which the last gate's acceptance criteria read.

**Go or no-go.** Launch only when the integration has passed its Test scenario, the agreed share of users is trained, and the executive sponsor has signed off.

**The standing review.** Agree it here, before anything is sunk, as the [Sustaining Adoption Review](./adoption-review.md) runs it: the cycle, notice of change (the seller's releases keyed to the touchpoints they touch, and the buyer's changes where it will commit to notice), a change process with a rate card, who re-verifies a stale row, and a step-up, a hostage or renewal-price cap that takes effect if the balance of what each side has sunk breaks the bond condition.

**Done when** every row matches the reference or carries a gated mitigation with an owner on each side.

---

## Allocation coverage

$$\text{ACR} = \frac{n_{allocated}}{n_{exposure}}$$

$n_{exposure}$ counts what either side sinks that only works here: the buyer's divergent steps, integration points and changed workflows after Test, and the seller's own specific build for this buyer. $n_{allocated}$ counts the items whose work began only after a signed Stage row covered them. **An item is covered when its row names all three:** who carries its adaptation risk, the gate it sits behind, and a right to stop priced below what continuing would cost the party holding it. Read it at go-live, with each allocation dated by its signed row.

**Read it against the share the deal needed.** The share settled in advance rises with the imbalance between what the two sides sink ([02-mathematical-models.md](../theory/01-foundation/02-mathematical-models.md) section 5.6). Below that share is the unallocated failure. Well above it on a deal where both sink evenly is the over-frictioned one. It is undefined where nothing specific was sunk.

---

## Scoring sheet

| Field | Value |
|---|---|
| Triage reading that opened the ledger, and its date | |
| Declared limits | |
| Economic event, dated and sized; sponsor, champion and skeptic named | |
| Rows in scope, including resource rows; rows surfacing in use | |
| Buyer's current-state map and data sample received (yes / no) | |
| Previous attempts, and why they failed | |
| $f_{seller}$, $f_{buyer}$, $\hat{\Delta}_{implementation}$, and the stage it sends the deal to | |
| Showstoppers, and what was done | |
| Gates, each with acceptance criteria, payment and right to stop | |
| Hostages and allocated rights | |
| Outcome measure | |
| Standing review: cadence and what each side can invoke | |
| Allocation coverage at go-live | |
| Date, and by whom | |

---

## Related

- **Theory:** [Constitution](../theory/01-foundation/00-tcg-constitution.md), Axiom III. Claim 12 states the staged plan this ledger builds.
- **Functional forms:** [02-mathematical-models.md](../theory/01-foundation/02-mathematical-models.md) sections 2, 5.2 and 5.4.
- **Research:** [costly-signals.md](../theory/02-research/costly-signals.md), [implementation-science.md](../theory/02-research/implementation-science.md), [fear-of-failure.md](../theory/02-research/fear-of-failure.md), [incomplete-contracts.md](../theory/02-research/incomplete-contracts.md).
- **Before it:** [Deal Triage Calculator](./deal-triage-calculator.md). **After it:** [Sustaining Adoption Review](./adoption-review.md).
