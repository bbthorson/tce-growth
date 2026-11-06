---
title: "The Market Reading"
layer: practice
status: active
version: 3.0
operationalizes: [axiom-1, axiom-2, axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# The Market Reading

Version: 3.0
Goal: Read a buyer population before any buyer is met, and decide whether a market exists here for this seller. Emit each cost's position across the population as it is and as buyers expect it, where the sale starts, whether a cost floor or the category prior holds buyers out, whether the population sinks anything specific, the seller's unfilled fraction, what the seller must build, and one of pursue, restructure or decline. Then write the search ledger the population's buyers will use. The motion an organization builds follows from this reading, and not from the motion that worked for a seller in a different market.

**Canonical reference:** [Constitution 6.1](../theory/01-foundation/00-tcg-constitution.md). Axiom I for both limits, the cost floor, the category prior and Turnkey. Axiom II for where the sale starts. The definition of workflow. The derivation is [08-from-axioms-to-instruments.md](../theory/01-foundation/08-from-axioms-to-instruments.md) sections 2.1 and 5.

| | |
|---|---|
| **Inputs** | The reference workflow the product encodes, with each touchpoint typed. Whatever the seller can source about the buyer population. |
| **Outputs** | A thirteen-row ledger with a source and fill status on every row, each cost's position as it is and as buyers expect it, where the sale starts, a floor-or-prior reading for any cost past its edge, an exposure reading, whether the population is Turnkey, the unfilled fraction, what the seller must build, pursue, restructure or decline, and the search ledger. |
| **Next step** | Pursue: publish the search ledger, run the [Deal Triage Calculator](./deal-triage-calculator.md) on the first buyer, and feed its counts back here. Restructure: build or partner for what is missing, then re-read. Decline: record why, and re-read when an adjacent market fills the ledger. |
| **Owner** | Whoever chooses the motion. A founder, a chief revenue officer, or the person about to hire for one. |

> [!IMPORTANT]
> **This instrument counts and it cites.** Every row is a number of named things, and every row carries the source that supplied it and one of three fill statuses. A row without a source is not filled. The counts are read against the same edges the Deal Triage Calculator uses, which [06-calibration.md](../theory/01-foundation/06-calibration.md) section 3.2 declares as chosen, and they are never converted to scores or summed.

---

## Step 0: Name the workflow

Write the reference workflow the product encodes, one row per step. Mark each step as internal, performed by the product alone, or as a touchpoint where the product meets the buyer's system of record, and type every touchpoint.

| Step | Internal or touchpoint | Touchpoint type | Role that performs it at the buyer | System touched |
|---|---|---|---|---|
| | | Enrollment, supplementation, writeback, foundational sync, or shared context | | |

The five types hold in any vertical, and [integration-touchpoints.md](../theory/02-research/integration-touchpoints.md) carries them. A seller who cannot fill this table stops here: a product that cannot name its workflow has no reference to read a buyer's divergence against, which is the Constitution's definition of workflow applied before selling begins.

---

## Step 1: Define the population

The population is the buyers running a recognizable variant of the Step 0 workflow. Name them, and name who codified the workflow: a regulator, an industry standard, or each buyer for itself. A regulator's codification converges the population and each buyer's fragments it, which shows up in the enforcement rows. Count the buyers and a typical contract value, each with a source and a fill status, because Step 6 asks whether the deals this population can produce repay what the seller must build.

---

## Step 2: Fill the ledger

Thirteen rows. Each carries a count, the source that supplied it, and a fill status: **Known** (a named source supplied it, including the seller's own deal readings here), **Inferred** (reasoned from the workflow, the touchpoint types or an adjacent market, and unconfirmed here), or **Unknown**.

The **prior** column is what buyers in this population believe the count is before they meet any seller: the vendors they think they must compare, the approvals they think a purchase like this needs, the integration work they think it takes. Read it from buyers who named the problem and bought from no one: public requests for proposal that never became a purchase, interviews with buyers who chose no one, and what analysts and peers say the category costs to buy and run. Questionnaires from buyers already in discovery read only the priors that did not keep them out. It carries its own source and fill status.

| Row | Component | What to count | Count | Prior | Source | Fill |
|---|---|---|---|---|---|---|
| V1 | Value | Buyers with a named trigger and a budget owner this year | | | | |
| S1 | Search | Whether buyers use a category name for the problem, and which | | | | |
| S2 | Search | Alternatives a typical buyer enumerates: named vendors, plus build, plus do nothing | | | | |
| S3 | Search | Whether published material lets a buyer compare those alternatives | | | | |
| S4 | Search | Whether this seller holds a path to the population today: a vendor program, a marketplace, a purchasing consortium, a channel | | | | |
| B1 | Bargaining | Decision roles the reference workflow carries at a typical buyer | | | | |
| B2 | Bargaining | Formal bodies that sit over them at a typical contract value: procurement, security review, a committee, and the spend threshold that brings each in | | | | |
| E1 | Enforcement | Touchpoints, counted by type | | | | |
| E2 | Enforcement | Procedures a typical buyer changes at go-live | | | | |
| E3 | Enforcement | Undocumented exception paths a typical buyer carries | | | | |
| E4 | Enforcement | Steps in a typical buyer's version with no counterpart in the reference | | | | |
| E5 | Enforcement | Who codified the workflow, from Step 1 | | | | |
| F1 | Frequency | The population's typical reading: one-shot, recurrent or continuous | | | | |

**Deriving B1 before any buyer is met.** The decision roles that police a touchpoint follow its type. Writeback brings whoever owns the record and whoever polices it. Enrollment brings whoever owns the operation the trigger sits in. Foundational sync brings whoever owns master data. Shared context brings security. Add whoever pays. A list derived this way is Inferred until deal readings confirm it.

**Exposure** reads E1 + E2 + E4. Where a typical buyer can trial the product against its own work and walk away without stranding spend or data, read it as none and say so. Where E4 is Unknown, leave it out and say so. A guessed divergence count is a guess dressed as a measurement.

---

## Step 3: Positions, floors and priors

**Positions.** Read each cost against its two edges, once on the count and once on the prior.

| Cost | Count | Self-serve edge | Participation edge | Keeps the buyer out regardless |
|---|---|---|---|---|
| Search | S2 | 4 | 8 | S1: buyers cannot name the problem. S4: no path from this seller to the population. |
| Bargaining | B1 plus B2's bodies | 1 | 7 | |
| Enforcement | E1 + E2 + E3 | 2 | 11 | |

Each position is $r_k = (n_k - \tau^{self}_k)/(\tau^{part}_k - \tau^{self}_k)$: self-serve at zero or below, needs investment up to one, keeps the buyer out above one. [`models/tcg_models.py`](../models/tcg_models.py) computes them with `threshold_position` and `cost_zone`.

**A cost past its edge: floor or prior?** The two look alike from outside, since in both the population names the problem and buys from no one. They take different remedies, so read which it is.

| Count | Prior | Reading | Remedy |
|---|---|---|---|
| Past its edge | Any | **Floor, or this seller's own cost.** Ask whether a seller that lowered the count would keep the return. If every seller in the category would share it, the floor holds it: the information environment, the buyers' institutions, or how verifiable delivery is. Read it on the lowest-count seller serving this population, from public material. If this seller's product sets the count, changing it is a product decision. | A floor falls only through investment made across deals, such as a marketplace, a certification or a standard, or a signal costly enough to separate this seller from the pool. Otherwise choose a different market. |
| Within reach | Past its edge | **Prior.** Buyers believe the cost is higher than it is, often because buyers burned by a misrepresented fit raised it. | Show this seller's own cost with evidence buyers can check before they meet anyone. The search ledger in Step 7 is where it goes. |
| Within reach | Within reach | **Can enter.** | Continue. |

**Where the sale starts** is the cost with the largest position on the prior, because buyers decide on what they expect before they enter. What the seller builds, in Step 5, is keyed to the count.

**Turnkey** is a population where every cost is self-serve and the exposure reads none. The low investment that defines it invites entrants, and each raises the search floor, so re-read S2 and S3 whenever the vendor count moves.

---

## Step 4: The unfilled fraction

$$\text{unfilled} = \frac{\text{rows Inferred or Unknown among V1, S2, B1, B2, E1 to E4}}{8}$$

The eight are the rows Steps 3 and 6 and the exposure reading use. The rows that are nearly free to fill stay out of it, so the fraction cannot be lowered without research. An Inferred row counts as unfilled, because a seller's inference is what a deal reading exists to test. The fraction is reported and not thresholded, and it says how far to trust Steps 3 and 6. A thin ledger also pushes an entrant onto price until it fills ([04-seller-surplus-model.md](../theory/01-foundation/04-seller-surplus-model.md) section 7.5).

---

## Step 5: What the seller must build

The seller's limit under Axiom I rests on what it has to build before the first deal, which no single deal repays. Take the cost with the largest position on the count, both when two tie, and any count past its edge. A prior past its edge is answered with evidence in Step 7, not built against. For each, count the activities below Read in the grid of [08-from-axioms-to-instruments.md](../theory/01-foundation/08-from-axioms-to-instruments.md) section 4 that the organization cannot perform today. A capability counts as present when a named person or team does it now, not when someone could.

| Component | Map | Test | Stage | Maintain | Missing, 0 to 4 |
|---|---|---|---|---|---|
| Search | Define what the buyer chooses between | Produce proof that travels without the seller | A path with a stake, or a trial where specificity is low | Refresh the proof as the category drifts | |
| Bargaining | Map each decision role's exposure, one to one | Collect positions apart, then hear them together | Written decision criteria and sequence | Re-read decision roles at every occupant change | |
| Enforcement | Map the buyer's environment step by step | Prove capability in their environment at the seller's cost | Gate mutual commitments with a right to stop | Re-map as the environment drifts | |

The count says which cost an organization is built to absorb. It is not a sum of money, because the seller-surplus arithmetic needs contract values this reading does not have.

---

## Step 6: Pursue, restructure or decline

**Two overrides first.** Where V1 is zero or Unknown, decline: no cost reading matters without buyers who have a reason and a budget. Where Step 3 reads a floor past its edge, decline, unless this seller will fund the shared investment that lowers it.

| Missing where the build is keyed | Reading |
|---|---|
| 0 | **Pursue.** The organization is built to absorb the cost this population carries. |
| 1 or more, and the population's buyers at the typical contract value can repay the build | **Restructure.** Build or partner for it. [04-seller-surplus-model.md](../theory/01-foundation/04-seller-surplus-model.md) section 7 is the arithmetic once the numbers exist. |
| 1 or more, and too few | **Decline.** |

The build is repaid across the population's deals, won and lost, so a thousand buyers who each buy once can carry it. F1 sets the governance each deal will need, and does not decide whether the build is repaid.

**The imitation check.** If the organization has already built a motion and this reading's sale starts somewhere else, doubt the motion before the reading. That is the imitation failure.

**The entrant clause.** A high unfilled fraction does not turn pursue into decline. It lowers the price at which pursuit is possible, and it makes the early deals the seller's investment in the ledger rather than discounting.

---

## Step 7: The search ledger

On pursue, write the search ledger. It lives at the market and is reused by every deal in the population. It closes the buyer's search gap only if a buyer can complete it without the seller, so its evidence comes from parties other than this seller: analysts, review sites, marketplaces, certifications and peer references.

| Alternative | Steps of the reference workflow it covers | Evidence that compares it, which the buyer can check | How a buyer reaches it | Added |
|---|---|---|---|---|
| Each named vendor S2 counts | | | | |
| Building it internally | | | | |
| Doing nothing | | | | |

**Done when** three buyers from the population who have not met the seller can, from the ledger alone, say which alternatives cover which steps and how to reach the seller. Each evidence cell has to pass the [Friction Allocation Diagnostic](./friction-allocation-diagnostic.md), and the comparison as a whole needs an adjudicator other than this seller with a stake in its accuracy, or it is a claim. Where Step 3 read a prior past its edge, the evidence that shows this seller's own bargaining or policing cost goes here too: published terms, a security packet, implementation timelines with references.

**Maintain it.** Append entrants as they arrive, and re-test the evidence when cheap signals start to swamp costly ones.

---

## Re-reading

Every deal reading in the population converts rows from Inferred or Unknown to Known. Deal readings come only from buyers who entered, so keep counts from buyers who declined or never answered apart, or each re-read drifts toward can enter. Re-run this reading when the unfilled fraction moves, when the book of deal readings disagrees with it, and once a year regardless. If the deal readings disagree with each other more than with this reading, the population is two markets: split it.

Adjacent markets inherit fill through the spine. A workflow that shares typed touchpoints with one the seller already serves starts with those enforcement rows Known, and the share inherited is the seller's redeployable value ([04-seller-surplus-model.md](../theory/01-foundation/04-seller-surplus-model.md) section 7.5). The bargaining rows transfer less reliably, because decision roles are local to the population even when touchpoint types are not.

---

## What this does not settle

- **No threshold on the unfilled fraction.** A line needs data from populations that were entered and populations that were declined.
- **The edges are chosen,** and the prior is softer still: it is what buyers say, read at second hand.
- **What the seller builds counts capabilities, not money,** and cannot tell a fixed build from per-deal spending ([07-open-questions.md](../theory/01-foundation/07-open-questions.md) item 56). A seller entering to learn whether the market exists is item 54.
- **No worked case yet.** Item 6 records the two-population test this reading has to pass.

---

## Scoring sheet

| Field | Value |
|---|---|
| Reference workflow named, with touchpoints typed (yes / no) | |
| Population, and who codified the workflow | |
| Buyers, and typical contract value | |
| V1: buyers with a trigger and a budget owner | |
| Rows Known / Inferred / Unknown | |
| Search position and zone: count, prior | |
| Bargaining position and zone: count, prior | |
| Enforcement position and zone: count, prior | |
| Any cost past its edge: floor, this seller's own, or prior | |
| Exposure (none / specific), E4 included (yes / no) | |
| **Where the sale starts** | |
| **Turnkey** (yes / no) | |
| Unfilled fraction | |
| Missing capabilities where the sale starts | |
| F1 | |
| **Reading: pursue, restructure or decline** | |
| Motion the organization has already built, if any | |
| Search ledger published (yes / no), and its alternatives | |
| Date read, and by whom | |

---

## Related

- **Theory:** [Constitution](../theory/01-foundation/00-tcg-constitution.md), Axiom I and Axiom II, and the definition of workflow.
- **Derivation:** [08-from-axioms-to-instruments.md](../theory/01-foundation/08-from-axioms-to-instruments.md) sections 2.1, 4 and 5.
- **The deal level:** [Deal Triage Calculator](./deal-triage-calculator.md).
- **The seller's side:** [04-seller-surplus-model.md](../theory/01-foundation/04-seller-surplus-model.md) section 7.5.
- **Touchpoint types:** [integration-touchpoints.md](../theory/02-research/integration-touchpoints.md).
- **Provenance of every edge:** [06-calibration.md](../theory/01-foundation/06-calibration.md).
