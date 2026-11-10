# Transaction Cost Growth (TCG) Knowledge Base

**A theory of go-to-market built on transaction cost economics: what a deal costs a buyer beyond the price decides how it has to be sold.**

---

## What is TCG?

Buying costs more than money. Finding a seller to trust, getting your own organization to agree, and making the product work in your own environment are three separate bills. The field calls them *search*, *consensus* and *implementation*.

> **The kind of cost in the buyer's way decides how to sell. Most teams pick a playbook because it is in fashion, and run it whatever the buyer faces.**

A buyer and a seller make three decisions in order: whether to enter a market, whether to sign, and whether to renew. Each cost has a home at one of those times. Conditions run forward, so the market shapes the deal and the deal shapes what the relationship has to manage. Expectations run backward, so a buyer prices a later cost when it makes an earlier decision.

The motions are named for the cost they carry: search-led, consensus-led and implementation-led. Product-led and sales-led name the seller's tool and say nothing about the buyer. The relay model, with one role per funnel stage and pay on bookings, is the right motion for a market where buyers can carry every cost alone, and the wrong one elsewhere. [01-motions.md](./theory/01-foundation/01-motions.md) maps the incumbent names.

The theory is twelve claims, each with a test that could fail. None is confirmed on booked deal data. The [Constitution](./theory/01-foundation/00-tcg-constitution.md) states them, and if this file and the Constitution ever disagree, the Constitution wins.

---

## Start here: three times, two parties

| Axiom | Time | The buyer asks | The seller asks | Claims |
|---|---|---|---|---|
| **I. Law of Transaction Cost Composition** | Time0, the market | Buy, build or do nothing? | Can I serve these buyers at a profit? | 1 to 5 |
| **II. Law of Transaction Investment** | Time1, contracting | Can my organization agree, and what will this take? | Is this deal worth what it takes? | 6 to 9 |
| **III. Law of Future Cost** | Time2, renewal | Did it work here, and am I free to leave? | Does the relationship pay? | 10 to 12 |

**Time0.** Which cost is in the way is a fact about the market. Two things a leader can see predict it before any deal: how settled and how entangled the buyers' workflow is, and how complex their organizations are. A claim that costs nothing to make raises every buyer's search cost. Rules set a floor that no seller lowers alone. A seller reaches only the buyers whose cost it is built to carry, and it pays its people for work on that cost.

**Time1.** A purchase is *plug-in* or *built-in*. A plug-in purchase works on arrival and the buyer can walk away. A built-in purchase has someone build something that works only here. Implementation is a fear at this point, and it acts through the buyer's own people, so the seller invites the organization's scrutiny. A discount moves money and lowers no cost. Work skipped here moves to Time2 and grows.

**Time2.** Whether the product worked here decides renewal. Lock-in earned by building something together holds, and lock-in made by control is hold-up. Where both sides build something specific, a contract built for partnership does what a discount cannot.

---

## How this repo is organized

| Function | Where | What it is |
|---|---|---|
| **[theory/](./theory/)** | `theory/01-foundation/` + `theory/02-research/` | The Constitution and what backs it. |
| **[practice/](./practice/)** | `practice/` | The instruments, one or more per time. |
| **[publishing/](./publishing/)** | `publishing/02-tools/` | The voice guide, the writing protocols, and the published posts kept verbatim. |
| **[tools/](./tools/)** | `tools/linting/` | The link, frontmatter and style checkers. |

**A trim is in progress.** Constitution 7.0 rewrote the theory around the twelve claims on 2026-11-10. The other files are being brought into line in passes, and until a file's pass it may still describe ideas 7.0 retired. [TRIM-PROPOSAL.md](./TRIM-PROPOSAL.md) lists the verdict on each file and the order of work.

---

## Looking for something specific

| If you want to... | Go here |
|---|---|
| Read the twelve claims | [00-tcg-constitution.md](./theory/01-foundation/00-tcg-constitution.md) |
| See how the motions map onto product-led and sales-led | [01-motions.md](./theory/01-foundation/01-motions.md) |
| See the evidence behind a claim | [theory/02-research/00-reading-guide.md](./theory/02-research/00-reading-guide.md) |
| See what the theory has not settled | [07-open-questions.md](./theory/01-foundation/07-open-questions.md) |
| Read a market before picking a playbook | [practice/00-market-reading.md](./practice/00-market-reading.md) |
| Read a live deal | [practice/deal-triage-calculator.md](./practice/deal-triage-calculator.md) |
| Write about TCG publicly | [publishing/02-tools/](./publishing/02-tools/) |

---

## Contributing

After cloning, turn on the pre-commit hook so the checks run on every commit:

```bash
git config core.hooksPath .githooks
```

To run them by hand:

```bash
python3 tools/linting/check_playbook.py && \
python3 tools/linting/check_frontmatter.py && vale .
```

Theory changes flow downstream to practice and publishing, never the reverse. [CLAUDE.md](./CLAUDE.md) lists the drift rules: what must be recorded in the same commit as a new statistic, a rename or an equation change.

---

**Version:** 7.0 (tracks the [Constitution](./theory/01-foundation/00-tcg-constitution.md) version; bump both together)
**Last updated:** 2026-11-10
