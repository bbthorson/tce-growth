# Transaction Cost Growth (TCG) Knowledge Base

**A theory of go-to-market built on transaction cost economics: what a deal costs a buyer beyond the price determines how it can be sold, and often whether it can be sold at all.**

---

## What is TCG?

Buying costs more than money. Finding a solution, getting your own organization to agree, and installing the thing without breaking something are three separate bills, and a buyer pays all three before they see any value. **Transaction Cost Growth is the claim that those three costs, not the product and not the pitch, determine which go-to-market motion a deal can support.**

> **Any one cost can keep a buyer out of the market, and ease on the other two never buys it back. Among the costs a buyer will bear, the one nearest its own threshold is where the sale starts.**

Part of each cost is out of any one seller's reach. Channel noise, the buyer's procurement and compliance rules, and outcomes nobody can attribute are set by the market a seller sells into. That part is the cost's *cost floor*, and it falls only through investment shared across deals, such as a marketplace, a certification or a standard. So the first go-to-market decision is where to sell.

The named motions are named after the cost a seller pays down first, and they are not competing philosophies. A sale that starts at finding and comparing is search-led. One that starts at getting the buyer's own people to decide is consensus-led. One that starts at whether the seller will deliver and the product will work here is implementation-led. A market where the buyer needs no seller help at all is [Turnkey](#turnkey-and-routing-outside-it). The familiar labels only partly line up. Sales-Led Growth is narrower than search-led, Product-Led Growth overlaps Turnkey without equaling it, and consensus-led has no established name at all, which is a finding rather than an omission. [01-motions.md section 10](./theory/01-foundation/01-motions.md) carries the map. Choosing between these motions as though they were strategies is choosing a label before measuring the thing the label is supposed to describe.

Three axioms carry the argument, each answering one question at one level: can a market exist, what has to be paid down at time 0, and what prevents churn and contraction at time 1. One premise sits under all three. The seller can absorb part of each cost the buyer carries, which is what sales and account management are, and each party acts on what it can check. The axioms are stated [below](#start-here-the-three-axioms).

Value sits above the axioms as a standing assumption. What the change can be worth to a buyer, its *realizable value*, is set by the offer and the buyer's situation. Within the sale the seller moves only the buyer's *recognized value*, its estimate of that worth. Evidence the buyer can check narrows the estimate and lowers the search cost. A claim that inflates it is persuasion, and the buyer carries the gap as a future cost until delivery exposes it. A discount moves surplus between the parties. Verification adds to it, but only when it lowers a loss both sides carry by more than the verification costs.

Everything in this repository derives from the axioms, and the derivation is checked rather than asserted: every equation has an implementation in [`models/`](./models/), every worked example is tested against it, and every headline statistic carries a provenance row.

**The numbers are held separately from the claims.** Every coefficient, threshold and band edge sits in [the calibration layer](./theory/01-foundation/06-calibration.md) with an honest provenance status, and none of them is fitted to booked deal data. The framework is coherent rather than confirmed, it says what would confirm it, and it is built so that doubting a number does not require doubting the structure the number sits in.

---

## How this repo is organized

The repo serves **three functions**, each in its own top-level directory, plus two directories holding the equations in code and the checkers.

| Function | Where | What it is |
|---|---|---|
| **[theory/](./theory/)** | `theory/01-foundation/` + `theory/02-research/` | Develop and pressure-test the TCG framework. Academic papers, axioms, definitions. |
| **[practice/](./practice/)** | `practice/` + `practice/implementation-motion/` | Operationalize the theory. The instruments the axioms name, and the measurement tools the tests assert. |
| **[publishing/](./publishing/)** | `publishing/02-tools/` | Turn the framework into public writing. Voice guide, writing protocols, content generators. |
| **[models/](./models/)** | `models/` | Executable forms of the equations, their tests and the figure generator. Python, no dependencies. |
| **[tools/](./tools/)** | `tools/linting/` | The link, frontmatter and style checkers. |

Each has a README listing what is inside it. For `tools/` it is [tools/linting/README.md](./tools/linting/README.md).

> [!NOTE]
> **The practice layer is frozen.** Constitution 6.0 is in force, and every file in `practice/` still derives from 4.1. Each one is marked `under-review` and stays as written until the layer is rebuilt from the current axioms. [CONSTITUTION-5.0-PROPOSAL.md](./CONSTITUTION-5.0-PROPOSAL.md) records the ten review decisions behind 5.0 and the rebuild step, and [CONSTITUTION-6.0-PROPOSAL.md](./CONSTITUTION-6.0-PROPOSAL.md) records the 6.0 restatement. Both retire to git history once the rebuild lands. Read an instrument's numbers and routing as 4.1 until then.

---

## Start here: the three axioms

Find the question you are asking, then open what the row points to. Each row condenses the statement in the [Constitution](./theory/01-foundation/00-tcg-constitution.md), and if the two ever disagree, the Constitution wins.

| Axiom | Question | Statement, condensed | Go here |
|---|---|---|---|
| **I. Law of Transaction Cost Composition** | Can a market exist? | Each side has a limit. A buyer enters only while every cost it expects to carry, after what the seller absorbs, sits below what it will bear, and easing the other two costs does not bring back one above it. A seller enters only while its cost of sale is repaid over the relationship. Part of each cost is set outside any deal. | [Deal Triage Calculator](./practice/deal-triage-calculator.md), then [01-motions.md](./theory/01-foundation/01-motions.md) |
| **II. Law of Transaction Investment** | What has to be paid down at time 0? | The cost the buyer expects nearest its limit decides whether it proceeds at all, so the seller absorbs that one first, in fact and in what the buyer can see. That cost names the motion. Each party goes ahead only if its own share is covered by its own return. Seller spending adds value only when it is cheaper than the buyer's own work or lowers the cost at time 1, so without retention it is a price cut. | [Contextual Blueprint](./practice/implementation-motion/01-discovery-contextual-blueprint.md), [04-seller-surplus-model.md](./theory/01-foundation/04-seller-surplus-model.md) |
| **III. Law of Future Cost** | What prevents churn and contraction at time 1? | Whatever a party sinks that pays off only in this relationship exposes it to what it cannot check or stop later. Time 1 is decided at time 0: the parties contract for what they can foresee and plan a standing review for what they cannot, because what was verified goes stale and fit drifts. | [Red Team](./practice/implementation-motion/02-validation-red-team-protocol.md), [MIP](./practice/implementation-motion/03-closing-mutual-implementation-plan.md), [05-governance-forms.md](./theory/01-foundation/05-governance-forms.md), [Sustaining Adoption Review](./practice/implementation-motion/04-sustaining-adoption-review.md) |

The field calls the three costs *search*, *consensus* and *implementation*, and the notation keeps those subscripts.

Two corollaries added in 5.0 carry much of the practical weight. Under Axiom I, **every cost has a cost floor**, the part introduced above that no seller lowers within one deal. Under Axiom III, **enforcement governs what verification cannot**: a party that can see the other side refuse to adapt and cannot stop it is protected by something the other side loses by defecting, such as a bond, staged fees or a reciprocal specific investment, or by a right settled in advance, such as an option to renew at a preset price. Either one changes what defection costs at every later boundary, which a one-off discount does not.

## Looking for something specific

| If you want to... | Go here |
|---|---|
| Understand the theory cold | [theory/01-foundation/](./theory/01-foundation/) |
| Look up a symbol or term | [03-glossary-and-notation.md](./theory/01-foundation/03-glossary-and-notation.md) |
| See the evidence behind a claim | [theory/02-research/00-reading-guide.md](./theory/02-research/00-reading-guide.md) |
| Decide whether to invest engineering in a deal | [04-seller-surplus-model.md](./theory/01-foundation/04-seller-surplus-model.md) |
| Compute a formula | [models/](./models/) |
| See which questions the theory has not settled | [07-open-questions.md](./theory/01-foundation/07-open-questions.md) |
| Write about TCG publicly | [publishing/02-tools/](./publishing/02-tools/) |

**Orientation lives in two places only:** this file, and [the research reading guide](./theory/02-research/00-reading-guide.md). Every other README is a local index of its own directory.

---

## Core concepts at a glance

### The two conditions

$$S_b = V_{switch}(t) - P - \sum_k I^b_k - L_b > 0 \qquad S_s = P - C_{deliver} - \sum_k I^s_k - L_s > 0 \qquad r_k \le 1 \;\; \forall k$$

- **$S_b$, $S_s$** = the buyer's and the seller's surplus. A deal closes only when both are positive. All terms are fractions of annual contract value.
- **$V_{switch}(t)$** = $\tilde{V}_{solution} \cdot e^{-\delta t} - V_{next\_best}$, the buyer's opportunity cost of staying put, decaying at rate $\delta$ after the triggering event. It is read on recognized value, the buyer's estimate, because that is what the buyer decides on.
- **$P$** = price over the relationship. It appears in both conditions and cancels when they are added, because price is a transfer and not a transaction cost.
- **$I^b_k$, $I^s_k$** = what the buyer and the seller invest today against cost $k \in \{search, consensus, implementation\}$ (Axiom II)
- **$L_b$, $L_s$** = each party's expected future loss, its specific exposure times the chance the exposure does not come back (Axiom III).
- **$r_k$** = where cost $k$ sits between the level the buyer can pay down alone and the level that keeps the buyer out. Above 1, the buyer does not enter the market (Axiom I). The sale starts at the largest (Axiom II).

The equations are in [Constitution Part II](./theory/01-foundation/00-tcg-constitution.md).

### Turnkey, and routing outside it

Turnkey is a market condition, not a deal class: every cost low enough for the buyer to pay down alone, and nothing specific sunk. It does not last on its own. The low investment that defines it invites entrants, and entrants raise the search cost. Outside it, a deal routes on two readings. The column split is the gate under Axiom III: where nothing specific is sunk and a trial verifies fit, the future cost is near zero and market terms hold.

| | **Nothing specific sunk** | **Something specific sunk** |
|---|---|---|
| **Every cost self-serve** | Turnkey. Self-serve and standard terms | Light sale, heavy contract. Staging and stop rights agreed before the investment is sunk |
| **Some cost needs seller investment** | Heavy sale, light contract. The seller pays down search or decision costs, then standard terms hold | The full implementation chain |

---

## Contributing

After cloning, turn on the pre-commit hook so the checks run on every commit:

```bash
git config core.hooksPath .githooks
```

To run them by hand:

```bash
python3 tools/linting/check_playbook.py && \
python3 tools/linting/check_frontmatter.py && \
python3 models/test_tcg_models.py && \
python3 models/make_figures.py --check && vale .
```

Theory changes flow downstream to practice and publishing, never the reverse. [CLAUDE.md](./CLAUDE.md) lists the drift rules: where a new statistic, constant, equation change or rename must be recorded in the same commit.

This is a living document. As you work:
- Refine field assets in [practice/](./practice/) based on what works.
- Update research with new evidence.

---

**Version:** 6.0 (tracks the [Constitution](./theory/01-foundation/00-tcg-constitution.md) version; bump both together)
**Last updated:** 2026-11-03
