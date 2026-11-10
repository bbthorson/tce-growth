# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A knowledge base for **Transaction Cost Growth (TCG)**, a theory of go-to-market built on transaction cost economics: what a deal costs a buyer beyond the price decides how it has to be sold. Search-led, consensus-led and implementation-led are motions inside it, each named after the cost it carries. Turnkey is the market where buyers can carry every cost alone and the purchase is plug-in. `theory/01-foundation/01-motions.md` maps them onto PLG and SLG. Almost all content is Markdown.

| Directory | Function |
|---|---|
| `theory/` | Develop and pressure-test the framework. Axioms, claims, academic backing. |
| `practice/` | Operationalize theory. The instruments the claims name. |
| `publishing/` | Turn the framework into public writing. Voice guide, writing protocols, content generators. |
| `tools/` | The two linters and the Vale style that keep the other directories consistent. Python, no dependencies. |

## Standing scope decisions

Recorded in the Constitution 5.0 proposal, now in git history (`git show b5b3386:CONSTITUTION-5.0-PROPOSAL.md`, section 6).

- **The math is scaffolding.** It keeps the argument honest and the falsifiers checkable, and it is not shown in public writing.
- **Supporting files stay only while they help defend a claim.** The 2026-11 trim applied this to `models/`, to the parameter tables in `06-calibration.md` and to the scores in the ledgers.
- **The audience is founders and revenue leaders, held to academic citation standards.** Health tech supplies the examples, built from public patterns.
- **Every falsifier is written for others to run.** The author's experience supplies hypotheses, not evidence.

Recorded in the trim proposal on 2026-11-10, now in git history (`git show 59ab41e:TRIM-PROPOSAL.md`):

- **The goal is a differentiated point of view for founders and revenue leaders.** The twelve claims in the Constitution are the ones the author holds, most of them already published. Material that defends a claim sits behind it. Do not add machinery to answer an objection unless asked.
- **The math and `models/` retired in the trim.** `02-mathematical-models.md` keeps sections 1.1 to 1.4, which show that price is a transfer. `06-calibration.md` is now a list of predictions and tests.

## Conceptual architecture

**The source of truth is `theory/01-foundation/00-tcg-constitution.md`**, version 7.0: three standing assumptions, a premise, and twelve numbered claims under three axioms. Each axiom covers one time and asks one question of each party. Each claim has a test that could fail and one failure mode. Cite a claim by its number, which is stable.

The premise: buying costs the buyer three things beyond price (search, consensus, implementation), the seller can carry part of each (sales before commitment, account management after), and each party acts on what it can check. Each cost has a home time. Conditions run forward and expectations run backward: the market shapes the deal and the deal shapes the relationship, and a buyer prices a later cost when it makes an earlier decision. A cost can stop a deal, and a large enough gain or someone else doing the work can offset it.

- **I, Composition. Time0, the market.** The buyer asks whether to buy, build or do nothing. The seller asks whether it can serve these buyers at a profit. Claims 1 to 5: the kind of cost in the way decides how to sell, workflow and organizational complexity predict that cost, cheap claims raise every buyer's search cost, rules set a floor, and a seller reaches only the buyers whose cost it is built to carry and pays its people for work on that cost.
- **II, Transaction Investment. Time1, contracting.** The buyer asks whether its organization can agree and what the purchase will take. The seller asks whether the deal is worth what it takes. Claims 6 to 9: a purchase is plug-in or built-in, implementation is a fear that acts through the buyer's own people, a discount moves money and lowers no cost, and work skipped here moves to Time2 and grows.
- **III, Future Cost. Time2, renewal.** The buyer asks whether it worked here and whether it is free to leave. The seller asks whether the relationship pays. Claims 10 to 12: whether the product worked here decides renewal, lock-in earned by building together holds while lock-in made by control is hold-up, and a contract built for partnership does what a discount cannot.

**The repository was trimmed around 7.0 on 2026-11-10,** in seven passes. Every file in `theory/`, `practice/` and `publishing/` now matches the Constitution. The trim removed the seller surplus model, the governance forms, the file that derived the instruments, most of the math, `models/`, the parameter tables, seven research files and the ledgers' arithmetic. All of it is in git history, and files that were cut say which commit holds the longer version. Git history before that date uses ideas 7.0 retired: positions, the two thresholds per cost, the gate, the tightest cost, where the sale starts, the governance forms and the drift rates. Where a file and the Constitution disagree, the Constitution governs.

The dependency chain runs one way: `theory/` → `practice/` → `publishing/`. Changes to theory propagate downstream. Changes to practice or publishing never modify theory.

Read before editing:
- **Any `practice/` file**: `practice/README.md`, for the question each instrument answers and the three-question test every section must pass. For the ledgers and the Adoption Review, also `theory/02-research/implementation-science.md`, section "Where each construct is read", so an edit does not drop a construct. The Deal Triage Calculator (`practice/deal-triage-calculator.md`) is referenced by nearly every instrument. No instrument scores a deal or adds the costs together, so do not add a score, a band or a fraction to one.
- **Any research file**: `theory/02-research/00-reading-guide.md`, which maps each paper to what it backs.
- **Before extending the theory**: `theory/01-foundation/07-open-questions.md`. An extension should land on a recorded gap or add one.

<!-- vale TCG.RetiredTerms = NO -->
Older analyses and git history use readings Constitution 4.0 retired: the friction vector, the summed 0-to-30 level, the Structural deal class, the coefficient 2.25, and the market states. Constitution 7.0 retired the old time labels, where "time 0" was the deal and "time 1" the relationship, along with positions, the gate and the two conditions as equations in the Constitution. `01-motions.md` and the Constitution's version history record what replaced them.
<!-- vale TCG.RetiredTerms = YES -->

## The one piece of accounting

The Constitution holds no equation. It relies on one result from `02-mathematical-models.md` sections 1.1 to 1.4: price is a transfer. What leaves the buyer arrives at the seller, so a discount changes the split and leaves the work of buying the same size. The exception is a price taken under a spend threshold, which removes an approver.

When diagnosing a stall or editing a prescription, name the claim it addresses and the time it sits at.

## Content conventions

Apply the voice rules in `publishing/02-tools/voice-guide.md`. Vale enforces most of them.

- **Component names**: *search*, *consensus* and *implementation* are the names of the three costs. They descend from Dahlman's (search and information, bargaining and decision, policing and enforcement) and differ in two places, which the Constitution's premise states. Cite Dahlman as their origin, and use his names only where a research file discusses his paper. A position in the buyer's coalition is a *decision role*.
- **The times** are written Time0, Time1 and Time2, with no space: the market, contracting and renewal.
- **Plug-in and built-in** name the two kinds of purchase. Define both at first use, because "plug-in" also names a software add-on. Research files keep the economists' word, *specific*.
- **Translate every technical term** in plain English right after first use.
- **Em dashes and semicolons**: at most 30 per file for reference material, 3 for prose written for publication. Restructure into periods rather than raising either limit.
- **Active voice with named actors.** No "It's not X, it's Y" constructions. No hype words, no emojis.
- **The Constitution is claims-first.** A statement that cannot be traced to one of the twelve claims does not belong in it. Operational content belongs in `practice/`.
- **Frontmatter**: every file in `theory/` and `practice/` opens with `title` (matching the H1), `layer`, `status`, optional `version`, `operationalizes` and `canonical_source`. `check_frontmatter.py` enforces the schema. `grep -rl "axiom-1" theory/ practice/` lists everything that claims to derive from an axiom.

## Drift rules

Do each step in the same commit as the change.

- **New headline statistic in `theory/`**: add a row to `theory/02-research/audits/citation-provenance-audit.md` with an honest verification status. When two files disagree on a number, record it there first, then fix both against the primary source.
- **New coefficient, threshold or band edge**: do not add one. The Constitution states no measured quantity. A prediction that only evidence can settle goes in `theory/01-foundation/06-calibration.md`, under a number that is never reused.
- **Changing the accounting**: `02-mathematical-models.md` sections 1.1 to 1.4 hold the only equations left. The price-window figure under claim 8 is a fixed image, so a change there means redrawing it by hand.
- **Renaming anything canonical**: grep the whole repo for the old term, add it to `swap:` in `tools/linting/styles/TCG/RetiredTerms.yml`, and bump the Constitution version and the root README footer together. Then check descriptions, not just names: a paragraph can use every current term and still describe a superseded axiom. `tools/linting/README.md` has the detail.

## Checking your work

Run all three before finishing an edit:

```bash
python3 tools/linting/check_playbook.py && \
python3 tools/linting/check_frontmatter.py && vale .
```

They also run in `.githooks/pre-commit`, which is active only after `git config core.hooksPath .githooks`, and in `.github/workflows/checks.yml` on every pull request and push to `main`.

## Publishing workflow

```
publishing/README.md (content pillars) → voice-guide.md → writing-protocols.md (context check) → {long-form | short-form}-generator.md → style-references/
```

`writing-protocols.md` also holds the AI persona for deal-analysis writing and the trenches protocol for analyzing a specific deal. Style references are published text kept verbatim, so Vale exempts them.
