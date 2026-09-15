---
title: "Motions"
layer: theory
status: active
version: 2.0
operationalizes: [axiom-1, axiom-2, axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# Motions

**Version:** 2.0
**Purpose:** To derive motion selection from the two quantities Axioms I and II name, so that a motion is a region of one space rather than an item on a list. Then to say what each region deploys, and how the names map onto the vocabulary the industry already uses.

> [!IMPORTANT]
> **This file carries the derivation behind two of the framework's claims.** Axiom I's composition equation and Axiom III's per-component amplification are stated in the [Constitution](./00-tcg-constitution.md) and argued here. The [Deal Triage Calculator](../../practice/deal-triage-calculator.md) emits both quantities and [03-glossary-and-notation.md](./03-glossary-and-notation.md) carries the symbols. Section 9 records what the model does not settle, and section 10 is the translation table for readers arriving with Product-Led and Sales-Led in hand.

A sales motion is the instrument set a seller deploys to reduce a buyer's transaction friction. A seller cannot alter the buyer's willingness to pay, which is a property of the product, so a motion works entirely by lowering one or more of three costs:

* **Search, $F_{search}$:** the buyer cannot discover, compare, or reach a viable solution at acceptable cost.
* **Bargaining, $F_{consensus}$:** the buyer's own stakeholders cannot reconcile competing priorities and operational risk. The field calls this the consensus cost.
* **Enforcement, $F_{implementation}$:** nobody can yet verify that post-signature execution will succeed without destructive disruption, and the buyer's own adaptation is sunk once it starts. The field calls this the implementation cost.

The three are separately addressable rather than separately caused. A workflow the product must fit but does not raises $F_{implementation}$ and generates $F_{consensus}$ at the same time, because an imposition creates a stakeholder whose objectives worsen. Treat them as three bills the buyer pays, not as three independent variables.

---

## 1. The two quantities

Axiom I states that transaction costs decompose into three components. Write them as one object:

$$\mathbf{F} = (F_{search},\; F_{consensus},\; F_{implementation})$$

Two properties of that object carry all the information a seller needs, and the first two axioms name one each.

**Direction.** Where the vector points. Which component dominates, and by how much.

$$\hat{\mathbf{F}} = \frac{\mathbf{F}}{\lVert \mathbf{F} \rVert}$$

**Magnitude.** How long the vector is. The total cost of transacting.

$$\lVert \mathbf{F} \rVert_1 = F_{search} + F_{consensus} + F_{implementation}$$

The two axioms map onto these directly. Axiom I's *the one that binds selects the motion* is a claim about direction. Axiom II's *the more specific the investment, the more a deal costs to transact* is a claim about magnitude. They are two claims about one object and they answer different questions, which is why an instrument that emits only their sum answers neither.

The $L^1$ norm is used because it is what the field already produces. The Deal Triage Calculator sums three component scores, which is a sum rather than a Euclidean length. Nothing in what follows depends on the choice.

---

## 2. Direction selects the instrument mix

A seller can lower the buyer's perceived cost, and the reduced form in [02-mathematical-models.md](./02-mathematical-models.md) section 1.2 establishes that lowering the price term alone is the weakest of the available levers. What remains is friction, and friction has three components.

**A motion is therefore defined by which component the seller spends to reduce.** There are three components, so there are three families of instrument, and no more.

| Component | What the buyer cannot do | What the seller produces |
|---|---|---|
| $F_{search}$ | Find a viable solution at acceptable cost | Artifacts that travel without the seller present |
| $F_{consensus}$ | Get their own organization to agree | Artifacts that let stakeholders reconcile competing objectives |
| $F_{implementation}$ | Tell whether installing it will break them | Artifacts that resolve technical and operational uncertainty |

**Direction gives a mix, not a label.** A deal at $(0.1,\, 0.7,\, 0.2)$ runs mostly consensus instruments over a light implementation layer. A deal at $(0.1,\, 0.3,\, 0.6)$ inverts that. Both are ordinary deals and neither is a special case.

This resolves a question the older framing could not answer. Asking whether consensus work is a separate motion or a phase of an implementation-heavy one assumes motions are exclusive. They never were. Every deal carries all three components, and what varies is the weighting.

### 2.1 The three sub-costs of search

$F_{search}$ carries three distinct blockers.

| Blocker | Instrument |
|---|---|
| The buyer cannot name the category | Commercial teaching, reference architectures, category definition |
| The buyer cannot reach the seller | Partnerships, channel, marketplace listing, group purchasing |
| The buyer cannot tell whether the fit holds | Trial, sandbox, self-serve evaluation |

The middle row is a cost most frameworks do not name. A hospital chief information officer can know the category, name five vendors, and still be structurally unreachable without a channel. That cost falls largely on the seller, and neither education nor a trial reduces it. Research backing is in [channel-collapse.md](../02-research/channel-collapse.md), and Axiom II's requirement that any adjudicator carry a stake applies directly to the channels involved.

These are three instruments serving one component. They are not three motions.

### 2.2 Consensus has a mature instrument set this repository does not carry

The consensus component is worked hard by the wider sales profession. Qualification frameworks built around economic buyer access, written decision criteria, documented decision process, and champion development are consensus instruments, and they are the incumbent practice for that component.

This repository measures the component and supplies no instruments for it. The [Consensus Friction Calculator](../../practice/consensus-friction-calculator.md) produces a number and then prescribes executive sponsorship, which is a single tactic rather than a motion. The component resists the instruments that work on the other two because its gap sits between the buyer's stakeholders, about each other, where nothing the seller knows and withholds is causing it. Research is in [buying-center-dynamics.md](../02-research/buying-center-dynamics.md).

The gap is real and it is the largest one this document surfaces.

---

## 3. Magnitude sets the apparatus

Magnitude answers a different question: how much machinery the deal can carry before the machinery costs more than it saves.

This is Axiom II's boundary condition. $k > k_{threshold}$ separates Turnkey deals from Structural deals, and $F_{deployed} \sim k$ requires the friction the seller deploys to scale with the specificity it manages. Both over-frictioning and under-frictioning are failures of magnitude rather than of direction.

Three component scores on $[0, 10]$ put the level on $[0, 30]$, so $k_{threshold} = 15$ sits at half the range, where the retired four-factor scale's 10 out of 20 sat. Multiply an archived score by 1.5 to compare it. Nothing about the boundary gained empirical support in the move, and [06-calibration.md](./06-calibration.md) records it as chosen.

**Level is read from base friction, before amplification.** Asset specificity is a property of the deal. What anyone currently knows about the deal is not, and folding the gaps into the level would make a well-mapped Structural deal reclassify itself as Turnkey the week the Blueprint landed.

**Direction and magnitude are independent.** A short vector pointed at implementation is a small technical purchase. A long vector pointed at implementation is a Structural deal. Same direction, different apparatus.

---

## 4. Four regions, and what each deploys

Named motions are regions of the space rather than members of a list. The dominance threshold of 0.50 is chosen, and a vector reaching no component's threshold is read as mixed rather than forced into the nearest label.

| Region | Signature | Name | What the seller deploys | State of the instruments |
|---|---|---|---|---|
| Short vector, any direction | Level below 15 | **Turnkey** | Published pricing, automated provisioning, self-service trial, zero-touch onboarding. Fit verification transfers entirely to the buyer. | None needed. A short vector repays no dedicated apparatus. |
| Long, search-dominant | $\hat{F}_{search} \ge 0.50$ | **Search-led** | The three search instruments of section 2.1: teaching where the category is unnamed, channel where the buyer is unreachable, trial where the fit is unverified. | Present and thin. No instrument file in this repository. |
| Long, consensus-dominant | $\hat{F}_{consensus} \ge 0.50$ | **Consensus-led** | Cross-department objective mapping, champion enablement, bilateral decision criteria. | Absent. Measured by the Consensus Friction Calculator and otherwise served by the incumbent qualification practice, outside this framework. |
| Long, implementation-dominant | $\hat{F}_{implementation} \ge 0.50$ | **Implementation-led** | Four sequenced governance artifacts: [Contextual Blueprint](../../practice/implementation-motion/01-discovery-contextual-blueprint.md), [Red Team Protocol](../../practice/implementation-motion/02-validation-red-team-protocol.md), [Mutual Implementation Plan](../../practice/implementation-motion/03-closing-mutual-implementation-plan.md), [Sustaining Adoption Review](../../practice/implementation-motion/04-sustaining-adoption-review.md). | Present and developed. |
| Long, no component at 0.50 | None reaches 0.50 | **Composed** | The top two instrument sets in proportion to their weights, heaviest first. | Whatever the two regions supply. |

The five names in the third column are the words the Deal Triage Calculator returns.

**Each region has a characteristic misread.** Turnkey's is a low seat count inside a complex enterprise architecture, which masks downstream integration cost. Search-led's is mid-cycle commoditization: as teaching succeeds, search cost falls and the buyer pivots to price comparison. Implementation-led's is applying governance artifacts to a search-dominant deal, forcing operational rigor onto an uncommitted prospect. Composed's is picking one of the two and calling it the motion.

**The short-vector region is a magnitude claim, not a direction.** A light marketing funnel feeding a low-cost trial feeding buyer-run deployment is a light touch on all three components at once. Reading it as a competitor to the other three regions is the error this document is most concerned to correct, and sections 6 and 8 say what that error costs.

Naming the consensus region beyond its component is still open. Any name chosen here would enter the repository ahead of the instrument set that justifies it, and the instrument set is the missing piece rather than the name.

---

## 5. Asymmetry rotates the vector, and drift rotates it back

The obvious way to write the effective cost equation applies one amplifier to the whole sum:

$$F_{effective} = (F_{search} + F_{consensus} + F_{implementation}) \cdot (1 + \hat{\Delta}_A)$$

Scaling every component by the same factor changes the length of the vector and leaves its direction untouched. The consequence is exact rather than approximate: **under that equation, no amount of asymmetry and no amount of work reducing it can change which motion a deal needs.** Direction would be invariant to $\hat{\Delta}_A$.

That contradicts ordinary experience. A seller who maps an environment has changed the shape of the deal, not only its size. This section is the argument that rules the single-multiplier form out.

### 5.1 Three pairs, three gaps

The single gap $\Delta_A = I_{seller} + I_{buyer}$ describes two parties, and the three components do not share one pair of parties between them.

| Component | Whose ignorance, about what |
|---|---|
| $F_{search}$ | The buyer, about the market |
| $F_{consensus}$ | The buyer's stakeholders, about each other |
| $F_{implementation}$ | The seller, about the buyer's environment |

Only the third is seller against buyer. The [Asymmetry Scorecard](../../practice/asymmetry-scorecard.md) measures that third pair.

Amplify each component by its own pair's gap, which is what Axiom III does:

$$F_{effective} = \sum_{k} F_k \, (1 + \hat{\Delta}_k)$$

The sum still factors exactly into $F_{base}(1 + \hat{\Delta}_A)$ when $\hat{\Delta}_A$ is read as the friction-weighted mean of the three, so nothing that needs only the total has to carry three numbers.

Direction now moves with the work. A deal that opens implementation-dominant rotates toward consensus as discovery closes $\Delta_{implementation}$, which is what a Blueprint is for.

### 5.2 Drift is the same rotation running backwards

Written at the deal level, drift is $\hat{\Delta}_A(t) = \hat{\Delta}_A(0) + \gamma t$ before signature, and section 7.2 of [04-seller-surplus-model.md](./04-seller-surplus-model.md) carries the same equation after it. Per component:

$$\Delta_k(t) = \Delta_k(0) + \gamma_k t$$

**Seller investment and drift are one mechanism with opposite signs.** Discovery lowers a component's gap and rotates the vector away from that component. Absent maintenance the gap rebuilds at $\gamma_k$ and the vector rotates back. A deal is therefore a path through the composition space rather than a point in it, and the same is true of an account after signature.

| Rate | What drives it | Where it is already named |
|---|---|---|
| $\gamma_{search}$ | New entrants, category redefinition | Nowhere |
| $\gamma_{consensus}$ | Stakeholder turnover, reorganization | Nowhere |
| $\gamma_{implementation}$ | Staff turnover, workflow change, systems installed unseen | [04-seller-surplus-model.md](./04-seller-surplus-model.md) section 7.2 |

**The field consequence sits in the consensus row.** A champion leaving is $\gamma_{consensus}$ arriving all at once. The alignment that stakeholder held is gone, the deal rotates back toward consensus-dominant, and it can leave the viable zone without any change in the product, the price or the technical work. That event is the most common way an enterprise deal dies.

**The same rotation runs at the level of a category.** An emerging category carries high search and high implementation cost and routes search-led or composed. As industry-wide education completes, search cost collapses and the buyer's risk concentrates on deployment, so the category rotates implementation-led. As integrations standardize and switching costs fall, every component drops below the boundary and the category commoditizes to Turnkey, at which point the apparatus retires. The second and third transitions are the pair sellers miss, and they miss the third more often, because nothing external prompts a re-score.

This also generalizes Axiom II's trajectory. $D(t)$ is written as a scalar, the distance between transaction cost and opportunity cost. Under per-component drift it is a path with a direction, and the direction says which instrument would arrest it.

### 5.3 What this demotes

The reduced form $y = a\hat{\Delta}_A^2 + c$ collapses the vector to a scalar, and [02-mathematical-models.md](./02-mathematical-models.md) section 1.4 already concedes that it "produces a number, not a diagnosis." Under this model the concession is heavier, because direction is the quantity that selects the motion and the reduced form destroys it. The form keeps its one job, which is showing why cutting price cannot offset a wide gap. It stops being a representation of transaction cost.

**Nothing weights one side of a gap against the other.** $I_{seller}$ and $I_{buyer}$ are summed unweighted, and $\beta$ elsewhere in this framework is the organizational complexity exponent in $F_{consensus} = \alpha N^{\beta}(1 + \text{Var}(I_i))$, which belongs to the consensus base cost and has nothing to do with asymmetry. Any future weighting between two sides of a gap would be a parameter of the implementation component alone, because that is the only component whose pair has two distinguishable sides.

---

## 6. What follows for the seller's market

A seller who runs only short-vector tactics can transact only with short-vector buyers. Buyers whose deals carry a long vector are not lost somewhere in the funnel. They were never reachable, because the motion offered no instrument for the cost that was blocking them.

Addressable market is therefore a property of the motion rather than of the product, and [05-governance-forms.md](./05-governance-forms.md) section 4 carries that argument and its three consequences.

---

## 7. A second symptom of under-frictioning

Axiom II names under-frictioning as the failure where asset specificity exceeds the friction deployed, and gives one symptom: the buyer declines to transact and builds internally.

There is a second symptom, and it appears after signature rather than before. A buyer whose implementation uncertainty was never resolved can still transact when the commercial path is easy enough. They buy, they fail to deploy, and they leave. The cause is identical. The symptom lands in retention rather than in win rate, which is why it is usually diagnosed as a product problem or an onboarding problem.

Both symptoms belong to the same failure, and Axiom II names both.

---

## 8. Why sellers choose the wrong region

The seller picks the motion, and the seller has a reason to pick the short-vector one that has nothing to do with the deal in front of them. Short-vector tactics carry lower cost of sale, and lower cost of sale reads well on an income statement.

**This is an Axiom II failure inside the seller's own organization.** The party choosing the motion holds no stake in the outcome the choice produces. A representative compensated on new bookings, or a leader measured on sales efficiency, is an adjudicator of motion selection with no exposure to the churn that follows a misread vector. Axiom II predicts exactly this: an adjudicator without a stake drifts from adjudication toward extraction, and here the extraction runs against the seller's own future revenue.

The remedy is vested compensation ([05-governance-forms.md](./05-governance-forms.md) section 5), which ties compensation to outcomes that survive past signature. It is usually read as protection against poor Structural deal execution. It is also the instrument that governs motion selection, and that is the wider of the two claims.

---

## 9. What this does not settle

- **The consensus region has no instrument file.** The [Deal Triage Calculator](../../practice/deal-triage-calculator.md) says so out loud when a deal routes there. Building the instrument set is the open work, and naming the region further before that would produce a label with nothing behind it.
- **Whether direction is vendor-relative.** An incumbent defending a renewal and a challenger attacking it face the same opportunity with different vectors, because the incumbent's implementation cost is already sunk. The instrument scores the deal rather than a seat, which is a decision rather than an oversight: a seat-scored instrument owes the reader an account of how each seat wins, and that account does not exist yet. Until it does, an incumbent scoring a renewal will read implementation-light for a reason the counts cannot see, and should say so on the sheet rather than trusting the routing.
- **Where the boundary between short and long sits.** The threshold sits at half the instrument's range and nothing but convention puts it there.
- **Whether the count bands are the right shape.** The instrument counts named things, which fixes the ordinal problem, and then converts counts to component scores through bands that are chosen rather than fitted. The counts are observations. The bands are not.
- **Whether the three drift rates behave as one mechanism.** $\gamma_{consensus}$ is the only one with a discrete field event attached, namely a departed stakeholder. The other two are asserted to be continuous and nothing tests that.
- **Whether $a$ is anywhere near 2.25.** The coefficient has stated units, which makes it checkable rather than correct. Section 6 of [02-mathematical-models.md](./02-mathematical-models.md) says what data would settle it.

---

## 10. The incumbent vocabulary

Everyone arriving here knows what Product-Led Growth means. This section says where it and its neighbours land in the space above, and where they mislead. Nothing here is used to decide anything.

<!-- vale TCG.RetiredTerms = NO -->
<!--
  The retired-term rule is off for the rest of this section. Naming retired
  terms is what the section is for, so the rule would fire on every row of the
  map and the fix would be to stop doing the job. This is the one place in the
  repository where an old name is the subject rather than a mistake.
-->

**The incumbent names do not form a set.** Product-Led Growth is named after the instrument, Sales-Led Growth after the actor, and Implementation-Led Growth after a cost component. Only the third names a cost, which is why the obvious extensions, Search-Led and Consensus-Led, had nowhere to sit. This framework names every motion after the cost it spends to reduce, because that is what the theory says a motion is. The set then closes: three costs, three motions, plus one reading for the case where no cost is large enough to warrant instruments.

| This framework | Closest incumbent term | Relationship |
|---|---|---|
| **Turnkey** | Product-Led Growth | Overlapping, not equal. Turnkey is a reading on one deal: its vector is short. Product-Led is a company-level strategy: the product is the primary acquisition instrument. They coincide often enough to be confused and come apart in the case that matters most, a Product-Led company moving upmarket. Security review arrives, the committee grows, integration deepens, the level crosses the boundary, and the deals are Structural while the company still calls its motion Product-Led. The deals rotated into a different region and the instrument set did not follow. Keeping the level as a per-deal reading is what makes that transition visible while it is happening. |
| **Search-led** | Sales-Led Growth, category creation, evangelical selling | Search-led is wider. It also covers channel and trial, which Sales-Led does not. |
| **Consensus-led** | No established term. Nearest neighbours are MEDDPICC-style qualification and multithreading | The incumbent practice exists as qualification discipline rather than as a named motion. |
| **Implementation-led** | Implementation-Led Growth, forward-deployed engineering, solution selling | Direct. This framework was called ILG before the theory outgrew the name. Older analyses still use it for the whole framework. |
| **Composed** | No established term | The industry treats motions as exclusive, so the case where two costs are comparable has no name. |

**Product-Led and Sales-Led are instruments for the same cost.** The industry treats them as opposites. Under section 2.1 they are two of the three search instruments: Sales-Led resolves a buyer who cannot name the category, Product-Led resolves a buyer who knows the category and cannot verify this particular fit. What separates them in practice is level rather than kind. A trial cannot resolve a six-month integration question, so self-service works where the other two components are also small. Education can run at any level, which is why it survives upmarket and trials often do not. Treating them as rival philosophies produces an argument that cannot resolve, because each side is right about its own blocker.

**What this framework is not competing with.** Go-to-market vocabulary mixes three tiers, and the tiers compose.

| Tier | What it decides | Examples |
|---|---|---|
| **Theory of transaction cost** | Which costs a deal carries, and therefore which instruments can reduce them | This framework |
| **Qualification framework** | What must be true before a deal is called committed | MEDDPICC, BANT |
| **Conversational methodology** | How a perspective gets reframed in the room | Challenger, SPIN |

A team using this framework still needs a qualification standard and a conversational technique. What changes is what the qualification evidence *is*: the economic buyer is confirmed in the Blueprint, the decision criteria are the Red Team's surfaced failure modes, and the champion is tested by whether they commit resources to the MIP. Qualification tells you whether a deal is real. It does not tell you which of three costs is blocking it, and it does not reduce any of them.

**On the missing acronyms.** The motions are written out as search-led, consensus-led and implementation-led. SLG would silently mean two things in one conversation, the field is already crowded with three-letter forms, and the written names match the words the Deal Triage Calculator returns, so nothing has to be translated between the reading and the motion.

<!-- vale TCG.RetiredTerms = YES -->

---

## Related

- [00-tcg-constitution.md](./00-tcg-constitution.md) — Axiom I supplies both quantities and Axiom III supplies the amplification derived here.
- [05-governance-forms.md](./05-governance-forms.md) — The third quantity, frequency, and what the seller's market follows from.
- [02-mathematical-models.md](./02-mathematical-models.md) — Functional forms for the components.
- [06-calibration.md](./06-calibration.md) — Provenance of every number named here: the boundary, the dominance threshold, the bands.
- [04-seller-surplus-model.md](./04-seller-surplus-model.md) — The seller's side of the transaction, which section 8 depends on.
- [transaction-cost-economics.md](../02-research/transaction-cost-economics.md) — Coase and Williamson, the source of the decomposition.
- [channel-collapse.md](../02-research/channel-collapse.md) — The reachability blocker, which most frameworks do not name as a cost.
- [Deal Triage Calculator](../../practice/deal-triage-calculator.md) — The instrument that emits both quantities, and the conditions under which the implementation-led region should be declined.
- [models/README.md](../../models/README.md) — Executable forms of the equations referenced here.
