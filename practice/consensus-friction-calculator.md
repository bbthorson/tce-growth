---
title: "Consensus Friction Calculator"
layer: practice
kind: instrument
status: active
operationalizes: [axiom-1]
canonical_source: theory/canon/constitution.md
---

# Consensus Friction Calculator

**Purpose:** To estimate how much organizational friction a buying committee will generate, and to decide whether the deal needs a stakeholder map, a joint steering committee, or executive sponsorship.

**Use when:** The [Deal Triage Calculator](./deal-triage-calculator.md) reads the deal as consensus-dominant, or the Blueprint has identified the buying committee and you need to size $F_{consensus}$ before forecasting a close date.

> [!IMPORTANT]
> **This is the consensus component's only dedicated instrument, and one instrument is not a set.** Consensus-dominant is a routing destination in its own right, and a deal arriving here finds a calculator that produces a number and then prescribes executive sponsorship, which is a tactic rather than a motion. Qualification frameworks built around economic buyer access, written decision criteria, documented decision process, and champion development are the incumbent practice for this component, and this repository does not carry them. Reach for those and say on the forecast call that you are working outside the framework, rather than substituting the implementation chain because it is the one that exists.

**Operationalizes:** Axiom III's $F_{consensus}$ term. Theory in [models.md](../theory/reference/models.md) Section 3, research in [buying-center-dynamics.md](../theory/evidence/buying-center-dynamics.md).

---

## The premise

A firm is not a single decision maker. It is a coalition whose members evaluate the same proposal against different objectives. Two things drive the cost of aligning them, and they compound rather than add:

- **Size.** Communication channels grow as $N(N-1)/2$, so the sixth stakeholder costs more than the second.
- **Goal conflict.** A large committee that agrees moves faster than a small one that does not.

---

## Inputs

### 1. Committee size ($N$)

Count every stakeholder holding veto power or direct evaluation responsibility, across executive, technical, legal, financial, and operational functions. Title does not matter. Veto power does.

Count the person who can stop the deal even if they never attend a meeting. Security architects and data protection officers are the ones most often missed.

### 2. Incentive variance (Var)

Score each stakeholder $i$ from $-1$ to $+1$ on how the initiative affects the objectives they are measured on:

- **+1** — advances their measured objectives directly
- **0** — no material effect
- **−1** — conflicts with their objectives or removes operational control

> [!IMPORTANT]
> **Score what they are measured on, never what they said in the room.** A stakeholder's stated position is shaped by who else is present. Stated positions converge under social pressure and measured objectives do not, so scoring from the meeting produces a variance that is too low, and it is worst in exactly the polarized committees this term exists to catch. Find the scorecard before you score the person: what number is on their review, and does this initiative move it up or down.
>
> A committee where every stakeholder reports alignment is not evidence of low variance. It is equally consistent with variance nobody has said aloud yet, which is the normal state before a late-stage veto. When you cannot find a single stakeholder who loses something, assume you have not yet met them and score 0.25 rather than 0.

Then compute the variance across the committee:

$$\bar{I} = \frac{1}{N}\sum_{i=1}^{N} I_i \qquad \text{Var} = \frac{1}{N}\sum_{i=1}^{N}(I_i - \bar{I})^2$$

Variance is bounded on $[0, 1]$ because the scores are bounded on $[-1, 1]$. If you calculate a value above 1, you have made an arithmetic error.

When you lack the detail to score each person, use the rubric:

| Estimate | Condition |
|---|---|
| **0.0** | Every stakeholder benefits and knows it. |
| **0.25** | Minor divergence in priority. Security wants rigor, operations wants speed, nobody is threatened. |
| **0.50** | Two camps with genuinely opposed positions. At least one stakeholder loses something real. |
| **1.00** | Polarized. Some stakeholders gain substantially and others are actively harmed. |

### 3. Technical overlap ($TO$)

Architectural alignment among the technical evaluators, scored 1 to 5. This is tracked separately from incentive variance because technical philosophy conflicts persist even when incentives align. Two architects can both want the project to succeed and still deadlock on hosting model.

This is the one ordinal rating left in the field instruments, and it survives on a technicality: it enters as $\gamma_{TO} \cdot TO$, which is linear, so nothing exponentiates it. Read it as a rank rather than a quantity, and do not carry it into any model that squares its inputs.

| Score | Condition |
|---|---|
| **1** | Unified standards and shared infrastructure principles. |
| **3** | Disagreement on integration patterns or hosting model. |
| **5** | Fractured philosophy. Cloud-native versus strict on-premise governance, or an unresolved build-versus-buy faction. |

---

## The calculation

$$F_{consensus} = \alpha \cdot N^{\beta} \cdot (1 + \text{Var}) \cdot (1 + \gamma \cdot TO)$$

With calibration defaults $\alpha = 1.0$, $\beta = 1.35$, $\gamma = 0.20$.

**Worked example.** A committee of 5, with two camps in genuine conflict (Var = 0.25) and disagreement on integration patterns (TO = 3):

$$F_{consensus} = 1.0 \times 5^{1.35} \times 1.25 \times 1.6 = 8.78 \times 1.25 \times 1.6 = 17.6$$

That lands in the medium band, which calls for a stakeholder alignment matrix and shared evaluation criteria before the deal is forecast.

> [!NOTE]
> These parameter values are reasoned defaults, not estimates fitted to booked deals. The output ranks deals against each other reliably. It does not predict a cycle length in weeks. See [models.md](../theory/reference/models.md) Section 6.

---

## Risk bands

| $F_{consensus}$ | Classification | What happens | Intervention |
|---|---|---|---|
| **Under 10** | Low | Linear decision path. Low stall risk. | Single-champion navigation. Standard approval workflow. |
| **10 to 25** | Medium | Delays from inter-departmental alignment cycles. The deal does not die, it drifts. | Deploy a stakeholder alignment matrix. Establish a joint steering committee and write down shared evaluation criteria before pricing. |
| **Above 25** | High | Evaluation deadlock or silent death. The most likely outcome is No Decision, not a competitive loss. | Executive sponsorship required. Run a joint Red Team workshop to force explicit trade-off resolution before the MIP is drafted. |

---

## Reading the output

**The single highest-leverage move is reducing variance, not reducing headcount.** The sensitivity of friction to variance scales with $N^{\beta}$:

$$\frac{\partial F_{consensus}}{\partial \text{Var}} = \alpha N^{\beta}$$

In a committee of three, aligning incentives produces a modest gain. In a committee of ten, it produces the largest single reduction available to the seller. This is the quantitative case for running the Red Team on large committees specifically.

**Do not respond to a high score by scheduling more meetings.** More meetings raise the coordination cost without touching the variance that generates it. The interventions that work force explicit trade-offs into the open, which is what the Red Team's prospective hindsight exercise does.

**A stakeholder scoring $-1$ is not irrational.** They are optimizing a scorecard the seller has not read. Name them in the Blueprint as the casualty, and build the containment plan. A committee where nobody scores below zero usually means the seller has not found the casualty yet, not that no casualty exists.

---

## Related

- [buying-center-dynamics.md](../theory/evidence/buying-center-dynamics.md) — Cyert-March and Webster-Wind. Why the coalition behaves this way.
- [models.md](../theory/reference/models.md) — Derivation and sensitivity analysis.
- [Contextual Blueprint](./implementation-motion/01-discovery-contextual-blueprint.md) — Where the committee gets mapped.
- [Red Team Protocol](./implementation-motion/02-validation-red-team-protocol.md) — The variance-reduction instrument.
- [Deal Triage Calculator](./deal-triage-calculator.md) — Counts the veto holders and the share of them with a documented measured objective, which is this component's gap.
- [Bilateral Asymmetry Scorecard](./asymmetry-scorecard.md) — The companion measure for $\Delta_A$.
