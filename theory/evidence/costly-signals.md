---
title: "Costly Signals"
layer: theory
kind: evidence
status: active
operationalizes: [axiom-3]
canonical_source: theory/canon/constitution.md
---

# Costly Signals

**Sources:**
- Akerlof, G. (1970). "The Market for Lemons: Quality Uncertainty and the Market Mechanism." *Quarterly Journal of Economics*, 84(3), 488–500. [PDF](https://www.sfu.ca/~wainwrig/Econ400/akerlof.pdf)
- Spence, M. (1973). "Job Market Signaling." *Quarterly Journal of Economics*, 87(3), 355–374. [PDF](https://www.sfu.ca/~allen/Spence.pdf)
- Crawford, V.P. & Sobel, J. (1982). "Strategic Information Transmission." *Econometrica*, 50(6), 1431–1451.
- Zahavi, A. (1975). "Mate selection — a selection for a handicap." *Journal of Theoretical Biology*. (Handicap Principle, evolutionary biology origin of costly signaling.)
- Jensen, M.C. & Meckling, W.H. (1976). "Theory of the Firm: Managerial Behavior, Agency Costs and Ownership Structure." *Journal of Financial Economics*, 3(4), 305–360.
- Eisenhardt, K.M. (1989). "Agency Theory: An Assessment and Review." *Academy of Management Review*, 14(1), 57–74.

**Abstract.** Akerlof showed that information asymmetry about quality causes adverse selection: rational buyers discount price to average quality, driving high-quality sellers out, until the market collapses to lemons. Spence's signaling theory provided the mechanism for restoring quality separation: a signal carries information only when its cost is proportionally lower for the high-quality actor — the *Single Crossing Property*. Crawford-Sobel formalized the limit case: when production costs collapse to zero, communication degenerates into a babbling equilibrium where receivers ignore all messages. The trio together explains why costly, rigorous sales processes are not waste — they are the only mathematically valid mechanism for separating quality vendors from imitators.

**Agency extension (Jensen-Meckling, Eisenhardt).** Akerlof and Spence describe asymmetry before the deal. Agency theory describes what happens after it. Jensen and Meckling showed that when one party acts on another's behalf and effort is unobservable, the acting party has a standing incentive to divert effort, and the cost of preventing that (monitoring, bonding, and the residual loss neither can eliminate) is a real cost of the transaction. Eisenhardt's review separates the two failures cleanly:

- **Adverse selection (before signing).** The buyer cannot distinguish a capable vendor from an incapable one, so they discount price toward the average. This is the failure costly signals solve.
- **Moral hazard (after signing).** Effort becomes unobservable once work begins, on both sides. The seller can under-resource delivery; the buyer can under-resource adoption. This is the failure governance solves, not signals.

Agency friction also runs along two vectors at once, and TCG treats them differently. The **inter-organizational vector** is the buyer-seller gap that $\Delta_A$ measures. The **intra-organizational vector** runs inside the buying committee, between an executive sponsor and the departments evaluating on their own scorecards. Costly signals reduce the first. They do nothing for the second, which is why the Blueprint and Red Team map stakeholder incentives rather than simply proving vendor capability.

**Key claims:**
- Information asymmetry without signals collapses markets to average (lemons) quality.
- Adverse selection and moral hazard are distinct failures requiring distinct instruments. Signals address the first, governance the second.
- Agency friction operates inside the buyer as well as across the buyer-seller boundary. A perfectly credible vendor still stalls in a misaligned committee.
- A signal carries information only if it satisfies the Single Crossing Property — cheaper to produce for the high-quality actor.
- Cheap talk has zero signal value; without cost, the receiver's rational response is to ignore.
- Paid pilots, rigorous discovery, and resource-intensive POCs are credible signals because lemons cannot afford them.
- Bilateral signaling is required — buyer refusal to invest signals low organizational commitment.
- When all signals become production-cheap, the channel reaches a babbling equilibrium (Crawford-Sobel).

**Supports in TCG:**
- **Axiom III — Law of Uncertainty Inflation** — direct theoretical basis. Friction is the signal, asymmetry is the noise.
- **Friction Allocation Principles** — all four principles derive from the Single Crossing Property.
- **Single Crossing Property** — direct.
- **Akerlof Exit Threshold** — direct.
- **Jevons Vulnerability** — Crawford-Sobel babbling equilibrium is what Jevons collapse produces at the channel level.
- **Axiom II — Law of Asset Specificity, governance corollary** — via the moral hazard axis. Once signing removes the screening problem, unobservable effort on both sides becomes the binding constraint, which is what the MIP's mutual resource commitments address.
- **$I_{buyer}$ in the asymmetry model** — the exponential decay of buyer doubt against accumulated vendor proof ($\nu e^{-\kappa K_{vendor}}$ in [models.md](../reference/models.md)) is Spence's separating equilibrium expressed as a field-measurable quantity.

**Quotes and statistics.** Citable passages from this source are collected in [source-quotes.md](../../publishing/02-tools/source-quotes.md). Its numbers are recorded, with provenance, in the [citation audit](./citation-provenance-audit.md).

---

## Extension: Trust Proxies vs. Produced Signals (drafted June 2026, PENDING REVIEW)

**Origin.** Derived from behavioral health care-enablement field research. Not yet canonical. Review before citing in field assets.

**The distinction.** Markets carry two kinds of trust instruments, and the difference determines what happens when friction is removed.

- A **trust proxy** is inherited from a third party and stands in for verification the buyer never performs directly. Credentials, certifications, network membership, and procedural friction (credentialing queues, security reviews, procurement gauntlets) are proxies. Proxies are gameable because the cost can be absorbed or amortized without producing the underlying quality. Delegated credentialing in behavioral health is the type case. Platforms absorbed the proxy's cost across thousands of providers, and the proxy survived in form while dying in function.
- A **produced trust signal** is generated by the seller's own observable performance. Measured, published outcomes are the base case. Produced signals satisfy the Single Crossing Property directly, because the cost of producing them falls as actual quality rises.

Removing a proxy without substituting a produced signal does not reduce friction. It reopens Akerlof's information gap, and the counterparty re-prices the pool to the average. Empirical instance: Aetna's flattening of psychotherapy rates across duration and credential level for Alma-contracted therapists, May 2026.

**Risk transfer as the apex signal.** A seller who takes financial risk on the buyer's outcome (performance guarantees, full-risk and value-based contracts) produces the strongest separation mechanism available. For the high-quality seller, the expected cost of the guarantee approaches zero, because they will deliver. For the lemon, the expected cost is the full penalty. Faking the signal costs the faker. This is the Single Crossing Property at maximum spread, and it is self-enforcing. No third-party verification is required because the contract itself executes the penalty. Empirical instance: firsthand's full-risk serious-mental-illness contract with Carelon, in which the provider holds total cost of care across physical, behavioral, and pharmacy spend ([BHB VALUE coverage, March 2026](https://bhbusiness.com/2026/03/12/payers-want-more-than-access-they-want-results/)).

**Signal hierarchy (weakest to strongest):**
1. **Cheap talk:** marketing claims. Zero production cost, zero information (Crawford-Sobel).
2. **Trust proxies:** credentials, certifications, network membership. Third-party cost, gameable by aggregation or delegation.
3. **Produced outcomes:** measured, published results. Seller-borne cost, externally verifiable.
4. **Risk transfer:** seller holds the financial downside of the buyer's outcome. Self-enforcing, unfakeable.

**Supports in TCG (proposed):**
- **Axiom III — Law of Uncertainty Inflation**: extends the friction-as-signal claim with a quality ordering of signals. Friction removal is safe only when the deleted proxy is replaced at tier 3 or 4.
- **Friction Allocation Principles**: candidate fifth principle, or a refinement of existing ones. When allocating friction, prefer friction that forces tier-3/tier-4 signal production over friction that merely gates access.
- **Δ_A in the Fundamental Equation**: tier-4 signals collapse Buyer Uncertainty ($I_{buyer}$) faster than any other mechanism, because the buyer no longer needs to resolve uncertainty before contracting. The seller has priced it.
