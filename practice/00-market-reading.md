---
title: "The Market Reading"
layer: practice
status: active
version: 1.0
operationalizes: [axiom-1, axiom-2]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# The Market Reading

Version: 1.0
Goal: Read a buyer population before any buyer is met. Emit the direction and level of its cost vector, the seller's unfilled fraction, the cost to serve by component, and one of pursue, restructure or decline. The motion an organization builds follows from this reading, and not from the motion that worked for a seller in a different market.

**Canonical reference:** [Constitution](../theory/01-foundation/00-tcg-constitution.md), Axiom I at the market level, the definitions of market and workflow, and the cost-to-serve and amortizability corollaries. The derivation is [08-from-axioms-to-instruments.md](../theory/01-foundation/08-from-axioms-to-instruments.md) section 2.1.

| | |
|---|---|
| **Inputs** | The reference workflow the product encodes, with each touchpoint typed. Whatever the seller can source about the buyer population. |
| **Outputs** | A twelve-row ledger with a source and fill status on every row, the buyer vector's level and direction, the unfilled fraction, missing capabilities by component, and pursue, restructure or decline. |
| **Next step** | Pursue: run the deal reading on the first buyer and feed its counts back here. Restructure: build or partner for the missing capability, then re-read. Decline: record why, and re-read when an adjacent market fills the ledger. |
| **Owner** | Whoever chooses the motion. A founder, a chief revenue officer, or the person about to hire for one. |

> [!IMPORTANT]
> **This instrument counts and it cites.** Every row is a number of named things, and every row carries the source that supplied it and one of three fill statuses. A row without a source is not filled. The reading is built from scratch on Constitution 3.0 and inherits nothing from the deal-level instruments except the count-to-score bands, which [06-calibration.md](../theory/01-foundation/06-calibration.md) declares as chosen.

---

## Step 0: Name the workflow

Write the reference workflow the product encodes, one row per step. Mark each step as internal, performed by the product alone, or as a touchpoint where the product meets the buyer's system of record, and type every touchpoint.

| Step | Internal or touchpoint | Touchpoint type | Role that performs it at the buyer | System touched |
|---|---|---|---|---|
| | | Enrollment, supplementation, writeback, foundational sync, or shared context | | |

The five types hold in any vertical and [integration-touchpoints.md](../theory/02-research/integration-touchpoints.md) carries them. A seller who cannot fill this table stops here. A product is an encoded reference workflow, and a product that cannot name its workflow has not chosen its market, which is Axiom II's corollary applied before selling begins. This table is also the spine every later ledger hangs on, so the time spent here is not spent again.

---

## Step 1: Define the population

A market is the buyers who call a problem by one name. The population this reading covers is narrower: the buyers running a recognizable variant of the workflow in Step 0. Name them, and name who codified the workflow.

| Question | Answer |
|---|---|
| Who runs a variant of this workflow | |
| Who codified it: a regulator, an industry standard, or each buyer for itself | |

Codification by a regulator converges the population and codification by each buyer fragments it, and the difference shows up in Step 2's enforcement rows. This step names a population and not a size. A market sized without a named motion measures the intersection of who needs the product with who the current motion can reach, and reports the first number.

---

## Step 2: Fill the ledger

Twelve rows. Each carries a count, the source that supplied it, and a fill status.

| Status | Meaning |
|---|---|
| **Known** | A named source supplied the count: a document, a dataset, a vendor program's own records, or the seller's deal readings in this population. |
| **Inferred** | The seller reasoned the count from the workflow, the touchpoint types or an adjacent market, and no source in this population confirms it. |
| **Unknown** | Nothing supplied it. |

| Row | Component | What to count | Source | Fill |
|---|---|---|---|---|
| S1 | Search | Whether buyers use a category name for the problem, and which | | |
| S2 | Search | Alternatives a typical buyer enumerates: named vendors, plus build, plus do nothing | | |
| S3 | Search | Whether published material lets a buyer compare those alternatives | | |
| S4 | Search | Whether this seller holds a path to the population today: a vendor program, a marketplace, a purchasing consortium, a channel | | |
| B1 | Bargaining | Seats the reference workflow carries at a typical buyer | | |
| B2 | Bargaining | Whether a formal body sits over them: procurement, security review, a committee | | |
| E1 | Enforcement | Touchpoints, counted by type | | |
| E2 | Enforcement | Procedures a typical buyer changes at go-live | | |
| E3 | Enforcement | Undocumented exception paths a typical buyer carries | | |
| E4 | Enforcement | Steps in a typical buyer's version with no counterpart in the reference | | |
| E5 | Enforcement | Who codified the workflow, from Step 1 | | |
| F1 | Frequency | The population's typical reading: one-shot, recurrent or continuous | | |

**Deriving B1 before any buyer is met.** The seats that police a touchpoint follow its type. Writeback brings whoever owns the record and whoever polices it, in a health system the clinical informatics and compliance seats. Enrollment brings whoever owns the operation the trigger sits in. Foundational sync brings whoever owns master data. Shared context brings security. Add whoever pays. A seat list derived this way is Inferred until deal readings confirm it, and the derivation is what lets the row be filled at all before the first conversation.

**Converting counts to scores.** The bands are the ones [06-calibration.md](../theory/01-foundation/06-calibration.md) section 3.2 declares, and they are chosen rather than fitted.

| Component | Count | Score |
|---|---|---|
| Search, from S2 | 2 alternatives, 3 to 4, 5 to 7, 8 or more | 1, 3, 6, 9 |
| Search, from S1 | Buyers cannot name the problem | 9, because the alternative set is unbounded |
| Search, from S4 | No path from this seller to the population | Add 2 |
| Bargaining, from B1 | 1 seat, 2 to 3, 4 to 6, 7 or more | 1, 3, 6, 9 |
| Bargaining, from B2 | A formal body sits over the seats | Add 1 |
| Enforcement, from E1 + E2 + E3 | 0 to 2 items, 3 to 5, 6 to 10, 11 or more | 1, 3, 6, 9 |
| Enforcement, from E4 | 0 divergent steps, 1 to 2, 3 to 5, 6 or more | Multiply by 1.0, 1.2, 1.5, 2.0, capped at 10 |

Where E4 is Unknown, apply no modifier and say so on the sheet. A modifier applied to a guessed count is a guess dressed as a measurement.

---

## Step 3: The buyer vector

**Level.** The three scores summed on base friction, on 0 to 30. Fifteen and above is a Structural population, one whose deals can carry apparatus and by Axiom II must. Below fifteen is Turnkey, and the motion is standard terms and self-service, whatever else this reading says.

**Direction.** Each component's share of the level. The population is search-dominant, bargaining-dominant or enforcement-dominant when one share reaches one half, and Composed when none does.

At the market level the direction is read on base friction with no amplification, and the reason matters. Amplification is the buyer's uncertainty about their own outcome, read per deal. The seller's ignorance of the population is the seller's cost, and Step 4 carries it. The deal reading rotates this direction as each buyer's gaps are read, and a book of deal readings whose direction disagrees with this one is evidence against this one.

[`models/tcg_models.py`](../models/tcg_models.py) computes the vector from the three scores. Pass the three component gaps as zero to obtain the market-level direction.

---

## Step 4: The unfilled fraction

$$\text{unfilled} = \frac{\text{rows Inferred} + \text{rows Unknown}}{12}$$

An Inferred row counts as unfilled because a seller's inference is the thing a deal reading exists to test. The fraction is reported and not thresholded. Nothing yet says where the line sits, and [06-calibration.md](../theory/01-foundation/06-calibration.md) records the row count as chosen.

Two readings follow from it. **Trust.** The vector in Step 3 is as good as the rows behind it, and a direction read from eight Inferred rows is a hypothesis. **Price.** A seller whose ledger is thin cannot close a buyer's enforcement gap cheaply, because the seller's own ignorance is half of it, and is pushed onto price and risk transfer until the ledger fills. That is why an entrant prices below an entrenched competitor, per [04-seller-surplus-model.md](../theory/01-foundation/04-seller-surplus-model.md) section 7.5, and the unfilled fraction is the number that says by how much for how long. The floor is twelve of twelve: a seller with an empty ledger has no reading to act on and should not be in the market.

---

## Step 5: Cost to serve

Take the component the direction points at, or the top two when the population is Composed. For each, walk the four activities below Read in the grid of [08-from-axioms-to-instruments.md](../theory/01-foundation/08-from-axioms-to-instruments.md) section 4 and count the ones the seller's organization cannot perform today. A capability counts as present when a named person or team does it now, not when someone could.

| Component | Map | Test | Stage | Maintain | Missing, 0 to 4 |
|---|---|---|---|---|---|
| Search | Define what the buyer chooses between | Produce proof that travels without the seller | A path with a stake, or a trial where specificity is low | Refresh the proof as the category drifts | |
| Bargaining | Map each seat's exposure, one to one | Collect positions apart, then hear them together | Written decision criteria and sequence | Re-read seats at every occupant change | |
| Enforcement | Map the buyer's environment step by step | Prove capability in their environment at the seller's cost | Gate mutual commitments with a right to stop | Re-map as the environment drifts | |

Cost to serve is a count of capabilities and not a sum of money, because the seller-surplus arithmetic needs contract values this reading does not have. Two organizations with identical missing counts can face different bills, and the count says only which cost each is built to pay.

---

## Step 6: Pursue, restructure or decline

Read F1 against the missing count on the dominant component.

| F1 | Missing capabilities on the dominant component | Reading |
|---|---|---|
| Any | 0 | **Pursue.** The organization is built to pay the cost this population carries. |
| Recurrent or continuous | 1 or more | **Restructure.** Build or partner for the capability, because repetitions can carry the cost of building it. Whether they do is the amortizability question, and [04-seller-surplus-model.md](../theory/01-foundation/04-seller-surplus-model.md) section 7 is where contract value and frequency answer it once the numbers exist. |
| One-shot | 1 or more | **Decline.** Nothing amortizes the apparatus. The same rule declines a Structural one-shot deal, applied to a population. |

**The imitation check.** If the organization has already built a motion and this reading's direction points somewhere else, the reading is not the thing to doubt first. That is the organization-level mis-composed failure the Constitution names: a motion adopted because it worked for a seller in a different market, aimed at a cost this population's buyers do not carry.

**The entrant clause.** A high unfilled fraction does not change pursue to decline. It changes the price at which pursuit is possible, per Step 4, and it says the early deals are the seller's investment in the ledger rather than discounting.

---

## Step 7: Worked scenario, two populations

The instrument earns its place if the vector differs between a saturated population and a novel one selling into the same kind of buyer. Two anonymized EHR-integration markets from HTD's work will fill this section. Every row below is missing until the anonymized integration guide arrives, and the predictions are stated before the data so that the data can contradict them.

| Row | Saturated population | Novel population | Prediction |
|---|---|---|---|
| S1 | [MISSING] | [MISSING] | Saturated has a name buyers use. Novel does not, and scores the maximum. |
| S2 | [MISSING] | [MISSING] | Saturated enumerates many. Novel cannot enumerate, which is the same maximum by a different route. |
| S3 | [MISSING] | [MISSING] | Saturated has comparison material. Whether it lets buyers rank on evidence, or has pooled into unverifiable claims, is register item 27's question. |
| S4 | [MISSING] | [MISSING] | Both depend on the seller's vendor-program status. |
| B1 | [MISSING] | [MISSING] | Same touchpoint types produce the same seats. Writeback brings the record owner and compliance in both. |
| B2 | [MISSING] | [MISSING] | A health system puts a formal body over both. |
| E1 to E4 | [MISSING] | [MISSING] | Saturated has standardized touchpoints and lower divergence. Novel has fewer touchpoints and higher divergence, because no reference has converged. |
| E5 | [MISSING] | [MISSING] | Saturated is codified by convention or standard. Novel is codified by each buyer. |
| F1 | [MISSING] | [MISSING] | Both recurrent. |
| **Direction** | | | Saturated reads bargaining- or enforcement-dominant with a search share held up by pooling. Novel reads search-dominant. |
| **Unfilled fraction** | | | Saturated is lower for a seller already in it. Novel is high for anyone. |

If both populations read the same direction, the instrument is not discriminating and this section says so.

---

## Re-reading: how deal readings feed the ledger

Every deal reading in the population converts rows from Inferred or Unknown to Known, and the ledger is the seller's accumulated insight about the market. Re-run this reading when the unfilled fraction moves, when the book of deal readings disagrees with it, and once a year regardless, because categories drift.

Adjacent markets inherit fill through the spine. A workflow that shares typed touchpoints with one the seller already serves starts with those rows Known, and the share of its ledger inherited that way is the seller's redeployable value, per [04-seller-surplus-model.md](../theory/01-foundation/04-seller-surplus-model.md) section 7.5. The inheritance transfers on the enforcement rows more reliably than on the bargaining rows, because seats and policing are local to the population even when the touchpoint types are not.

---

## What this does not settle

- **No threshold on the unfilled fraction.** It is reported. A line will need data from populations that were entered and populations that were declined.
- **The bands are chosen.** The counts are observations and the scores are not, and the calibration page says so for every band.
- **A typical buyer hides dispersion.** A population whose members carry two different seat structures around the same workflow is two markets, and the typical-buyer counts will average them into one. When the deal readings disagree with each other more than with the market reading, split the population.
- **Cost to serve counts capabilities and not money.** The count says which cost an organization is built to pay. It does not say what building the missing one would cost, and the seller-surplus arithmetic does not run without contract values.
- **Direction is read on base friction.** The population's typical gaps are not read here, on the argument in Step 3, and a population whose buyers are uniformly uncertain about one component would rotate at the first deal reading in a way this instrument cannot anticipate.
- **The scenario is unfilled.** Step 7 carries predictions and no data.

---

## Scoring sheet

| Field | Value |
|---|---|
| Reference workflow named, with touchpoints typed (yes / no) | |
| Population | |
| Who codified the workflow | |
| Rows Known / Inferred / Unknown | |
| $F_{search}$ | |
| $F_{consensus}$ | |
| $F_{implementation}$, modifier applied (yes / no) | |
| **Level** | |
| **Direction** | |
| Unfilled fraction | |
| Missing capabilities on the dominant component | |
| F1 | |
| **Reading: pursue, restructure or decline** | |
| Motion the organization has already built, if any | |
| Date read, and by whom | |

---

## Related

- **Theory:** [Constitution](../theory/01-foundation/00-tcg-constitution.md), Axiom I at the market level, the definitions, and the cost-to-serve and amortizability corollaries under Axioms I and II.
- **Derivation:** [08-from-axioms-to-instruments.md](../theory/01-foundation/08-from-axioms-to-instruments.md) sections 2.1, 4 and 5.
- **The seller's side:** [04-seller-surplus-model.md](../theory/01-foundation/04-seller-surplus-model.md) section 7.5, the market-level information asset and the entrant's pricing.
- **Touchpoint types:** [integration-touchpoints.md](../theory/02-research/integration-touchpoints.md).
- **Provenance of every band:** [06-calibration.md](../theory/01-foundation/06-calibration.md).
- **Executable form:** [`models/tcg_models.py`](../models/tcg_models.py).
