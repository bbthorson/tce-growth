---
title: "Fear of Failure: The Empirical Evidence"
layer: theory
status: active
operationalizes: [axiom-2, axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# Fear of Failure: The Empirical Evidence

**Sources:**
- The Standish Group. *CHAOS Report* (1994–2024). Longitudinal IT project outcomes study. Original sample: 3,682 projects. [PDF (1994 baseline)](https://www.utdallas.edu/~chung/SYSM6309/chaos_report.pdf)
- McKinsey & Company / University of Oxford. "Delivering large-scale IT projects on time, on budget, and on value." Sample: 5,400+ IT projects. [Link](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/delivering-large-scale-it-projects-on-time-on-budget-and-on-value)
- Gartner Research. Multiple surveys (2022–2025) on buyer regret, rep-free preferences, GenAI adoption, AI personalization.
- CISQ (Consortium for Information & Software Quality). *Cost of Poor Software Quality in the U.S.: A 2022 Report.* [Link](https://www.it-cisq.org/the-cost-of-poor-quality-software-in-the-us-a-2022-report/)
- Boehm, B. & Basili, V.R. (2001). "Software Defect Reduction Top 10 List." *IEEE Computer*, 34(1), 135–137. [PDF](https://www.cs.umd.edu/projects/SoftEng/ESEG/papers/82.78.pdf)
- Dixon, M. & McKenna, T. (2022). *The JOLT Effect: How High Performers Overcome Customer Indecision.* Portfolio. [Site](https://www.jolteffect.com/)

**Abstract.** This is the empirical evidence behind the Fear Economy thesis: documented failure rates, regret data, and "No Decision" statistics that explain why buyers default to inaction. Project success rates have stayed low for three decades (69% of projects were challenged or failed in the 2020 CHAOS data, against 83.8% in the 1994 baseline); 56% of buyers regret recent purchases (Gartner); 40–60% of qualified pipelines die in "No Decision" — and 56% of that is *FOMU* (Fear of Messing Up), not status quo preference. The Standish/McKinsey/JOLT corpus together provides the quantitative case that buyer risk-aversion is rational, not pathological, and explains why generic FOMO sales tactics backfire 84% of the time on indecisive buyers.

**Key claims:**
- Project success rates have never cleared 40% in three decades of CHAOS tracking: 16.2% in 1994, 37% in 2012, 31% in 2020 (Standish).
- Roughly half of projects become "zombies": operational but over budget and under-delivering. Standish counted 52.7% challenged in 1994 (with 189% average cost overruns) and 50% in 2020.
- The average large IT project runs 45% over budget while delivering 56% less value than predicted (McKinsey/Oxford).
- 56% of B2B buyers regret their most recent purchase (Gartner).
- 56% of "No Decision" is fear-driven (FOMU), not preference-for-status-quo.
- FOMO sales tactics *increase* loss likelihood by 84% on indecisive buyers (Dixon/McKenna).
- Fixing a defect after delivery costs up to 100× more than fixing it during requirements and design on large systems, and closer to 5× on small ones (Boehm & Basili).
- 17% of large initiatives present existential threat to the organization (McKinsey).

**Supports in TCG:**
- **Axiom II — Law of Asset Specificity** — empirical scale of $F_{implementation}$. Documented failure rates are why implementation is the dominant cost component in high-specificity deals, and the 17% existential-threat rate is why a buyer facing hold-up risk prefers the "make" alternative (Williamson). This is the under-frictioned Structural failure mode measured.
- **Axiom III — Law of Uncertainty Inflation** — empirical grounding for why $\Delta_A$ multiplies friction rather than reducing value. Also the limit case: buyers leave the market entirely (Akerlof saturation) when failure rates exceed risk tolerance, because no costly signal can credibly reduce a gap that wide.
- **Akerlof Exit Threshold** (clarifying concept, elaborating Axiom III) — the 40–60% No Decision rate is the threshold being crossed.
- **Decay Clock** (bridge concept) — 17% existential threat rate and technical debt servicing (roughly a third of developer time, CISQ 2022) describe how time pressure compounds.
- **Reputation Depreciation** — 60% renewal regret rate (Gartner 2023) is the failure-mode signal.

**Notable quotes:**
- "The primary barrier to revenue is not the competitor's feature set; it is the buyer's calculation of risk."
- "High-pressure (FOMO) tactics increase the likelihood of losing the deal by 84% when the buyer is indecisive."
- "Organizations are so consumed by servicing the debt of previous failures that they lack the bandwidth to innovate."

**Notable statistics:**
- 69% project failure/challenged rate (Standish, 2020: 31% success, 50% challenged, 19% failed). The 1994 baseline was 83.8%.
- 56% purchase regret (Gartner, 2022).
- 40–60% "No Decision" pipeline loss (Dixon/McKenna JOLT Effect).
- 189% average cost overrun on challenged projects (Standish, 1994).
- 100× cost multiplier for post-delivery fixes vs. the requirements and design phase, on large systems (Boehm & Basili, 2001).
- $2.41 trillion CPSQ (Cost of Poor Software Quality, CISQ 2022).
- 17% existential threat rate on large initiatives (McKinsey).
- 45% budget overrun and 7% schedule overrun on the average large project (McKinsey/Oxford).
- 60% renewal regret rate (Gartner, 2023).
- 30% GenAI project abandonment post-POC (Gartner).
- Roughly 300 SaaS applications per enterprise (Zylo, 2026 index: average 305, median 240), with about half of licenses unused (Zylo, 2024: 49% utilization).

> **Citation Provenance.** Every statistic above traces to a primary source documented in [audits/citation-provenance-audit.md](./audits/citation-provenance-audit.md).
