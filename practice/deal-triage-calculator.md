---
title: "The Deal Triage Calculator"
layer: practice
status: active
version: 7.0
operationalizes: [axiom-1, axiom-2, axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# The Deal Triage Calculator

Version: 7.0
Goal: Emit the three quantities Axioms I and II name, so that the motion follows from the deal rather than from a label. Direction selects the instruments. Level sets how much apparatus the deal can carry. Frequency sets what kind of arrangement can hold it, and whether the apparatus can be paid for at all.

**Canonical Reference:** [TCG Constitution, Axiom I](../theory/01-foundation/00-tcg-constitution.md) for level and direction and [Axiom III](../theory/01-foundation/00-tcg-constitution.md) for the amplification. The derivation is [01-motions.md](../theory/01-foundation/01-motions.md).

| | |
|---|---|
| **Inputs** | A live deal, and a willingness to count things rather than rate them. |
| **Outputs** | Three component scores, three component gaps, a direction, a level, a frequency, a governance form, and a routing. |
| **Next step** | See Step 4. |
| **Owner** | AE / pre-sales, with a spot-check on the counts rather than on the scores. |

> [!IMPORTANT]
> **This instrument counts. It does not rate.** Every input below is a number of named things, and every number is backed by a list. Earlier versions asked for ratings of 1 to 5, and the models downstream raised those ratings to powers. Exponentiating an ordinal rating is not a defensible operation, because the distance between a 2 and a 3 was never established as equal to the distance between a 4 and a 5. Counts have a true zero and equal intervals, which is what the equations need. The closing section says what counting does and does not fix.

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

Each component takes one count of a named thing. Write the list, then the number. **A number with no list attached is not a score.**

### 1a. Search

**Count: alternatives the buyer must rule out before they can choose.** Every named vendor, plus "build it internally" as one, plus "do nothing" as one.

$$n_{search} = (\text{named vendors}) + (\text{build}) + (\text{do nothing})$$

| $n_{search}$ | $F_{search}$ |
|---|---|
| 2 | 1 |
| 3 to 4 | 3 |
| 5 to 7 | 6 |
| 8 or more | 9 |

**Add 2 if no path to this buyer exists that you hold today.** A buyer who knows the category, can name five vendors, and sits behind a purchasing consortium you have no agreement with is unreachable, and neither education nor a trial touches that cost. Research is in [channel-collapse.md](../theory/02-research/channel-collapse.md).

> [!WARNING]
> **A buyer who cannot name the category does not score 2. They score 9.** The alternative set is not small, it is unbounded, because the buyer cannot enumerate what they are choosing between. Treating an unnamed category as a short list is the most common misreading this instrument produces.

**Evidence, four items.** Count how many hold, with a document or a named person behind each: a recognized category name the buyer uses, three or more vendors the buyer can name, published third-party comparison material, and a path from you to this buyer that you hold today.

$$\hat{\Delta}_{search} = 1 - \frac{\text{items evidenced}}{4}$$

### 1b. Consensus

**Count: people who can say no.** Not people who attend. People whose objection stops the purchase.

$$n_{consensus} = (\text{individuals with a veto})$$

| $n_{consensus}$ | $F_{consensus}$ |
|---|---|
| 1 | 1 |
| 2 to 3 | 3 |
| 4 to 6 | 6 |
| 7 or more | 9 |

**Add 1 if a formal procurement process, security review, or board approval is required.** A body is not a person and does not belong in the headcount, but it holds a veto and it costs time.

**Evidence: how many of those people have a written statement of what they are measured on.**

$$\hat{\Delta}_{consensus} = 1 - \frac{\text{people with a documented measured objective}}{n_{consensus}}$$

What a stakeholder says in a room containing the others is not evidence. Stated positions converge under social pressure and measured objectives do not, so a committee where nobody voices dissent is as consistent with suppressed variance as with agreement. [02-mathematical-models.md](../theory/01-foundation/02-mathematical-models.md) section 3.2 carries the argument and [buying-center-dynamics.md](../theory/02-research/buying-center-dynamics.md) the research.

### 1c. Implementation

**Count: three things, summed.**

$$n_{impl} = (\text{integration points}) + (\text{workflows that change}) + (\text{undocumented exception paths})$$

An integration point is one system that must exchange data with yours. A workflow that changes is one procedure a named group performs differently after go-live. An undocumented exception path is one branch of the workflow with no written handling and no volume attached.

| $n_{impl}$ | $F_{implementation}$ |
|---|---|
| 0 to 2 | 1 |
| 3 to 5 | 3 |
| 6 to 10 | 6 |
| 11 or more | 9 |

**Evidence: how many of those counted items have a written artifact behind them.** A schema, an API document, a procedure with volumes, a security policy. A verbal assurance is not an artifact.

$$\hat{\Delta}_{implementation} = 1 - \frac{\text{items with a written artifact}}{n_{impl}}$$

This is a seller-side reading and it is provisional. It measures $I_{seller}$ only. Once discovery has run far enough to score the buyer's side, the [Bilateral Asymmetry Scorecard](./asymmetry-scorecard.md) supersedes it, because the implementation pair is the one bilateral pair and half of it is invisible from here.

### 1d. Frequency

**A classification, not a count, and it does not enter the level.** Frequency is how often the same two parties transact. It selects the governance form and decides whether the apparatus the level calls for can be amortized at all. See [05-governance-forms.md](../theory/01-foundation/05-governance-forms.md).

| Reading | Condition | Evidence |
|---|---|---|
| **One-shot** | The transaction completes and neither party has a structural reason to meet again. A migration, a perpetual licence, a fixed-scope build. | No renewal date exists, and nobody on either side can name what a second purchase would be. |
| **Recurrent** | The transaction renews on a cycle and either party can decline at the boundary. | A renewal date, and a named owner of it on each side. |
| **Continuous** | The product sits inside the buyer's operations and leaving is itself a project. | Ask what migrating away would cost them. If nobody can answer, it is continuous. |

**Do not read your own pricing model as the answer.** A product billed annually that the buyer treats as a one-time installation with a maintenance fee is one-shot, whatever the invoice says.

---

## Step 2: The divergence modifier

The counts measure how *large* the installation is. None measures how far the buyer's workflow sits from the one the product was built around. Those are different quantities, and the second decides whether the installation succeeds. Research calls the gap *misfit*, per [process-misfit.md](../theory/02-research/process-misfit.md). It operationalizes the CFIR **Compatibility** construct in its workflow sense, where Step 0 operationalizes the same construct in its maturity sense.

Two gates decide whether divergence governs at all.

**Gate A: must the product fit a workflow the buyer has already encoded?**

| Answer | Condition | Route |
|---|---|---|
| **No, greenfield** | No encoded workflow exists for this problem. The product creates the practice. | Skip the modifier. Divergence has no reference point. |
| **No, the product absorbs it** | The product ships underspecified on purpose, and the buyer encodes their own workflow inside it without vendor engineering. | Skip the modifier. |
| **Yes** | The buyer runs an encoded workflow the product must fit, extend, or replace. | Continue to Gate B. |

**Gate B: can the buyer measure the gap themselves, and reverse the decision?** This is CFIR's **Trialability** construct. A trial transfers the divergence measurement to the buyer, who is the only party positioned to perform it. Where that transfer works, the seller does not need to supply proof before signature, which is the entire reason the implementation instruments exist. All three must hold:

- The buyer can run the product against their real work, with their real data, without seller engineering.
- Discovering a bad fit costs them days rather than quarters.
- Walking away strands no committed spend and no migrated data.

If all three hold, skip the modifier and route on the vector as counted. Otherwise divergence governs.

**Count: how many steps in the buyer's workflow have no counterpart in the product's assumed workflow.** Walk the procedure and mark each step the product cannot perform as written.

| Divergent steps | Modifier on $F_{implementation}$ |
|---|---|
| 0 | $\times 1.0$ |
| 1 to 2 | $\times 1.2$ |
| 3 to 5 | $\times 1.5$ |
| 6 or more | $\times 2.0$ |

The modifier is capped so that $F_{implementation}$ does not exceed 10.

> [!IMPORTANT]
> **The modifier multiplies one component. It is never added to the level.** Level measures size and divergence measures fit. Adding them would let a large aligned deal and a small misaligned deal produce the same number. Multiplying the implementation component instead is what makes a small misaligned deal read as implementation-dominant, which is the routing it needs.

**Who codified the workflow predicts the count.** A workflow codified by a regulator converges across buyers, which is how mature Turnkey categories form. A workflow codified by the buyer diverges from every other buyer, and more so the longer it has been in place. A demonstration reaches two of misfit's six domains, functionality and data. Usability, role, control and organizational culture surface during implementation unless the [Contextual Blueprint](./implementation-motion/01-discovery-contextual-blueprint.md) goes looking for them.

---

## Step 3: Compute the vector

**Level.** The sum of the three component scores, on base friction, before amplification.

$$\text{Level} = \lVert \mathbf{F} \rVert_1 = F_{search} + F_{consensus} + F_{implementation} \qquad \in [0, 30]$$

| Level | Class | What it means |
|---|---|---|
| 0 to 14 | **Turnkey** | The deal cannot carry heavy apparatus. Blueprints and gate structures cost more than they save. |
| 15 to 30 | **Structural** | The deal can carry apparatus, and $F_{deployed} \sim k$ requires that it does. |

The threshold sits at half the range and carries no empirical support. [06-calibration.md](../theory/01-foundation/06-calibration.md) records it as chosen.

**Direction.** The share of *effective* cost each component carries, after each is amplified by its own gap.

$$\hat{F}_k = \frac{F_k (1 + \hat{\Delta}_k)}{\sum_j F_j (1 + \hat{\Delta}_j)}$$

| Reading | Condition |
|---|---|
| **Search-dominant** | $\hat{F}_{search} \ge 0.50$ |
| **Consensus-dominant** | $\hat{F}_{consensus} \ge 0.50$ |
| **Implementation-dominant** | $\hat{F}_{implementation} \ge 0.50$ |
| **Composed** | No component reaches 0.50 |

**Level uses base friction and direction uses amplified friction, and the difference is the point.** Level is asset specificity, a property of the deal that discovery does not change. Direction is where the unresolved cost currently sits, and it moves every time an artifact closes a gap. Re-run this step at every artifact boundary, because the answer is supposed to change.

---

## Step 4: Route

**Overrides first.**

| Condition | Route |
|---|---|
| Step 0 returned Chaos Trap | Stop. Consulting or a paid definition workshop. |
| The buyer asked for a pilot or proof of concept | Structural, implementation-dominant, whatever was counted. A buyer requesting a pilot is reporting Structural-level perceived risk, and pilots are governed by the [Red Team Protocol](./implementation-motion/02-validation-red-team-protocol.md). |

**Then the vector.**

| Level | Direction | Motion | Run |
|---|---|---|---|
| Turnkey | Not evaluated | **Turnkey** | Standard terms, published pricing, self-service provisioning. No instrument file: a short vector needs none. |
| Structural | Search-dominant | **Search-led** | Commercial teaching, reference architectures, category definition, channel work. No instrument file in this repository. |
| Structural | Consensus-dominant | **Consensus-led** | Stakeholder mapping from the [Blueprint](./implementation-motion/01-discovery-contextual-blueprint.md), then the [Red Team](./implementation-motion/02-validation-red-team-protocol.md), sized by the [Consensus Friction Calculator](./consensus-friction-calculator.md). No dedicated instrument exists, and a deal routing here is routing to a gap. Say so rather than substituting the implementation chain because it is the one that exists. |
| Structural | Implementation-dominant | **Implementation-led** | In sequence: [Blueprint](./implementation-motion/01-discovery-contextual-blueprint.md) → [Red Team](./implementation-motion/02-validation-red-team-protocol.md) → [MIP](./implementation-motion/03-closing-mutual-implementation-plan.md) → [Adoption Review](./implementation-motion/04-sustaining-adoption-review.md). |
| Structural | No component at 0.50 | **Composed** | The top two instrument sets in proportion, heaviest first. Do not pick one and call it the motion. |

The five names in the Motion column are the words this instrument returns, and [01-motions.md](../theory/01-foundation/01-motions.md) section 4 specifies each region.

**Hidden Structural deal.** A Turnkey level that reads implementation-dominant after a divergence modifier of 1.5 or more is a Structural deal wearing Turnkey clothes. Every count is low and the workflow underneath matches nothing the product assumes. Route to the implementation instruments anyway and record why. This is Axiom II's under-frictioned failure mode, and it is the one the level alone cannot see.

**Possible over-frictioning.** A Structural level that reads implementation-dominant with a divergence count of zero is large but aligned. Deep integration against a standard the vendor already builds to is expensive work, not uncertain work. Run the implementation instruments and confirm the full chain earns its cost.

### The governance form

Read it off level and frequency together. It answers a different question from the routing above: what shape the arrangement should take after signature.

| Level | Frequency | Form | What to write |
|---|---|---|---|
| Turnkey | Any | **Market** | Standard terms, published pricing, no relationship apparatus. |
| Structural | One-shot | **Trilateral** | Safeguards from outside the pair. Fixed scope, external acceptance criteria, escrow or arbitration, a named third party who adjudicates. |
| Structural | Recurrent | **Bilateral** | A [Mutual Implementation Plan](./implementation-motion/03-closing-mutual-implementation-plan.md). Mutual commitments, staged gates, symmetric consequence. |
| Structural | Continuous | **Bilateral, watching for unified** | The MIP still applies. Also ask what the buyer's build alternative now costs, because rising specificity on a continuous relationship eventually makes integrating beat any contract you can write. |

> [!WARNING]
> **A Structural one-shot deal is the case to escalate.** The level says it needs the full instrument chain and the frequency says there is nothing to amortize that chain over. Do not resolve it by running a lighter version of the motion, which produces the under-frictioned failure with the cost already sunk. Either find a structure that makes the relationship recurrent, which changes the governance form rather than making an expensive one cheaper, or decline.

### When to decline the implementation-led region

Deploying the implementation chain when the deal cannot repay it destroys margin. Any one condition below routes the deal away from the implementation instruments or out of the pipeline. The first three are properties of the deal. The last three are properties of the environment or the seller, and they are the ones teams skip when auditing their own boundary.

| Condition | Why it fails | Route |
|---|---|---|
| **No operational baseline** (Step 0 Level 1) | Mapping a nonexistent workflow produces fabricated alignment, and the Red Team stress-tests fiction. | Decline. Advisory work to establish the process, then re-qualify. |
| **The deal cannot amortize the apparatus** (Structural one-shot) | Pre-sale engineering has nothing to recover against. [04-seller-surplus-model.md](../theory/01-foundation/04-seller-surplus-model.md) section 7 shows the spend amortizes across renewals, so a first-year margin test is right where retention is weak and too strict where it holds. | Restructure as recurrent, or decline. |
| **The category has commoditized** | Standardized integrations have pushed the level below the boundary. | Re-score, run Turnkey, retire the pre-sale engineering. |
| **The specification is externally fixed** | A regulatory mandate or rigid request for proposal has removed the discovery surplus. | Compete on unit economics, service levels, and delivery credibility. |
| **The buyer lacks implementation capacity** | The MIP assigns tasks to engineering staff the buyer does not have. | Defer until the capacity exists, or contract as a managed service. |
| **The seller lacks delivery depth** | A Red Team run without technical competence produces false confidence and downstream failure. | Stop the motion until the delivery capability is real. |

---

## Why counts, and what counts do not fix

**What the change buys.** The models raise their inputs to powers, and $F_{consensus} = \alpha N^{\beta}(1 + \text{Var}(I_i))$ needs $N$ to be a count for $N^{1.35}$ to mean anything. A count of stakeholders is one. The bands above then convert counts to component scores on one common scale, because three counts of different things cannot be summed directly, and the band edges are chosen rather than fitted.

**What it does not buy: honesty.** A count can be manipulated, and anyone who wants a deal routed to a velocity motion can undercount every component. Three things make that harder than manipulating a rating, and none makes it impossible. Every count is a list, so a disputed count is an argument about whether a named system is on it, which one party can lose. The counts are re-taken after the fact at the [Adoption Review](./implementation-motion/04-sustaining-adoption-review.md), and the variance is recorded. And both directions cost something: inflating routes the deal into heavier apparatus, deflating produces the post-signature failure Axiom II names, which vested compensation ([05-governance-forms.md](../theory/01-foundation/05-governance-forms.md) section 5) attaches to the representative's own payout.

**What it also does not buy: measurement.** These are counts of real things converted to scores by chosen bands. Read the level as a comparison between deals in one book, never as a quantity.

---

## Scoring sheet

| Field | Value |
|---|---|
| Workflow maturity (1, 2, 3) | |
| Alternatives to rule out | |
| Channel exists today (yes / no) | |
| $F_{search}$ | |
| Search evidence items (of 4) | |
| $\hat{\Delta}_{search}$ | |
| People who can say no | |
| Formal procurement or board required (yes / no) | |
| $F_{consensus}$ | |
| Of those people, how many have a documented measured objective | |
| $\hat{\Delta}_{consensus}$ | |
| Integration points | |
| Workflows that change | |
| Undocumented exception paths | |
| $n_{impl}$ | |
| $F_{implementation}$ before modifier | |
| Of those items, how many have a written artifact | |
| $\hat{\Delta}_{implementation}$ | |
| Gate A answer | |
| Gate B answer | |
| Divergent steps | |
| $F_{implementation}$ after modifier | |
| **Level** | |
| **Direction** | |
| **Routing** | |
| Frequency reading | |
| Governance form | |
| Date scored, and by whom | |

Re-score at every artifact boundary and keep the old rows. The sequence of directions is the record of what discovery moved, and a deal whose direction never changes is a deal where nothing was learned.

---

## Related

- **Theory:** [TCG Constitution, Axiom I](../theory/01-foundation/00-tcg-constitution.md) supplies level and direction. [Axiom III](../theory/01-foundation/00-tcg-constitution.md) supplies the per-component amplification this instrument feeds.
- **Derivation:** [01-motions.md](../theory/01-foundation/01-motions.md) is why the instrument emits a vector rather than a label, and maps the named motions onto regions of the vector space.
- **Functional forms:** [02-mathematical-models.md](../theory/01-foundation/02-mathematical-models.md) sections 2.4 and 3.1 consume these counts.
- **Provenance:** [06-calibration.md](../theory/01-foundation/06-calibration.md) records every band and threshold above as chosen.
- **Deeper implementation gap:** [Bilateral Asymmetry Scorecard](./asymmetry-scorecard.md) supersedes this instrument's provisional implementation gap once both halves are scored.
