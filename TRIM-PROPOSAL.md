# Trim Proposal

<!-- vale TCG.RetiredTerms = NO -->
<!-- Old names are the subject of this file, so the retired-term rule is off for all of it. -->

**Status:** proposed on 2026-11-10, with the five decisions in section 4 made the same day. Nothing has been moved, rewritten or deleted yet. Section 1 is the test and section 3 is the verdict on each file. This file retires to git history once the trim is applied.

**Why trim.** Constitution versions 5.0 to 6.4 all date from one month, and most of what they added answers a reviewer. The author's own claims are fewer and plainer, and he has published most of them already. The trim puts those claims in front and moves what defends them behind.

---

## 1. The core

Two parties make three decisions in order. Conditions run forward: the market shapes the deal, and the deal shapes what the relationship has to manage. Expectations run backward: a buyer prices a later cost when it makes an earlier decision. The relay model, with one role per funnel stage and a fixed playbook for each, has neither.

Each claim names where the author said it. "Session" means the working sessions of 2026-11-09 and 2026-11-10.

### Time0, the market

The buyer asks whether to buy, build or do nothing. The seller asks whether it can serve these buyers at a profit. The home cost is search.

| # | Claim | Where it was said |
|---|---|---|
| 1 | The kind of cost in the way decides how to sell. Leaders pick the playbook by fashion. | [tce-sales-saas.md](./publishing/02-tools/style-references/blog-posts/tce-sales-saas.md), session |
| 2 | Two things a leader can see predict that cost before any deal: how settled and how entangled the workflow is, and how complex the buyer's organization is. | The curve in the same post, session |
| 3 | A claim that costs nothing to make raises every buyer's search cost. Buyers believe a seller for what it gave up. | [cheap-signals.md](./publishing/02-tools/style-references/short-form-posts/cheap-signals.md) |
| 4 | Rules set a floor that no seller lowers alone, and the floor favors whoever has already paid it. | [access-model-hidden-tax.md](./publishing/02-tools/style-references/blog-posts/access-model-hidden-tax.md), [hcc.md](./publishing/02-tools/style-references/short-form-posts/hcc.md) |
| 5 | A seller reaches only the buyers whose cost it is built to carry, and it pays its people for work on that cost. Where little is in the way, pay rewards fast movement from search to contract. Where implementation is in the way, part of the pay waits until the implementation confirms the scope. That holds only where the seller has defined what a complete discovery is. Where it has not, the rep is not paid on an outcome they cannot affect. | The same long post, [comp.md](./publishing/02-tools/style-references/short-form-posts/comp.md), session |

### Time1, contracting

The buyer asks whether its organization can agree, and what the purchase will take. The seller asks whether the deal is worth what it takes. The home cost is consensus.

| # | Claim | Where it was said |
|---|---|---|
| 6 | A purchase is plug-in or built-in. A plug-in purchase works on arrival, and the buyer can walk away from it. A built-in purchase has the buyer build something that works only here. Which one it is decides how much the sale has to do. | [bridge-v-toaster.md](./publishing/02-tools/style-references/short-form-posts/bridge-v-toaster.md) |
| 7 | Implementation is a fear at this point, and it acts through the buyer's own people. A buyer that cannot buy alone needs its organization's scrutiny invited. A demo aimed at one person gives colleagues more to object to. | The same long post, session |
| 8 | A discount moves money and lowers no cost, and it can signal the wrong thing. What lowers the fear is a commitment the seller would not make if it expected to fail, traded for what the buyer knows. | [comp.md](./publishing/02-tools/style-references/short-form-posts/comp.md), session |
| 9 | Work skipped here moves to Time2 and grows. Work pulled forward is paid for by buyers, through a price averaged across deals. | [go-slow.md](./publishing/02-tools/style-references/short-form-posts/go-slow.md), session |

### Time2, renewal

The buyer asks whether it worked here, and whether it is free to leave. The seller asks whether the relationship pays. The home cost is implementation.

| # | Claim | Where it was said |
|---|---|---|
| 10 | Whether the product worked here decides renewal. | [tce-sales-saas.md](./publishing/02-tools/style-references/blog-posts/tce-sales-saas.md) |
| 11 | Lock-in earned by building something together holds. Lock-in made by control is hold-up, where one side squeezes the other once it cannot leave. | [competing-on-value-not-control.md](./publishing/02-tools/style-references/blog-posts/competing-on-value-not-control.md) |
| 12 | Where both sides build something specific, a contract built for partnership does what a discount cannot. | The ACCESS post, session |

---

## 2. What the core does not need

Each of these defends a claim above or answers a reviewer. None is a claim of the author's.

- Positions, the two thresholds per cost and the default edges.
- The hard gate. In session the author described a buyer with a hard-to-move organization seeking a tenfold gain or someone to do the legwork. That has value trading against cost, so a cost is a steep penalty and not a wall.
- The two conditions written as fractions of contract value, beyond the point that price is a transfer.
- Drift rates, the bond condition, the hazard form of the allocation rule.
- The four governance forms as a table, and the split between hostages and allocated rights.
- The realizable, recognized and realized split of value.
- Twenty-two failure modes. One per claim is enough.

---

## 3. Verdicts

**Keep** stays as it is, with names updated. **Shorten** keeps the file and cuts what section 2 lists. **Rewrite** rebuilds the file around the core. **Fold** moves the held ideas into another file and retires the rest. **Retire** removes the file from the tree, and `git show` recovers it.

### theory/01-foundation

| File | Words | Verdict | Reason |
|---|---|---|---|
| `00-tcg-constitution.md` | 7,600 | Rewrite | Becomes section 1: three times, twelve claims, one falsifier each. |
| `01-motions.md` | 5,800 | Rewrite | Home of claim 1. Keep the map onto product-led and sales-led, and the contrast with the relay. |
| `02-mathematical-models.md` | 9,400 | Retire, keep sections 1.1 to 1.4 | Only "price is a transfer" serves a claim. See decision 3. |
| `03-glossary-and-notation.md` | 5,300 | Rewrite | A short glossary of the core's terms. The notation index goes with the math. |
| `04-seller-surplus-model.md` | 2,800 | Fold | The seller's question at each time moves into the Constitution. The equations go. |
| `05-governance-forms.md` | 4,700 | Fold | Claims 5, 11 and 12 move into the Constitution. The forms table and bond condition go. |
| `06-calibration.md` | 5,800 | Rewrite | Keep section 4.1 as a short list of predictions and tests. The parameter tables go with the math. |
| `07-open-questions.md` | 5,000 | Shorten | Keep what bears on a claim, such as 45, 62, 66 and 67. The closed list goes to git history. |
| `08-from-axioms-to-instruments.md` | 5,700 | Retire | Each instrument states its own purpose. |

### theory/02-research

| File | Words | Verdict | Reason |
|---|---|---|---|
| `transaction-cost-economics.md` | 1,400 | Keep | The foundation for all twelve claims. |
| `buyer-cost-neighbors.md` | 3,600 | Shorten | Says what is differentiated. Add the neighbors found in session. |
| `costly-signals.md` | 1,700 | Keep | Claim 3. |
| `channel-collapse.md` | 500 | Keep | Claim 3, the noise. |
| `information-environment.md` | 2,100 | Keep | Claim 4. |
| `buying-center-dynamics.md` | 1,400 | Keep | Claim 7. |
| `process-misfit.md` | 800 | Keep | Claims 2 and 6. |
| `integration-touchpoints.md` | 1,100 | Keep | Claim 2, the workflow first. |
| `fear-of-failure.md` | 800 | Keep | Claim 7. |
| `prospect-theory.md`, `real-options.md` | 900 | Fold into `fear-of-failure.md` | Two short files on why a buyer waits. |
| `incomplete-contracts.md` | 1,500 | Keep | Claim 12. |
| `klein-crawford-alchian.md` | 600 | Fold into `transaction-cost-economics.md` | One idea, hold-up, for claim 11. |
| `game-theory-and-nrr.md` | 400 | Keep | Claim 5, on pay. |
| `cfir.md`, `re-aim-framework.md` | 1,400 | Fold into one file | Implementation science, for claim 10. |
| `value-and-persuasion.md` | 3,300 | Shorten | Keep the evidence on discounts and persuasion for claim 8. |
| `tce-empirical-record.md` | 1,700 | Keep | Records where the theory is weakest. |
| `adversarial-review-2026-11.md`, `research-review-2026-11-09.md` | 5,900 | Retire, keep the review's section 4 | Their responses are applied. The separating predictions and public-data tests move to the predictions list. |
| `00-reading-guide.md`, `README.md` | 1,700 | Rewrite | Map each paper to a claim. |
| `audits/citation-provenance-audit.md` | 3,400 | Shorten | Drop rows for statistics that leave. |

### practice

| File | Words | Verdict | Reason |
|---|---|---|---|
| `00-market-reading.md` | 2,900 | Rewrite | The instrument for claims 1 to 5. Lead with the two signals in claim 2 and the value reading in open question 66. |
| `deal-triage-calculator.md` | 4,000 | Rewrite | Keep the workflow check and the two gates. Drop positions and default edges. |
| `bargaining-ledger.md` | 1,900 | Shorten | Claim 7. Drop the bands and the gap arithmetic. |
| `enforcement-ledger.md` | 2,200 | Shorten | The author's original playbook. Drop the routing fractions. |
| `adoption-review.md` | 2,300 | Shorten | Claim 10. |
| `friction-allocation-diagnostic.md` | 1,400 | Keep | Claim 3 as a test. |
| `README.md` | 700 | Rewrite | Index by time. |

### publishing, models, tools and the root

| File | Verdict | Reason |
|---|---|---|
| `publishing/02-tools/style-references/` | Keep | The record of what went out. |
| Voice guide, protocols, generators, source quotes | Keep | Not theory. Prune quotes whose source leaves. |
| `publishing/README.md` | Rewrite | Content pillars follow the three times. |
| `models/` | Retire | The code checks equations that leave. See decision 3. |
| `tools/linting/` | Keep | Update the retired-terms list for decisions 1 and 4. |
| `README.md`, `CLAUDE.md` | Rewrite | Follow the Constitution. |

---

## 4. Decisions that are the author's

All five were decided by the author on 2026-11-10.

1. **Rename the times.** Decided: rename. Before 7.0 the Constitution called the deal "time 0" and the relationship "time 1". The core uses Time0 for the market, Time1 for contracting and Time2 for renewal. This is a canonical rename and an axiom-level change, so it is Constitution 7.0.
2. **Drop the hard gate.** Decided: drop it. A cost can stop a deal, and value trades against it.
3. **Retire the math and the model code.** Decided: retire, keeping sections 1.1 to 1.4. The standing scope decision already says they stay only while they defend a claim. Two of the five checks, the model tests and the figure check, leave with them, and so do the generated figures unless one or two stay as fixed images.
4. **Name the two kinds of purchase in claim 6.** Decided on 2026-11-10: plug-in and built-in. The author published the toaster and the bridge and has come to find the pair confusing, and the linter already retires it. Theory prose keeps "specific" for the technical term. Define both names at first use, because "plug-in" also names a software add-on.
5. **Retire the two review records.** Decided: retire, once their predictions are copied out.

---

## 5. Order of work

Each pass is one reviewable change with the checks green.

1. The Constitution, the root README and CLAUDE.md, with the rename.
2. Motions and the glossary.
3. The Market Reading and the Deal Triage Calculator.
4. Fold the seller surplus model and the governance forms. Retire the derivation file.
5. The math, the models, calibration and the open questions.
6. Research folds and re-pointing, and the citation audit.
7. The three ledgers, the practice README and the publishing pillars.

<!-- vale TCG.RetiredTerms = YES -->
