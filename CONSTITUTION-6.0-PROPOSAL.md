# Constitution 6.0 Proposal

**Status:** Accepted 2026-11-06, with choices C1 to C5 taken as proposed. Being applied.
**Date:** 2026-11-05

This file follows the precedent of the 4.0 and 5.0 proposals: written at the root, reviewed, applied in steps, then retired to git history. Section 2 records the kernel agreed in review on 2026-11-05. Section 3 sorts every block of Constitution 5.2 against it.

---

## 1. Why revise

Constitution 5.2 runs to about 10,000 words, and its three axiom statements to 181. The gap grew one review at a time. Each review was answered by adding a clause, a corollary or a paragraph against an objection, so the length and the unclear passages have one cause. Corollaries now argue rather than follow: the cost floor corollary alone is 417 words and brings in four sources. The second standing assumption carries a theory of persuasion. And one idea, that a party acts on what it can check, is restated in four places under four names.

This revision starts from the essence and rebuilds down. The kernel in section 2 is the theory in about 600 words. Every block of 5.2 either says what the kernel says, follows from it in one step, needs a premise the kernel lacks, or repeats something said elsewhere. Section 3 makes that call for each block.

---

## 2. The kernel

> Buying costs more than the price. The buyer has to find a seller it trusts (search), get its own organization to agree (bargaining, the field's *consensus*), and make the product work in its own environment (policing, the field's *implementation*). The seller can absorb part of each cost. Sales is the seller absorbing them before the buyer commits, and account management is the seller absorbing them after. Each party acts on what it can check, so each cost has two readings: what it is, and what the buyer expects it to be.
>
> **I. Can a market exist?** Each side has a limit. A buyer enters only while every cost it expects to carry, after what the seller absorbs, sits below what it will bear. One cost above that keeps it out, and easing the other two does not bring it back. A seller enters only while its cost of sale, the cost of absorbing enough to bring buyers in, is repaid by what their contracts are worth over the relationship. A market exists only where both limits hold. Part of each cost is set outside any deal, by the information environment, the buyer's institutions and how verifiable delivery is. Where that part puts either side past its limit, no single seller's effort opens the market.
>
> **II. What has to be paid down at time 0?** Every buyer moves through the same stages. Moving through them is an investment the buyer makes against what it expects all three costs to be, including the ones it has not reached yet. So the cost it expects to sit nearest its limit decides whether it proceeds at all, even at awareness. The seller absorbs that one first, in fact and in what the buyer can see, so the buyer will invest in the work that lowers both sides' costs. That cost names the motion. Each party goes ahead only if its own share is covered by its own return. Seller spending makes the deal worth more to both in one of two ways: the seller does the work more cheaply than the buyer could, or the work lowers what the relationship will cost at time 1. Discovery is usually the second kind. It can cost more than the buyer would have spent, and it pays back in drift that never has to be fixed. Spending that does neither only moves cost from one side to the other, as a discount does. The seller recovers any of it only over the relationship, so without retention, sales spending is a price cut by another name.
>
> **III. What prevents churn and contraction at time 1?** Whatever a party sinks that pays off only in this relationship exposes it to what it cannot check or stop later. Left alone, that exposure shows up as churn, as contraction at renewal, or as a seller that stops delivering. So time 1 is decided at time 0, before either side sinks anything. What the parties can foresee, they contract for: who carries which exposure, staged how, and what each loses by walking away. What they cannot foresee, they plan for with a standing review, such as a quarterly business review, that catches drift between them before it shows up at renewal. Drift has two sources. What was verified goes stale, and the fit itself moves as either side changes.
>
> Only evidence the other side can check changes a deal. A discount changes the split. Verification changes what the deal is worth to both.

### Decisions taken in review

| # | Decision | What it replaces in 5.2 |
|---|---|---|
| D1 | The axioms answer three questions at three units: can a market exist, what has to be paid down at time 0, what prevents churn and contraction at time 1. | Three decisions in time order, all the buyer's, all read at the deal |
| D2 | One premise: each party acts on what it can check. Every cost and every value has the reading it has and the reading a party expects. | Recognized value (standing assumption 2), recognized cost (Axiom I), the gaps (Axiom III), restated separately |
| D3 | The seller absorbs the buyer's costs. Sales absorbs them before the buyer commits, account management after. The seller has its own limit, and a market exists only where both limits hold. | The pursuit corollary under Axiom II |
| D4 | The buyer moves through fixed stages and prices all three costs from the first. The cost it expects nearest its limit decides whether it proceeds, and that cost names the motion, now stated under II. | "Where the sale starts" under Axiom I |
| D5 | Seller spending creates value when the seller does the work more cheaply or the work lowers the cost at time 1. Discovery is usually the second kind. Without retention, sales spending is a price cut. | The "moving investment" corollary, which had the first two parts and not the third |
| D6 | Time 1 is decided at time 0. What can be foreseen is contracted. What cannot is planned for with a standing review. | The staging, enforcement, drift and account management corollaries, stated separately |

---

## 3. The sort

Each block of Constitution 5.2 gets one call.

- **Keep.** It says what the kernel says, or carries the mathematics behind it. It stays, reworded to the kernel where needed.
- **Compress.** It follows from the kernel in one step and changes what someone does. It stays as one or two sentences.
- **Move.** It needs a premise the kernel lacks, or answers an objection. It goes to a sibling file, with a link left behind. Most destinations already carry the material, so the move is a deletion.
- **Cut.** The kernel or another block already says it.

Line numbers are from 5.2 at commit 61e589e. *After* is an estimate of the words the block keeps in 6.0.

### 3.1 Front matter, standing assumptions and definitions

| # | Lines | Block | Words | Call | Destination | Note | After |
|---|---|---|---|---|---|---|---|
| 1 | 10-16 | Version, purpose, structure note | 108 | Compress | | The purpose names the three questions. The note that the document states structure and no measured quantity becomes one sentence. | 50 |
| 2 | 22 | Standing assumptions, lead-in | 28 | Keep | | | 28 |
| 3 | 24 | Bounded rationality and opportunism | 50 | Keep | | Axiom III rests on it. | 50 |
| 4 | 25 | Value: three kinds, persuasion, decay, catalyst, falsifier | 267 | Compress, Move | Decay equation and catalyst to `02-mathematical-models.md` section 4. Persuasion falsifier to `value-and-persuasion.md`. | Realizable, recognized and realized value fold into the premise (D2). The assumption keeps one claim: value is set by the offer and the buyer's situation, and it decays from the trigger. | 90 |
| 5 | 26 | Every actor acts on their own payoff | 139 | Compress, Move | Ghoshal and Moran to `tce-empirical-record.md`, which already carries the critique | Keeps who the parties are: the decision roles on each side and every intermediary, each with a payoff that is not its organization's. | 50 |
| 6 | 28 | Value-decay figure | 37 | Move | `02-mathematical-models.md` section 4 | It draws an equation that now lives there. | 0 |
| 7 | 34-37 | Definitions: workflow, decision role | 197 | Compress, Move | Departure events to `03-glossary-and-notation.md` | Both definitions stay. Workflow keeps the reference-workflow sentence, which Axiom III needs. | 80 |
| 8 | new | The premise paragraph | 0 | Add | | The kernel's opening: three costs, the seller absorbs them, each party acts on what it can check. Carries the division of labor in one sentence (row 25). | 120 |

### 3.2 Part I lead-in

| # | Lines | Block | Words | Call | Destination | Note | After |
|---|---|---|---|---|---|---|---|
| 9 | 43-49 | Lead-in and axiom table | 224 | Rewrite | | Columns become question, unit, time, statement, from the kernel (D1). | 150 |
| 10 | 51 | Two sources: Dahlman by kind, Williamson by time | 80 | Compress | | One sentence. Kind gives the three costs, time gives the line between II and III. | 35 |
| 11 | 53 | On the component names | 47 | Move | `03-glossary-and-notation.md`, which already carries the mapping | The premise introduces both names in one clause each. | 0 |

### 3.3 Axiom I: can a market exist?

| # | Lines | Block | Words | Call | Destination | Note | After |
|---|---|---|---|---|---|---|---|
| 12 | 59-63 | Statement, plain English, origin | 199 | Rewrite | | One plain statement from the kernel replaces the formal and plain-English pair (choice C1). Gains the seller's limit (D3). Origin kept. | 140 |
| 13 | 65 | Mechanism lead-in | 42 | Cut | | | 0 |
| 14 | 67-71 | The cost table | 241 | Keep, narrow | "What B2B adds" column to `03-glossary-and-notation.md` | The buyer's question, what lowers each cost and what sets its floor are the axiom's working parts. | 170 |
| 15 | 73 | Negotiation against policing, adaptation as investment | 85 | Compress | | One sentence. The adaptation work is an investment, stated under II. | 30 |
| 16 | 75 | Dahlman's single root, coupling, dated reading | 253 | Compress, Move | Coupling to `02-mathematical-models.md` section 3.5. Dahlman's reduction to `transaction-cost-economics.md`. | Keeps two sentences: exposure raises the bargaining cost, and until fit is verified on the buyer's workflow the reading is a lower bound. | 50 |
| 17 | 77 | Exit cost is not a fourth cost | 112 | Move | `buyer-cost-neighbors.md` | Answers an objection. The axiom does not need it. | 0 |
| 18 | 79-83 | Thresholds and $r_k$ | 144 | Keep, split | "The sale starts at the largest $r_k$" moves to II | The participation test, $r_k \le 1$ for every cost, stays here. | 110 |
| 19 | 85 | Non-compensatory costs, one payer's capacity, contrast with total cost of ownership | 117 | Compress, Move | Ellram contrast to `buyer-cost-neighbors.md` | | 60 |
| 20 | 87 | Figure: both readings of each cost | 67 | Move within | Axiom II | It draws where the sale starts. | 0 |
| 21 | 89 | Recognized cost | 209 | Compress | | The premise carries the two readings. Keeps: the seller invests twice against a cost, to lower it and to show it, and a buyer that expects a cost past its limit never enters discovery. | 60 |
| 22 | 93 | Corollary: the motion is where the sale starts | 52 | Move within | Axiom II | The kernel names the motion under II (D4). | 0 |
| 23 | 94 | Corollary: Turnkey and its erosion | 208 | Compress | Separation dynamics already in `02-mathematical-models.md` section 5.8. Erosion detail to `01-motions.md`. | Stays under I as a market condition: every cost self-serve, nothing specific sunk, eroded by entry unless something holds the search cost down. | 70 |
| 24 | 95 | Corollary: copying a motion | 77 | Move within, Compress | Axiom II | One sentence beside the motion. | 0 |
| 25 | 96 | Corollary: division of sales labor | 183 | Compress | `01-motions.md` section 9 already carries it | One sentence in the premise: business development absorbs search, the account executive bargaining, the solutions engineer policing, account management time 1. | 0 |
| 26 | 97 | Corollary: addressable market is a property of the motion | 34 | Keep | | Sits beside the seller's limit. | 34 |
| 27 | 134 | Pursuit, from Axiom II | 59 | Move within | Axiom I | Becomes the seller's limit in the statement (D3). | 0 |
| 28 | 135 | Cost floor and category prior, from Axiom II | 417 | Move within, Compress, Move | Floor dynamics, message volume and the category's shared reputation to `information-environment.md`. Remedies already in `01-motions.md` section 6. | Stays under I in three sentences: part of each cost is set outside the deal, it falls only through investment across deals or a signal costly enough to separate, and a floor above the limit and a prior above it look alike and take different remedies. | 110 |
| 29 | 99-101 | Falsifiers and failure-mode pointer | 167 | Redistribute | Sequencing and recognized-cost findings to II | Participation and Turnkey findings stay, with the cost-floor findings from row 37. | 120 |

### 3.4 Axiom II: what has to be paid down at time 0?

| # | Lines | Block | Words | Call | Destination | Note | After |
|---|---|---|---|---|---|---|---|
| 30 | 107-111 | Statement, plain English, origin | 88 | Rewrite | | Kernel II (D4, D5). Longer than 5.2's, because it now carries the motion. | 150 |
| 31 | 113 | Mechanism | 62 | Cut | | The statement says it. | 0 |
| 32 | 115-125 | The two conditions, the joint condition, price cancelling | 203 | Keep | | | 190 |
| 33 | 127 | Price-window figure | 46 | Keep | | | 46 |
| 34 | from 87, 93, 95 | Motion, the figure, copying a motion | 0 | Add | | Moved from I. The sale starts at the largest $r_k$, read on the expected cost until the buyer has entered. A motion copied from another market pays down a cost these buyers do not carry. | 110 |
| 35 | 131 | Price is not a transaction cost | 19 | Keep | | | 19 |
| 36 | 132 | Moving investment between parties | 79 | Rewrite | | D5: cheaper, or lowers the cost at time 1. Discovery is the second kind. Without retention, sales spending is a price cut. The forward-deployed engineer stays as the case where both hold. | 80 |
| 37 | 133 | Cost to serve is directional | 46 | Cut | | The motion says it. | 0 |
| 38 | 137-139 | Falsifiers | 121 | Redistribute, Add | Cost-floor findings to I | Adds: cost of sale spent on discovery and verification predicts net revenue retention, and cost of sale spent on persuasion does not. If both predict it equally, the axiom is wrong. | 110 |

### 3.5 Axiom III: what prevents churn and contraction at time 1?

| # | Lines | Block | Words | Call | Destination | Note | After |
|---|---|---|---|---|---|---|---|
| 39 | 145-149 | Statement, plain English, origin | 159 | Rewrite | | Kernel III (D6). | 140 |
| 40 | 151 | Specificity and the appropriable quasi-rent | 120 | Keep | | | 100 |
| 41 | 153-159 | Gap table: who cannot check what | 178 | Keep | | The premise's map, cost by cost. | 170 |
| 42 | 161 | Which gaps decide the future loss | 105 | Compress | | Keeps: the bargaining gap is opposed interest, which proof cannot close. What proof closes is each role's uncertainty about its own exposure. | 50 |
| 43 | 163 | Allocation settled in advance, imbalance, incomplete contracts | 160 | Compress, Move | Imbalance net of boundary loss already in `02-mathematical-models.md` sections 5.5 and 5.6 | Becomes "contract what you can foresee, plan for what you cannot" (D6), with the Strong and Volkoff point that some misfit surfaces only in use. | 50 |
| 44 | 165 | Residual control | 75 | Compress | | Keeps why more legal review does not move a stalled specific deal. | 35 |
| 45 | 167-171 | $L_p = Q_p \cdot \pi_p$ | 176 | Keep, trim | Renegotiation imbalance to `02-mathematical-models.md` section 5.5 | | 120 |
| 46 | 173-175 | Rebuild equation, discovery as a discrete step, departed champion | 48 | Keep | | Discovery is where II pays off in III. | 48 |
| 47 | 177 | Drift figure | 47 | Keep | | | 47 |
| 48 | 179, 187 | Staged loss and the staged-commitment corollary | 108 | Merge | Real options detail stays in the Milestone Valuation Model | One paragraph under "contract". | 50 |
| 49 | 183 | The gate | 50 | Keep | | | 50 |
| 50 | 184 | Governance form | 84 | Compress | `05-governance-forms.md` section 2 | | 45 |
| 51 | 185 | Frequency buys mutual sanction | 123 | Compress | `05-governance-forms.md` section 5 | One sentence. | 35 |
| 52 | 186 | Enforcement: hostages and allocated rights | 219 | Compress | `incomplete-contracts.md`, `05-governance-forms.md` | Folds into "contract": what each side loses by walking away, and who controls a renegotiation. | 60 |
| 53 | 188 | Whose exposure | 44 | Keep | | | 44 |
| 54 | 189 | Stakes for agents and adjudicators | 153 | Move | `05-governance-forms.md` section 5, which already carries it | One-line pointer. | 25 |
| 55 | 190 | Friction Allocation Principles | 87 | Keep | | They define "evidence the other side can check". | 87 |
| 56 | 191 | Three levers | 154 | Compress | | The kernel's closing line, plus a guarantee being part transfer and part verification. | 70 |
| 57 | 192, 193 | Reputation depreciates, two things drift, account management | 162 | Rewrite | | Becomes "plan for what you cannot foresee": a standing review agreed at time 0, and account management funded while the margin at the next boundary covers it. | 80 |
| 58 | 194 | The Decay Clock | 47 | Compress | `02-mathematical-models.md` section 4 | | 25 |
| 59 | 196-198 | Falsifiers | 111 | Keep, Add | | Adds: relationships with a review cadence agreed before either side sinks anything drift less than matched relationships without one. | 130 |

### 3.6 Parts II and III, history and links

| # | Lines | Block | Words | Call | Destination | Note | After |
|---|---|---|---|---|---|---|---|
| 60 | 202-231 | Part II, the derivations table | 419 | Cut | | Each axiom's corollaries are its derivations and name their files, so the table repeats them (choice C3). | 0 |
| 61 | 235-246 | The two conditions and what each term means | 170 | Keep | | | 150 |
| 62 | 248-257 | Reading a stall, eight steps | 255 | Compress, Move | Eight-step version to `practice/deal-triage-calculator.md` | Becomes the three questions asked in order (choice C4). | 60 |
| 63 | 259-284 | Failure modes, 20 rows | 425 | Keep, regroup | | Unamortizable joins I with the seller's limit. Unhostaged merges with defection, and reputation hoarding with drift. About 17 rows. | 350 |
| 64 | 288-311 | Version history | 1538 | Compress | git history | One line per version from 4.0, the way the nineteen earlier revisions already sit in git. | 250 |
| 65 | 315-338 | Related | 195 | Compress | `00-reading-guide.md` carries the per-axiom research map | Keeps the sibling list and the practice map. | 110 |

---

## 4. What 6.0 would look like

Sums of the *Words* and *After* columns in section 3. Blocks that move between axioms are counted where they land, so pursuit and the cost floor count under Axiom I.

| | 5.2 | 6.0 estimate |
|---|---|---|
| Front matter, assumptions, definitions, premise | 826 | 468 |
| Part I lead-in | 351 | 185 |
| Axiom I | 2,666 | 954 |
| Axiom II | 664 | 705 |
| Axiom III | 2,410 | 1,461 |
| Parts II and III, version history, links | 3,002 | 920 |
| **Total** | **9,919** | **4,693** |

The counted blocks cover 9,919 of the file's 9,995 words. The rest is headings.

Axiom II grows, because it now carries the motion. Axioms I and III each lose more than a third. Most of the remaining cut comes from three blocks that are not theory: the derivations table, the eight-step stall reading and the version history.

The structure of 6.0:

1. Purpose and the structure note
2. Standing assumptions (three, shorter)
3. Definitions (workflow, decision role)
4. The premise: three costs, the seller absorbs them, each party acts on what it can check
5. Axiom I: can a market exist? Both limits, cost floors, Turnkey
6. Axiom II: what has to be paid down at time 0? The two conditions, the motion, what seller spending buys
7. Axiom III: what prevents churn and contraction at time 1? Exposure, contract or plan, drift
8. The two conditions, the three questions as the stall reading, failure modes
9. Version history, related

---

## 5. Choices still open

- **C1. One statement per axiom.** 5.2 states each axiom twice, formally and then in plain English. The kernel is already plain. Proposed: one statement each, in the kernel's words, with the mathematics beside it.
- **C2. Version 6.0.** The axiom statements change for the first time since 4.0, and so does each axiom's unit. Proposed: 6.0, with the root README footer bumped together.
- **C3. Cut the derivations table.** Nothing checks it, and the corollaries already name their files. Proposed: cut. The test of whether a claim belongs, that it traces to an axiom, moves into the purpose statement.
- **C4. Where the eight-step stall reading goes.** Proposed: `practice/deal-triage-calculator.md`, since it is operational. The Constitution keeps the three questions in order.
- **C5. Register entries.** The seller's limit extends item 6 in `07-open-questions.md`. The two new falsifiers, discovery spending predicting retention and a review cadence reducing drift, each need an entry saying what evidence would settle them.

---

## 6. Applying it

1. Rewrite `00-tcg-constitution.md` from section 3, one Part at a time.
2. Check each Move destination. Most already carry the material, so the move is a deletion. Add only what a destination is missing.
3. Carry the change downstream: `01-motions.md` (the motion now stated under II), `04-seller-surplus-model.md` (pursuit now under I), `03-glossary-and-notation.md`, `05-governance-forms.md`, the root `CLAUDE.md` description of the axioms, and the four files that cite "Constitution, Part III" or "Part I" by name.
4. Rerun `make_figures.py` if a figure moves, then the five checks.
5. One review pass over the finished Constitution before merge.
