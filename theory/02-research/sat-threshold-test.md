---
title: "The Simplified Acquisition Threshold Test"
layer: theory
status: under-review
operationalizes: [axiom-1, axiom-2]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# The Simplified Acquisition Threshold Test

> [!NOTE]
> **This is a registered test, kept as it was written on 2026-11-09 under Constitution 6.4.** It tested the rule that one cost past its limit keeps a buyer out whatever else is easy, which the file calls the gate. Constitution 7.0 retired that rule the next day. Sections 1 to 6 keep the wording of the test as registered, so they use terms 7.0 no longer does, and section 7 says what the result means now. Two things the text cites are in git history: the research review (`git show b449f40:theory/02-research/research-review-2026-11-09.md`) and section 6 of the math file (`git show 0e13ebf:theory/01-foundation/02-mathematical-models.md`).

**What it tests.** Axiom I says the costs are non-compensatory: ease on one cost never buys back another past its threshold, because each payer's capacity is specific to it. This file runs the first test of that claim on public data. It uses the rise of the US simplified acquisition threshold, the *SAT*, from \$100,000 to \$150,000, effective 1 October 2010. Above the SAT a federal purchase goes through full procedures, more steps and approvals for the contracting office, which in TCG's terms is consensus demand on that office.

**Status.** The design and predictions below were written on 2026-11-09, before the counts were pulled. Before writing them, one count pair was seen while checking the API: fiscal 2010 awards at \$95,000 to \$100,000 against \$100,000 to \$105,000, by award type. Results follow in section 4, and nothing in sections 1 to 3 changed after they arrived.

**In short.** The threshold deters purchases, more on the open market than through contract vehicles. The registered test of non-compensation failed: products and services responded differently, in the direction neither the gate nor a compensatory account predicted. Products and services differ in more than their policing cost, so the comparison could not isolate non-compensation. The gate's own signature, the contracting office's capacity, is the next test, described in section 6.

---

## 1. Why the review's version of the test does not separate the theories

The research review of 2026-11-09, in its section 4, proposed splitting the threshold's effect by purchase vehicle: an order under an existing contract vehicle, such as a GSA Schedule, carries lower search and policing cost than an open-market buy, so a non-compensatory gate predicts equal deterrence in both. That premise fails. The procedure the SAT adds is itself smaller for an order under a vehicle than for an open-market buy, which moves from simplified procedures to full ones. Both the gate and a compensatory account predict less deterrence for orders, so the split separates nothing. It is reported below as a description, not a test.

## 2. Design

**Data.** Contract award counts from the USAspending API (`/api/v2/search/spending_by_award_count/`), award types A to D, dated by the award's signing date. The amount is the award's total obligation as the API reports it today, which includes later modifications. Counts are taken in \$5,000 bins from \$50,000 to \$250,000 for fiscal years 2008 to 2013. Fiscal 2008 to 2010 sit under the \$100,000 threshold and fiscal 2011 to 2013 under \$150,000. The script is [`models/sat_bunching.py`](../../models/sat_bunching.py), and the counts it pulled are saved beside it.

**Groups.** Purchase vehicle: open market, purchase orders and definitive contracts (types B and D), against orders under a vehicle, delivery orders and BPA calls (types C and A). A purchase order above the SAT becomes a definitive contract, so the two open-market types are pooled. Cost kind, from the product and service code: products against services, research and development left out.

**The comparison that tests non-compensation.** Inside the open market, products and services meet the same added procedure above the SAT, carried by the same payer, the contracting office. Services carry the larger policing cost, because their delivery is harder to specify and verify, and that cost falls on a different payer, the program office that oversees performance. The gate says the threshold's effect on the contracting office does not depend on the policing cost. A compensatory account, where the buyer goes ahead while its surplus covers all its costs together, says purchases already carrying a larger policing cost are closer to the margin, so the threshold deters more of them.

**Measures.** For each group:

- **M1, bunching at a threshold.** The log of the count in the \$5,000 below the threshold over the count in the \$5,000 above it, in the years the threshold applies, minus the same log ratio at the same amount in the years it does not. The difference removes round-number heaping, since \$100,000 and \$150,000 are round in every year. Read at \$100,000 (fiscal 2008 to 2010 minus 2011 to 2013) and at \$150,000 (the reverse).
- **M2, the extensive margin.** The log change, from fiscal 2008–2010 to fiscal 2011–2013, in the count of awards from \$90,000 to \$150,000, minus the log change in a reference band from \$50,000 to \$90,000 that no threshold touched. Bunched purchases that move back to their own amount stay inside the window, so a positive M2 counts purchases the old threshold kept from happening at all, which is the gate's outcome. A second reference band, \$200,000 to \$250,000, above both thresholds, is the robustness check.

Standard errors treat each count as Poisson.

## 3. Predictions

- **P1, both accounts.** M1 is positive in every group at both thresholds, and larger for open-market buys than for orders under a vehicle.
- **P2, the gate.** Inside the open market, M2 does not differ between services and products. A compensatory account predicts M2 larger for services. The two are taken to differ when the services-minus-products difference exceeds both twice its standard error and 0.05 log points, a materiality bar chosen here and not derived. M1 is reported by cost kind but not used for P2, because a service purchase is easier to resize under a threshold than a product, which raises its bunching for reasons neither account is about.

**What the test cannot do.** Commercial items, which skew toward products, could use simplified procedures above the SAT under a test program, so products may face less added procedure than services. That biases the result toward the compensatory prediction. A finding of no difference therefore counts for the gate more than a finding of a difference counts against it. The test also cannot read the contracting office's capacity, which section 6 of the math file, as it then stood, names as the gate's own signature.

## 4. Results

The counts were pulled on 2026-11-09: 960 cells covering 1,244,037 awards. Values are in log points, with Poisson standard errors in brackets.

| Group | M1 at \$100,000 | M1 at \$150,000 | M2, lower reference | M2, upper reference |
|---|---|---|---|---|
| Open market, products | +0.86 (0.03) | +1.18 (0.05) | +0.31 (0.01) | +0.48 (0.02) |
| Open market, services | +0.47 (0.04) | +0.46 (0.06) | +0.12 (0.01) | +0.16 (0.02) |
| Open market, all | +0.69 (0.03) | +0.89 (0.04) | +0.23 (0.01) | +0.36 (0.01) |
| Orders, products | +0.28 (0.02) | +0.07 (0.03) | +0.03 (0.01) | −0.01 (0.01) |
| Orders, services | +0.08 (0.02) | +0.15 (0.03) | +0.07 (0.01) | −0.04 (0.01) |
| Orders, all | +0.19 (0.02) | +0.12 (0.02) | +0.03 (0.01) | −0.02 (0.01) |

**P1 holds.** M1 is positive in every group at both thresholds, and larger for open-market buys than for orders under a vehicle. Both accounts predicted this, so it tests neither.

**P2 fails as stated.** Inside the open market, the extensive margin differs between products and services by more than the stated bar against both reference bands. Services minus products is −0.19 (0.02) against the lower band and −0.32 (0.03) against the upper. The direction contradicts both accounts. The gate predicted no difference, and a compensatory account predicted the larger margin for services. Products, which carry the smaller policing cost, responded more. The commercial-items bias named in section 3 pushes the other way, so it does not explain the result.

**Exploratory checks, run after the results.** None of these was planned, and they carry less weight.

- **Purchases did not move between vehicles.** Between \$90,000 and \$150,000, the share of product purchases made as orders under a vehicle fell from 0.70 under the \$100,000 threshold to 0.64 under \$150,000, and for services from 0.75 to 0.73. Orders in that window did not fall against the reference band, though: their M2 is +0.03 for products and +0.07 for services. The share fell because open-market purchases rose, not because buyers moved purchases back from vehicles.
- **Pooling across vehicles only dilutes.** Pooled M2 is +0.12 for products and +0.08 for services against the lower band, a difference under the 0.05 bar, and +0.13 against +0.01 against the upper band, over it. Orders outnumber open-market awards and respond little, so pooling narrows the gap by arithmetic and is no evidence for either account.
- **No sign of split purchases.** The ratio of open-market awards at \$50,000 to \$75,000 to those at \$75,000 to \$90,000 rose for products after the change and held for services. Purchases split to stay under the old threshold would have made it fall.
- **The two cost kinds trended apart.** Open-market service awards fell by about a quarter from fiscal 2010 to 2013 while products held steady. The reference bands absorb a fall that is even across amounts, and not one that is not.

## 5. What it means for TCG

- **The compensatory prediction failed as registered.** Services never responded more than products, though a compensatory account in which product buys carry less surplus could produce what was seen.
- **The gate's equality prediction failed as registered,** so this test gives the non-compensatory rule no support. The pooled reading looks closer to equality only by dilution.
- **The comparison did not isolate one cost.** On the open market the threshold deterred more product purchases than service purchases. Products and services differ in more than their policing cost. Product buys may carry less surplus per dollar, which a compensatory account would read as closer to the margin. They may also run through smaller contracting offices with less capacity for full procedures, which the gate would read as a larger position at the same demand. This test cannot tell those apart.
- **The design lesson.** A test of non-compensation needs two groups that differ in one cost and meet the same added demand on the same payer. Products and services are not that pair.

## 6. The next test

Section 6 of the math file, as it then stood, names what separates the gate from the buyer's condition. Bunching that scales with each purchase's surplus belongs to the buyer's condition. Bunching that ignores surplus and moves with the contracting office's capacity belongs to the gate. Federal award records name the awarding office, so an office's workload, its awards per year against the size of its staff where that is published, can stand in for its capacity. The test asks whether deterrence at the threshold rises with workload, within one cost kind and one vehicle, and across the fiscal 2018 rise of the SAT to \$250,000 as well as the fiscal 2011 one. It is described here and not yet registered. Its windows wait on confirming when each agency adopted the \$250,000 threshold by class deviation, and its measure of capacity waits on finding which offices publish staffing.

## 7. What it means under Constitution 7.0

Added on 2026-11-10. Nothing above was changed except two links to files that have since left.

- **The rule this test was built for is gone.** Constitution 7.0 says a cost can stop a deal and that a large enough gain can offset it. The registered equality prediction failed, so the test gave the retired rule no support. It did not refute it either, for the reason section 5 gives.
- **An approval threshold deters purchases.** On the open market, bunching under the threshold is large, and some purchases the old threshold had kept from happening appeared once it rose. That backs claim 8's exception, that a price taken under a spend threshold removes an approver.
- **A contract vehicle responds less.** Orders under a vehicle bunched less, and on the pooled figures showed almost no purchases kept out. Orders for services are the exception: against the lower reference band they show +0.07, where open-market services show +0.12. The threshold adds less procedure to such an order, so the finding describes a pre-approved contract carrying part of the cost, as claim 4 has it. It is a description and not a test.
- **Item 68 in [06-calibration.md](../01-foundation/06-calibration.md) carries the prediction forward.** The test in section 6 would now read how much of the deterrence follows the contracting office's workload.

## Related

- [buying-center-dynamics.md](./buying-center-dynamics.md), for Carril's study of the same threshold.
- [information-environment.md](./information-environment.md), for the floor a pre-approved contract lowers.
- [`models/README.md`](../../models/README.md), for how to run the script.

