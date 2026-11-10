---
title: "Mathematical Models"
layer: theory
status: active
version: 3.0
operationalizes: [axiom-2]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# Mathematical Models

**Version:** 3.0
**Purpose:** To show the one piece of accounting the [Constitution](./00-tcg-constitution.md) relies on: price is a transfer. What leaves the buyer arrives at the seller, so a discount changes the split and leaves the work of buying the same size. Claim 8 states the result, and this file derives it.

> [!NOTE]
> **This file used to be longer.** Version 2.0 specified forms for the gaps, the consensus cost, urgency decay, future loss and the thresholds, in sections 1.5 to 9. The trim retired them on 2026-11-10, because only this result serves a claim. A reference elsewhere to one of those sections means version 2.0: `git show 0e13ebf:theory/01-foundation/02-mathematical-models.md`.

Nothing here is measured. The two conditions structure an argument, and they forecast nothing.

---

## 1. The Two Conditions

### 1.1 One condition per party

$$S_b = V_{switch} - P - \sum_{k} I^b_k - L_b \qquad S_s = P - C_{deliver} - \sum_{k} I^s_k - L_s$$

| Symbol | Meaning |
|---|---|
| $S_b$, $S_s$ | What the buyer and the seller each gain from the deal. Each goes ahead only when its own is above zero |
| $V_{switch}$ | What the change is worth to the buyer over its next best alternative, which includes building it and doing nothing |
| $P$ | Price over the relationship |
| $C_{deliver}$ | The seller's cost of delivering against that price |
| $I^b_k$, $I^s_k$ | What the buyer and the seller each put in before signature against cost $k$: search, consensus or implementation |
| $L_b$, $L_s$ | What each party expects to lose after signature, if the product does not work here or the other side squeezes it |

The first condition is the buyer's question at Time1, and the second is the seller's.

### 1.2 Units

**Every term is a fraction of annual contract value.** That makes the two conditions comparable. A seller can price its own engineering hours, and a buyer can price the staff time its integration will take. A deal at list price with no other cost has $P = 1$, and an expected loss of 0.75 means three quarters of a year's contract value.

### 1.3 Price cancels

Adding the two conditions:

$$S_b + S_s = V_{switch} - C_{deliver} - \sum_{k} \left(I^b_k + I^s_k\right) - L_b - L_s$$

$P$ is gone, because price is a transfer: what leaves the buyer arrives at the seller. The sum is what the deal creates, and price appears nowhere in it. The rest of this section follows from that accounting and from no coefficient.

**A discount moves the split.** While the same people must approve, a discount adds to $S_b$ exactly what it takes from $S_s$, and the sum stays where it was. There is one exception. A price taken under a spend threshold removes an approver and the consensus work that approver required, so the buyer's $I^b_{consensus}$ falls. That role's concern returns at renewal.

**What raises the sum.**

| What the seller does | What it moves | Effect on the sum |
|---|---|---|
| Discounts | $P$ | None while the same roles must approve. Surplus moves from seller to buyer one for one |
| Makes a commitment: a guarantee, capped overages, fees staged against delivery | Part of $L_b$ onto the seller | None for the part that only moves the loss. It rises by as much as the commitment lowers the loss, by changing what the seller does or by showing which sellers can afford to offer it |
| Verifies: discovery, proof in the buyer's own environment | $L$ for whichever party could not check | Rises. A loss both sides were carrying shrinks |

**A guarantee is part transfer and part verification.** The transfer moves loss without shrinking it. The verification is Spence's selection effect. A seller confident of delivering expects to pay little on its guarantee, and a weak one expects to pay the full penalty, so the offer itself tells the buyer something. The sorting is clean only when every seller can carry the penalty, because a guarantee also screens on balance sheet. It is clean only when the outcome is the seller's to deliver, because a buyer that under-resources adoption makes the seller pay for its slack. [costly-signals.md](../02-research/costly-signals.md) carries the argument.

**A commitment or a proof can close a deal that no discount could.** When the sum is negative, no price makes both conditions positive at once, and only something that raises the sum can rescue the deal. When the sum is positive, a discount can close the deal by moving the split, and so can verification. The figure under claim 8 of the Constitution plots both cases against price. It is a fixed image, and the code that drew it is in git history with the rest of the math.

**Hold-up is a transfer too.** What one side takes at a renegotiation, the other receives. Hold-up costs the pair through the investment a party declines to make because it would keep only part of the return (Grossman and Hart 1986). Claim 11 states the consequence.

**A discount still changes which deals happen and how long they last.** At a newspaper and an online grocer, customers acquired on a deeper discount bought again less (Lewis 2006). What stays empirical is whether a given verification costs less than the loss it removes, since the verification's own cost is an investment under Axiom II.

### 1.4 Moving investment between parties

Write each party's cost of doing a unit of the work against cost $k$ as $\theta^b_k$ and $\theta^s_k$. Moving a share $w$ of that work from buyer to seller changes the sum by

$$\Delta(S_b + S_s) = w\left(\theta^b_k - \theta^s_k\right) - \Delta L_b - \Delta L_s$$

The first term is specialization. It is positive when the seller does the work more cheaply, which is the Constitution's premise for why a seller carries part of a buyer's cost. The other two terms enter with a minus because each condition subtracts its loss. The move can lower the buyer's expected loss, by catching a misfit before it surfaces in use. It also raises the seller's, because the seller's work is now specific to this buyer.

With equal unit costs and no change in either loss, the move only changes the split. It can still close a deal, because it lifts $S_b$ above zero whenever $S_s$ has room to fall. A forward-deployed engineer is the case where all three terms move, and claim 9 states who pays for it.

---

## Related

- [00-tcg-constitution.md](./00-tcg-constitution.md), claim 8 for the result and claims 9 and 11 for its two neighbors.
- [costly-signals.md](../02-research/costly-signals.md), for why a commitment informs.
- [value-and-persuasion.md](../02-research/value-and-persuasion.md), for the evidence on discounts.
- [citation-provenance-audit.md](../02-research/audits/citation-provenance-audit.md), which records the provenance of the Lewis (2006) finding.
