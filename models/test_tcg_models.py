#!/usr/bin/env python3
"""Assert that every worked example in the playbook reproduces from tcg_models.

The documents are the specification. Each test names the file and section it
checks, so a failure says which prose to read rather than which line to edit.
Where a document and the module disagree, fix the module.

Standard library only:

    python3 models/test_tcg_models.py
"""

import math
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import tcg_models as m


# ==========================================================================
# models.md section 1.5, the normalization guard.
# ==========================================================================

class TestGapNormalization(unittest.TestCase):
    """Section 1.5 makes normalization mandatory before either cost equation.

    Confusing the raw and normalized scales is a documented past bug that
    produces cost estimates off by an order of magnitude.
    """

    def test_endpoints_of_the_scorecard_range_map_to_zero_and_one(self):
        self.assertEqual(m.normalize_gap(2.0), 0.0)
        self.assertEqual(m.normalize_gap(10.0), 1.0)
        self.assertEqual(m.normalize_gap(6.0), 0.5)

    def test_scorecard_midband_matches_the_documented_formula(self):
        # (raw - 2) / 8, spelled out rather than reusing the implementation.
        for raw in (2.0, 3.5, 4.0, 7.0, 9.25, 10.0):
            self.assertAlmostEqual(m.normalize_gap(raw), (raw - 2.0) / 8.0)

    def test_a_raw_score_outside_the_scorecard_range_is_rejected(self):
        for raw in (0.0, 1.9, 10.1, 14.55):
            with self.assertRaises(ValueError):
                m.normalize_gap(raw)

    def test_structural_multiplier_stays_within_one_and_two(self):
        # Section 1.5: normalizing "keeps the structural multiplier in [1, 2]".
        for raw in (2.0, 5.0, 7.5, 10.0):
            gap = m.normalize_gap(raw)
            self.assertTrue(1.0 <= 1.0 + gap <= 2.0)

    def test_effective_cost_refuses_a_bare_float(self):
        with self.assertRaises(TypeError):
            m.effective_cost(10.0, 10.0, 10.0, 0.5)

    def test_reduced_cost_refuses_a_bare_float(self):
        with self.assertRaises(TypeError):
            m.reduced_cost(0.5)

    def test_the_documented_past_bug_cannot_be_reproduced(self):
        """A raw 10 would inflate base friction elevenfold. Section 1.5 says no
        observed deal supports that, so the type system has to stop it."""
        with self.assertRaises(TypeError):
            m.effective_cost(1.0, 1.0, 1.0, 10.0)

    def test_a_normalized_gap_may_exceed_one_under_drift(self):
        """Section 1.5: the gap may exceed 1 when asymmetry rebuilds past the
        instrument's ceiling. The scorecard measures a point in time."""
        drifted = m.asymmetry_drift(m.normalize_gap(9.0), gamma=0.1, t=6.0)
        self.assertGreater(drifted, 1.0)
        self.assertIsInstance(drifted, m.NormalizedGap)
        # And it is still accepted by the cost equations.
        self.assertGreater(m.reduced_cost(drifted), m.A_RISK_AVERSION)

    def test_a_negative_normalized_gap_is_rejected(self):
        with self.assertRaises(ValueError):
            m.NormalizedGap(-0.01)


# ==========================================================================
# models.md section 1, the two cost representations.
# ==========================================================================

class TestTransactionCost(unittest.TestCase):

    def test_effective_cost_matches_the_structural_form(self):
        gap = m.normalize_gap(6.0)  # 0.5
        self.assertAlmostEqual(m.effective_cost(10.0, 20.0, 30.0, gap), 90.0)

    def test_reduced_form_uses_the_anchored_coefficient(self):
        self.assertEqual(m.A_RISK_AVERSION, 2.25)
        gap = m.normalize_gap(10.0)  # 1.0
        self.assertAlmostEqual(m.reduced_cost(gap, c=5.0), 2.25 + 5.0)

    def test_reduced_form_is_convex(self):
        """Convexity is the property section 1.4 says the reduced form exists
        to preserve, and the Three Sales Levers argument depends on it."""
        gaps = [m.NormalizedGap(x / 10.0) for x in range(11)]
        costs = [m.reduced_cost(g) for g in gaps]
        second_differences = [
            costs[i + 1] - 2 * costs[i] + costs[i - 1]
            for i in range(1, len(costs) - 1)
        ]
        for d in second_differences:
            self.assertGreater(d, 0.0)

    def test_discounting_cannot_offset_a_large_gap(self):
        """Section 1.2's argument, stated as a test. Cutting c to zero from a
        starting price does less than closing the gap."""
        wide = m.normalize_gap(10.0)
        narrow = m.normalize_gap(3.0)
        priced = m.reduced_cost(wide, c=1.0)
        discounted_to_free = m.reduced_cost(wide, c=0.0)
        gap_closed = m.reduced_cost(narrow, c=1.0)
        self.assertLess(gap_closed, discounted_to_free)
        self.assertLess(discounted_to_free, priced)

    def test_expanded_form_equals_the_quadratic_it_derives(self):
        """Section 1.3: (c + b*gap)(1 + gap) = b*gap^2 + (b + c)*gap + c."""
        b, c = 2.25, 4.0
        for x in (0.0, 0.25, 0.5, 0.75, 1.0):
            gap = m.NormalizedGap(x)
            expanded = m.effective_cost_expanded(gap, b, c)
            polynomial = b * x ** 2 + (b + c) * x + c
            self.assertAlmostEqual(expanded, polynomial)

    def test_the_dropped_linear_term_is_not_negligible(self):
        """Section 1.4 states the linear term is comparable to the quadratic
        term over the operating range and sometimes larger. That is a claim
        about the models, so it is checkable."""
        b, c = 2.25, 4.0
        larger_at = []
        for x in (0.1, 0.25, 0.5, 0.75, 1.0):
            quadratic = b * x ** 2
            linear = (b + c) * x
            if linear > quadratic:
                larger_at.append(x)
        self.assertTrue(larger_at, "the linear term should dominate somewhere")

    def test_the_gap_is_a_sum_not_a_difference(self):
        """Section 2.1. The Asymmetry Scorecard records that an earlier version
        computed a difference and scored the most dangerous deal on the board
        as symmetric and therefore forecastable."""
        both_blind = m.asymmetry_gap(5.0, 5.0)
        one_sided = m.asymmetry_gap(5.0, 1.0)
        self.assertEqual(both_blind, 10.0)
        self.assertGreater(both_blind, one_sided)


# ==========================================================================
# models.md sections 1.1 and 2.4, and motions.md.
# Per-component amplification, adopted in Constitution v17.0.
# ==========================================================================

class TestPerComponentAmplification(unittest.TestCase):
    """Section 1.1 asserts the two forms are the same quantity, exactly.

    The claim is load-bearing. If the identity only held approximately, every
    downstream result that consumed the scalar gap would have inherited an
    unquantified error when v17.0 split it into three.
    """

    def setUp(self):
        self.f = (2.0, 5.0, 3.0)
        self.g = (m.NormalizedGap(0.2), m.NormalizedGap(0.8),
                  m.NormalizedGap(0.4))

    def test_the_two_forms_agree_exactly(self):
        per_component = m.effective_cost_per_component(*(self.f + self.g))
        mean = m.weighted_mean_gap(*(self.f + self.g))
        self.assertAlmostEqual(per_component,
                               m.effective_cost(*(self.f + (mean,))), places=12)

    def test_equal_gaps_reproduce_the_single_multiplier_form(self):
        gap = m.NormalizedGap(0.6)
        self.assertAlmostEqual(
            m.effective_cost_per_component(*(self.f + (gap, gap, gap))),
            m.effective_cost(*(self.f + (gap,))))

    def test_the_mean_is_friction_weighted_not_arithmetic(self):
        # Section 1.1 spells the weighting out; an arithmetic mean would be 0.4667.
        mean = m.weighted_mean_gap(*(self.f + self.g))
        expected = (2.0 * 0.2 + 5.0 * 0.8 + 3.0 * 0.4) / 10.0
        self.assertAlmostEqual(mean, expected)
        self.assertNotAlmostEqual(mean, (0.2 + 0.8 + 0.4) / 3.0)

    def test_the_mean_is_a_normalized_gap_the_cost_equations_accept(self):
        mean = m.weighted_mean_gap(*(self.f + self.g))
        self.assertIsInstance(mean, m.NormalizedGap)
        m.reduced_cost(mean)  # would raise TypeError on a bare float

    def test_zero_base_friction_has_no_composition(self):
        with self.assertRaises(ValueError):
            m.weighted_mean_gap(0, 0, 0, *self.g)

    def test_raw_gaps_are_refused_per_component_too(self):
        with self.assertRaises(TypeError):
            m.effective_cost_per_component(2.0, 5.0, 3.0, 0.2, 0.8, 0.4)


class TestFrictionVector(unittest.TestCase):
    """motions.md sections 1 to 3, and Axiom I's composition claim.

    Level is the L1 norm of base friction and direction is the share of
    effective cost. Keeping them on different quantities is what makes
    discovery rotate the vector without reclassifying the deal.
    """

    def test_direction_shares_sum_to_one(self):
        v = m.friction_vector(2.0, 5.0, 3.0, m.NormalizedGap(0.2),
                              m.NormalizedGap(0.8), m.NormalizedGap(0.4))
        self.assertAlmostEqual(sum(v.direction), 1.0)

    def test_level_is_base_friction_and_ignores_the_gaps(self):
        wide = m.friction_vector(2.0, 5.0, 3.0, m.NormalizedGap(0.9),
                                 m.NormalizedGap(0.9), m.NormalizedGap(0.9))
        closed = m.friction_vector(2.0, 5.0, 3.0, m.NormalizedGap(0.0),
                                   m.NormalizedGap(0.0), m.NormalizedGap(0.0))
        self.assertEqual(wide.magnitude, closed.magnitude)
        self.assertEqual(wide.magnitude, 10.0)

    def test_closing_one_gap_rotates_the_vector_away_from_it(self):
        """The claim v17.0 exists to make representable.

        A deal opens implementation-dominant. The Blueprint closes the
        implementation gap and nothing else changes. Under the single
        multiplier this rotation is impossible by construction.
        """
        opened = m.friction_vector(1.0, 4.0, 4.0, m.NormalizedGap(0.1),
                                   m.NormalizedGap(0.5), m.NormalizedGap(0.9))
        self.assertEqual(opened.dominant, "implementation")
        after = m.friction_vector(1.0, 4.0, 4.0, m.NormalizedGap(0.1),
                                  m.NormalizedGap(0.5), m.NormalizedGap(0.0))
        self.assertEqual(after.dominant, "consensus")
        self.assertEqual(opened.magnitude, after.magnitude)

    def test_one_multiplier_cannot_rotate_the_vector(self):
        """The negative result stated in Axiom III's mathematical content."""
        base = (1.0, 4.0, 4.0)
        shares = []
        for level in (0.0, 0.3, 0.9):
            gap = m.NormalizedGap(level)
            v = m.friction_vector(*(base + (gap, gap, gap)))
            shares.append(v.direction)
        for other in shares[1:]:
            for a, b in zip(shares[0], other):
                self.assertAlmostEqual(a, b)

    def test_a_vector_with_no_component_at_half_reads_as_composed(self):
        v = m.friction_vector(3.0, 3.0, 3.0, m.NormalizedGap(0.0),
                              m.NormalizedGap(0.0), m.NormalizedGap(0.0))
        self.assertEqual(v.dominant, "composed")

    def test_component_gap_counts_what_is_unevidenced(self):
        # Section 2.4: four stakeholders in scope, one with a documented
        # measured objective.
        self.assertAlmostEqual(m.component_gap(4, 1), 0.75)
        self.assertAlmostEqual(m.component_gap(4, 4), 0.0)
        self.assertAlmostEqual(m.component_gap(4, 0), 1.0)

    def test_nothing_counted_is_not_symmetry(self):
        with self.assertRaises(ValueError):
            m.component_gap(0, 0)

    def test_more_evidence_than_items_is_an_arithmetic_error(self):
        with self.assertRaises(ValueError):
            m.component_gap(3, 4)


# ==========================================================================
# models.md section 2, the two halves of the gap.
# ==========================================================================

class TestScorecardDimensions(unittest.TestCase):
    """asymmetry-scorecard.md v3.0, which counts rather than rates."""

    def test_the_endpoints_match_the_retired_rubric(self):
        self.assertAlmostEqual(m.dimension_score(4, 4), 1.0)
        self.assertAlmostEqual(m.dimension_score(4, 0), 5.0)

    def test_a_dimension_with_nothing_in_scope_is_not_a_one(self):
        """Nothing evidenced out of nothing counted is a different finding."""
        with self.assertRaises(ValueError):
            m.dimension_score(0, 0)

    def test_the_normalized_gap_is_the_mean_of_the_unevidenced_fractions(self):
        """The card's stated identity: the 1-to-5 presentation cancels.

        Seller has evidence for half of what they need, buyer for a quarter.
        """
        seller = [m.dimension_score(4, 2)] * 4
        buyer = [m.dimension_score(4, 1)] * 4
        raw = m.asymmetry_gap(sum(seller) / 4.0, sum(buyer) / 4.0)
        self.assertAlmostEqual(m.normalize_gap(raw), (0.5 + 0.75) / 2.0)
        self.assertAlmostEqual(m.normalize_gap(raw), 0.625)

    def test_the_presentation_scale_carries_no_extra_information(self):
        for evidenced in range(9):
            f = 1.0 - evidenced / 8.0
            self.assertAlmostEqual(m.dimension_score(8, evidenced), 1.0 + 4.0 * f)


class TestAsymmetryHalves(unittest.TestCase):

    def test_seller_ignorance_is_increasing_and_convex_in_both_inputs(self):
        rising = [m.seller_ignorance(u, 5.0) for u in (0, 2, 4, 6, 8, 10)]
        self.assertEqual(rising, sorted(rising))
        steps = [rising[i + 1] - rising[i] for i in range(len(rising) - 1)]
        self.assertEqual(steps, sorted(steps))  # accelerating, not proportional

    def test_seller_ignorance_weights_must_sum_to_one(self):
        with self.assertRaises(ValueError):
            m.seller_ignorance(5.0, 5.0, w_tech=0.7, w_process=0.7)

    def test_buyer_uncertainty_falls_with_proof_and_approaches_a_floor(self):
        """Section 2.3's most useful field implication: no quantity of costly
        signaling drives buyer uncertainty to zero while the return itself
        remains volatile."""
        cv = 0.4
        doubts = [m.buyer_uncertainty(cv, k) for k in (0, 2, 4, 8, 10)]
        self.assertEqual(doubts, sorted(doubts, reverse=True))
        floor = m.buyer_uncertainty_floor(cv)
        self.assertAlmostEqual(floor, 0.4)
        # Proof never reaches the floor, it only approaches it.
        self.assertGreater(doubts[-1], floor)
        self.assertAlmostEqual(m.buyer_uncertainty(cv, 10.0),
                               floor + 2.0 * math.exp(-0.5 * 10.0))
        self.assertLess(doubts[-1] - floor, 0.02)

    def test_proof_shows_diminishing_returns(self):
        gains = []
        prev = m.buyer_uncertainty(0.4, 0.0)
        for k in (2, 4, 6, 8, 10):
            here = m.buyer_uncertainty(0.4, k)
            gains.append(prev - here)
            prev = here
        self.assertEqual(gains, sorted(gains, reverse=True))


# ==========================================================================
# consensus-friction-calculator.md line 84, the worked example.
# ==========================================================================

class TestConsensusFriction(unittest.TestCase):
    """The calculator's worked example:

        F = 1.0 * 5^1.35 * 1.25 * 1.6 = 8.78 * 1.25 * 1.6 = 17.6

    with alpha = 1.0, N = 5, beta = 1.35, Var = 0.25, TO = 3, gamma_TO = 0.20.
    """

    def test_the_committee_term_matches_the_documented_intermediate(self):
        self.assertAlmostEqual(5 ** m.BETA_COMMITTEE, 8.78, places=2)

    def test_the_worked_example_reproduces(self):
        result = m.consensus_friction_field(
            n=5, var_i=0.25, technical_overlap=3)
        self.assertAlmostEqual(result, 17.6, places=1)

    def test_the_worked_example_reproduces_factor_by_factor(self):
        result = m.consensus_friction_field(
            n=5, var_i=0.25, technical_overlap=3)
        self.assertAlmostEqual(
            result, 1.0 * 5 ** 1.35 * 1.25 * 1.6, places=10)

    def test_the_worked_example_lands_in_the_medium_band(self):
        """The document reads the result as medium, which calls for a
        stakeholder alignment matrix and shared evaluation criteria."""
        result = m.consensus_friction_field(5, 0.25, 3)
        self.assertEqual(m.consensus_band(result), "medium")

    def test_band_edges_match_the_risk_table(self):
        self.assertEqual(m.consensus_band(9.99), "low")
        self.assertEqual(m.consensus_band(10.0), "medium")
        self.assertEqual(m.consensus_band(25.0), "medium")
        self.assertEqual(m.consensus_band(25.01), "high")

    def test_defaults_match_the_documented_calibration(self):
        self.assertEqual(m.ALPHA_COORDINATION, 1.0)
        self.assertEqual(m.BETA_COMMITTEE, 1.35)
        self.assertEqual(m.GAMMA_TECHNICAL_OVERLAP, 0.20)

    def test_the_core_form_is_the_field_form_without_overlap(self):
        """Section 3.4: the two-term form is what the axioms require, and the
        third term is a field refinement."""
        core = m.consensus_friction(5, 0.25)
        field = m.consensus_friction_field(5, 0.25, technical_overlap=3)
        self.assertAlmostEqual(field, core * (1.0 + 0.20 * 3))

    def test_perfect_agreement_still_costs_something(self):
        """Section 3.1: size alone imposes cost even under perfect
        agreement, and friction reduces to the structural floor."""
        self.assertAlmostEqual(m.consensus_friction(5, 0.0), 5 ** 1.35)

    def test_the_sixth_stakeholder_costs_more_than_the_second(self):
        """Section 3.1's stated consequence of beta > 1."""
        second = m.consensus_friction(2, 0.0) - m.consensus_friction(1, 0.0)
        sixth = m.consensus_friction(6, 0.0) - m.consensus_friction(5, 0.0)
        self.assertGreater(sixth, second)

    def test_sensitivity_to_variance_scales_with_committee_size(self):
        """Section 3.3: d F / d Var = alpha * N^beta, checked numerically."""
        for n in (3, 5, 10):
            h = 1e-7
            numeric = (m.consensus_friction(n, 0.5 + h)
                       - m.consensus_friction(n, 0.5 - h)) / (2 * h)
            self.assertAlmostEqual(
                numeric, m.consensus_sensitivity_to_variance(n), places=5)

    def test_aligning_a_committee_of_ten_beats_aligning_three(self):
        """Section 3.3's field claim, and the calculator's case for running the
        Red Team on large committees specifically."""
        self.assertGreater(m.consensus_sensitivity_to_variance(10),
                           m.consensus_sensitivity_to_variance(3))

    def test_incentive_variance_is_bounded_above_by_one(self):
        """Section 3.2: bounded because I_i is bounded on [-1, 1]. A computed
        value above 1 indicates an arithmetic error."""
        worst = m.incentive_variance([-1.0, 1.0, -1.0, 1.0])
        self.assertAlmostEqual(worst, 1.0)
        self.assertLessEqual(worst, 1.0)

    def test_identical_alignment_gives_zero_variance(self):
        self.assertAlmostEqual(m.incentive_variance([0.5] * 6), 0.0)

    def test_a_score_outside_the_stakeholder_range_is_rejected(self):
        with self.assertRaises(ValueError):
            m.incentive_variance([0.0, 1.5])

    def test_variance_uses_the_population_form(self):
        """Section 3.2 divides by N, not by N - 1."""
        scores = [1.0, -1.0, 0.0]
        mean = 0.0
        expected = sum((s - mean) ** 2 for s in scores) / 3
        self.assertAlmostEqual(m.incentive_variance(scores), expected)


# ==========================================================================
# models.md section 4, urgency decay.
# ==========================================================================

class TestUrgencyDecay(unittest.TestCase):

    def test_with_no_catalyst_decay_runs_at_full_inertia(self):
        """Section 4.3's first boundary."""
        self.assertAlmostEqual(m.decay_rate(0.8, e_external=0.0), 0.8)

    def test_a_strong_catalyst_pushes_decay_toward_zero(self):
        """Section 4.3's second boundary."""
        weak = m.decay_rate(0.8, e_external=0.0)
        strong = m.decay_rate(0.8, e_external=10.0)
        self.assertLess(strong, weak)
        self.assertAlmostEqual(strong, 0.8 / 6.0)

    def test_decay_falls_in_the_catalyst_and_rises_in_inertia(self):
        """The two signed partials of section 4.3."""
        rates = [m.decay_rate(0.8, e) for e in (0, 2, 4, 6, 8, 10)]
        self.assertEqual(rates, sorted(rates, reverse=True))
        by_inertia = [m.decay_rate(x, 4.0) for x in (0.2, 0.5, 1.0, 2.0)]
        self.assertEqual(by_inertia, sorted(by_inertia))

    def test_value_decays_exponentially_from_the_triggering_event(self):
        self.assertAlmostEqual(m.value_decay(100.0, 0.0, 12.0), 100.0)
        self.assertAlmostEqual(m.value_decay(100.0, 0.1, 0.0), 100.0)
        self.assertAlmostEqual(m.value_decay(100.0, math.log(2), 1.0), 50.0)

    def test_a_catalyst_is_the_only_term_a_seller_can_move(self):
        """Section 4.3's field implication, as a comparison at twelve months."""
        v_no_catalyst = m.value_decay(100.0, m.decay_rate(1.0, 0.0), 12.0)
        v_catalyst = m.value_decay(100.0, m.decay_rate(1.0, 8.0), 12.0)
        self.assertGreater(v_catalyst, v_no_catalyst)

    def test_asymmetry_drift_is_linear_in_time(self):
        start = m.normalize_gap(4.0)
        self.assertAlmostEqual(m.asymmetry_drift(start, 0.05, 0.0), start)
        self.assertAlmostEqual(m.asymmetry_drift(start, 0.05, 10.0),
                               float(start) + 0.5)

    def test_maintenance_holds_the_drift_rate_down(self):
        """seller-surplus.md section 7.2: C_sustain is the spend that
        holds gamma down, and Net Revenue Retention is this equation run past
        signature."""
        start = m.normalize_gap(2.0)
        unmaintained = m.asymmetry_drift(start, gamma=0.08, t=24.0)
        maintained = m.asymmetry_drift(start, gamma=0.02, t=24.0)
        self.assertLess(maintained, unmaintained)


# ==========================================================================
# friction-efficiency-index.md
# ==========================================================================

class TestFrictionEfficiencyIndex(unittest.TestCase):

    def test_the_composite_weights_sum_to_one(self):
        """Section 5 states the weights sum to 1.00, which is what bounds the
        index on [0, 100]. The parameter reference records that the split has
        no empirical basis."""
        self.assertAlmostEqual(sum(m.FEI_WEIGHTS), 1.00)

    def test_the_weights_are_the_documented_split(self):
        self.assertEqual(m.FEI_WEIGHTS, (0.35, 0.25, 0.25, 0.15))

    def test_rms_regression_ten_identified_none_resolved_returns_zero(self):
        """Section 3's recorded arithmetic error. The canvas form
        N_edge / (N_edge + N_unresolved) scored 10/20 = 0.50, reporting half
        the risk mitigated when in fact none was."""
        self.assertEqual(m.risk_mitigation_score(10, 10), 0.0)

    def test_rms_does_not_reproduce_the_double_counted_value(self):
        buggy = 10 / (10 + 10)
        self.assertNotAlmostEqual(m.risk_mitigation_score(10, 10), buggy)
        self.assertAlmostEqual(buggy, 0.50)

    def test_rms_matches_the_documented_shallow_workshop_examples(self):
        """Section 3: two surfaced and both closed scores 1.00; forty surfaced
        and thirty-five closed scores 0.875. The lazier workshop wins, which is
        why the count must be reported alongside."""
        self.assertAlmostEqual(m.risk_mitigation_score(2, 0), 1.00)
        self.assertAlmostEqual(m.risk_mitigation_score(40, 5), 0.875)
        self.assertFalse(m.rms_is_credible(2))
        self.assertTrue(m.rms_is_credible(40))

    def test_rms_rejects_more_unresolved_than_identified(self):
        with self.assertRaises(ValueError):
            m.risk_mitigation_score(10, 11)

    def test_rms_is_undefined_when_nothing_was_identified(self):
        with self.assertRaises(ValueError):
            m.risk_mitigation_score(0, 0)

    def test_far_is_blind_to_scale(self):
        """Section 1's stated property, which is why the total must be
        reported alongside the ratio."""
        small = m.friction_allocation_ratio(10, 5)
        large = m.friction_allocation_ratio(1000, 500)
        self.assertAlmostEqual(small, large)
        self.assertAlmostEqual(small, 2 / 3)

    def test_far_reference_band_edges(self):
        self.assertFalse(m.far_in_band(0.59))
        self.assertTrue(m.far_in_band(0.60))
        self.assertTrue(m.far_in_band(0.75))
        self.assertFalse(m.far_in_band(0.76))

    def test_bcv_penalizes_committee_size(self):
        """Section 2: the N^0.5 denominator is a correction, not decoration.
        The canvas form rewarded dragging more people into rooms, which the
        Consensus Friction Calculator correctly scores as worse."""
        four_depts_small_committee = m.buyer_commitment_velocity(4, 3, 4)
        four_depts_large_committee = m.buyer_commitment_velocity(4, 3, 16)
        self.assertGreater(four_depts_small_committee,
                           four_depts_large_committee)

    def test_bcv_guard_prevents_division_by_zero_on_same_day_response(self):
        self.assertAlmostEqual(m.buyer_commitment_velocity(4, 0, 4), 2.0)

    def test_svi_penalizes_early_delivery_as_heavily_as_late(self):
        """Section 4: deliberate. A wrong estimate on the optimistic side
        produces the same credibility loss as one on the pessimistic side."""
        early = m.scope_variance_index(t_actual=50, t_scoped=100, c_orders=0)
        late = m.scope_variance_index(t_actual=150, t_scoped=100, c_orders=0)
        self.assertAlmostEqual(early, late)
        self.assertAlmostEqual(early, 0.5)

    def test_svi_change_order_coefficient(self):
        """One change order is worth about as much scope instability as a
        25 percent schedule miss."""
        one_order = m.scope_variance_index(100, 100, 1)
        quarter_miss = m.scope_variance_index(125, 100, 0)
        self.assertAlmostEqual(one_order, quarter_miss)

    def test_svi_caps_at_one(self):
        """Section 5: allowing the term to run higher would let one
        catastrophic project dominate a cohort average."""
        self.assertAlmostEqual(m.normalize_svi(3.5), 1.0)

    def test_bcv_normalization_caps_at_one(self):
        self.assertAlmostEqual(m.normalize_bcv(2.0, bcv_ref=0.5), 1.0)
        self.assertAlmostEqual(m.normalize_bcv(0.25, bcv_ref=0.5), 0.5)

    def test_the_index_is_bounded_on_zero_to_one_hundred(self):
        best = m.friction_efficiency_index(far=1.0, bcv=10.0, rms=1.0, svi=0.0)
        worst = m.friction_efficiency_index(far=0.0, bcv=0.0, rms=0.0, svi=5.0)
        self.assertAlmostEqual(best, 100.0)
        self.assertAlmostEqual(worst, 0.0)

    def test_the_index_matches_the_weighted_sum_written_out(self):
        far, bcv, rms, svi = 0.70, 0.40, 0.80, 0.30
        expected = 100.0 * (0.35 * far
                            + 0.25 * min(bcv / 0.5, 1.0)
                            + 0.25 * rms
                            + 0.15 * (1.0 - min(svi, 1.0)))
        self.assertAlmostEqual(
            m.friction_efficiency_index(far, bcv, rms, svi), expected)

    def test_a_high_far_can_hide_a_low_rms(self):
        """Section 5's stated failure of the composite: an expensive, shallow
        process still produces a respectable score."""
        shallow = m.friction_efficiency_index(far=0.75, bcv=0.5, rms=0.10,
                                              svi=0.10)
        self.assertGreater(shallow, 50.0)
        self.assertLess(m.risk_mitigation_score(40, 36), 0.15)

    def test_band_edges_match_the_composite_table(self):
        self.assertEqual(m.fei_band(75.1), "front-loaded")
        self.assertEqual(m.fei_band(75.0), "mixed")
        self.assertEqual(m.fei_band(50.0), "mixed")
        self.assertEqual(m.fei_band(49.9), "late")


# ==========================================================================
# milestone-valuation-model.md
# ==========================================================================

class TestMilestoneValuation(unittest.TestCase):
    """The reference stage structure table, with mu of 25, 50 and 80 percent
    and residuals of 0.75, 0.375 and 0.075 times x_0."""

    MUS = (0.25, 0.50, 0.80)

    def test_the_reference_residual_chain_reproduces(self):
        x0 = m.normalize_gap(10.0)  # x_0 = 1.0, so residuals read directly
        schedule = m.residual_schedule(x0, self.MUS)
        self.assertAlmostEqual(schedule[0], 1.000)
        self.assertAlmostEqual(schedule[1], 0.750)
        self.assertAlmostEqual(schedule[2], 0.375)
        self.assertAlmostEqual(schedule[3], 0.075)

    def test_the_chain_scales_with_the_scorecard_gap(self):
        x0 = m.normalize_gap(6.0)  # 0.5
        schedule = m.residual_schedule(x0, self.MUS)
        self.assertAlmostEqual(schedule[1], 0.750 * 0.5)
        self.assertAlmostEqual(schedule[2], 0.375 * 0.5)
        self.assertAlmostEqual(schedule[3], 0.075 * 0.5)

    def test_residual_compounds_downward_rather_than_stepping_linearly(self):
        """Each mu applies to what remains rather than to the original gap.

        The reference table's three fractions sum to 1.55, so reading them as
        shares of the original gap would drive the residual negative by stage
        3. Compounding keeps it positive and approaching zero, which is what
        the table's own residual column shows.
        """
        x0 = m.normalize_gap(10.0)
        schedule = m.residual_schedule(x0, self.MUS)
        self.assertGreater(sum(self.MUS), 1.0)
        linear_reading = float(x0) * (1.0 - sum(self.MUS))
        self.assertLess(linear_reading, 0.0)
        self.assertGreater(schedule[-1], 0.0)
        # Every stage removes a share of what remains, never of the original.
        for before, after, mu in zip(schedule, schedule[1:], self.MUS):
            self.assertAlmostEqual(before - after, mu * before)

    def test_residual_matches_the_product_form(self):
        x0 = m.normalize_gap(8.0)
        expected = float(x0)
        for mu in self.MUS:
            expected *= (1 - mu)
        self.assertAlmostEqual(m.residual_uncertainty(x0, self.MUS), expected)

    def test_a_gate_that_cannot_fail_resolves_nothing(self):
        """The vanity criteria failure mode: acceptance conditions written so
        loosely that no outcome fails them make mu effectively zero."""
        x0 = m.normalize_gap(10.0)
        self.assertAlmostEqual(m.residual_uncertainty(x0, (0.0, 0.0, 0.0)), 1.0)

    def test_stage_surplus_uses_the_reduced_form_cost(self):
        # Every term in annual contract values, per section 1.7. The payment
        # is 0.25 of ACV, not 25 of anything.
        x_m = m.NormalizedGap(0.375)
        surplus = m.stage_surplus(p_m=0.8, v_gross_m=1.5, x_m=x_m, c_m=0.25)
        expected = 0.8 * (1.5 - (2.25 * 0.375 ** 2 + 0.25))
        self.assertAlmostEqual(surplus, expected)

    def test_the_uncertainty_profile_across_the_reference_gates(self):
        """The table the milestone model calls the argument.

        Entering uncertainty is worth roughly five times the first gate's
        payment and three percent of the last one's. That profile is why the
        refundable component belongs early, and it only reads that way when
        payments are fractions of annual contract value.
        """
        x0 = m.normalize_gap(10.0)
        entering = m.residual_schedule(x0, self.MUS)[1:]
        payments = (0.25, 0.35, 0.40)
        ratios = [m.reduced_cost(x) / c for x, c in zip(entering, payments)]
        self.assertAlmostEqual(ratios[0], 5.06, places=2)
        self.assertAlmostEqual(ratios[1], 0.90, places=2)
        self.assertAlmostEqual(ratios[2], 0.03, places=2)
        # Strictly decreasing: the option to stop is worth most when least is
        # known, which is the whole staging argument.
        self.assertGreater(ratios[0], ratios[1])
        self.assertGreater(ratios[1], ratios[2])

    def test_reading_the_payments_as_percent_inverts_the_argument(self):
        """Section 1.7 calls this a unit error rather than a second reading."""
        x0 = m.normalize_gap(10.0)
        entering = m.residual_schedule(x0, self.MUS)[1:]
        as_percent = [m.reduced_cost(x) / c
                      for x, c in zip(entering, (25.0, 35.0, 40.0))]
        # Under this reading uncertainty never reaches even a tenth of any
        # payment, so risk never outweighs return and Axiom III is false.
        self.assertLess(max(as_percent), 0.1)

    def test_staging_raises_surplus_by_shrinking_residual_uncertainty(self):
        """The point of the whole model: staging does not reduce the work, it
        reduces how much must be committed before the buyer knows."""
        unstaged = m.stage_surplus(0.8, 100.0, m.NormalizedGap(1.0), 25.0)
        staged = m.stage_surplus(0.8, 100.0, m.NormalizedGap(0.075), 25.0)
        self.assertGreater(staged, unstaged)

    def test_stage_surplus_requires_a_normalized_residual(self):
        with self.assertRaises(TypeError):
            m.stage_surplus(0.8, 100.0, 0.375, 25.0)

    def test_a_mu_outside_zero_to_one_is_rejected(self):
        x0 = m.normalize_gap(10.0)
        with self.assertRaises(ValueError):
            m.residual_uncertainty(x0, (1.5,))


# ==========================================================================
# seller-surplus.md
# ==========================================================================

class TestSellerSurplus(unittest.TestCase):

    def test_section_two_form(self):
        self.assertAlmostEqual(
            m.seller_surplus(p_close=0.5, v_contract=1000.0,
                             c_deliver=400.0, c_invest=200.0),
            0.5 * 600.0 - 200.0)

    def test_invest_is_sunk_whether_or_not_the_deal_closes(self):
        """Section 2's stated asymmetry: C_deliver is contingent and C_invest
        is not."""
        lost = m.seller_surplus(0.0, 1000.0, 400.0, 200.0)
        self.assertAlmostEqual(lost, -200.0)

    def test_a_buyer_viable_deal_can_be_seller_negative(self):
        """Section 2: a deal inside the buyer's potential well can sit outside
        the seller's, and closing it is accretive for the customer and dilutive
        for the seller's own firm."""
        buyer_side = m.deal_surplus(v_effective=900.0, v_next_best=300.0,
                                    f_effective=200.0)
        seller_side = m.seller_surplus(0.3, 1000.0, 400.0, 400.0)
        self.assertGreater(buyer_side, 0.0)
        self.assertLess(seller_side, 0.0)

    def test_quasi_rent_is_the_exposure_not_the_total_spend(self):
        """Section 3: two engagements consuming identical hours carry different
        exposure when one produces a reusable connector."""
        reusable = m.quasi_rent(c_invest=200.0, r_redeploy=150.0)
        one_off = m.quasi_rent(c_invest=200.0, r_redeploy=0.0)
        self.assertAlmostEqual(reusable, 50.0)
        self.assertAlmostEqual(one_off, 200.0)
        self.assertLess(reusable, one_off)

    def test_redeployable_value_cannot_exceed_the_investment(self):
        with self.assertRaises(ValueError):
            m.quasi_rent(c_invest=100.0, r_redeploy=150.0)

    def test_the_marginal_rule_threshold_is_the_reciprocal_of_margin(self):
        """Section 4 inverted into section 6's endorsed question: what would
        have to be true about the derivative for this spend to make sense."""
        threshold = m.required_marginal_close_gain(v_contract=1000.0,
                                                   c_deliver=400.0)
        self.assertAlmostEqual(threshold, 1.0 / 600.0)

    def test_the_threshold_and_the_rule_agree_at_the_boundary(self):
        v, c = 1000.0, 400.0
        threshold = m.required_marginal_close_gain(v, c)
        self.assertFalse(m.marginal_investment_rule(threshold, v, c))
        self.assertTrue(m.marginal_investment_rule(threshold * 1.01, v, c))
        self.assertFalse(m.marginal_investment_rule(threshold * 0.99, v, c))

    def test_no_investment_can_justify_a_non_positive_margin(self):
        with self.assertRaises(ValueError):
            m.required_marginal_close_gain(v_contract=400.0, c_deliver=400.0)

    def test_thin_margin_demands_a_larger_probability_gain(self):
        thin = m.required_marginal_close_gain(1000.0, 900.0)
        fat = m.required_marginal_close_gain(1000.0, 100.0)
        self.assertGreater(thin, fat)

    def test_repeated_form_reduces_to_the_single_shot_at_t_equals_one(self):
        """Section 7 states the single-shot form of section 2 is this
        expression with T = 1 and C_sustain = 0. That identity is the join
        between the two models, so it is asserted rather than assumed."""
        p_close, v, c_deliver, c_invest = 0.6, 1000.0, 400.0, 200.0
        repeated = m.repeated_seller_surplus(
            r=[p_close], v=[v], c_deliver=[c_deliver], c_sustain=[0.0],
            rho=0.0, c_invest=c_invest)
        single = m.seller_surplus(p_close, v, c_deliver, c_invest)
        self.assertAlmostEqual(repeated, single)

    def test_a_durable_relationship_can_justify_a_single_shot_negative_deal(self):
        """Section 7's correction: C_invest amortizes across the stream, not
        against the first contract, so a first-year margin test disqualifies
        deals a durable relationship would justify."""
        single = m.seller_surplus(0.6, 500.0, 300.0, 200.0)
        self.assertLess(single, 0.0)
        repeated = m.repeated_seller_surplus(
            r=[0.6, 0.55, 0.5], v=[500.0] * 3, c_deliver=[300.0] * 3,
            c_sustain=[20.0] * 3, rho=0.10, c_invest=200.0)
        self.assertGreater(repeated, 0.0)

    def test_discounting_reduces_the_value_of_later_periods(self):
        args = dict(r=[0.9] * 5, v=[100.0] * 5, c_deliver=[40.0] * 5,
                    c_sustain=[5.0] * 5, c_invest=50.0)
        self.assertGreater(m.repeated_seller_surplus(rho=0.0, **args),
                           m.repeated_seller_surplus(rho=0.15, **args))

    def test_mismatched_period_lengths_are_rejected(self):
        with self.assertRaises(ValueError):
            m.repeated_seller_surplus(r=[0.9, 0.9], v=[100.0],
                                      c_deliver=[40.0], c_sustain=[0.0],
                                      rho=0.0, c_invest=0.0)

    def test_lock_in_raises_the_cooperation_threshold(self):
        """Section 7.1: raising the seller's temptation payoff raises the
        threshold the seller's own discount factor must clear, so the
        arrangement becomes harder to sustain exactly as the seller's position
        strengthens."""
        base = m.cooperation_threshold(temptation=5.0, reward=3.0,
                                       punishment=1.0)
        locked_in = m.cooperation_threshold(temptation=9.0, reward=3.0,
                                            punishment=1.0)
        self.assertGreater(locked_in, base)

    def test_cooperation_requires_a_prisoners_dilemma_payoff_order(self):
        with self.assertRaises(ValueError):
            m.cooperation_threshold(temptation=1.0, reward=3.0, punishment=5.0)


# ==========================================================================
# deal-triage-calculator.md v5.0
# ==========================================================================

class TestDealTriageCalculator(unittest.TestCase):
    """The instrument counts named things and emits a level and a direction.

    Every test below names the step it checks. The document is the
    specification: where it and the module disagree, the module is the bug.
    """

    STRUCTURAL_DEAL = dict(
        workflow_maturity=3, n_alternatives=4, search_evidence=4,
        n_vetoes=6, n_with_documented_objective=1,
        integration_points=7, changed_workflows=3, undocumented_exceptions=4,
        items_with_artifact=2, gate_b_trialable=False, divergent_steps=4,
        frequency=m.RECURRENT)

    # --- Step 0 -------------------------------------------------------
    def test_an_undefined_workflow_stops_before_anything_is_counted(self):
        result = m.triage(**dict(self.STRUCTURAL_DEAL, workflow_maturity=1))
        self.assertEqual(result.route, m.CHAOS_TRAP)
        self.assertIsNone(result.level)

    def test_a_medium_product_survives_an_undefined_workflow(self):
        """Step 0's exception: nothing to misfit against is not a trap."""
        result = m.triage(**dict(self.STRUCTURAL_DEAL, workflow_maturity=1,
                                 product_automates_process=False))
        self.assertNotEqual(result.route, m.CHAOS_TRAP)
        self.assertIn("undefined-workflow-product-supplies-medium", result.flags)

    def test_an_emergent_workflow_flags_rather_than_stops(self):
        result = m.triage(**dict(self.STRUCTURAL_DEAL, workflow_maturity=2))
        self.assertIn("emergent-workflow-blueprint-must-reconstruct",
                      result.flags)

    # --- Step 1a, search ----------------------------------------------
    def test_the_alternative_count_cannot_fall_below_two(self):
        """Build and do-nothing are always on the list."""
        with self.assertRaises(ValueError):
            m.search_score(1)

    def test_an_unnamed_category_scores_the_maximum_not_the_minimum(self):
        """The document's loudest warning. An unnamed category is an unbounded
        alternative set, and reading it as a short list is the same error the
        retired market-stage step called reading absence of competition as
        maturity."""
        self.assertEqual(m.search_score(2, category_named=True), 1)
        self.assertEqual(m.search_score(2, category_named=False), 9)

    def test_no_channel_adds_two_and_the_score_is_capped(self):
        self.assertEqual(m.search_score(4, channel_exists=False), 5)
        self.assertEqual(
            m.search_score(20, category_named=False, channel_exists=False),
            m.COMPONENT_SCORE_MAX)

    def test_search_bands_match_the_document(self):
        for count, expected in ((2, 1), (3, 3), (4, 3), (5, 6), (7, 6),
                                (8, 9), (30, 9)):
            self.assertEqual(m.search_score(count), expected, count)

    # --- Step 1b, consensus -------------------------------------------
    def test_consensus_bands_match_the_document(self):
        for count, expected in ((1, 1), (2, 3), (3, 3), (4, 6), (6, 6),
                                (7, 9), (40, 9)):
            self.assertEqual(m.consensus_score(count), expected, count)

    def test_a_formal_body_adds_one_without_joining_the_headcount(self):
        self.assertEqual(m.consensus_score(3), 3)
        self.assertEqual(m.consensus_score(3, formal_body_required=True), 4)

    def test_a_purchase_nobody_can_stop_is_not_a_purchase(self):
        with self.assertRaises(ValueError):
            m.consensus_score(0)

    def test_the_consensus_gap_is_measured_against_the_veto_count(self):
        # Six people can say no and one has a documented measured objective.
        self.assertAlmostEqual(m.consensus_gap(6, 1), 5.0 / 6.0)
        self.assertAlmostEqual(m.consensus_gap(6, 6), 0.0)

    # --- Step 1c and step 2, implementation ---------------------------
    def test_the_implementation_count_sums_three_named_things(self):
        self.assertEqual(m.implementation_count(7, 3, 4), 14)

    def test_implementation_bands_match_the_document(self):
        for count, expected in ((0, 1), (2, 1), (3, 3), (5, 3), (6, 6),
                                (10, 6), (11, 9)):
            self.assertEqual(m.implementation_score(count), expected, count)

    def test_divergence_modifier_bands_match_the_document(self):
        for steps, expected in ((0, 1.0), (1, 1.2), (2, 1.2), (3, 1.5),
                                (5, 1.5), (6, 2.0), (20, 2.0)):
            self.assertAlmostEqual(m.divergence_modifier(steps), expected)

    def test_the_modifier_multiplies_and_the_result_is_capped(self):
        self.assertAlmostEqual(m.implementation_score(4, divergent_steps=3),
                               4.5)
        self.assertAlmostEqual(m.implementation_score(11, divergent_steps=6),
                               m.COMPONENT_SCORE_MAX)

    def test_the_modifier_never_reaches_the_level_as_an_addend(self):
        """Summing size and fit would let a large aligned deal and a small
        misaligned one produce the same number."""
        aligned = m.triage(**dict(self.STRUCTURAL_DEAL, divergent_steps=0))
        diverged = m.triage(**dict(self.STRUCTURAL_DEAL, divergent_steps=9))
        self.assertGreater(diverged.level, aligned.level)
        self.assertLess(diverged.level - aligned.level, 9)

    # --- The gates ----------------------------------------------------
    def test_gate_a_skips_the_modifier_when_there_is_nothing_to_misfit(self):
        for answer in (m.GATE_A_GREENFIELD, m.GATE_A_PRODUCT_ABSORBS):
            result = m.triage(**dict(self.STRUCTURAL_DEAL, gate_a=answer,
                                     divergent_steps=9))
            self.assertIn("divergence-skipped-gate-a", result.flags)

    def test_gate_b_skips_the_modifier_when_the_buyer_can_measure_the_gap(self):
        result = m.triage(**dict(self.STRUCTURAL_DEAL, gate_b_trialable=True,
                                 divergent_steps=9))
        self.assertIn("divergence-skipped-gate-b", result.flags)

    def test_gate_b_must_be_answered_when_gate_a_says_encoded(self):
        with self.assertRaises(ValueError):
            m.triage(**dict(self.STRUCTURAL_DEAL, gate_b_trialable=None))

    def test_divergence_is_required_when_both_gates_fail(self):
        with self.assertRaises(ValueError):
            m.triage(**dict(self.STRUCTURAL_DEAL, divergent_steps=None))

    # --- Step 3, the two quantities -----------------------------------
    def test_the_level_boundary_sits_at_half_the_range(self):
        self.assertEqual(m.deal_class(14), m.TURNKEY)
        self.assertEqual(m.deal_class(15), m.STRUCTURAL)
        self.assertEqual((m.LEVEL_MIN, m.LEVEL_MAX), (0, 30))

    def test_an_archived_score_converts_by_one_and_a_half(self):
        """4-to-20 with a boundary at 10 maps onto 0-to-30 at 15."""
        self.assertEqual(m.deal_class(10 * 1.5), m.STRUCTURAL)
        self.assertEqual(m.deal_class(9 * 1.5), m.TURNKEY)

    def test_level_ignores_the_gaps_entirely(self):
        blind = m.triage(**dict(self.STRUCTURAL_DEAL, search_evidence=0,
                                items_with_artifact=0,
                                n_with_documented_objective=0))
        mapped = m.triage(**dict(self.STRUCTURAL_DEAL, search_evidence=4,
                                 items_with_artifact=14,
                                 n_with_documented_objective=6))
        self.assertEqual(blind.level, mapped.level)

    def test_closing_every_gap_equally_does_not_rotate_the_vector(self):
        """Axiom III's negative result, reproduced at the instrument.

        Uniform gaps are the single-multiplier case, and there the proportions
        are fixed. Only closing one gap faster than the others rotates
        anything, which is why the instrument scores three gaps rather than
        averaging them into one.
        """
        blind = m.triage(**dict(self.STRUCTURAL_DEAL, search_evidence=0,
                                items_with_artifact=0,
                                n_with_documented_objective=0))
        mapped = m.triage(**dict(self.STRUCTURAL_DEAL, search_evidence=4,
                                 items_with_artifact=14,
                                 n_with_documented_objective=6))
        for a, b in zip(blind.direction, mapped.direction):
            self.assertAlmostEqual(a, b)

    def test_closing_one_gap_alone_does_rotate_it(self):
        blind = m.triage(**dict(self.STRUCTURAL_DEAL, search_evidence=0,
                                items_with_artifact=0,
                                n_with_documented_objective=0))
        one_closed = m.triage(**dict(self.STRUCTURAL_DEAL, search_evidence=0,
                                     items_with_artifact=14,
                                     n_with_documented_objective=0))
        self.assertEqual(blind.level, one_closed.level)
        self.assertGreater(blind.direction[2], one_closed.direction[2])

    def test_closing_the_implementation_gap_rotates_the_routing(self):
        """The claim the whole rebuild rests on, at the instrument level.

        Nothing about the deal's size changes. The Blueprint documents the
        implementation items, and the deal stops routing to implementation.
        """
        deal = dict(self.STRUCTURAL_DEAL, n_alternatives=2, search_evidence=4,
                    n_with_documented_objective=0)
        opened = m.triage(**dict(deal, items_with_artifact=0))
        self.assertEqual(opened.route, "implementation")
        after = m.triage(**dict(deal, items_with_artifact=14))
        self.assertEqual(after.route, "consensus")
        self.assertEqual(opened.level, after.level)

    # --- Step 4, routing ----------------------------------------------
    def test_a_pilot_request_overrides_the_counts(self):
        light = dict(self.STRUCTURAL_DEAL, n_alternatives=2, n_vetoes=1,
                     n_with_documented_objective=1, integration_points=1,
                     changed_workflows=0, undocumented_exceptions=0,
                     items_with_artifact=1, divergent_steps=0)
        self.assertEqual(m.triage(**light).deal_class, m.TURNKEY)
        forced = m.triage(**dict(light, pilot_requested=True))
        self.assertEqual(forced.deal_class, m.STRUCTURAL)
        self.assertIn("pilot-override", forced.flags)

    def test_a_turnkey_level_routes_to_the_turnkey_motion(self):
        light = dict(self.STRUCTURAL_DEAL, n_alternatives=2, n_vetoes=1,
                     n_with_documented_objective=1, integration_points=1,
                     changed_workflows=0, undocumented_exceptions=0,
                     items_with_artifact=1, divergent_steps=0)
        result = m.triage(**light)
        self.assertEqual(result.route, "turnkey")

    def test_the_hidden_structural_deal_escapes_the_turnkey_route(self):
        """A small installation on a workflow that matches nothing. Every count
        is low and the level alone cannot see it."""
        hidden = dict(self.STRUCTURAL_DEAL, n_alternatives=2, n_vetoes=1,
                      n_with_documented_objective=1, integration_points=2,
                      changed_workflows=1, undocumented_exceptions=1,
                      items_with_artifact=0, search_evidence=4,
                      divergent_steps=8)
        result = m.triage(**hidden)
        self.assertEqual(result.deal_class, m.TURNKEY,
                         "the level must stay Turnkey for this to be hidden")
        self.assertEqual(result.route, "implementation")
        self.assertIn("hidden-structural", result.flags)

    def test_a_consensus_route_says_the_instrument_set_is_thin(self):
        deal = dict(self.STRUCTURAL_DEAL, n_vetoes=9,
                    n_with_documented_objective=0, formal_body_required=True,
                    integration_points=3, changed_workflows=2,
                    undocumented_exceptions=1, items_with_artifact=6,
                    divergent_steps=0, n_alternatives=2, search_evidence=4)
        result = m.triage(**deal)
        self.assertEqual(result.deal_class, m.STRUCTURAL)
        self.assertEqual(result.route, "consensus")
        self.assertIn("consensus-instrument-set-is-thin", result.flags)

    def test_a_vector_with_no_dominant_component_routes_to_composed(self):
        even = dict(self.STRUCTURAL_DEAL, n_alternatives=8, search_evidence=0,
                    n_vetoes=7, n_with_documented_objective=0,
                    integration_points=6, changed_workflows=3,
                    undocumented_exceptions=2, items_with_artifact=0,
                    divergent_steps=0)
        result = m.triage(**even)
        self.assertEqual(result.route, "composed")
        self.assertEqual(result.deal_class, m.STRUCTURAL)

    def test_a_large_aligned_deal_is_flagged_for_over_frictioning(self):
        result = m.triage(**dict(self.STRUCTURAL_DEAL, divergent_steps=0))
        self.assertIn("possible-over-frictioning", result.flags)

    # --- Frequency and the governance form ----------------------------
    def test_the_four_forms_match_the_document(self):
        for freq, expected in ((m.ONE_SHOT, m.TRILATERAL),
                               (m.RECURRENT, m.BILATERAL),
                               (m.CONTINUOUS, m.UNIFIED_RISK)):
            self.assertEqual(m.governance_form(m.STRUCTURAL, freq), expected)
        for freq in m.FREQUENCIES:
            self.assertEqual(m.governance_form(m.TURNKEY, freq), m.MARKET,
                             "below the boundary the form is market at any "
                             "frequency")

    def test_frequency_does_not_enter_the_level(self):
        """It selects the governance form. It is not a cost."""
        levels = {m.triage(**dict(self.STRUCTURAL_DEAL, frequency=f)).level
                  for f in m.FREQUENCIES}
        self.assertEqual(len(levels), 1)

    def test_a_structural_one_shot_deal_is_flagged_for_escalation(self):
        """The level says it needs the full chain and the frequency says
        nothing will pay for it. Both readings are correct."""
        result = m.triage(**dict(self.STRUCTURAL_DEAL, frequency=m.ONE_SHOT))
        self.assertEqual(result.deal_class, m.STRUCTURAL)
        self.assertIn("structural-one-shot-escalate", result.flags)
        self.assertFalse(m.apparatus_is_amortizable(m.STRUCTURAL, m.ONE_SHOT))

    def test_a_turnkey_one_shot_deal_is_not_flagged(self):
        light = dict(self.STRUCTURAL_DEAL, n_alternatives=2, n_vetoes=1,
                     n_with_documented_objective=1, integration_points=1,
                     changed_workflows=0, undocumented_exceptions=0,
                     items_with_artifact=1, divergent_steps=0,
                     frequency=m.ONE_SHOT)
        result = m.triage(**light)
        self.assertEqual(result.deal_class, m.TURNKEY)
        self.assertEqual(result.governance, m.MARKET)
        self.assertNotIn("structural-one-shot-escalate", result.flags)

    def test_making_a_deal_recurrent_changes_the_form_not_the_deal(self):
        """The strategic claim in governance-forms.md section 5: recurrence
        is partly a commercial choice, and it changes which governance form
        applies rather than making an expensive one cheaper."""
        one_shot = m.triage(**dict(self.STRUCTURAL_DEAL, frequency=m.ONE_SHOT))
        recurrent = m.triage(**dict(self.STRUCTURAL_DEAL, frequency=m.RECURRENT))
        self.assertEqual(one_shot.level, recurrent.level)
        self.assertEqual(one_shot.direction, recurrent.direction)
        self.assertEqual(one_shot.governance, m.TRILATERAL)
        self.assertEqual(recurrent.governance, m.BILATERAL)

    def test_an_unknown_frequency_is_refused(self):
        for bad in ("annual", "subscription", None, ""):
            with self.assertRaises(ValueError):
                m.triage(**dict(self.STRUCTURAL_DEAL, frequency=bad))

    def test_a_chaos_trap_has_no_governance_form(self):
        """No level, so nothing to select a form from."""
        result = m.triage(**dict(self.STRUCTURAL_DEAL, workflow_maturity=1))
        self.assertEqual(result.route, m.CHAOS_TRAP)
        self.assertIsNone(result.governance)

    def test_every_route_is_a_component_name_or_a_documented_special_case(self):
        routes = set()
        for deal in (self.STRUCTURAL_DEAL,
                     dict(self.STRUCTURAL_DEAL, workflow_maturity=1),
                     dict(self.STRUCTURAL_DEAL, n_alternatives=2, n_vetoes=1,
                          n_with_documented_objective=1, integration_points=1,
                          changed_workflows=0, undocumented_exceptions=0,
                          items_with_artifact=1, divergent_steps=0)):
            routes.add(m.triage(**deal).route)
        self.assertTrue(routes <= set(m.COMPONENTS) | {"turnkey", m.CHAOS_TRAP,
                                                       "composed"})


# ==========================================================================
# Cross-cutting: the calibration discipline itself.
# ==========================================================================

class TestCalibrationDiscipline(unittest.TestCase):
    """Constraint 1 of this work: the parameters are unfitted and must stay
    labelled as such. These tests fail if a docstring stops saying so."""

    UNFITTED_MARKERS = ("not fitted", "unfitted", "chosen", "anchored",
                        "convention", "no empirical basis")

    def test_the_module_docstring_states_the_calibration_status(self):
        doc = m.__doc__.lower()
        self.assertIn("nothing in this module is fitted", doc)
        self.assertIn("specified, not fitted", doc)
        self.assertIn("do not quote", doc)

    def test_the_anchored_coefficient_is_not_presented_as_a_measurement(self):
        doc = m.__doc__.lower()
        self.assertIn("anchored by analogy", doc)
        self.assertIn("is not a measurement", doc)

    def test_every_public_function_carries_a_docstring(self):
        for name in dir(m):
            if name.startswith("_"):
                continue
            obj = getattr(m, name)
            if callable(obj) and getattr(obj, "__module__", None) == "tcg_models":
                self.assertTrue(
                    obj.__doc__,
                    "{} needs a docstring naming its canonical home".format(name))

    def test_the_parameter_defaults_match_the_documents(self):
        """A single table of every default this module ships, checked against
        the parameter reference tables. Retuning a coefficient without editing
        the document it came from fails here."""
        self.assertEqual(m.A_RISK_AVERSION, 2.25)
        self.assertEqual(m.ALPHA_COORDINATION, 1.0)
        self.assertEqual(m.BETA_COMMITTEE, 1.35)
        self.assertEqual(m.GAMMA_TECHNICAL_OVERLAP, 0.20)
        self.assertEqual((m.W_TECH, m.W_PROCESS), (0.6, 0.4))
        self.assertEqual((m.PHI_TECH, m.PHI_PROCESS), (1.2, 1.1))
        self.assertEqual(m.MU_RETURN_UNCERTAINTY, 1.0)
        self.assertEqual(m.NU_VENDOR_DOUBT, 2.0)
        self.assertEqual(m.KAPPA_PROOF_DECAY, 0.5)
        self.assertEqual(m.GAMMA_RESPONSIVENESS, 0.5)
        self.assertEqual(m.FEI_WEIGHTS, (0.35, 0.25, 0.25, 0.15))
        self.assertEqual(m.BCV_REF_DEFAULT, 0.5)
        self.assertEqual(m.MIN_CREDIBLE_EDGE_CASES, 8)
        self.assertEqual((m.RAW_GAP_MIN, m.RAW_GAP_MAX), (2.0, 10.0))
        self.assertEqual((m.LEVEL_MIN, m.LEVEL_MAX), (0, 30))
        self.assertEqual((m.TURNKEY_MAX, m.STRUCTURAL_MIN), (14, 15))
        self.assertEqual(m.COMPONENT_SCORE_MAX, 10)
        self.assertEqual(m.DOMINANCE_THRESHOLD, 0.50)
        self.assertEqual(m.SEARCH_EVIDENCE_ITEMS, 4)

    def test_beta_stays_inside_its_documented_range(self):
        with self.assertRaises(ValueError):
            m.consensus_friction(5, 0.25, beta=2.5)
        with self.assertRaises(ValueError):
            m.consensus_friction(5, 0.25, beta=1.0)

    def test_every_numeric_constant_is_listed_in_the_calibration_layer(self):
        """calibration.md is the single home for every value in the model.

        The point of quarantining the numbers is that a reader can accept the
        structural claims without accepting any of them, and that only works
        if the quarantine is complete. A constant that ships in the module and
        appears nowhere in the calibration layer is a number the framework is
        using and not declaring.
        """
        here = os.path.dirname(os.path.abspath(__file__))
        page = open(os.path.join(here, "..", "theory", "reference",
                                 "calibration.md"), encoding="utf-8").read()
        # Names, not values: a value can legitimately appear under a different
        # label, but every knob has to be findable.
        knobs = ("A_RISK_AVERSION", "DOMINANCE_THRESHOLD", "ALPHA_COORDINATION",
                 "BETA_COMMITTEE", "GAMMA_TECHNICAL_OVERLAP", "W_TECH",
                 "W_PROCESS", "PHI_TECH", "PHI_PROCESS", "NU_VENDOR_DOUBT",
                 "KAPPA_PROOF_DECAY", "GAMMA_RESPONSIVENESS", "BCV_REF_DEFAULT",
                 "MIN_CREDIBLE_EDGE_CASES", "STRUCTURAL_MIN",
                 "COMPONENT_SCORE_MAX", "SEARCH_EVIDENCE_ITEMS", "LEVEL_MAX")
        missing = []
        for name in knobs:
            value = getattr(m, name)
            # The page may write 0.50 where repr gives 0.5, so accept either.
            forms = {str(value), "{:g}".format(value)}
            if isinstance(value, float):
                forms.add("{:.2f}".format(value))
            if not any(f in page for f in forms):
                missing.append("{} = {}".format(name, value))
        self.assertEqual(missing, [],
                         "values in the module that calibration.md does not "
                         "declare: {}".format(missing))

    def test_the_calibration_layer_claims_nothing_is_measured(self):
        here = os.path.dirname(os.path.abspath(__file__))
        page = open(os.path.join(here, "..", "theory", "reference",
                                 "calibration.md"), encoding="utf-8").read()
        self.assertIn("No value on this page is a measurement", page)

    def test_the_module_has_no_third_party_imports(self):
        """It must stay dependency-free like the two existing checkers."""
        source = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   "tcg_models.py"), encoding="utf-8").read()
        imported = set()
        for line in source.splitlines():
            line = line.strip()
            if line.startswith("import "):
                imported.add(line[len("import "):].split()[0].split(".")[0])
            elif line.startswith("from "):
                imported.add(line[len("from "):].split()[0].split(".")[0])
        self.assertTrue(imported <= {"math", "collections"},
                        "unexpected imports: {}".format(imported))


if __name__ == "__main__":
    unittest.main()
