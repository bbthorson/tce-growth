---
title: "Friction Allocation Diagnostic"
layer: practice
status: active
version: 1.0
operationalizes: [axiom-2]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# Friction Allocation Diagnostic

**Version:** 1.0
**Audience:** Sales reps, sales leadership, marketing, anyone designing or evaluating a signal mechanism.
**Goal:** Check whether a signal mechanism — a sales artifact, an outreach channel, a marketing asset, a third-party validator — actually reduces buyer-side uncertainty, or whether it is cheap talk dressed up as effort.

**Canonical Reference:** [TCG Constitution, Axiom II — Law of Uncertainty Inflation](../theory/01-foundation/00-tcg-constitution.md). The four principles are primary derivations of Axiom II.

| | |
|---|---|
| **Inputs** | A signal mechanism: a sales artifact, a channel for outreach, a piece of marketing collateral, an evaluation by a third-party adjudicator (e.g., a ratings firm). |
| **Outputs** | A pass/fail diagnosis against the four principles, with named violations and prescribed fixes. |
| **When to run** | (1) Designing a new artifact or process. (2) Diagnosing why an existing signal mechanism isn't producing the expected $\Delta_A$ reduction. (3) Evaluating channels or platforms before committing to them. |
| **Owner** | Whoever is designing or selecting the mechanism (sales, marketing, sales leadership, RevOps). |

---

## The four principles

A signal mechanism reduces the asymmetry multiplier $(1 + \Delta_A)$ only when all four principles hold. If even one fails, the signal is debaseable, miscalibrated, misallocated, or unaccountable — and will not deliver durable friction reduction.

### Principle 1 — Friction must be non-automatable

**The principle.** A signal carries information only when its cost cannot be removed by efficiency tools. Production-cost friction is debaseable; expertise, relationship investment, and demonstrated work are not. This is the Single Crossing Property in plain language.

**Test.** What is the binding constraint on producing this signal?

| Binding constraint | Status |
|---|---|
| Production cost (time to draft, money to deploy, tooling) | **Debaseable** — once efficiency tools collapse production cost, signal collapses |
| Expertise (years of work, technical depth, scars) | Non-debaseable |
| Relationship capital (who vouches, who introduces) | Non-debaseable |
| Time and presence (in-person attendance, site visits) | Non-debaseable |
| Demonstrated work (named customers, audited outcomes, public IP) | Non-debaseable |

**Common violations.** "Best AI" marketing claims. AI-generated personalized cold emails. Vanity metrics chosen for novelty. Badges and certifications with no enforcement. Generic "thought leadership" content optimized for volume.

**Fix.** Replace debaseable production-cost effort with non-debaseable demonstration. If your outreach is built on tools that any competitor can also use, the signal is collapsing. Migrate to channels and artifacts where the cost is in the doing, not the producing.

---

### Principle 2 — Friction borne by the claimant

**The principle.** The party making the claim pays the cost of producing the signal. When the receiver bears the cost — filtering, evaluating, deciphering — the signal mechanism is broken regardless of how good any individual signal is.

**Test.** Walk through the actual transaction. Who pays each step?

| Mechanism | Who bears cost |
|---|---|
| Seller spends a week on a Blueprint the buyer reviews | Claimant |
| Seller sends 1,000 cold emails the buyer must filter | Receiver |
| Seller pays for SOC2 / security audit before approaching the buyer | Claimant |
| Platform sends notifications the buyer must triage | Receiver |
| Vendor commissions third-party validation prior to introducing themselves | Claimant |

**Common violations.** Cold outreach at scale. RFPs where the seller submits boilerplate and the buyer must read everyone's. "Reach out and we'll connect you with a specialist" lead-capture flows. Channels where the platform monetizes sends rather than signal quality.

**Fix.** Move the cost of signal evaluation to the producer. If your mechanism makes the receiver work harder to evaluate it, redesign so the producer does the work first and presents only the validated outcome.

---

### Principle 3 — Friction scales with stakes

**The principle.** The signal cost should match the size of the claim. A small claim requires modest signal; a large claim requires substantial signal. Mismatch fails in both directions — over-frictioned small claims feel disproportionate, under-frictioned large claims feel reckless.

**Test.** What is the financial / strategic / political stake of the buyer's decision, and what is the cost of the signal you're producing? Are they proportional?

| Stake | Signal cost | Verdict |
|---|---|---|
| $50K SaaS deal | 30-min discovery call | Proportional |
| $5M ERP deal | 30-min discovery call | Wildly under-frictioned |
| $50K SaaS deal | Three-month paid pilot | Over-frictioned |
| $5M ERP deal | Three-month paid pilot | Proportional |
| Buyer asks for pilot/POC at any stake | Anything less than implementation-led motion | Under-frictioned (override applies — see [Deal Triage Calculator](./deal-triage-calculator.md)) |

**Common violations.** A Structural deal sold with Turnkey-grade signals (under-frictioned). A Turnkey deal sold with Structural-grade signals (over-frictioned). Generic enterprise sales motion applied to a high-stakes deal without escalating the signal cost. Treating an enterprise buyer like a mid-market buyer because the territory categorization said so.

**Fix.** Match signal weight to stakes. The [Deal Triage Calculator](./deal-triage-calculator.md) returns a level and a direction. The signal's weight should scale to the level, and the component it targets should match the direction.

---

### Principle 4 — Adjudicators bear consequences of their validation

**The principle.** Parties that validate or filter signals — channels, platforms, ratings agencies, governance bodies — must lose something when they let bad signals through. Without this, the adjudicator drifts from gatekeeper to extractor.

**Test.** What does the adjudicator lose when their validation turns out wrong?

| Adjudicator type | Skin in the game? |
|---|---|
| Sales platform paid per email sent, regardless of reply rate | None |
| Ratings agency paid by vendors being rated | None (conflict of interest) |
| KLAS / Gartner / Forrester after rating a vendor that underperforms | Mild reputational loss; no direct cost — drift risk |
| Peer who personally recommended you, when the recommendation goes badly | Relationship cost — real |
| Platform that takes a percentage of post-sale value (success-fee) | Direct loss |
| Incumbent vendor whose channel access is revoked for bad delivery | Direct loss |

**Common violations.** Pay-per-send platforms. Volume-based ad networks. Ratings agencies funded by the rated. Reputation systems that don't depreciate (the KLAS "coast on residual brand" pattern). Internal review processes where reviewers face no consequences for approving bad deals.

**Fix.** Either (a) select adjudicators who already have skin in the game — peers, success-fee platforms, hostage-based access — or (b) introduce demurrage so reputation must be continuously re-earned and stale credibility loses weight. See [Constitution Axiom III: Reputation Depreciation](../theory/01-foundation/00-tcg-constitution.md).

---

## How to use this diagnostic

### Use case 1 — Designing a new artifact or process

When creating any new sales artifact, marketing asset, or process step, run the four principles as a checklist:

- [ ] **P1:** Is the cost non-automatable? What's the binding constraint on production?
- [ ] **P2:** Does the producer bear the cost, not the receiver?
- [ ] **P3:** Is the cost proportional to the stakes of the buyer's decision?
- [ ] **P4:** If there's an adjudicator (a platform, ratings agency, or internal reviewer), do they have skin tied to signal quality?

If any answer is no, redesign before launching.

### Use case 2 — Diagnosing a failing signal mechanism

When an artifact, channel, or campaign isn't producing the expected results (low reply rates, no $\Delta_A$ reduction, deals stalling), walk through the four principles to identify the failed one:

| Symptom | Likely violation |
|---|---|
| Channel reply rates collapsing across the board | **P1** — production cost was the binding constraint, now collapsed (Jevons). |
| Individual outreach gets ignored despite quality effort | **P1** collapse + **P2** misallocation (receiver overwhelmed by aggregate volume). |
| Deal feels under-resourced for its size; buyer keeps asking for "more proof" | **P3** — friction below stakes; signals don't feel substantial enough. |
| Buyer references a rating or certification that turned out to be misleading | **P4** — adjudicator drift; the signal source has lost reliability. |
| Champion is enthusiastic but the deal still stalls in procurement | Often **P3** — signals strong enough for the champion don't scale to the broader committee. |
| Deal closes but churns within 90 days | **P3** + **P4** — implementation signal was under-weighted, and the adjudicator (rep's manager forecasting it) had no skin in the post-sale outcome. |

### Use case 3 — Evaluating a channel or platform before commitment

Before investing time in a new outreach channel, platform, or third-party validator, score it against the principles. A channel that fails one or more principles will not produce durable signal — investing there is donating attention to a structure that will drift toward extraction.

Specifically for channel selection, **P1** is the load-bearing test:

- If the binding constraint on volume in this channel is production cost → Jevons-vulnerable, will collapse.
- If the binding constraint is something else (time, relationships, expertise, demonstrated work) → Jevons-resistant.

---

## Why these are the only four

The principles look like a list, but they cover the necessary and sufficient conditions for a signal to carry information:

| Principle | Question it answers |
|---|---|
| 1 (non-automatable) | *Does* it carry information? |
| 2 (claimant pays) | Is the cost on the right party? |
| 3 (scales with stakes) | Is the cost calibrated to the claim? |
| 4 (adjudicator skin) | Does the validation mechanism stay honest over time? |

If all four hold, $\Delta_A$ shrinks. If any one fails, it doesn't — regardless of how well the others hold. They are conditions, not optimizations.

---

## Related

- **Theory:** [TCG Constitution — Axiom II (Law of Uncertainty Inflation) and the Friction Allocation Principles](../theory/01-foundation/00-tcg-constitution.md).
- **Channel evaluation:** [channel-collapse.md](../theory/02-research/channel-collapse.md) describes when production cost is the binding constraint, making the channel vulnerable to Principle 1 failure.
- **Adjudicator design:** [Constitution Axiom III — Reputation Depreciation](../theory/01-foundation/00-tcg-constitution.md) describes how to design demurrage into adjudicator structures.
- **Deal-level scoring:** [Deal Triage Calculator](./deal-triage-calculator.md) — Principle 3 (scales with stakes) is operationalized by classifying deals first.
