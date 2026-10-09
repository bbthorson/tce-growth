#!/usr/bin/env python3
"""Executable forms of the equations the TCG playbook states in LaTeX.

The playbook keeps roughly a dozen formulas in prose. Nothing verified that a
worked example still matched its formula, that weights still summed to 1, or
that a figure still depicted the equation it illustrated. This module is the
single implementation those documents are checked against, the way
RetiredTerms.yml is the single record renames are checked against.

**The documents are the specification.** Where a document and this module
disagree, the document wins and the module is the bug. Every function names its
canonical home in its docstring, and test_tcg_models.py asserts that each worked
example in those documents reproduces here.

CALIBRATION STATUS
------------------
Nothing in this module is fitted. Every parameter default is a reasoned
starting value carried over from the documents, and the documents say so
themselves: 02-mathematical-models.md states the functional forms are
"specified, not fitted" and exist "to structure judgment, not to forecast."

- Constitution 4.0 states the theory as two conditions, one per party, in
  fractions of annual contract value. Its thresholds, the floor on the chance
  of future loss, and the drift rates are named and not valued, so this module
  takes them as arguments rather than shipping defaults.
- The edges the Deal Triage Calculator reads each count against are chosen,
  placed on the boundaries of the score bands earlier versions used. They are
  not measurements.
- beta = 1.35 is chosen inside a motivated range. Only the fact that beta > 1
  carries literature support; the value does not.
- The Friction Efficiency Index weights have no empirical basis at all.
- The seller-surplus forms have no parameter anchored in published literature.

Outputs rank deals against each other. They do not predict a cycle length, a
close date, or a probability. Do not quote any number this module produces as
an empirical estimate.

No dependencies, standard library only, matching the two checkers in
tools/linting/.
"""

import collections
import math

# --------------------------------------------------------------------------
# Parameter defaults.
#
# Provenance for each of these is in the parameter reference tables of
# theory/01-foundation/02-mathematical-models.md section 5 and
# practice/friction-efficiency-index.md.
# Read those columns before quoting any value outside this repository.
# --------------------------------------------------------------------------

ALPHA_COORDINATION = 1.0     # normalizing convention
BETA_COMMITTEE = 1.35        # chosen within [1.2, 2.0]
GAMMA_TECHNICAL_OVERLAP = 0.20   # chosen field refinement
W_TECH, W_PROCESS = 0.6, 0.4     # chosen, sum to 1
PHI_TECH, PHI_PROCESS = 1.2, 1.1  # chosen
MU_RETURN_UNCERTAINTY = 1.0  # normalizing convention
NU_VENDOR_DOUBT = 2.0        # chosen
KAPPA_PROOF_DECAY = 0.5      # chosen
GAMMA_RESPONSIVENESS = 0.5   # chosen

# Raw Bilateral Asymmetry Scorecard range, from
# practice/asymmetry-scorecard.md part 3.
RAW_GAP_MIN, RAW_GAP_MAX = 2.0, 10.0

# Friction Efficiency Index composite weights, in ACR / BCV / RMS / SVI order.
FEI_WEIGHTS = (0.35, 0.25, 0.25, 0.15)
BCV_REF_DEFAULT = 0.5  # convention until twenty closed deals with specific exposure exist


# ==========================================================================
# theory/01-foundation/02-mathematical-models.md section 1.5
# Normalizing the gap before substitution.
# ==========================================================================

class NormalizedGap(float):
    """A Bilateral Asymmetry Gap already mapped onto the [0, 1] scale.

    This type exists to make a documented past bug unrepresentable. The
    Asymmetry Scorecard emits a raw score on [2, 10]. Neither cost equation
    accepts that range: section 1.5 notes that substituting a raw 10 would
    inflate base friction elevenfold, "which no observed deal supports," and
    that confusing the two scales "produces cost estimates off by an order of
    magnitude."

    Because a bare float cannot say which scale it is on, every function here
    that takes a gap accepts only this type. Reach it one of two ways:

    - normalize_gap(raw) for a score straight off the scorecard, or
    - NormalizedGap(x) when you already hold a normalized value and are
      asserting that deliberately.

    Values above 1 are refused. Constitution 4.0 bounds drift at the ceiling,
    and every count-based gap is a share of unevidenced items, which cannot
    exceed all of them. 02-mathematical-models.md section 5.3.
    """

    __slots__ = ()

    def __new__(cls, value):
        value = float(value)
        if value < 0.0:
            raise ValueError(
                "a normalized gap cannot be negative; 0 is complete "
                "informational symmetry (section 2.1)"
            )
        if math.isnan(value) or math.isinf(value):
            raise ValueError("a normalized gap must be finite")
        if value > 1.0:
            raise ValueError(
                "a normalized gap cannot exceed 1; drift relaxes toward the "
                "ceiling and never past it (section 5.3)")
        return super().__new__(cls, value)

    def __repr__(self):
        return "NormalizedGap({:g})".format(float(self))


def normalize_gap(raw_gap):
    """Map a raw scorecard gap on [2, 10] onto [0, 1]. Section 2.5.

        gap_hat = (raw - 2) / 8

    Use the raw score for the scorecard's own field triage bands, and this
    value everywhere else.
    """
    raw_gap = float(raw_gap)
    if not RAW_GAP_MIN <= raw_gap <= RAW_GAP_MAX:
        raise ValueError(
            "raw gap {:g} is outside the scorecard range [{:g}, {:g}]; the "
            "scorecard sums two halves each on [1, 5]".format(
                raw_gap, RAW_GAP_MIN, RAW_GAP_MAX)
        )
    return NormalizedGap((raw_gap - RAW_GAP_MIN) / (RAW_GAP_MAX - RAW_GAP_MIN))


def _require_normalized(gap, caller):
    if not isinstance(gap, NormalizedGap):
        raise TypeError(
            "{} requires a NormalizedGap, not a bare {}. The Asymmetry "
            "Scorecard emits a raw score on [2, 10] and no equation here "
            "accepts that range. Call normalize_gap(raw) first, or wrap an "
            "already-normalized value in NormalizedGap(). See "
            "02-mathematical-models.md section 2.5.".format(
                caller, type(gap).__name__)
        )
    return float(gap)


COMPONENTS = ("search", "consensus", "implementation")


# ==========================================================================
# theory/01-foundation/02-mathematical-models.md section 2.4
# ==========================================================================

def component_gap(n_items, n_evidenced):
    """A one-sided component gap, 02-mathematical-models.md section 2.4.

        gap_k = 1 - evidenced / in_scope

    Used for the search and consensus components, whose pairs have no seller
    side and whose instruments emit counts rather than ratings. The result
    lands on [0, 1] with a true zero, so it needs no rescaling.

    An instrument that put no items in scope leaves the gap undefined rather
    than zero. Nothing evidenced out of nothing counted is not symmetry.
    """
    n_items, n_evidenced = int(n_items), int(n_evidenced)
    if n_items < 0 or n_evidenced < 0:
        raise ValueError("counts cannot be negative")
    if n_evidenced > n_items:
        raise ValueError(
            "{} items carry evidence but only {} are in scope".format(
                n_evidenced, n_items))
    if n_items == 0:
        raise ValueError(
            "no items in scope, so this component's gap is undefined; "
            "section 2.4 refuses to read that as symmetry")
    return NormalizedGap(1.0 - float(n_evidenced) / n_items)


# ==========================================================================
# theory/01-foundation/02-mathematical-models.md section 2
# The Bilateral Asymmetry Gap.
# ==========================================================================

def dimension_score(items_in_scope, items_evidenced):
    """One scorecard dimension, from a pair of counts. Scorecard v3.0.

        f = 1 - evidenced / in_scope,  score = 1 + 4f

    The unevidenced fraction mapped onto the 1-to-5 scale the card has always
    presented, so the bands and the normalization are unchanged while the
    underlying measurement becomes a count. Fully evidenced scores 1 and fully
    unevidenced scores 5, which is what the retired rubric's endpoints meant.

    A dimension with nothing in scope raises rather than returning 1. Nothing
    evidenced out of nothing counted is not the same finding as everything
    evidenced, and the card says to leave it blank.
    """
    return 1.0 + 4.0 * float(component_gap(items_in_scope, items_evidenced))


def asymmetry_gap(i_seller, i_buyer):
    """Section 2.1.

        gap = I_seller + I_buyer

    A sum, not a difference. A deal where both sides are equally blind is not
    symmetric in any useful sense; it is maximally uninformed on both sides.
    The Asymmetry Scorecard carries a note recording that an earlier version
    computed a difference and scored exactly that deal as forecastable.

    Returns a raw quantity on whatever scale the two halves were measured on.
    Pass it through normalize_gap before either cost equation.
    """
    if i_seller < 0 or i_buyer < 0:
        raise ValueError("neither half of the gap can be negative")
    return i_seller + i_buyer


def seller_ignorance(u_tech, u_process, w_tech=W_TECH, w_process=W_PROCESS,
                     phi_tech=PHI_TECH, phi_process=PHI_PROCESS):
    """Section 2.2.

        I_seller = w_t * U_tech^phi_t + w_p * U_process^phi_p

    What the seller has not yet mapped about the buyer's architecture and
    operations, with both inputs on [0, 10]. Because both exponents are at
    least 1 the function is convex: unmapped technical complexity generates
    accelerating discovery risk rather than proportional discovery risk. The
    Blueprint targets this term.

    Note this is NOT the same quantity as the Asymmetry Scorecard's I_seller,
    which is the mean of four dimensions each scored 1 to 5 and therefore lands
    on [1, 5]. This form ranges to about 14.6 on its stated inputs. See the
    discrepancy note in models/README.md.
    """
    for name, value in (("u_tech", u_tech), ("u_process", u_process)):
        if not 0.0 <= value <= 10.0:
            raise ValueError("{} must lie on [0, 10]".format(name))
    if abs((w_tech + w_process) - 1.0) > 1e-9:
        raise ValueError("w_tech and w_process must sum to 1")
    if phi_tech < 1 or phi_process < 1:
        raise ValueError("acceleration exponents must be at least 1")
    return w_tech * u_tech ** phi_tech + w_process * u_process ** phi_process


def buyer_uncertainty(cv_roi, k_vendor, mu=MU_RETURN_UNCERTAINTY,
                      nu=NU_VENDOR_DOUBT, kappa=KAPPA_PROOF_DECAY):
    """Section 2.3.

        I_buyer = mu * (sigma_ROI / R_bar) + nu * exp(-kappa * K_vendor)

    Doubt about return variance and vendor capability. Proof reduces doubt with
    diminishing returns, and as proof accumulates the term approaches a floor
    of mu * cv_roi set by return variance alone.

    That floor is the model's most useful field implication: no quantity of
    costly signaling drives buyer uncertainty to zero while the return itself
    remains volatile. Past a point the seller stops investing in proof and
    starts working on the variance of the projected return. The Red Team
    targets K_vendor; the MIP targets sigma_ROI by bounding downside through
    staged gates.
    """
    if cv_roi < 0:
        raise ValueError("a coefficient of variation cannot be negative")
    if not 0.0 <= k_vendor <= 10.0:
        raise ValueError("k_vendor must lie on [0, 10]")
    if mu <= 0 or nu <= 0 or kappa <= 0:
        raise ValueError("mu, nu and kappa must all be positive")
    return mu * cv_roi + nu * math.exp(-kappa * k_vendor)


def buyer_uncertainty_floor(cv_roi, mu=MU_RETURN_UNCERTAINTY):
    """The limit of buyer_uncertainty as vendor proof grows without bound."""
    if cv_roi < 0:
        raise ValueError("a coefficient of variation cannot be negative")
    return mu * cv_roi


# ==========================================================================
# theory/01-foundation/02-mathematical-models.md section 3
# practice/consensus-friction-calculator.md
# Consensus friction.
# ==========================================================================

def incentive_variance(scores):
    """Section 3.2, and the calculator's input 2.

        I_bar = mean(I_i)      Var = mean((I_i - I_bar)^2)

    Population variance, not the sample form. Each I_i is the stakeholder's
    utility from the initiative on [-1, 1], scored from the objectives they are
    measured on rather than the position they stated in a room containing the
    others. Stated positions converge under social pressure and measured
    objectives do not, so scoring from the meeting understates this term, and
    it understates it most in the polarized committees where it matters most.

    Bounded above by 1 because the scores are bounded on [-1, 1]. A computed
    value above 1 indicates an arithmetic error, not an unusually divided
    committee.
    """
    scores = list(scores)
    if not scores:
        raise ValueError("a committee needs at least one stakeholder")
    for s in scores:
        if not -1.0 <= s <= 1.0:
            raise ValueError(
                "stakeholder alignment {:g} is outside [-1, 1]".format(s))
    mean = sum(scores) / len(scores)
    return sum((s - mean) ** 2 for s in scores) / len(scores)


def consensus_friction(n, var_i, alpha=ALPHA_COORDINATION,
                       beta=BETA_COMMITTEE):
    """Two-term core form, section 3.1.

        F_consensus = alpha * N^beta * (1 + Var(I_i))

    N counts stakeholders holding veto power or direct evaluation
    responsibility. Title does not matter; veto power does. beta > 1 reflects
    communication channels growing as N(N-1)/2 rather than as N, so adding the
    sixth stakeholder costs more than adding the second.

    When every stakeholder holds identical alignment the variance term
    vanishes and friction reduces to the structural floor alpha * N^beta. Size
    alone imposes cost even under perfect agreement.

    Section 3.4 calls this two-term form "what the axioms require."
    """
    if n < 1:
        raise ValueError("committee size must be at least 1")
    if not 0.0 <= var_i <= 1.0:
        raise ValueError(
            "incentive variance {:g} is outside [0, 1]; a value above 1 "
            "indicates an arithmetic error".format(var_i))
    if alpha <= 0:
        raise ValueError("alpha must be positive")
    if beta < 1.2 or beta > 2.0:
        raise ValueError("beta is documented on [1.2, 2.0]")
    return alpha * n ** beta * (1.0 + var_i)


def consensus_friction_field(n, var_i, technical_overlap,
                             alpha=ALPHA_COORDINATION, beta=BETA_COMMITTEE,
                             gamma_to=GAMMA_TECHNICAL_OVERLAP):
    """Three-term field form, section 3.4 and the calculator's main equation.

        F_consensus = alpha * N^beta * (1 + Var) * (1 + gamma_TO * TO)

    TO on [1, 5] scores architectural alignment among technical evaluators.
    The term exists because incentive variance under-captures a specific and
    common failure: two architects can both want the project to succeed, score
    identically on incentive alignment, and still deadlock on hosting model.
    Treating technical philosophy conflict as incentive conflict causes the
    model to score fractured engineering organizations as low-friction.

    Section 3.4 is explicit that this is a field refinement rather than core
    theory. The two-term form above is what the axioms require.
    """
    if not 1.0 <= technical_overlap <= 5.0:
        raise ValueError("technical overlap is scored on [1, 5]")
    if gamma_to < 0:
        raise ValueError("gamma_TO cannot be negative")
    core = consensus_friction(n, var_i, alpha=alpha, beta=beta)
    return core * (1.0 + gamma_to * technical_overlap)


def consensus_band(f_consensus):
    """Risk band from the calculator's table: low, medium or high."""
    if f_consensus < 0:
        raise ValueError("consensus friction cannot be negative")
    if f_consensus < 10.0:
        return "low"
    if f_consensus <= 25.0:
        return "medium"
    return "high"


def consensus_sensitivity_to_variance(n, alpha=ALPHA_COORDINATION,
                                      beta=BETA_COMMITTEE):
    """Section 3.3.

        d F_consensus / d Var = alpha * N^beta

    The return on reducing misalignment scales with N^beta. In a committee of
    three, aligning incentives produces a modest gain. In a committee of ten it
    produces the largest single reduction available to the seller, which is the
    quantitative case for running the Red Team on large committees
    specifically, and why the calculator escalates to executive sponsorship
    above a threshold rather than recommending more meetings.
    """
    if n < 1:
        raise ValueError("committee size must be at least 1")
    return alpha * n ** beta


# ==========================================================================
# theory/01-foundation/02-mathematical-models.md section 4
# Urgency decay.
# ==========================================================================

def decay_rate(lambda_inertia, e_external, gamma_r=GAMMA_RESPONSIVENESS):
    """Section 4.2.

        delta = lambda_inertia / (1 + gamma_r * E_external)

    With no external catalyst, decay runs at the full rate of organizational
    inertia. With an overwhelming catalyst it approaches zero and perceived
    value holds.

    The seller cannot change the buyer's inertia. The seller can find, name and
    quantify an external catalyst the buyer has not yet connected to this
    decision, which is the only term here a seller can move, and why the
    Blueprint asks for the economic event by name.

    gamma_r is the responsiveness factor and is distinct from gamma in the
    asymmetry drift equation. The glossary keeps them separate by subscript.
    """
    if not 0.1 <= lambda_inertia <= 2.0:
        raise ValueError("organizational inertia is documented on [0.1, 2.0]")
    if not 0.0 <= e_external <= 10.0:
        raise ValueError("external catalyst magnitude is documented on [0, 10]")
    if not 0.1 <= gamma_r <= 1.0:
        raise ValueError("responsiveness is documented on [0.1, 1.0]")
    return lambda_inertia / (1.0 + gamma_r * e_external)


def value_decay(v0, delta, t):
    """Section 4.1, and the value-decay standing assumption.

        V_effective(t) = V_0 * exp(-delta * t)

    v0 is peak perceived value at the triggering event and t is elapsed months.
    As V decays the buyer's relative preference shifts back toward the next
    best alternative, including building it themselves.
    """
    if delta < 0:
        raise ValueError("the decay rate cannot be negative")
    if t < 0:
        raise ValueError("elapsed time cannot be negative")
    return v0 * math.exp(-delta * t)


def asymmetry_drift(gap0, gamma, t):
    """Drift toward the ceiling, 02-mathematical-models.md section 5.3.

        gap_hat(t) = 1 - (1 - gap_hat(0)) * exp(-gamma * t)

    Absent maintenance each gap relaxes toward its ceiling and never past it.
    Post-close, section 7.2 of 04-seller-surplus-model.md reads the same
    equation as the erosion of an incumbent's information advantage, and Net
    Revenue Retention is that document's phrase for it run past signature.

    gamma cannot be negative. Discovery is a separate, discrete step down that
    someone pays for, not drift running backwards.
    """
    gap0 = _require_normalized(gap0, "asymmetry_drift")
    if gamma < 0:
        raise ValueError(
            "gamma cannot be negative; discovery is a separate step down, and "
            "maintenance holds gamma down rather than reversing it")
    if t < 0:
        raise ValueError("elapsed time cannot be negative")
    return NormalizedGap(1.0 - (1.0 - gap0) * math.exp(-gamma * t))


# ==========================================================================
# theory/01-foundation/02-mathematical-models.md sections 1, 5 and 6.
# The two conditions, future loss, and each cost's position between its own
# thresholds. Every term is a fraction of annual contract value, and every
# threshold and floor is an argument because the theory names them without
# valuing them.
# ==========================================================================

def switching_value(v_effective, v_next_best):
    """V_switch(t), section 1.1: the buyer's opportunity cost of staying put.

        V_switch(t) = V_solution * exp(-delta * t) - V_next_best

    Pass value_decay(...) as v_effective. V_next_best includes building it.
    """
    return v_effective - v_next_best


def _total(investments, who):
    values = tuple(investments)
    for value in values:
        if value < 0:
            raise ValueError("{} investment cannot be negative".format(who))
    return sum(values)


def _require_loss(loss, who):
    if loss < 0:
        raise ValueError("{} future loss cannot be negative".format(who))
    return loss


def buyer_condition(v_switch, price, buyer_investments, buyer_loss):
    """The buyer's condition, Constitution Part III and section 1.1.

        S_b = V_switch(t) - P - sum_k I_b,k - L_b

    buyer_investments is what the buyer invests today against each cost.
    """
    return (v_switch - price - _total(buyer_investments, "buyer")
            - _require_loss(buyer_loss, "buyer"))


def seller_condition(price, c_deliver, seller_investments, seller_loss):
    """The seller's condition, Constitution Part III and section 1.1.

        S_s = P - C_deliver - sum_k I_s,k - L_s

    04-seller-surplus-model.md section 2 with the investment split by the cost
    it pays down and the future loss written out.
    """
    return (price - c_deliver - _total(seller_investments, "seller")
            - _require_loss(seller_loss, "seller"))


def joint_surplus(v_switch, c_deliver, buyer_investments, seller_investments,
                  buyer_loss, seller_loss):
    """The two conditions added, section 1.3. Price does not appear.

        S_b + S_s = V_switch - C_deliver - sum_k (I_b,k + I_s,k) - L_b - L_s

    Price is a transfer. A discount moves the split and leaves this unchanged,
    which is the accounting behind the three levers.
    """
    return (v_switch - c_deliver
            - _total(buyer_investments, "buyer")
            - _total(seller_investments, "seller")
            - _require_loss(buyer_loss, "buyer")
            - _require_loss(seller_loss, "seller"))


def investment_shift_gain(work_moved, buyer_unit_cost, seller_unit_cost,
                          change_in_buyer_loss=0.0, change_in_seller_loss=0.0):
    """Change in joint surplus from moving work buyer to seller, section 1.4.

        d(S_b + S_s) = w (theta_b - theta_s) - dL_b - dL_s

    Zero when unit costs match and no future loss moves: the move then only
    changes the split. A forward-deployed engineer moves all three terms.
    """
    if work_moved < 0:
        raise ValueError("work moved cannot be negative; swap the parties")
    if buyer_unit_cost < 0 or seller_unit_cost < 0:
        raise ValueError("unit costs cannot be negative")
    return (work_moved * (buyer_unit_cost - seller_unit_cost)
            - change_in_buyer_loss - change_in_seller_loss)


def loss_chance(gaps, floor):
    """The chance a party's exposure does not come back, section 5.2.

        pi = floor + (1 - floor) * mean(gaps)

    A placeholder. The straight line and the mean are chosen, and no curvature
    is claimed. The floor is named and not valued in 06-calibration.md, so the
    caller supplies it. gaps are the normalized gaps the party cannot close:
    for the buyer, its half of the implementation gap and the bargaining gap.
    """
    gaps = [_require_normalized(g, "loss_chance") for g in gaps]
    if not gaps:
        raise ValueError("a party with no gaps in scope has no loss chance")
    if not 0.0 <= floor < 1.0:
        raise ValueError("the floor lies on [0, 1)")
    return floor + (1.0 - floor) * sum(gaps) / len(gaps)


def future_loss(quasi_rent_value, chance):
    """Expected future loss, Constitution Axiom III and section 5.1.

        L_p = Q_p * pi_p

    A shortfall in the return the party expected, bounded by its quasi-rent.
    Not a second charge for the investment Axiom II already counted.
    """
    if quasi_rent_value < 0:
        raise ValueError("a quasi-rent cannot be negative")
    if not 0.0 <= chance <= 1.0:
        raise ValueError("a chance lies on [0, 1]")
    return quasi_rent_value * chance


def staged_loss(stage_quasi_rents, stage_residuals, floor):
    """Expected loss across gates, section 5.4.

        L_b = sum_m Q_m * pi(x_m)

    Each gate sinks Q_m against the residual uncertainty x_m entering it, so a
    schedule that puts the large commitments late loses less than committing
    everything against x_0.
    """
    quasi_rents = tuple(stage_quasi_rents)
    residuals = tuple(stage_residuals)
    if len(quasi_rents) != len(residuals):
        raise ValueError("one quasi-rent per gate, one residual per gate")
    return sum(future_loss(q, loss_chance([x], floor))
               for q, x in zip(quasi_rents, residuals))


SELF_SERVE = "self-serve"
NEEDS_INVESTMENT = "needs investment"
KEEPS_BUYER_OUT = "keeps the buyer out"


def threshold_position(cost, tau_self, tau_part):
    """A cost's position between its own two thresholds, section 6.

        r_k = (F_k - tau_self) / (tau_part - tau_self)

    Dimensionless, so the three costs compare without sharing a scale. Both
    thresholds are named and not valued in the theory.
    """
    if not tau_part > tau_self:
        raise ValueError(
            "the participation threshold must sit above the self-serve one")
    return (cost - tau_self) / (tau_part - tau_self)


def cost_zone(position):
    """The zone a position falls in, section 6."""
    if position <= 0.0:
        return SELF_SERVE
    if position <= 1.0:
        return NEEDS_INVESTMENT
    return KEEPS_BUYER_OUT


def participates(positions):
    """Axiom I's gate: no cost keeps the buyer out. positions maps cost to r_k."""
    if not positions:
        raise ValueError("no costs read")
    return all(r <= 1.0 for r in positions.values())


def sale_start(positions):
    """Where the sale starts, Axiom I: the cost with the largest position.

    Returns a tuple, because two costs at the same position are run together
    rather than one being picked. positions maps cost name to r_k.
    """
    if not positions:
        raise ValueError("no costs read")
    top = max(positions.values())
    return tuple(sorted(k for k, r in positions.items() if r == top))


# ==========================================================================
# practice/friction-efficiency-index.md
# Retrospective execution metrics. Every threshold, weight and coefficient on
# that page is a reasoned starting value; none is fitted to booked deal data.
# ==========================================================================

def allocation_coverage_ratio(n_allocated, n_exposure):
    """ACR, section 1. The index's target.

        ACR = n_allocated / n_exposure

    n_exposure is the deal's exposure count from the Deal Triage Calculator,
    re-taken at the Adoption Review. n_allocated counts the items whose work
    began only after a written allocation covered them, naming who bears the
    item's adaptation risk, the gate it sits behind and a right to stop there.

    Higher is better and there is no band: Axiom III asks that nothing
    specific be sunk before someone agreed who carries it. Undefined when
    nothing specific was sunk, because such a deal has nothing to allocate
    and sits outside the cohort the index reads.
    """
    if n_allocated < 0 or n_exposure < 0:
        raise ValueError("counts cannot be negative")
    if n_allocated > n_exposure:
        raise ValueError(
            "{} items allocated but only {} specific items were sunk".format(
                n_allocated, n_exposure))
    if n_exposure == 0:
        raise ValueError(
            "nothing specific was sunk, so there is nothing to allocate and "
            "the deal sits outside the cohort this index reads")
    return n_allocated / n_exposure


def friction_allocation_ratio(h_pre, h_post):
    """FAR, section 1.1. Descriptive, with no target and no weight.

        FAR = H_pre / (H_pre + H_post)

    The share of total implementation effort spent before signature. It says
    where the effort went. Constitution 3.0 established that what must come
    before the investment is sunk is the allocation, not the work, so a target
    on this ratio rewarded forcing discovery that only use can do, and the
    composite no longer carries it.

    FAR is blind to scale. An engagement spending 10 pre-sale and 5 post-sale
    hours scores identically to one spending 1,000 and 500, so always report it
    alongside the total.
    """
    if h_pre < 0 or h_post < 0:
        raise ValueError("logged hours cannot be negative")
    total = h_pre + h_post
    if total == 0:
        raise ValueError("FAR is undefined with no logged hours")
    return h_pre / total


def buyer_commitment_velocity(s_dept, d_prov, n):
    """BCV, section 2.

        BCV = S_dept / ((D_prov + 1) * N^0.5)

    How quickly the buyer mobilizes internal resources once asked. S_dept
    counts departments that supplied a named participant, D_prov is calendar
    days from request to first delivered artifact or confirmed attendee, and N
    is total committee size.

    The N^0.5 denominator is a correction rather than decoration. The canvas
    form was S_dept / (D_prov + 1), which rewards engaging more departments and
    so inverts Axiom III: the consensus model treats stakeholder count as a cost
    driver. Uncorrected, an organization could raise its score by dragging more
    people into rooms, which the Consensus Friction Calculator correctly scores
    as worse.

    The +1 guards against division by zero on same-day response. It is a
    convention, not a modelled quantity.
    """
    if s_dept < 0:
        raise ValueError("department count cannot be negative")
    if d_prov < 0:
        raise ValueError("provisioning days cannot be negative")
    if n < 1:
        raise ValueError("committee size must be at least 1")
    return s_dept / ((d_prov + 1.0) * math.sqrt(n))


def risk_mitigation_score(n_identified, n_unresolved):
    """RMS, section 3.

        RMS = 1 - N_unresolved / N_identified

    The share of discovered edge cases closed before signature.

    This form corrects an arithmetic error the document records. The canvas
    version read N_edge / (N_edge + N_unresolved), which double-counts, because
    unresolved cases are a subset of identified cases and so appear in both
    numerator and denominator. A Red Team that identified ten edge cases and
    resolved none scored 10/20 = 0.50 under that form, reporting half the risk
    mitigated when in fact none was. This form returns 0.

    RMS rewards shallow discovery and must never be read alone. A workshop
    surfacing two edge cases and closing both scores 1.00; one surfacing forty
    and closing thirty-five scores 0.875. The lazier workshop wins. Report
    n_identified next to the score every time and treat a low count as the
    finding: below roughly eight on a deal with specific exposure the workshop did
    not do its job, and the score carries no information however high it is.
    """
    if n_identified < 0 or n_unresolved < 0:
        raise ValueError("edge case counts cannot be negative")
    if n_unresolved > n_identified:
        raise ValueError(
            "unresolved edge cases are a subset of identified ones, so "
            "{} unresolved of {} identified is impossible".format(
                n_unresolved, n_identified))
    if n_identified == 0:
        raise ValueError(
            "RMS is undefined when nothing was identified; a Red Team that "
            "surfaced no edge cases is the finding, not a score of 1.0")
    return 1.0 - n_unresolved / n_identified


MIN_CREDIBLE_EDGE_CASES = 8


def rms_is_credible(n_identified):
    """Whether the edge-case count clears the shallow-Red-Team heuristic."""
    return n_identified >= MIN_CREDIBLE_EDGE_CASES


def scope_variance_index(t_actual, t_scoped, c_orders):
    """SVI, section 4. Lower is better.

        SVI = |T_actual - T_scoped| / T_scoped + 0.25 * C_orders

    The absolute value penalizes early delivery as heavily as late delivery,
    which is deliberate: finishing in half the scoped time means the estimate
    was wrong, and a wrong estimate on the optimistic side produces the same
    buyer-facing credibility loss as one on the pessimistic side.

    The 0.25 coefficient on change orders is chosen with no source. It encodes
    a judgment that one change order is worth about as much scope instability
    as a 25 percent schedule miss.
    """
    if t_scoped <= 0:
        raise ValueError("scoped duration must be positive")
    if t_actual < 0:
        raise ValueError("actual duration cannot be negative")
    if c_orders < 0:
        raise ValueError("change order count cannot be negative")
    return abs(t_actual - t_scoped) / t_scoped + 0.25 * c_orders


def normalize_bcv(bcv, bcv_ref=BCV_REF_DEFAULT):
    """Section 5. BCV_hat = min(BCV / BCV_ref, 1).

    BCV_ref is the trailing median across your last twenty closed deals
    with specific exposure. Until twenty exist, the default of 0.5 applies and every reported
    figure is marked provisional.
    """
    if bcv < 0:
        raise ValueError("BCV cannot be negative")
    if bcv_ref <= 0:
        raise ValueError("the BCV reference must be positive")
    return min(bcv / bcv_ref, 1.0)


def normalize_svi(svi):
    """Section 5. SVI_hat = min(SVI, 1).

    SVI caps at 1 because a 100 percent schedule overrun is already a total
    scoping failure, and allowing the term to run higher would let one
    catastrophic project dominate a cohort average.
    """
    if svi < 0:
        raise ValueError("SVI cannot be negative")
    return min(svi, 1.0)


def friction_efficiency_index(acr, bcv, rms, svi, bcv_ref=BCV_REF_DEFAULT):
    """The composite, section 5.

        FEI = 100 * (0.35*ACR + 0.25*BCV_hat + 0.25*RMS + 0.15*(1 - SVI_hat))

    The weights sum to 1.00 by construction, so the index is bounded on
    [0, 100] once both normalizations are applied. They have no empirical
    basis: the parameter reference states the split is chosen. ACR inherited
    the weight the effort ratio carried.

    Read the four components before the composite. Any weighted index can hide
    an offsetting pair, and the common one here is a high ACR carrying a low
    RMS: every gate written down and the workshop still shallow.
    """
    if not 0.0 <= acr <= 1.0:
        raise ValueError("ACR is a ratio on [0, 1]")
    if not 0.0 <= rms <= 1.0:
        raise ValueError("RMS is bounded on [0, 1]")
    w_acr, w_bcv, w_rms, w_svi = FEI_WEIGHTS
    return 100.0 * (
        w_acr * acr
        + w_bcv * normalize_bcv(bcv, bcv_ref)
        + w_rms * rms
        + w_svi * (1.0 - normalize_svi(svi))
    )


def fei_band(fei):
    """Reading from the composite table: allocated, mixed or late."""
    if not 0.0 <= fei <= 100.0:
        raise ValueError("FEI is bounded on [0, 100]")
    if fei > 75.0:
        return "allocated"
    if fei >= 50.0:
        return "mixed"
    return "late"


# ==========================================================================
# practice/milestone-valuation-model.md
# ==========================================================================

def residual_uncertainty(x0, mus):
    """The uncertainty decay chain.

        x_m = x_0 * product over k=1..m of (1 - mu_k)

    Each mu_k applies to what remains rather than to the original gap, which is
    why the reference table's residual compounds downward rather than stepping
    linearly. x_0 is the normalized IMPLEMENTATION gap from the Asymmetry
    Scorecard, not a mean of the three gaps: the gates resolve
    implementation uncertainty specifically.

    A gate written so loosely that no outcome fails it resolves no uncertainty,
    so its mu is effectively zero regardless of what the plan claims.
    """
    x0_f = _require_normalized(x0, "residual_uncertainty")
    x = x0_f
    for i, mu in enumerate(mus, start=1):
        if not 0.0 <= mu <= 1.0:
            raise ValueError(
                "stage {} resolves a fraction of remaining uncertainty, so "
                "mu must lie on [0, 1], not {:g}".format(i, mu))
        x *= (1.0 - mu)
    return NormalizedGap(x)


def residual_schedule(x0, mus):
    """Residual uncertainty entering each stage, as a list.

    Element 0 is x_0 itself, element m is the residual after stage m has
    cleared. Reproduces the reference stage structure table.
    """
    x0_f = _require_normalized(x0, "residual_schedule")
    out = [NormalizedGap(x0_f)]
    running = x0_f
    for i, mu in enumerate(mus, start=1):
        if not 0.0 <= mu <= 1.0:
            raise ValueError(
                "stage {} mu must lie on [0, 1], not {:g}".format(i, mu))
        running *= (1.0 - mu)
        out.append(NormalizedGap(running))
    return out


def stage_surplus(v_gross_m, c_m, q_m, x_m, floor, payment_follows_proof=True):
    """The stage equation, on expected loss.

        S_m = (1 - pi_m)(V_gross,m - c_m) - pi_m * Q_m
        pi_m = floor + (1 - floor) * x_m

    The Constitution's future loss L = Q * pi, read one gate at a time.
    V_gross,m is the value realized on completing the stage, c_m the payment
    allocated to it, Q_m what the buyer sinks at this stage and cannot recover
    if it fails, and x_m the residual uncertainty entering it.

    With payment_follows_proof, the payment is made only when the stage's
    acceptance criteria are met, which is the model's second design rule. A
    calendar-triggered payment is made either way, and the stage surplus falls
    by pi_m * c_m.

    UNITS. Every term is a fraction of annual contract value. The floor is
    named and not valued, so the caller supplies it.
    """
    pi_m = loss_chance([x_m], floor)
    if q_m < 0:
        raise ValueError("what a stage sinks cannot be negative")
    if payment_follows_proof:
        return (1.0 - pi_m) * (v_gross_m - c_m) - pi_m * q_m
    return (1.0 - pi_m) * v_gross_m - c_m - pi_m * q_m


# ==========================================================================
# theory/01-foundation/04-seller-surplus-model.md
# Nothing in this section is fitted, and section 6 says so in stronger terms
# than 02-mathematical-models.md: this model has no parameter anchored in
# published literature at all.
# ==========================================================================

def seller_surplus(p_close, v_contract, c_deliver, c_invest):
    """Section 2.

        S_seller = p_close * (V_contract - C_deliver) - C_invest

    The asymmetry sits in the last two terms. C_deliver is contingent, incurred
    only against revenue. C_invest is not: it leaves the building before anyone
    signs, and it leaves whether p_close resolves to one or to zero.

    Both parties face a boundary and both must clear it. The Constitution's
    S > 0 governs whether the buyer will transact. This one governs whether the
    seller should want them to. A deal sitting comfortably inside the buyer's
    potential well can sit outside the seller's, and the seller who closes it
    has done accretive work for the customer and dilutive work for their own
    firm.

    p_close is not directly observable. Section 6 is explicit that producing a
    number and calling it a probability is not a use this model supports.
    """
    if not 0.0 <= p_close <= 1.0:
        raise ValueError("p_close is a probability on [0, 1]")
    if c_invest < 0:
        raise ValueError("pre-signature investment cannot be negative")
    return p_close * (v_contract - c_deliver) - c_invest


def quasi_rent(c_invest, r_redeploy):
    """Section 3.

        Q = C_invest - R_redeploy

    C_invest overstates the exposure. The correct measure is the appropriable
    quasi-rent, where R_redeploy is the value of that work redeployed
    elsewhere: reusable connectors, a reference architecture, domain knowledge
    that transfers to the next deal in the segment.

    Q is what a buyer can extract by threatening to walk after the engineering
    is spent, and it is the number that belongs in a risk review. Two
    engagements consuming identical hours carry different exposure when one
    produces a connector the seller ships to every subsequent customer and the
    other produces a mapping to a schema that exists in exactly one hospital.

    R_redeploy has no scoring method anywhere in this repository. It is a
    caller-supplied input on purpose: inventing a rubric here would put a
    number into a risk review that no document backs. It is listed as an open
    question in section 8 of that document and in models/README.md.
    """
    if c_invest < 0:
        raise ValueError("pre-signature investment cannot be negative")
    if r_redeploy < 0:
        raise ValueError("redeployable value cannot be negative")
    if r_redeploy > c_invest:
        raise ValueError(
            "redeployable value cannot exceed the investment that produced "
            "it; Q is what remains unprotected, and it floors at zero")
    return c_invest - r_redeploy


def marginal_investment_rule(dp_close_dc_invest, v_contract, c_deliver):
    """Section 4, evaluated.

        (d p_close / d C_invest) * (V_contract - C_deliver) > 1

    Spend the next increment while a unit of pre-signature engineering raises
    the close probability enough that the expected gross margin gain exceeds
    the unit spent. Stop when it does not.

    **This function cannot be evaluated from anything in this repository.**
    The derivative is not observable and no record of scored deals exists. The
    caller must supply it, and supplying a guess produces a guess. Prefer
    required_marginal_close_gain below, which is the direction section 6
    actually endorses.
    """
    return dp_close_dc_invest * (v_contract - c_deliver) > 1.0


def required_marginal_close_gain(v_contract, c_deliver):
    """Section 4, inverted into the question a manager can actually ask.

        d p_close / d C_invest > 1 / (V_contract - C_deliver)

    Section 6 names this as the model's real use: "a manager can use section 4
    to ask what would have to be true about d p_close / d C_invest for this
    spend to make sense, and can compare that answer against experience."

    Returns the threshold the derivative must clear, in close-probability per
    unit of currency invested. It asserts nothing about whether a given deal
    clears it, which is the point. Producing a number and calling it a
    probability is what section 6 rules out.
    """
    margin = v_contract - c_deliver
    if margin <= 0:
        raise ValueError(
            "gross margin is not positive, so no pre-signature investment "
            "can satisfy the marginal rule at any derivative")
    return 1.0 / margin


def repeated_seller_surplus(r, v, c_deliver, c_sustain, rho, c_invest):
    """Section 7, the repeated game.

        S_seller = sum over t of r_t (V_t - C_deliver,t - C_sustain,t)
                   / (1+rho)^t   -   C_invest

    Subscription businesses do not have single transactions. r_t is the
    probability the relationship is live in period t, with r_1 equal to
    p_close. C_sustain is the ongoing relationship investment that holds the
    asymmetry drift rate gamma down, and section 7.2 argues it is not overhead:
    it is what defends the incumbent's information advantage, which is the
    durable asset rather than lock-in.

    The single-shot form of section 2 is this expression with T = 1 and
    C_sustain = 0. test_tcg_models.py asserts that identity.

    rho is a policy choice rather than a measurement, and r_t is no better
    observed than p_close.
    """
    lengths = {len(r), len(v), len(c_deliver), len(c_sustain)}
    if len(lengths) != 1:
        raise ValueError(
            "r, v, c_deliver and c_sustain must cover the same periods")
    if rho < 0:
        raise ValueError("the discount rate cannot be negative")
    if c_invest < 0:
        raise ValueError("pre-signature investment cannot be negative")
    total = 0.0
    for t, (r_t, v_t, cd_t, cs_t) in enumerate(
            zip(r, v, c_deliver, c_sustain), start=1):
        if not 0.0 <= r_t <= 1.0:
            raise ValueError(
                "the survival probability in period {} is not on "
                "[0, 1]".format(t))
        total += r_t * (v_t - cd_t - cs_t) / (1.0 + rho) ** t
    return total - c_invest


def cooperation_threshold(temptation, reward, punishment):
    """Axiom II's cooperation condition.

        delta_discount > (T - R) / (T - P)

    Returns the threshold the party's discount factor must exceed. Section 7.1
    of the seller model uses it to argue that lock-in is a liability: raising
    the buyer's switching cost raises the seller's temptation payoff T, which
    raises this threshold, so the arrangement becomes harder to sustain exactly
    as the seller's position strengthens.
    """
    if not punishment < reward < temptation:
        raise ValueError(
            "the payoff structure requires P < R < T for the condition to "
            "describe a prisoner's dilemma")
    return (temptation - reward) / (temptation - punishment)


# ==========================================================================
# practice/deal-triage-calculator.md (v8.0)
#
# The instrument counts named things and reads each count against two edges
# of its own: below the self-serve edge the buyer pays that cost down alone,
# above the participation edge the cost keeps the buyer out. The counts are
# never converted to scores or summed, so they need no common scale. A
# separate reading says whether the deal sinks anything specific, which with
# frequency selects the governance form. Constitution 4.0.
# ==========================================================================

CHAOS_TRAP = "Chaos Trap"

# The two edges per cost, (self-serve, participation), as counts. Chosen, and
# placed on the boundaries of the score bands earlier versions used. Declared
# in 06-calibration.md section 3.2.
SEARCH_EDGES = (4, 8)
CONSENSUS_EDGES = (1, 7)
IMPLEMENTATION_EDGES = (2, 11)

# Gate A: must the product fit a workflow the buyer has already encoded?
GATE_A_GREENFIELD = "greenfield"
GATE_A_PRODUCT_ABSORBS = "product-absorbs"
GATE_A_ENCODED = "encoded"

SEARCH_EVIDENCE_ITEMS = 4

# Frequency. Step 1d. With the exposure reading it selects the governance
# form and decides whether the seller's investment can be amortized at all.
ONE_SHOT, RECURRENT, CONTINUOUS = "one-shot", "recurrent", "continuous"
FREQUENCIES = (ONE_SHOT, RECURRENT, CONTINUOUS)

MARKET = "market"
TRILATERAL = "trilateral"
BILATERAL = "bilateral"
UNIFIED_RISK = "bilateral, watching for unified"

TURNKEY = "turnkey"
KEEPS_OUT = "keeps-out"
ALLOCATE = "allocate"

TriageResult = collections.namedtuple(
    "TriageResult",
    "route positions zones sale_start specific exposure gaps frequency "
    "governance flags reason")


def _check_frequency(frequency):
    if frequency not in FREQUENCIES:
        raise ValueError(
            "frequency is one of {}, not {!r}".format(FREQUENCIES, frequency))


def governance_form(specific, frequency):
    """Williamson's selection, on specific exposure and frequency.

    05-governance-forms.md section 2. With nothing specific sunk the form is
    market governance at any frequency: the parties are strangers and the
    contract is complete.

    With specific exposure, a one-shot transaction takes trilateral
    governance, because neither party will build relational machinery for a
    single event. A recurrent one takes bilateral governance, where the next
    repetition is the safeguard and the MIP is the instrument. A continuous
    relationship stays bilateral and carries a standing question, because
    rising specificity eventually makes the buyer's own integration beat any
    contract the two parties can write.
    """
    _check_frequency(frequency)
    if not specific:
        return MARKET
    if frequency == ONE_SHOT:
        return TRILATERAL
    if frequency == CONTINUOUS:
        return UNIFIED_RISK
    return BILATERAL


def apparatus_is_amortizable(specific, frequency):
    """Whether the seller's investment has anything to amortize over.

    False only for a specific one-shot deal, which the document says to
    escalate: restructure it as recurring, or decline. Running a lighter
    version produces the unallocated failure with the cost already sunk.
    """
    _check_frequency(frequency)
    return not (specific and frequency == ONE_SHOT)


def search_count(n_alternatives):
    """n_search, step 1a: named vendors plus build plus do nothing.

    The floor is 2, because building it and doing nothing are always options.
    """
    if n_alternatives < 2:
        raise ValueError(
            "the alternative count includes 'build it internally' and 'do "
            "nothing', so it cannot fall below 2")
    return n_alternatives


def search_position(n_alternatives, category_named=True, channel_exists=True):
    """The search position, step 3.

    A buyer who cannot name the category faces an unbounded alternative set,
    and a buyer with no path to the seller cannot reach it. Either keeps the
    buyer out whatever the count, so the position is infinite: the cost sits
    in the third zone and only category definition or a channel pulls it
    back into range.
    """
    n = search_count(n_alternatives)
    if not category_named or not channel_exists:
        return float("inf")
    return threshold_position(n, *SEARCH_EDGES)


def search_gap(items_evidenced):
    """The search component's gap, from the four evidence items. Step 1a."""
    return component_gap(SEARCH_EVIDENCE_ITEMS, items_evidenced)


def consensus_count(n_vetoes, formal_body_required=False):
    """n_consensus, step 1b: decision roles that can say no, plus one for a
    formal procurement process, security review or board."""
    if n_vetoes < 1:
        raise ValueError(
            "a purchase with nobody able to say no is not a purchase; the "
            "veto count starts at 1")
    return n_vetoes + (1 if formal_body_required else 0)


def consensus_position(n_vetoes, formal_body_required=False):
    """The consensus position, step 3."""
    return threshold_position(consensus_count(n_vetoes, formal_body_required),
                              *CONSENSUS_EDGES)


def consensus_gap(n_vetoes, n_with_documented_objective):
    """The consensus gap, a proxy. Step 1b.

    The denominator is the roles that can say no, without the formal body,
    which is not a person. The measured objective is the seller's view of each
    role, which 07-open-questions.md item 14 records as a proxy for each
    occupant's own uncertainty about their exposure.
    """
    return component_gap(n_vetoes, n_with_documented_objective)


def implementation_count(integration_points, changed_workflows,
                         undocumented_exceptions):
    """n_impl, the three implementation counts summed. Step 1c."""
    parts = {"integration points": integration_points,
             "changed workflows": changed_workflows,
             "undocumented exception paths": undocumented_exceptions}
    for name, value in parts.items():
        if value < 0:
            raise ValueError("{} cannot be negative".format(name))
    return sum(parts.values())


def implementation_position(n_impl):
    """The implementation position, step 3."""
    return threshold_position(n_impl, *IMPLEMENTATION_EDGES)


def exposure_count(integration_points, changed_workflows, divergent_steps):
    """n_exposure, step 2: what the deal sinks that only works here."""
    for name, value in (("integration points", integration_points),
                        ("changed workflows", changed_workflows),
                        ("divergent steps", divergent_steps)):
        if value < 0:
            raise ValueError("{} cannot be negative".format(name))
    return integration_points + changed_workflows + divergent_steps


def triage(workflow_maturity,
           n_alternatives, search_evidence,
           n_vetoes, n_with_documented_objective,
           integration_points, changed_workflows, undocumented_exceptions,
           items_with_artifact, frequency, gate_b_trialable,
           category_named=True, channel_exists=True,
           formal_body_required=False,
           gate_a=GATE_A_ENCODED, divergent_steps=None,
           pilot_requested=False, product_automates_process=True):
    """Run the whole instrument and return a TriageResult.

    Order of operations, which the document fixes:

    0. The workflow maturity gate runs before anything is counted.
    1. The three counts, their positions, and their gaps.
    2. The two gates and the specific-exposure reading. Gate B is answered on
       every deal, because a buyer who can trial and walk away sinks nothing
       specific. Divergence is counted only when gate A answers "encoded" and
       gate B fails.
    3. The overrides: a pilot request, then any cost that keeps the buyer out.
    4. The two readings: every cost self-serve or not, exposure none or
       specific. The governance form comes from exposure and frequency.
    """
    flags = []

    # --- Step 0: workflow maturity gate --------------------------------
    if workflow_maturity not in (1, 2, 3):
        raise ValueError("workflow maturity is scored 1, 2 or 3")
    _check_frequency(frequency)
    if workflow_maturity == 1:
        if product_automates_process:
            return TriageResult(
                route=CHAOS_TRAP, positions=None, zones=None, sale_start=None,
                specific=None, exposure=None, gaps=None, frequency=frequency,
                governance=None, flags=("chaos-trap",),
                reason="Step 0: no written process exists and the product "
                       "automates the process. Redirect to consulting or a "
                       "paid workshop to define the process first.")
        flags.append("undefined-workflow-product-supplies-medium")
    elif workflow_maturity == 2:
        flags.append("emergent-workflow-blueprint-must-reconstruct")

    # --- Step 1: counts, positions, gaps -------------------------------
    n_impl = implementation_count(integration_points, changed_workflows,
                                  undocumented_exceptions)
    positions = {
        "search": search_position(n_alternatives, category_named,
                                  channel_exists),
        "consensus": consensus_position(n_vetoes, formal_body_required),
        "implementation": implementation_position(n_impl),
    }
    gaps = {"search": search_gap(search_evidence),
            "consensus": consensus_gap(n_vetoes, n_with_documented_objective),
            "implementation": component_gap(n_impl, items_with_artifact)
            if n_impl else None}
    zones = {k: cost_zone(r) for k, r in positions.items()}

    # --- Step 2: gates and exposure ------------------------------------
    if gate_a not in (GATE_A_GREENFIELD, GATE_A_PRODUCT_ABSORBS,
                      GATE_A_ENCODED):
        raise ValueError("gate A answers greenfield, product-absorbs or encoded")
    if gate_b_trialable is None:
        raise ValueError(
            "gate B is answered on every deal: can the buyer trial against "
            "its own work and walk away without stranding spend or data?")
    if gate_b_trialable:
        exposure = 0
        flags.append("gate-b-passed-nothing-specific")
    else:
        steps = 0
        if gate_a == GATE_A_ENCODED:
            if divergent_steps is None:
                raise ValueError(
                    "gate A answered 'encoded' and gate B failed, so the "
                    "divergent step count is required")
            steps = divergent_steps
        exposure = exposure_count(integration_points, changed_workflows, steps)
    specific = exposure > 0
    governance = governance_form(specific, frequency)
    if not apparatus_is_amortizable(specific, frequency):
        flags.append("specific-one-shot-escalate")

    def result(route, sale_start, reason, extra=()):
        return TriageResult(
            route=route, positions=positions, zones=zones,
            sale_start=sale_start, specific=specific, exposure=exposure,
            gaps=gaps, frequency=frequency, governance=governance,
            flags=tuple(flags) + tuple(extra), reason=reason)

    # --- Step 3: overrides ---------------------------------------------
    if pilot_requested:
        return result(
            "implementation", ("implementation",),
            "Override: the buyer asked for a pilot or proof of concept, which "
            "reports that it cannot verify fit alone, whatever was counted. "
            "Pilots are governed by the Red Team Protocol.",
            ("pilot-override",))

    out = tuple(sorted(k for k, z in zones.items() if z == KEEPS_BUYER_OUT))
    if out:
        return result(
            KEEPS_OUT, out,
            "A cost keeps the buyer out of the market. Pull it back into "
            "range with the instrument for that cost, or decline. No work on "
            "the other two reaches it.")

    # --- Step 4: the two readings --------------------------------------
    if all(z == SELF_SERVE for z in zones.values()):
        if specific:
            return result(
                ALLOCATE, None,
                "Light sale, heavy contract: every cost is self-serve, and the "
                "deal still sinks something that only works here. Agree "
                "staging and stop rights before it is sunk.",
                ("light-sale-heavy-contract",))
        return result(
            TURNKEY, None,
            "Turnkey: every cost is self-serve and nothing specific is sunk. "
            "Standard terms and self-service provisioning.")

    start = sale_start(positions)
    extra = []
    if not specific:
        extra.append("heavy-sale-light-contract")
        if "implementation" in start:
            extra.append("possible-over-frictioning")
    elif "implementation" in start:
        extra.append("full-chain")
    if "consensus" in start:
        extra.append("consensus-instrument-set-is-thin")
    reasons = {
        "search": "The sale starts at search: the buyer cannot yet find and "
                  "compare on its own. Education, reference architectures, "
                  "category definition and channel work.",
        "consensus": "The sale starts at consensus: the buyer's decision "
                     "roles cannot reach a decision on their own. This is the "
                     "thinnest instrument set in the repository.",
        "implementation": "The sale starts at implementation: the buyer "
                          "cannot verify that it will work here on its own. "
                          "Blueprint, Red Team, MIP and Adoption Review.",
    }
    if len(start) == 1:
        reason = reasons[start[0]]
    else:
        reason = ("Two costs sit at the same position, so the sale starts at "
                  "both and they are run together: " + ", ".join(start) + ".")
    return result("+".join(start), start, reason, extra)
