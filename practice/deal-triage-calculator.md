---
title: "The Deal Triage Calculator"
layer: practice
status: active
version: 8.0
operationalizes: [axiom-1, axiom-2, axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# The Deal Triage Calculator

Version: 8.0
Goal: Read each of the three costs against its own two thresholds, so that the motion follows from the deal rather than from a label. Whether any cost keeps the buyer out, and where the sale starts, are Axiom I. Whether anything specific is sunk, and what arrangement holds it, are Axiom III. Frequency decides whether the seller's investment can be paid back at all.

**Canonical Reference:** [TCG Constitution](../theory/01-foundation/00-tcg-constitution.md), Axiom I for the positions and Axiom III for the specific exposure and the gate. The functional forms are [02-mathematical-models.md](../theory/01-foundation/02-mathematical-models.md) section 6. The motions are [01-motions.md](../theory/01-foundation/01-motions.md).

| | |
|---|---|
| **Inputs** | A live deal, and a willingness to count things rather than rate them. |
| **Outputs** | Three positions and their zones, three component gaps, where the sale starts, a specific-exposure reading, a frequency, a governance form, and a routing. |
| **Next step** | See Step 4. |
| **Owner** | AE / pre-sales, with a spot-check on the counts. |

> [!IMPORTANT]
> **This instrument counts. It does not rate.** Every input below is a number of named things, and every number is backed by a list. Earlier versions asked for ratings of 1 to 5, and the models downstream raised those ratings to powers. Exponentiating an ordinal rating is not a defensible operation, because the distance between a 2 and a 3 was never established as equal to the distance between a 4 and a 5. Counts have a true zero and equal intervals, which is what the equations need. Since version 8.0 the counts are never converted to scores or summed: each is read against its own two edges, so there is no common scale to defend. The closing section says what counting does and does not fix.

---

## Step 0: Workflow Maturity Gate

**Before counting anything, classify the buyer's workflow for the specific problem being solved.** You cannot digitize a process nobody has defined, and a count of exception paths means nothing when no path is written down.

| Level | Condition | Evidence | Route |
|---|---|---|---|
| **1. Undefined** | No written process. Steps vary by person. | Ask three people to describe the workflow and get three different answers. | **Stop. Chaos Trap**, *if the product automates the process.* Redirect to consulting or a paid workshop to define the process first. If the product supplies a medium the buyer encodes their own workflow into, an undefined workflow is not a trap. See Gate A. |
| **2. Emergent** | A process exists and is partly written down, but units have diverged and nobody owns the variance. | A written procedure people describe as out of date. | **Conditional.** Continue, but the Blueprint must reconstruct the workflow before the Red Team runs. |
| **3. Codified** | Documented, followed, and exception handling is quantified. | The current procedure, plus volumes for the exception paths. | **Continue.** |

**Level 2 is the level that gets misread.** A buyer at Level 2 can produce a document on request, which reads as Level 3 to anyone who does not check whether the document matches practice. The failure surfaces during implementation as unmapped exception paths, which is the single most common source of post-signature scope expansion. When in doubt, score down.

Workflow maturity is not a friction component. A Level 1 workflow with a legible category and a single decision maker is a Chaos Trap, not a light deal, and no reading of the vector says so. Run this gate on its own evidence.

---

## Step 1: Count the three components

Each component takes one count of a named thing. Write the list, then the number. **A number with no list attached is not a count.**

Each count is read against two edges of its own. Below the self-serve edge the buyer can pay that cost down alone. Above the participation edge the cost keeps the buyer out of the market. Both edges are chosen, placed on the boundaries of the score bands earlier versions used, and [06-calibration.md](../theory/01-foundation/06-calibration.md) records them as chosen.

### 1a. Search

**Count: alternatives the buyer must rule out before they can choose.** Every named vendor, plus "build it internally" as one, plus "do nothing" as one.

$$n_{search} = (\text{named vendors}) + (\text{build}) + (\text{do nothing})$$

| Edge | $n_{search}$ |
|---|---|
| Self-serve, $\tau^{self}$ | 4 |
| Participation, $\tau^{part}$ | 8 |

Up to four alternatives, the buyer rules them out alone. Above eight, the buyer cannot compare them without help it does not have.

**No path to this buyer that you hold today keeps the buyer out.** A buyer who knows the category, can name five vendors, and sits behind a purchasing consortium you have no agreement with is unreachable, and neither education nor a trial touches that cost. Pull it back into range with a channel, or decline. Research is in [channel-collapse.md](../theory/02-research/channel-collapse.md).

> [!WARNING]
> **A buyer who cannot name the category is not a short list. They are kept out.** The alternative set is not small, it is unbounded, because the buyer cannot enumerate what they are choosing between. Treating an unnamed category as a short list is the most common misreading this instrument produces. The route is category definition, which pulls the cost back into range.

**Evidence, four items.** Count how many hold, with a document or a named person behind each: a recognized category name the buyer uses, three or more vendors the buyer can name, published third-party comparison material, and a path from you to this buyer that you hold today.

$$\hat{\Delta}_{search} = 1 - \frac{\text{items evidenced}}{4}$$

### 1b. Consensus

**Count: decision roles that can say no.** Not people who attend. Roles whose objection stops the purchase.

$$n_{consensus} = (\text{individuals with a veto})$$

**Add 1 to the count if a formal procurement process, security review, or board approval is required.** A body is not a person and does not belong in the evidence denominator below, but it holds a veto and it costs time.

| Edge | $n_{consensus}$, with any formal body |
|---|---|
| Self-serve, $\tau^{self}$ | 1 |
| Participation, $\tau^{part}$ | 7 |

One decision role decides alone. Above seven, the coalition does not converge without help.

**Evidence: how many of those roles have a written statement of what they are measured on.**

$$\hat{\Delta}_{consensus} = 1 - \frac{\text{roles with a documented measured objective}}{\text{roles that can say no}}$$

This is a proxy. Axiom III's bargaining gap is the share of decision roles whose occupant has stated their own exposure, and [07-open-questions.md](../theory/01-foundation/07-open-questions.md) item 14 records the difference until the consensus block reads it directly. What a stakeholder says in a room containing the others is not evidence. Stated positions converge under social pressure and measured objectives do not, so a committee where nobody voices dissent is as consistent with suppressed variance as with agreement. [02-mathematical-models.md](../theory/01-foundation/02-mathematical-models.md) section 3.2 carries the argument and [buying-center-dynamics.md](../theory/02-research/buying-center-dynamics.md) the research.

### 1c. Implementation

**Count: three things, summed.**

$$n_{impl} = (\text{integration points}) + (\text{workflows that change}) + (\text{undocumented exception paths})$$

An integration point is one system that must exchange data with yours. A workflow that changes is one procedure a named group performs differently after go-live. An undocumented exception path is one branch of the workflow with no written handling and no volume attached.

| Edge | $n_{impl}$ |
|---|---|
| Self-serve, $\tau^{self}$ | 2 |
| Participation, $\tau^{part}$ | 11 |

Up to two items, the buyer verifies fit and adapts alone. Above eleven, the buyer cannot bound the delivery risk without help.

**Evidence: how many of those counted items have a written artifact behind them.** A schema, an API document, a procedure with volumes, a security policy. A verbal assurance is not an artifact.

$$\hat{\Delta}_{implementation} = 1 - \frac{\text{items with a written artifact}}{n_{impl}}$$

This is a seller-side reading and it is provisional. It measures $I_{seller}$ only. Once discovery has run far enough to score the buyer's side, the [Bilateral Asymmetry Scorecard](./asymmetry-scorecard.md) supersedes it, because the implementation pair is the one bilateral pair and half of it is invisible from here.

### 1d. Frequency

**A classification, not a count.** Frequency is how often the same two parties transact. With the specific-exposure reading in Step 2, it selects the governance form and decides whether the seller's investment can be amortized at all. See [05-governance-forms.md](../theory/01-foundation/05-governance-forms.md).

| Reading | Condition | Evidence |
|---|---|---|
| **One-shot** | The transaction completes and neither party has a structural reason to meet again. A migration, a perpetual licence, a fixed-scope build. | No renewal date exists, and nobody on either side can name what a second purchase would be. |
| **Recurrent** | The transaction renews on a cycle and either party can decline at the boundary. | A renewal date, and a named owner of it on each side. |
| **Continuous** | The product sits inside the buyer's operations and leaving is itself a project. | Ask what migrating away would cost them. If nobody can answer, it is continuous. |

**Do not read your own pricing model as the answer.** A product billed annually that the buyer treats as a one-time installation with a maintenance fee is one-shot, whatever the invoice says.

---

## Step 2: Specific exposure

The counts measure how much cost the buyer faces today. None says whether the deal sinks anything that is worth less outside this relationship, and that is what decides the future cost under Axiom III and the arrangement that has to hold it.

Two gates decide whether anything specific is sunk, and whether divergence is counted.

**Gate A: must the product fit a workflow the buyer has already encoded?**

| Answer | Condition | Route |
|---|---|---|
| **No, greenfield** | No encoded workflow exists for this problem. The product creates the practice. | Do not count divergence. It has no reference point. |
| **No, the product absorbs it** | The product ships underspecified on purpose, and the buyer encodes their own workflow inside it without vendor engineering. | Do not count divergence. |
| **Yes** | The buyer runs an encoded workflow the product must fit, extend, or replace. | Count divergence if Gate B fails. |

**Gate B: can the buyer measure the gap themselves, and reverse the decision?** Answer it on every deal. This is CFIR's **Trialability** construct, and it is the Constitution's gate under Axiom III. A trial transfers the fit measurement to the buyer, who is the only party positioned to perform it, and a reversible decision sinks nothing specific. Where that holds, the seller does not need to supply proof before signature and no governance apparatus is needed after it. All three must hold:

- The buyer can run the product against their real work, with their real data, without seller engineering.
- Discovering a bad fit costs them days rather than quarters.
- Walking away strands no committed spend and no migrated data.

If all three hold, nothing specific is sunk and the exposure reading is none. Otherwise read the exposure below.

**Count, where Gate B fails: what the deal sinks that only works here.**

$$n_{exposure} = (\text{integration points}) + (\text{workflows that change}) + (\text{divergent steps})$$

Integration points and changed workflows are the Step 1c counts. Divergent steps are counted only when Gate A answers yes: walk the buyer's procedure and mark each step the product cannot perform as written. Research calls the gap *misfit*, per [process-misfit.md](../theory/02-research/process-misfit.md), and the count operationalizes the CFIR **Compatibility** construct in its workflow sense.

| Reading | Condition |
|---|---|
| **None** | Gate B passes, or $n_{exposure} = 0$ |
| **Specific** | Gate B fails and $n_{exposure} > 0$ |

Divergence is never added to a cost. Earlier versions multiplied the implementation score by it, which let discovery move a reading that was supposed to be fixed. It belongs here, because a workflow that matches nothing the product assumes is exactly what makes an investment worthless outside this deal.

**Who codified the workflow predicts the count.** A workflow codified by a regulator converges across buyers, which is how mature Turnkey categories form. A workflow codified by the buyer diverges from every other buyer, and more so the longer it has been in place. A demonstration reaches two of misfit's six domains, functionality and data. Usability, role, control and organizational culture surface during implementation unless the [Contextual Blueprint](./implementation-motion/01-discovery-contextual-blueprint.md) goes looking for them.

---

## Step 3: Positions

For each cost, its position between its own two edges:

$$r_k = \frac{n_k - \tau^{self}_k}{\tau^{part}_k - \tau^{self}_k}$$

| Position | Zone |
|---|---|
| $r_k \le 0$ | **Self-serve.** The buyer pays this cost down alone. |
| above zero and at most one | **Needs investment.** Bearable, with seller investment. |
| $r_k > 1$ | **Keeps the buyer out.** Pull it back into range first, or decline. |

An unnamed category or a missing channel puts search in the third zone whatever the count.

**Where the sale starts:** the cost with the largest position. Two costs at the same position are run together, and the instrument returns both rather than picking one.

**The positions are never summed.** Each count is compared against its own edges, so three counts of different things need no common scale. The gaps from Step 1 are reported beside the positions and do not move them: they feed the chance of future loss under Axiom III, not today's cost. Re-take the counts at every artifact boundary, because discovery changes what is counted, and the sequence of readings is the record of what it moved.

---

## Step 4: Route

**Overrides first.**

| Condition | Route |
|---|---|
| Step 0 returned Chaos Trap | Stop. Consulting or a paid definition workshop. |
| The buyer asked for a pilot or proof of concept | Implementation-led, whatever was counted. A buyer requesting a pilot is reporting that it cannot verify fit alone, and pilots are governed by the [Red Team Protocol](./implementation-motion/02-validation-red-team-protocol.md). |
| Any cost keeps the buyer out | Name it. Pull it back into range with the instrument for that cost, or decline. No work on the other two reaches it. |

**Then the two readings.**

| | Exposure: none | Exposure: specific |
|---|---|---|
| **Every cost self-serve** | **Turnkey.** Standard terms, published pricing, self-service provisioning. | **Light sale, heavy contract.** The sale is easy and the allocation is not. Agree staging and stop rights before the specific investment is sunk, with the [Mutual Implementation Plan](./implementation-motion/03-closing-mutual-implementation-plan.md). |
| **Some cost needs investment** | **Heavy sale, light contract.** Run the motion where the sale starts, then standard terms hold. | **The motion where the sale starts, with governance.** Where the sale starts at implementation, this is the full chain. |

**The motion where the sale starts:**

| Sale starts at | Motion | Run |
|---|---|---|
| Search | **Search-led** | Commercial teaching, reference architectures, category definition, channel work. No instrument file in this repository. |
| Consensus | **Consensus-led** | Stakeholder mapping from the [Blueprint](./implementation-motion/01-discovery-contextual-blueprint.md), then the [Red Team](./implementation-motion/02-validation-red-team-protocol.md), sized by the [Consensus Friction Calculator](./consensus-friction-calculator.md). No dedicated instrument exists, and a deal routing here is routing to a gap. Say so rather than substituting the implementation chain because it is the one that exists. |
| Implementation | **Implementation-led** | In sequence: [Blueprint](./implementation-motion/01-discovery-contextual-blueprint.md) → [Red Team](./implementation-motion/02-validation-red-team-protocol.md) → [MIP](./implementation-motion/03-closing-mutual-implementation-plan.md) → [Adoption Review](./implementation-motion/04-sustaining-adoption-review.md). |
| A tie | Both, run together | Do not pick one and call it the motion. |

[01-motions.md](../theory/01-foundation/01-motions.md) section 4 specifies each motion.

**Possible over-frictioning.** Implementation needs investment and the exposure reads none. The work is real and nothing about it is specific: deep integration against a standard the vendor already builds to is expensive work, not uncertain work. Run the implementation instruments that pay down today's cost and skip the governance apparatus.

### The governance form

Read it off the exposure and the frequency together. It answers a different question from the routing above: what shape the arrangement should take after signature.

| Exposure | Frequency | Form | What to write |
|---|---|---|---|
| None | Any | **Market** | Standard terms, published pricing, no relationship apparatus. |
| Specific | One-shot | **Trilateral** | Safeguards from outside the pair. Fixed scope, external acceptance criteria, escrow or arbitration, a named third party who adjudicates. |
| Specific | Recurrent | **Bilateral** | A [Mutual Implementation Plan](./implementation-motion/03-closing-mutual-implementation-plan.md). Mutual commitments, staged gates, symmetric consequence. |
| Specific | Continuous | **Bilateral, watching for unified** | The MIP still applies. Also ask what the buyer's build alternative now costs, because rising specificity on a continuous relationship eventually makes integrating beat any contract you can write. |

> [!WARNING]
> **A specific one-shot deal is the case to escalate.** Something will be sunk and there is nothing to amortize the seller's investment over. Do not resolve it by running a lighter version of the motion, which produces the unallocated failure with the cost already sunk. Either find a structure that makes the relationship recurrent, which changes the governance form rather than making an expensive one cheaper, or decline.

### When to decline the implementation-led region

Deploying the implementation chain when the deal cannot repay it destroys margin. Any one condition below routes the deal away from the implementation instruments or out of the pipeline. The first three are properties of the deal. The last three are properties of the environment or the seller, and they are the ones teams skip when auditing their own boundary.

| Condition | Why it fails | Route |
|---|---|---|
| **No operational baseline** (Step 0 Level 1) | Mapping a nonexistent workflow produces fabricated alignment, and the Red Team stress-tests fiction. | Decline. Advisory work to establish the process, then re-qualify. |
| **The deal cannot amortize the apparatus** (specific one-shot) | Pre-sale engineering has nothing to recover against. [04-seller-surplus-model.md](../theory/01-foundation/04-seller-surplus-model.md) section 7 shows the spend amortizes across renewals, so a first-year margin test is right where retention is weak and too strict where it holds. | Restructure as recurrent, or decline. |
| **The category has commoditized** | Standardized integrations have pulled every cost into the self-serve zone. | Re-count, run Turnkey, retire the pre-sale engineering. |
| **The specification is externally fixed** | A regulatory mandate or rigid request for proposal has removed the discovery surplus. | Compete on unit economics, service levels, and delivery credibility. |
| **The buyer lacks implementation capacity** | The MIP assigns tasks to engineering staff the buyer does not have. | Defer until the capacity exists, or contract as a managed service. |
| **The seller lacks delivery depth** | A Red Team run without technical competence produces false confidence and downstream failure. | Stop the motion until the delivery capability is real. |

---

## Why counts, and what counts do not fix

**What the change buys.** The models raise their inputs to powers, and $F_{consensus} = \alpha N^{\beta}(1 + \text{Var}(I_i))$ needs $N$ to be a count for $N^{1.35}$ to mean anything. A count of stakeholders is one. Since version 8.0 the counts are not converted to scores at all. Each is compared against two edges on its own scale, which is the only operation the positions need.

**What it does not buy: honesty.** A count can be manipulated, and anyone who wants a deal routed to a velocity motion can undercount every component. Three things make that harder than manipulating a rating, and none makes it impossible. Every count is a list, so a disputed count is an argument about whether a named system is on it, which one party can lose. The counts are re-taken after the fact at the [Adoption Review](./implementation-motion/04-sustaining-adoption-review.md), and the variance is recorded. And both directions cost something: inflating routes the deal into heavier apparatus, deflating produces the post-signature failure Axiom III names, which vested compensation ([05-governance-forms.md](../theory/01-foundation/05-governance-forms.md) section 5) attaches to the representative's own payout.

**What it also does not buy: measurement.** The counts are observations and the edges are not. A position is only as defensible as the two edges behind it, and both are chosen. Read the positions as a comparison between deals in one book, never as a quantity.

---

## Scoring sheet

| Field | Value |
|---|---|
| Workflow maturity (1, 2, 3) | |
| Alternatives to rule out | |
| Category named (yes / no), channel exists today (yes / no) | |
| Search position and zone | |
| Search evidence items (of 4), $\hat{\Delta}_{search}$ | |
| Decision roles that can say no, formal body (yes / no) | |
| Consensus position and zone | |
| Roles with a documented measured objective, $\hat{\Delta}_{consensus}$ | |
| Integration points, workflows that change, undocumented exception paths | |
| Implementation position and zone | |
| Items with a written artifact, $\hat{\Delta}_{implementation}$ | |
| Gate A answer, Gate B answer | |
| Divergent steps | |
| **Exposure** (none / specific), with the count | |
| **Where the sale starts** | |
| **Routing** | |
| Frequency reading | |
| Governance form | |
| Date counted, and by whom | |

Re-count at every artifact boundary and keep the old rows. The sequence of readings is the record of what discovery moved, and a deal whose readings never change is a deal where nothing was learned.

---

## Related

- **Theory:** [TCG Constitution](../theory/01-foundation/00-tcg-constitution.md). Axiom I supplies the thresholds and where the sale starts. Axiom III supplies the specific exposure, the gate and the governance forms.
- **Derivation:** [01-motions.md](../theory/01-foundation/01-motions.md) maps the motions onto where the sale starts.
- **Functional forms:** [02-mathematical-models.md](../theory/01-foundation/02-mathematical-models.md) sections 2.4, 3.1 and 6 consume these counts.
- **Provenance:** [06-calibration.md](../theory/01-foundation/06-calibration.md) records every edge above as chosen.
- **Deeper implementation gap:** [Bilateral Asymmetry Scorecard](./asymmetry-scorecard.md) supersedes this instrument's provisional implementation gap once both halves are scored.
