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
# 02-mathematical-models.md section 2.5, the normalization guard.
# ==========================================================================

class TestGapNormalization(unittest.TestCase):
    """Section 2.5 makes normalization mandatory before any equation.

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

    def test_a_raw_score_is_refused_where_a_gap_is_expected(self):
        """The documented past bug: a raw scorecard 10 read as a normalized
        gap. The type system stops it at every function that takes a gap."""
        with self.assertRaises(TypeError):
            m.loss_chance([10.0], floor=0.1)
        with self.assertRaises(TypeError):
            m.asymmetry_drift(0.5, 0.1, 1.0)

    def test_a_normalized_gap_cannot_exceed_one(self):
        """Section 5.3: drift relaxes toward the ceiling and never past it."""
        with self.assertRaises(ValueError):
            m.NormalizedGap(1.01)
        drifted = m.asymmetry_drift(m.normalize_gap(9.0), gamma=0.5, t=60.0)
        self.assertLessEqual(drifted, 1.0)
        self.assertIsInstance(drifted, m.NormalizedGap)

    def test_a_negative_normalized_gap_is_rejected(self):
        with self.assertRaises(ValueError):
            m.NormalizedGap(-0.01)


# ==========================================================================
# 02-mathematical-models.md section 1, the two conditions, and section 2.1.
# ==========================================================================

class TestTwoConditions(unittest.TestCase):
    """Constitution 4.0 Part III: one condition per party, in fractions of
    annual contract value, and price cancels when they are added."""

    def test_the_buyer_condition_matches_section_one(self):
        self.assertAlmostEqual(
            m.buyer_condition(v_switch=2.0, price=1.0,
                              buyer_investments=(0.1, 0.2, 0.3),
                              buyer_loss=0.15),
            2.0 - 1.0 - 0.6 - 0.15)

    def test_the_seller_condition_matches_section_one(self):
        self.assertAlmostEqual(
            m.seller_condition(price=1.0, c_deliver=0.4,
                               seller_investments=(0.0, 0.1, 0.2),
                               seller_loss=0.05),
            1.0 - 0.4 - 0.3 - 0.05)

    def test_price_cancels_when_the_conditions_are_added(self):
        """Section 1.3. Whatever the price, the sum is the joint surplus."""
        args = dict(v_switch=2.0, c_deliver=0.4,
                    buyer_investments=(0.1, 0.2, 0.3),
                    seller_investments=(0.0, 0.1, 0.2),
                    buyer_loss=0.15, seller_loss=0.05)
        joint = m.joint_surplus(**args)
        for price in (0.0, 0.5, 1.0, 1.7):
            total = (m.buyer_condition(args["v_switch"], price,
                                       args["buyer_investments"],
                                       args["buyer_loss"])
                     + m.seller_condition(price, args["c_deliver"],
                                          args["seller_investments"],
                                          args["seller_loss"]))
            self.assertAlmostEqual(total, joint)

    def test_a_discount_moves_the_split_and_not_the_joint_surplus(self):
        """The first of section 1.3's three levers."""
        before = (m.buyer_condition(2.0, 1.0, (0.5,), 0.3),
                  m.seller_condition(1.0, 0.4, (0.2,), 0.0))
        after = (m.buyer_condition(2.0, 0.8, (0.5,), 0.3),
                 m.seller_condition(0.8, 0.4, (0.2,), 0.0))
        self.assertAlmostEqual(after[0] - before[0], 0.2)
        self.assertAlmostEqual(after[1] - before[1], -0.2)
        self.assertAlmostEqual(sum(after), sum(before))

    def test_no_price_rescues_a_deal_with_negative_joint_surplus(self):
        """Section 1.3: when the joint surplus is negative, no price makes
        both conditions positive at once. Only verification can help."""
        v_switch, c_deliver, i_b, i_s, l_b = 1.0, 0.4, (0.3,), (0.2,), 0.4
        self.assertLess(m.joint_surplus(v_switch, c_deliver, i_b, i_s, l_b,
                                        0.0), 0.0)
        for price in [x / 100.0 for x in range(0, 201)]:
            both = (m.buyer_condition(v_switch, price, i_b, l_b) > 0
                    and m.seller_condition(price, c_deliver, i_s, 0.0) > 0)
            self.assertFalse(both)
        # Verification lowers the buyer's loss, and the joint surplus turns.
        self.assertGreater(m.joint_surplus(v_switch, c_deliver, i_b, i_s,
                                           0.0, 0.0), 0.0)

    def test_moving_work_changes_only_the_split_at_equal_cost(self):
        """Section 1.4: equal unit costs and no change in future loss."""
        self.assertEqual(m.investment_shift_gain(10.0, 0.02, 0.02), 0.0)

    def test_a_forward_deployed_engineer_moves_all_three_terms(self):
        """Section 1.4: cheaper work and a lower buyer loss raise the joint
        surplus, and the seller's new exposure lowers it."""
        gain = m.investment_shift_gain(10.0, buyer_unit_cost=0.03,
                                       seller_unit_cost=0.02,
                                       change_in_buyer_loss=-0.2,
                                       change_in_seller_loss=0.05)
        self.assertAlmostEqual(gain, 10.0 * 0.01 + 0.2 - 0.05)

    def test_switching_value_subtracts_the_next_best(self):
        self.assertAlmostEqual(m.switching_value(3.0, 1.0), 2.0)

    def test_negative_investment_is_refused(self):
        with self.assertRaises(ValueError):
            m.buyer_condition(2.0, 1.0, (-0.1,), 0.0)

    def test_the_gap_is_a_sum_not_a_difference(self):
        """Section 2.1. The Asymmetry Scorecard records that an earlier version
        computed a difference and scored the most dangerous deal on the board
        as symmetric and therefore forecastable."""
        both_blind = m.asymmetry_gap(5.0, 5.0)
        one_sided = m.asymmetry_gap(5.0, 1.0)
        self.assertEqual(both_blind, 10.0)
        self.assertGreater(both_blind, one_sided)


# ==========================================================================
# 02-mathematical-models.md section 5, future loss.
# ==========================================================================

class TestFutureLoss(unittest.TestCase):

    def test_loss_chance_runs_from_the_floor_to_one(self):
        """Section 5.2's placeholder: a straight line from floor to ceiling."""
        floor = 0.1
        self.assertAlmostEqual(m.loss_chance([m.NormalizedGap(0.0)], floor),
                               floor)
        self.assertAlmostEqual(m.loss_chance([m.NormalizedGap(1.0)], floor),
                               1.0)
        self.assertAlmostEqual(m.loss_chance([m.NormalizedGap(0.5)], floor),
                               0.55)

    def test_a_party_gaps_combine_as_a_mean(self):
        chance = m.loss_chance([m.NormalizedGap(0.2), m.NormalizedGap(0.6)],
                               floor=0.0)
        self.assertAlmostEqual(chance, 0.4)

    def test_proof_never_drives_the_chance_below_the_floor(self):
        """Section 2.3's floor read as a probability."""
        self.assertGreater(m.loss_chance([m.NormalizedGap(0.0)], 0.05), 0.0)

    def test_the_floor_has_no_default(self):
        """06-calibration.md declares the floor named and not valued."""
        with self.assertRaises(TypeError):
            m.loss_chance([m.NormalizedGap(0.5)])

    def test_future_loss_is_exposure_times_chance(self):
        q = m.quasi_rent(c_invest=0.8, r_redeploy=0.2)
        self.assertAlmostEqual(m.future_loss(q, 0.25), 0.15)

    def test_future_loss_is_bounded_by_the_quasi_rent(self):
        self.assertLessEqual(m.future_loss(0.6, 1.0), 0.6)
        with self.assertRaises(ValueError):
            m.future_loss(0.6, 1.2)

    def test_staging_loses_less_than_committing_everything_up_front(self):
        """Section 5.4: the large commitments come late, against small
        residuals, so the staged loss is smaller."""
        residuals = m.residual_schedule(m.NormalizedGap(1.0),
                                        (0.25, 0.50, 0.80))[1:]
        stages = (0.25, 0.35, 0.40)
        staged = m.staged_loss(stages, residuals, floor=0.05)
        unstaged = m.future_loss(sum(stages),
                                 m.loss_chance([m.NormalizedGap(1.0)], 0.05))
        self.assertLess(staged, unstaged)

    def test_staging_needs_one_residual_per_gate(self):
        with self.assertRaises(ValueError):
            m.staged_loss((0.5, 0.5), (m.NormalizedGap(0.5),), 0.05)


# ==========================================================================
# 02-mathematical-models.md section 6, thresholds and positions.
# ==========================================================================

class TestPositions(unittest.TestCase):

    def test_position_is_zero_at_self_serve_and_one_at_participation(self):
        self.assertAlmostEqual(m.threshold_position(0.2, 0.2, 0.6), 0.0)
        self.assertAlmostEqual(m.threshold_position(0.6, 0.2, 0.6), 1.0)
        self.assertAlmostEqual(m.threshold_position(0.4, 0.2, 0.6), 0.5)

    def test_the_three_zones(self):
        self.assertEqual(m.cost_zone(-0.3), m.SELF_SERVE)
        self.assertEqual(m.cost_zone(0.0), m.SELF_SERVE)
        self.assertEqual(m.cost_zone(0.5), m.NEEDS_INVESTMENT)
        self.assertEqual(m.cost_zone(1.0), m.NEEDS_INVESTMENT)
        self.assertEqual(m.cost_zone(1.2), m.KEEPS_BUYER_OUT)

    def test_one_cost_above_its_threshold_keeps_the_buyer_out(self):
        """Axiom I: a cost at a small share of the total can still end it."""
        positions = {"search": 1.1, "consensus": -0.5, "implementation": -0.5}
        self.assertFalse(m.participates(positions))
        self.assertTrue(m.participates({"search": 0.9, "consensus": 0.2,
                                        "implementation": 0.0}))

    def test_the_sale_starts_at_the_largest_position_not_the_largest_cost(self):
        """Positions compare costs measured on different scales. A large
        cost far from its own threshold is not where the sale starts."""
        search = m.threshold_position(5.0, tau_self=4.0, tau_part=20.0)
        consensus = m.threshold_position(0.9, tau_self=0.2, tau_part=1.0)
        self.assertEqual(
            m.sale_start({"search": search, "consensus": consensus}),
            ("consensus",))

    def test_a_tie_is_run_together(self):
        self.assertEqual(
            m.sale_start({"search": 0.4, "consensus": 0.7,
                          "implementation": 0.7}),
            ("consensus", "implementation"))

    def test_thresholds_must_be_ordered(self):
        with self.assertRaises(ValueError):
            m.threshold_position(0.5, tau_self=0.6, tau_part=0.6)


# ==========================================================================
# 02-mathematical-models.md section 2.4, the one-sided gaps.
# ==========================================================================

class TestComponentGap(unittest.TestCase):

    def test_component_gap_counts_what_is_unevidenced(self):
        self.assertAlmostEqual(m.component_gap(4, 3), 0.25)
        self.assertAlmostEqual(m.component_gap(5, 0), 1.0)
        self.assertAlmostEqual(m.component_gap(5, 5), 0.0)

    def test_nothing_counted_is_not_symmetry(self):
        with self.assertRaises(ValueError):
            m.component_gap(0, 0)

    def test_more_evidence_than_items_is_an_arithmetic_error(self):
        with self.assertRaises(ValueError):
            m.component_gap(3, 4)


# ==========================================================================
# 02-mathematical-models.md section 2, the two halves of the gap.
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
# 02-mathematical-models.md section 4, urgency decay.
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

    def test_asymmetry_drift_relaxes_toward_the_ceiling(self):
        """Section 5.3: 1 - (1 - gap0) * exp(-gamma t), bounded at 1."""
        start = m.normalize_gap(4.0)  # 0.25
        self.assertAlmostEqual(m.asymmetry_drift(start, 0.05, 0.0), start)
        self.assertAlmostEqual(m.asymmetry_drift(start, 0.05, 10.0),
                               1.0 - 0.75 * math.exp(-0.5))
        far = [m.asymmetry_drift(start, 0.05, t) for t in (10, 50, 200, 1000)]
        self.assertEqual(far, sorted(far))
        self.assertLessEqual(far[-1], 1.0)

    def test_drift_cannot_run_backwards(self):
        """Discovery is a separate step down, not a negative rate."""
        with self.assertRaises(ValueError):
            m.asymmetry_drift(m.NormalizedGap(0.5), -0.1, 1.0)

    def test_maintenance_holds_the_drift_rate_down(self):
        """04-seller-surplus-model.md section 7.2: C_sustain is the spend that
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

    def test_far_has_no_band(self):
        """Section 1.1: FAR is description, with no target and no weight."""
        self.assertFalse(hasattr(m, "far_in_band"))

    def test_acr_counts_what_was_allocated_before_it_was_sunk(self):
        """Section 1: three of four exposure items sunk under an allocation."""
        self.assertAlmostEqual(m.allocation_coverage_ratio(3, 4), 0.75)
        self.assertAlmostEqual(m.allocation_coverage_ratio(4, 4), 1.0)

    def test_acr_is_undefined_when_nothing_specific_was_sunk(self):
        with self.assertRaises(ValueError):
            m.allocation_coverage_ratio(0, 0)

    def test_acr_cannot_allocate_more_than_was_sunk(self):
        with self.assertRaises(ValueError):
            m.allocation_coverage_ratio(5, 4)

    def test_more_allocation_always_scores_higher(self):
        """Section 6's resolved defect: the composite was monotonic in FAR
        while calling a high FAR a failure. ACR is better all the way to 1.0,
        so a monotonic weight is the right shape."""
        scores = [m.friction_efficiency_index(acr / 10.0, 0.5, 0.8, 0.2)
                  for acr in range(11)]
        self.assertEqual(scores, sorted(scores))

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
        best = m.friction_efficiency_index(acr=1.0, bcv=10.0, rms=1.0, svi=0.0)
        worst = m.friction_efficiency_index(acr=0.0, bcv=0.0, rms=0.0, svi=5.0)
        self.assertAlmostEqual(best, 100.0)
        self.assertAlmostEqual(worst, 0.0)

    def test_the_index_matches_the_weighted_sum_written_out(self):
        acr, bcv, rms, svi = 0.70, 0.40, 0.80, 0.30
        expected = 100.0 * (0.35 * acr
                            + 0.25 * min(bcv / 0.5, 1.0)
                            + 0.25 * rms
                            + 0.15 * (1.0 - min(svi, 1.0)))
        self.assertAlmostEqual(
            m.friction_efficiency_index(acr, bcv, rms, svi), expected)

    def test_a_high_acr_can_hide_a_low_rms(self):
        """Section 5's stated failure of the composite: a well-documented,
        shallow process still produces a respectable score."""
        shallow = m.friction_efficiency_index(acr=0.75, bcv=0.5, rms=0.10,
                                              svi=0.10)
        self.assertGreater(shallow, 50.0)
        self.assertLess(m.risk_mitigation_score(40, 36), 0.15)

    def test_band_edges_match_the_composite_table(self):
        self.assertEqual(m.fei_band(75.1), "allocated")
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

    FLOOR = 0.05
    STAGE_SUNK = (0.10, 0.25, 0.50)

    def test_stage_surplus_matches_the_stage_equation(self):
        """S_m = (1 - pi)(V - c) - pi Q, pi = floor + (1 - floor) x."""
        x_m = m.NormalizedGap(0.375)
        pi = 0.05 + 0.95 * 0.375
        surplus = m.stage_surplus(1.5, 0.25, 0.25, x_m, floor=0.05)
        self.assertAlmostEqual(surplus, (1 - pi) * (1.5 - 0.25) - pi * 0.25)

    def test_the_reference_table_reproduces(self):
        """The milestone model's table: chances 0.763, 0.406, 0.121, expected
        losses 0.076, 0.102, 0.061, and 0.238 in total."""
        entering = m.residual_schedule(m.NormalizedGap(1.0), self.MUS)[1:]
        chances = [m.loss_chance([x], self.FLOOR) for x in entering]
        for got, want in zip(chances, (0.763, 0.406, 0.121)):
            self.assertAlmostEqual(got, want, delta=0.0005 + 1e-9)
        losses = [m.future_loss(q, p) for q, p in zip(self.STAGE_SUNK, chances)]
        for got, want in zip(losses, (0.076, 0.102, 0.061)):
            self.assertAlmostEqual(got, want, delta=0.0005 + 1e-9)
        self.assertAlmostEqual(
            m.staged_loss(self.STAGE_SUNK, entering, self.FLOOR), 0.238,
            places=3)

    def test_staging_cuts_the_loss_and_order_matters(self):
        """The table's argument: 0.85 sunk at signature loses 0.85, staged
        small-first it loses 0.24, staged large-first it loses 0.49."""
        entering = m.residual_schedule(m.NormalizedGap(1.0), self.MUS)[1:]
        at_signature = m.future_loss(
            sum(self.STAGE_SUNK),
            m.loss_chance([m.NormalizedGap(1.0)], self.FLOOR))
        small_first = m.staged_loss(self.STAGE_SUNK, entering, self.FLOOR)
        large_first = m.staged_loss(self.STAGE_SUNK[::-1], entering,
                                    self.FLOOR)
        self.assertAlmostEqual(at_signature, 0.85)
        self.assertAlmostEqual(large_first, 0.495, places=3)
        self.assertLess(small_first, large_first)
        self.assertLess(large_first, at_signature)

    def test_payment_before_proof_costs_pi_times_the_payment(self):
        """Rule 2. At the first gate it costs 0.19, at the last 0.05."""
        entering = m.residual_schedule(m.NormalizedGap(1.0), self.MUS)[1:]
        for x, c, want in ((entering[0], 0.25, 0.19),
                           (entering[2], 0.40, 0.05)):
            proof = m.stage_surplus(1.0, c, 0.1, x, self.FLOOR)
            calendar = m.stage_surplus(1.0, c, 0.1, x, self.FLOOR,
                                       payment_follows_proof=False)
            self.assertAlmostEqual(proof - calendar, want, places=2)

    def test_stage_surplus_requires_a_normalized_residual(self):
        with self.assertRaises(TypeError):
            m.stage_surplus(1.5, 0.25, 0.25, 0.375, floor=0.05)

    def test_a_mu_outside_zero_to_one_is_rejected(self):
        x0 = m.normalize_gap(10.0)
        with self.assertRaises(ValueError):
            m.residual_uncertainty(x0, (1.5,))


# ==========================================================================
# 04-seller-surplus-model.md
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
        buyer_side = m.buyer_condition(
            v_switch=m.switching_value(900.0, 300.0), price=150.0,
            buyer_investments=(50.0,), buyer_loss=0.0)
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
# deal-triage-calculator.md v8.0
# ==========================================================================

class TestDealTriageCalculator(unittest.TestCase):
    """The instrument counts named things, reads each count against two edges
    of its own, and reads specific exposure apart. Every test names the step
    it checks. The document is the specification."""

    DEAL = dict(
        workflow_maturity=3, n_alternatives=4, search_evidence=4,
        n_vetoes=4, n_with_documented_objective=1,
        integration_points=4, changed_workflows=2, undocumented_exceptions=2,
        items_with_artifact=3, gate_b_trialable=False, divergent_steps=3,
        frequency=m.RECURRENT)

    def run_deal(self, **changes):
        args = dict(self.DEAL)
        args.update(changes)
        return m.triage(**args)

    # --- Step 0 -------------------------------------------------------
    def test_an_undefined_workflow_stops_before_anything_is_counted(self):
        result = self.run_deal(workflow_maturity=1)
        self.assertEqual(result.route, m.CHAOS_TRAP)
        self.assertIsNone(result.positions)

    def test_a_medium_product_survives_an_undefined_workflow(self):
        result = self.run_deal(workflow_maturity=1,
                               product_automates_process=False)
        self.assertNotEqual(result.route, m.CHAOS_TRAP)
        self.assertIn("undefined-workflow-product-supplies-medium",
                      result.flags)

    def test_an_emergent_workflow_flags_rather_than_stops(self):
        result = self.run_deal(workflow_maturity=2)
        self.assertIn("emergent-workflow-blueprint-must-reconstruct",
                      result.flags)

    # --- Step 1: counts and edges --------------------------------------
    def test_the_edges_match_the_document(self):
        self.assertEqual(m.SEARCH_EDGES, (4, 8))
        self.assertEqual(m.CONSENSUS_EDGES, (1, 7))
        self.assertEqual(m.IMPLEMENTATION_EDGES, (2, 11))

    def test_each_edge_sits_on_a_retired_band_boundary(self):
        """06-calibration.md: the edges are placed on the boundaries of the
        score bands earlier versions used. Search 2 | 3-4 | 5-7 | 8+,
        consensus 1 | 2-3 | 4-6 | 7+, implementation 0-2 | 3-5 | 6-10 | 11+."""
        self.assertIn(m.SEARCH_EDGES[0], (2, 4, 7))
        self.assertIn(m.SEARCH_EDGES[1], (3, 5, 8))
        self.assertIn(m.CONSENSUS_EDGES[0], (1, 3, 6))
        self.assertIn(m.CONSENSUS_EDGES[1], (2, 4, 7))
        self.assertIn(m.IMPLEMENTATION_EDGES[0], (2, 5, 10))
        self.assertIn(m.IMPLEMENTATION_EDGES[1], (3, 6, 11))

    def test_the_alternative_count_cannot_fall_below_two(self):
        with self.assertRaises(ValueError):
            m.search_position(1)

    def test_positions_are_read_against_each_cost_s_own_edges(self):
        self.assertAlmostEqual(m.search_position(4), 0.0)
        self.assertAlmostEqual(m.search_position(8), 1.0)
        self.assertAlmostEqual(m.consensus_position(4), 0.5)
        self.assertAlmostEqual(m.implementation_position(11), 1.0)

    def test_an_unnamed_category_keeps_the_buyer_out(self):
        """The warning in step 1a: an unnamed category is not a short list."""
        self.assertEqual(m.cost_zone(m.search_position(2, category_named=False)),
                         m.KEEPS_BUYER_OUT)

    def test_no_channel_keeps_the_buyer_out(self):
        self.assertEqual(m.cost_zone(m.search_position(3, channel_exists=False)),
                         m.KEEPS_BUYER_OUT)

    def test_a_formal_body_counts_as_one_more_veto(self):
        self.assertEqual(m.consensus_count(3, formal_body_required=True), 4)
        self.assertGreater(m.consensus_position(3, True),
                           m.consensus_position(3, False))

    def test_a_purchase_nobody_can_stop_is_not_a_purchase(self):
        with self.assertRaises(ValueError):
            m.consensus_count(0)

    def test_the_consensus_gap_leaves_the_formal_body_out(self):
        result = self.run_deal(n_vetoes=4, n_with_documented_objective=1,
                               formal_body_required=True)
        self.assertAlmostEqual(result.gaps["consensus"], 0.75)

    def test_the_implementation_count_sums_three_named_things(self):
        self.assertEqual(m.implementation_count(4, 2, 2), 8)

    def test_the_counts_are_never_summed(self):
        """Version 8.0 has no level: the result carries no total."""
        result = self.run_deal()
        self.assertNotIn("level", result._fields)

    def test_the_gaps_do_not_move_the_positions(self):
        """Step 3: the gaps feed future loss, not today's cost."""
        known = self.run_deal(search_evidence=4, n_with_documented_objective=4,
                              items_with_artifact=8)
        unknown = self.run_deal(search_evidence=0,
                                n_with_documented_objective=0,
                                items_with_artifact=0)
        self.assertEqual(known.positions, unknown.positions)
        self.assertEqual(known.route, unknown.route)

    # --- Step 2: exposure ----------------------------------------------
    def test_gate_b_must_be_answered_on_every_deal(self):
        with self.assertRaises(ValueError):
            self.run_deal(gate_b_trialable=None)
        with self.assertRaises(ValueError):
            self.run_deal(gate_b_trialable=None, gate_a=m.GATE_A_GREENFIELD)

    def test_a_trialable_reversible_deal_sinks_nothing_specific(self):
        result = self.run_deal(gate_b_trialable=True)
        self.assertFalse(result.specific)
        self.assertEqual(result.governance, m.MARKET)

    def test_exposure_counts_integration_workflows_and_divergence(self):
        result = self.run_deal()
        self.assertEqual(result.exposure, 4 + 2 + 3)
        self.assertTrue(result.specific)

    def test_divergence_is_counted_only_against_an_encoded_workflow(self):
        result = self.run_deal(gate_a=m.GATE_A_GREENFIELD, divergent_steps=None)
        self.assertEqual(result.exposure, 4 + 2)

    def test_divergence_is_required_when_gate_a_says_encoded_and_b_fails(self):
        with self.assertRaises(ValueError):
            self.run_deal(divergent_steps=None)

    def test_divergence_never_moves_a_position(self):
        """It belongs to exposure. Earlier versions multiplied the
        implementation score by it and let discovery move the level."""
        aligned = self.run_deal(divergent_steps=0)
        misaligned = self.run_deal(divergent_steps=8)
        self.assertEqual(aligned.positions, misaligned.positions)
        self.assertGreater(misaligned.exposure, aligned.exposure)

    # --- Step 3 and 4: routing -----------------------------------------
    def test_a_pilot_request_overrides_the_counts(self):
        result = self.run_deal(n_alternatives=2, n_vetoes=1,
                               integration_points=0, changed_workflows=0,
                               undocumented_exceptions=0,
                               items_with_artifact=0, pilot_requested=True)
        self.assertEqual(result.route, "implementation")
        self.assertIn("pilot-override", result.flags)

    def test_a_cost_above_its_edge_keeps_the_buyer_out(self):
        result = self.run_deal(n_vetoes=9)
        self.assertEqual(result.route, m.KEEPS_OUT)
        self.assertEqual(result.sale_start, ("consensus",))

    def test_the_unnamed_category_deal_is_no_longer_turnkey(self):
        """The review's case: one decision maker, no integrations, an unnamed
        category. The retired level summed it to 11 and routed it Turnkey."""
        result = m.triage(3, 2, 0, 1, 1, 0, 0, 0, 0, m.RECURRENT, True,
                          category_named=False)
        self.assertEqual(result.route, m.KEEPS_OUT)
        self.assertEqual(result.sale_start, ("search",))

    def test_the_trialable_deal_gets_market_governance(self):
        """The review's case: trialable, four vetoes plus security review.
        The retired level scored it 18 and prescribed trilateral governance."""
        result = m.triage(3, 5, 4, 4, 0, 1, 0, 0, 0, m.ONE_SHOT, True,
                          formal_body_required=True)
        self.assertEqual(result.governance, m.MARKET)
        self.assertFalse(result.specific)

    def test_the_custom_interface_deal_is_a_light_sale_heavy_contract(self):
        """The review's case: one custom interface, one rewired workflow. The
        retired level scored it 3, Turnkey, market terms."""
        result = m.triage(3, 2, 4, 1, 1, 1, 1, 0, 2, m.RECURRENT, False,
                          divergent_steps=0)
        self.assertEqual(result.route, m.ALLOCATE)
        self.assertEqual(result.governance, m.BILATERAL)

    def test_every_cost_self_serve_and_nothing_specific_is_turnkey(self):
        result = m.triage(3, 3, 4, 1, 1, 1, 1, 0, 2, m.RECURRENT, True)
        self.assertEqual(result.route, m.TURNKEY)
        self.assertEqual(result.governance, m.MARKET)

    def test_the_sale_starts_at_the_largest_position(self):
        result = self.run_deal()  # search 0, consensus 0.5, impl 6/9
        self.assertEqual(result.sale_start, ("implementation",))
        self.assertEqual(result.route, "implementation")
        self.assertIn("full-chain", result.flags)

    def test_a_tie_is_run_together(self):
        # consensus 4 -> 0.5; implementation n = 6.5 is not possible, so tie
        # search 6 -> 0.5 against consensus 4 -> 0.5.
        result = self.run_deal(n_alternatives=6, integration_points=1,
                               changed_workflows=1, undocumented_exceptions=0,
                               items_with_artifact=1)
        self.assertEqual(result.sale_start, ("consensus", "search"))
        self.assertEqual(result.route, "consensus+search")

    def test_a_consensus_start_says_the_instrument_set_is_thin(self):
        result = self.run_deal(n_vetoes=6, integration_points=1,
                               changed_workflows=1, undocumented_exceptions=0,
                               items_with_artifact=1)
        self.assertEqual(result.route, "consensus")
        self.assertIn("consensus-instrument-set-is-thin", result.flags)

    def test_heavy_implementation_with_nothing_specific_is_flagged(self):
        """Possible over-frictioning: expensive work, not uncertain work."""
        result = self.run_deal(gate_b_trialable=True)
        self.assertEqual(result.route, "implementation")
        self.assertIn("heavy-sale-light-contract", result.flags)
        self.assertIn("possible-over-frictioning", result.flags)

    # --- Governance form -----------------------------------------------
    def test_the_four_forms_match_the_document(self):
        self.assertEqual(m.governance_form(False, m.ONE_SHOT), m.MARKET)
        self.assertEqual(m.governance_form(False, m.CONTINUOUS), m.MARKET)
        self.assertEqual(m.governance_form(True, m.ONE_SHOT), m.TRILATERAL)
        self.assertEqual(m.governance_form(True, m.RECURRENT), m.BILATERAL)
        self.assertEqual(m.governance_form(True, m.CONTINUOUS), m.UNIFIED_RISK)

    def test_a_specific_one_shot_deal_is_flagged_for_escalation(self):
        result = self.run_deal(frequency=m.ONE_SHOT)
        self.assertIn("specific-one-shot-escalate", result.flags)
        self.assertEqual(result.governance, m.TRILATERAL)

    def test_a_one_shot_deal_with_nothing_specific_is_not_flagged(self):
        result = self.run_deal(frequency=m.ONE_SHOT, gate_b_trialable=True)
        self.assertNotIn("specific-one-shot-escalate", result.flags)

    def test_making_a_deal_recurrent_changes_the_form_not_the_deal(self):
        one_shot = self.run_deal(frequency=m.ONE_SHOT)
        recurrent = self.run_deal(frequency=m.RECURRENT)
        self.assertEqual(one_shot.positions, recurrent.positions)
        self.assertEqual(one_shot.route, recurrent.route)
        self.assertNotEqual(one_shot.governance, recurrent.governance)

    def test_an_unknown_frequency_is_refused(self):
        with self.assertRaises(ValueError):
            self.run_deal(frequency="annual")

    def test_a_chaos_trap_has_no_governance_form(self):
        self.assertIsNone(self.run_deal(workflow_maturity=1).governance)

    def test_every_route_is_a_cost_or_a_documented_special_case(self):
        allowed = {m.CHAOS_TRAP, m.KEEPS_OUT, m.TURNKEY, m.ALLOCATE}
        for changes in ({}, {"n_vetoes": 9}, {"gate_b_trialable": True},
                        {"workflow_maturity": 1}, {"n_alternatives": 6}):
            route = self.run_deal(**changes).route
            parts = set(route.split("+"))
            self.assertTrue(route in allowed or parts <= set(m.COMPONENTS),
                            route)


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

    def test_the_edges_are_not_presented_as_measurements(self):
        doc = m.__doc__.lower()
        self.assertIn("edges", doc)
        self.assertIn("not measurements", doc)

    def test_named_parameters_ship_no_default(self):
        """The theory names the floor and the thresholds without valuing them,
        so the module must not value them either."""
        with self.assertRaises(TypeError):
            m.loss_chance([m.NormalizedGap(0.5)])
        with self.assertRaises(TypeError):
            m.threshold_position(0.5)

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
        self.assertEqual(m.SEARCH_EDGES, (4, 8))
        self.assertEqual(m.CONSENSUS_EDGES, (1, 7))
        self.assertEqual(m.IMPLEMENTATION_EDGES, (2, 11))
        self.assertEqual(m.SEARCH_EVIDENCE_ITEMS, 4)

    def test_beta_stays_inside_its_documented_range(self):
        with self.assertRaises(ValueError):
            m.consensus_friction(5, 0.25, beta=2.5)
        with self.assertRaises(ValueError):
            m.consensus_friction(5, 0.25, beta=1.0)

    def test_every_numeric_constant_is_listed_in_the_calibration_layer(self):
        """06-calibration.md is the single home for every value in the model.

        The point of quarantining the numbers is that a reader can accept the
        structural claims without accepting any of them, and that only works
        if the quarantine is complete. A constant that ships in the module and
        appears nowhere in the calibration layer is a number the framework is
        using and not declaring.
        """
        here = os.path.dirname(os.path.abspath(__file__))
        page = open(os.path.join(here, "..", "theory", "01-foundation",
                                 "06-calibration.md"), encoding="utf-8").read()
        # Names, not values: a value can legitimately appear under a different
        # label, but every knob has to be findable.
        knobs = ("ALPHA_COORDINATION",
                 "BETA_COMMITTEE", "GAMMA_TECHNICAL_OVERLAP", "W_TECH",
                 "W_PROCESS", "PHI_TECH", "PHI_PROCESS", "NU_VENDOR_DOUBT",
                 "KAPPA_PROOF_DECAY", "GAMMA_RESPONSIVENESS", "BCV_REF_DEFAULT",
                 "MIN_CREDIBLE_EDGE_CASES", "SEARCH_EVIDENCE_ITEMS")
        edges = ("SEARCH_EDGES", "CONSENSUS_EDGES", "IMPLEMENTATION_EDGES")
        missing = []
        for name in knobs:
            value = getattr(m, name)
            # The page may write 0.50 where repr gives 0.5, so accept either.
            forms = {str(value), "{:g}".format(value)}
            if isinstance(value, float):
                forms.add("{:.2f}".format(value))
            if not any(f in page for f in forms):
                missing.append("{} = {}".format(name, value))
        for name in edges:
            low, high = getattr(m, name)
            row = "| {} | {} |".format(low, high)
            if row not in page:
                missing.append("{} = {}".format(name, (low, high)))
        self.assertEqual(missing, [],
                         "values in the module that 06-calibration.md does not "
                         "declare: {}".format(missing))

    def test_the_calibration_layer_claims_nothing_is_measured(self):
        here = os.path.dirname(os.path.abspath(__file__))
        page = open(os.path.join(here, "..", "theory", "01-foundation",
                                 "06-calibration.md"), encoding="utf-8").read()
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
