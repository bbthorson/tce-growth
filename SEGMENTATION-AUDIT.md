# Segmentation Audit

**Status:** proposed 2026-09-21. Steps 1 and 2 of section 6.6 applied 2026-09-22. Steps 3 to 6 are not, and steps 4 and 6 want the author's eyes on each file before they merge.

**Scope:** what the repo currently holds, what repeats, what is stale, and a proposed segmentation to flesh out against. It replaces `RESTRUCTURE-PLAN.md`, whose six steps were all applied and which step 2 below deleted.

| Step | Result |
|---|---|
| 1. Correctness | Applied. The stale threshold, the retired axiom description, the two unsourced read-aloud statistics, the three Reputation Depreciation misattributions and the live plural of a retired term are fixed. The provenance rule now covers `practice/`, and the plural trap has swap rows. |
| 2. Cruft | Applied. `RESTRUCTURE-PLAN.md` and the checked-in `.claude/` memory are deleted, `.claude/` is ignored, the reading guide's stale diagram is gone, the cases README is trimmed and the superseded case is marked. |

The findings below are kept as written, as the record of what was found rather than a description of the tree today.

---

## 1. Where the repo stands

Four Python checks pass on the current head. Vale is not installed in the session this audit was written in, so the fifth check did not run.

| Group | Files | Words | Restructure target | Verdict |
|---|---|---|---|---|
| `theory/01-foundation/` | 9 | 22,800 | 22,000 | Hit |
| `theory/02-research/` | 16 | 8,000 | whole | Hit |
| `practice/` | 12 | 19,200 | 12,000 | Over by 60% |
| `publishing/`, live text | 9 | 4,500 | 17,000 | Under |
| `publishing/style-references/` | 10 | 14,600 | verbatim | Kept by design |
| `models/`, `tools/` | 2 READMEs | 2,600 | unchanged | Fine |

**The headline.** The last restructure aimed at theory, and theory landed on target. Practice did not. It is now the heaviest live layer in the repo, and 3,300 of the 5,400 words inside `practice/implementation-motion/` are the oldest text in the repository by voice and the only text that still disagrees with the axioms. Section 4 covers that.

Per-file, in the two layers that matter:

| File | Words |
|---|---|
| `00-tcg-constitution.md` | 4,678 |
| `01-motions.md` | 3,670 |
| `deal-triage-calculator.md` | 3,484 |
| `02-mathematical-models.md` | 3,388 |
| `03-glossary-and-notation.md` | 3,277 |
| `04-sustaining-adoption-review.md` | 2,152 |
| `04-seller-surplus-model.md` | 2,098 |
| `friction-efficiency-index.md` | 1,934 |
| `05-governance-forms.md` | 1,930 |
| `06-calibration.md` | 1,855 |
| `asymmetry-scorecard.md` | 1,732 |
| `friction-allocation-diagnostic.md` | 1,660 |
| `cfir-field-mapping.md` | 1,624 |
| `milestone-valuation-model.md` | 1,530 |
| `07-open-questions.md` | 1,526 |
| `02-validation-red-team-protocol.md` | 1,458 |
| `consensus-friction-calculator.md` | 1,262 |
| `01-discovery-contextual-blueprint.md` | 991 |
| `03-closing-mutual-implementation-plan.md` | 824 |

---

## 2. The one failure mode worth designing against

The repo has three mechanisms that each stop one kind of drift, and they work:

| Mechanism | Stops |
|---|---|
| `RetiredTerms.yml` | Rename drift |
| `citation-provenance-audit.md` | Statistic drift |
| `tcg_models.py` plus its test suite | Formula drift |

There is a fourth kind of drift and nothing stops it. Call it **scope drift**: a file growing content that belongs to a different kind of document. It is what produced 99,000 words the first time and it is already visible again eleven commits after the restructure finished.

The mechanism is specific and repeatable. A claim is stated in the Constitution. The claim's argument is pushed out to an owning file, and a pointer is left behind. The pointer acquires a sentence of context so the reader does not have to follow it. The sentence becomes a paragraph. The paragraph becomes a corollary with its own mechanism and its own citation, and now the claim has two prose homes that have to be maintained together. Nothing in the tooling can see that happen, because both files pass every check.

**Everything in sections 3 and 5 is one symptom of this.** The proposed segmentation in section 6 is chosen to make it mechanically catchable rather than to tidy the directory tree.

---

## 3. What overlaps

### 3.1 Level and direction, explained eight times

The distinction between the friction vector's length and its heading is the framework's central operational idea, and it carries a full prose explanation in eight files: the root `README.md`, `CLAUDE.md`, the Constitution's Axiom I, `01-motions.md` sections 1 and 3, `05-governance-forms.md` section 6, `03-glossary-and-notation.md`, `02-mathematical-models.md`, and `deal-triage-calculator.md` Step 3. Each one says the same two things in its own words, so a revision to the idea is an eight-file edit and any file missed is a file that now describes a superseded version.

**One prose home, `01-motions.md` section 1.** Everywhere else, a link.

### 3.2 The three pairs, four times

Axiom III's claim that each component has its own pair of parties, and therefore its own gap, is tabulated in `00-tcg-constitution.md` line 128, `01-motions.md` line 133, `02-mathematical-models.md` line 166, and again as a warning callout in `asymmetry-scorecard.md` line 21. Four tables, four column sets, one claim. The math file's version is the most complete and is the one that should survive.

### 3.3 Two registers of open questions

`07-open-questions.md` opens by stating its own rule: "Where a file already carries its own 'what this does not settle' section, the entry here points at it rather than restating it."

It does not do that. Item 9 restates `05-governance-forms.md` section 7 bullet 4. Item 10 restates bullet 2. Item 11 restates bullet 1. Items 14 and 15 restate two bullets of `01-motions.md` section 9. The wordings have already diverged, which is what double maintenance looks like at eleven commits.

Seven files carry a local register of their own gaps: `01-motions.md` section 9, `05-governance-forms.md` section 7, `04-seller-surplus-model.md` Open questions, `02-mathematical-models.md` section 6, `06-calibration.md` sections 4 and 5, `friction-efficiency-index.md` sections 6 and 7, and `models/README.md`.

**Default taken:** one register. `07-open-questions.md` becomes the only prose home, the file-local sections are deleted, and each file links to the register's anchor for its own axiom. The counter-case is that a reader of `05-governance-forms.md` wants the caveats where they stand, and it loses, because the register is grouped by axiom and the axiom index is the one the repo already publishes.

### 3.4 The Constitution's corollary bullets against Part II

Part II is a table titled Derivations. It has fifteen rows, and each row names a derivation, the axiom it follows from, and the file that states it. Immediately above it, the three axioms carry fourteen corollary bullets, and thirteen of those bullets are the same derivations written out again in two to five sentences each, with their own mechanisms and citations.

The bullets are roughly 1,500 words of the Constitution's 4,678, and they are the exact place scope drift reaches first, because a corollary is where a new source gets parked.

**Default taken:** collapse the corollary bullets into rows of the Part II table. The table already names every one of them. The Constitution drops to roughly 3,200 words and lands on the target the last restructure set for it.

### 3.5 Smaller repeats

- **Addressable market as a property of the motion.** Constitution Axiom I corollary, `01-motions.md` section 6, `05-governance-forms.md` section 4. The governance file owns it and the other two should link.
- **Vesting compensation on surviving outcomes.** Constitution Axiom II corollary, `01-motions.md` section 8, `05-governance-forms.md` section 5. Same treatment.
- **Fit verification is not a search blocker.** Constitution Axiom I, `01-motions.md` section 2.1, plus a `RetiredTerms.yml` row. The motions file owns it.
- **Research directory front matter.** `theory/02-research/README.md` and `00-reading-guide.md` both answer "where do I start" and both carry a "what you will not find here" section. Merge into the reading guide and reduce the README to a pointer.
- **The `models/README.md` open-questions section** repeats items 20 and 21 of the register.

---

## 4. Part of the practice layer did not come along

`practice/` was flattened and relinked in the restructure. Three of its four implementation artifacts were moved and never rewritten, so they pass every check while describing a version of the theory that no longer exists. This is the largest correctness problem in the repo and it is invisible to the tooling for a reason section 4.4 gives.

**The affected set is `01-discovery-contextual-blueprint.md`, `02-validation-red-team-protocol.md` and `03-closing-mutual-implementation-plan.md`, and it is not the whole directory.** `04-sustaining-adoption-review.md` was rewritten during the restructure and is clean: it uses the locked numbering correctly ("Axiom II's governance corollary", "Axiom III's second clause"), it consumes the count re-take and Count Variance vocabulary the calculator's 7.0 rebuild introduced, and it carries no Ratio Check. Section 4.7 says why that distinction is the useful one.

### 4.1 A stale threshold

`practice/implementation-motion/01-discovery-contextual-blueprint.md` line 22 gates itself on "Structural classification (score ≥ 10) from Deal Triage Calculator".

The threshold has been 15 since the move to three components on `[0, 10]` each. `01-motions.md` line 97 says so explicitly, and it even records the conversion: "Multiply an archived score by 1.5 to compare it." The Blueprint is carrying the archived number, so as written it admits deals at two-thirds of the intended specificity into the heaviest instrument chain in the repository.

### 4.2 A retired axiom

`03-closing-mutual-implementation-plan.md` line 27 states what it reduces: "Defection risk via mutual skin in the game (Axiom II — Governance)."

Governance stopped being an axiom in Constitution 2.0 and became a corollary of Axiom II. The name Axiom II is now correct and the description attached to it is not, which is precisely the case `CLAUDE.md` warns about under "Renaming anything canonical": "A paragraph can use every current term and still describe a superseded version of an axiom." `RetiredTerms.yml` has a `Law of Governance` row and it cannot fire here, because the text does not use the retired name.

### 4.3 An unsourced statistic in a customer-facing script

`01-discovery-contextual-blueprint.md` line 44 is a passage marked "Read Aloud to Customer":

> "Research consistently shows that two-thirds of enterprise IT projects fail to deliver their promised ROI (Standish Group CHAOS Report, 2020; BCG, 2020)."

`02-validation-red-team-protocol.md` line 96 carries the same claim with the same two citations.

Two problems. The provenance audit's own discrepancy 2 records that "the 2020 figures put challenged plus failed at 69%", and it was written to correct exactly this kind of restatement. And "BCG, 2020" appears nowhere else in the repository: not in `fear-of-failure.md`, not in the provenance audit, not in `source-quotes.md`. It is the only citation in the repo with no traceable home, and it sits in the one passage a seller reads to a buyer verbatim.

### 4.4 Why nothing caught any of this

`CLAUDE.md` states the provenance rule as: "Any quantitative claim added to `theory/` gets a row in the provenance audit in the same commit." The audit's own maintenance section repeats the scope: "A new headline statistic anywhere in `theory/`."

`practice/` is outside the rule. That is a one-line fix and it should go in whatever commit lands first.

### 4.5 A ratio with no derivation

All three pre-signature artifacts open with a section called "Rep Compliance: The Ratio Check", which asks the seller to verify a content split across Business, Product and Technical: 50/30/20 in the Blueprint, 20/50/30 in the Red Team, 10/20/70 in the MIP.

Those nine numbers appear nowhere in `theory/`, have no row in `06-calibration.md`, and are not asserted by any test. `test_tcg_models.py` asserts that every numeric constant in the module is declared on the calibration page, which is the rule that keeps numbers honest, and these numbers are not in the module so the rule never sees them. They are either a field heuristic that deserves a calibration row marked **Chosen**, or they are residue from the sales-enablement era and should go. They read as the second.

### 4.6 Voice

The three artifacts are the only files in the repo that use the football register ("The Ratio Check", "Honesty Hour", "The Ghost Town Risk", "Skin in the Game") outside `publishing/style-references/`, which is exempt from lint by design because it is a verbatim record. Everything else in `theory/` and `practice/` has been rewritten into the flat, forensic voice the Constitution uses. The gap is visible to any reader who opens a foundation file and a field artifact in the same sitting.

### 4.7 What actually predicts which files rotted

`test_tcg_models.py` carries a section banner naming each document it asserts. Five practice files have one: `deal-triage-calculator.md`, `asymmetry-scorecard.md`, `consensus-friction-calculator.md`, `milestone-valuation-model.md` and `friction-efficiency-index.md`. Those five are the five that are current. Nothing in the suite names `implementation-motion/01`, `02` or `03`, and those three are the three that rotted.

The correlation is not quite causal, and `04-sustaining-adoption-review.md` is the case that shows why. Nothing asserts it either, and it is clean, because it was actually rewritten in step 3 of the restructure. So the rule is not that untested files rot. It is that **an untested file which also skipped a rewrite has nothing at all holding it to the theory**, and both conditions were true of exactly three files.

Two consequences. A rebuild of those three should produce something the suite can assert, which means each artifact needs at least one worked example tied to a term in the equation. And `04` is the template: it is the one artifact that has already made the transition from rep collateral to author-facing specification, so it shows what the other three should look like when they are done.

### 4.8 Two defects the axiom rename left behind

Neither is in the three artifacts, and one is in `theory/`.

**Reputation Depreciation is attributed to the wrong axiom in three places.** The Constitution puts it under Axiom III, both as a corollary at line 164 and as a row of the Part II table at line 190, and `03-glossary-and-notation.md` line 199 agrees. Three files still call it Axiom II: `friction-allocation-diagnostic.md` lines 108 and 168, and `04-seller-surplus-model.md` line 141. This is the Constitution 2.0 renumbering, where Uncertainty Inflation moved from II to III, not fully swept.

**A retired term is live because of a plural.** `friction-allocation-diagnostic.md` line 16 reads "The four principles are primary derivations of Axiom III." The derivation tiers were removed in Constitution 2.0 and `RetiredTerms.yml` carries a `primary derivation` row for exactly this. It does not fire, because the rule anchors on word boundaries and the boundary after "derivation" is not one in "derivations". Worth adding the plural to the swap list in the same commit, since the same trap applies to several other rows.

**Default taken:** the defects in 4.1 through 4.3 and 4.8 are correctness and should be fixed immediately, in their own small commit, before any restructuring. The ratio check and the voice are editorial and belong in the rebuild, because deciding them means deciding what a field artifact is allowed to contain, which is what section 6 decides.

---

## 5. Stale cruft

Each of these is a cheap delete with no downstream reader.

| Item | Why it goes |
|---|---|
| `RESTRUCTURE-PLAN.md` | All six steps applied. It is now a second, contradicting description of the repo: it reports the Constitution at 9,400 words and targets about 40 files, neither of which is true. The Constitution's version history table already carries the record. |
| `.claude/projects/-Users-brad-htd-Code-ilg-playbook/memory/` | Three memory files checked in at v12, keyed to a local machine path from the ILG era. One of them plans to "add Theory basis declarations after axiom restructuring is settled", which the `operationalizes` frontmatter field has since done. Delete and add `.claude/` to `.gitignore`. |
| The ASCII diagram in `theory/02-research/00-reading-guide.md` | It puts NRR at the top of the stack over CFIR and RE-AIM, which is the pre-axiom reading. The guide below it references "three sources added in Constitution v13", a numbering that no longer exists. The diagram now contradicts the per-axiom backing table the Constitution publishes in its Related section. Redraw it by axiom, or drop it and keep the numbered "read after X" notes, which are still correct. |
| `publishing/01-cases/` | Two scouting reports totalling 47 lines, behind a 27-line README explaining the directory. `hcti-teyame-scouting-report.md` frames the analysis on `$\Delta_A$ and $F_{base}$`, which is the single-multiplier reading retired in v17.0. Keep the cases as raw material, but the README should shrink to a header, and the hcti frame should be corrected or the file marked as archived. |

---

## 6. Proposed segmentation

### 6.1 The principle

**Segment by document contract, not by topic.** What a file promises a reader determines how long it is allowed to be and what it is allowed to contain. Six contracts cover the repo:

| Contract | Promises | Rule |
|---|---|---|
| **Canon** | The claims, and only the claims | One statement, one mechanism, one falsifier, one pointer per claim. No derivations, no worked examples, no instruments. Word cap. |
| **Reference** | Exhaustive lookup | Never read linearly, so length does not matter. States, does not argue. |
| **Argument** | An extension that stands on its own | Downstream of canon, explicitly not part of it, free to be wrong on its own terms. |
| **Instrument** | Something you fill in on a live deal | Inputs, steps, outputs, scoring sheet. One "why this exists" line and no more theory prose. |
| **Evidence** | Where a claim came from | Sources, abstracts, what each backs. No synthesis, no numbers without a provenance row. |
| **Production** | Turning the framework into public writing | Unchanged. This layer works. |

The contract is what makes scope drift catchable. A corollary that grows a mechanism inside a canon file is a contract violation, not a judgment call, and a linter can see part of it.

### 6.2 The tree

```
theory/
  canon/
    constitution.md            axioms, standing assumptions, derivations table,
                               surplus equation, failure modes.  Cap 3,000 words.
    motions.md                 the region derivation and the incumbent map.
                               Cap 3,000 words.
  reference/
    notation.md                from 03-glossary-and-notation.md
    models.md                  from 02-mathematical-models.md
    calibration.md             from 06-calibration.md
  arguments/
    seller-surplus.md          from 04-seller-surplus-model.md
    governance-forms.md        from 05-governance-forms.md
  evidence/                    from 02-research/, contents unchanged
    reading-guide.md
    <the 15 source files>
    citation-provenance-audit.md
  open-questions.md            the single register, at the theory root

practice/                      stays flat, see 6.3
  deal-triage-calculator.md
  asymmetry-scorecard.md
  consensus-friction-calculator.md
  milestone-valuation-model.md
  friction-efficiency-index.md
  friction-allocation-diagnostic.md
  cfir-field-mapping.md
  implementation-motion/
    01..04 unchanged in shape, rewritten per section 4

publishing/                    unchanged
models/  tools/                unchanged
```

### 6.3 Three decisions inside that, and why

**Named directories instead of numeric prefixes, in theory only.** The numbering implies a reading order nobody follows: nothing is gained by reading the math models between the motions and the glossary, and the foundation README already admits this by annotating three files "*(reference)*" inline. The numbering also costs real churn. `RetiredTerms.yml` carries six rows that exist only to record foundation renumbers, from `03-mathematical-models.md` through `08-calibration.md`, and every future insertion adds more. Named directories end that permanently.

**`practice/` stays flat.** The last restructure flattened it on the grounds that twelve files do not earn a directory split, and that reasoning still holds. The contract split inside practice is instrument against design reference, which is two kinds across two files, and the README table already carries it.

**`open-questions.md` sits at the theory root, not inside canon.** It is the register for all three contracts below it, and putting it inside any one of them makes it look like it belongs to that one.

### 6.4 Making the contract mechanical

Add a `kind:` field to the frontmatter schema, taking one of the six values in 6.1, and teach `check_frontmatter.py` three rules:

1. `kind` must match the directory, the way `layer` already must.
2. A `canon` file over its word cap fails.
3. A `canon` file containing a worked example, a scoring table, or a parameter default fails. Those belong to reference or instrument.

Rules 1 and 2 are mechanical. Rule 3 needs a heuristic and will have false positives, so it should start as a warning. Even as a warning it is the thing that would have caught the Constitution's corollaries regrowing.

This is the same trick the repo already runs three times. Name the drift, then give it a file or a check that fails when it happens.

### 6.5 Migration notes

- `check_frontmatter.py` hardcodes `theory/01-foundation/00-tcg-constitution.md` when it compares the Constitution version against the root README footer. That path changes with the move.
- `.vale.ini` scopes the punctuation rules by directory and needs the new paths.
- Every moved file gets a `RetiredTerms.yml` row for its old path, per the standing rule.
- The four Python checks should be green at each step, and each step below is one commit.

### 6.6 Suggested order

| Step | What | Risk |
|---|---|---|
| 1 | **Applied.** Correctness: the defects in 4.1 to 4.3 and 4.8, extend the provenance rule to `practice/`, add the plural to the `primary derivation` swap row | None. No structure touched. |
| 2 | **Applied.** Cruft: everything in section 5 | None. |
| 3 | Deduplicate: sections 3.1, 3.2, 3.3, 3.5. One prose home each, links elsewhere | Low. Mechanical, reviewable per claim. |
| 4 | Constitution corollaries into the Part II table, section 3.4 | Needs your eyes. It is the text the rest of the repo is held to. |
| 5 | Move to the tree in 6.2, add `kind:` and the linter rules in 6.4 | Low but wide. Touches every link. |
| 6 | Rebuild `implementation-motion/` 01 to 03 against the locked axioms, using 04 as the template, sections 4.5 to 4.7 | Needs your eyes. It decides what a field artifact contains. |

Steps 1 and 2 are applied. Steps 3 through 6 remain, and steps 4 and 6 want your read on each file before it merges.

---

## 7. What this audit does not decide

- **Whether the seller surplus model belongs here at all.** The last plan deferred this and it is still open. Putting it under `arguments/` makes the question askable without answering it, which is the point of that directory.
- **Whether the consensus region gets an instrument.** Register item 2 calls it the largest gap in the framework. It is the biggest piece of new writing available and nothing in this audit touches it.
- **Whether `tcg_models.py` at 64 KB is itself bloated.** Unchanged from the last plan. Out of scope.
- **Whether to rename the repo.** The directory is `tce-growth`, the framework is TCG, the first commit called it ILG. Three names, still.
