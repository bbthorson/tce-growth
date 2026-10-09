---
title: "Motions"
layer: theory
status: active
version: 2.2
operationalizes: [axiom-1, axiom-2, axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# Motions

**Version:** 2.2
**Purpose:** To derive the motion from where the sale starts, which is the cost nearest its own participation threshold under Axiom I. Then to say what each motion deploys, why Turnkey is a condition of a market rather than a fourth motion, and how the names map onto the vocabulary the industry already uses.

> [!IMPORTANT]
> **This file carries the argument behind Axiom I's first corollary, that the motion is where the sale starts.** The positions and thresholds are stated in the [Constitution](./00-tcg-constitution.md) and given their functional form in [02-mathematical-models.md](./02-mathematical-models.md) section 6. The [Deal Triage Calculator](../../practice/deal-triage-calculator.md) emits them, and [03-glossary-and-notation.md](./03-glossary-and-notation.md) carries the symbols. Section 9 records what this file does not settle, and section 10 is the translation table for readers arriving with Product-Led and Sales-Led in hand.

A sales motion is the instrument set a seller deploys to pay down a buyer's cost of using the market. A seller cannot alter the buyer's willingness to pay, which is a property of the product, and price is a transfer that cancels between the two parties' conditions under Axiom II. So a motion works entirely by lowering one or more of three costs, which take Dahlman's (1979) names in theory and keep the field's names in the notation:

* **Search and information, $F_{search}$:** the buyer cannot discover, compare, or reach a viable solution at acceptable cost.
* **Bargaining and decision, $F_{consensus}$:** the buyer's decision roles cannot agree, because each is uncertain what the change does to its own budget, headcount and standing. The field calls this the consensus cost.
* **Policing and enforcement, $F_{implementation}$:** the buyer cannot yet verify that the seller will deliver what was promised and that the product will work in its environment. The field calls this the implementation cost. The buyer's own adaptation work, the integrations built and the workflows rewired, is an investment against this cost under Axiom II rather than the cost itself.

The three are separately addressable rather than separately caused. A workflow the product must fit but does not raises $F_{implementation}$ and creates $F_{consensus}$ at the same time, because an imposition creates a decision role whose objectives worsen. Treat them as three bills the buyer pays, not as three independent variables.

---

## 1. Where the sale starts

Axiom I reads each cost against two thresholds of its own. Below the self-serve threshold $\tau^{self}_k$ the buyer can pay the cost down alone. Above the participation threshold $\tau^{part}_k$ the buyer does not enter the market. Each cost's position between its own two is

$$r_k = \frac{F_k - \tau^{self}_k}{\tau^{part}_k - \tau^{self}_k}, \qquad k \in \{search,\; consensus,\; implementation\}$$

| Position | Zone |
|---|---|
| $r_k \le 0$ | Self-serve. The buyer pays this cost down alone. |
| above zero and at most one | Bearable, with seller investment |
| $r_k > 1$ | Keeps the buyer out, whatever the other two read |

**The sale starts at the largest $r_k$**, the cost nearest the point where it would keep the buyer out. That cost is where the seller's first investment goes, and the motion is named after it. Two costs at the same position are run together.

**Positions, not shares.** Earlier versions summed the three costs into a level and divided each by the total to get a direction. Both operations assumed the three costs sat on one scale, and they never did. A position compares each cost against its own thresholds and never against the other two, so the three are comparable without sharing a scale. It also catches the case shares could not: a cost holding a small share of the total can still sit above its participation threshold and end the deal.

The costs are in fractions of annual contract value, per [02-mathematical-models.md](./02-mathematical-models.md) section 1.2. The thresholds are named in the theory and placed as edges on the calculator's counts, and [06-calibration.md](./06-calibration.md) records every edge as chosen.

---

## 2. Each cost has its own instrument family

A seller can discount, and a discount moves surplus from seller to buyer one for one without shrinking any cost ([02-mathematical-models.md](./02-mathematical-models.md) section 1.3). What remains is the three costs.

**A motion is therefore defined by which cost the seller pays down first.** There are three costs, so there are three families of instrument, and no more.

| Cost | What the buyer cannot do | What the seller produces |
|---|---|---|
| $F_{search}$ | Find a viable solution at acceptable cost | Artifacts that travel without the seller present |
| $F_{consensus}$ | Get their own organization to agree | Artifacts that let each decision role see and accept its own outcome |
| $F_{implementation}$ | Tell whether the seller will deliver and the product will work here | Artifacts that resolve technical and operational uncertainty |

**Where the sale starts gives an order, not a label.** A deal with positions $(0.2,\, 0.8,\, 0.5)$ starts at consensus and runs implementation instruments behind it. Pay the consensus cost down and the order can invert. Both are ordinary deals and neither is a special case.

This resolves a question the older framing could not answer. Asking whether consensus work is a separate motion or a phase of an implementation-heavy one assumes motions are exclusive. They never were. Every deal carries all three costs, and what varies is which one sits nearest its threshold now.

### 2.1 The two blockers inside search

$F_{search}$ carries two distinct blockers.

| Blocker | Instrument |
|---|---|
| The buyer cannot name the category | Commercial teaching, reference architectures, category definition |
| The buyer cannot reach the seller | Partnerships, channel, marketplace listing, group purchasing |

**Fit verification is not a search blocker.** Trying the product is verification the buyer runs on themselves, and it resolves fit only when nothing specific is sunk, because nobody can trial a six-month integration. Where nothing specific is sunk, a trial settles the question at no cost and market terms hold under Axiom III's gate. Where something is, the same question becomes the policing pair's uncertainty and needs the seller's proof. Gate B of the [Deal Triage Calculator](../../practice/deal-triage-calculator.md) is where the framework reads which case it is in.

The second row is a cost most frameworks do not name. A hospital chief information officer can know the category, name five vendors, and still be structurally unreachable without a channel. A missing channel puts search above its participation threshold whatever else the deal reads, and neither education nor a trial reduces it. Research backing is in [channel-collapse.md](../02-research/channel-collapse.md), and Axiom III's requirement that any adjudicator carry a stake applies directly to the channels involved.

These are two instruments serving one cost. They are not two motions.

### 2.2 Bargaining has a mature instrument set this repository does not carry

The bargaining and decision cost, which the field calls consensus, is worked hard by the wider sales profession. Qualification frameworks built around economic buyer access, written decision criteria, documented decision process, and champion development are instruments for that cost, and they are the incumbent practice for it.

This repository measures the cost and supplies no instruments for it. The [Consensus Friction Calculator](../../practice/consensus-friction-calculator.md) produces a number and then prescribes executive sponsorship, which is a single tactic rather than a motion. The cost resists the instruments that work on the other two because its gap sits inside each decision role, about its own outcome, where nothing the seller knows and withholds is causing it. Research is in [buying-center-dynamics.md](../02-research/buying-center-dynamics.md).

The gap is real and it is the largest one this document surfaces.

---

## 3. What positions do not read

Positions answer where the sale starts. Two other questions sit beside them, and each belongs to a different axiom.

**Whether the buyer enters at all.** A cost above its participation threshold keeps the buyer out, and no work on the other two reaches it. The seller pulls that cost back into range with the instrument for it, or declines. Working it as though it were an ordinary sales problem is the kept-out failure Axiom I names.

**How much apparatus the deal needs.** Earlier versions read this off the summed level and drew a Turnkey and Structural boundary at half its range. Both retired in Constitution 4.0, because the level stood in for specificity and conflated it with size. The question now splits in two. How much the seller must invest today is Axiom II's seller condition: the seller goes ahead only when its own share is covered by its own return. Whether governance apparatus is needed is Axiom III's specific exposure: whether the deal sinks anything worth less outside this relationship. Apparatus applied where nothing specific is sunk is the over-frictioned failure.

**Where the sale starts and specific exposure are independent.** A deal can start at implementation and sink nothing specific, which is expensive work against a standard rather than uncertain work. A deal can have every cost self-serve and still sink a specific integration, which is a light sale with a heavy contract. The calculator crosses the two readings for that reason.

---

## 4. Four readings, and what each deploys

The three motions are named after the cost the seller pays down first. Turnkey names the condition where no cost needs paying down.

| Condition | Name | What the seller deploys | State of the instruments |
|---|---|---|---|
| Every cost self-serve, nothing specific sunk | **Turnkey** | Published pricing, automated provisioning, self-service trial, zero-touch onboarding. Fit verification transfers entirely to the buyer. | None needed. A market in this condition repays no dedicated apparatus. |
| The sale starts at search | **Search-led** | The two search instruments of section 2.1: teaching where the category is unnamed, channel where the buyer is unreachable. | Present and thin. No instrument file in this repository. |
| The sale starts at consensus | **Consensus-led** | Mapping each decision role's exposure, champion enablement, bilateral decision criteria. | Absent. Measured by the Consensus Friction Calculator and otherwise served by the incumbent qualification practice, outside this framework. |
| The sale starts at implementation | **Implementation-led** | Four sequenced governance artifacts: [Contextual Blueprint](../../practice/implementation-motion/01-discovery-contextual-blueprint.md), [Red Team Protocol](../../practice/implementation-motion/02-validation-red-team-protocol.md), [Mutual Implementation Plan](../../practice/implementation-motion/03-closing-mutual-implementation-plan.md), [Sustaining Adoption Review](../../practice/implementation-motion/04-sustaining-adoption-review.md). | Present and developed. |
| Two costs at the same position | **Run together** | Both instrument sets, neither picked as the motion. | Whatever the two motions supply. |

The names in the second column are the words the Deal Triage Calculator returns.

**Each reading has a characteristic misread.** Turnkey's is a low decision-role count inside a complex enterprise architecture, which masks a specific integration downstream. Search-led's is mid-cycle commoditization: as teaching succeeds, search cost falls and the buyer pivots to price comparison. Implementation-led's is applying governance artifacts to a deal that starts at search, forcing operational rigor onto an uncommitted prospect. Running together's is picking one of the two and calling it the motion.

**Turnkey is a condition of the market, not a fourth cost to pay down.** A light marketing funnel feeding a low-cost trial feeding buyer-run deployment is a light touch on all three costs at once, and it works only while all three stay self-serve. Reading it as a competitor to the other three motions is the error this document is most concerned to correct, and sections 6 and 8 say what that error costs. The condition also does not last on its own, for the reason section 5.2 gives.

Naming the consensus motion beyond its cost is still open. Any name chosen here would enter the repository ahead of the instrument set that justifies it, and the instrument set is the missing piece rather than the name.

---

## 5. Positions move, and gaps rebuild

Where the sale starts is a reading taken at a moment. Two mechanisms change it, and they belong to different axioms.

**Investment moves positions.** A seller's investment against a cost pays it down under Axiom II and lowers that cost's position. Pay down the cost where the sale started and another cost becomes nearest its threshold. The calculator re-takes its counts at every artifact boundary for this reason, and the sequence of readings is the record of what the work moved.

**Verification closes gaps.** Each cost runs between its own pair of parties, and each pair's uncertainty is a gap. Under Constitution 4.0 the gaps no longer multiply costs. They feed the chance of future loss under Axiom III, and closing one lowers a loss both sides were carrying.

### 5.1 Three pairs, three gaps

| Cost | Whose uncertainty, about what |
|---|---|
| $F_{search}$ | The buyer's, about the market |
| $F_{consensus}$ | Each decision role's, about its own outcome |
| $F_{implementation}$ | Bilateral. The seller's, about the buyer's environment. The buyer's, about the seller's capability in it. |

The [Asymmetry Scorecard](../../practice/asymmetry-scorecard.md) measures the third pair alone. The search gap mostly prices today's cost and decides participation. The other two decide what each party can lose once something specific is sunk.

### 5.2 Drift, departures and categories

Absent maintenance, each gap rebuilds toward its ceiling at its own rate $\gamma_k$, per [02-mathematical-models.md](./02-mathematical-models.md) section 5.3. Discovery is a separate, discrete step down that someone pays for. A deal is therefore a path rather than a point, and so is an account after signature.

| Rate | What drives it | Where it is already named |
|---|---|---|
| $\gamma_{search}$ | New entrants, category redefinition | Nowhere |
| $\gamma_{consensus}$ | Occupant turnover, reorganization | Nowhere |
| $\gamma_{implementation}$ | Staff turnover, workflow change, systems installed unseen | [04-seller-surplus-model.md](./04-seller-surplus-model.md) section 7.2 |

**The field consequence sits in the bargaining row.** A champion leaving is the bargaining gap reopening all at once. What the new occupant cannot verify is open again, and the deal can leave the viable zone without any change in the product, the price or the technical work. That event is among the most common ways an enterprise deal dies, and the framework has not sourced how common. It is also one of two events. A decision role can dissolve rather than change occupant, when the mandate leaves with the person, and then the coalition changes and the bargaining cost with it. No re-statement by a successor recovers that.

**Where the sale starts moves at the level of a category too.** An emerging category carries high search and policing cost and the sale starts at search. As industry-wide education completes, search cost collapses and the sale starts at implementation. As integrations standardize, every cost falls into the self-serve zone and the category reaches Turnkey, at which point the apparatus retires. Sellers miss the second and third transitions, and they miss the third more often, because nothing external prompts a re-count.

**Turnkey then erodes through entry.** A motion that needs little seller investment is cheap to copy, so competitors enter. Each entrant is another alternative to rule out, which raises the search cost, and free trials and identical claims stop separating good sellers from bad, which raises the policing cost. The category leaves Turnkey unless something holds the search cost down as sellers arrive. The Constitution states this as an Axiom I corollary, and a self-serve motion kept running through it is the Turnkey-erosion-unread failure.

### 5.3 What this retires

The per-component multiplier, the summed level, the direction shares and the reduced form $y = a\hat{\Delta}_A^2 + c$ all retired in Constitution 4.0. [02-mathematical-models.md](./02-mathematical-models.md) section 7 records why each went. The argument the reduced form existed to make, that cutting price cannot offset a wide gap, now follows from price cancelling between the two conditions.

---

## 6. What follows for the seller's market

A seller who runs only self-serve tactics can transact only with buyers whose every cost is self-serve. Buyers whose sale starts at a cost that needs investment are not lost somewhere in the funnel. They were never reachable, because the motion offered no instrument for the cost that was nearest to keeping them out.

Addressable market is therefore a property of the motion rather than of the product, and [05-governance-forms.md](./05-governance-forms.md) section 4 carries that argument and its three consequences.

---

## 7. Two symptoms of the unallocated failure

Axiom III's unallocated failure, specific investment sunk with no staging or stop rights agreed, shows in two places. Before the investment, a party that expects to be held up declines to sink it at all, and the buyer defers or builds internally. After it, a buyer whose policing uncertainty was never resolved signs on an easy commercial path, fails to deploy, and leaves, and the failure is misdiagnosed as product or onboarding. The second is the one positions alone cannot see, which is why the calculator reads specific exposure apart from where the sale starts and names the light-sale, heavy-contract case.

---

## 8. Why sellers choose the wrong motion

Self-serve tactics carry a lower cost of sale, and a representative paid on bookings or a leader measured on efficiency picks them for reasons that have nothing to do with the deal in front of them. By the Constitution's third standing assumption that is expected, and by Axiom III's stakes corollary the remedy is vesting compensation on outcomes that survive signature ([05-governance-forms.md](./05-governance-forms.md) section 5). It is usually read as protection against poor execution on specific deals. It is also the instrument that governs motion selection, and that is the wider claim. At the level of an organization the same mistake is imitation: a motion copied from another market, with the organization built to pay down a cost its buyers do not carry.

---

## 9. What this does not settle

Each item points at its entry in [07-open-questions.md](./07-open-questions.md) where one exists.

- **The consensus motion has no instrument file.** The [Deal Triage Calculator](../../practice/deal-triage-calculator.md) says so out loud when a deal routes there. Building the instrument set is the open work, and naming the motion further before that would produce a label with nothing behind it. Open question 2.
- **Whether the largest position is the right rule.** Starting the sale at the cost nearest its participation threshold was agreed as the starting reading in Constitution 4.0, to be revisited once the zones are calibrated. The falsifier is in the Constitution: deals where the first investment went to the largest $r_k$ convert no faster than matched deals where it went elsewhere.
- **Where the thresholds sit.** Both edges on every count are chosen, placed on the boundaries of the score bands earlier versions used, and [06-calibration.md](./06-calibration.md) records them as chosen. The counts are observations. The edges are not.
- **Whether the position is vendor-relative.** An incumbent defending a renewal and a challenger attacking it face the same opportunity with different positions, because the incumbent's adaptation is already sunk. The instrument scores the deal rather than a vendor, which is a decision rather than an oversight: a vendor-scored instrument owes the reader an account of how each vendor wins, and that account does not exist yet. Until it does, an incumbent counting a renewal will read implementation-light for a reason the counts cannot see, and should say so on the sheet rather than trusting the routing.
- **Whether the coupling between costs moves where the sale starts.** Misfit raises the policing cost and creates a bargaining cost at once, so the reading partly depends on when it is taken. Open question 3.
- **Whether the three drift rates behave as one mechanism.** $\gamma_{consensus}$ is the only one with a discrete field event attached, an occupant change. The other two are asserted to be continuous and nothing tests that. Open question 15.

---

## 10. The incumbent vocabulary

Everyone arriving here knows what Product-Led Growth means. This section says where it and its neighbours land, and where they mislead. Nothing here is used to decide anything.

<!-- vale TCG.RetiredTerms = NO -->
<!--
  The retired-term rule is off for the rest of this section. Naming retired
  terms is what the section is for, so the rule would fire on every row of the
  map and the fix would be to stop doing the job. This is the one place in the
  repository where an old name is the subject rather than a mistake.
-->

**The incumbent names do not form a set.** Product-Led Growth is named after the instrument, Sales-Led Growth after the actor, and Implementation-Led Growth after a cost. Only the third names a cost, which is why the obvious extensions, Search-Led and Consensus-Led, had nowhere to sit. This framework names every motion after the cost the seller pays down first, because that is what the theory says a motion is. The set then closes: three costs, three motions, plus one market condition in which no cost needs a seller's investment.

| This framework | Closest incumbent term | Relationship |
|---|---|---|
| **Turnkey** | Product-Led Growth | Overlapping, not equal. Turnkey is a condition of a market: every cost self-serve and nothing specific sunk. Product-Led is a company-level strategy: the product is the primary acquisition instrument, and it works under that condition. The two come apart in the case that matters most, a Product-Led company moving upmarket. Security review arrives and the committee grows, so the bargaining cost leaves the self-serve zone. Integration deepens, so something specific is sunk. The deals have left Turnkey while the company still calls its motion Product-Led, and the instrument set did not follow. Entry produces the same split with the company unchanged, because a Product-Led market that fills with competitors raises its own search cost. Reading each cost's position deal by deal is what makes either transition visible while it is happening. |
| **Search-led** | Sales-Led Growth, category creation, evangelical selling | Search-led is wider. It also covers channel and trial, which Sales-Led does not. |
| **Consensus-led** | No established term. Nearest neighbours are MEDDPICC-style qualification and multithreading | The incumbent practice exists as qualification discipline rather than as a named motion. |
| **Implementation-led** | Implementation-Led Growth, forward-deployed engineering, solution selling | Direct. This framework was called ILG before the theory outgrew the name. Older analyses still use it for the whole framework. |
| **Run together** | No established term | The industry treats motions as exclusive, so the case where two costs sit at the same position has no name. Older analyses in this repository call it Composed. |

**Product-Led and Sales-Led name the seller, not the cost, and each bundles several costs.** A sales-led company runs evangelical representatives, who reduce search, and enterprise representatives working a committee, who reduce bargaining, and solutions engineers, who reduce policing uncertainty. Calling all of that one instrument narrows the term to one of its functions. And a trial, the Product-Led instrument, is not a search instrument at all: it is verification the buyer runs alone, and it works only when nothing specific is sunk, so the buyer can walk away at no cost. Read by cost, the argument the two camps are having splits into two measurable questions. Can the buyer verify fit alone, which is Axiom III's gate. Does the buyer know what they are looking for, which is Axiom I. Neither answer is a philosophy.

**What this framework is not competing with.** Go-to-market vocabulary mixes three tiers, and the tiers compose.

| Tier | What it decides | Examples |
|---|---|---|
| **Theory of transaction cost** | Which costs a deal carries, and therefore which instruments can reduce them | This framework |
| **Qualification framework** | What must be true before a deal is called committed | MEDDPICC, BANT |
| **Conversational methodology** | How a perspective gets reframed in the room | Challenger, SPIN |

A team using this framework still needs a qualification standard and a conversational technique. Qualification tells you whether a deal is real. It does not tell you which of three costs sits nearest to keeping the buyer out, and it does not reduce any of them.

The motions are written out rather than abbreviated, because SLG would mean two things in one conversation and the written names match the words the Deal Triage Calculator returns.

<!-- vale TCG.RetiredTerms = YES -->

---

## Related

- [00-tcg-constitution.md](./00-tcg-constitution.md) — Axiom I supplies the positions and participation thresholds, Axiom II the investment that moves them, and Axiom III the specific exposure and the gate.
- [02-mathematical-models.md](./02-mathematical-models.md) — Section 6 for the thresholds and positions, section 7 for the forms Constitution 4.0 retired.
- [05-governance-forms.md](./05-governance-forms.md) — Frequency, the governance form, and what the seller's market follows from.
- [06-calibration.md](./06-calibration.md) — Provenance of every number named here, including every threshold edge.
- [07-open-questions.md](./07-open-questions.md) — The register section 9 points into.
- [04-seller-surplus-model.md](./04-seller-surplus-model.md) — The seller's side of the transaction, which section 8 depends on.
- [transaction-cost-economics.md](../02-research/transaction-cost-economics.md) — Coase's question, Dahlman's three costs and Williamson's split by time.
- [channel-collapse.md](../02-research/channel-collapse.md) — The reachability blocker, which most frameworks do not name as a cost.
- [Deal Triage Calculator](../../practice/deal-triage-calculator.md) — The instrument that emits the positions and the specific exposure, and the conditions under which the implementation-led motion should be declined.
- [models/README.md](../../models/README.md) — Executable forms of the equations referenced here.
