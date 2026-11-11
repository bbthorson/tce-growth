---
title: "The Deal Triage Calculator"
layer: practice
status: active
version: 10.0
operationalizes: [axiom-1, axiom-2, axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# The Deal Triage Calculator

Version: 10.0
Goal: Read one deal at Time1, under its market reading. Five questions, in order. Does this buyer pay for the problem? Is its workflow settled? Is the purchase plug-in or built-in? Which cost is in the way? What must the seller's spending do? The answers route the deal to an instrument.

**Canonical reference:** [Constitution 7.0](../theory/01-foundation/00-tcg-constitution.md), claims 6 to 9, with claim 2 read on one buyer and claim 12 for what a built-in purchase settles before anyone builds. The Constitution's Part II asks the same questions of a stall, in the same order.

| | |
|---|---|
| **Inputs** | A live deal, its [market reading](./00-market-reading.md), and a willingness to count things rather than rate them. |
| **Outputs** | Whether the buyer pays for the problem and holds a mandate. How settled its workflow is. Plug-in or built-in, with what would be built and who builds first. The cost in the way, as discovery finds it and as the buyer expects it. What the seller's spending must do, and what repays it. A routing. |
| **Next step** | See Step 6. |
| **Owner** | The account executive or pre-sales lead, with a spot-check on the counts by someone who does not carry the deal. |

> [!IMPORTANT]
> **This instrument counts. It does not rate.** Every input is a number of named things, backed by a list. A number with no list attached is not a count. A count can still be gamed, but a disputed count is an argument about a named item on a list, and the [Adoption Review](./adoption-review.md) re-takes every count at renewal. The counts size the work and compare deals in one book. No line is drawn on a count, and counts for different costs are never added.

---

## Step 0: The market reading

Name the market reading this deal sits under, its verdict, and the cost it says is in the way. A deal in a market the seller declined, or never read, is one the seller has not decided it is built for, so every routing below is provisional. Note where this deal reads differently from its market. A book of deals that disagree with the market reading is the evidence the market reading is wrong.

---

## Step 1: Does this buyer pay for the problem?

Read this before any cost, and date it before the seller invests. A buyer that does not want the change looks like a buyer with a cost in the way, and no work on a cost moves it.

| Ask | List |
|---|---|
| What does the buyer pay for the problem today? | Staff hours on a workaround, an incumbent tool, a consultant, an internal build |
| What has the buyer put into this purchase that it will not get back? | A workflow map, a data sample, named staff time |

A buyer's statement that it wants the change is a claim until it costs the buyer something. A stall reads as a cost only where the first list is not empty. On a deal that has already stalled, the test is whether the buyer puts in more once the cost it named falls. A new objection alone shows nothing, because lowering one cost exposes the next.

**The mandate.** Is there a named executive sponsor, and is money allocated to this initiative? Read it apart from the decision roles, and re-read it whenever an occupant changes. A mandate that dissolves overrides every role, and its loss usually arrives looking like one person's departure.

This step is new and untested ([open question 66](../theory/01-foundation/07-open-questions.md)).

---

## Step 2: Is the workflow settled?

Classify the buyer's workflow for the problem being solved. A count of exception paths means nothing when no path is written down.

| Reading | Condition | Evidence | Route |
|---|---|---|---|
| **Not settled** | No written procedure. Steps vary by person. | Ask three people to describe the workflow and get three different answers. | **Teach.** The buyer cannot yet name what it is buying. Give it a hypothesis about its own workflow, or a paid workshop to define it. Proof of fit has nothing to run against. Where the product automates the process, pressing on is the *Chaos Trap*. Where the buyer writes its own workflow inside the product, an unsettled workflow is no trap. See Step 3. |
| **Partly settled** | A procedure is written down, units have diverged, and nobody owns the variance. | A written procedure people describe as out of date. | **Continue, on a condition.** The [Enforcement Ledger](./enforcement-ledger.md)'s Map stage reconstructs the workflow before its Test stage runs. |
| **Settled** | Written, followed, and the exceptions carry volumes. | The current procedure, plus volumes for the exception paths. | **Continue.** |

**Partly settled is the reading that gets misread.** A buyer there can produce a document on request, which reads as settled to anyone who does not check whether it matches practice. The failure surfaces during implementation as unmapped exception paths, the most common source of scope that grows after signature. When in doubt, read the workflow as less settled.

---

## Step 3: Plug-in or built-in?

A *plug-in* purchase works on arrival. A *built-in* purchase has the buyer, the seller or both build something that is worth less anywhere else. Claim 6 gives three tests, and all three must hold for a purchase to be plug-in.

- The buyer can run the product on its real work, with its real data, without the seller's engineers.
- Discovering a bad fit costs it days rather than quarters.
- Walking away strands no committed spend and no migrated data.

**All three hold: plug-in.** Standard terms and a trial. Discovery workshops and joint plans laid over a plug-in purchase lose the buyer to a lighter competitor. Go to Step 4 with implementation out of the way.

**Any one fails: built-in.** List what would be built.

| What is built | What to list |
|---|---|
| Integration points | Each system that must exchange data with the product |
| Workflows that change | Each procedure a named group performs differently after go-live |
| Divergent steps | Each step in the buyer's procedure that the product cannot perform as written |

**Is there a written workflow the product must fit?** Divergent steps are counted only where the answer is yes.

| Answer | Condition | Divergent steps |
|---|---|---|
| **No, the practice is new** | No workflow exists for this problem. The product creates the practice. | None to count. Nothing exists to diverge from. |
| **No, the buyer writes it inside the product** | The product ships open on purpose, and the buyer encodes its own workflow in it without the seller's engineers. | None to count. |
| **Yes** | The buyer runs a workflow the product must fit, extend or replace. | Walk the buyer's procedure and mark each step the product cannot perform as written ([process-misfit.md](../theory/02-research/process-misfit.md)). |

A demonstration reaches misfits in function and data. Misfits in roles, controls and culture surface only in use.

**Who builds first.** Record which party builds first. Whoever built more has more to lose (claim 11). Where the seller builds before signature, as with engineers placed in the deal, the seller is the exposed party, and the two sides settle who carries which risk before the seller spends.

---

## Step 4: Which cost is in the way?

Read each cost as in the way or not, backed by a count. Take each reading twice: what discovery finds, and what the buyer says before discovery it expects. The buyer decides on what it expects.

### Search

**In the way when** the buyer cannot name the category, the seller holds no path to this buyer, or the buyer cannot yet compare the alternatives it has named.

**Count:** the alternatives the buyer must rule out. Every named vendor, plus building it internally as one, plus doing nothing as one.

> [!WARNING]
> **A buyer who cannot name the category has no short list.** It cannot enumerate what it is choosing between, and the route is category definition. **A buyer the seller holds no path to is out of reach** however well it knows the category. Neither teaching nor a trial touches that cost. A channel does. [channel-collapse.md](../theory/02-research/channel-collapse.md) carries the research.

### Consensus

**In the way when** the buyer cannot buy alone: more than one role can say no, or the buyer's rules require a formal body at this price.

**Count:** the decision roles that can say no, plus one for each formal body the buyer's rules require at this deal's size, such as a procurement process, a security review or a board. A role counts when its objection stops the purchase. Attendance does not make one.

**Record the spend thresholds.** For each formal body, note the contract value above which the buyer's rules require it. A price taken under a threshold removes that approver, which is the one exception in claim 8. The role's concern returns at renewal, so record it as an open row in the [Bargaining Ledger](./bargaining-ledger.md)'s decision-role map.

### Implementation

**In the way when** the purchase is built-in. At Time1 implementation is a fear, and it acts through the buyer's own decision roles (claim 7).

**Count, to size the work:** integration points, plus workflows that change, plus undocumented exception paths. An undocumented exception path is one branch of the workflow with no written handling and no volume attached. Ask the technical owners about the integrations and the operating owners about the changed workflows, because different people carry each.

### What the buyer expects

| Discovery finds | The buyer expects | Reading |
|---|---|---|
| Not in the way | In the way | The buyer fears a cost it would not meet. Show the cost with evidence the buyer can check: published terms, a security packet, an implementation timeline with references. Nothing else reaches a buyer that will not enter discovery. |
| In the way | Not in the way | The buyer has not priced a cost it will meet. Say so before signature. Work skipped now moves to Time2 and grows (claim 9). |
| The two agree | | Continue. |

**The cost in the way** is what this step returns. Where two are in the way, the instrument returns both, and nothing here ranks them ([open question 67](../theory/01-foundation/07-open-questions.md)). Date every reading and say what had been verified when it was taken. Until fit is verified on the buyer's own workflow, the consensus and implementation counts are lower bounds. Keep every old reading, because a reading written after the outcome tests nothing.

---

## Step 5: What must the seller's spending do?

**The job.** Spending on the cost in the way earns its cost in one of two ways. It shows the buyer what it will face, or it does work the buyer would otherwise do at a higher cost. A discount and quarter-end pressure do neither, because price is a transfer (claim 8). Where the buyer's fear is the obstacle, offer a commitment the seller would not make if it expected to fail: capped overages, remediation hours written into the contract, a guarantee tied to the buyer's own environment. Trade it for what the buyer knows about that environment.

**Pull forward what this buyer needs, and no more.** Discovery skipped to close comes back at Time2 as scope changes. Engineering put into a deal that did not need it is charged to every buyer through the price (claim 9).

**What repays the seller.** Name what repays the seller's planned work: the first contract, renewal, expansion, or the deals this one unlocks. Spending that nothing repays is a price cut. A built-in purchase with no renewal behind it is the case to escalate, because something is built and nothing follows to repay it. Find a structure that renews, price the work, or decline. Do not read the seller's own pricing model as the answer. A product billed annually that the buyer treats as a one-time installation has no renewal.

**What the buyer must put in.** List the people and time the plan asks of the buyer against each cost, and check that it has them. A plan that assigns work to staff the buyer does not have fails whatever the price.

---

## Step 6: Route

**Overrides first.**

| Condition | Route |
|---|---|
| Step 1: the buyer pays nothing for the problem and has put nothing in | Stop spending on the deal. Ask the buyer to invest first, with a workflow map or a data sample. |
| Step 1: no mandate | Run the previous-attempts check in the [Enforcement Ledger](./enforcement-ledger.md)'s Map stage before any other investment. |
| Step 2: the workflow is not settled | Teach, or sell a workshop that defines it. |
| Step 4: the buyer expects a cost that discovery does not find | Show it first, with evidence the buyer can check. |
| Step 5: nothing repays the seller's work, or the buyer lacks the people | Move work to the party that does it more cheaply, restructure so the deal renews, or decline. |
| The specification is fixed from outside, by a mandate or a rigid request for proposal | Compete on unit economics, service levels and delivery credibility. Discovery has nothing left to win. |
| The buyer asked for a pilot or proof of concept | Read the purchase as built-in, whatever Step 3 returned. A buyer requesting a pilot is reporting that it expects an implementation cost it cannot check alone. Pilots run under the Enforcement Ledger's Test stage. |

**Then the motion, by the cost in the way.**

| Cost in the way | Motion | Run |
|---|---|---|
| None | None | Standard terms, published pricing and a trial. |
| Search | **Search-led** | Category definition, teaching, reference architectures and channel work, run from the [Market Reading](./00-market-reading.md)'s search ledger. |
| Consensus | **Consensus-led** | The [Bargaining Ledger](./bargaining-ledger.md): each decision role's concern collected one to one, an arrangement each role accepts, and a sponsor inside the buyer who holds the decision together. Do not substitute the Enforcement Ledger because it is the more familiar one. |
| Implementation | **Implementation-led** | The [Enforcement Ledger](./enforcement-ledger.md)'s Map, Test and Stage, then the [Adoption Review](./adoption-review.md). The Bargaining Ledger runs beside it. |
| Two at once | Both, run together | Do not pick one and call it the motion. |

**And the contract, by the kind of purchase.**

| Purchase | What to settle |
|---|---|
| Plug-in | Standard terms. No workshop, no joint plan and no relationship apparatus. |
| Built-in | Before either side builds, settle who carries which risk, in stages, with a point at each stage where either side can stop at a known price. Agree a standing review for what nobody can foresee, with what each side can invoke from it: a re-scoping, a change process, a right to stop. A review with nothing to invoke is a meeting. The Enforcement Ledger's Stage builds the plan (claim 12). |

---

## Auditing the counts

At each renewal of every recurring deal, plug-in purchases included, the [Adoption Review](./adoption-review.md) re-counts what this instrument counted: integration points, workflows that change, undocumented exception paths and divergent steps. Whoever owns the triage across the book records each beside the count taken here and the deal's outcome.

Read the variance across the book, never on one deal. A counter whose variance runs one way deal after deal has a counting problem, and the direction says which. Counting consistently under sends built-in purchases out as plug-in, and their renewals are where that shows. Counting consistently over lays apparatus on deals that did not need it. Lost deals and deals with no renewal are never re-counted, so the audit sees only deals that closed and renewed. It audits the counter. Whether the counts predict outcomes needs the outcome logged beside them.

---

## Record sheet

| Field | Value |
|---|---|
| Market reading, its verdict, and the cost it names | |
| What the buyer pays for the problem today. What it has put into this purchase | |
| Mandate: sponsor named, money allocated | |
| Workflow: not settled, partly settled or settled | |
| The three plug-in tests (yes / no each) | |
| **Plug-in or built-in** | |
| Integration points, workflows that change, divergent steps. A written workflow to fit (yes / no) | |
| Who builds first | |
| Search: category named, path held, alternatives to rule out. Found, and expected | |
| Consensus: roles that can say no, formal bodies and their spend thresholds. Found, and expected | |
| Implementation: integration points, workflows that change, undocumented exception paths. Found, and expected | |
| **The cost in the way**, dated, with what had been verified | |
| The job the seller's spending must do | |
| What repays the seller (first contract, renewal, expansion, unlocked deals, nothing). The buyer has the people (yes / no) | |
| What is settled before anyone builds, and what each side can invoke from the review | |
| **Routing** | |
| Date counted, and by whom | |

Re-count whenever the deal moves to a new instrument or stage, and keep the old rows. A deal whose readings never change is a deal where nothing was learned.

---

## Related

- **Theory:** [Constitution](../theory/01-foundation/00-tcg-constitution.md), claims 6 to 9 and claim 12, and [01-motions.md](../theory/01-foundation/01-motions.md) for the motions.
- **The market:** [The Market Reading](./00-market-reading.md), read before this one.
- **Where the routing sends a deal:** the [Bargaining Ledger](./bargaining-ledger.md), the [Enforcement Ledger](./enforcement-ledger.md) and the [Adoption Review](./adoption-review.md).
- **Misfit and trial:** [process-misfit.md](../theory/02-research/process-misfit.md), and [implementation-science.md](../theory/02-research/implementation-science.md) for the constructs Steps 2 and 3 read.
