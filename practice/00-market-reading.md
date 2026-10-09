---
title: "The Market Reading"
layer: practice
status: active
version: 2.0
operationalizes: [axiom-1, axiom-2, axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# The Market Reading

Version: 2.0
Goal: Read a buyer population before any buyer is met. Emit each cost's position and zone across that population, where the sale starts, whether the population sinks anything specific, the seller's unfilled fraction, the cost to serve by component, and one of pursue, restructure or decline. The motion an organization builds follows from this reading, and not from the motion that worked for a seller in a different market.

**Canonical reference:** [Constitution](../theory/01-foundation/00-tcg-constitution.md), Axiom I across a population, the definition of workflow, the Turnkey corollary, and the cost-to-serve and pursuit corollaries under Axiom II. The derivation is [08-from-axioms-to-instruments.md](../theory/01-foundation/08-from-axioms-to-instruments.md) section 2.1.

| | |
|---|---|
| **Inputs** | The reference workflow the product encodes, with each touchpoint typed. Whatever the seller can source about the buyer population. |
| **Outputs** | A twelve-row ledger with a source and fill status on every row, three positions and their zones, where the sale starts, an exposure reading, whether the population is Turnkey, the unfilled fraction, missing capabilities by component, and pursue, restructure or decline. |
| **Next step** | Pursue: run the deal reading on the first buyer and feed its counts back here. Restructure: build or partner for the missing capability, then re-read. Decline: record why, and re-read when an adjacent market fills the ledger. |
| **Owner** | Whoever chooses the motion. A founder, a chief revenue officer, or the person about to hire for one. |

> [!IMPORTANT]
> **This instrument counts and it cites.** Every row is a number of named things, and every row carries the source that supplied it and one of three fill statuses. A row without a source is not filled. The reading inherits nothing from the deal-level instruments except the edges each count is read against, which [06-calibration.md](../theory/01-foundation/06-calibration.md) declares as chosen.

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
| B1 | Bargaining | Decision roles the reference workflow carries at a typical buyer | | |
| B2 | Bargaining | Whether a formal body sits over them: procurement, security review, a committee | | |
| E1 | Enforcement | Touchpoints, counted by type | | |
| E2 | Enforcement | Procedures a typical buyer changes at go-live | | |
| E3 | Enforcement | Undocumented exception paths a typical buyer carries | | |
| E4 | Enforcement | Steps in a typical buyer's version with no counterpart in the reference | | |
| E5 | Enforcement | Who codified the workflow, from Step 1 | | |
| F1 | Frequency | The population's typical reading: one-shot, recurrent or continuous | | |

**Deriving B1 before any buyer is met.** The decision roles that police a touchpoint follow its type. Writeback brings whoever owns the record and whoever polices it, in a health system the clinical informatics and compliance roles. Enrollment brings whoever owns the operation the trigger sits in. Foundational sync brings whoever owns master data. Shared context brings security. Add whoever pays. A decision-role list derived this way is Inferred until deal readings confirm it, and the derivation is what lets the row be filled at all before the first conversation.

**Reading the counts.** Each cost is read against the same two edges the [Deal Triage Calculator](./deal-triage-calculator.md) uses, and [06-calibration.md](../theory/01-foundation/06-calibration.md) section 3.2 declares them as chosen. The counts are never converted to scores or summed.

| Cost | Count | Self-serve edge | Participation edge | Keeps the buyer out regardless |
|---|---|---|---|---|
| Search | S2 | 4 | 8 | S1: buyers cannot name the problem. S4: no path from this seller to the population. |
| Bargaining | B1, plus 1 if B2 | 1 | 7 | |
| Enforcement | E1 + E2 + E3 | 2 | 11 | |

**Exposure** reads E1 + E2 + E4. Where a typical buyer can trial the product against its own work and walk away without stranding spend or data, read it as none and say so on the sheet. Where E4 is Unknown, leave it out of the count and say so. A guessed divergence count is a guess dressed as a measurement.

---

## Step 3: Positions, and whether the population is Turnkey

**Positions.** Each cost's position between its own two edges, $r_k = (n_k - \tau^{self}_k)/(\tau^{part}_k - \tau^{self}_k)$, and its zone: self-serve at zero or below, needs investment up to one, keeps the buyer out above one.

**Where the sale starts** is the cost with the largest position. Any cost that keeps the typical buyer out is named first, because no motion reaches a buyer who does not enter the market.

**Turnkey** is a population where every cost is self-serve and the exposure reads none. Product-led growth works there and almost nowhere else. A Turnkey reading carries a standing warning from the Constitution: the low investment that defines it invites entrants, and entrants raise the search cost. Re-read S2 and S3 whenever the vendor count moves.

The population's typical gaps are not read here. They feed the chance of future loss deal by deal, and each deal reading in the population reports them.

[`models/tcg_models.py`](../models/tcg_models.py) computes the positions with `threshold_position` and the zones with `cost_zone`.

---

## Step 4: The unfilled fraction

$$\text{unfilled} = \frac{\text{rows Inferred} + \text{rows Unknown}}{12}$$

An Inferred row counts as unfilled because a seller's inference is the thing a deal reading exists to test. The fraction is reported and not thresholded. Nothing yet says where the line sits, and [06-calibration.md](../theory/01-foundation/06-calibration.md) records the row count as chosen.

Two readings follow from it. **Trust.** The positions in Step 3 are as good as the rows behind them, and a sale start read from eight Inferred rows is a hypothesis. **Price.** A seller whose ledger is thin cannot close a buyer's enforcement gap cheaply, because the seller's own ignorance is half of it, and is pushed onto price and risk transfer until the ledger fills. That is why an entrant prices below an entrenched competitor, per [04-seller-surplus-model.md](../theory/01-foundation/04-seller-surplus-model.md) section 7.5, and the unfilled fraction is the number that says by how much for how long. The floor is twelve of twelve: a seller with an empty ledger has no reading to act on and should not be in the market.

---

## Step 5: Cost to serve

Take the cost where the sale starts, both when two tie, and any cost that keeps the typical buyer out. For each, walk the four activities below Read in the grid of [08-from-axioms-to-instruments.md](../theory/01-foundation/08-from-axioms-to-instruments.md) section 4 and count the ones the seller's organization cannot perform today. A capability counts as present when a named person or team does it now, not when someone could.

| Component | Map | Test | Stage | Maintain | Missing, 0 to 4 |
|---|---|---|---|---|---|
| Search | Define what the buyer chooses between | Produce proof that travels without the seller | A path with a stake, or a trial where specificity is low | Refresh the proof as the category drifts | |
| Bargaining | Map each decision role's exposure, one to one | Collect positions apart, then hear them together | Written decision criteria and sequence | Re-read decision roles at every occupant change | |
| Enforcement | Map the buyer's environment step by step | Prove capability in their environment at the seller's cost | Gate mutual commitments with a right to stop | Re-map as the environment drifts | |

Cost to serve is a count of capabilities and not a sum of money, because the seller-surplus arithmetic needs contract values this reading does not have. Two organizations with identical missing counts can face different bills, and the count says only which cost each is built to pay.

---

## Step 6: Pursue, restructure or decline

Read F1 against the missing count on the cost where the sale starts.

| F1 | Missing capabilities where the sale starts | Reading |
|---|---|---|
| Any | 0 | **Pursue.** The organization is built to pay the cost this population carries. |
| Recurrent or continuous | 1 or more | **Restructure.** Build or partner for the capability, because repetitions can carry the cost of building it. Whether they do is the amortizability question, and [04-seller-surplus-model.md](../theory/01-foundation/04-seller-surplus-model.md) section 7 is where contract value and frequency answer it once the numbers exist. |
| One-shot | 1 or more | **Decline.** Nothing amortizes the apparatus. The same rule declines a specific one-shot deal, applied to a population. |

**The imitation check.** If the organization has already built a motion and this reading's sale starts somewhere else, the reading is not the thing to doubt first. That is the organization-level mis-composed failure the Constitution names: a motion adopted because it worked for a seller in a different market, aimed at a cost this population's buyers do not carry.

**The entrant clause.** A high unfilled fraction does not change pursue to decline. It changes the price at which pursuit is possible, per Step 4, and it says the early deals are the seller's investment in the ledger rather than discounting.

---

## Step 7: Worked scenario, two populations

The instrument earns its place if the readings differ between a saturated population and a novel one selling into the same kind of buyer. Two anonymized EHR-integration markets from HTD's work will fill this section. Every row below is missing until the anonymized integration guide arrives, and the predictions are stated before the data so that the data can contradict them.

| Row | Saturated population | Novel population | Prediction |
|---|---|---|---|
| S1 | [MISSING] | [MISSING] | Saturated has a name buyers use. Novel does not, so search keeps the buyer out until the category is defined. |
| S2 | [MISSING] | [MISSING] | Saturated enumerates many, which may push search past its participation edge through entry alone. Novel cannot enumerate. |
| S3 | [MISSING] | [MISSING] | Saturated has comparison material. Whether it lets buyers rank on evidence, or has pooled into unverifiable claims, is register item 27's question. |
| S4 | [MISSING] | [MISSING] | Both depend on the seller's vendor-program status. |
| B1 | [MISSING] | [MISSING] | Same touchpoint types produce the same decision roles. Writeback brings the record owner and compliance in both. |
| B2 | [MISSING] | [MISSING] | A health system puts a formal body over both. |
| E1 to E4 | [MISSING] | [MISSING] | Saturated has standardized touchpoints and lower divergence. Novel has fewer touchpoints and higher divergence, because no reference has converged. |
| E5 | [MISSING] | [MISSING] | Saturated is codified by convention or standard. Novel is codified by each buyer. |
| F1 | [MISSING] | [MISSING] | Both recurrent. |
| **Where the sale starts** | | | Saturated starts at bargaining or enforcement, with search held up by pooling. Novel has search keeping the buyer out. |
| **Unfilled fraction** | | | Saturated is lower for a seller already in it. Novel is high for anyone. |

If both populations start the sale at the same cost with the same zones, the instrument is not discriminating and this section says so.

---

## Re-reading: how deal readings feed the ledger

Every deal reading in the population converts rows from Inferred or Unknown to Known, and the ledger is the seller's accumulated insight about the market. Re-run this reading when the unfilled fraction moves, when the book of deal readings disagrees with it, and once a year regardless, because categories drift.

Adjacent markets inherit fill through the spine. A workflow that shares typed touchpoints with one the seller already serves starts with those rows Known, and the share of its ledger inherited that way is the seller's redeployable value, per [04-seller-surplus-model.md](../theory/01-foundation/04-seller-surplus-model.md) section 7.5. The inheritance transfers on the enforcement rows more reliably than on the bargaining rows, because decision roles and policing are local to the population even when the touchpoint types are not.

---

## What this does not settle

- **No threshold on the unfilled fraction.** It is reported. A line will need data from populations that were entered and populations that were declined.
- **The edges are chosen.** The counts are observations and the edges are not, and the calibration page says so for every edge.
- **A typical buyer hides dispersion.** A population whose members carry two different decision-role structures around the same workflow is two markets, and the typical-buyer counts will average them into one. When the deal readings disagree with each other more than with the market reading, split the population.
- **Cost to serve counts capabilities and not money.** The count says which cost an organization is built to pay. It does not say what building the missing one would cost, and the seller-surplus arithmetic does not run without contract values.
- **The gaps are not read here.** A population whose buyers are uniformly uncertain about one component carries a future loss this reading cannot see, and the first deal readings will show it.
- **The scenario is unfilled.** Step 7 carries predictions and no data.

---

## Scoring sheet

| Field | Value |
|---|---|
| Reference workflow named, with touchpoints typed (yes / no) | |
| Population | |
| Who codified the workflow | |
| Rows Known / Inferred / Unknown | |
| Search position and zone | |
| Bargaining position and zone | |
| Enforcement position and zone | |
| Exposure (none / specific), E4 included (yes / no) | |
| **Where the sale starts** | |
| **Turnkey** (yes / no) | |
| Unfilled fraction | |
| Missing capabilities where the sale starts | |
| F1 | |
| **Reading: pursue, restructure or decline** | |
| Motion the organization has already built, if any | |
| Date read, and by whom | |

---

## Related

- **Theory:** [Constitution](../theory/01-foundation/00-tcg-constitution.md), Axiom I across a population, the definition of workflow, the Turnkey corollary, and the cost-to-serve and pursuit corollaries under Axiom II.
- **Derivation:** [08-from-axioms-to-instruments.md](../theory/01-foundation/08-from-axioms-to-instruments.md) sections 2.1, 4 and 5.
- **The seller's side:** [04-seller-surplus-model.md](../theory/01-foundation/04-seller-surplus-model.md) section 7.5, the market-level information asset and the entrant's pricing.
- **Touchpoint types:** [integration-touchpoints.md](../theory/02-research/integration-touchpoints.md).
- **Provenance of every edge:** [06-calibration.md](../theory/01-foundation/06-calibration.md).
- **Executable form:** [`models/tcg_models.py`](../models/tcg_models.py).
