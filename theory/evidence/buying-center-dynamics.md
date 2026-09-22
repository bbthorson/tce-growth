---
title: "Buying Center Dynamics"
layer: theory
kind: evidence
status: active
operationalizes: [axiom-1, axiom-3]
canonical_source: theory/canon/constitution.md
---

# Buying Center Dynamics

**Sources:**
- Cyert, R.M. & March, J.G. (1963). *A Behavioral Theory of the Firm*. Prentice-Hall.
- Webster, F.E. & Wind, Y. (1972). "A General Model for Understanding Organizational Buying Behavior." *Journal of Marketing*, 36(2), 12–19.
- Johnston, W.J. & Bonoma, T.V. (1981). "The Buying Center: Structure and Interaction Patterns." *Journal of Marketing*, 45(3), 143–156.

**Abstract.** Classical economics treats the firm as a single agent maximizing one utility function. Cyert and March showed it is nothing of the kind. A firm is a coalition of participants holding conflicting goals, operating under bounded rationality, and resolving disagreement through sequential attention and negotiated quasi-resolution rather than optimization. Webster and Wind carried this into procurement as the *Buying Center*: the set of people who participate in a purchase decision, each evaluating the same proposal against a different objective. The practical consequence is that a B2B proposal is never evaluated once. It is evaluated N times against N objectives, and it must survive all of them.

**Key claims:**
- The buying organization is a coalition, not an agent. It has no single utility function to appeal to.
- Buying center members apply distinct and sometimes mutually exclusive evaluation criteria: strategic outcome (executive sponsor), risk and compliance exposure (security and legal), cost predictability (finance and procurement), and workflow disruption (operations and end users).
- Coordination cost grows faster than committee size, because communication channels grow as $N(N-1)/2$.
- Conflict is resolved by quasi-resolution rather than reconciliation. Departments pursue incompatible goals sequentially, which surfaces as late-stage vetoes rather than early-stage debate.
- Goal heterogeneity, not size alone, drives paralysis. A large committee that agrees moves faster than a small one that does not.
- Any member holding veto power is a decision maker regardless of title or seniority.

**Supports in TCG:**
- **Axiom I — Law of Transaction Cost Composition** — supplies the internal structure of the bargaining cost, $F_{consensus}$. The Constitution names the bargaining cost, which the field calls consensus. Cyert-March and Webster-Wind explain what generates it.
- **Consensus Friction model** — direct theoretical basis for $F_{consensus} = \alpha N^{\beta}(1 + \text{Var}(I_i))$ in [models.md](../reference/models.md). The exponent $\beta > 1$ follows from channel growth, and the variance term follows from goal heterogeneity.
- **The Red Team Protocol** — operationalizes variance reduction. Forcing stakeholders to state failure modes aloud converts quasi-resolution into explicit trade-off, which is the only mechanism that lowers $\text{Var}(I_i)$ before signature.
- **The Saboteur** (CFIR field mapping) — the buying center model explains why a saboteur is structurally normal rather than exceptional. A stakeholder whose measured objectives worsen under the initiative is behaving rationally by blocking it.
- **Axiom II — Law of Asset Specificity, governance corollary** — intra-organizational alignment is a cooperation condition applied inside the buyer, not only across the buyer-seller boundary.

**Quotes and statistics.** Citable passages from this source are collected in [source-quotes.md](../../publishing/02-tools/source-quotes.md). Its numbers are recorded, with provenance, in the [citation audit](./citation-provenance-audit.md).
