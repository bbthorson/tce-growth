---
title: "Mathematical Models"
layer: theory
status: active
version: 1.0
operationalizes: [axiom-1, axiom-2, axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# Mathematical Models

**Version:** 1.0
**Purpose:** To specify the functional forms behind the variables the [Constitution](./00-tcg-constitution.md) names but does not compute.

The Constitution is axioms-first. It states that effective transaction cost rises with the bilateral asymmetry gap, that the bargaining cost rises with committee size, and that urgency decays from a triggering event. It does not say *by how much*, or *as a function of what*. This file supplies those functional forms.

Nothing here introduces new claims. Every model traces to a term the Constitution already defines. If a model here cannot be traced to an axiom, it does not belong in this file either.

> [!IMPORTANT]
> **Calibration status.** The functional forms below are specified, not fitted. Parameter defaults are reasoned starting values, not empirical estimates from booked deal data. Section 6 marks which parameters carry literature support and which are placeholders. Use these models to structure judgment, not to forecast.

---

## 1. The Two Representations of Transaction Cost

Axiom III carries two equations for the same quantity. The Constitution presents both and asserts they are representations of one thing. This section shows why that assertion holds.

### 1.1 The structural form

$$F_{effective} = \sum_{k} F_k \cdot (1 + \hat{\Delta}_k), \qquad k \in \{search,\; consensus,\; implementation\}$$

This form decomposes cost into three components that arise from distinct conditions and respond to distinct interventions, and amplifies each by the asymmetry inside its own pair of parties. Its value is diagnostic. When a deal stalls, this form tells you which component is binding and therefore which artifact to deploy.

**The single-multiplier form is what this factors into.** Collecting the sum:

$$\sum_{k} F_k (1 + \hat{\Delta}_k) = F_{base} \cdot (1 + \hat{\Delta}_A), \qquad \hat{\Delta}_A \equiv \frac{\sum_{k} F_k \hat{\Delta}_k}{\sum_{k} F_k}$$

The identity is exact. The deal-level gap $\hat{\Delta}_A$ is the friction-weighted mean of the three component gaps, which is what lets the reduced form below run on a single scalar. Section 2 gives the three gaps and their instruments. What the scalar cannot represent is stated in section 1.4.

### 1.2 The reduced form

$$y = a \hat{\Delta}_A^2 + c$$

This form collapses the decomposition into a single convex curve. Its value is argumentative. It shows why the traditional levers fail: because cost grows faster than linearly in uncertainty, cutting the constant term $c$ through discounting cannot offset a large $\Delta_A$.

### 1.3 The derivation connecting them

The structural form leaves one assumption implicit: that base friction is independent of the asymmetry gap. It is not.

An uncertain buyer does not simply pay a surcharge on a fixed quantity of work. The uncertainty changes how much work exists. A buyer who cannot verify the seller's claims adds stakeholders to the evaluation, adds security review cycles, adds proof-of-concept stages, and widens scope to cover contingencies they cannot rule out. Each addition raises $F_{consensus}$ and $F_{implementation}$ directly, before any multiplier applies.

Write base friction as a function of the gap:

$$F_{base}(\hat{\Delta}_A) = c + b \hat{\Delta}_A$$

Where $c$ is the irreducible floor (license fees, direct outlays, the deployment work that happens even under perfect information) and $b$ is the rate at which base friction grows per unit of asymmetry.

Substituting into the structural form:

$$F_{effective} = (c + b\hat{\Delta}_A)(1 + \hat{\Delta}_A) = b\hat{\Delta}_A^2 + (b + c)\hat{\Delta}_A + c$$

The reduced form is this expression with the middle term dropped and $a$ identified with $b$. The derivation runs on the factored scalar, so it is untouched by the split into three gaps. The two representations describe the same cost. The reduced form is the structural form after you let base friction depend on asymmetry and then discard the linear term.

### 1.4 What the reduced form gives up

Two things. It drops the linear term $(b + c)\hat{\Delta}_A$, which is not small over the operating range, so the reduced form is a two-parameter approximation of a three-parameter expression and a fitted $a$ and $c$ would absorb the discarded term. And it drops the component decomposition, and with it the direction that selects the motion, so it produces a number rather than a diagnosis. What survives is convexity, which is the one property the three-levers argument needs.

**Operating rule.** Diagnose a deal with the structural form. Explain why discounting fails with the reduced form. Never choose an intervention from the reduced form.

### 1.5 Normalizing the gap before substitution

The [Bilateral Asymmetry Scorecard](../../practice/asymmetry-scorecard.md) produces a raw score on $[2, 10]$. Neither equation accepts that range directly. At a raw score of 10 the structural multiplier $(1 + \Delta_A)$ would inflate base friction elevenfold, which no observed deal supports.

Normalize before substituting:

$$\hat{\Delta}_A = \frac{\Delta_A^{raw} - 2}{8}, \qquad \hat{\Delta}_A \in [0, 1]$$

This keeps the structural multiplier in $[1, 2]$ and keeps the reduced form's quadratic term bounded by $a$. Use the raw score for the field triage bands in the scorecard. Use the normalized value in either equation. Confusing the two produces cost estimates off by an order of magnitude.

**Each component gap normalizes on its own instrument's range.** The scorecard's $[2, 10]$ is the enforcement pair's range, because that is the pair it measures. The search and bargaining gaps are emitted directly on $[0, 1]$ by the [Deal Triage Calculator](../../practice/deal-triage-calculator.md) as evidenced fractions, so they need no rescaling. Section 2.4 gives all three.

The normalized gap may exceed 1 when asymmetry rebuilds past the instrument's ceiling under the Decay Clock dynamics ($\hat{\Delta}_A(t) = \hat{\Delta}_A(0) + \gamma t$). The scorecard measures a point in time and cannot observe drift beyond its own range.

### 1.6 A note on the coefficient $a$

The derivation identifies $a$ with $b$, the rate at which base friction grows per unit of asymmetry, not with the loss aversion coefficient $\lambda$. The anchor $a \approx 2.25$ borrows $\lambda$'s magnitude as a reason $b$ should be large: buyers add review cycles and contingency scope because they weight losses roughly twice as heavily as gains. That supports the order of magnitude and is not a measurement. [06-calibration.md](./06-calibration.md) records how far the analogy stretches.

### 1.7 The scale of $y$, $c$ and $a$

The reduced form adds $a\hat{\Delta}_A^2$ to $c$, so $a$ carries $c$'s units. **All three are fractions of annual contract value.** A deal at list price with no internal cost has $c = 1$, and the [Milestone Valuation Model](../../practice/milestone-valuation-model.md) is where $a$, $c$ and the payment schedule meet on that scale.

| Stage | Payment $c_m$ | Residual entering, $x_m$ | $a x_m^2$ | Ratio to that stage's payment |
|---|---|---|---|---|
| 1. Core integration | 0.25 | 0.750 | 1.266 | 5.06 |
| 2. Pilot | 0.35 | 0.375 | 0.316 | 0.90 |
| 3. Full rollout | 0.40 | 0.075 | 0.0127 | 0.032 |

Computed at $x_0 = 1$. Entering the deal, the uncertainty the buyer is asked to carry is worth five times the first payment. By the last gate it is three percent of it. That profile is the staging argument, and it is why gate design should return most of the option value early.

Read the same table in percentage points and the uncertainty term becomes a rounding error at every stage, which inverts the framework's central claim. The percentage reading is a unit error, not a second option. Stating the units makes $a$ wrong in a checkable way: a fitted value would come back in annual contract values per unit of squared normalized gap, and section 6 says what data that needs.

---

## 2. The Bilateral Asymmetry Gap

### 2.1 Definition

$$\Delta_A = I_{seller} + I_{buyer}$$

The gap is a **sum**, not a difference. Total informational misalignment across the buyer-seller boundary is the seller's ignorance of the buyer's environment plus the buyer's uncertainty about the seller's capability. A deal where both sides are equally blind is not symmetric in any useful sense. It is maximally uninformed on both sides, and $\Delta_A$ must reflect that.

$\Delta_A = 0$ represents complete informational symmetry.

**This is the enforcement component's gap, the implementation gap in field terms, not the deal's.** Sections 2.2 and 2.3 model its two halves. Section 2.4 gives the other two components' gaps, which have different parties and different instruments, and section 1.1 gives the weighted mean that recovers the deal-level scalar from all three.

### 2.2 Seller Ignorance

Seller Ignorance measures what the seller has not yet mapped about the buyer's architecture and operations:

$$I_{seller} = w_t \cdot U_{tech}^{\phi_t} + w_p \cdot U_{process}^{\phi_p}$$

| Symbol | Meaning | Range | Default |
|---|---|---|---|
| $U_{tech}$ | Unmapped technical complexity (legacy systems, custom APIs, security controls) | $[0, 10]$ | measured |
| $U_{process}$ | Unmapped operational variance (undocumented workflows, cross-department edge cases) | $[0, 10]$ | measured |
| $w_t, w_p$ | Weights, with $w_t + w_p = 1$ | $(0, 1)$ | 0.6, 0.4 |
| $\phi_t, \phi_p$ | Risk acceleration exponents | $\ge 1$ | 1.2, 1.1 |

**Properties.** The function increases in both inputs:

$$\frac{\partial I_{seller}}{\partial U_{tech}} = w_t \phi_t U_{tech}^{\phi_t - 1} > 0$$

Because $\phi_t, \phi_p \ge 1$, the second derivative is non-negative. Unmapped technical complexity generates accelerating discovery risk rather than proportional discovery risk. The Blueprint targets this term.

### 2.3 Buyer Uncertainty

Buyer Uncertainty measures doubt about return variance and vendor capability:

$$I_{buyer} = \mu \cdot \frac{\sigma_{ROI}}{\bar{R}} + \nu \cdot e^{-\kappa K_{vendor}}$$

| Symbol | Meaning | Range | Default |
|---|---|---|---|
| $\sigma_{ROI} / \bar{R}$ | Coefficient of variation of projected return | $\ge 0$ | measured |
| $K_{vendor}$ | Demonstrated vendor proof (blueprints, reference architectures, validated benchmarks) | $[0, 10]$ | measured |
| $\mu$ | Sensitivity to return uncertainty | $> 0$ | 1.0 |
| $\nu$ | Baseline doubt for an unvalidated vendor | $> 0$ | 2.0 |
| $\kappa$ | Decay of doubt per unit of proof | $> 0$ | 0.5 |

**Properties.** Proof reduces doubt with diminishing returns:

$$\frac{\partial I_{buyer}}{\partial K_{vendor}} = -\nu \kappa e^{-\kappa K_{vendor}} < 0$$

As proof accumulates, buyer uncertainty approaches a floor set by return variance alone:

$$\lim_{K_{vendor} \to \infty} I_{buyer} = \mu \cdot \frac{\sigma_{ROI}}{\bar{R}}$$

This floor is the model's most useful field implication. No quantity of costly signaling drives buyer uncertainty to zero while the return itself remains volatile. Past a point, the seller stops investing in proof and starts working on the variance of the projected return. The Red Team targets $K_{vendor}$. The MIP targets $\sigma_{ROI}$ by bounding downside through staged gates.

### 2.4 The three component gaps

Axiom III amplifies each friction component by the asymmetry inside its own pair of parties. The three pairs are different, so the three gaps have different instruments and cannot be read off one score.

| Gap | Pair | What is unknown | Instrument | Closed by |
|---|---|---|---|---|
| $\hat{\Delta}_{search}$ | The buyer against the market | Which category this is, who sells it, how to reach a seller at all | [Deal Triage Calculator](../../practice/deal-triage-calculator.md), search block | Education, reference architectures, category definition, channel |
| $\hat{\Delta}_{consensus}$ | The buyer's stakeholders against each other | What each of the others is measured on | [Deal Triage Calculator](../../practice/deal-triage-calculator.md), consensus block | Stakeholder mapping in the Blueprint, then the Red Team workshop |
| $\hat{\Delta}_{implementation}$ | The seller against the buyer | The buyer's environment, and the seller's capability in it | [Bilateral Asymmetry Scorecard](../../practice/asymmetry-scorecard.md) | Blueprint, Red Team, MIP |

**Only the enforcement gap is bilateral.** Sections 2.2 and 2.3 model its two halves, $I_{seller}$ and $I_{buyer}$, and section 2.1's sum applies to that pair alone:

$$\hat{\Delta}_{implementation} = \frac{I_{seller} + I_{buyer} - 2}{8}$$

The other two gaps have no seller-side term. A buyer who cannot name the category is not ignorant *of the seller*, and two stakeholders who cannot see each other's objectives are not separated by anything the seller knows and withholds. Each is measured as the fraction of its own instrument's items that remain unevidenced, which lands on $[0, 1]$ with a true zero and needs no rescaling:

$$\hat{\Delta}_{search} = 1 - \frac{e_{search}}{n_{search}}, \qquad \hat{\Delta}_{consensus} = 1 - \frac{e_{consensus}}{n_{consensus}}$$

Where $n_k$ counts the items in scope and $e_k$ counts those with evidence attached. The bargaining reading is a proxy: the instrument counts stakeholders whose measured objective the seller can read, while Axiom III names each stakeholder's own uncertainty about their outcome. [07-open-questions.md](./07-open-questions.md) item 13 records the gap. An instrument emitting no items at all leaves its gap undefined rather than zero, and a component with no cost carries no weight in the mean either way.

**The bargaining gap is not the same quantity as incentive variance.** $\text{Var}(I_i)$ in section 3.2 measures how far apart the stakeholders' interests actually sit. $\hat{\Delta}_{consensus}$ measures how much of that the room can see. A committee can be genuinely aligned and unable to prove it, which is cheap to fix, or genuinely split and unaware, which is the expensive case and the one that surfaces late. The two terms enter $F_{effective}$ at different places: variance raises the base cost $F_{consensus}$, and the gap amplifies it.

**A note on $\beta$.** Section 3.1's $\beta$ is the organizational complexity exponent and belongs to the bargaining base cost. Nothing in this framework weights one side's ignorance against the other's inside a gap. $I_{seller}$ and $I_{buyer}$ are summed unweighted by section 2.1, and any future weighting parameter would be a parameter of the enforcement pair specifically, since it is the only pair with two distinguishable sides.

---

## 3. Bargaining Cost (Consensus Friction)

### 3.1 Formulation

$$F_{consensus} = \alpha \cdot N^{\beta} \cdot (1 + \text{Var}(I_i))$$

| Symbol | Meaning | Range | Default |
|---|---|---|---|
| $N$ | Stakeholders with veto power or evaluation responsibility | $\ge 1$ | measured |
| $\text{Var}(I_i)$ | Variance in stakeholder incentive alignment | $[0, 1]$ | measured |
| $\alpha$ | Baseline coordination overhead | $> 0$ | 1.0 |
| $\beta$ | Organizational complexity exponent | $[1.2, 2.0]$ | 1.35 |

Variance is bounded above by 1 because $I_i$ is bounded on $[-1, 1]$. A computed value above 1 indicates an arithmetic error, not an unusually divided committee.

The exponent $\beta > 1$ reflects that communication channels grow as $N(N-1)/2$ rather than as $N$. Adding the sixth stakeholder to a committee costs more than adding the second.

### 3.2 Incentive variance

Let $I_i \in [-1, 1]$ denote stakeholder $i$'s utility from the initiative, where $+1$ means the initiative advances their incentives, 0 means no effect, and $-1$ means it conflicts directly with their measured objectives or operational control.

$$\bar{I} = \frac{1}{N}\sum_{i=1}^{N} I_i \qquad \text{Var}(I_i) = \frac{1}{N}\sum_{i=1}^{N}(I_i - \bar{I})^2$$

When every stakeholder holds identical alignment, variance is zero and friction reduces to the structural floor $\alpha N^{\beta}$. Size alone imposes cost even under perfect agreement.

**$I_i$ is not directly observable, and the observable proxy is biased downward.** The definition above is the stakeholder's utility from the initiative, meaning the effect on the objectives they are measured on. What a seller can actually watch is the position each stakeholder states in a room containing the others. Stated positions converge under social pressure while measured objectives do not, so variance computed from stated positions understates $\text{Var}(I_i)$, and it understates it most in the polarized committees where the term matters most.

Two consequences. Score $I_i$ from what a stakeholder is measured on, never from what they said in the meeting. And read unanimous stated alignment as weak evidence, since a committee where nobody voices dissent is as consistent with suppressed variance as with genuine agreement. This is the quasi-resolution Cyert and March describe, and it is why a saboteur surfaces late rather than early. See [buying-center-dynamics.md](../02-research/buying-center-dynamics.md).

### 3.3 Sensitivity

$$\frac{\partial F_{consensus}}{\partial N} = \alpha \beta N^{\beta-1}(1 + \text{Var}(I_i)) \qquad \frac{\partial^2 F_{consensus}}{\partial N^2} > 0$$

$$\frac{\partial F_{consensus}}{\partial \text{Var}(I_i)} = \alpha N^{\beta}$$

The return on reducing misalignment scales with $N^{\beta}$. In a committee of three, aligning incentives produces modest gains. In a committee of ten, it produces the largest single reduction available to the seller. This is the quantitative case for running the Red Team workshop on large committees specifically, and it is why the [Consensus Friction Calculator](../../practice/consensus-friction-calculator.md) escalates to executive sponsorship above a threshold rather than recommending more meetings.

### 3.4 Field extension: technical overlap

The field calculator carries one term this section does not:

$$F_{consensus} = \alpha N^{\beta}(1 + \text{Var}(I_i))(1 + \gamma_{TO} \cdot TO)$$

Where $TO \in [1, 5]$ scores architectural alignment among technical evaluators and $\gamma_{TO} = 0.20$.

The term exists because incentive variance under-captures a specific and common failure. Two architects can both want the project to succeed, score identically on incentive alignment, and still deadlock on hosting model or integration pattern. Technical philosophy conflict is not incentive conflict, and treating it as one causes the model to score fractured engineering organizations as low-friction.

Treat $TO$ as a field refinement rather than core theory. The two-term form above is what the axioms require. The three-term form is what practitioners need to avoid a predictable blind spot.

---

## 4. Urgency Decay

### 4.1 Value decay

$$V_{solution}(t) = V_0 \cdot e^{-\delta t}$$

Where $V_0$ is peak perceived value at the triggering event and $t$ is elapsed months. This is the value-decay half of the Decay Clock, the second standing assumption in the Constitution.

### 4.2 Structural form of the decay rate

The Constitution treats $\delta$ as a parameter. It has structure:

$$\delta = \frac{\lambda_{inertia}}{1 + \gamma_r E_{external}}$$

| Symbol | Meaning | Range | Default |
|---|---|---|---|
| $\lambda_{inertia}$ | Organizational inertia (bureaucracy, competing projects, status quo preference) | $[0.1, 2.0]$ | measured |
| $E_{external}$ | Magnitude of external catalyst (regulatory mandate, competitive threat, market shift) | $[0, 10]$ | measured |
| $\gamma_r$ | Responsiveness converting external pressure into internal action | $[0.1, 1.0]$ | 0.5 |

Note that $\gamma_r$ here is the responsiveness factor and is distinct from the $\gamma_k$ of the Constitution's asymmetry drift equation $\hat{\Delta}_k(t) = \hat{\Delta}_k(0) + \gamma_k t$. Both families carry subscripts, and they are told apart by what the subscript names: a friction component, or a mechanism.

### 4.3 Boundary behavior

With no external catalyst, decay runs at the full rate of organizational inertia:

$$\lim_{E_{external} \to 0} \delta = \lambda_{inertia}$$

With an overwhelming catalyst, decay approaches zero and perceived value holds:

$$\lim_{E_{external} \to \infty} \delta = 0$$

$$\frac{\partial \delta}{\partial E_{external}} = \frac{-\gamma_r \lambda_{inertia}}{(1 + \gamma_r E_{external})^2} < 0 \qquad \frac{\partial \delta}{\partial \lambda_{inertia}} = \frac{1}{1 + \gamma_r E_{external}} > 0$$

**Field implication.** The seller cannot change the buyer's inertia. The seller can find, name, and quantify an external catalyst the buyer has not yet connected to this decision. That is the only term in $\delta$ a seller can move, which is why the Blueprint asks for the economic event by name.

---

## 5. Parameter Reference

Every parameter in this file, and every threshold and band elsewhere in the framework, lives in [06-calibration.md](./06-calibration.md). It is the single home for them on purpose: two tables of the same values drift, and the separation is what lets the structural claims above be read without any of the numbers.

Nothing in that file is a measurement. Read the provenance column before quoting any value outside this repository.

---

## 6. What Would Make These Models Empirical

Five conditions, in [06-calibration.md](./06-calibration.md) section 4, in rough order of how much each one buys. The first is logging the three component gaps separately at open and at every artifact boundary, which is what makes the drift rates estimable and what would test the framework's central dynamic claim.

Until then, treat every output as a structured comparison between deals rather than a quantity. A deal scoring 7.2 is meaningfully worse than one scoring 4.1. Neither number predicts a close date.

---

## Related

- [00-tcg-constitution.md](./00-tcg-constitution.md) — The axioms these models serve. Axiom III carries both cost representations reconciled in Section 1.
- [01-motions.md](./01-motions.md) — Motion selection, which consumes the calculator's level and direction rather than these models.
- [Bilateral Asymmetry Scorecard](../../practice/asymmetry-scorecard.md) — Field instrument producing $\Delta_A$.
- [Consensus Friction Calculator](../../practice/consensus-friction-calculator.md) — Field instrument producing $F_{consensus}$.
- [Milestone Valuation Model](../../practice/milestone-valuation-model.md) — Applies staged uncertainty decay to MIP gate design.
- [real-options.md](../02-research/real-options.md) — Source for the staging logic behind $\delta$ and milestone gating.
- [Friction Efficiency Index](../../practice/friction-efficiency-index.md) — Retrospective execution metrics (FAR, BCV, RMS, SVI). Deliberately downstream of this file: those measures score how the motion was run rather than deriving from an axiom term.
