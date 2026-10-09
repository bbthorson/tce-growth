---
title: "Milestone Valuation Model"
layer: practice
status: active
operationalizes: [axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# Milestone Valuation Model

**Purpose:** To design MIP phase gates so that each one resolves a defined tranche of uncertainty, and to structure payments so the buyer never carries more committed cost than the stage has de-risked.

**Use when:** The Red Team has surfaced the failure modes and you are drafting the MIP's timeline and commercial terms.

**Operationalizes:** Staged Commitment, an Axiom III corollary. Theory in the [Constitution](../theory/01-foundation/00-tcg-constitution.md), research in [real-options.md](../theory/02-research/real-options.md).

---

## The premise

A buyer who accepts the business case and still declines is usually not stalling. They are pricing the option to wait, and pricing it correctly.

When an investment is irreversible and the environment is uncertain, the ability to defer carries real economic value. Demanding full commitment at signature asks the buyer to destroy that entire option in one step, which they will often refuse to do even when expected return is positive. Staging does not reduce the work. It reduces how much of the work must be committed before the buyer knows whether it will succeed.

This model is what separates a phased *project plan* from a phased *commitment*. A project plan with four phases and one signature preserves no option value. The buyer must be able to stop.

---

## The stage equation

For each stage $m$, the buyer's expected surplus is:

$$S_m = (1 - \pi_m)\left(V_{gross,m} - c_m\right) - \pi_m \, Q_m$$

| Term | Meaning |
|---|---|
| $V_{gross,m}$ | Incremental value the buyer realizes on completing stage $m$ |
| $c_m$ | Payment allocated to stage $m$, paid only when the stage's acceptance criteria are met |
| $Q_m$ | What the buyer sinks at stage $m$ that it cannot recover if the stage fails: adaptation, staff time, anything non-refundable |
| $\pi_m$ | The chance stage $m$ fails, from the residual uncertainty entering it: $\pi_m = \pi_0 + (1 - \pi_0)\,x_m$ |
| $x_m$ | Residual uncertainty **entering** stage $m$, normalized to $[0, 1]$ |

This is the Constitution's future loss, $L = Q \cdot \pi$, read one gate at a time. [02-mathematical-models.md](../theory/01-foundation/02-mathematical-models.md) sections 5.2 and 5.4 carry the forms, and the straight line from the floor $\pi_0$ is a placeholder declared as chosen. Your own delivery history in comparable environments is evidence that should lower $x_m$ and the floor, and it enters there rather than as a separate probability.

> [!IMPORTANT]
> **Every term is a fraction of annual contract value.** $V_{gross,m}$, $c_m$ and $Q_m$ share one scale, because the equation subtracts them from each other. Write payments as 0.25, never as 25. [02-mathematical-models.md](../theory/01-foundation/02-mathematical-models.md) section 1.2 carries the units.

**The payment sits inside the success term because rule 2 puts it there.** A payment that follows proof is only made when the stage succeeds. A payment triggered by the calendar is made either way, and the stage surplus falls to $(1 - \pi_m)V_{gross,m} - c_m - \pi_m Q_m$. The difference, $\pi_m c_m$, is what the buyer pays for the seller's delivery risk, and it is largest at the first gate.

Uncertainty decays as gates clear, with each stage resolving a fraction of what remains:

$$x_m = x_0 \cdot \prod_{k=1}^{m}(1 - \mu_k)$$

Where $x_0$ is the normalized implementation gap from the [Bilateral Asymmetry Scorecard](./asymmetry-scorecard.md) and $\mu_k$ is the fraction of remaining uncertainty that stage $k$ resolves. The gates resolve implementation uncertainty specifically, so the scorecard's gap is the right input.

---

## The three design rules

**1. Low commitment before validation.** Capital committed before technical validation is limited to baseline setup. The buyer must be able to exit the Blueprint stage having spent an amount they would not need to defend internally.

**2. Payment follows proof, not calendar.** Transfers trigger on mutual sign-off against written acceptance criteria, never on elapsed time. A date-triggered payment converts a real option back into an unconditional commitment, which defeats the entire structure.

**3. Symmetric consequence.** If a stage fails on seller execution, unused fees are credited or refunded and the seller supplies remediation engineering without additional billing. Without this, the gate is a checkpoint the buyer cannot act on, and it carries no option value at all.

Rule 3 is the one most often dropped in negotiation, and dropping it removes the mechanism. A gate the buyer cannot walk away from is a milestone, not an option.

---

## Reference stage structure

Payments are fractions of annual contract value. Adjust the count and the decay profile to the deal. The shape is what matters.

| Stage | Acceptance criteria | Entering $x_m$ | Resolved $\mu_m$ | Exiting | Payment $c_m$ | Risk-sharing term |
|---|---|---|---|---|---|---|
| **0. Blueprint** | Architecture audit and data schema mapping complete and signed. | $x_0$ | 0.25 | $x_1$ | Discovery fee only | Fully refundable if the audit finds the architecture unworkable. No license commitment. |
| **1. Core integration** | API throughput and security protocols verified in sandbox against written benchmarks. | $x_1$ | 0.50 | $x_2$ | 0.25 | Contingent on meeting the stated throughput and security benchmarks. |
| **2. Pilot** | A defined user group operating on live production workflows. | $x_2$ | 0.80 | $x_3$ | 0.35 | Service level guarantees on stability and latency, with credit clawback. |
| **3. Full rollout** | Enterprise deployment and system sign-off. | $x_3$ | Remaining | approaching 0 | 0.40 | Standard recurring license and maintenance terms begin. |

Where $x_1 = 0.75\,x_0$, $x_2 = 0.375\,x_0$ and $x_3 = 0.075\,x_0$.

Each $\mu_m$ applies to what remains rather than to the original gap, which is why the residual compounds downward rather than stepping linearly.

**Entering and exiting are different columns, and the equation takes the entering one.** A single residual column reads as the value after that row's gate cleared, which is the next row's input rather than its own. The two are separated here because the arithmetic below turns on which one is substituted.

### Where the specific investment belongs

At a fully open gap ($x_0 = 1$), with an illustrative floor of $\pi_0 = 0.05$ and the buyer sinking 0.85 of a year's contract value in total:

| Stage | Entering $x_m$ | $\pi_m$ | Sunk $Q_m$ | Expected loss $\pi_m Q_m$ |
|---|---|---|---|---|
| 1. Core integration | 0.750 | 0.763 | 0.10 | 0.076 |
| 2. Pilot | 0.375 | 0.406 | 0.25 | 0.102 |
| 3. Full rollout | 0.075 | 0.121 | 0.50 | 0.061 |
| **Total** | | | **0.85** | **0.238** |

**This table is the argument.** The same 0.85 sunk all at signature, against the full gap, is an expected loss of 0.85. Staged with the small commitments early and the large one late, it is 0.24, under a third. Run the same three stages in the wrong order, with 0.50 sunk at core integration and 0.10 at rollout, and the loss is 0.49: staging helps, and the order of the commitments decides how much. The right to stop is worth most when least is known, which is why the small, refundable commitments belong early and why a single signature at the top destroys the option the buyer is actually protecting.

The same profile prices payment timing. At the first gate a payment made before proof costs the buyer $\pi_1 c_1 = 0.763 \times 0.25 = 0.19$ of a year's contract value in expected terms. At the last gate the same rule costs $\pi_3 c_3 = 0.121 \times 0.40 = 0.05$. Payment following proof matters most exactly where sellers most want cash up front.

The floor and the sunk amounts are illustrative and [06-calibration.md](../theory/01-foundation/06-calibration.md) records them as chosen. The shape is the argument and the values are not.

---

## How to use it in a negotiation

**Work backwards from the buyer's exit point.** Ask which stage they would need to be able to stop at for the first signature to feel survivable. That stage is where the largest refundable component belongs.

**Quantify what the buyer gives up.** The buyer holds the option today. Naming its value, and then showing that the staged structure returns most of it, is a stronger argument than any return projection. Buyers who resist discounting will accept staging, because staging costs the seller cash flow timing rather than margin.

**Check that payment never leads proof.** Walk the table left to right. At every row, committed payment to date should sit below value realized to date. If a row breaks that rule, the buyer is financing the seller's delivery risk, and they will find it during legal review.

**Do not stage a deal that sinks nothing specific.** Gate design carries real administrative cost on both sides. Where the buyer can trial and walk away, $Q_m$ is near zero at every gate, the expected loss staging reduces is near zero too, and the structure destroys more surplus than it preserves. Confirm the exposure reading with the [Deal Triage Calculator](./deal-triage-calculator.md) first.

**Quote the payment schedule in one unit and say which.** A schedule written as "25 / 35 / 40" reads as percent to a buyer and as contract values to this model. Legal review will read it the first way and the model was computed the second way. Write fractions in the model and percentages in the contract, and never carry a number from one into the other without converting it.

---

## Failure modes

- **Phases without exits.** Four stages, one signature, no ability to stop. Preserves no option value and produces the same resistance as a single commitment.
- **Calendar gates.** Payment triggered by date rather than acceptance. Reintroduces unconditional commitment.
- **Asymmetric consequence.** The buyer is bound at each gate and the seller is not. The buyer's counsel will find this, and it damages more trust than the staging built.
- **Vanity criteria.** Acceptance conditions written so loosely that no outcome fails them. A gate that cannot fail resolves no uncertainty, so $\mu_m$ is effectively zero regardless of what the plan claims.
- **Mixed units.** A payment entered as 25 rather than 0.25 swamps every other term, and the model then reads as though value and exposure did not matter. This is not a rounding difference. It reverses the conclusion.
- **Large commitments early.** A schedule that front-loads the buyer's adaptation sinks the most against the widest gap. The stages exist, and they protect almost nothing.

---

## Related

- [real-options.md](../theory/02-research/real-options.md) — Dixit-Pindyck. Why waiting has value and staging recovers it.
- [00-tcg-constitution.md](../theory/01-foundation/00-tcg-constitution.md) — Staged Commitment, an Axiom III corollary.
- [Mutual Implementation Plan](./implementation-motion/03-closing-mutual-implementation-plan.md) — The artifact these gates go into.
- [Bilateral Asymmetry Scorecard](./asymmetry-scorecard.md) — Supplies $x_0$.
