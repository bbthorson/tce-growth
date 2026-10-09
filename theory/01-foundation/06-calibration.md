---
title: "The Calibration Layer"
layer: theory
status: active
version: 1.0
operationalizes: [axiom-1, axiom-2, axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# The Calibration Layer

**Version:** 1.0
**Purpose:** To hold every number in this framework in one place, so that the structural claims can be read, argued with, and accepted or rejected without any of them.

---

## 1. Why the numbers are quarantined

The framework makes two kinds of claim and they carry very different weight.

**Structural claims** say what depends on what. Using the market costs three things, and any one of them can keep the buyer out. The sale starts at the cost nearest its own threshold. Each party goes ahead only when its own share of today's investment is covered by its own return, and price cancels between the two conditions. What a party sinks exposes it to what it cannot verify, and the gaps rebuild unless maintained. Specificity and frequency select the governance form. These are the framework, they are argued from mechanism, and they are what a reader is being asked to accept.

**Parameters** say how much. Every one of them is a reasoned starting value. None is fitted to booked deal data.

Mixing the two makes the framework weaker than it is. A reader who doubts where a band edge sits should be able to doubt that without doubting that any one cost can keep a buyer out, because the second claim does not depend on the first. Keeping the numbers here is what makes those two positions separable.

> [!IMPORTANT]
> **No value on this page is a measurement.** Read the provenance column before quoting any of them outside this repository, and do not present any of them as an empirical estimate of anything. The framework is currently coherent rather than confirmed, and section 4 says what would change that.

---

## 2. Provenance vocabulary

| Status | What it means |
|---|---|
| **Structurally motivated** | The *shape* follows from a stated argument. A published result constrains the direction or the sign. The specific value does not follow and is chosen inside whatever range the argument allows. |
| **Anchored by analogy** | The magnitude is borrowed from a measured quantity in another domain, as an order-of-magnitude justification. The borrowing does not transfer the original's provenance. |
| **Convention** | A normalizing choice with no empirical content. Setting it to something else rescales the output and changes nothing about the model. |
| **Chosen** | No source. A reasoned starting value and nothing more. |
| **Named, not valued** | The parameter exists in the model and no default is offered, because offering one would read as an estimate. |

---

## 3. Every parameter in the framework

### 3.1 The two conditions, the gaps and future loss ([02-mathematical-models.md](./02-mathematical-models.md))

| Parameter | Symbol | Value | Provenance |
|---|---|---|---|
| Self-serve threshold, per cost | $\tau^{self}_k$ | — | **Named, not valued.** The theory states the threshold exists. The field instrument places it as an edge on each count, section 3.2. |
| Participation threshold, per cost | $\tau^{part}_k$ | — | **Named, not valued.** As above. Whether it rises with the value at stake is open. |
| Floor on the chance of loss | $\pi_0$ | — | **Named, not valued.** That a floor above zero exists is structurally motivated by the return-variance floor in section 2.3 of the math file. No value is offered. |
| Shape of the chance of loss | — | straight line | **Chosen.** A placeholder between floor and ceiling. No curvature is claimed. |
| How a party's gaps combine | — | arithmetic mean | **Chosen.** No source. |
| Drift ceiling | — | 1 | **Convention.** The top of the range every count-based gap is defined on. |
| Component drift rates | $\gamma_{search}$, $\gamma_{consensus}$, $\gamma_{implementation}$ | — | **Named, not valued.** |
| Technical weight | $w_t$ | 0.6 | **Chosen.** No source. |
| Process weight | $w_p$ | 0.4 | **Chosen.** Fixed by $w_t + w_p = 1$. |
| Tech acceleration exponent | $\phi_t$ | 1.2 | **Structurally motivated.** Convexity follows from Williamson's asset specificity argument. The value does not. |
| Process acceleration exponent | $\phi_p$ | 1.1 | **Chosen.** No source. |
| Return uncertainty sensitivity | $\mu$ | 1.0 | **Convention.** |
| Unvalidated vendor doubt | $\nu$ | 2.0 | **Chosen.** No source. |
| Vendor proof decay | $\kappa$ | 0.5 | **Structurally motivated.** Diminishing returns follow from Spence (1973). The rate does not. |
| Coordination overhead | $\alpha$ | 1.0 | **Convention.** Also the conversion of the bargaining cost into contract value, which nobody has measured. |
| Committee complexity exponent | $\beta$ | 1.35 | **Structurally motivated.** $\beta > 1$ follows from $N(N-1)/2$ channel growth (Cyert and March 1963; Webster and Wind 1972). The value inside $[1.2, 2.0]$ is chosen. |
| Technical overlap weight | $\gamma_{TO}$ | 0.20 | **Chosen.** Field refinement, not core theory. |
| Responsiveness factor | $\gamma_r$ | 0.5 | **Chosen.** Staging logic follows from Dixit and Pindyck (1994). The value does not. |

**Retired in Constitution 4.0.** The reduced form $y = a\hat{\Delta}_A^2 + c$ took three parameters with it: the coefficient $a = 2.25$, anchored by analogy to loss aversion, the convexity exponent, and the base friction growth rate $b$. The Deal Triage Calculator's score bands, level range, Structural boundary, addends, divergence modifier and dominance threshold went when the calculator was rebuilt on positions. [02-mathematical-models.md](./02-mathematical-models.md) section 7 records why. None of them is in the model.

### 3.2 The triage instrument ([Deal Triage Calculator](../../practice/deal-triage-calculator.md))

Every input to this instrument is a count of a named thing, and each count is read against two edges of its own. The edges are where the arbitrariness that counting removed comes back. Each is placed on a boundary of the score bands earlier versions used, so that a reader comparing old and new readings can see where the line moved, and that placement is the only argument behind any of them.

| Cost | Self-serve edge | Participation edge | Provenance |
|---|---|---|---|
| Search, alternatives to rule out | 4 | 8 | **Chosen.** The top of the old 3-to-4 band and the bottom of the old 8-or-more band. |
| Consensus, decision roles that can say no plus any formal body | 1 | 7 | **Chosen.** The old single-veto band and the bottom of the old 7-or-more band. |
| Implementation, integration points plus changed workflows plus undocumented exceptions | 2 | 11 | **Chosen.** The top of the old 0-to-2 band and the bottom of the old 11-or-more band. |

| Parameter | Value | Provenance |
|---|---|---|
| Unnamed category, or no channel | Keeps the buyer out | **Structurally motivated.** An unbounded alternative set and an unreachable seller are argued in step 1a. Neither is a count, so neither has an edge. |
| Formal body | Counts as one veto | **Convention.** A body holds a veto and is not a person, so it joins the position count and not the evidence denominator. |
| Search evidence items | 4 | **Chosen.** The four questions are argued; the count of them is an artifact of that argument. |

### 3.2a The market reading ([The Market Reading](../../practice/00-market-reading.md))

The reading reuses every edge in section 3.2 and adds one structural count of its own.

| Parameter | Value | Provenance |
|---|---|---|
| Ledger rows | 12 | **Chosen.** The rows are argued from the three components and frequency. The count of them is an artifact of that argument, and the unfilled fraction is a share of it. |
| Unfilled-fraction threshold | none | **Named, not valued.** The fraction is reported. A line needs data from populations entered and populations declined. |
| Missing-capability range | 0 to 4 per component | **Convention.** The four activities below Read in the activity grid. |

### 3.3 The asymmetry scorecard ([Bilateral Asymmetry Scorecard](../../practice/asymmetry-scorecard.md))

| Parameter | Value | Provenance |
|---|---|---|
| Raw gap range | $[2, 10]$ | **Convention.** Two halves each on $[1, 5]$. |
| Normalization | $(\Delta_A - 2) / 8$ | **Convention.** Maps the raw range onto $[0, 1]$, which every equation that takes a gap requires. |
| Dimension mapping | $f \cdot 4 + 1$ | **Convention.** Puts an unevidenced fraction onto the presentation scale. Carries no information the fraction does not. |
| Risk band edges | 4.0, 7.0 | **Chosen.** No source. |
| Commercial hold threshold | 7.0 | **Chosen.** No source. |

### 3.4 Staged commitment ([Milestone Valuation Model](../../practice/milestone-valuation-model.md))

| Parameter | Value | Provenance |
|---|---|---|
| Reference resolution profile | $\mu$ = 0.25, 0.50, 0.80 | **Chosen.** The shape is the argument and the values are illustrative. |
| Reference payment schedule | 0.25, 0.35, 0.40 of annual contract value | **Chosen.** Illustrative. The constraint that matters is that committed payment stays below value realized at every row. |
| Reference sunk amounts | 0.10, 0.25, 0.50 of annual contract value | **Chosen.** Illustrative. The shape, small commitments early and large late, is the argument. |
| Illustrative floor on the chance of loss | 0.05 | **Chosen.** Used only in the worked table. The theory names the floor and does not value it, and nothing in the model ships it as a default. |

### 3.5 Retrospective measures ([Friction Efficiency Index](../../practice/friction-efficiency-index.md))

Weakest layer in the framework, and the only one whose parameters have no argument behind them at all.

| Parameter | Value | Provenance |
|---|---|---|
| Composite weights | 0.35, 0.25, 0.25, 0.15 | **Chosen.** No source. |
| Friction allocation target band | 0.60-0.75 | **Chosen.** No source. |
| Committee-size correction | $N^{0.5}$ | **Structurally motivated.** Direction follows from the bargaining cost rising in $N$. The exponent is chosen. |
| Provisioning guard | +1 | **Convention.** Prevents division by zero. |
| Change-order weight | 0.25 | **Chosen.** No source. |
| Buyer commitment reference | 0.5 | **Convention** until twenty closed Structural deals exist, then a trailing median. |
| Minimum credible edge cases | 8 | **Chosen.** No source. |

---

## 4. What would make any of this empirical

The framework becomes predictive rather than organizing when deals are instrumented. Five things, in rough order of how much each one buys.

1. **The three component gaps logged separately** at deal open and at every artifact boundary. This makes the drift rates estimable and tests the framework's central dynamic claim, that discovery rotates the vector rather than only shortening it. A book of deals whose composition at close matches its composition at open falsifies it.
2. **Each party's investment and specific exposure logged in contract value** at signature, with the outcome at each renewal. That makes the chance of loss estimable against the gaps, and it is the estimation problem with a stated unit on both sides.
3. **Committee size and stakeholder alignment recorded as structured fields** rather than narrative notes, which makes $\beta$ estimable.
4. **Triggering events dated**, which makes the decay rate observable as the fall in buyer-reported urgency between the event and close.
5. **Count Variance recorded at every Adoption Review**, which is the only check the counting instrument has on itself and the fastest way to learn whether the bands in section 3.2 are the right shape.

Until then, treat every output as a structured comparison between deals inside one book. A deal scoring 7.2 is meaningfully worse than one scoring 4.1. Neither number predicts a close date.

---

## 5. Known defects in this layer

Recorded rather than fixed, because each fix means choosing a shape and that is a decision rather than a repair.

**The edges reintroduce what counting removed.** The instrument counts named things, which fixes the ordinal problem at the input, and since Constitution 4.0 it no longer converts them to scores. Each count is still read against two chosen edges, so a position is only as defensible as the edges behind it. The step functions are gone and the edges remain.

**The zone edges are cliffs.** A count one below an edge and a count one above it land in different zones. The dominance threshold carried the same defect and is gone. The zone edges carry it in a weaker form, because where the sale starts is read from positions, which are continuous, and only the zone label jumps.

**The shape of the chance of loss is not identified.** The straight line between floor and ceiling is a placeholder, and nothing in the framework distinguishes it from any other increasing form. Constitution 3.0 carried the same defect as an unidentified convexity exponent on the retired reduced form.

**The Friction Efficiency Index composite carries three defects of its own**, recorded in section 6 of that file. They are defects in the measure rather than in its parameters, so they are not repeated here.

---

## Related

- [00-tcg-constitution.md](./00-tcg-constitution.md) — The structural claims, which are stated without reference to any value on this page.
- [02-mathematical-models.md](./02-mathematical-models.md) — The functional forms these parameters sit inside.
- [citation-provenance-audit.md](../02-research/audits/citation-provenance-audit.md) — The companion for headline statistics, on the same discipline. That file traces numbers cited from outside; this one traces numbers chosen inside.
- [models/README.md](../../models/README.md) — Why nothing here is fitted, and what fitting to synthetic data would cost.
