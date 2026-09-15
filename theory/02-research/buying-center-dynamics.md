---
title: "Buying Center Dynamics"
layer: theory
status: active
operationalizes: [axiom-2, axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
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
- **Axiom II — Law of Uncertainty Inflation** — supplies the internal structure of $F_{consensus}$. The Constitution names consensus cost. Cyert-March and Webster-Wind explain what generates it.
- **Consensus Friction model** — direct theoretical basis for $F_{consensus} = \alpha N^{\beta}(1 + \text{Var}(I_i))$ in [02-mathematical-models.md](../01-foundation/02-mathematical-models.md). The exponent $\beta > 1$ follows from channel growth, and the variance term follows from goal heterogeneity.
- **The Red Team Protocol** — operationalizes variance reduction. Forcing stakeholders to state failure modes aloud converts quasi-resolution into explicit trade-off, which is the only mechanism that lowers $\text{Var}(I_i)$ before signature.
- **The Saboteur** (CFIR field mapping) — the buying center model explains why a saboteur is structurally normal rather than exceptional. A stakeholder whose measured objectives worsen under the initiative is behaving rationally by blocking it.
- **Axiom III — Law of Governance** — intra-organizational alignment is a cooperation condition applied inside the buyer, not only across the buyer-seller boundary.

**Notable quotes:**
- The proposal is evaluated once per stakeholder, against a different objective each time, and it must survive all of them.
- A saboteur is usually not irrational. They are optimizing a scorecard the seller never read.
- Committee size sets the floor on consensus cost. Goal conflict sets the ceiling.

**Notable statistics:**
- The typical buying group for a complex B2B purchase involves 6 to 10 decision makers (Gartner, [The B2B Buying Journey](https://www.gartner.com/en/sales/insights/b2b-buying-journey)).
- 40–60% of B2B deals end in "No Decision" (Dixon/McKenna). See [fear-of-failure.md](./fear-of-failure.md) for the verified chain.
