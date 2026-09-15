# Restructure Plan

**Status:** approved 2026-09-15. Steps 1 to 3 are applied on this branch. Step 4, the Constitution rewrite, waits on the axiom discussion.

| Step | Commit | Result |
|---|---|---|
| 1. Housekeeping and publishing | applied | Concept map deleted, protocols merged, hook and CLAUDE.md defects fixed, README reduced-form notation corrected. |
| 2. Practice cut and flatten | applied | Ten files deleted, practice flattened to one directory, linters moved to `tools/`, CFIR mapping moved to practice, scorecard and index moved out of internal-ops. |
| 3. Theory merges | applied | Three motion files merged into `01-motions.md`, foundation renumbered 00 to 06, Constitution version history reduced to a table, reading guide and glossary trimmed, triage calculator and adoption review compressed. |
| 4. Constitution rewrite | pending | Needs the author's agreement on each axiom first. |

Where the applied steps landed against the targets below: live text (excluding verbatim published posts) went from about 84,000 words to about 59,000. Theory is 37,000 against a target of 22,000, and the remaining 15,000 is almost entirely the Constitution, which step 4 addresses. The triage calculator landed at 3,500 words rather than 2,000, because its tables are the instrument and the cut took prose only. The adoption review landed at 2,100 rather than 1,500 for the same reason.
**Audience for the trimmed repo:** the author, who needs a tight, defensible theory to publish from. A seller who needs to run a deal this week is not the audience, and that decision sets what counts as fat.

## 1. Where the repo stands

| | First commit (2025-11-24) | Today (2026-09-15) | Target |
|---|---|---|---|
| Markdown files | 18 | 83 | about 40 |
| Words, all files | about 5,000 | about 99,000 | about 52,000 |
| Words, excluding verbatim published posts | about 5,000 | about 84,000 | about 37,000 |
| Constitution | about 500 words | 9,400 words | about 3,000 words |
| Theory foundation files | 3 | 11 | 8 |
| Practice files | 8 | 26 | 12 |

The five machine checks pass on the current head, Vale included.

## 2. Diagnosis

Four things happened over 104 commits, and each one is defensible on its own. Together they buried the theory.

- **The axioms grew by accretion.** Each research file added since launch contributed a paragraph to an axiom. Axiom I now carries the friction vector, frequency, governance form, the decay clock, Klein-Crawford-Alchian exposure and four failure modes. It is 1,500 words. An axiom should state one claim, its mechanism, its mathematical content and its citation.
- **Motion selection is explained three times.** The motion taxonomy, the friction vector and the motion vocabulary total 5,500 words. The friction vector already declares that it superseded parts of the taxonomy.
- **The practice layer was built for a sales org that does not exist yet.** Comp plans, a veto policy, a manager forensic checklist, call scripts, order forms and a calibration workshop are 11,000 words of operating procedure for a team of reps. They are also the least defensible material in the repo, because none of it has been run.
- **The publishing layer kept a stale map.** The concept map still carries the Implementation-Led Growth title, the retired market phases, a PARIHS layer the theory dropped, and eight headline statistics with no provenance rows.

Two housekeeping defects surfaced while surveying:

- `.githooks/pre-commit` calls `models/test_ilg_models.py`, which no longer exists. The hook has been failing silently on step 3, or the hook is not installed.
- `CLAUDE.md` says friction vector section 10 records what adoption retired. The file ends at section 9.

## 3. Target shape

### Theory: 42,000 words to about 22,000

**Constitution, 9,400 to about 3,000.** One page per axiom. Each axiom keeps its statement, plain-English translation, mechanism with citation, mathematical content and operating instruction. Everything else moves to the file that owns it:

- Frequency and governance form move to the governance forms file, which already exists to hold them.
- The friction vector math moves to the merged motions file.
- The Klein-Crawford-Alchian paragraph moves to the seller surplus model, which is its home.
- Failure modes collapse into the single table in Part III. Four per axiom is a list, one table is a falsification test.
- Part II becomes a table: derivation, which axioms it follows from, where it is stated. The prose derivations already live in the files the table points to.
- Version history, 1,650 words, becomes a five-line pointer to the git log and the RetiredTerms file.

**Motions, three files to one.** The friction vector is the derivation and survives as the spine. The taxonomy's motion specifications become a section in it. The taxonomy's exclusion criteria and operational checklist are practice content and move to the triage calculator or go. The motion vocabulary's map onto Product-Led and Sales-Led becomes a closing section of about 600 words.

**Math and calibration stay.** They are the defensibility spine and the tests run against them. One merge: the parameter reference in the mathematical models file duplicates the calibration page. The calibration page wins.

**Seller surplus and governance forms stay.** Both are genuine theoretical extensions with their own research backing, and the Constitution rewrite pushes material into them rather than out of them.

**Glossary stays, trimmed.** The notation index is canonical and stays whole. The term index loses every entry whose source file is cut.

**CFIR field mapping moves to practice.** It exists to tell someone modifying a field asset which research construct each section operationalizes. That is an artifact-design document, and it sits next to the artifacts.

**Research stays whole.** Fifteen files, each under 1,300 words, each with a stated job in the reading guide, each cited from the foundation. The reading guide loses its "Implementation-Led Growth" narrative paragraph and its audience table for sales enablement. The provenance audit stays because it is the instrument that makes any number in this repo quotable.

### Practice: 32,000 words to about 12,000

**Keep** because theory cites it, the tests assert it, or it is one of the original three artifacts:

| File | Reason | Action |
|---|---|---|
| Deal Triage Calculator | 22 links from theory, tested | Compress 4,200 to about 2,000. Cut the manager calibration questions and the common mistakes section. Keep the counting instrument, scoring sheet and routing. |
| Milestone Valuation Model | 10 links, tested | Keep |
| Bilateral Asymmetry Scorecard | 8 links, tested | Keep. Move out of internal-ops incentives, where a measurement instrument does not belong, into field assets. |
| Consensus Friction Calculator | Tested | Keep |
| Friction Efficiency Index | 7 links, tested | Keep, trimmed. It is the only instrument that could falsify Axiom III after the fact. |
| Contextual Blueprint, Red Team Protocol, Mutual Implementation Plan | The original three artifacts | Keep |
| Sustaining Adoption Review | The relationship-state instrument | Compress 2,500 to about 1,500 |
| Friction Allocation Diagnostic | Operationalizes Axiom II's four principles | Keep |

**Delete**, about 11,000 words of operating procedure with no theoretical content the surviving files lack:

- `costly-signal-discovery-scripts.md`, call scripts
- `structural-deal-calibration-checklist.md`, AE and SE pre-close self-audit
- `turnkey-motion/` all three files, order protocol, order form, prospect evaluation
- `search-motion/01-education-motion.md`, which its own README calls deliberately thin
- `consensus-motion/README.md`, which documents that nothing exists there. One sentence in the motions file says the same.
- `00-setup-implementation-guide.md`, calibration workshop
- `02-governance-review-checklist.md`, manager forensic checklist
- `03-incentives-vested-commission.md`, comp plan addendum
- `06-governance-implementation-veto.md`, veto policy
- `07-variable-ownership.md`

Anything in a deleted file that an axiom depends on gets checked before deletion. The vested commission file is the only one with a claim to that: it descended from the original Axiom VI. The claim it carries, that compensation must vest on outcomes for Axiom III's cooperation condition to hold, becomes one paragraph in the governance forms file.

**Flatten.** With 12 files, the field-assets and internal-ops split stops earning its README pair. One `practice/` directory with the implementation chain as its only subdirectory.

### Publishing: 19,800 words to about 17,000

- **Style references stay verbatim.** 15,000 words, zero inbound links, exempt from lint by design. They are the published record and cost nothing to keep.
- **Delete the concept map.** Its one live asset, the content pillars, becomes a short section of the publishing README. Its eight statistics either get provenance rows or go.
- **Voice guide stays.** It is the rule set the linter enforces.
- **Merge the small tools.** The AI persona, context request protocol and trenches protocol are 700 words across three files. One `writing-protocols.md`. The two generators stay as they are.
- **Cases stay.**

### Tooling

- Move `tools/linting/` to a top-level `tools/` directory next to `models/`. The linter guards the whole repo and does not belong under practice. This touches `.vale.ini`, the pre-commit hook, `CLAUDE.md` and the root README. Optional, but the practice flatten is the moment to do it.
- Fix the pre-commit hook's stale test filename.
- Fix the section 10 reference in `CLAUDE.md`.
- No model code or tests are removed. Every file the tests assert survives the cut list. The triage calculator compression keeps every worked example the suite checks.
- Every deleted file's title and every merged file's old name goes into `RetiredTerms.yml`.

## 4. Sequence

Four commits on this branch, each leaving the five checks green, each one reviewable on its own. Later steps depend on earlier ones only where noted.

1. **Housekeeping and publishing.** Hook fix, `CLAUDE.md` fix, concept map deletion, small-tools merge. Low risk, no theory touched.
2. **Practice cut and flatten.** Delete the ten files, move the scorecard and the CFIR mapping, flatten the directories, update every inbound link. Constitution version bump.
3. **Theory merges.** Motions merge, parameter reference merge, reading guide trim, glossary trim, version history cut. Constitution version bump.
4. **Constitution rewrite.** The hard one. Each axiom rewritten to one page with its material pushed to the owning file. This step needs the author's eyes on every axiom before it merges, because it is the text the rest of the repo will be held to.

## 5. What this plan does not decide

- **Whether `models/tcg_models.py` at 64 KB is itself bloated.** It reproduces every worked example and the suite is fast. Trimming it is a separate exercise and no worked example is cut here.
- **Whether the seller surplus model belongs in a repo about how buyers transact.** It stays because it is defensible, not because it is central. Revisit after the Constitution rewrite shows what the core actually needs.
- **Whether to rename the repo.** The directory is still `tce-growth`, the framework is TCG, and the first commit called it ILG. Three names for one idea.
