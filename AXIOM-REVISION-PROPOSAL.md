# Axiom Revision Proposal

**Status:** Draft for review. Nothing in `theory/` or `practice/` has changed. Section 6 lists what is settled and what is still open.
**Date:** 2026-10-08, cost model added 2026-10-09

This file follows the precedent of the 2026-09 restructure plan: written at the root, reviewed, applied in steps, then retired to git history.

---

## 1. Why revise

An adversarial review of each axiom against its own mechanism, research files and model found that the core claim of each one holds, and that the statements and the math beneath them do not. The defects that drive this proposal:

1. **Axiom II defines specificity as total cost.** The Constitution sets $k = \lVert \mathbf{F} \rVert_1$, the sum of all three components, and the Deal Triage Calculator says "Level is asset specificity." Two of the three counts are vendors and veto holders, which have nothing to do with specificity. Run through `models/tcg_models.triage`, a trialable deal in an unnamed category with four vetoes scores level 18, Structural, trilateral governance. A single custom interface into a homegrown system plus one rewired workflow scores level 3, Turnkey. The first clause of the axiom is also circular under this definition: more total cost means more cost.
2. **The third component is filled with something its name excludes.** The Constitution calls it Coase's enforcement, defines it as the buyer's own adaptation work (line 75), and then says enforcement in Coase's sense is policing the seller and that adaptation is "the other half" (line 107).
3. **"The one that binds" is undefined.** The equation is additive, so no component binds in it. Largest share is used as a proxy for where seller effort pays most, without the assumptions that would make it one.
4. **The sum adds costs as though one party paid them all.** A forward-deployed engineer moves adaptation cost from buyer to seller and barely changes the total, yet it changes whether deals close. Each party decides on its own share.
5. **The three-way decomposition is uncited.** Its names are Dahlman's (1979), and Dahlman appears nowhere in the repository.

Axiom III's math, the bounded multiplier, the reduced form and the coefficient $a$, was the subject of the second phase of this review, and section 4 carries its replacement.

---

## 2. The frame: three decisions, in time order

| Axiom | The decision | Source |
|---|---|---|
| **I** | Should I use the market? | Coase (1937) for the question. Dahlman (1979) for the three costs. |
| **II** | What will it cost me today? | Williamson (1985), ex ante costs: drafting, negotiating and safeguarding the agreement, and the investment each party makes to get the transaction running. |
| **III** | What might it cost me later? | Williamson (1985), ex post costs: maladaptation, haggling, running the governance, bonding. Klein, Crawford and Alchian (1978) for why sunk specific investment creates them. |

The levels change meaning. The current Constitution indexes the axioms on market, workflow and deal. This frame indexes them on the decision and its time: whether, how much now, how much later. **Open:** whether the four Definitions (market, workflow, seat, deal) survive as units the axioms are read at, or become vocabulary only.

**Why both Dahlman and Williamson.** They answer different questions. Dahlman classifies transaction costs by kind and supplies the names Axiom I uses. Williamson splits them by time, before and after the agreement, and makes asset specificity the thing that creates the after. The split by kind is Axiom I. The split by time is the line between Axioms II and III.

**Dahlman's objection, answered in advance.** Dahlman argued the three reduce to one cost, resource losses from imperfect information. The framework's reply is that they respond to different seller investments, so they are separate for the purpose of choosing what to invest in, whatever their common root. That reply should be stated in the Constitution, since a reader who knows Dahlman will raise it.

---

## 3. The draft axioms

### Axiom I: The Law of Transaction Cost Composition

**Decision:** Should I use the market? It is the buyer's decision. The seller reads it to know where the sale starts.

> **Using the market costs the buyer three things beyond price: search and information, bargaining and decision, and policing and enforcement. A buyer will not use the market while any one of them exceeds what it will bear, and among costs it will bear, their relative size is where the sale starts.**

*Plain English: buying costs more than money. Finding the right seller, getting your own organization to decide, and making sure the seller delivers are three separate bills. If any one of them is too high, the buyer stays out of the market altogether. If all three are bearable, the largest is the first thing a seller has to pay down.*

**Mechanism.** Each cost yields to a different seller investment.

| Cost | The buyer's question | What lowers it |
|---|---|---|
| Search and information (field name: search) | Which solutions exist, and does this one fit? | Category definition, education, reachable channels |
| Bargaining and decision (field name: consensus) | Can my organization agree to this? | Decision-role mapping, an arrangement each role can say yes to |
| Policing and enforcement (field name: implementation) | Will the seller deliver what was promised, and will it work here? | Outside validation: referrals, references, guarantees, a channel with a stake |

The third row carries Dahlman's meaning, and the field keeps calling it implementation, because "will this get implemented and work" is the buyer's form of the policing question. The buyer's adaptation work, the integrations built and workflows rewired, is not itself this cost. It is one of the investments Axiom II says pay it down, and a forward-deployed engineer is the same investment made by the seller.

**Each cost is also a participation threshold.** Every cost has a level above which the buyer does not enter the market at all: a search cost too high to start, a decision the organization cannot reach, a delivery risk nobody can bound. A cost at a small share of the total can still end the deal this way, so relative size orders the costs only among those the buyer will bear. This is where Akerlof's exit lands in the framework: a buyer who cannot afford to tell good sellers from bad stays out. Whether the threshold rises with the value at stake is still open, section 6.

**What changes from the current axiom.**
- "The one that binds selects the motion" becomes "their relative size is where the sale starts." The claim is about sequence: which cost the seller pays down first.
- Coase's two-word names become Dahlman's full names, and Dahlman is cited.
- Each cost becomes a participation threshold as well as a share, so a single cost can end a deal at a small share.

**Corollary: Turnkey is a market condition, and it does not last on its own.** Turnkey is the condition under which product-led growth works. It holds when every one of the three costs sits below a second, lower threshold, the level at which the buyer can pay it down alone, with no seller investment, and when nothing specific is sunk under Axiom III. Each cost is tested on its own and not in a sum. The current calculator shows why: a buyer who cannot name the category, with one decision maker and no integrations, scores search at 9 of 10 and 90% of the direction, sums to 11, and is routed Turnkey to a self-serve motion the buyer will never find.

The condition erodes because of what defines it. A motion that needs little seller investment is cheap to copy, so competitors enter. Entry raises search and information cost directly, because every entrant is another alternative to rule out, and it raises policing and enforcement cost through pooling, because free trials and identical claims stop separating good sellers from bad. A Turnkey market leaves the condition unless something holds search cost down as sellers arrive: a de facto standard, a network effect, a dominant brand, or a channel that does the filtering and has a stake in getting it right. [07-open-questions.md](./theory/01-foundation/07-open-questions.md) item 27 already records that a named category can slide back to pooling. Entry is the mechanism that register entry was missing.

**Corollary: copying a motion copies another market's costs.** A motion that worked in one market is adopted in another by imitation, which the Constitution already names as the organization-level mis-composed failure. It runs both ways. Product-led growth where the costs are not all low under-invests, and leaves the buyer holding costs it cannot pay down alone. Forward-deployed engineering where the policing and enforcement cost is not what keeps the buyer out over-invests, and pays down an adaptation nobody was worried about. Read the other way, the investment a motion demands is also its defense against entry: forward-deployed engineering is expensive to copy, and product-led growth is cheap.

**Falsifier.** In a book of deals, those where the seller's first investment went to the largest cost convert no faster than matched deals where it went elsewhere. Or buyers facing one cost above any plausible threshold participate at the same rate as buyers who do not.

**Falsifier for the entry corollary.** In categories where self-serve selling dominated, a rising vendor count should come before falling trial-to-paid conversion and the arrival of sales-assist teams. Conversion that falls with no rise in entry, or entry that leaves conversion unchanged, refutes the mechanism. This corollary is new theory rather than repair, and it is the first claim in the framework about how a market's costs move over time.

### Axiom II: The Law of Transaction Investment

**Decision:** What will it cost me today? Asked by each party separately.

> **Each of those costs is paid down by an investment from the buyer, the seller or both, and each party goes ahead only when its own share is covered by its own return.**

*Plain English: someone has to pay to get the deal done, and it does not have to be the buyer. Each side asks whether its own part is worth it, and the deal happens only when both say yes.*

**Mechanism.** The deal has two conditions, one per party. The repository already carries the second one in [04-seller-surplus-model.md](./theory/01-foundation/04-seller-surplus-model.md), as a supplement to the Constitution. This axiom promotes it.

- **Buyer:** the value of switching exceeds the price plus the buyer's share of today's investment plus the buyer's expected future cost from Axiom III.
- **Seller:** the margin over the relationship exceeds the seller's share of today's investment plus the seller's expected future cost from Axiom III. Today this is $S_{seller} = p_{close}(V_{contract} - C_{deliver}) - C_{invest}$.

**Price is a transfer, not a transaction cost.** Once each party has its own condition, price is visibly what leaves the buyer and arrives at the seller. It belongs in both conditions and in neither party's transaction cost. This settles the inconsistency the review found, where Axiom I excludes price and the reduced form $y = a\hat{\Delta}^2 + c$ includes it.

**Moving cost between parties is the seller's main lever.** A forward-deployed engineer, a paid pilot, or a seller-built integration moves part of today's investment from buyer to seller. The move is worth making when it lowers the joint cost, because the seller does the work more cheaply or because doing it shrinks a future cost under Axiom III. It closes the deal when it lifts the buyer above zero without pushing the seller below. The seller's cost of acquiring customers lives here as the seller's share.

**What changes from the current axiom.**
- Asset specificity leaves this axiom and moves to Axiom III, where Williamson puts its effect.
- The buyer's adaptation work, the integrations built and workflows rewired, lands here as investment.
- "Allocated before signature" becomes "allocated before the investment is sunk," and moves with specificity to Axiom III.
- The summed level stops deciding anything. Section 4.5 replaces it.

**Falsifier.** Deals where the seller absorbed part of the buyer's investment close at no higher rate than matched deals where it did not, at equal total cost.

### Axiom III: The Law of Future Cost

**Decision:** What might it cost me later? Asked by each party separately.

> **Whatever a party sinks that is worth less outside this relationship exposes it to what it cannot verify later. That exposure is a future cost, it rebuilds unless maintained, and its allocation must be settled before the investment is sunk.**

*Plain English: once you have spent money that only pays off with this partner, you are exposed to everything you could not check in advance. That risk is part of the price of the deal, it grows back if nobody tends it, and who carries it has to be agreed before anyone spends.*

**Mechanism.** Two of Williamson's three dimensions, combined. Specificity creates the exposure: the appropriable quasi-rent of Klein, Crawford and Alchian, already in the repository as $Q = C_{invest} - R_{redeploy}$. Uncertainty decides how much of the exposure turns into cost: what the party cannot verify about the other side's performance, about its own fit, and about its own coalition. Frequency, the third dimension, decides what arrangement can hold the exposure, and the governance forms carry over as corollaries.

**What carries over from the current Axioms II and III.**
- The governance forms, the staging argument and mutual sanction (05-governance-forms.md, real-options.md).
- The per-component gaps and the Friction Allocation Principles. Spence's single crossing is limited to signals the seller sends, per the review.
- Drift and reputation depreciation, as the "rebuilds unless maintained" clause.
- The gate, restated: where nothing specific is sunk and a trial verifies fit, the future cost is near zero and market terms hold. That is now a corollary of this axiom instead of the role of Axiom II.

**Whose exposure.** Both parties'. The forward-deployed engineer is the clean case: the seller takes on today's investment under Axiom II, shrinks the buyer's future cost under this axiom, and inherits a future cost of its own, because its sunk engineering is specific to this buyer.

**Falsifier.** Specific deals with pre-agreed staging and stop rights retain no better than specific deals without them.

### Routing outside Turnkey, and the retirement of Structural

The current Turnkey and Structural boundary answers two questions with one number: how much the seller must invest today (Axiom II), and whether anything specific is sunk (Axiom III). The two come apart, and the deals the current level misclassifies sit exactly where they do. Structural is retired as a label. Turnkey survives as the market condition in Axiom I. Deals outside it are routed on the two readings directly.

| | Nothing specific sunk | Something specific sunk |
|---|---|---|
| **Light investment today** | Turnkey, if the market condition also holds. Self-serve and standard terms. | **Light sale, heavy contract.** Easy to sell, but staging and stop rights must be agreed before the specific investment is sunk. A custom interface into a homegrown system plus one rewired workflow sits here, and the current level scores it 3. |
| **Heavy investment today** | **Heavy sale, light contract.** The seller pays down search or decision costs, then standard terms hold. A trialable product in an unnamed category with four veto holders sits here, and the current level scores it 18 and prescribes trilateral governance. | **The full implementation chain.** Blueprint, Red Team, Mutual Implementation Plan, Adoption Review. |

The cell names are working labels. Section 4.5 says how each reading is measured.

---

## 4. The cost model

Phase two, agreed on 2026-10-09. The model is rebuilt from what the three axioms need, not from the current equations.

| Axiom | What it computes | What that needs |
|---|---|---|
| I | Is any cost above the buyer's participation threshold? Are all three below the self-serve threshold? Which cost does the sale start with? | Comparisons only. Each cost against its own two thresholds. No sum and no ratio. |
| II | Does each party's share of today's investment fit inside its own return? | Money, per party. Hours, headcount and integration effort can be estimated in it. |
| III | What does each party expect to lose later, given what it sank and what it could not verify? | Money for the exposure, and a probability-like term driven by the gaps. |

**Units.** The theory states Axioms II and III in fractions of annual contract value, which is what investment and exposure can actually be estimated in. The field instrument stays in counts and emits zones. It never claims a money figure.

### 4.1 Two conditions, one per party

$$S_b = V_{switch}(t) - P - \sum_k I^b_k - L_b \qquad S_s = P - C_{deliver} - \sum_k I^s_k - L_s$$

Where $V_{switch}(t) = V_{solution}\,e^{-\delta t} - V_{next\_best}$ keeps the second standing assumption, $P$ is price over the relationship, $I^b_k$ and $I^s_k$ are what the buyer and the seller invest today against cost $k$, and $L_b$ and $L_s$ are each party's expected future loss from Axiom III. The deal happens when both are positive, and when Axiom I's gate holds: every cost $F_k$ the buyer faces sits below its participation threshold $\tau^{part}_k$.

The seller's condition is today's $S_{seller} = p_{close}(V_{contract} - C_{deliver}) - C_{invest}$ with the investment split by component and the future loss made explicit. Recurrence enters through $P$ and $C_{deliver}$ summed over expected renewals, which `repeated_seller_surplus` already computes.

### 4.2 Price cancels, and that carries three results

Adding the two conditions:

$$S_b + S_s = V_{switch}(t) - C_{deliver} - \sum_k \left(I^b_k + I^s_k\right) - L_b - L_s$$

$P$ is gone, because price is a transfer. Three results follow from the accounting rather than from any coefficient.

1. **Price is not a transaction cost.** The contradiction between Axiom I's "beyond price" and the reduced form's $c$ disappears.
2. **Verification beats discounting, and no curve is needed to say so.** A discount moves $P$, so it shifts surplus from seller to buyer one for one and leaves the joint surplus where it was. Verification lowers the chance of future loss, so it shrinks $L_b$ or $L_s$, a cost both sides were carrying. A guarantee or a clawback sits between the two: it moves loss from buyer to seller, which is a transfer, unless it also changes what the seller does, in which case it lowers the loss as well. The old conjecture rested on $a = 2.25$ and a squared term. The new claim rests on what a transfer is. What stays empirical is whether a given verification costs less than the loss it removes.
3. **Moving investment between parties changes the split, not the total,** unless the party taking it on does the work more cheaply, or doing it lowers a future loss. A forward-deployed engineer is the case where both hold: the seller's engineers adapt their own product at lower cost, and their presence in use catches misfit early, which lowers $L_b$. It also creates $L_s$, because the engineering is specific to this buyer.

### 4.3 Future loss

$$L_p = Q_p \cdot \pi_p, \qquad p \in \{b, s\}$$

$Q_p$ is what party $p$ has sunk that is worth less outside the relationship, the appropriable quasi-rent already in the model as $Q = C_{invest} - R_{redeploy}$, now read for both parties. $\pi_p$ is the chance it does not come back. It rises with the gaps party $p$ cannot close, and it has a floor above zero, because some risk survives any amount of proof: the floor `buyer_uncertainty_floor` already models for return variance. Its shape is not claimed. The model will carry a straight line between the floor and the ceiling as a placeholder, declared as chosen.

**Which gaps feed which party.** The buyer's loss runs mainly on the implementation gap, whether the seller delivers and the product fits, and on the consensus gap, whether the coalition holds once the investment is sunk. The seller's loss runs on the buyer-side gaps, the environment it could not map and the coalition it could not see.

**Staging is the same equation at each gate.** A buyer who commits in stages sinks $Q_m$ at gate $m$ against residual uncertainty $x_m$, so the expected loss is $\sum_m Q_m\,\pi(x_m)$ rather than $Q\,\pi(x_0)$. Staging puts the small commitments where the uncertainty is high, and a right to stop caps what each gate can lose. This replaces the Milestone Valuation Model's stage equation, which ran on $a\,x_m^2$.

**The bargaining gap gets one definition:** the share of decision roles whose occupant has stated their own exposure. [08-from-axioms-to-instruments.md](./theory/01-foundation/08-from-axioms-to-instruments.md) section 2.2 already states it. The other three readings retire.

### 4.4 Drift, bounded

$$\hat{\Delta}_k(t) = 1 - \left(1 - \hat{\Delta}_k(0)\right) e^{-\gamma_k t}$$

A gap rebuilds toward its ceiling and never past it. Discovery is a separate, discrete step down that someone pays for at an artifact boundary, so drift and discovery are two causes rather than one mechanism with two signs. The code's refusal of a negative rate becomes correct instead of contradicting the text. The rates $\gamma_k$ stay named and not valued.

### 4.5 The field instrument: zones, not scores

The Deal Triage Calculator keeps its counts, its evidence fractions, Step 0, both gates and the frequency reading. It drops the sum, the 15 boundary, the shares and the 0.50 dominance threshold, which removes the cliff the calibration page records as a known defect.

**Each cost lands in one of three zones**, set by two band edges per component:

| Zone | Meaning | Route |
|---|---|---|
| Self-serve | The buyer can pay this cost down alone | No seller investment on this cost |
| Needs investment | Bearable, but only with seller investment | The seller invests here |
| Keeps the buyer out | Above the participation threshold | Pull it back into range first, or decline |

**Where the sale starts:** the cost in the highest zone. Within a zone, the cost nearest its own participation threshold, read as position between that component's two edges. Two costs at the same position are run together, in proportion, rather than one being picked.

**The 2x2 reads directly off the instrument.** The row is the zones: light investment means all three costs are self-serve, and heavy means at least one needs investment. The column is a specific-exposure reading built from what the current calculator already counts: divergent steps, integration points, and changed workflows. Gate B passing, a buyer who can trial and walk away, sets it to none. The divergence modifier moves here, out of the level, which resolves fix 1 in section 7 by deleting the thing it contradicted.

**The Market Reading** takes the same zones across a buyer population. Turnkey is the population where every cost is self-serve and nothing specific is sunk.

### 4.6 What retires

| Retires | Why |
|---|---|
| The level $\lVert \mathbf{F} \rVert_1$ and the 15 boundary | Summed costs that were never on a common scale, and it was standing in for specificity |
| Direction shares and the 0.50 threshold | Ratios of ordinal scores, and a cliff |
| The multiplier $(1 + \hat{\Delta}_k)$ and the deal-level gap $\hat{\Delta}_A$ | Capped at doubling, so it could not produce exit. Uncertainty now does two other jobs: it is most of what today's search and policing costs are made of, and it drives the chance of future loss |
| $y = a\hat{\Delta}_A^2 + c$, the coefficient $a = 2.25$, the convexity exponent and $b$ | Convexity came from counting uncertainty twice, and the anchor produces a kink rather than a curve. Section 4.2 makes the argument without them |
| The stage equation $S_m = p_m[V_{gross,m} - (a x_m^2 + c_m)]$ | Rebuilt on expected loss in section 4.3 |
| Linear drift | Unbounded, and it left the range the gap is defined on |

**What survives unchanged:** value decay and its catalyst term, the two halves of the implementation gap and their floor, the decision cost's structural form $\alpha N^{\beta}(1 + \text{Var}(I_i))$ with $\alpha$ now carrying money, the quasi-rent, the seller's repeated game, and the cooperation threshold.

### 4.7 New parameters, for the calibration page

| Parameter | Provenance |
|---|---|
| Two band edges per component, self-serve and participation | **Chosen.** Placed on the existing count bands |
| The floor of $\pi$ | **Structurally motivated.** It exists because return variance survives any proof. The value is chosen |
| The shape of $\pi$ between floor and ceiling | **Chosen.** Straight-line placeholder, curvature unclaimed |
| The drift ceiling, 1 | **Convention.** The top of the range the gap is defined on |
| $\gamma_k$ | **Named, not valued.** Unchanged |

---

## 5. Where the existing pieces land

| Piece | Today | Under this proposal |
|---|---|---|
| The three components | Search, bargaining, enforcement, with field names consensus and implementation | Dahlman's three costs, field names kept. Adaptation work becomes an Axiom II investment against the third cost. |
| Level, the 0 to 30 sum | Called specificity, sets Turnkey or Structural | Retired. Section 4.5 replaces it with zones and a specific-exposure reading. |
| Direction | Largest effective share selects the motion | Retired as a share. The sale starts at the cost nearest its own participation threshold. |
| Turnkey and Structural | Deal classes set by the level | Turnkey becomes a market condition: every cost self-serve, nothing specific sunk. Structural is retired, and deals outside Turnkey route on the 2x2 in section 3. |
| Deal Triage Calculator | Emits level, direction, frequency | Emits a zone per cost, where the sale starts, a specific-exposure reading, frequency and governance form. Counts and gates kept. |
| The Fundamental Equation | One buyer-side surplus | Two conditions, one per party, section 4.1. CLAUDE.md, the README and the glossary carry it and change with it. |
| Seller surplus model | A supplement to the Constitution | Promoted into Axiom II |
| Milestone Valuation Model | Stage equation on $a\,x_m^2$ | Rebuilt on expected loss per gate |
| Bilateral Asymmetry Scorecard | Feeds the multiplier on the implementation cost | Feeds $\pi$ for the implementation gap |
| Governance forms | Corollaries of Axiom II | Corollaries of Axiom III |
| Blueprint, Red Team, MIP, Adoption Review | The implementation-led chain | Kept. The Blueprint prices today's investment, the MIP allocates the specific part before it is sunk, the Adoption Review maintains against rebuild. |
| Implementation-led motion | Named after the enforcement component | Name kept. Led by the policing and enforcement cost, and run by the seller co-investing in the buyer's adaptation today to shrink the future cost. |
| Market Reading | Level and direction on base friction across a population | Zones across a population, section 4.5 |
| Friction Efficiency Index | Retrospective measures | Unaffected in this pass. Its committee correction uses $N$, which survives |

---

## 6. Decisions

Settled on 2026-10-08:
- The field names stay, and implementation is policing and enforcement.
- Each cost is a participation threshold.
- Turnkey is a market condition, tested cost by cost, and erodes through entry. Structural is retired.
- Workflow stays a Definition, because Axiom III's specificity is read as the buyer's divergence from the workflow the product assumes. Market and deal become plain vocabulary.
- Seat becomes decision role. The definition keeps the rule that a role is a position, not a person, so an occupant leaving reopens a gap while the role dissolving changes the deal. A canonical rename: about 50 uses, mostly in 08-from-axioms-to-instruments.md and the Market Reading, plus a `RetiredTerms.yml` entry.

Settled on 2026-10-09:
- Money in the theory, zones in the field.
- The sale starts at the cost nearest its own participation threshold. Agreed as the starting reading, to revisit once the zones exist.
- $y = a\hat{\Delta}^2 + c$ and $a = 2.25$ retire.

Still open:
1. **Whether the participation threshold rises with the value at stake.** A buyer plausibly tolerates a higher search cost for a bigger prize. That is a structural claim, and stating it would put value into Axiom I's gate.
2. **Where the band edges sit.** Chosen values, to be set when the calculator is rebuilt.

---

## 7. Fixes that do not wait for the revision

Each is a mismatch between two files, or a stale pointer, and holds under the current axioms and the proposed ones alike.

1. The divergence modifier enters the level in the code (`models/tcg_models.py`, `implementation_score`) and "never" does in [deal-triage-calculator.md](./practice/deal-triage-calculator.md) line 161. By CLAUDE.md, the document is the specification.
2. The level's floor is 3, not 0, because every component scores at least 1.
3. [tce-empirical-record.md](./theory/02-research/tce-empirical-record.md) line 41 marks Axiom II "Supported." The robust result is that specificity predicts governance form, not that it raises transaction cost.
4. [04-seller-surplus-model.md](./theory/01-foundation/04-seller-surplus-model.md) line 60 says Axiom II treats specificity as the buyer's problem, which the Constitution no longer says.
5. [friction-allocation-diagnostic.md](./practice/friction-allocation-diagnostic.md) lines 108 and 168 send reputation depreciation to Axiom II. It sits under Axiom III.

---

## 8. Sequence once approved

1. Rewrite the Constitution, bump it to 4.0 with the README footer, and record the retired terms.
2. Rewrite 02-mathematical-models.md and the calibration page against section 4, then `models/tcg_models.py` and its tests, in the order CLAUDE.md fixes for an equation change: document first, then code, then figures.
3. Rebuild the Deal Triage Calculator, the Milestone Valuation Model and the Market Reading.
4. Propagate the rest: glossary, CLAUDE.md, README, then publishing.
5. Retire this file.
