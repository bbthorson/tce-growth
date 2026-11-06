---
title: "The Deal Triage Calculator"
layer: practice
status: active
version: 9.0
operationalizes: [axiom-1, axiom-2, axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# The Deal Triage Calculator

Version: 9.0
Goal: Read one deal against the Constitution's three questions, in order. Can this buyer enter? What has to be paid down at time 0, and what must the seller's spending do? What has to be settled before anything is sunk, so time 1 does not decay? This is the deal reading that [08-from-axioms-to-instruments.md](../theory/01-foundation/08-from-axioms-to-instruments.md) section 2.2 derives. It varies around [the Market Reading](./00-market-reading.md), which is read first.

**Canonical reference:** [Constitution 6.1](../theory/01-foundation/00-tcg-constitution.md). Axiom I for the positions and the buyer's expected reading, Axiom II for where the sale starts and what seller spending buys, Axiom III for the exposure, the gate, the governance form and the standing review. The functional forms are [02-mathematical-models.md](../theory/01-foundation/02-mathematical-models.md) section 6. The motions are [01-motions.md](../theory/01-foundation/01-motions.md).

| | |
|---|---|
| **Inputs** | A live deal, its market reading, and a willingness to count things rather than rate them. |
| **Outputs** | Each cost's position as measured and as the buyer expects it, where the sale starts, the mandate, the job the seller's spending must do, a specific-exposure reading, a frequency, a governance form with what to contract and what to review, and a routing. |
| **Next step** | See Step 4. |
| **Owner** | The account executive or pre-sales lead, with a spot-check on the counts by someone who does not carry the deal. |

> [!IMPORTANT]
> **This instrument counts. It does not rate.** Every input is a number of named things, backed by a list. A number with no list attached is not a count. Counts have a true zero and equal intervals, and each is read against two edges of its own, so the counts are never converted to scores or summed. A count can still be gamed, but a disputed count is an argument about a named item on a list, and the [Adoption Review](./implementation-motion/04-sustaining-adoption-review.md) re-takes every count. The edges are chosen, so read positions as comparisons between deals in one book ([06-calibration.md](../theory/01-foundation/06-calibration.md)).

---

## Step 0: Before the deal

**0a. The market reading.** Name the market reading this deal sits under and its verdict. A deal in a market the seller declined, or never read, is one the seller has not decided it can afford, so every routing below is provisional. A book of deal readings that disagrees with its market reading is the evidence the market reading is wrong.

**0b. Workflow maturity.** Classify the buyer's workflow for the problem being solved. A count of exception paths means nothing when no path is written down.

| Level | Condition | Evidence | Route |
|---|---|---|---|
| **1. Undefined** | No written process. Steps vary by person. | Ask three people to describe the workflow and get three different answers. | **Stop, the Chaos Trap**, if the product automates the process. Redirect to consulting or a paid workshop to define it. If the product supplies a medium the buyer encodes its own workflow into, an undefined workflow is not a trap. See Gate A. |
| **2. Emergent** | A process exists and is partly written down, but units have diverged and nobody owns the variance. | A written procedure people describe as out of date. | **Conditional.** Continue, but the Blueprint must reconstruct the workflow before the Red Team runs. |
| **3. Codified** | Documented, followed, and exception handling is quantified. | The current procedure, plus volumes for the exception paths. | **Continue.** |

**Level 2 is the level that gets misread.** A buyer at Level 2 can produce a document on request, which reads as Level 3 to anyone who does not check whether it matches practice. The failure surfaces during implementation as unmapped exception paths, the most common source of scope expansion after signature. When in doubt, score down.

---

## Step 1: Can this buyer enter? (Axiom I)

Count each cost twice. The **measured** count $n_k$ is what discovery establishes. The **expected** count $\tilde{n}_k$ is what the buyer says, before discovery, it thinks the cost will take: which vendors it must compare, who must sign, what must integrate. The buyer decides on the expected count. Both are read against the same two edges: below the self-serve edge the buyer pays the cost down alone, and above the participation edge it cannot get through it at any price. [06-calibration.md](../theory/01-foundation/06-calibration.md) section 3.2 records every edge as chosen.

### 1a. Search

**Count: alternatives the buyer must rule out before it can choose.** Every named vendor, plus "build it internally" as one, plus "do nothing" as one.

$$n_{search} = (\text{named vendors}) + (\text{build}) + (\text{do nothing})$$

| Edge | $n_{search}$ |
|---|---|
| Self-serve, $\tau^{self}$ | 4 |
| Participation, $\tau^{part}$ | 8 |

> [!WARNING]
> **A buyer who cannot name the category is not a short list. It is kept out.** Its alternative set is unbounded, because it cannot enumerate what it is choosing between. The route is category definition. **A buyer you hold no path to today is kept out too**, however well it knows the category, and neither education nor a trial touches that cost. Pull it back into range with a channel, or decline. [channel-collapse.md](../theory/02-research/channel-collapse.md) carries the research.

### 1b. Bargaining and decision (consensus)

**Count: decision roles that can say no.** Not people who attend. Roles whose objection stops the purchase. Add one for each formal body the buyer's rules require at this deal's size and exposure: a procurement process, a security review, a board.

$$n_{consensus} = (\text{decision roles with a veto}) + (\text{formal bodies required})$$

| Edge | $n_{consensus}$ |
|---|---|
| Self-serve, $\tau^{self}$ | 1 |
| Participation, $\tau^{part}$ | 7 |

**Record the spend thresholds.** For each formal body, note the contract value above which the buyer's rules require it. Price sets who must approve, so a deal split or ramped under a threshold drops that body from the count. It does not settle the exposure of the role behind the body, which returns at renewal under Axiom III. Record any such restructuring as an open row in the decision-role map.

### 1c. Policing and enforcement (implementation)

**Count: three things, summed.**

$$n_{impl} = (\text{integration points}) + (\text{workflows that change}) + (\text{undocumented exception paths})$$

An integration point is one system that must exchange data with yours. A workflow that changes is one procedure a named group performs differently after go-live. An undocumented exception path is one branch of the workflow with no written handling and no volume attached.

| Edge | $n_{impl}$ |
|---|---|
| Self-serve, $\tau^{self}$ | 2 |
| Participation, $\tau^{part}$ | 11 |

### 1d. Positions

For each cost, its position between its own two edges, once on each count:

$$r_k = \frac{n_k - \tau^{self}_k}{\tau^{part}_k - \tau^{self}_k} \qquad \tilde{r}_k = \frac{\tilde{n}_k - \tau^{self}_k}{\tau^{part}_k - \tau^{self}_k}$$

| Position | Zone |
|---|---|
| $\le 0$ | **Self-serve.** The buyer pays this cost down alone. |
| above zero and at most one | **Needs investment.** Bearable, with what the seller absorbs. |
| $> 1$ | **Keeps the buyer out.** |

**Read the two together.**

| Measured | Expected | Reading | Route |
|---|---|---|---|
| At most one | At most one | **Can enter** | Continue to Step 2. |
| At most one | Above one | **Unshown.** The cost is within reach and the buyer does not believe it. | Show the cost with evidence the buyer can check, such as published terms, a security packet or an implementation timeline with references. That is the second job of seller spending under Step 2. |
| Above one | Any | **Kept out.** | Pull it back into range with the instrument for that cost, invest across deals if its cost floor holds it there, or decline. No work on the other two costs reaches it. |

An unnamed category or a missing channel puts search in the third row whatever the count. The positions are never summed, and ease on one cost never buys back another above its edge.

---

## Step 2: What has to be paid down at time 0? (Axiom II)

### 2a. Where the sale starts

**The cost with the largest expected position before the buyer has entered discovery, and the largest measured position after.** Two costs at the same position are run together, and the instrument returns both. Date every reading and say what had been verified when it was taken. Until fit is verified on the buyer's own workflow, the policing and bargaining counts are lower bounds. Keep every old reading, because a reading written after the outcome cannot test the sequencing falsifier.

**The gaps are not read here.** They change no output of this instrument. They are filled during discovery and drive the plan: [08-from-axioms-to-instruments.md](../theory/01-foundation/08-from-axioms-to-instruments.md) section 2.2 defines each, the decision-role map reads the bargaining gap, and the [Enforcement Ledger](./enforcement-ledger.md) reads the policing gap.

### 2b. The mandate

**Is there a named executive sponsor, and is capital allocated to this initiative?** Read it apart from the decision roles and re-read it at every occupant change. A mandate that dissolves overrides every role, and its loss usually arrives looking like one person's departure. No mandate routes the deal to the previous-attempts check in the [Enforcement Ledger](./enforcement-ledger.md)'s Map stage before any other investment.

### 2c. What the seller's spending must do, and who pays

Seller spending on the cost where the sale starts earns its cost by one of two jobs. Where that cost is Unshown, the job is to let a deal that creates value go ahead: show the cost with evidence the buyer can check. Otherwise the job is to raise what the deal creates, by doing the work more cheaply than the buyer could or by lowering what the relationship will cost at time 1, as discovery does. A discount or quarter-end pressure does neither. Which investment does which job is the plan's to record ([07-open-questions.md](../theory/01-foundation/07-open-questions.md) item 45).

**The seller's share.** Can what this relationship pays, the first contract, renewal and expansion, or the deals it unlocks, recover the seller's planned investment? Name which one repays it. Spending that nothing repays is a price cut.

**The buyer's share.** What is the buyer being asked to invest against each cost, in people and time, and does it have them? A plan that assigns work to staff the buyer does not have fails Axiom II on the buyer's side, whatever the price.

Where either share is not covered, move work to the party that does it more cheaply or whose doing it lowers a future loss, restructure, or decline.

---

## Step 3: What has to be settled before anything is sunk? (Axiom III)

### 3a. Specific exposure

**Gate A: must the product fit a workflow the buyer has already encoded?**

| Answer | Condition | Route |
|---|---|---|
| **No, greenfield** | No encoded workflow exists for this problem. The product creates the practice. | Do not count divergence. It has no reference point. |
| **No, the product absorbs it** | The product ships underspecified on purpose, and the buyer encodes its own workflow inside it without vendor engineering. | Do not count divergence. |
| **Yes** | The buyer runs an encoded workflow the product must fit, extend or replace. | Count divergence if Gate B fails. |

**Gate B: can the buyer measure the gap itself, and reverse the decision?** This is the Constitution's gate, and CFIR's Trialability construct. All three must hold:

- The buyer can run the product against its real work, with its real data, without seller engineering.
- Discovering a bad fit costs it days rather than quarters.
- Walking away strands no committed spend and no migrated data.

If all three hold, nothing specific is sunk and the exposure reading is none. Otherwise count what the deal sinks that only works here:

$$n_{exposure} = (\text{integration points}) + (\text{workflows that change}) + (\text{divergent steps})$$

Integration points and changed workflows are the Step 1c counts. Divergent steps are counted only when Gate A answers yes: walk the buyer's procedure and mark each step the product cannot perform as written ([process-misfit.md](../theory/02-research/process-misfit.md)).

| Reading | Condition |
|---|---|
| **None** | Gate B passes, or $n_{exposure} = 0$ |
| **Specific** | Gate B fails and $n_{exposure} > 0$ |

**Who sinks first.** Record which party sinks its specific investment first. Where the seller does, as with forward-deployed engineering before signature, the seller is the exposed party and the allocation has to be settled before the seller spends.

**Who codified the workflow predicts the count.** A regulator's codification converges across buyers, and a buyer's own diverges. A demonstration reaches functionality and data misfits, and misfits in roles, controls and culture surface only in use.

### 3b. Frequency

**A classification, not a count.** How often the same two parties transact. With the exposure reading it selects the governance form.

| Reading | Condition | Evidence |
|---|---|---|
| **One-shot** | The transaction completes and neither party has a structural reason to meet again. | No renewal date exists, and nobody on either side can name what a second purchase would be. |
| **Recurrent** | The transaction renews on a cycle and either party can decline at the boundary. | A renewal date, and a named owner of it on each side. |
| **Continuous** | The product sits inside the buyer's operations and leaving is itself a project. | Ask what migrating away would cost. If nobody can answer, it is continuous. |

**Do not read your own pricing model as the answer.** A product billed annually that the buyer treats as a one-time installation with a maintenance fee is one-shot.

### 3c. What to contract, and what to review

Read the governance form off the exposure and the frequency together ([05-governance-forms.md](../theory/01-foundation/05-governance-forms.md)).

| Exposure | Frequency | Form | What to contract |
|---|---|---|---|
| None | Any | **Market** | Standard terms, published pricing, no relationship apparatus. |
| Specific | One-shot | **Trilateral** | Safeguards from outside the pair: fixed scope, external acceptance criteria, escrow or arbitration, a named third party who adjudicates. |
| Specific | Recurrent | **Bilateral** | A [Mutual Implementation Plan](./enforcement-ledger.md): staged gates with a priced right to stop at each, who carries which adaptation risk, and what each side loses by walking away. |
| Specific | Continuous | **Bilateral, watching for unified** | The Mutual Implementation Plan, plus a reading of what the buyer's build alternative now costs, because rising specificity eventually makes integrating beat any contract. |

Where one side sinks far more than the other, contract a hostage, such as fees staged against delivery, or an allocated right, such as an option to renew at a preset price or who owns the integration and the data. For any specific exposure, agree the standing review before anything is sunk, with what each side can invoke from it: a re-scoping, a change process, a right to stop. A review with nothing to invoke is a meeting ([07-open-questions.md](../theory/01-foundation/07-open-questions.md) item 46).

> [!WARNING]
> **A specific one-shot deal is the case to escalate.** Something will be sunk and there is nothing to amortize the seller's investment over. Do not run a lighter version of the motion, which produces the unallocated failure with the cost already sunk. Find a structure that makes the relationship recurrent, which changes the governance form, or decline.

---

## Step 4: Route

**Overrides first.**

| Condition | Route |
|---|---|
| Step 0b returned the Chaos Trap | Stop. Consulting or a paid definition workshop. |
| Any cost is Kept out in Step 1d | Name it. Pull it back into range, invest across deals if its floor holds it, or decline. |
| Any cost is Unshown in Step 1d | Show it first, with evidence the buyer can check. Nothing else reaches a buyer that will not enter discovery. |
| A share in Step 2c that nothing covers | Move work to the party that does it more cheaply, restructure as recurrent, or decline. |
| The specification is externally fixed by a mandate or a rigid request for proposal | Compete on unit economics, service levels and delivery credibility. Discovery has nothing left to win. |
| The seller lacks the delivery depth the motion needs | Stop the motion until the capability is real. A Red Team run without it produces false confidence. |
| The buyer asked for a pilot or proof of concept | Implementation-led, whatever was counted. A buyer requesting a pilot is reporting that it expects a policing cost it cannot verify alone. Pilots run under the [Red Team Protocol](./enforcement-ledger.md). |

**Then the two readings.**

| | Exposure: none | Exposure: specific |
|---|---|---|
| **Every cost self-serve** | **Turnkey.** Standard terms, published pricing, self-service provisioning. | **Light sale, heavy contract.** The sale is easy and the allocation is not. Settle Step 3c before the specific investment is sunk. |
| **Some cost needs investment** | **Heavy sale, light contract.** Run the motion where the sale starts, then standard terms hold. | **The motion where the sale starts, with governance.** Where the sale starts at implementation, this is the full chain. |

**The motion where the sale starts:**

| Sale starts at | Motion | Run |
|---|---|---|
| Search | **Search-led** | Category definition, commercial teaching, reference architectures, channel work. No instrument file in this repository. |
| Consensus | **Consensus-led** | The [Bargaining Ledger](./bargaining-ledger.md): each decision role's exposure mapped one to one, an arrangement each exposed role ratifies, and a safeguard inside the buyer. Do not substitute the Enforcement Ledger because it is the more familiar one. |
| Implementation | **Implementation-led** | The [Enforcement Ledger](./enforcement-ledger.md)'s Map, Test and Stage, then the [Adoption Review](./implementation-motion/04-sustaining-adoption-review.md). |
| A tie | Both, run together | Do not pick one and call it the motion. |

**Possible over-frictioning.** Implementation needs investment and the exposure reads none. Deep integration against a standard the vendor already builds to is expensive work, not uncertain work. Run the instruments that pay down today's cost and skip the governance apparatus.

---

## Scoring sheet

| Field | Value |
|---|---|
| Market reading, and its verdict | |
| Workflow maturity (1, 2, 3) | |
| Alternatives to rule out: measured, expected. Category named, channel exists today | |
| Search position and zone: measured, expected | |
| Decision roles that can say no, formal bodies and their spend thresholds | |
| Consensus position and zone: measured, expected | |
| Integration points, workflows that change, undocumented exception paths: measured, expected | |
| Implementation position and zone: measured, expected | |
| Step 1d reading per cost (can enter, Unshown, Kept out) | |
| **Where the sale starts**, dated, with what had been verified | |
| Mandate: sponsor named, capital allocated | |
| The job the seller's spending must do | |
| Seller's share repaid by (first contract, renewal, expansion, unlocked deals, nothing). Buyer's share staffed (yes / no) | |
| Gate A, Gate B, divergent steps | |
| **Exposure** (none / specific), with the count, and who sinks first | |
| Frequency | |
| Governance form, what is contracted, the review and what each side can invoke | |
| **Routing** | |
| Date counted, and by whom | |

Re-count at every artifact boundary and keep the old rows. A deal whose readings never change is a deal where nothing was learned.

---

## Related

- **Theory:** [Constitution](../theory/01-foundation/00-tcg-constitution.md). Axiom I for the positions, Axiom II for where the sale starts and what seller spending buys, Axiom III for the exposure, the gate, the governance forms and the standing review.
- **Derivation:** [08-from-axioms-to-instruments.md](../theory/01-foundation/08-from-axioms-to-instruments.md) section 2.2, and [01-motions.md](../theory/01-foundation/01-motions.md) for the motions.
- **Market level:** [The Market Reading](./00-market-reading.md), read before this one.
- **Functional forms:** [02-mathematical-models.md](../theory/01-foundation/02-mathematical-models.md) sections 2.4, 3.1 and 6 consume these counts.
- **Provenance:** [06-calibration.md](../theory/01-foundation/06-calibration.md) section 3.2 records every edge as chosen.
- **Policing gap:** the [Enforcement Ledger](./enforcement-ledger.md) reads both halves.
