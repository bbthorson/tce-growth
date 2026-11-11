---
title: "Citation Provenance Audit"
layer: theory
status: active
---

# Citation Provenance Audit

**Purpose:** trace every headline statistic the TCG framework cites to its primary source, and record how far each trace goes. The research files quote these numbers, and this file is where their provenance lives. Check a statistic's status here before quoting it outside this repository.

**Status vocabulary:**

- **Primary linked.** The repo links the original study, report or announcement. A stable rehosted copy of the original text counts, and is noted.
- **Primary cited.** The original study is fully cited but not linked. Retrievable through any library.
- **Primary named.** The original study is identified, but every working link is secondary (press coverage, an aggregator, a vendor blog). Verify against the original before external use.
- **Abstract only.** A peer-reviewed source read at its abstract. Cite the direction and not the size until someone reads the paper.
- **Unverified.** No primary source is confirmed. Do not cite externally.

**Last reviewed:** 2026-11-10, for the trim. The file now holds only figures that a file in `theory/` cites today. Rows for figures cited nowhere, the retired coefficient, the untraced lists and the vendor figures from the 2026-11 adversarial review left with the files that carried them. They are in git history, so a later citation can recover the trace: `git show b449f40:theory/02-research/audits/citation-provenance-audit.md`.

---

## Project delivery outcomes (Standish Group CHAOS)

| Statistic | Cited in | Primary source | Status |
|---|---|---|---|
| 16.2% success, 52.7% challenged (n = 3,682) | [fear-of-failure.md](../fear-of-failure.md) | Standish Group, *CHAOS Report* (1994) | **Primary linked.** Rehosted copy: [utdallas.edu PDF](https://www.utdallas.edu/~chung/SYSM6309/chaos_report.pdf). |
| 189% average cost overrun on challenged projects | [fear-of-failure.md](../fear-of-failure.md) | Standish Group, *CHAOS Report* (1994) | **Primary linked** (same PDF). A 1994 Standish figure, once misattributed to McKinsey and corrected on 2026-08-28. |
| 31% success and 50% challenged in 2020 | [fear-of-failure.md](../fear-of-failure.md) | Standish Group, CHAOS research (2020) | **Primary named.** Repo links only summaries ([OpenCommons](https://opencommons.org/CHAOS_Report_on_IT_Project_Outcomes)). The recent reports are paywalled. |

**Validity note (2026-09).** Every CHAOS row keeps its provenance status and carries a validity caveat. Eveleens and Verhoef (2010, *IEEE Software* 27(1), 30–36) and Jørgensen and Moløkken-Østvold (2006) show that Standish's success definition measures conformance to the initial estimate, ignores underruns and rests on self-selected surveys, and that the data has not been released for replication. Cite these figures as what buyers believe about project risk. Do not cite them as failure rates.

## Large-scale IT projects (McKinsey and University of Oxford)

| Statistic | Cited in | Primary source | Status |
|---|---|---|---|
| 45% average budget overrun and 56% less value than predicted (projects over $15M, n > 5,400) | [fear-of-failure.md](../fear-of-failure.md) | McKinsey & Company with the BT Centre for Major Programme Management, University of Oxford, "Delivering large-scale IT projects on time, on budget, and on value" (2012) | **Primary linked** ([article](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/delivering-large-scale-it-projects-on-time-on-budget-and-on-value), [PDF](https://www.mckinsey.com/~/media/McKinsey/dotcom/client_service/BTO/PDF/MOBT_27_Delivering_large-scale_IT_projects_on_time_budget_and_value.ashx)). The same study reports a 7% schedule overrun, which the repo once gave as 45%. |
| 17% of large projects threaten the existence of the company (overruns of 200 to 400%) | [fear-of-failure.md](../fear-of-failure.md) | same study | **Primary linked.** |

## Software quality cost

| Statistic | Cited in | Primary source | Status |
|---|---|---|---|
| 100× cost multiplier for fixes after delivery against the requirements and design phase on large systems, and closer to 5× on small ones | [fear-of-failure.md](../fear-of-failure.md) | Boehm & Basili (2001), "Software Defect Reduction Top 10 List," *IEEE Computer*, 34(1), 135–137 | **Primary linked** ([PDF, UMD rehost](https://www.cs.umd.edu/projects/SoftEng/ESEG/papers/82.78.pdf)). Once attributed to an IBM Systems Sciences Institute study that has never surfaced publicly. Re-attributed on 2026-08-28. |

## Loss aversion and personal value

| Statistic | Cited in | Primary source | Status |
|---|---|---|---|
| A loss weighs about 2.25 times a matching gain | [fear-of-failure.md](../fear-of-failure.md) | Tversky & Kahneman (1992), "Advances in Prospect Theory," *Journal of Risk and Uncertainty*, 5(4) | **Primary cited.** Supported by a 2024 meta-analysis across 30+ studies ([*Journal of Economic Psychology*, indexed at RePEc](https://ideas.repec.org/a/eee/joepsy/v103y2024ics0167487024000485.html)). The framework borrows the direction and no coefficient. |
| Personal value carries about twice the weight of business value in purchase outcomes | [fear-of-failure.md](../fear-of-failure.md) | CEB Marketing Leadership Council with Google and Motista, "From Promotion to Emotion" (2013) | **Primary linked** ([whitepaper PDF](https://www.thinkwithgoogle.com/_qs/documents/3988/promotion-emotion-b2b_articles_q5pm53H.pdf)). Vendor research. |

## Buyer indecision and regret (JOLT, Gartner)

| Statistic | Cited in | Primary source | Status |
|---|---|---|---|
| 40 to 60% of qualified pipeline lost to no decision | [fear-of-failure.md](../fear-of-failure.md) | Dixon & McKenna, *The JOLT Effect* (2022), from 2.5M recorded sales conversations | **Primary cited** ([book site](https://www.jolteffect.com/)). Repo also links a [Gong interview](https://podcast.gong.io/public/76/Reveal%3A-The-Revenue-Intelligence-Podcast-05b3e1e1/af9f3a56) as a secondary summary. |
| 56% of no-decision losses driven by indecision and not by a preference for the status quo | [fear-of-failure.md](../fear-of-failure.md) | same book | **Primary cited.** The repo once carried both 56% and 60%. Standardized to 56% on 2026-08-28. |
| Urgency tactics backfire in 84% of cases with indecisive buyers | [fear-of-failure.md](../fear-of-failure.md) | same book | **Primary cited.** |
| 56% of organizations report significant regret over their largest recent technology purchase | [fear-of-failure.md](../fear-of-failure.md) | Gartner survey of 1,120 organizations, fielded November to December 2021 | **Primary linked** ([press release, 2022-07-12](https://www.gartner.com/en/newsroom/press-releases/2022-07-12-gartner-finds-that-majority-of-technology-purchases-come-with-high-degree-of-regret)). |
| 60% of technology buyers involved in renewal decisions regret nearly every purchase | [fear-of-failure.md](../fear-of-failure.md) | Gartner survey of 1,503 respondents at organizations with $50M+ revenue, fielded February to March 2023 | **Primary linked** ([press release, 2023-06-14](https://www.gartner.com/en/newsroom/press-releases/2023-06-14-gartner-survey-reveals-60-percent-of-technology-buyers-involved-in-renewal-decisions-regret-nearly-every-purchase-they-make)). |

## Discounts, pay and retention

| Statistic | Cited in | Primary source | Status |
|---|---|---|---|
| Customers acquired on a deeper discount bought again less, at a newspaper and an online grocer | [Constitution, claim 8](../../01-foundation/00-tcg-constitution.md), [02-mathematical-models.md](../../01-foundation/02-mathematical-models.md) section 1.3, [value-and-persuasion.md](../value-and-persuasion.md) | Lewis (2006), *Journal of Marketing Research* | **Abstract only.** Cited for the direction. Check at the primary whether the effect is selection or the step up to full price at renewal before citing it further. |

## Product adoption

| Statistic | Cited in | Primary source | Status |
|---|---|---|---|
| 80% of features rarely or never used | [implementation-science.md](../implementation-science.md) | Pendo, *The 2019 Feature Adoption Report* (615 subscriptions, three months of usage data) | **Primary linked** ([report PDF](https://go.pendo.io/rs/185-LQW-370/images/2019%20Feature%20Adoption%20Report%20Digital.pdf)), verified against the report text. Vendor research. |

## Channel volume and response

| Statistic | Cited in | Primary source | Status |
|---|---|---|---|
| Email volume of 293B a day in 2019 growing to 376B a day in 2025 | [channel-collapse.md](../channel-collapse.md) | Radicati Group, *Email Statistics Reports* | **Primary linked** ([2019-2023 executive summary](https://www.radicati.com/wp/wp-content/uploads/2018/12/Email-Statistics-Report-2019-2023-Executive-Summary.pdf), [2021-2025 executive summary](https://www.radicati.com/wp/wp-content/uploads/2021/Email_Statistics_Report,_2021-2025_Executive_Summary.pdf)). |
| Reply rates of 8.5% in 2019 against low single digits in 2026 | [channel-collapse.md](../channel-collapse.md) | Backlinko and Pitchbox 2019 study of 12M outreach emails, and Instantly cold-email platform benchmarks | **Primary named** ([Instantly benchmarks](https://instantly.ai/blog/cold-email-reply-rate-benchmarks/)). The 2019 figure measures link-building and PR outreach and the later one measures cold sales email, so the decline is a direction and not a measured drop. |

---

## Cited without a number

- Larkin (2014) is cited in [value-and-persuasion.md](../value-and-persuasion.md) for the direction of its finding. The paper was read at the abstract, so its size is not quoted.
- CFIR's count of 19 earlier theories, in [implementation-science.md](../implementation-science.md), is from Damschroder et al. (2009) and has not been checked against the paper.
- The results in [sat-threshold-test.md](../sat-threshold-test.md) are the repository's own measurements. The script and counts in `models/` reproduce them.
- Schiebler, Lee and Brodbeck (2026), a meta-analysis of expectation and disconfirmation in *Journal of the Academy of Marketing Science*, is cited qualitatively in [value-and-persuasion.md](../value-and-persuasion.md) and marked unconfirmed there. Not located at the primary.
- The sources listed in section 4 of [06-calibration.md](../../01-foundation/06-calibration.md) reached the repository through outside reviews. No file quotes a figure from them. Open the paper before any file does.

## Maintaining this file

- A new headline statistic anywhere in `theory/` gets a row here in the same commit, with an honest status.
- A status moves up only when someone opens the primary source and checks the number against it.
- When two files disagree, record the disagreement here first, then fix the files against the primary.
- When a figure leaves every file, its row leaves too, and git history keeps the trace.
