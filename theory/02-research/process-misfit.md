---
title: "Process Misfit"
layer: theory
status: active
operationalizes: [axiom-1, axiom-2]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# Process Misfit

**Sources:**
- Soh, C., Kien, S.S. & Tay-Yap, J. (2000). "Enterprise Resource Planning: Cultural Fits and Misfits: Is ERP a Universal Solution?" *Communications of the ACM*, 43(4), 47–51.
- Strong, D.M. & Volkoff, O. (2010). "Understanding Organization-Enterprise System Fit: A Path to Theorizing the Information Technology Artifact." *MIS Quarterly*, 34(4), 731–756.
- Williamson, O.E. (1985). *The Economic Institutions of Capitalism.* Free Press. (Asset specificity; see [transaction-cost-economics.md](./transaction-cost-economics.md).)

**Abstract.** Packaged software rarely matches the workflow of the organization installing it. Soh, Kien and Tay-Yap named that gap *misfit*, and showed that a buyer who hits one picks from exactly four responses: change the organization to match the software, accept the shortfall, build a workaround, or customize the package. Strong and Volkoff spent three years inside a single enterprise system implementation and decomposed misfit into six domains, each running in two directions. The consequence for TCG is that implementation cost belongs to neither party on its own. It is a property of the distance between a specific buyer and a specific product, which means the seller can measure it before signature and no feature list will ever reveal it.

**Key claims:**
- Misfit is the gap between what the package delivers and what the adopting organization requires. It is a relational measure, not a product defect and not a buyer deficiency.
- Buyers resolve misfit four ways: adapt the organization, live with the shortfall, institute a workaround, or customize the package. The four carry different costs and different reversibility, and the buyer chooses under uncertainty about all four.
- Strong and Volkoff identified six misfit domains: functionality, data, usability, role, control, and organizational culture. A product demonstration exposes the first two. The remaining four surface during implementation.
- Within each domain, misfit runs in two directions. A *deficiency* means the system does less than the organization needs. An *imposition* means the system forces a practice the organization did not ask for. Impositions generate resistance that deficiencies do not, because someone must change their behavior rather than merely go without.
- The same package fits one buyer and fails at the next. Vendor-side evidence therefore cannot resolve misfit, and a reference customer proves only that misfit was low in one other environment.
- A codified workflow does not reduce misfit on its own. Codification records the choices an organization has already made, and those recorded choices are precisely what the package must then match.

**Supports in TCG:**
- **Axiom I — Law of Transaction Cost Composition** — supplies the internal structure of $F_{implementation}$. Williamson explains why asset specificity (an investment locked to one relationship) raises governance cost. The misfit literature explains what that specificity consists of in a software deal: six named domains a seller can inspect one at a time.
- **Axiom II — Law of Uncertainty Inflation** — misfit is invisible to both parties at first contact, which makes it a direct generator of the bilateral asymmetry gap $\Delta_A$. The buyer cannot articulate exception paths they have stopped noticing. The seller cannot see them from outside. Neither side is withholding information; the information does not yet exist in a form either can transmit.
- **Contextual Blueprint** — the six domains give the Blueprint a coverage checklist. Role misfit and control misfit are what stakeholder mapping is for, and they are the two domains a demonstration-led process never reaches.
- **Red Team Protocol** — deficiency and imposition are two distinct classes of failure mode. A Red Team that surfaces only deficiencies has done half the work, because impositions are what produce the Saboteur described in [buying-center-dynamics.md](./buying-center-dynamics.md).
- **Milestone Valuation Model** — the four resolution responses are what a phase gate actually chooses between. A gate that has not named which response the buyer will take has not resolved the uncertainty it claims to price.

**Open question this source raises.** The [Deal Triage Calculator](../../practice/deal-triage-calculator.md) treats workflow maturity as a precondition gate and workflow divergence as a multiplier on the implementation component. The misfit literature suggests workflow codification and implementation cost are coupled rather than independent, because codification is itself a relationship-specific investment. Resolving this requires deciding whether workflow definition and workflow divergence are one variable or two. The framework treats these as two variables and does not argue that they are.

**Notable quotes:**
- Implementation cost is not a property of the product or of the buyer. It is the distance between them, and distance takes two points to measure.
- A demonstration can only fail on functionality and data. The four domains that kill implementations do not appear on a screen.
- A deficiency asks the buyer to go without. An imposition asks a named person to work differently. Only one of those creates an enemy.
- Codifying a workflow does not make it standard. It makes it explicit, and explicit is what a package has to match.

**Notable statistics:** None. Both sources are qualitative, and no headline number from either is used elsewhere in this repository. Practitioner sources on process standardization circulate figures for cost reduction and revenue growth that trace to no primary study; those figures are deliberately excluded. See [audits/citation-provenance-audit.md](./audits/citation-provenance-audit.md) for the standard.
