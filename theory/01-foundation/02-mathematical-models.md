---
title: "Mathematical Models"
layer: theory
status: active
version: 2.0
operationalizes: [axiom-1, axiom-2, axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# Mathematical Models

**Version:** 2.0
**Purpose:** To specify the functional forms behind the variables the [Constitution](./00-tcg-constitution.md) names but does not compute.

The Constitution is axioms-first. It states that each cost has a threshold that keeps the buyer out, that each party goes ahead only when its own share of today's investment is covered by its own return, and that what a party sinks exposes it to what it cannot verify or enforce. It does not say *by how much*, or *as a function of what*. This file supplies those functional forms.

Nothing here introduces new claims. Every model traces to a term the Constitution already defines. If a model here cannot be traced to an axiom, it does not belong in this file either.

> [!IMPORTANT]
> **Calibration status.** The functional forms below are specified, not fitted. Parameter defaults are reasoned starting values, not empirical estimates from booked deal data. [06-calibration.md](./06-calibration.md) marks which parameters carry literature support and which are placeholders. Use these models to structure judgment, not to forecast.

---

## 1. The Two Conditions

### 1.1 One condition per party

$$S_b = V_{switch}(t) - P - \sum_{k} I^b_k - L_b \qquad S_s = P - C_{deliver} - \sum_{k} I^s_k - L_s$$

| Symbol | Meaning |
|---|---|
| $V_{switch}(t)$ | $\tilde{V}_{solution} \cdot e^{-\delta t} - V_{next\_best}$, the buyer's opportunity cost of staying where they are, read on recognized value $\tilde{V}_{solution}$ because that is what the buyer decides on. $V_{next\_best}$ includes building it internally. Section 4 gives the decay. |
| $P$ | Price over the relationship |
| $C_{deliver}$ | The seller's cost of delivering against that price |
| $I^b_k$, $I^s_k$ | What the buyer and the seller invest today against cost $k \in \{search,\; consensus,\; implementation\}$ (Axiom II) |
| $L_b$, $L_s$ | Each party's expected future loss (Axiom III), section 5 |

A deal closes when $S_b > 0$, $S_s > 0$, no cost sits above its participation threshold, and no payer carries more than its capacity across the costs it carries (section 6). Recurrence enters through $P$ and $C_{deliver}$ summed over expected renewals, which [04-seller-surplus-model.md](./04-seller-surplus-model.md) section 7 writes out with a retention probability and a discount rate.

The seller's condition is the seller surplus model's $S_{seller} = p_{close}(V_{contract} - C_{deliver}) - C_{invest}$ conditional on a close, with $C_{invest}$ split by the cost it pays down and the future loss written out instead of left inside $p_{close}$.

### 1.2 Units

**Every term is a fraction of annual contract value.** That is what makes the two conditions comparable and what lets investment and exposure be estimated at all: a seller can price its own engineering hours, and a buyer can price the staff time its integration will take. A deal at list price with no other cost has $P = 1$.

Reading any of these terms in percentage points instead is a unit error and not a second option. A future loss of 0.75 means three quarters of a year's contract value, not three quarters of a percent. The gate is the exception: it reads demand in each payer's own units (section 6).

### 1.3 Price cancels

Adding the two conditions:

$$S_b + S_s = V_{switch}(t) - C_{deliver} - \sum_{k} \left(I^b_k + I^s_k\right) - L_b - L_s$$

$P$ is gone, because price is a transfer: what leaves the buyer arrives at the seller. Price belongs in both conditions and in neither party's cost of transacting. Three results follow from the accounting rather than from any coefficient.

**Hold-up is a transfer too.** Section 5.5 splits each party's future loss into the part a failed fit destroys and the part the other side can take at a renegotiation: $L_p = L^{fit}_p + L^{hold}_p$, with $L^{fit}_p = Q_p\,\pi^{gap}_p$ and $L^{hold}_p = (1 - \pi^{gap}_p)\,H_p$. What one side takes, the other receives, so only the fit loss enters what the deal creates. The two conditions as written count the hold-up each side fears and leave out the take the other side plans, so

$$W = V_{switch}(t) - C_{deliver} - \sum_{k} \left(I^b_k + I^s_k\right) - L^{fit}_b - L^{fit}_s, \qquad S_b + S_s = W - L^{hold}_b - L^{hold}_s$$

Where each side expects exactly the take the other plans, that take belongs in the taker's condition, the sum is $W$, and some price closes any deal with $W > 0$. Hold-up then costs both sides through the specific investment a party declines to sink because it keeps only part of its return (Grossman and Hart 1986), which lowers $W$ itself. Where one side fears more than the other plans, the difference is the *hold-up wedge*, the premise's two readings applied to $H$, and a deal with $W > 0$ can fail one side's condition because of it. A posted bond, staged fees or an allocated right close the wedge without changing $W$. A reciprocal specific investment closes it too, but it is itself sunk, so it lowers $W$ unless it is productive. Haggling over the renegotiation also destroys value, and it is not modeled here. Where the bond condition holds, both $H_p$ are zero, the wedge closes, and $S_b + S_s = W$, which is what every worked example assumes.

**The three levers.** A seller can move a deal three ways. A discount never raises what the deal creates, and the other two raise it only by lowering $\pi^{gap}$.

| Lever | What it moves | Effect on $W$ |
|---|---|---|
| Discount | $P$ | None. Surplus moves from seller to buyer one for one. |
| Guarantee, clawback, hostage | Part of $L_b$ onto the seller, $\pi^{gap}$, and $H_p$ | None for the transfer itself. Rises by as much as the commitment lowers $\pi^{gap}$, by changing what the seller does or by revealing which sellers can afford to offer it. A bond or staged fees that lower $H_p$ close the hold-up wedge without changing $W$. A reciprocal specific investment also adds to the other side's $L^{fit}$ |
| Verification | $\pi^{gap}$ for whichever party cannot verify | Rises. A cost both sides were carrying shrinks. |

**Persuasion moves the decision more than $W$.** Read on realizable value, as the Constitution reads the joint condition, persuasion leaves $V_{solution}$ where it was and moves $\tilde{V}_{solution}$ or $\tilde{n}_k$. What the seller spends on it sits in $I^s_k$ beside the work section 6 prices, so $W$ falls by that much. Where it lowers $\tilde{n}_k$ below $n_k$, the buyer provides for less work than it will meet, and $W$ falls further. Where it carries a buyer into a deal with $W < 0$, the gap is a loss the buyer carries after go-live. A claim the buyer cannot check that happens to be true can let through a deal with $W > 0$, as far as cheap talk informs. Persuasion raises $W$ only where a convinced buyer adopts harder and realizes more, the case where the second standing assumption fails ([value-and-persuasion.md](../02-research/value-and-persuasion.md)). A discount leaves $W$ alone in each deal and changes which deals occur and, where retention depends on the price path, how long they last: in consumer subscriptions, customers acquired on a discount retain worse (Lewis 2006).

**A guarantee is part transfer and part verification.** The transfer moves loss without shrinking it. The selection effect is Spence's: a seller confident of delivering expects to pay little on its guarantee and a weak one expects to pay the full penalty, so the offer itself narrows the buyer's half of the implementation gap. The sorting is clean only when every seller can carry the penalty, because a guarantee also screens on balance sheet, and only when the outcome is the seller's to deliver, because a buyer that under-resources adoption makes the seller pay for its slack. [costly-signals.md](../02-research/costly-signals.md) carries the argument.

A resolved gap can therefore close a deal that no discount could. When the joint surplus is negative, no price makes both conditions positive at once, and only a lever that raises the joint surplus can rescue the deal. When it is positive, a discount can close the deal by moving the split, and so can verification. What stays empirical is whether a given verification costs less than the loss it removes, and the verification's own cost is an investment under Axiom II.

### 1.4 Moving investment between parties

Write the work against cost $k$ as $W_k$, and each party's cost of doing a unit of it as $\theta^b_k$ and $\theta^s_k$. Moving a share $w$ of the work from buyer to seller changes the joint surplus by

$$\Delta(S_b + S_s) = w\left(\theta^b_k - \theta^s_k\right) - \Delta L_b - \Delta L_s$$

The first term is specialization: positive when the seller does the work more cheaply. The second and third are Axiom III, entering with a minus because each condition subtracts its loss. The move can lower the buyer's future loss, by catching misfit in use, which raises the joint surplus. It also raises the seller's, by making the seller's investment specific to this buyer, which lowers it. With equal unit costs and no change in future loss, the move only changes the split. It still closes deals, because it lifts $S_b$ above zero whenever $S_s$ has room to fall.

A forward-deployed engineer is the case where all three terms move. [04-seller-surplus-model.md](./04-seller-surplus-model.md) carries the seller's side.

### 1.5 Where the seller's next dollar goes

The gate says how much demand the seller must move, $(n_k - \kappa_k)^+$ off each payer (section 6). With every capacity known, the deal goes once all of it is moved, so the gate fixes the total and not the order. Order matters where capacities are uncertain, which before discovery they always are.

**Across payers.** For payers that each carry one cost, write $G_k$ for the seller's belief about $\kappa_k$, $\hat{\kappa}_k$ for its central estimate, and $S_k = 1 - G_k(n_k - a_k)$ for the chance the payer already carries what is left. With the payers independent, $\Pr(\text{go}) = \prod_k S_k$. Each unit moved off a payer costs the seller $c^s_k$, so a dollar on cost $k$ raises the chance of going ahead by

$$\frac{g_k\left(n_k - a_k\right)}{c^s_k} \prod_{j \ne k} S_j = \Pr(\text{go}) \cdot \frac{h_k}{c^s_k}$$

where $h_k = g_k / S_k$, the *hazard*, is the proportional rise in that payer's chance of carrying the rest when one more unit is moved. A payer whose limit most likely sits just under what is left has a high hazard. A limit spread thinly over a wide range has a low one, so uncertainty alone earns no dollar. Where the paydown carries over to rivals' deals, as category education does, the seller keeps only $\chi_k$, its chance of winning a buyer the dollar tips. The next dollar goes to the largest $\chi_k h_k / c^s_k$. Spending dollar by dollar this way is optimal only where each $S_k$ is log-concave, and a limit the seller knows exactly is all or nothing, compared by the lump it needs.

**Within a payer.** Costs one payer carries draw on one capacity, so they tip together. A dollar goes to the cost that frees the most of that capacity per dollar, the smallest $c^s_k \kappa_k$, whatever its position.

**Past the limit.** If the seller is sure a cost exceeds $\kappa_k + \bar{A}_k$, $\Pr(\text{go})$ is zero and no absorption on any cost moves it. Only a change to $n_k$ does. Because $\Pr(\text{go})$ scales every dollar in the deal, a seller that expects one cost likely past its limit gains little from spending anywhere else in it. Before entry the buyer tests $\tilde{n}_k \le \kappa_k + \bar{A}_k$, so the lever there is evidence that lowers $\tilde{n}_k$, which this section prices only as spending.

**The tightest cost is a special case.** The rule pays down the largest remaining position until it meets the next when the payers are separate, $(\kappa_k - \hat{\kappa}_k)/\bar{A}_k$ has one distribution across costs with a rising hazard, each position is read at $\hat{\kappa}_k$, a unit of position costs the seller the same on every cost ($c^s_k \bar{A}_k$ equal), and $\chi_k$ is equal. The instruments use it as their default until the seller reads the rest, and record any other order with its reason. It fails where a known limit needs a lump, where the seller absorbs another cost far more cheaply, where a paydown carries over to rivals, and before discovery, where measuring a cost can be worth more than paying one down.

**What the rule leaves out.** Each unit absorbed also lowers the buyer's investment by $c^b_k$, which raises $S_b$, the second route in section 6. A dollar spent where the seller works more cheaply, $\theta^s_k < \theta^b_k$ in section 1.4, raises what the deal creates. Spending specific to the seller also shifts its win share among buyers who would go anyway. $G_k$, $h_k$ and $\chi_k$ are named and not valued ([06-calibration.md](./06-calibration.md) section 3.2).

---

## 2. The Three Gaps

Each of the three costs runs between its own pair of parties, and each pair's uncertainty is measured on its own instrument. The gaps decide the chance of future loss in section 5. They no longer multiply any cost: Constitution 4.0 retired the per-component multiplier.

### 2.1 The implementation gap is a sum

$$\Delta_A = I_{seller} + I_{buyer}$$

The gap is a **sum**, not a difference. Total informational misalignment across the buyer-seller boundary is the seller's ignorance of the buyer's environment plus the buyer's uncertainty about the seller's capability. A deal where both sides are equally blind is not symmetric in any useful sense. It is maximally uninformed on both sides, and $\Delta_A$ must reflect that. $\Delta_A = 0$ represents complete informational symmetry.

**This is the policing and enforcement cost's gap, the implementation gap in field terms, not the deal's.** It is the only bilateral pair, so it is the only gap with two halves, and the halves matter separately: the buyer's future loss runs on $I_{buyer}$, and the seller's on $I_{seller}$.

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

This floor is the model's most useful field implication, and it is why the chance of future loss in section 5 has a floor above zero. No quantity of costly signaling drives buyer uncertainty to zero while the return itself remains volatile. Past a point, the seller stops investing in proof and starts working on the variance of the projected return. The Red Team targets $K_{vendor}$. The MIP targets $\sigma_{ROI}$ by bounding downside through staged gates.

### 2.4 The three gaps and their instruments

| Gap | Pair | What is unknown | Instrument |
|---|---|---|---|
| $\hat{\Delta}_{search}$ | The buyer against the market | Which category this is, who sells it, how to reach a seller at all | [Deal Triage Calculator](../../practice/deal-triage-calculator.md), search block |
| $\hat{\Delta}_{consensus}$ | Each decision role, about its own outcome | What the change does to that role's budget, headcount and standing | [Deal Triage Calculator](../../practice/deal-triage-calculator.md), consensus block |
| $\hat{\Delta}_{implementation}$ | The seller against the buyer | The buyer's environment, and the seller's capability in it | [Enforcement Ledger](../../practice/enforcement-ledger.md) |

The search and bargaining gaps are measured as the fraction of their own instrument's items that remain unevidenced, which lands on $[0, 1]$ with a true zero:

$$\hat{\Delta}_{search} = 1 - \frac{e_{search}}{m_{search}}, \qquad \hat{\Delta}_{consensus} = 1 - \frac{e_{consensus}}{m_{consensus}}$$

Where $m_k$ counts the items in scope and $e_k$ counts those with evidence attached. An instrument emitting no items leaves its gap undefined rather than zero.

**The bargaining gap has one definition:** the share of decision roles whose occupant has stated their own exposure. [08-from-axioms-to-instruments.md](./08-from-axioms-to-instruments.md) section 2.2 carries the argument. Earlier calculators read a proxy, the share with a documented measured objective, which is the seller's uncertainty about them rather than theirs about themselves. The Deal Triage Calculator 9.0 retired it, and [07-open-questions.md](./07-open-questions.md) item 2 records that the decision-role map that reads the gap is not yet built.

**The bargaining gap is not the same quantity as incentive variance.** $\text{Var}(I_i)$ in section 3.2 measures how far apart the decision roles' interests actually sit, and it sets the size of the bargaining cost. The gap measures what each role cannot yet see about its own exposure, and it feeds the chance of future loss. A committee can be genuinely aligned and unable to prove it, which is cheap to fix, or genuinely split and unaware, which is the expensive case and the one that surfaces late.

### 2.5 Normalizing the scorecard

The [Enforcement Ledger](../../practice/enforcement-ledger.md) reports the policing gap already normalized, as the mean of its two unevidenced fractions. Earlier versions of the field instrument produced a raw gap on $[2, 10]$, two halves each on $[1, 5]$, and the model keeps that form, so a raw score is normalized first:

$$\hat{\Delta}_{implementation} = \frac{\Delta_A^{raw} - 2}{8}, \qquad \hat{\Delta}_{implementation} \in [0, 1]$$

Each half normalizes the same way on its own range, $(h - 1)/4$, which is what section 5 needs when it reads the buyer's half and the seller's half apart. Use the raw score for the scorecard's own triage bands. Use the normalized value everywhere else. Confusing the two produces results off by an order of magnitude, and `models/tcg_models.py` refuses a raw value at the type level.

---

## 3. Bargaining Cost (Consensus Friction)

### 3.1 Formulation

$$F_{consensus} = \alpha \cdot N^{\beta} \cdot (1 + \text{Var}(I_i))$$

| Symbol | Meaning | Range | Default |
|---|---|---|---|
| $N$ | Decision roles with veto power or evaluation responsibility | $\ge 1$ | measured |
| $\text{Var}(I_i)$ | Variance in decision-role incentive alignment | $[0, 1]$ | measured |
| $\alpha$ | Baseline coordination overhead, the conversion into contract value | $> 0$ | 1.0 |
| $\beta$ | Organizational complexity exponent | $[1.2, 2.0]$ | 1.35 |

This is the structural form of the bargaining and decision cost with nothing moved yet (section 6). $N$ is wider than the gate's consensus demand, since evaluators add coordination work without holding a veto. $\alpha$ is what converts it into fractions of annual contract value, and its default of 1.0 is a normalizing convention rather than a conversion anyone has measured.

Variance is bounded above by 1 because $I_i$ is bounded on $[-1, 1]$. A computed value above 1 indicates an arithmetic error, not an unusually divided committee.

The exponent $\beta > 1$ reflects that communication channels grow as $N(N-1)/2$ rather than as $N$. Adding the sixth decision role costs more than adding the second.

### 3.2 Incentive variance

Let $I_i \in [-1, 1]$ denote decision role $i$'s utility from the initiative, where $+1$ means the initiative advances its incentives, 0 means no effect, and $-1$ means it conflicts directly with its measured objectives or operational control.

$$\bar{I} = \frac{1}{N}\sum_{i=1}^{N} I_i \qquad \text{Var}(I_i) = \frac{1}{N}\sum_{i=1}^{N}(I_i - \bar{I})^2$$

When every decision role holds identical alignment, variance is zero and the cost reduces to the structural floor $\alpha N^{\beta}$. Size alone imposes cost even under perfect agreement.

**$I_i$ is not directly observable, and the observable proxy is biased downward.** The definition above is the role's utility from the initiative, meaning the effect on the objectives it is measured on. What a seller can actually watch is the position each occupant states in a room containing the others. Stated positions converge under social pressure while measured objectives do not, so variance computed from stated positions understates $\text{Var}(I_i)$, and it understates it most in the polarized committees where the term matters most.

Two consequences. Score $I_i$ from what a role is measured on, never from what its occupant said in the meeting. And read unanimous stated alignment as weak evidence, since a committee where nobody voices dissent is as consistent with suppressed variance as with genuine agreement. This is the quasi-resolution Cyert and March describe, and it is why a saboteur surfaces late rather than early. See [buying-center-dynamics.md](../02-research/buying-center-dynamics.md).

### 3.3 Sensitivity

$$\frac{\partial F_{consensus}}{\partial N} = \alpha \beta N^{\beta-1}(1 + \text{Var}(I_i)) \qquad \frac{\partial^2 F_{consensus}}{\partial N^2} > 0$$

$$\frac{\partial F_{consensus}}{\partial \text{Var}(I_i)} = \alpha N^{\beta}$$

The return on reducing misalignment scales with $N^{\beta}$. In a committee of three, aligning incentives produces modest gains. In a committee of ten, it produces the largest single reduction available to the seller. This is the quantitative case for running the Red Team workshop on large committees specifically, and it is why the [Bargaining Ledger](../../practice/bargaining-ledger.md) answers a high reading with a staked sponsor and a ratified arrangement rather than more meetings.

### 3.4 Field extension: technical overlap

The field calculator carries one term this section does not:

$$F_{consensus} = \alpha N^{\beta}(1 + \text{Var}(I_i))(1 + \gamma_{TO} \cdot TO)$$

Where $TO \in [1, 5]$ scores architectural alignment among technical evaluators and $\gamma_{TO} = 0.20$.

The term exists because incentive variance under-captures a specific and common failure. Two architects can both want the project to succeed, score identically on incentive alignment, and still deadlock on hosting model or integration pattern. Technical philosophy conflict is not incentive conflict, and treating it as one causes the model to score fractured engineering organizations as low-friction.

Treat $TO$ as a field refinement rather than core theory. The two-term form above is what the axioms require. The three-term form is what practitioners need to avoid a predictable blind spot.

### 3.5 The count is read after exposure

$N$ is not fixed before the policing reading. Two mechanisms add decision roles as the deal's specific exposure grows, and both run from Axiom III exposure into this count.

$$N = \left| R_0 \cup R_{imp} \right| + N_{rules}(n_{exposure})$$

| Symbol | Meaning |
|---|---|
| $R_0$ | The roles mapped so far that can say no |
| $R_{imp}$ | The roles a divergent step imposes on. An imposition forces a practice on whoever runs the step, and that role objects. A deficiency the buyer accepts or works around adds exposure and no veto (Strong and Volkoff 2010, in [process-misfit.md](../02-research/process-misfit.md)) |
| $N_{rules}$ | The approvers and formal reviews the buyer's own rules require at this deal's size and specific exposure: a spend threshold, a security review above a data class, a board above a commitment. A group demands broader agreement when a decision can do more harm (Buchanan and Tullock 1962), and these rules are how a buyer writes that down. They are the bargaining cost floor, set outside the deal and triggered by it |

Every term is a count read off the buyer, so the coupling adds no parameter. The union keeps a role that is already counted from being counted twice. The coupling also runs back. Each role added brings requirements, and a requirement the product does not meet is a new divergent step, which may impose on a further role. The loop is named and not modeled, and the count stops when a pass adds no role. A larger coalition costs more by the convexity in section 3.3, so the feedback raises the cost faster than the count.

**The count is dated.** $R_{imp}$ and $n_{exposure}$ are counted on the divergence found so far. Before fit is verified on the buyer's own workflow, both the implementation position and $N$ are lower bounds, and section 6 reads the start on that basis.

---

## 4. Urgency Decay

### 4.1 Value decay

$$\tilde{V}_{solution}(t) = \tilde{V}_0 \cdot e^{-\delta t}$$

Where $\tilde{V}_0$ is the buyer's recognized value at the triggering event and $t$ is elapsed months. This is the value-decay half of the Decay Clock, the second standing assumption in the Constitution.

![Two exponential decay curves falling toward a floor at the value of the next best alternative. Organizational inertia alone reaches the floor in the second month. A named external catalyst holds value above it until the eleventh.](./assets/value-decay.svg)

### 4.2 Structural form of the decay rate

The Constitution treats $\delta$ as a parameter. It has structure:

$$\delta = \frac{\lambda_{inertia}}{1 + \gamma_r E_{external}}$$

| Symbol | Meaning | Range | Default |
|---|---|---|---|
| $\lambda_{inertia}$ | Organizational inertia (bureaucracy, competing projects, status quo preference) | $[0.1, 2.0]$ | measured |
| $E_{external}$ | Magnitude of external catalyst (regulatory mandate, competitive threat, market shift) | $[0, 10]$ | measured |
| $\gamma_r$ | Responsiveness converting external pressure into internal action | $[0.1, 1.0]$ | 0.5 |

Note that $\gamma_r$ here is the responsiveness factor and is distinct from the $\gamma_k$ of the drift equation in section 5.3. Both families carry subscripts, and they are told apart by what the subscript names: a cost, or a mechanism.

### 4.3 Boundary behavior

With no external catalyst, decay runs at the full rate of organizational inertia:

$$\lim_{E_{external} \to 0} \delta = \lambda_{inertia}$$

With an overwhelming catalyst, decay approaches zero and perceived value holds:

$$\lim_{E_{external} \to \infty} \delta = 0$$

$$\frac{\partial \delta}{\partial E_{external}} = \frac{-\gamma_r \lambda_{inertia}}{(1 + \gamma_r E_{external})^2} < 0 \qquad \frac{\partial \delta}{\partial \lambda_{inertia}} = \frac{1}{1 + \gamma_r E_{external}} > 0$$

**Field implication.** The seller cannot change the buyer's inertia. The seller can find, name, and quantify an external catalyst the buyer has not yet connected to this decision. That is the only term in $\delta$ a seller can move, which is why the Blueprint asks for the economic event by name.

---

## 5. Future Loss

### 5.1 Exposure times the chance it does not come back

$$L_p = Q_p \cdot \pi_p, \qquad Q_p = C^{p}_{invest} - R^{p}_{redeploy}, \qquad p \in \{b, s\}$$

$Q_p$ is the appropriable quasi-rent of Klein, Crawford and Alchian: what party $p$ has sunk, less what it could recover by redeploying it elsewhere. [04-seller-surplus-model.md](./04-seller-surplus-model.md) section 3 defines it for the seller, and the definition reads the same for the buyer, whose non-redeployable investment is the integration built and the workflows rewired to fit this product.

$L_p$ is a shortfall in the return party $p$ expected from the relationship, through hold-up or through a fit that fails in use. It is not a second charge for the investment Axiom II already counted, which is why it sits on the return side: $Q_p$ bounds it because it is the most the other side can extract or a failure can destroy.

### 5.2 The chance of loss

$\pi_p$ rises with the gaps party $p$ cannot close.

| Party | The gaps its loss runs on |
|---|---|
| Buyer | Its own half of the implementation gap, $I_{buyer}$: whether the seller delivers and the product fits. The bargaining gap: whether the coalition holds once the investment is sunk. |
| Seller | Its own half of the implementation gap, $I_{seller}$: the environment it has not mapped. The bargaining gap: the coalition it cannot see. |

The search gap does not appear. It prices today's search cost and decides participation under Axiom I, and once a buyer has chosen, it has stopped mattering to what that buyer loses later.

**The form is a placeholder.** Writing $g_p \in [0, 1]$ for the mean of the normalized gaps in that party's row:

$$\pi_p = \pi_0 + (1 - \pi_0)\, g_p$$

The floor $\pi_0 > 0$ exists because some risk survives any amount of proof, which is section 2.3's floor read as a probability. The straight line between floor and ceiling is chosen, and nothing in the framework claims a curvature. Constitution 3.0 argued for a convex cost of uncertainty, and the argument rested on counting uncertainty twice. Section 7 records it. The mean as the way two gaps combine is also chosen.

### 5.3 Drift

Two things drift after go-live, and they answer to different tools.

**What was verified goes stale.** Nothing has to change for this. The evidence ages, the people who saw it move on, and absent maintenance each gap rebuilds toward its ceiling:

$$\hat{\Delta}_k(t) = 1 - \left(1 - \hat{\Delta}_k(0)\right) e^{-\gamma_k t}$$

The gap stays on $[0, 1]$, the range every count-based instrument can actually report: a share of unevidenced items cannot exceed all of them. The rate $\gamma_k \ge 0$ is named and not valued. Maintenance is re-verification, usage evidence, outcome reviews and references kept current, and it pulls the gap down at a rate $\eta_k$ in proportion to its size:

$$\frac{d\hat{\Delta}_k}{dt} = \gamma_k\left(1 - \hat{\Delta}_k\right) - \eta_k \hat{\Delta}_k \qquad \hat{\Delta}^*_k = \frac{\gamma_k}{\gamma_k + \eta_k}$$

The gap moves toward $\hat{\Delta}^*_k$ at rate $\gamma_k + \eta_k$, from wherever it starts. With $\eta_k = 0$ this is the unmaintained curve, which ends at the ceiling, where the incumbent knows no more than a challenger. Any maintenance holds it below. That is the condition between the two curves in the Constitution's drift figure, and section 5.7 says how much maintenance a seller funds. The proportional form is chosen.

**The fit itself drifts.** Each party changes: the buyer its workflow, its roles and the rules it works under, the seller its product, its releases and its team. Each change can open a divergent step that did not exist at go-live, at rates $\psi_b$ and $\psi_s$, named and not valued. This is not a gap. Perfect knowledge of a misfit does not remove it, so re-verification does not reach it. It raises $n_{exposure}$ and, through section 3.5, the coalition, so the implementation and consensus positions at the next renewal rise even while every gap is held down. Three tools reach it.

- **Notice of change.** Each side commits to tell the other before it changes the product or the workflow. It does not lower $\psi$. It turns the other side's change into a dated event either can plan around, rather than a divergence discovered at renewal.
- **Re-adaptation.** Closing a divergent step is an investment under Axiom II, paid by whoever the arrangement says pays it.
- **A change process allocated before either side changes.** Who pays to adapt is the dispute fit drift creates, and it is cheapest to settle before anyone has moved. This is Axiom III's enforcement remedy applied after go-live, the Mutual Implementation Plan continued past it.

The seller can lower $\psi_s$ directly, through stability and deprecation commitments. It lowers $\psi_b$ only through configuration the buyer owns, which absorbs the buyer's change without opening a divergent step.

**Discovery is a separate mechanism.** It is a discrete step down that someone pays for at an artifact boundary, not drift running backwards. A departed champion is the opposite discrete event, the bargaining gap reopening at once. Between the two, the gap relaxes toward its ceiling at $\gamma_k$, and maintenance is whatever holds it down.

### 5.4 Staging

A buyer who commits in stages sinks $Q_m$ at gate $m$ against the residual uncertainty $x_m$ entering it:

$$L_b = \sum_{m} Q_m \, \pi(x_m) \qquad \text{rather than} \qquad Q \, \pi(x_0)$$

Because the residual falls from gate to gate, the staged loss is smaller whenever the large commitments come late, and a right to stop caps what each gate can lose. The Stage column of the [Enforcement Ledger](../../practice/enforcement-ledger.md) applies it.

**The stage equation.** At gate $m$ the buyer's expected surplus is

$$S_m = (1 - \pi_m)\left(V_{gross,m} - c_m\right) - \pi_m\,Q_m, \qquad \pi_m = \pi_0 + (1 - \pi_0)\,x_m$$

where $V_{gross,m}$ is the value the buyer realizes on completing the stage, $c_m$ the payment for it, paid only when its acceptance criteria are met, and $Q_m$ what the buyer sinks there and cannot recover. All three are fractions of annual contract value. A payment triggered by the calendar is made whether or not the stage succeeds, so the surplus falls by $\pi_m c_m$, which is largest at the first gate.

**The residual chain.** Each stage resolves a share $\mu_k$ of what remains, starting from the normalized policing gap $x_0$:

$$x_m = x_0 \prod_{k=1}^{m}(1 - \mu_k)$$

The reference profile, with each $\mu$ at 0.25, 0.50 and 0.80, leaves 0.75, 0.375 and 0.075 of $x_0$. Each share applies to what remains, so the residual compounds toward zero rather than stepping below it.

**Why the order of commitments matters.** With $x_0$ at 1, an illustrative floor $\pi_0$ of 0.05, and 0.85 of a year's contract value sunk in total:

| Gate | Entering $x_m$ | $\pi_m$ | Sunk $Q_m$ | $\pi_m Q_m$ |
|---|---|---|---|---|
| Core integration | 0.750 | 0.763 | 0.10 | 0.076 |
| Pilot | 0.375 | 0.406 | 0.25 | 0.102 |
| Full rollout | 0.075 | 0.121 | 0.50 | 0.061 |
| **Total** | | | **0.85** | **0.238** |

Sunk at once against the full gap, the same 0.85 is an expected loss of 0.85. Staged small first, it is 0.24. In the wrong order, 0.50 first and 0.10 last, it is 0.49. Staging helps, and the order decides how much. The values are illustrative and [06-calibration.md](./06-calibration.md) section 3.4 records them as chosen. The shape is the argument.

### 5.5 Joint exposure and the bond condition

Section 5.2 reads the chance of loss off the gaps a party cannot close, which is the hidden-information half of Axiom III. The other half is hold-up in plain view. At a renewal, or in a state the contract did not foresee, one side forces a renegotiation and the other can watch it happen and cannot stop it (Wathne and Heide 2000). What decides whether that pays is both quasi-rents at once.

**The renegotiation.** If the two parties part at a boundary, each loses what it sank and cannot redeploy, so continuing is worth $Q_b + Q_s$ more to the pair than parting. Where the contract is silent, the pair splits that amount when it renegotiates. Write $\omega$ for the share the other side, $-p$, captures. Party $p$ expected to recover its whole quasi-rent and recovers $(1 - \omega)(Q_p + Q_{-p})$, so the most the other side can take from it is $\omega Q_p - (1 - \omega) Q_{-p}$.

Forcing the renegotiation also costs the other side something: the future surplus it puts at risk by souring the relationship, $F_{-p}$, read in contract value off the repeated game in [04-seller-surplus-model.md](./04-seller-surplus-model.md) section 7. It forces the renegotiation only when the gain exceeds that cost, so party $p$'s hold-up loss is

$$H_p = \max\left(0,\; \omega\, Q_p - (1 - \omega)\, Q_{-p} - F_{-p}\right)$$

**The bond condition.** Mutual exposure is a bond for party $p$, rather than a liability, when $H_p = 0$:

$$\omega\, Q_p \;\le\; (1 - \omega)\, Q_{-p} + F_{-p}$$

With an even split, $\omega = 0.5$, this reads $Q_p - Q_{-p} \le 2F_{-p}$. It always holds for the party that sank less. So the pair is bonded in both directions when the gap between the two quasi-rents is no larger than twice what forcing a renegotiation would cost the party that sank less. Three things follow.

- **The imbalance creates the hazard, and the level does not.** Raising both quasi-rents together keeps the bond. Raising one alone breaks it once the difference outgrows the other side's future stake. The seller surplus model's rule that the relationship is healthy while the seller's quasi-rent keeps pace with its temptation is this condition read from the buyer's side.
- **The two enforcement remedies act on different terms.** A hostage raises $Q_{-p}$, through a bond or a reciprocal specific investment, or raises $F_{-p}$, through fees staged against delivery or the seller's referenceability. A right allocated in advance changes the renegotiation itself. An option to renew at a preset price or a priced right to stop fixes where it starts, which in this form lowers $\omega$. A discount moves none of the three terms, which is why it does not answer drift.
- **Whoever sinks first is exposed first.** In a forward-deployed motion $Q_s$ rises before $Q_b$, so the seller fails the condition until the buyer's own investment catches up. That is the Constitution's reason to settle the allocation before the seller spends.

**How it enters the conditions.** Hold-up and a failed fit are two ways the return falls short, and hold-up matters only in the states where the fit did not fail anyway. Writing $\pi^{gap}_p$ for section 5.2's form:

$$\pi_p = 1 - \left(1 - \pi^{gap}_p\right)\left(1 - \frac{H_p}{Q_p}\right), \qquad L_p = Q_p\,\pi_p = Q_p\,\pi^{gap}_p + \left(1 - \pi^{gap}_p\right) H_p$$

So $L_p = Q_p \pi_p$ keeps its form and its bound, and $H_p / Q_p$ never exceeds $\omega$. Where the bond condition holds, $H_p = 0$ and $\pi_p$ is the gap form alone, which is what every worked example in the repository assumes.

**The split is a placeholder.** $\omega = 0.5$ is the symmetric split Grossman and Hart (1986) use for the renegotiation, chosen and not fitted, and it describes a renegotiation with nothing allocated in advance. $F_{-p}$ is named and not valued. It is also the variable under the three frequency readings, which [05-governance-forms.md](./05-governance-forms.md) section 1 reads off this condition.

*Falsifier.* Among deals where both parties sink specific investment, forced renegotiations and terminations should track the imbalance between the two quasi-rents against the value left in the relationship, and not the total sunk. If they rise with the total at a fixed imbalance, the condition is wrong.

### 5.6 What to settle in advance, and what to do in advance

Axiom III says a specific deal's allocation must be settled before the investment is sunk, and that the work done in advance can fall as uncertainty rises. This section gives each half a form.

**The allocation required.** An allocation is adequate when, at the moment party $p$ sinks its investment, the other side can take nothing in plain view. The bond covers part of $p$'s quasi-rent through what the other side has sunk and stands to lose (section 5.5). What the bond leaves uncovered has to be settled in advance, by a hostage or by a right:

$$A_p = \max\left(0,\; \omega\, Q_p - (1 - \omega)\, Q_{-p} - F_{-p}\right), \qquad \alpha_p = \frac{A_p}{Q_p}$$

$A_p$ is the hold-up loss $H_p$ read at the moment of sinking. $\alpha_p$ is the share of $p$'s quasi-rent that needs an allocation, and it never exceeds $\omega$.

- **The requirement rises with the imbalance, and not with specificity as such.** At a fixed $Q_{-p}$ and $F_{-p}$, $\alpha_p$ rises with $Q_p$ toward $\omega$, which is the axiom's earlier claim in the case where one party sinks alone. When both sink evenly, $\alpha_p$ falls toward zero and the bond does the work. Constitution 5.1 states the mechanism this way.
- **Staging keeps the requirement small.** Read at each gate on the quasi-rents sunk so far, $A_p$ stays near zero while the two sides' investments grow together, which is what [05-governance-forms.md](./05-governance-forms.md) section 5 means by the two stakes growing together. A gate where one side sinks alone is the gate that needs the allocation.
- **Allocation answers hold-up, and not a failed fit.** The fit term $Q_p \pi^{gap}_p$ is lowered by verification and by staging (section 5.4), and moved by a guarantee.

The [Enforcement Ledger](../../practice/enforcement-ledger.md)'s allocation coverage ratio reads whether an allocation was made. $\alpha_p$ says how much was needed.

**The work done in advance.** Discovery before sinking lowers the gap a party carries into the investment, but only the part discovery can reach. Write $\rho$ for the share of the gap that surfaces only in use. It is near zero where the specification is static and rises with technological and organizational uncertainty (Crocker and Reynolds 1993, Strong and Volkoff 2010). Closing a fraction $x$ of the reachable part lowers the party's mean gap by $x(1 - \rho) g_p$, and its expected loss by $Q_p (1 - \pi_0)(1 - \rho)\, g_p\, x$. If discovery's cost rises with the square of $x$ at a scale $c$, the share of the gap worth closing before sinking is

$$x^* = \min\left(1,\; \frac{Q_p (1 - \pi_0)(1 - \rho)\, g_p}{c}\right), \qquad \sigma_p = (1 - \rho)\, x^*$$

$\sigma_p$ is the share of the gap closed in advance. It rises with $Q_p$, because a larger quasi-rent makes the loss worth more to avoid. It falls with $\rho$, because more of the gap lies beyond discovery's reach and each unit of discovery buys less. The rest is closed after sinking, in stages, which keeps the option to stop that Dixit and Pindyck (1994) price.

**The two halves come apart.** Uncertainty does not enter $\alpha_p$, and $\sigma_p$ falls as $\rho$ rises. So a deal that is specific and uncertain settles more and does less before anything is sunk, which is a minimum viable integration with a staged remainder. Where $\rho$ is near zero both rise with $Q_p$, and front-end definition pays directly (Merrow 2011).

**Placeholders.** The quadratic cost of discovery is chosen. $c$ and $\rho$ are named and not valued. $A_p$ inherits $\omega$ from section 5.5.

### 5.7 Account management is the seller's maintenance

Account management is a seller function and a seller investment, justified by the seller's condition like any other. It is $C_{sustain}$ in [04-seller-surplus-model.md](./04-seller-surplus-model.md) section 7, and what it protects is the seller's margin at the next boundary, its stake $F_s$ from section 5.5. Write its cost as $c_\eta$ per unit of $\eta$ each period, and read the chance the buyer does not renew as rising with the held gap on the form of section 5.2. The seller then funds the rate that maximizes $F_s\left(1 - \pi(\hat{\Delta}^*)\right) - c_\eta \eta$:

$$\eta^* = \sqrt{\frac{(1 - \pi_0)\, F_s\, \gamma}{c_\eta}} - \gamma, \qquad \eta^* > 0 \;\text{ only when }\; (1 - \pi_0)\, F_s > c_\eta\, \gamma$$

- **Below a threshold the seller funds none.** Where the margin at stake does not cover the cost of keeping pace with the rebuild, the account is unmaintained. Pooled or automated customer success below some contract value follows rather than being assumed.
- **With no stake there is no maintenance.** At $F_s = 0$, a one-shot deal by section 1 of [05-governance-forms.md](./05-governance-forms.md), the seller maintains nothing, and the account follows the unmaintained curve.
- **Spend rises slower than the stake.** Here as its square root.
- **Fast drift can make maintenance not worth funding.** $\eta^*$ rises with $\gamma$ and then falls, to zero at $\gamma = (1 - \pi_0) F_s / c_\eta$. With no drift there is nothing to maintain, and with very fast drift no affordable rate holds the gap. Past the peak the seller does better to lower $\gamma$ than to chase it.

The threshold and the zero at no stake follow from any maintenance cost that is positive at the margin. The rise and fall in $\gamma$ follows from the two limits. The square root is illustrative, from the proportional, linear and straight-line forms, and $c_\eta$ is named and not valued.

Fit drift is weighed against the same stake. Re-adaptation and an allocated change process are seller investments when the arrangement puts them on the seller, and the seller funds them while the margin they protect covers them. The account manager holds a decision role inside the seller, so by [05-governance-forms.md](./05-governance-forms.md) section 5 its pay needs a stake at the renewal it maintains. The buyer maintains its own side, the owner of its workflow, out of its own condition, and that is not account management.

### 5.8 Separation in a market

A costly signal $s$ tells a good seller from a bad one when the good seller can afford it and the bad one cannot, against $B$, the premium a seller earns by being told apart from the pool (Spence 1973):

$$c_{good}(s) < B < c_{bad}(s)$$

Separation is a condition a market crosses in both directions, not a resting point.

- **Entry pools.** Entrants copy the signals that automate, which pulls $c_{bad}$ toward $c_{good}$, the first Friction Allocation Principle failing, and the condition fails. This is the Turnkey corollary's route out of the condition.
- **Pooling pays for re-separation.** While the pool holds, buyers judge every seller by the category's average, and misfits discovered after sinking pull that average down further (the cost floor corollary). Both raise $B$, which pays for a costlier signal or a shared institution, a certification, a standard or a staked channel, that restores the condition.
- **Saturation ends it.** When no signal a good seller can afford clears the bad seller's cost, the buyer exits. That is the Akerlof saturation failure mode.

The structure is section 5.3's at the level of a category: entry and misrepresentation rebuild what buyers cannot tell apart, and costly signals and shared institutions hold it down. The two are kept separate on purpose. At the deal level one seller chooses $\eta$. At the market level the shared institutions benefit every seller in the pool, so by the cost floor corollary no one seller funds them at a return its own deals repay, and the category is maintained less than any seller in it would choose.

**The search cost responds to information by its verifiability.** Information the buyer can check narrows its range and lowers $\tilde{n}_{search}$, the demand the buyer expects. Information it cannot check takes attention without narrowing anything and raises it. Only the signs are claimed. This is the second standing assumption's line between evidence and persuasion, read together with the cost floor corollary's message volume.

---

## 6. Thresholds and Positions

Each cost's demand $n_k$ is what the deal asks of the payer who carries it, in the payer's own units. The payer carries up to its capacity $\kappa_k$ alone, and the seller or an outside party can move up to $\bar{A}_k$ off it within the deal:

$$\tau^{self}_k = \kappa_k \qquad \tau^{part}_k = \kappa_k + \bar{A}_k \qquad r_k = \frac{n_k - \tau^{self}_k}{\tau^{part}_k - \tau^{self}_k}$$

The position is the share of the movable demand that has to be moved: self-serve at zero or below, bearable up to one, and above one the buyer is out, since moving everything movable leaves more than the payer can carry.

| Cost | Payer | Demand $n_k$ | Capacity $\kappa_k$ | Movable $\bar{A}_k$ |
|---|---|---|---|---|
| Search | The evaluators | Alternatives to rule out, counting building it and doing nothing | Alternatives the team can take to a written comparison in the decision window | Alternatives an outside comparison the buyer can check rules out |
| Consensus | The sponsor | Decision roles with a veto, plus formal bodies | Roles it can bring to a decision at this contract value without escalating, under the written delegation of authority | Formal bodies a channel or prior clearance satisfies, such as a pre-approved vendor list. A person's veto cannot be moved. |
| Implementation | The technical owners | Integration points | Integration points its staff can build in the delivery window | Points the seller's engineers or an integrator build |
| Implementation | The operating owners | Changed workflows and undocumented exception paths | Changes its people can take on in the window | Exception paths a seller or consultant handles. A changed workflow cannot be moved. |

Assign each cost to a payer before the outcome. Where a cost falls on two payers, read each part against its own and take the larger position.

**What a reading can test.** A capacity read from what the payer can show, its staffing or its written authority, supports the step at one. A capacity read from its record on a comparable purchase, counted net of what outside parties carried, is biased both ways and supports only the graded claim that entry falls as the position rises. Positions on the default edges in [06-calibration.md](./06-calibration.md) section 3.2 are evidence neither way. Read both thresholds of a cost from the same source.

**The buyer reads its own positions.** $\tilde{r}_k$ is the same position read on $\tilde{n}_k$, the demand the buyer expects, and the buyer enters discovery only while every $\tilde{r}_k \le 1$ and every shared payer passes. Before it meets a seller, $\tilde{n}_k$ is the category prior, and only evidence the buyer can check moves it toward $n_k$. The sale starts at the largest $r_k$, the tightest cost, at a stated moment, and before fit is verified the implementation and consensus positions are lower bounds by section 3.5.

**Non-compensation.** Capacity is specific to its payer: knowledge, authority and skill do not move between payers even where nobody bargains over them, and inside one firm capacity moves only by order, which is itself work for the sponsor (Milgrom and Roberts 1988). So ease on one payer never buys back another above its threshold. Costs one payer carries draw on one capacity, and with everything movable moved:

$$\sum_{k \in K_p} \frac{\left(n_k - \bar{A}_k\right)^+}{\kappa_k} \le 1 \qquad \text{for each payer } p \text{ carrying the costs } K_p$$

For one cost this is $r_k \le 1$. That the kinds of work trade against one capacity in a straight line is chosen.

**What the work costs.** In fractions of annual contract value,

$$F_k = c^b_k \left(n_k - a_k\right) + c^s_k \, a_k \qquad 0 \le a_k \le \bar{A}_k$$

where $a_k$ is the demand moved and $c^b_k$ and $c^s_k$ are what a unit of the work costs each side, named and not valued. The two terms are the investments $I^b_k$ and $I^s_k$ in section 1, and what the seller spends showing a cost adds to $I^s_k$. The seller does the work more cheaply where $c^s_k < c^b_k$, and section 3.1's form is $F_{consensus}$ with nothing moved. The gate and the conditions share no quantity, so price never moves a threshold, though it can add demand, as a spend threshold adds an approver, and can make it worth moving more.

A cost keeps a buyer out by either route: its demand passes the participation threshold, which the gate reads, or the work costs more than the deal is worth, which $S_b$ reads. When the US simplified acquisition threshold rose, buyers bunched under it and dropped some purchases above it (Carril 2021), which moved demand and cost together and so does not separate the routes. Bunching that scales with each purchase's surplus would be $S_b$, and bunching that ignores surplus and moves with the contracting office's staffing would be the gate.

*What would falsify the gate.* With capacity read from staffing or written authority, buyers whose demand passes the participation threshold enter as often as matched buyers within it, or deals blocked by one payer past its threshold are rescued by lowering a cost another payer carries. With capacity read from a record, entry does not fall as the position rises.

---

## 7. What Constitution 4.0 retired from this file

Recorded so a reader who meets the old forms in an older analysis knows why they went.

| Form | Why it went |
|---|---|
| The per-component multiplier $F_k(1 + \hat{\Delta}_k)$ and the deal-level gap $\hat{\Delta}_A$ | Capped at doubling a cost, so it could not produce the buyer exit Akerlof describes. Exit is now Axiom I's participation threshold, and uncertainty does its other work through the chance of future loss. |
| The reduced form $y = a\hat{\Delta}_A^2 + c$ | Its convexity came from letting uncertainty raise base cost and then multiply it again. It then dropped the linear term, which is never smaller than the quadratic one on $[0, 1]$. And its $c$ was price, which Axiom I excludes. |
| The coefficient $a = 2.25$ | Borrowed from loss aversion, which produces a kink at the reference point rather than a convex curve. The verification-beats-discounting argument it supported now follows from section 1.3 without it. |
| Linear drift $\hat{\Delta}_k(0) + \gamma_k t$ | Unbounded, so it left the range the gaps are defined on. |
| The summed level $\lVert \mathbf{F} \rVert_1$ and direction shares | Summed and divided scores that were never on a common scale, and the level stood in for specificity. Section 6 replaces both. |

The Deal Triage Calculator was rebuilt on positions and the Milestone Valuation Model on expected loss in the same revision, and none of the retired forms survives in `models/tcg_models.py`.

---

## 8. Parameter Reference

Every parameter in this file, and every threshold and band elsewhere in the framework, lives in [06-calibration.md](./06-calibration.md). It is the single home for them on purpose: two tables of the same values drift, and the separation is what lets the structural claims above be read without any of the numbers.

Nothing in that file is a measurement. Read the provenance column before quoting any value outside this repository.

---

## 9. What Would Make These Models Empirical

Six conditions, in [06-calibration.md](./06-calibration.md) section 4, in rough order of how much each one buys. The first is logging the three gaps separately at open and at every artifact boundary, which is what makes the drift rates estimable.

Until then, treat every output as a structured comparison between deals rather than a quantity. A deal whose future loss reads 0.4 is meaningfully more exposed than one reading 0.1. Neither number predicts a close date.

---

## Related

- [00-tcg-constitution.md](./00-tcg-constitution.md) — The axioms these models serve. Part II carries the two conditions.
- [01-motions.md](./01-motions.md) — Motion selection, which consumes the positions in section 6.
- [04-seller-surplus-model.md](./04-seller-surplus-model.md) — The seller's condition in full, including the repeated game.
- [Enforcement Ledger](../../practice/enforcement-ledger.md) — Field instrument producing the implementation gap.
- [Bargaining Ledger](../../practice/bargaining-ledger.md) — Field instrument producing $F_{consensus}$.
- [Enforcement Ledger](../../practice/enforcement-ledger.md) — Its Stage column applies section 5.4 to gate design.
- [real-options.md](../02-research/real-options.md) — Source for the staging logic.
