---
title: "Citation Provenance Audit"
layer: theory
status: active
---

# Citation Provenance Audit

**Purpose:** trace every headline statistic the TCG framework cites to its primary source, and record how far each trace currently goes. The research entries quote these numbers. This file is where their provenance lives. Check a statistic's status here before quoting it outside this repository.

**Status vocabulary:**

- **Primary linked.** The repo links the original study, report, or announcement. A stable rehosted copy of the original text counts, and is noted.
- **Primary cited.** The original study is fully cited but not linked. Retrievable through any library.
- **Primary named.** The original study is identified, but every working link is secondary (press coverage, an aggregator, a vendor blog). Verify against the original before external use.
- **Unverified.** No primary source is confirmed. Do not cite externally.

**Last reviewed:** 2026-09-10.

---

## Project delivery outcomes (Standish Group CHAOS)

| Statistic | Cited in | Primary source | Status |
|---|---|---|---|
| 16.2% success, 52.7% challenged, 31.1% canceled (n = 3,682) | [fear-of-failure.md](../fear-of-failure.md) | Standish Group, *CHAOS Report* (1994) | **Primary linked.** Rehosted copy: [utdallas.edu PDF](https://www.utdallas.edu/~chung/SYSM6309/chaos_report.pdf). |
| 189% average cost overrun on challenged projects | [fear-of-failure.md](../fear-of-failure.md) | Standish Group, *CHAOS Report* (1994) | **Primary linked** (same PDF). A 1994 Standish figure, previously misattributed to McKinsey. See discrepancy 3. |
| 42% of proposed features delivered (large organizations) | this audit | Standish Group, *CHAOS Report* (1994) | **Primary linked** (same PDF). |
| Later-year rates: 37/42/21 (2012), 31/50/19 (2020) | [fear-of-failure.md](../fear-of-failure.md), this audit | Standish Group, CHAOS research (2012, 2020) | **Primary named.** Repo links only summaries ([OpenCommons](https://opencommons.org/CHAOS_Report_on_IT_Project_Outcomes)). The recent reports are paywalled. |
| Success by company size: 9% large, 16.2% medium, 28% small | this audit | Standish Group, *CHAOS Report* (1994) | **Primary linked.** Rehosted copy: [ResearchGate](https://www.researchgate.net/publication/263849222_The_Chaos_Report). |

## Large-scale IT projects (McKinsey and University of Oxford)

| Statistic | Cited in | Primary source | Status |
|---|---|---|---|
| 45% average budget overrun, 7% schedule overrun, 56% less value than predicted (projects over $15M, n > 5,400) | [fear-of-failure.md](../fear-of-failure.md), this audit, and the read-aloud passages in the [Contextual Blueprint](../../../practice/implementation-motion/01-discovery-contextual-blueprint.md) and [Red Team Protocol](../../../practice/implementation-motion/02-validation-red-team-protocol.md) | McKinsey & Company with the BT Centre for Major Programme Management, University of Oxford, "Delivering large-scale IT projects on time, on budget, and on value" (2012) | **Primary linked** ([article](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/delivering-large-scale-it-projects-on-time-on-budget-and-on-value), [PDF](https://www.mckinsey.com/~/media/McKinsey/dotcom/client_service/BTO/PDF/MOBT_27_Delivering_large-scale_IT_projects_on_time_budget_and_value.ashx)). |
| 17% of large projects threaten the existence of the company (overruns of 200 to 400%) | [fear-of-failure.md](../fear-of-failure.md) | same study | **Primary linked.** |
| $66B total cost overrun in the sample. Expected overrun grows 15 percentage points per additional year of schedule | this audit | same study | **Primary linked.** |

## Software quality cost (CISQ)

| Statistic | Cited in | Primary source | Status |
|---|---|---|---|
| $2.41T total cost of poor software quality in the US (2022) | [fear-of-failure.md](../fear-of-failure.md) | CISQ, *The Cost of Poor Software Quality in the US: A 2022 Report* | **Primary linked** ([report page](https://www.it-cisq.org/the-cost-of-poor-quality-software-in-the-us-a-2022-report/), [PDF](https://www.it-cisq.org/wp-content/uploads/sites/6/2022/11/CPSQ-Report-Nov-22-2.pdf)). |
| $1.52T accumulated technical debt (2022) | this audit | same report | **Primary linked.** |
| 650% increase in open-source supply-chain failures (2020 to 2021) | this audit | same report | **Primary linked.** |
| Roughly 33% of developer time spent on technical debt (13.5 hours of a 41-hour week) | [fear-of-failure.md](../fear-of-failure.md), [re-aim-framework.md](../re-aim-framework.md), this audit | same report | **Primary linked.** Repo figures reconciled to this number on 2026-08-28. See discrepancy 4. |
| 100× cost multiplier for post-delivery fixes vs. the requirements and design phase (large systems; closer to 5:1 for small systems) | [fear-of-failure.md](../fear-of-failure.md) | Boehm & Basili (2001), "Software Defect Reduction Top 10 List," *IEEE Computer*, 34(1), 135–137 | **Primary linked** ([PDF, UMD rehost](https://www.cs.umd.edu/projects/SoftEng/ESEG/papers/82.78.pdf)). Previously attributed to an IBM Systems Sciences Institute study that has never surfaced publicly. Re-attributed on 2026-08-28. |

## Behavioral economics (loss aversion and personal value)

| Statistic | Cited in | Primary source | Status |
|---|---|---|---|
| λ ≈ 2.25, α, β ≈ 0.88 | [prospect-theory.md](../prospect-theory.md), [fear-of-failure.md](../fear-of-failure.md), Constitution | Tversky & Kahneman (1992), "Advances in Prospect Theory," *Journal of Risk and Uncertainty*, 5(4) | **Primary cited.** Supported by a 2024 meta-analysis across 30+ studies ([*Journal of Economic Psychology*, indexed at RePEc](https://ideas.repec.org/a/eee/joepsy/v103y2024ics0167487024000485.html)). |
| $a = 2.25$ annual contract values per unit of squared normalized gap | [02-mathematical-models.md §1.7](../../01-foundation/02-mathematical-models.md), Constitution Axiom III | None. The magnitude is borrowed from λ above by analogy and the units are stated by the Constitution, not measured | **Unverified.** Do not cite externally as an estimate. This row exists because $a$ has stated units, which turns an unfalsifiable number into a checkable one: the reading is that entering uncertainty is worth roughly five times the first milestone payment and three percent of the last. Both figures are arithmetic from $a$ and the milestone table, not observations. λ itself is measured and dimensionless, and lending its magnitude to $a$ does not lend it its provenance. |
| Personal Value carries 2× the impact of Business Value on purchase outcomes | [prospect-theory.md](../prospect-theory.md) | CEB Marketing Leadership Council with Google and Motista, "From Promotion to Emotion" (2013) | **Primary linked** ([whitepaper PDF](https://www.thinkwithgoogle.com/_qs/documents/3988/promotion-emotion-b2b_articles_q5pm53H.pdf)). |
| 14% of buyers perceive enough differentiation to pay a premium. 86% perceive little or no difference between suppliers | [prospect-theory.md](../prospect-theory.md) | same whitepaper | **Primary linked.** |
| 71% purchase likelihood and 8× premium likelihood when high Personal Value is present | [prospect-theory.md](../prospect-theory.md) | same whitepaper | **Primary linked.** |

## Buyer indecision and regret (JOLT, Gartner)

| Statistic | Cited in | Primary source | Status |
|---|---|---|---|
| 40 to 60% of qualified pipeline lost to No Decision | [fear-of-failure.md](../fear-of-failure.md), [costly-signals.md](../costly-signals.md), [buying-center-dynamics.md](../buying-center-dynamics.md), [channel-collapse.md](../channel-collapse.md) | Dixon & McKenna, *The JOLT Effect* (2022), from 2.5M recorded sales conversations | **Primary cited** ([book site](https://www.jolteffect.com/)). Repo also links a [Gong interview](https://podcast.gong.io/public/76/Reveal%3A-The-Revenue-Intelligence-Podcast-05b3e1e1/af9f3a56) as a secondary summary. |
| 56% of No Decision losses driven by indecision (Fear of Messing Up) rather than status quo preference | [fear-of-failure.md](../fear-of-failure.md), [costly-signals.md](../costly-signals.md) | same book | **Primary cited.** The repo previously carried both 56% and 60%. Standardized to 56% on 2026-08-28. See discrepancy 1. |
| FOMO tactics backfire in 84% of cases with indecisive buyers | [fear-of-failure.md](../fear-of-failure.md) | same book | **Primary cited.** |
| 56% of organizations report significant regret over their largest recent tech purchase | [fear-of-failure.md](../fear-of-failure.md) | Gartner survey of 1,120 organizations, fielded November to December 2021 | **Primary linked** ([press release, 2022-07-12](https://www.gartner.com/en/newsroom/press-releases/2022-07-12-gartner-finds-that-majority-of-technology-purchases-come-with-high-degree-of-regret)). |
| Regret causes: 52% unmet functional requirements, 44% longer implementations, 41% insufficient implementation resources | this audit | same Gartner survey | **Primary named.** The press release above is the primary. These sub-figures were sourced from secondary coverage ([RouteSmart](https://www.routesmart.com/preventing-buyers-remorse-survey-report/)) and still need line-checking against it. |
| 61 to 75% of buyers prefer a rep-free experience | this audit | Gartner sales surveys. The 75% figure is Gartner's 2019 finding for low-complexity purchases | **Primary linked.** 61%: [press release, 2025-06-25](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-sales-survey-finds-61-percent-of-b2b-buyers-prefer-a-rep-free-buying-experience). The newest figure is 67% ([press release, 2026-03-09](https://www.gartner.com/en/newsroom/press-releases/2026-03-09-gartner-sales-survey-finds-67-percent-of-b2b-buyers-prefer-a-rep-free-experience)). The unrelated Experian link is retired. |
| Median buying group of six to 10 decision makers | [buying-center-dynamics.md](../buying-center-dynamics.md) | Gartner, The B2B Buying Journey research | **Primary linked** ([Gartner research page](https://www.gartner.com/en/sales/insights/b2b-buying-journey)). The page blocks automated access. The figure is confirmed by multiple outlets quoting it verbatim. |
| Personalization effects: 3.2× regret risk (passive), 2.3× decision confidence (active), 1.8× premium likelihood | this audit | Gartner survey of 1,464 B2B and B2C buyers (2025) | **Primary linked** ([press release](https://www.gartner.com/en/newsroom/press-releases/2025-06-03-gartner-survey-reveals-personalization-can-triple-the-likelihood-of-customer-regret-at-key-journey-points)). |
| 61% of potential B2B deals fall through with No Decision | [prospect-theory.md](../prospect-theory.md) | Genius Drive, B2B sales research article | **Primary linked** ([Genius Drive article](https://geniusdrive.com/b2b-sales-research-the-proven-impact-of-value-selling/)). The article does not document its research base. Prefer the JOLT 40 to 60% figure for external use. |
| 60% of technology buyers involved in renewal decisions regret nearly every purchase | [fear-of-failure.md](../fear-of-failure.md), [game-theory-and-nrr.md](../game-theory-and-nrr.md) | Gartner survey of 1,503 respondents at organizations with $50M+ revenue, fielded February to March 2023 | **Primary linked** ([press release, 2023-06-14](https://www.gartner.com/en/newsroom/press-releases/2023-06-14-gartner-survey-reveals-60-percent-of-technology-buyers-involved-in-renewal-decisions-regret-nearly-every-purchase-they-make)). game-theory-and-nrr.md previously paraphrased this as regret "within the first year". Corrected on 2026-08-28. |

## AI implementation gap

| Statistic | Cited in | Primary source | Status |
|---|---|---|---|
| Roughly 80% of AI projects fail, twice the rate of traditional IT projects | this audit | RAND Corporation, "The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed" (RRA2680-1, August 2024), 65 practitioner interviews | **Primary linked** ([report page](https://www.rand.org/pubs/research_reports/RRA2680-1.html), [PDF](https://www.rand.org/content/dam/rand/pubs/research_reports/RRA2600/RRA2680-1/RAND_RRA2680-1.pdf)). |
| 30% of GenAI projects abandoned after proof of concept by end of 2025 | [fear-of-failure.md](../fear-of-failure.md), this audit | Gartner press release (July 2024) | **Primary linked** ([press release, 2024-07-29](https://www.gartner.com/en/newsroom/press-releases/2024-07-29-gartner-predicts-30-percent-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025)). |
| 10/20/70 effort split (algorithms / infrastructure / people and process) | this audit | unclear | **Unverified.** Circulates in consulting commentary. The repo's chain (a Medium post attributing it to RAND and McKinsey) does not establish it. |

## Retention, alignment, and valuation

| Statistic | Cited in | Primary source | Status |
|---|---|---|---|
| Involuntary churn ~0.8% and voluntary churn ~2.6%, average B2B SaaS | [game-theory-and-nrr.md](../game-theory-and-nrr.md) | Recurly churn rate benchmarks | **Primary linked** ([Recurly research](https://recurly.com/research/churn-rate-benchmarks/)). |
| 36% higher retention and 38% higher win rates from tight functional alignment | [game-theory-and-nrr.md](../game-theory-and-nrr.md) | Aberdeen Group (with MathMarketing), sales-marketing alignment research | **Primary named.** The original report is no longer distributed and circulates through quotation. Previously misattributed to Sales-CS alignment. Corrected on 2026-08-28. |
| 15% churn reduction from clawback implementation | previously [game-theory-and-nrr.md](../game-theory-and-nrr.md) | none found | **Unverified.** Circulates in compensation-vendor blogs attributed to an unnamed "Harvard Business Review study." Removed from the research entry on 2026-08-28. |
| NRR above 120% roughly doubles the revenue multiple relative to 100 to 110% NRR | [game-theory-and-nrr.md](../game-theory-and-nrr.md), [re-aim-framework.md](../re-aim-framework.md) | FE International, NRR valuation analysis | **Primary named** ([FE International guide](https://www.feinternational.com/blog/net-revenue-retention-saas-valuation)). Replaces the untraceable "5.7× vs. 3.1× (46% discount)" pair on 2026-08-28. |

## Product adoption and SaaS utilization

| Statistic | Cited in | Primary source | Status |
|---|---|---|---|
| 80% of features rarely or never used, ~$29.5B invested in them, and 12% of features generating 80% of daily usage volume | [re-aim-framework.md](../re-aim-framework.md) | Pendo, *The 2019 Feature Adoption Report* (615 subscriptions, three months of usage data) | **Primary linked** ([report PDF](https://go.pendo.io/rs/185-LQW-370/images/2019%20Feature%20Adoption%20Report%20Digital.pdf)), verified against the report text. The repo previously said 6.4% of features drive 80% of clicks. The report says 12%. Corrected on 2026-08-28. |
| 57% of weekly active users never touch features driving 70% of expansion revenue | previously [re-aim-framework.md](../re-aim-framework.md) | none found | **Unverified.** No source located. Removed from the research entry on 2026-08-28. |
| $18M average annual license waste and 49% license utilization | [re-aim-framework.md](../re-aim-framework.md), [fear-of-failure.md](../fear-of-failure.md) | Zylo, *2024 SaaS Management Index* | **Primary linked** ([announcement](https://zylo.com/news/2024-saas-management-index/)). The repo previously cited the 2025 index for these 2024 figures. |
| Roughly 300 SaaS applications per enterprise (average 305, median 240) | [fear-of-failure.md](../fear-of-failure.md) | Zylo, *2026 SaaS Management Index* | **Primary linked** ([announcement](https://zylo.com/news/2026-saas-management-index)). Replaces the unsourced "106 to 275" range on 2026-08-28. |
| Average SaaS DAU/MAU ratio of 13% | [re-aim-framework.md](../re-aim-framework.md) | Mixpanel, product benchmarks report | **Primary named.** The former claim that 40% is the healthy B2B threshold is not supported. Published guidance puts healthy B2B at 10 to 20%, with 40%+ marking habitual-use products. Corrected on 2026-08-28. |

## Channel volume and response

| Statistic | Cited in | Primary source | Status |
|---|---|---|---|
| Email volume of 293B/day (2019) growing to 376B/day (2025) | [channel-collapse.md](../channel-collapse.md) | Radicati Group, *Email Statistics Reports* | **Primary linked** ([2019-2023 executive summary](https://www.radicati.com/wp/wp-content/uploads/2018/12/Email-Statistics-Report-2019-2023-Executive-Summary.pdf), [2021-2025 executive summary](https://www.radicati.com/wp/wp-content/uploads/2021/Email_Statistics_Report,_2021-2025_Executive_Summary.pdf)). |
| Reply rates of 8.5% (2019) vs. 3.4% (2026) | [channel-collapse.md](../channel-collapse.md) | Backlinko/Pitchbox 2019 study of 12M outreach emails; Instantly cold-email platform benchmarks | **Primary named** ([Instantly benchmarks](https://instantly.ai/blog/cold-email-reply-rate-benchmarks/)). The 2019 figure measures link-building and PR outreach and the 2026 figure measures cold sales email, so the decline is directional rather than a measured drop. Annotated in the research entry on 2026-08-28. |

## Case figures

| Statistic | Cited in | Primary source | Status |
|---|---|---|---|
| Hershey (1999): roughly $100M in unfulfilled orders, quarterly profit down 19%, stock down 8% | [transaction-cost-economics.md](../transaction-cost-economics.md) | Contemporaneous business press, chronicled in CIO's "Hershey's Bittersweet Lesson" | **Primary named** ([CIO article](https://www.cio.com/article/2440386/supply-chain---hershey-s-bittersweet-lesson.html)). The repo previously called the 19% figure a stock drop. It was the profit drop, and the stock fell 8%. Corrected on 2026-08-28. |
| Nike i2 (2000): roughly $100M in lost sales and a ~20% stock decline | [transaction-cost-economics.md](../transaction-cost-economics.md) | Nike's February 2001 earnings warning, chronicled in CIO's "Nike Rebounds" (Koch, 2004) | **Primary named.** Figures match contemporaneous coverage. |

---

## Discrepancies found

The point of a provenance audit is to catch drift between files. Most severe first. A resolved item keeps its entry as the record of the correction:

1. **FOMU share of No Decision: resolved.** [costly-signals.md](../costly-signals.md) said 60% and [fear-of-failure.md](../fear-of-failure.md) said 56%. The JOLT figure is 56%. costly-signals.md was corrected on 2026-08-28.
2. **"84% failure/challenged (Standish, 2020)": resolved.** 83.8% is the 1994 figure. The 2020 figures put challenged plus failed at 69%. [fear-of-failure.md](../fear-of-failure.md) now states the 2020 figures alongside the 1994 baseline, in both the abstract and the statistics list. Corrected on 2026-08-28.
3. **"189% budget overruns on large projects (McKinsey)": resolved.** 189% is the Standish 1994 average overrun on challenged projects. The McKinsey large-project average is 45%. The statistics list in [fear-of-failure.md](../fear-of-failure.md) now attributes 189% to Standish 1994, and the "zombie projects" claim was rewritten to keep the Standish overrun and the McKinsey value shortfall separate. Corrected on 2026-08-28.
4. **Developer time on technical debt: resolved.** The repo carried 69% of dev time ([fear-of-failure.md](../fear-of-failure.md)) and 44.1 hours per week ([re-aim-framework.md](../re-aim-framework.md)). Both files now carry the CISQ 2022 figure: roughly 33%, or 13.5 hours of a 41-hour week. Corrected on 2026-08-28.
5. **"45% timeline slippage": resolved.** The McKinsey primary reports 45% budget overrun and 7% schedule overrun. [fear-of-failure.md](../fear-of-failure.md) now states both figures. Corrected on 2026-08-28.
6. **Buying group size (6 to 10 decision makers, Gartner): resolved.** The figure is Gartner's B2B Buying Journey research. [buying-center-dynamics.md](../buying-center-dynamics.md) now cites it directly and the inline caveat is removed. Resolved on 2026-08-28.
7. **"Two-thirds of IT projects fail (Standish 2020; BCG 2020)" in two field artifacts: resolved.** The [Contextual Blueprint](../../../practice/implementation-motion/01-discovery-contextual-blueprint.md) and the [Red Team Protocol](../../../practice/implementation-motion/02-validation-red-team-protocol.md) each carried this claim inside a passage marked for reading aloud to the buyer. Two faults. The Standish 2020 figures put challenged plus failed at 69% rather than two-thirds, and that row is only **Primary named** here because the recent reports are paywalled, so it was not quotable externally in the first place. And "BCG, 2020" appears nowhere else in the repository and no primary source for it was ever recorded. Both passages now cite the McKinsey and Oxford 2012 finding of 56% less value than predicted, which is **Primary linked** above and makes the same point about delivered value. Corrected on 2026-09-22. The provenance rule was extended to `practice/` in the same commit, because it had never covered the directory where a statistic gets spoken to a customer.

## Not yet traced

- No-decision rate: 40–60% in enterprise sales (partly channel-level phenomenon). *(moved from channel-collapse.md when the statistics sections were retired, 2026-09; provenance not yet checked)*
- Wörgl scrip historical example: depreciated 1% per month, incentivizing circulation — demurrage in practice. *(moved from channel-collapse.md when the statistics sections were retired, 2026-09; provenance not yet checked)*
- λ ≈ 2.25 (loss aversion coefficient; validated by 2024 meta-analysis across 30+ studies). Represents the parameter $a$ in the transaction cost model. *(moved from prospect-theory.md when the statistics sections were retired, 2026-09; provenance not yet checked)*
- α, β ≈ 0.88 (diminishing sensitivity exponents). *(moved from prospect-theory.md when the statistics sections were retired, 2026-09; provenance not yet checked)*

Statistics quoted in research entries with no provenance row yet. Add a row when each is verified. The sourcing pass of 2026-08-28 cleared the original list into the tables above; two items remain:

- Gartner's $299B 2025 SaaS spending forecast (19.2% growth), in [re-aim-framework.md](../re-aim-framework.md).
- Technical debt consuming 20 to 40% of IT budgets, in [re-aim-framework.md](../re-aim-framework.md).

## Maintaining this file

- A new headline statistic anywhere in `theory/` or `practice/` gets a row here in the same commit, with an honest status. A statistic a field artifact reads aloud to a buyer needs **Primary linked** status, not **Primary named**: reading a paywalled summary figure to a customer is external use.
- A status moves up only when someone opens the primary source and checks the number against it.
- When two files disagree, record the disagreement here first, then fix the files against the primary.
