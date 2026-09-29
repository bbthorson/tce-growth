---
title: "Buying Center Dynamics"
layer: theory
status: active
operationalizes: [axiom-1, axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# Buying Center Dynamics

**Sources:**
- Cyert, R.M. & March, J.G. (1963). *A Behavioral Theory of the Firm*. Prentice-Hall.
- Webster, F.E. & Wind, Y. (1972). "A General Model for Understanding Organizational Buying Behavior." *Journal of Marketing*, 36(2), 12–19.
- Johnston, W.J. & Bonoma, T.V. (1981). "The Buying Center: Structure and Interaction Patterns." *Journal of Marketing*, 45(3), 143–156.
- Stasser, G. & Titus, W. (1985). "Pooling of Unshared Information in Group Decision Making: Biased Information Sampling During Discussion." *Journal of Personality and Social Psychology*, 48(6), 1467–1478.
- Lu, L., Yuan, Y.C. & McLeod, P.L. (2012). "Twenty-Five Years of Hidden Profiles in Group Decision Making: A Meta-Analysis." *Personality and Social Psychology Review*, 16(1), 54–75.
- Kuran, T. (1995). *Private Truths, Public Lies: The Social Consequences of Preference Falsification.* Harvard University Press.
- Jackall, R. (1988). *Moral Mazes: The World of Corporate Managers.* Oxford University Press.
- Arikan, A.T. (2020). "Opportunism Is in the Eye of the Beholder: Antecedents of Subjective Opportunism Judgments." Venue to be verified.

The last five sources reached the repository through an external review in 2026-09. Citations are to be verified against the record before any is quoted.

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
- **Consensus Friction model** — direct theoretical basis for $F_{consensus} = \alpha N^{\beta}(1 + \text{Var}(I_i))$ in [02-mathematical-models.md](../01-foundation/02-mathematical-models.md). The exponent $\beta > 1$ follows from channel growth, and the variance term follows from goal heterogeneity.
- **The Red Team Protocol** — operationalizes variance reduction. Forcing stakeholders to state failure modes aloud converts quasi-resolution into explicit trade-off, which is the only mechanism that lowers $\text{Var}(I_i)$ before signature.
- **The Saboteur** (CFIR field mapping) — the buying center model explains why a saboteur is structurally normal rather than exceptional. A stakeholder whose measured objectives worsen under the initiative is behaving rationally by blocking it.
- **Axiom II — Law of Asset Specificity, governance corollary** — intra-organizational alignment is a cooperation condition applied inside the buyer, not only across the buyer-seller boundary.

---

## Extension: hidden profiles and the private diagnosis (2026-09)

**The room suppresses what one member knows.** Stasser and Titus showed that groups over-sample information every member already holds and under-sample what one member holds alone, and the meta-analysis by Lu, Yuan and McLeod across twenty-five years of hidden-profile experiments confirms that groups facing distributed private information rarely reach the answer the pooled information supports. Kuran's preference falsification says why the private information is withheld: people misrepresent what they want when the social cost of candor is high. Jackall's ethnography says what the cost is inside a corporation: managers survive on calculated ambiguity, and a written record of a parochial interest is ammunition for a peer.

**What follows for the bargaining instrument.** The premise of the seat ledger in [08-from-axioms-to-instruments.md](../01-foundation/08-from-axioms-to-instruments.md) is confirmed: positions stated in a room are not evidence of anyone's exposure. Its first design was wrong in one respect: occupants will state a reservation one to one and will not write it on a document a seller holds and a peer can find, and Arikan adds that a probe of private vulnerability reads as opportunism however it is framed. So the diagnosis is private and the arrangement is shared, objections are collected apart before any room convenes, and Axiom III's bargaining row in the Constitution says so.

**Quotes and statistics.** Citable passages from this source are collected in [source-quotes.md](../../publishing/02-tools/source-quotes.md). Its numbers are recorded, with provenance, in the [citation audit](./audits/citation-provenance-audit.md).
