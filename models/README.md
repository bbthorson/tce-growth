# Models

**Executable forms of the equations the playbook states in LaTeX, plus the figures generated from them.** No dependencies. Python 3, standard library only, matching the two checkers in [`tools/linting/`](../tools/linting/).

```bash
python3 models/test_tcg_models.py      # every worked example in the docs
python3 models/make_figures.py --check # figures still match the equations
```

## Why this exists

Roughly a dozen formulas lived only as prose. Nothing verified that a worked example still matched its formula, that weights still summed to 1, or that a figure still depicted the equation it illustrated. Retune a coefficient and the prose went on quietly asserting the old one.

That is the drift problem [`RetiredTerms.yml`](../tools/linting/styles/TCG/RetiredTerms.yml) solves for renames and the [citation provenance audit](../theory/evidence/citation-provenance-audit.md) solves for statistics. This directory is the equivalent for formulas.

## The documents are the specification

Where a document and the code disagree, **the document wins and the code is the bug.** Every function names its canonical home in its docstring, and every test names the file and section it checks, so a failure says which prose to read rather than which line to edit.

Fixing a formula therefore means editing the document first. The test then fails against the old code, which is the point.

## Why it sits at the root

The dependency chain runs `theory/` to `practice/` to `publishing/`, one way. This module implements formulas from both `theory/` and `practice/`, so it is downstream of both and cannot live inside either without misrepresenting that chain. It is a fourth group beside the three, not a member of one of them.

`.py` files need no frontmatter, and [`check_frontmatter.py`](../tools/linting/check_frontmatter.py) scopes itself to `theory/` and `practice/`, so this README is out of its scope. It is still inside the scope of `check_playbook.py` and Vale.

## What is here

| File | What it does |
|---|---|
| `tcg_models.py` | Every live formula, one function each, with its canonical home named in the docstring. |
| `test_tcg_models.py` | 118 assertions. Every worked example in the documents, plus the properties the documents claim (convexity, boundedness, monotonicity, the band edges). |
| `make_figures.py` | Writes the three axiom figures in `theory/canon/assets/` by sampling `tcg_models.py`. `--check` regenerates and fails on any diff. |

Formula coverage, by canonical home:

| Document | What the module implements |
|---|---|
| [models.md](../theory/reference/models.md) | Both cost representations and the derivation joining them, the section 1.5 normalization, both halves of the asymmetry gap, consensus friction in core and field form, and the decay rate. |
| [seller-surplus.md](../theory/arguments/seller-surplus.md) | Seller surplus, the quasi-rent, the marginal investment rule, the repeated form, and the cooperation threshold. |
| [consensus-friction-calculator.md](../practice/consensus-friction-calculator.md) | The worked example, the risk bands, and the variance rubric bounds. |
| [milestone-valuation-model.md](../practice/milestone-valuation-model.md) | The stage equation and the uncertainty decay chain. |
| [friction-efficiency-index.md](../practice/friction-efficiency-index.md) | FAR, BCV, RMS, SVI, both normalizations, and the composite. |
| [deal-triage-calculator.md](../practice/deal-triage-calculator.md) | The maturity gate, the three component counts and their bands, both divergence gates and the modifier, the level and direction routing, and the frequency reading. |
| [governance-forms.md](../theory/arguments/governance-forms.md) | The four governance forms selected by level and frequency, and whether the apparatus the level calls for can be amortized. |

## Nothing here is fitted, and it must stay that way

Every parameter default is a reasoned starting value. `models.md` states the forms are "specified, not fitted" and exist "to structure judgment, not to forecast," and the Friction Efficiency Index carries a stronger warning still.

- $a = 2.25$ is anchored by analogy to prospect theory's loss aversion coefficient. Section 1.6 is explicit that $a$ is not that coefficient, only borrowing its magnitude as a reason to believe $a$ is large.
- $\beta = 1.35$ is chosen inside a motivated range. Only $\beta > 1$ carries literature support.
- The Friction Efficiency Index weights have no empirical basis at all.
- The seller-surplus forms have no parameter anchored in published literature.

`TestCalibrationDiscipline` fails if the module docstring stops saying so, and `test_the_parameter_defaults_match_the_documents` fails if any default is retuned without editing the document it came from.

**Do not fit these to synthetic data.** A previous session evaluated a public "AWS SaaS Sales" dataset for this purpose: 9,994 rows from a fictitious company, with no cycle stages, no stakeholder counts, and no implementation outcomes. Fitting to it produces parameters that look empirical and are not, which would launder invented numbers past the provenance audit. Synthetic data is acceptable only as a test fixture that never produces a published number.

What would make the models empirical is already written down, in section 6 of `models.md` and section 6 of the Friction Efficiency Index. Those conditions are about logging real deals, not about finding a dataset.

## The figures

`theory/canon/assets/` holds three SVGs, one per axiom, replacing hand-made PNGs that depicted a potential-well curve no equation in the repository produced.

Each is sampled from `tcg_models.py`, so a coefficient change moves the picture or fails the check. The SVG is written by hand rather than by a plotting library so the check runs anywhere Python does, the output is byte-for-byte reproducible, and the `prefers-color-scheme` block is authored directly rather than injected by post-processing. The old PNGs glared in dark mode.

**Vale does not read SVG.** Its scope is `*.md`, so label text inside a figure escapes the banned-word list, the emoji ban, and the retired-terms rule. `check_figure_text()` in `make_figures.py` closes that hole by reading the same `RetiredTerms.yml` and `AntiHype.yml` files Vale uses. It covers the figures this repository generates and nothing else, so an SVG added by hand is still unchecked.

## Discrepancies found while building this

Recorded rather than silently reconciled, on the same principle the provenance audit uses for statistics.

**1. $I_{seller}$ has two incompatible definitions.** `models.md` section 2.2 gives a weighted power form over inputs on $[0, 10]$, which ranges to about 14.6. The [Asymmetry Scorecard](../practice/asymmetry-scorecard.md) defines the same symbol as the mean of four dimensions each scored 1 to 5, which lands on $[1, 5]$. Section 1.5's normalization assumes the scorecard's range, so the theory's own functional forms cannot feed the normalizer the theory makes mandatory. The module implements both under separate names and does not pretend they compose. Resolving this means deciding which one the symbol denotes. Scorecard v3.0 did not resolve it: the dimensions became pairs of counts, but the presentation scale stayed at $[1, 5]$ deliberately so the bands and the normalizer kept working, so the two definitions still disagree by the same amount.

**2. The consensus worked example is labelled against its own rubric.** [consensus-friction-calculator.md](../practice/consensus-friction-calculator.md) describes its worked example as "two camps in genuine conflict (Var = 0.25)". The rubric a few lines above assigns that description to 0.50 and gives 0.25 as "minor divergence in priority, nobody is threatened". The arithmetic is correct and reproduces to 17.6. Only the prose label is wrong, so the test asserts the arithmetic and this note records the rest.

**3. Two market-stage vocabularies were both canonical, and Constitution v17.0 retired both.** The replaced PNGs labelled their x-axis regions "Nascent, Efficient, Saturated" and the calculator's step 1 named the stages "Nascent, Transitional, Mature". Neither file was wrong and the pair could not be reconciled, because the taxonomy was a proxy for a quantity nothing measured. Direction is now measured, so the proxy is gone and its three legibility signals survive as search evidence items. One file still carries a stage name in prose: [channel-collapse.md](../theory/evidence/channel-collapse.md) refers to Stage 3 buyers, which is a claim about the research rather than a routing rule, and it is left alone under the rule that research files are not rewritten to match a framework revision.

**4. The retired panels plotted no equation the repository contains.** The U-shaped transaction cost curve over workflow legibility is not the reduced form, and no other documented form produces it. That is why the replacements plot one stated equation each rather than redrawing the same shape in code.

## Open questions this work did not resolve

Both are theory gaps rather than module defects, so they are stated in [open-questions.md](../theory/reference/open-questions.md) as items 28 and 30. What belongs here is what the module does about them, which is to decline to guess.

**$p_{close}$ is not observable.** The module expresses the marginal rule and deliberately does not evaluate it. `required_marginal_close_gain()` inverts it into the question section 6 of the seller model actually endorses: what would the derivative have to be for this spend to make sense.

**$R_{redeploy}$ has no scoring method.** `quasi_rent()` takes it as a caller-supplied input rather than deriving it, because a rubric invented here would put a number into a risk review that no document backs.

## Related

- [CLAUDE.md](../CLAUDE.md) for the repository conventions this directory follows.
- [tools/linting/](../tools/linting/) for the two checkers this one sits alongside in `.githooks/pre-commit`.
- [theory/reference/notation.md](../theory/reference/notation.md) for the canonical meaning of every symbol implemented here.
