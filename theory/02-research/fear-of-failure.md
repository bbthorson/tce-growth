---
title: "Fear of Failure: Why a Buyer Waits"
layer: theory
status: active
operationalizes: [axiom-2, axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# Fear of Failure: Why a Buyer Waits

**Sources:**

*What buyers believe about failure*
- The Standish Group. *CHAOS Report* (1994–2024). Original sample: 3,682 projects. [PDF (1994 baseline)](https://www.utdallas.edu/~chung/SYSM6309/chaos_report.pdf)
- McKinsey & Company and University of Oxford (2012). "Delivering large-scale IT projects on time, on budget, and on value." Sample: 5,400+ IT projects. [Link](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/delivering-large-scale-it-projects-on-time-on-budget-and-on-value)
- Gartner Research. Surveys of technology buyers on purchase regret (2022, 2023).
- Boehm, B. & Basili, V.R. (2001). "Software Defect Reduction Top 10 List." *IEEE Computer*, 34(1), 135–137. [PDF](https://www.cs.umd.edu/projects/SoftEng/ESEG/papers/82.78.pdf)
- Dixon, M. & McKenna, T. (2022). *The JOLT Effect: How High Performers Overcome Customer Indecision.* Portfolio. A practitioner book built on recorded sales calls. [Site](https://www.jolteffect.com/)
- Staw, B.M. (1976). "Knee-Deep in the Big Muddy: A Study of Escalating Commitment to a Chosen Course of Action." *Organizational Behavior and Human Performance*, 16(1), 27–44. (not yet read here)

*Why a loss weighs more than a gain*
- Kahneman, D. & Tversky, A. (1979). "Prospect Theory: An Analysis of Decision under Risk." *Econometrica*, 47(2), 263–292.
- Tversky, A. & Kahneman, D. (1992). "Advances in Prospect Theory: Cumulative Representation of Uncertainty." *Journal of Risk and Uncertainty*, 5(4), 297–323.
- Samuelson, W. & Zeckhauser, R. (1988). "Status Quo Bias in Decision Making." *Journal of Risk and Uncertainty*, 1(1), 7–59.
- CEB Marketing Leadership Council with Google and Motista (2013). "From Promotion to Emotion: Connecting B2B Customers to Brands."

*Why waiting is worth something*
- Dixit, A.K. & Pindyck, R.S. (1994). *Investment under Uncertainty*. Princeton University Press.
- McDonald, R. & Siegel, D. (1986). "The Value of Waiting to Invest." *Quarterly Journal of Economics*, 101(4), 707–728.
- Trigeorgis, L. (1996). *Real Options: Managerial Flexibility and Strategy in Resource Allocation*. MIT Press.

**Abstract.** Claim 7 of the [Constitution](../01-foundation/00-tcg-constitution.md) says implementation is a fear at Time1. The work comes later, and at signature the buyer holds only an expectation of it. This file holds three accounts of why a buyer that wants a change still waits. The first is evidence: buyers believe most projects disappoint, and many regret what they bought. The second is prospect theory, which says a possible loss weighs more than a matching gain. The third is real options, which says that when a decision cannot be undone, waiting has a value of its own. Together they explain why a discount does little for a fearful buyer and why a commitment and a staged plan do more.

> [!WARNING]
> **The CHAOS figures measure estimation accuracy, not delivery failure.** Eveleens and Verhoef (2010, *IEEE Software* 27(1)) and Jørgensen and Moløkken-Østvold (2006) show that Standish counts a project as challenged whenever it misses its initial estimate, ignores underruns, samples by self-selection, and has declined to release its data. Cite them as evidence of what buyers believe about projects, which is what claim 7 needs, and not as failure rates. The [citation audit](./audits/citation-provenance-audit.md) carries the validity note.

## 1. What buyers believe about failure

- Standish counted 16.2% of projects as successful in 1994 and 31% in 2020. It counted about half as challenged in both years, with a 189% average cost overrun on challenged projects in 1994.
- The average large IT project runs 45% over budget and delivers 56% less value than predicted, and 17% go badly enough to threaten the company (McKinsey and Oxford).
- 56% of organizations report significant regret over their largest recent technology purchase, and 60% of buyers involved in a renewal decision regret nearly every purchase (Gartner).
- 40 to 60% of qualified pipeline ends in no decision. Dixon and McKenna attribute 56% of those losses to indecision, the buyer's fear of making a mistake, and the rest to a preference for the status quo. In their recordings, pressing an indecisive buyer with urgency backfired 84% of the time.
- Fixing a defect after delivery costs up to 100 times more than fixing it during requirements and design on large systems, and closer to 5 times on small ones (Boehm and Basili).

A no-decision rate is an outcome, so it cannot say which cause produced it. A stall can come from fear, from a buyer that does not want the change enough, or from an organization that cannot agree. The Constitution's Part II asks about value first for that reason.

## 2. Why a loss weighs more than a gain

Kahneman and Tversky showed that people judge an outcome against a reference point, usually the status quo, and not as an absolute level. Measured from that point, a loss weighs more than a gain of the same size. Tversky and Kahneman (1992) estimated the ratio at about 2.25 in laboratory gambles. Samuelson and Zeckhauser showed that the same asymmetry makes the current arrangement the default, since leaving it puts a certain loss against an uncertain gain.

The CEB study adds the personal side. It found that what a purchase does for the individual's career and standing carried about twice the weight of the business case in purchase outcomes. That is the third standing assumption seen from the buyer's side: a decision role acts on its own payoff.

The framework borrows the direction and no number. List's field experiments found that market experience weakens loss aversion among practiced traders, so an experienced procurement group may sit nearer neutrality than an individual does. [tce-empirical-record.md](./tce-empirical-record.md) carries that critique.

## 3. Why waiting is worth something

Dixit and Pindyck showed that when an investment cannot be undone and its outcome is uncertain, the ability to wait has economic value. Committing gives up the chance to learn first, and a standard return calculation leaves that cost out. A buyer can therefore decline a purchase with a positive expected return and be right to. More uncertainty raises the value of waiting, so it delays a commitment and does more than discount it.

The corollary matters more than the theorem. An investment split into stages, each taken after some uncertainty has resolved, is worth more than the same investment committed at once, because each stage keeps the option to stop. A right to stop at a known price limits the worst case, and that raises the value of the whole sequence with no change in the expected return. A contract that forces full commitment before anyone has learned anything destroys that value.

## Supports in TCG

- **Claim 7.** The evidence in section 1 is what the buyer's expectation of implementation looks like before any seller arrives. Section 2 says why it acts through people: each decision role weighs what the change could cost it personally, and weighs that more than the gain to the organization.
- **Claim 8.** A discount adds to the gain. A commitment the seller would not make if it expected to fail removes part of the loss, and section 2 says the loss is the heavier side. Urgency tactics fail for the same reason: they press on the gain while the buyer is looking at the loss.
- **Claims 6 and 12.** Section 3 is the theory under the staged plan. Stages with a stop point at a known price are options to stop. Dixon and McKenna's remedy for indecision, limited and reversible commitments, is the same idea from practice, and the Constitution credits them at Axiom II. On a plug-in purchase the trial already gives the buyer that option, which is why claim 6 says a staged plan adds nothing there.
- **Claim 9.** Boehm and Basili's cost multiplier is the software form of work skipped at Time1 growing at Time2.
- **Open question 59.** Staw's escalation of commitment is why a sponsor with a stake is a party to the dispute it is asked to judge.

**Quotes and statistics.** Citable passages from these sources are collected in [source-quotes.md](../../publishing/02-tools/source-quotes.md). The numbers are recorded, with provenance, in the [citation audit](./audits/citation-provenance-audit.md).
