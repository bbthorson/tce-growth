---
title: "Costly Signals"
layer: theory
status: active
operationalizes: [axiom-1, axiom-2]
canonical_source: theory/01-foundation/00-tcg-constitution.md
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

Agency friction also runs along two vectors at once, and TCG treats them differently. The **inter-organizational vector** is the gap between buyer and seller. The **intra-organizational vector** runs inside the buying committee, between an executive sponsor and the departments evaluating on their own scorecards. Costly signals reduce the first. They do nothing for the second, which is why the [Bargaining Ledger](../../practice/bargaining-ledger.md) maps each decision role's reservation rather than simply proving vendor capability.

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
- **Claim 3.** Direct basis. Akerlof is why buyers who cannot tell good sellers from bad assume the worst and many buy from no one. Spence is why a signal informs only when it costs a weak seller more than a strong one. Crawford and Sobel give the end state when a message costs nothing to send: receivers ignore all of them, which [channel-collapse.md](./channel-collapse.md) shows at the level of a channel.
- **Claim 8.** A commitment the seller would not make if it expected to fail is a Spence signal. The extension below ranks such signals and names two limits on a guarantee.
- **Claim 7.** A signal lowers doubt between the two firms. It does nothing for disagreement inside the buyer, which is why a seller its buyer believes can still stall in an organization that has not agreed.
- **Claim 12.** Once signing ends the screening problem, effort neither side can observe becomes the problem. The staged plan in the [Enforcement Ledger](../../practice/enforcement-ledger.md) governs it.
- **Friction Allocation Principles.** The first three derive from the single crossing property, and the fourth from the theory of certification intermediaries. The section below says why there are four.

## Why four principles

Each Friction Allocation Principle answers a different question a receiver needs answered before a signal can move what it believes. The [Friction Allocation Diagnostic](../../practice/friction-allocation-diagnostic.md) applies them.

| Principle | The question it answers | Where it comes from |
|---|---|---|
| 1. The cost cannot be automated away | Does the signal cost a weak sender more than a strong one? | The single crossing property. A cost tools remove falls for every sender alike, and the signal pools. |
| 2. The claimant bears the cost | Does the cost fall on the party whose quality is in doubt? | The single crossing property again. A cost the receiver pays tells it nothing about the sender. |
| 3. The cost scales with the claim | Is the cost large enough to separate at this claim's stakes? | Spence's condition, read against what a seller earns by being told apart. A larger claim raises what a weak seller gains by faking it. |
| 4. The adjudicator loses when a bad signal passes | Does whoever certifies the signal keep certifying honestly over time? | The theory of certification intermediaries, carried in [information-environment.md](./information-environment.md). An adjudicator with nothing to lose drifts from screening toward extraction. Lizzeri (1999) adds that even an honest certifier gains by coarsening what it reveals to pass or fail, so a staked adjudicator that discloses a grade beats one that does not. |

The first three are conditions on the sender's cost. The fourth is a condition on the institution that carries the signal across time and buyers. Each is necessary: a signal that is too cheap, paid for by the wrong party or vouched for by someone with nothing to lose is cheap talk, which informs only as far as the two sides' interests already agree. The third also fails the other way, and evidence far costlier than the claim needs is waste, which is what claim 6 says of heavy proof laid over a plug-in purchase. The framework claims necessity only. Whether the four suffice is untested, and the trust-proxy extension below is the standing candidate for a fifth.

**Quotes and statistics.** Citable passages from this source are collected in [source-quotes.md](../../publishing/02-tools/source-quotes.md). Its numbers are recorded, with provenance, in the [citation audit](./audits/citation-provenance-audit.md).

---

## Extension: Trust Proxies vs. Produced Signals (drafted June 2026, PENDING REVIEW)

**Origin.** Derived from behavioral health care-enablement field research. Not yet canonical. Review before citing in field assets.

**The distinction.** Markets carry two kinds of trust instruments, and the difference determines what happens when friction is removed.

- A **trust proxy** is inherited from a third party and stands in for verification the buyer never performs directly. Credentials, certifications, network membership, and procedural friction (credentialing queues, security reviews, procurement gauntlets) are proxies. Proxies are gameable because the cost can be absorbed or amortized without producing the underlying quality. Delegated credentialing in behavioral health is the type case. Platforms absorbed the proxy's cost across thousands of providers, and the proxy survived in form while dying in function.
- A **produced trust signal** is generated by the seller's own observable performance. Measured, published outcomes are the base case. Produced signals satisfy the Single Crossing Property directly, because the cost of producing them falls as actual quality rises.

Removing a proxy without substituting a produced signal does not reduce friction. It reopens Akerlof's information gap, and the counterparty re-prices the pool to the average. Empirical instance: Aetna's flattening of psychotherapy rates across duration and credential level for Alma-contracted therapists, May 2026.

**Risk transfer as the apex signal.** A seller who takes financial risk on the buyer's outcome (performance guarantees, full-risk and value-based contracts) produces the strongest separation mechanism available. For the high-quality seller, the expected cost of the guarantee approaches zero, because they will deliver. For the lemon, the expected cost is the full penalty. Faking the signal costs the faker. This is the Single Crossing Property at its widest spread. Two limits keep it short of unfakeable. It screens on balance sheet as well as quality: a strong seller too small to carry the penalty cannot send it, and a weak one with capital to spare can. And it separates only when the outcome is the seller's to deliver. Where the buyer can under-resource adoption, the moral hazard the agency section above names, a full-risk contract makes the seller pay for the buyer's slack, and someone has to adjudicate whose miss it was, which is the fourth Friction Allocation Principle. Mutual commitments, as in the Mutual Implementation Plan, answer the second limit. Empirical instance: firsthand's full-risk serious-mental-illness contract with Carelon, in which the provider holds total cost of care across physical, behavioral, and pharmacy spend ([BHB VALUE coverage, March 2026](https://bhbusiness.com/2026/03/12/payers-want-more-than-access-they-want-results/)).

**Signal hierarchy (weakest to strongest):**
1. **Cheap talk:** marketing claims. Zero production cost, zero information (Crawford-Sobel).
2. **Trust proxies:** credentials, certifications, network membership. Third-party cost, gameable by aggregation or delegation.
3. **Produced outcomes:** measured, published results. Seller-borne cost, externally verifiable.
4. **Risk transfer:** seller holds the financial downside of the buyer's outcome. The widest separation, within the two limits above.

**Supports in TCG (proposed):**
- **Claim 3**: extends it with an ordering of signals by quality. Friction removal is safe only when the deleted proxy is replaced at tier 3 or 4.
- **Friction Allocation Principles**: candidate fifth principle, or a refinement of existing ones. When allocating friction, prefer friction that forces tier-3/tier-4 signal production over friction that merely gates access.
- **Claim 8**: a tier-4 signal does two things to the buyer, and they should be kept apart. As insurance, it means the buyer no longer has to resolve its uncertainty before contracting, because the seller carries the loss. As a signal, the offer itself narrows the uncertainty, because only a seller confident of delivering can afford it. [02-mathematical-models.md](../01-foundation/02-mathematical-models.md) section 1.3 counts the first as a transfer and the second as verification.
