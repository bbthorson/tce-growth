---
title: "The Bilateral Asymmetry Scorecard"
layer: practice
status: active
version: 3.0
operationalizes: [axiom-2]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# The Bilateral Asymmetry Scorecard

Type: Internal Ops / Deal Desk
Owner: Sales Manager and Rep
Frequency: Weekly forecast call
**Purpose:** To measure the implementation component's gap by counting what neither side has evidence for, and to route the deal to whichever artifact closes the wider half.

- **Theory:** Per Axiom II, the implementation component is amplified by $\hat{\Delta}_{implementation}$, and that gap is bilateral: $\Delta_A = I_{seller} + I_{buyer}$. The gap is a **sum**, not a difference.
- **Rule:** Above 7.0, place a commercial hold. Do not issue pricing into a gap that wide.

> [!IMPORTANT]
> **This instrument measures one component, not the deal.** Axiom II amplifies each friction component by the asymmetry inside its own pair of parties, and three components mean three pairs. Search asymmetry is the buyer against the market. Consensus asymmetry is the buyer's stakeholders against each other. This scorecard measures the third pair, seller against buyer, which is the implementation component and the only bilateral one. Substituting its output for the deal-level gap $\hat{\Delta}_A$ treats one pair's gap as though it governed all three, and it is the substitution that was standard practice before v17.0. The [Deal Triage Calculator](./deal-triage-calculator.md) emits the other two.

> [!IMPORTANT]
> **Version 3.0 counts. Version 2 rated.** Every dimension below used to be rated 1 to 5 on a rubric, and the models downstream raise their inputs to powers, which is not a defensible operation on an ordinal rating. Each dimension is now a pair of counts: how many items are in scope, and how many of those have evidence behind them. The dimension score is derived from the fraction, and the derivation is stated so the output scale is unchanged.

---

## How to score

**Every dimension is two numbers and a list.** Count the items in scope. Count how many carry evidence, meaning a document, a recorded conversation, or a named person who confirmed it. A rep who cannot produce the list has not scored the dimension.

The unevidenced fraction becomes the dimension score on the same 1 to 5 scale the instrument has always emitted:

$$f = 1 - \frac{\text{items evidenced}}{\text{items in scope}}, \qquad \text{score} = 1 + 4f$$

So a fully evidenced dimension scores 1 and a fully unevidenced one scores 5, which is what the old rubric's endpoints meant. **Higher is worse.** A dimension with nothing in scope is not scored 1. It is left blank, because nothing evidenced out of nothing counted is not the same finding as everything evidenced.

---

## Part 1: Seller Ignorance ($I_{seller}$)

What we still do not know about their environment. The [Contextual Blueprint](./implementation-motion/01-discovery-contextual-blueprint.md) is the instrument that reduces this half.

| Dimension | Items in scope | Evidence that counts |
|---|---|---|
| **S1. Technical architecture, data lineage, and security constraints** | Every system that must exchange data with ours, plus every security control that governs the exchange. | A schema, an API document, a data lineage diagram, or the written security policy. A verbal assurance is not evidence. |
| **S2. Operational workflow and exception handling** | Every branch of the workflow, including the exception paths and the manual interventions. | A written procedure for that branch **with a volume attached**. A procedure without volumes covers the happy path and nothing else. |
| **S3. The economic event** | Every event claimed as the driver: an audit, a board mandate, a regulatory date, a financial target. | The event named, dated, and sized, confirmed by the economic buyer in their own words. If nobody has tied it to a date or a number, it is in scope and unevidenced. |
| **S4. The political map** | Every person or team who loses budget, headcount, or operational control if we win. | The person identified by name **and** a containment plan in writing. |

$$I_{seller} = \frac{1}{4}\sum_{k=1}^{4} S_k \qquad I_{seller} \in [1, 5]$$

**S4 is the dimension that gets scored wrong, and it fails in a specific direction.** A rep who has found no casualty records zero items in scope and leaves the dimension blank, which reads as an absence of information rather than as a low score. That is the correct handling. A rep who instead writes "nobody loses anything" and scores 1 has asserted the highest-confidence claim on the card from the weakest evidence available, which is that nobody has mentioned it. In a Structural deal, a change that costs nobody anything is the rarer finding than a casualty nobody has named yet.

**Seller Ignorance score:** ______

---

## Part 2: Buyer Uncertainty ($I_{buyer}$)

What they still do not know about us, the work, or their own exposure. The [Red Team Protocol](./implementation-motion/02-validation-red-team-protocol.md) is the instrument that reduces this half.

| Dimension | Items in scope | Evidence that counts |
|---|---|---|
| **B1. Vendor capability and product limits** | Every capability the buyer expects, including the ones they have assumed rather than asked for. | Demonstrated in a comparable environment, or written into a gap analysis the buyer has signed acknowledging what the product cannot do. Unchallenged sales claims count against, not for. |
| **B2. Adoption and change burden** | Every group whose daily work changes, and every retraining or behavior change required of them. | A sequenced change plan naming that group, with the hours estimated and an owner on their side. |
| **B3. Cost and resource predictability** | Every internal resource commitment the rollout needs: people, hours, infrastructure, and third-party work. | A named owner and a fixed commitment. A budget line with no named owner is in scope and unevidenced. |
| **B4. Price of failure** | Every cost of inaction the business case rests on. | Quantified in currency **and stated back to us by the buyer**. If we said it to them, it is unevidenced. |

$$I_{buyer} = \frac{1}{4}\sum_{k=1}^{4} B_k \qquad I_{buyer} \in [1, 5]$$

**Buyer Uncertainty score:** ______

---

## Part 3: The gap

$$\Delta_A = I_{seller} + I_{buyer} \qquad \Delta_A \in [2, 10]$$

**Total gap:** ______

The sum is deliberate and it corrects a documented error. An earlier version computed the gap as the absolute difference between the two halves, which contradicted Axiom II and produced a specific false negative: a deal where both sides were equally blind scored as symmetric and therefore forecastable, when it was the most dangerous deal on the board. The sum is the headline metric. The balance between the halves is still used, for routing rather than for risk.

### Risk bands

| $\Delta_A$ | Classification | What it means | Required action |
|---|---|---|---|
| **2.0 to 4.0** | Low | Low technical and political risk. Standard procurement path is viable. Often a Turnkey profile. | Proceed. Lightweight MIP is sufficient. Confirm against the [Deal Triage Calculator](./deal-triage-calculator.md) that the implementation instruments are warranted at all. |
| **4.0 to 7.0** | Moderate | Real gaps exist that will surface during deployment rather than before it. | Run an explicit Blueprint alignment phase. Hold final pricing until S2 and B3 are each at 2 or below. |
| **7.0 to 10.0** | High | Structural profile with severe stall and post-signature failure risk. | Commercial hold. Red Team architectural audit and workflow discovery before any contract terms are issued. |

### Routing: which half is wider

The sum sets the risk. The balance sets the next action.

- **$I_{seller}$ exceeds $I_{buyer}$ by 1.0 or more.** We are flying blind. Return to the Blueprint. Do not run a Red Team on an environment we have not mapped, because the workshop will surface our ignorance rather than their risk.
- **$I_{buyer}$ exceeds $I_{seller}$ by 1.0 or more.** They are working from an imagined version of the product. Return to the Red Team. Pricing into this imbalance produces a signature followed by a churn.
- **Within 1.0 of each other and both high.** The most dangerous state on the card, and the one the old difference-based scale scored as healthy. Both sides are guessing. Run Blueprint and Red Team in sequence before forecasting.

### Feeding the equations

The raw gap on $[2, 10]$ does not substitute directly into the cost equations. Normalize first:

$$\hat{\Delta}_{implementation} = \frac{\Delta_A - 2}{8}, \qquad \hat{\Delta}_{implementation} \in [0, 1]$$

Use the raw score for the bands above. Use the normalized value as the implementation component's amplifier in $F_{effective}$, and as $x_0$ in the [Milestone Valuation Model](./milestone-valuation-model.md), whose gates resolve implementation uncertainty specifically. See [03-mathematical-models.md](../theory/01-foundation/03-mathematical-models.md) sections 1.5 and 2.4.

**The normalized gap is the mean of the two unevidenced fractions.** Substituting $S_k = 1 + 4f_k$ through both halves:

$$\hat{\Delta}_{implementation} = \frac{\bar{f}_{seller} + \bar{f}_{buyer}}{2}$$

The whole 1-to-5 presentation cancels. A deal where the seller has evidence for half of what they need and the buyer for a quarter has a normalized gap of 0.625, and that number is a share of unevidenced items rather than an average of ratings. It is worth checking the arithmetic this way when a score looks wrong: the presentation scale exists for the field bands and carries no information the fractions do not.

**Do not substitute this value for $\hat{\Delta}_A$.** The deal-level gap is the friction-weighted mean of all three components' gaps, and the other two come from the Deal Triage Calculator.

---

## Manager calibration questions

- "Show me the list behind S1. How many systems are in scope, and which of them have a schema on file?"
- "How many exception paths did you count, and how many have volumes attached? A procedure with no volumes is one unevidenced item, not one evidenced one."
- "Who is the casualty? If you counted zero people in scope on S4, what did you look at before concluding that?"
- "Has the buyer said the cost of inaction back to us in their own words, or did we say it to them?"
- "Which half is wider, and which artifact are we running next because of it?"

---

## Related

- [00-tcg-constitution.md](../theory/01-foundation/00-tcg-constitution.md) — Axiom II defines the three component gaps. This card measures the implementation one.
- [03-mathematical-models.md](../theory/01-foundation/03-mathematical-models.md) — Functional forms for $I_{seller}$ and $I_{buyer}$, the normalization rule, and the three-gap table in section 2.4.
- [Deal Triage Calculator](./deal-triage-calculator.md) — Emits the search and consensus gaps, and a provisional implementation gap this card supersedes.
- [Contextual Blueprint](./implementation-motion/01-discovery-contextual-blueprint.md) — Reduces $I_{seller}$.
- [Red Team Protocol](./implementation-motion/02-validation-red-team-protocol.md) — Reduces $I_{buyer}$.
