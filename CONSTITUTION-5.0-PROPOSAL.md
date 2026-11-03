# Constitution 5.0 Proposal

**Status:** Draft for review. Nothing in `theory/` or `practice/` has changed. Section 8 lists the choices still open.
**Date:** 2026-11-02

This file follows the precedent of the 4.0 revision proposal: written at the root, reviewed, applied in steps, then retired to git history. It records ten decisions taken in review between 2026-10-27 and 2026-11-02, and turns each into proposed text.

---

## 1. Why revise

Constitution 4.0 fixed the mechanics. This revision asks whether the position can be defended in public against the frameworks a founder or revenue leader already uses. Five findings drive it.

1. **"Value" means two things.** The second standing assumption says willingness to pay is exogenous. The glossary defines $V_{solution}$ as "peak perceived value." Perceived value is exactly what value sellers claim to move, so the assumption as written is either false or circular.
2. **"Never summed" overclaims.** The buyer's condition already subtracts the sum of the buyer's investments, so the costs add in money terms. What 4.0 meant, and what is worth defending, is that ease on one cost cannot buy back another above its threshold.
3. **Axiom III covers only what cannot be verified.** Wathne and Heide (2000) show hold-up under full information: a party can see the other side refuse to adapt or force a renegotiation and still be unable to stop it. Verification instruments do nothing about that case, and it is how most incentive drift after signature looks.
4. **No cost has a cost floor.** Part of each cost is set outside the deal, by the information environment, the buyer's institutions and the measurement environment. The Constitution treats every cost as the seller's to pay down, and so cannot explain deals that fail for reasons no seller controls.
5. **The neighbors are uncredited.** Research pass 2 found no prior work making TCG's assembly, and found close neighbors for most of its parts. Cannon and Homburg (2001), Wathne and Heide (2000), Buchanan and Tullock (1962) and Hockenmaier (2023) appear nowhere in the repository.

---

## 2. The position, in three lines

For founders and revenue leaders, with health tech as the home case:

- **Hook, the cost floor.** Some of your cost of sale cannot be lowered by any seller in any one deal. Channel noise, the buyer's procurement and compliance rules, and outcomes nobody can attribute are set by the market you sell into, so the first decision is where to sell.
- **Thesis, non-compensatory costs.** A buyer pays three costs beyond price: finding and trusting a seller, getting its own organization to agree, and making sure the seller delivers. The deal dies at the cost nearest its own threshold, and effort spent making the other two easier does not rescue it.
- **Recurring line.** A discount moves the surplus. Verification creates it.

Every change below serves one of the three. The PLG-as-market-condition claim stays in the Constitution and is held back from publication until a market where it fits, since health tech has few self-serve categories.

---

## 3. Changes to the Constitution

Each change gives the current text, the proposed text, the evidence, the falsifier and the register entries it closes or opens. Each falsifier is tagged **public** (testable from published evidence) or **deal data** (needs a book of deals someone else holds). By decision 10, no test relies on HTD data, anonymized or not.

### 3.1 Standing assumption 2: three kinds of value

**Current** (line 25):

> **Value is exogenous to the seller, and it decays.** Willingness to pay is a property of the product and the buyer's situation. The seller's levers are the cost of transacting and who bears it.

**Proposed:**

> **Value is exogenous to the sale, and it decays.** For a given offer, what the change can be worth to this buyer is its *realizable value*, set by the product and the buyer's situation: its workflow, its alternatives and what it will invest in adoption. The seller can change the offer, which is a product decision even when it is made inside a deal. Within the sale, the seller moves only the buyer's *recognized value*, its current estimate of realizable value, usually held as a range, and what the buyer pays. Evidence that narrows that range by means the buyer can check lowers the search cost. A claim that moves the estimate without narrowing the range is persuasion, and the buyer carries the gap as exposure under Axiom III, realized when delivery makes it visible. What the buyer captures after go-live is its *realized value*, which adoption and delivery raise toward realizable. Where value moves during a cycle it moves down, from the triggering event.

*Plain English: the seller cannot make the product worth more to this buyer without changing the product or the deal. The seller can help the buyer see what it is worth, honestly or not. Honest help narrows the buyer's uncertainty with proof the buyer can check. Dishonest help inflates the estimate, and the buyer pays for the difference later.*

Three clarifications go with it, each settled in review:

- **Helping the buyer win budget or a mandate lowers the bargaining cost.** It does not change the buyer's state.
- **Naming a real catalyst is recognition.** The catalyst already existed, and the seller made it visible.
- **Scope, bundling, customization and committed services change the offer,** so "for a given offer" carries them.

**Notation.** $V_{solution}$ means realizable value. The buyer evaluates its condition on recognized value, written $\tilde{V}_{solution}$, so at the moment of decision $V_{switch}(t) = \tilde{V}_{solution} \cdot e^{-\delta t} - V_{next\_best}$. The chance that realized value falls short of what the buyer recognized enters $L_b$ through $\pi_b$, so persuasion that inflates $\tilde{V}_{solution}$ raises the buyer's expected future loss by the same mechanism Axiom III already prices. The joint surplus, where price cancels, is read on realizable value. The glossary's "peak perceived value" becomes the definition of $\tilde{V}_{solution}$.

**Evidence.**
- Kamenica and Gentzkow (2011) hold the payoff fixed and show the seller works only on beliefs.
- DellaVigna and Gentzkow (2010) split persuasion into belief-based and preference-based, which is the same split.
- Anchoring and framing effects shrink with buyer expertise, information and comparators.
- The largest business anchoring effect, on first offers, moves price, which is already a transfer.
- The penalty for inflation depends on post-sale verifiability rather than on the size of the oversell. Expectation-disconfirmation research finds assimilation on average.
- A buyer's conviction can raise its own adoption effort. TCG prices that as buyer investment under Axiom II rather than as value moving.

**Falsifier (deal data).** Code each won deal's pre-signature value claims as verified on the buyer's own data or situation, or asserted from vendor benchmarks and other customers' cases. Hold the claimed magnitude constant.
- TCG predicts win rate depends mostly on verification and weakly on magnitude.
- Value selling predicts magnitude matters whatever the verification mode.
- Among won deals with outcomes the buyer can measure, a larger gap between claimed and realized value should lower net revenue retention. Among deals with unmeasurable outcomes it should not. A penalty in the unmeasurable group counts against the Axiom III mechanism.

**Register.** Replaces open question 20. Opens a new entry for the strongest objection: preferences for unfamiliar, complex purchases may be constructed during evaluation (Payne, Bettman and Schkade 1999), so realizable value may have no stable referent before the sale.

### 3.2 Axiom I: the costs add, and they do not compensate

**Current** (line 81):

> A cost at $r_k > 1$ keeps the buyer out, whatever the other two read. **The sale starts at the largest $r_k$.** Each cost is measured against its own thresholds and never summed with the others, so the three are comparable without sharing a scale, and a cost at a small share of the total can still end the deal.

**Proposed:**

> A cost at $r_k > 1$ keeps the buyer out, whatever the other two read. **The sale starts at the largest $r_k$.** Each cost is measured against its own thresholds, so the three are comparable without sharing a scale. **The costs are non-compensatory.** They add, in the buyer's condition under Axiom II and wherever one payer carries more than one of them, but ease on one never buys back another above its threshold. Where a single person or budget pays more than one cost, those costs draw on one capacity, and the participation test applies to their total as well as to each.

The axiom statement gains three words, "however low the other two": *A buyer will not use the market while any one of them exceeds what it will bear, however low the other two, and among costs it will bear, their relative size is where the sale starts.*

**Why this holds together.** The costs act separately because different people and budgets pay them: the researcher pays search, the committee pays bargaining, operations pays policing. The fewer the payers, the more the thresholds collapse toward one shared capacity. A one-person buyer approaches a single summed test. A large coalition approaches three separate ones. Open question 30 already settled that the participation threshold is capacity, so this is that settlement applied to a shared payer.

**Evidence.**
- Ellram (1993, 1995): total cost of ownership sums the buyer's costs beyond price for supplier selection. TCG concedes the sum and denies the offset.
- Cannon and Homburg (2001): near 500 buying organizations expand purchases from suppliers that lower each of their costs. They model the effects as additive, and TCG predicts an interaction.
- The Skok and Janz contract-size heuristic: spend-based approval rules make price cause bargaining cost. That is a bargaining floor (section 3.4), and it explains why the heuristic works where approval tracks spend and breaks where something else drives the bargaining cost.

**Falsifiers.**
- *Deal data.* Large-buyer deals blocked on one cost are rescued by lowering the other two.
- *Deal data.* Small-buyer deals show no response to lowering a cost that is not the largest.
- *Public, partial.* Cannon and Homburg's kind of survey data can test the interaction directly: lowering a cost not nearest its threshold should do little until the binding one falls.

**Register.** No entry closes. Item 3 (coupling) gains a note: shared capacity is one coupling the Constitution now states.

### 3.3 Axiom I: contracting is part of the bargain

**Current** (bargaining row, line 70):

> The buyer is a coalition, not an agent. Most of the bargain is internal, among the decision roles, before any term is negotiated with the seller (Webster and Wind 1972).

**Proposed:**

> The buyer is a coalition, not an agent. The bargain has two parts. One is internal, among the decision roles (Webster and Wind 1972). The other is with the seller over terms: procurement, legal, security review and the paper process. Negotiating a term is bargaining cost paid today. What the term governs after signature belongs to policing and enforcement, which is Williamson's line between ex ante and ex post.

Buchanan and Tullock (1962) join the citation. Their decision-making cost rises with the share of a group whose agreement is required, which is the theory under the coalition claim. They add that groups require more approvers when the stakes are high, so part of the bargaining cost responds to Axiom III exposure.

**Falsifier.** Inherited from Axiom I. Contracting needs none of its own unless it is claimed as a fourth cost.

**Register.** Item 1 updates: contracting has been tested against the separateness rule and folded into bargaining. Exit cost remains the only candidate fourth cost.

### 3.4 New corollary: every cost has a cost floor

The cost floor follows from Axiom II, so it enters as a corollary there rather than as a new axiom. Each party goes ahead only when its own return covers its own share. The cost floor is the part of a cost whose paydown no single deal's return can cover. The name keeps it apart from the floor above zero on $\pi_p$ in Axiom III, which keeps its existing wording.

**Proposed corollary, under Axiom II:**

> **Every cost has a cost floor.** Part of each cost is set outside the deal. For search it is the information environment: the volume of messages against the buyer's attention, and the record of the category the seller inherits. For bargaining it is the buyer's institutions: procurement rules, spend thresholds, required reviews and how decisions get made. For policing it is the measurement environment: whether outcomes can be attributed, what standards exist and how verifiable delivery is. No seller can lower a cost floor within one deal at a return that deal repays, because the return is shared by every deal sitting on it. A cost floor falls only through investment made across deals, such as a marketplace, a certification, an intermediary with a stake or a standard, or is cleared by a signal costly enough to separate the seller from the pool. Otherwise the seller chooses its cost floors when it chooses its market and channel. Cost floors move. The search cost floor rises as the volume of messages outgrows the attention buyers can give them, and cheap seller effort raises it further.

A column goes into the Axiom I mechanism table, "What sets its cost floor," with the three entries above. The corollary also gets a row in Part II's derivation table, from Axiom II applied to Axiom I.

**What it absorbs.** The Turnkey erosion corollary becomes a case of the cost floor: entry raises the search cost floor and pools the policing signals. The Jevons-collapse failure mode is the search cost floor rising when sending becomes free. Both stay where they are and point here.

**Evidence.**
- *Search:* Anderson and de Palma (2009) show message congestion as an externality among senders. Van Zandt (2004) shows receivers become the bottleneck as sending costs fall. Tirole (1996) shows a new entrant inherits its category's reputation. Together these reconcile Bakos (1997), where digitization lowers search cost per alternative, with the user's observation that total volume now outruns attention.
- *What lowers cost floors:* Biglaiser (1993) on expert middlemen, Lizzeri (1999) on certifiers, and Spulber (1996, 1999) on intermediation. Lizzeri adds a caution for Friction Allocation Principle 4: a monopoly certifier reveals only pass or fail.
- *Bargaining:* Ouchi (1980) separates goal incongruence from performance ambiguity, and the cost floor is the institutional part of the first.
- *Policing:* Holmström (1979), Baker (1992) and Holmström and Milgrom (1991) show measurement noise decides which contract forms work. Filippas, Horton and Golden (2022) show reputation measures inflate and lose information.
- *Placement in TCE:* Williamson (1991) treats the institutional environment as shift parameters on the comparative cost of governance, which puts the cost floor inside transaction cost economics rather than beside it.

**Falsifier (public, partial).** Holding deal-level effort fixed, sellers who invest in shared institutions (marketplace contracts, certifications, consortia, standards bodies) clear deals in markets where equally strong sellers who invest only deal by deal fail. Public procurement records and certification registries can test part of this. The search-floor claim has a cleaner public test: buyer search effort per purchase should rise with a category's vendor count, against Bakos's prediction that it falls.

**Register.** Opens three entries.
- How to read a cost floor apart from the deal's own cost.
- Whether AI buying agents break the link between entry and the search cost floor (Shahidi et al. 2025). If they do, erosion runs through pooling instead.
- Whether a cost floor can sit above the participation threshold for a whole market, so no seller can enter it deal by deal. The corollary implies it. Nothing yet says how to recognize one.

### 3.5 Axiom III: what a party cannot verify or enforce

**Current** (line 134):

> Whatever a party sinks that is worth less outside this relationship exposes it to what it cannot verify later.

**Proposed:**

> Whatever a party sinks that is worth less outside this relationship exposes it to what it cannot verify or enforce later.

Line 142, "What turns exposure into cost is what the exposed party cannot verify," becomes: *What turns exposure into cost is what the exposed party cannot verify, and what it can see but cannot stop.* The plain-English gloss gains one clause: *and to anything the other side can do in plain sight that you cannot prevent.*

**Proposed corollary, among the governance corollaries:**

> **Hostages govern what verification cannot.** A party that can see the other side refuse to adapt, force a renegotiation or move its best people elsewhere, and cannot stop it, is exposed under full information, and no amount of proof protects it. What protects it is something the other side loses by defecting: a bond, a reciprocal specific investment, fees staged against delivery, the seller's referenceability. Hostages run in both directions, and each party is entitled to ask what the other loses if it stops trying. They are the remedy for drift after signature, when nobody hides anything and incentives simply move.

This sits next to the existing frequency corollary, whose mutual sanction is a hostage renewed at each boundary. [05-governance-forms.md](./theory/01-foundation/05-governance-forms.md) carries the full treatment.

**Evidence.** Wathne and Heide (2000), read in full. Opportunism splits into evasion, refusal to adapt, violation and forced renegotiation. Lock-in and information asymmetry are separate facilitating conditions. Monitoring is limited to information-based opportunism. Incentives, including hostages, govern lock-in. Heide and John (1990, 1992) and Heide (1994) supply the governance line in marketing.

**Falsifier (deal data).** At equal verification, deals where both parties hold something to lose drift less after signature than deals where only one side has sunk investment.

**Register.** Item 9 (joint exposure has no bond condition) gains urgency and a source. A new entry opens: who drifts first, and whether it depends on which side sank more. The theory makes no claim either way.

---

## 4. Where TCG stands against its neighbors

This table is the defense. It says where a neighbor is right, where TCG concedes, and the one prediction that separates them.

| Neighbor | Where it is right | Where TCG diverges, as a prediction |
|---|---|---|
| **Total cost of ownership** (Ellram) | Choosing among viable vendors. Small buyers, where one payer carries all three costs. | A supplier with a low total and one prohibitive cost ranks first under TCO. TCG predicts the deal does not happen. |
| **MEDDICC** | Execution and coalition mapping. Its paper process and economic buyer overlap with the bargaining cost. | A fully qualified deal with an implementation cost above the buyer's threshold this year. MEDDICC scores it qualified. TCG predicts no decision. |
| **Skok and Janz** | Contract value must cover acquisition cost. Price causes bargaining cost where approval tracks spend. | A low-value tool needing security review and finance sign-off. They predict low touch. TCG predicts it stalls unless a channel pays the bargaining cost, such as a marketplace contract or a pre-approved vendor list. |
| **Gartner buyer enablement** | The closest practitioner body. The purchase fails on the buyer's side, and purchase ease predicts better deals. | Sensemaking pays only where the bargaining cost binds. In a deal blocked on "will it work here," TCG predicts no gain. |
| **Value selling, Challenger** | Documented, quantified value against the next-best alternative. | A reframe with no new verifiable evidence. Challenger predicts higher close rate and price. TCG predicts no change in what the buyer realizes, and exposure where the claim outruns it. |
| **Moore** | Firms are built for complex systems or for volume, and are clumsy at the other. | A low-value product with a high policing cost. Moore files it under volume. TCG calls it implementation-led. TCG also predicts a guarantee can stand in for peer references. |
| **Cannon and Homburg** | The seller wins by lowering the buyer's costs beyond price. | Additive effects against a gate: TCG predicts an interaction. |
| **Marketing TCE** (Heide, John, Anderson, Wathne and Heide) | Axiom III nearly in full. | TCG moves the question from the firm's governance to the buyer's decision whether to use the market and the seller's choice of motion. |
| **Hockenmaier** | The same Dahlman triad applied to a go-to-market question, marketplaces. | His stages remove costs in a fixed order. TCG predicts the first investment goes to whichever cost is nearest its threshold. |

**What is original.** No source found makes the assembly. That means Dahlman's costs applied to the buyer's decision in a B2B sale, a self-serve and a participation threshold per cost, the non-compensatory rule, and the motion derived from the cost nearest its threshold. Also unattested elsewhere: PLG recast as a market condition that erodes through entry, and "price is a transfer" turned into sales doctrine. The rest is synthesis, and the research files will say so by name.

---

## 5. Research and provenance

**New research files**, each with frontmatter and an entry in the reading guide:

| File | Backs | Sources |
|---|---|---|
| `buyer-cost-neighbors.md` | Section 4, Axioms I and II | Cannon and Homburg 2001, Rangan, Menezes and Maier 1992, Moriarty and Moran 1990, Rackham and DeVincentis 1999, Ellram 1993 and 1995, Hockenmaier 2023, Gartner buyer enablement, Moore, MEDDICC, Skok and Janz |
| `information-environment.md` | The cost floor corollary | Anderson and de Palma 2009, Van Zandt 2004, Tirole 1996, Bakos 1997, Biglaiser 1993, Lizzeri 1999, Spulber 1996 and 1999, Williamson 1991, Ouchi 1980, Holmström 1979, Baker 1992, Holmström and Milgrom 1991, Filippas, Horton and Golden 2022, Shahidi et al. 2025 |
| `value-and-persuasion.md` | Standing assumption 2 | Kamenica and Gentzkow 2011, DellaVigna and Gentzkow 2010, Mullainathan, Schwartzstein and Shleifer 2008, Payne, Bettman and Schkade 1999, the anchoring and expectation-disconfirmation record, Anderson, Narus and van Rossum 2006 |

Additions to existing files:
- Wathne and Heide (2000) go into [incomplete-contracts.md](./theory/02-research/incomplete-contracts.md).
- Buchanan and Tullock (1962) go into [buying-center-dynamics.md](./theory/02-research/buying-center-dynamics.md).
- Heide and John go into [transaction-cost-economics.md](./theory/02-research/transaction-cost-economics.md), whose "what the framework adds" section is rewritten against section 4.

**Citation status.** Every source carries the status its research memo recorded: primary, secondary or unconfirmed. Unconfirmed sources are checked at the primary before they enter a file, or they stay out. Kent and Allen (1994) and Simonson (2008) stayed out. Moriarty and Moran (1990) entered marked secondary. Schiebler, Lee and Brodbeck (2026) entered [value-and-persuasion.md](./theory/02-research/value-and-persuasion.md) marked unconfirmed, cited for no figure, and is listed in the audit as untraced.

**Provenance audit** (`citation-provenance-audit.md`), done in step 2:

| Item | What the audit now records |
|---|---|
| Gartner 2019: contradictory information makes buyers "153 percent more likely" to settle for a smaller purchase | New row, primary named. Discrepancy 7 records the later opposite-direction use. Not quoted until resolved. |
| Gartner 2019: sensemaking 80%, telling 50%, giving 30% high-quality, low-regret deals | New row, primary named. Sample and instrument unpublished. |
| Gartner 2022: self-service buyers 1.65 times more likely to report high regret | New row, primary named. |
| Gartner: six to ten decision makers | Row already existed, primary linked. Discrepancy 6 gains the 5 to 11 and Forrester spread. |
| Gartner 2025 and 2026: 61% then 67% prefer a rep-free experience | Row already existed, primary linked. No change. |
| JOLT: 40 to 60% of pipeline lost to No Decision | Row already existed, primary cited. No change. |
| Cannon and Homburg 2001 sample, Schiebler et al. 2026 | Added under "Not yet traced". |

---

## 6. Scope decisions

These change no Constitution text, and the sequence in section 7 depends on them.

- **Core** is the Constitution, [01-motions.md](./theory/01-foundation/01-motions.md) and [07-open-questions.md](./theory/01-foundation/07-open-questions.md). **Evidence** is `theory/02-research/` and the audit. The glossary and governance forms are **supporting**, and are candidates to fold into the core.
- **The math is scaffolding.** It is kept to keep the argument honest and to make falsifiers checkable, and it is not shown in public. The two conditions and the participation test are the formal core. The useful parts of `02-mathematical-models.md` and `04-seller-surplus-model.md` fold into a Constitution appendix.
- **On trial after 5.0:** `06-calibration.md`, `08-from-axioms-to-instruments.md` and `models/`. The test is whether a file helps defend the claim or only makes it look precise. Code that checks the Constitution's worked examples passes. Simulation with invented coefficients does not.
- **Practice is frozen now and rebuilt after 5.0.** Every `practice/` file goes to `status: under-review` with a pointer to this proposal, and nothing else in practice changes. After 5.0, the instrument set is derived fresh from the axioms, at the smallest size they require, and whatever is not derived is archived. The parked decision-role ledger draft is input to that rebuild at most.
- **Audience and home case.** Founders and revenue leaders, held to academic citation standards. Health tech supplies the examples, built from public patterns and never from HTD clients or material.
- **Testing.** Every falsifier is written for others to run. The user's experience supplies hypotheses, not evidence.

---

## 7. Sequence once approved

1. **Freeze practice.** Set every `practice/` file to `under-review` with the pointer. One commit.
2. **Research first.** Write the three new research files and the additions, and add the audit rows. Theory cites only what exists.
3. **Constitution.** Apply sections 3.1 to 3.5, add the 5.0 version-history entry, and bump the root README footer with it.
4. **Propagate in theory.** The edits by file:
   - Glossary: $V_{solution}$, the three value terms, $F_k$'s "never summed," and the cost floor.
   - `01-motions.md`: the non-compensatory rule and the cost floor as hook.
   - `02-mathematical-models.md` line 313.
   - `05-governance-forms.md`: hostages.
   - `07-open-questions.md`: items 1, 3, 9 and 20, and the new entries.
5. **Wording sweep.** "Never summed" appears in `README.md` line 11, `CLAUDE.md` line 46, the Constitution line 81, `02-mathematical-models.md` line 313 and the glossary line 73. Each becomes the non-compensatory statement. The practice instances wait for the rebuild. "Never summed" is a description, not a canonical term, so it gets no `RetiredTerms.yml` entry. A Vale rule could catch its return, and that is a separate choice.
6. **Equations.** Section 3.1's notation changes the buyer's condition. Edit the Constitution and glossary first, then `models/tcg_models.py`, then rerun `make_figures.py`, then fix any worked example that moved.
7. **Run the five checks,** then retire this file to git history.

---

## 8. Choices

Settled on 2026-11-02:

1. **Which value enters the buyer's condition.** $V_{solution}$ is realizable value. The buyer decides on recognized value, $\tilde{V}_{solution}$, and the shortfall risk enters $L_b$. Section 3.1 carries the notation.
2. **The name.** *Cost floor* everywhere. Axiom III's floor above zero on $\pi_p$ keeps its wording.
3. **Placement.** A corollary under Axiom II, a column in Axiom I's table and a row in Part II. The Axiom I statement does not change for it.

4. **The hook stays out of the Constitution.** The cost floor is the public hook, and the Constitution is axioms-first, so its text stays plain and publishing carries the framing.
