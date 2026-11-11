---
title: "Friction Allocation Diagnostic"
layer: practice
status: active
version: 2.0
operationalizes: [axiom-1, axiom-2]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# Friction Allocation Diagnostic

Version: 2.0
Goal: Decide whether one piece of evidence counts as verification, meaning a buyer can rely on it to lower what it cannot check. Evidence that fails is a claim, however much it cost to produce.

**Canonical reference:** [Constitution 7.0](../theory/01-foundation/00-tcg-constitution.md), claim 3: a signal informs only when it costs a weak seller more than a strong one. The diagnostic tests whether a piece of the seller's spending gives the buyer evidence it can check, which is what claim 8 asks of it. It does not test spending that lowers the cost at Time2, so a discovery workshop can fail here and still earn its cost under claim 9. Why each of the four principles is needed is argued in [costly-signals.md](../theory/02-research/costly-signals.md).

| | |
|---|---|
| **Inputs** | One signal and the claim it supports. A signal is a piece of evidence, an artifact, a channel or a third-party validator. |
| **Outputs** | Pass, or every principle it fails, each with its fix. |
| **When to run** | On the evidence for each Test row of the [Enforcement Ledger](./enforcement-ledger.md), on each evidence cell of the [Market Reading](./00-market-reading.md)'s search ledger, and on any artifact, channel or validator before the seller spends on it. |
| **Grader** | Someone other than whoever produced the signal. In the Enforcement Ledger, the buyer's skeptic. In the search ledger, the buyers who have not met the seller. |

---

## What a failure means

A signal too cheap to separate a strong seller from a weak one is *cheap talk*: anyone can send it, so it says nothing about who sent it. Cheap talk still informs as far as the two sides' interests already agree (Crawford and Sobel 1982), so a failure matters where they diverge: whether the product fits here, whether the seller will deliver, and what the change will cost to run.

**Where a failure lands.** In Test, evidence that fails leaves the row without the skeptic's verdict, so the row stays open on the buyer's side. In the search ledger, the cell is marked as a claim. For [open question 45](../theory/01-foundation/07-open-questions.md)'s cost-of-sale tagging, a pass would tag the activity as verification and a failure as persuasion, unless the activity lowered the cost at Time2.

**Signals screen before signature and are re-earned after it.** A deal that closed on evidence that was sound and current, and then failed, is a failure after signature, read against the Enforcement Ledger's staged plan in the [Sustaining Adoption Review](./adoption-review.md).

---

## The four tests

Run all four and record every failure. Fix them in this order, because a signal that fails test 1 says nothing however the others come out.

**Whose signal it is.** Where the seller produced the evidence, the seller is the claimant. Where a third party produced it, such as an analyst ranking, a review site or a certification, the third party is the claimant for tests 1 to 3 and the adjudicator for test 4.

### 1. The cost cannot be automated away

**Ask:** what limits how much of this the claimant can produce?

| What limits it | Result |
|---|---|
| Production cost: drafting time, sends, tooling | **Fails.** Competitors' tools remove the cost, weak sellers copy the signal, and the category *pools*, meaning buyers can no longer tell sellers apart and judge them all by the average. |
| Expertise shown on the buyer's own problem | Passes |
| A relationship someone stakes, such as a named reference | Passes |
| Time and presence, such as a site visit | Passes |
| Demonstrated work: outcomes someone outside the seller audited, work in the buyer's environment | Passes |

**Fix:** move the cost into the doing.

### 2. The claimant bears the cost

**Ask:** walk through the exchange step by step. Who pays for each one?

**It fails** when the receiver pays: filtering volume, reading boilerplate, or evaluating a claim it has no means to check. Cold outreach at scale and boilerplate answers to a request for proposal fail here.

**Fix:** the claimant does the work first and hands the buyer only a result it can check, such as a security audit commissioned before the first meeting or a gap analysis of the buyer's own workflow.

### 3. The cost scales with the claim

**Ask two questions.** What does the buyer sink if the claim is wrong? And would a weak seller gain more by faking this evidence than it would cost to fake? The more the buyer pays and sinks on a claim, the more a weak seller gains by being taken for a strong one, so the evidence has to cost a weak seller more as the stake grows.

**Read the stake from what the caller already has.** For a Test row, the row's own touchpoint and the workflows it changes. For a search-ledger cell, whether the Market Reading reads the purchase as plug-in, working on arrival, or built-in.

**It fails** when a claim the buyer will sink *specific investment* on, meaning spending worth little outside this relationship, rests on evidence a weak seller could match cheaply.

**Fix:** a demonstration in the buyer's environment, evidence the skeptic grades in Test, or a guarantee. A guarantee is partly verification, because only a seller confident of delivering can afford to offer one.

**The opposite mistake is waste.** Where the triage reads the purchase as plug-in, meaning the buyer can measure fit itself and walk away, a trial is the signal. A paid pilot there is the over-built failure under claim 6, and it usually fails test 2 as well.

**What signals cannot do.** Aim signals at the search cost, the implementation cost, and each decision role's uncertainty about what the change does to its own measure. Where roles want opposed things, proof cannot reconcile them, and the [Bargaining Ledger](./bargaining-ledger.md) answers with terms instead.

### 4. The adjudicator loses when a bad signal passes

**Ask:** who vouches for or filters this signal, and what do they lose if it proves wrong? Where the buyer checks the evidence directly, with nobody between, the test passes.

| What the adjudicator loses | Result | Example |
|---|---|---|
| Nothing | **Fails** | A ratings firm or certifier paid by the vendors it rates. A channel paid on referral. A sponsor staked on success judging between the buyer's own roles ([open question 59](../theory/01-foundation/07-open-questions.md)). A seller's manager forecasting a built-in deal with no stake in what happens after signature. |
| Reputation only | **Passes while re-earned.** Standing that is not refreshed with evidence of continued delivery depreciates, so weight the signal by how recently it was earned. | An analyst ranking. A review site. |
| Something direct | Passes | A peer whose relationship rides on the recommendation. A channel paid on a share of what survives signature (claim 3 of the Constitution). |

**Prefer an adjudicator that discloses a grade over one that reports pass or fail.** A certifier does best by revealing only whether quality clears a minimum, so even an honest one tells the buyer less than it knows ([information-environment.md](../theory/02-research/information-environment.md)).

---

## Reading a failing signal

| Symptom | Test that failed |
|---|---|
| Reply rates fall across a whole channel | 1. Production cost was the limit, and tools removed it ([channel-collapse.md](../theory/02-research/channel-collapse.md)). |
| Careful individual work gets ignored | 2, usually with 1. The receiver pays to sort the volume everyone else sends. |
| The buyer keeps asking for more proof | 3. The evidence is cheap beside what the buyer will sink. |
| The champion is convinced and procurement or security is not | 3 if the approvers the exposure adds need different evidence. If they want back something the change takes from them, no signal answers it, and the Bargaining Ledger does. |
| The buyer balks at a pilot for a product it could try alone | 3, the waste direction. |
| A rating or certification the buyer relied on proved wrong | 4. |

---

## Related

- [00-tcg-constitution.md](../theory/01-foundation/00-tcg-constitution.md), claims 3 and 8.
- [costly-signals.md](../theory/02-research/costly-signals.md), for why each principle is needed, and the trust-proxy extension that is the standing candidate for a fifth.
