---
title: "The Constitution of Transaction Cost Growth (TCG)"
layer: theory
status: active
version: 5.1
---

# The Constitution of Transaction Cost Growth (TCG)

**Version:** 5.1
**Purpose:** To state the three claims from which everything else in this repository derives, each answering one decision a party to a deal must make, each in time order, and each falsifiable on its own.

Version history is at the end of this document.

> [!IMPORTANT]
> **This document states structure. It states no measured quantity.** Every claim below says what depends on what, and each is argued from a mechanism. The thresholds, rates and band edges that turn those claims into numbers live in [06-calibration.md](./06-calibration.md), none of them is fitted, and a reader can reject any number there without rejecting the claim it sits inside.

---

## Standing assumptions

Three premises sit above the axioms. They are inherited rather than argued, and each is named here so a reader who rejects one knows what falls with it.

1. **Bounded rationality and opportunism** (Williamson 1985). No party can foresee every state the relationship will reach, so every contract is incomplete. And a party will exploit a gap once the other side's position is exposed. The first is why uncertainty has a price. The second is why safeguards exist.
2. **Value is exogenous to the sale, and it decays.** For a given offer, what the change can be worth to this buyer is its *realizable value*, $V_{solution}$, set by the product and the buyer's situation: its workflow, its alternatives and what it will invest in adoption. The seller can change the offer, which is a product decision even when it is made inside a deal. Within the sale, the seller moves only the buyer's *recognized value*, $\tilde{V}_{solution}$, its current estimate of realizable value, usually held as a range, and what the buyer pays. Evidence that narrows that range by means the buyer can check lowers the search cost. A claim that moves the estimate without narrowing the range is persuasion, and the buyer carries the gap as exposure under Axiom III, realized when delivery makes it visible. What the buyer captures after go-live is its *realized value*, which adoption and delivery raise toward realizable. Helping the buyer win a budget or a mandate lowers the bargaining cost and leaves the buyer's situation where it was. Where value moves during a cycle it moves down, from the triggering event: $V_{effective}(t) = \tilde{V}_{solution} \cdot e^{-\delta t}$. This is a modeling assumption, stated in [02-mathematical-models.md](./02-mathematical-models.md) section 4, and the one term in $\delta$ a seller can touch is whether an external catalyst has been named. Naming one is recognition, because the catalyst already existed. The assumption fails if, at equal claimed size, value claims the buyer cannot check win as often as claims verified on the buyer's own data. [value-and-persuasion.md](../02-research/value-and-persuasion.md) carries the evidence and the objection that survives it.
3. **Every actor acts on their own payoff** (Jensen and Meckling 1976). The parties the axioms reason about are the decision roles on each side and every intermediary standing between the two firms, and a role's payoff is not its organization's. An actor whose payoff does not depend on the outcome behaves as though the outcome does not matter, whatever their intent. The bargaining cost rests on this premise, and so do the stakes Axiom III derives for the seller's own representatives and for channels. The assumption is descriptive, and the framework does not build governance as though it predicted bad faith. Ghoshal and Moran (1996) showed that designing around opportunism can produce the opportunism it assumes, and the instruments take the other route: they make the arrangement one each party can say yes to. [tce-empirical-record.md](../02-research/tce-empirical-record.md) carries the critique.

![Two exponential decay curves falling toward a floor at the value of the next best alternative. Organizational inertia alone reaches the floor in the second month. A named external catalyst holds value above it until the eleventh.](./assets/value-decay.svg)

---

## Definitions

Two words the axioms use with a meaning narrower than ordinary speech. They are definitions rather than claims. *Market* and *deal* keep their ordinary meanings: the buyers who call a problem by one name, and one buyer's purchase.

- **Workflow.** The procedure a product changes. A product is an encoded reference workflow, and how far a buyer's version sits from the reference is what makes an investment in the deal specific under Axiom III. A product that cannot name its workflow has no reference to read that distance against.
- **Decision role.** A position in the buyer's organization that holds a veto or an evaluation over the purchase, defined by its relation to the workflow rather than by its occupant: who runs it, who owns it, who pays for it, who polices it. A decision role is measured on something the change touches and survives the person in it. A departure is one of two events. An occupant change on a stable role reopens what the new occupant cannot verify and leaves the cost where it was. The dissolution of a role, when the mandate leaves with the person, changes the coalition and the cost with it.

---

## Part I: The Three Axioms

Each axiom answers one decision, and the three are numbered in the order a party meets them in time: whether to transact at all, what it costs today, and what it might cost later.

| Axiom | The decision | Statement |
|---|---|---|
| **I. Law of Transaction Cost Composition** | Should I use the market? | Using the market costs the buyer three things beyond price: search and information, bargaining and decision, and policing and enforcement. A buyer will not use the market while any one of them exceeds what it will bear, however low the other two, and among costs it will bear, their relative size is where the sale starts. |
| **II. Law of Transaction Investment** | What will it cost me today? | Each of those costs is paid down by an investment from the buyer, the seller or both, and each party goes ahead only when its own share is covered by its own return. |
| **III. Law of Future Cost** | What might it cost me later? | Whatever a party sinks that is worth less outside this relationship exposes it to what it cannot verify or enforce later. That exposure is a future cost, it rebuilds unless maintained, and its allocation must be settled before the investment is sunk. |

**Two sources divide the work.** Dahlman (1979) classified the costs of using a market by kind, and his three names are Axiom I's. Williamson (1985) divided them by time, into the ex ante costs of drafting, negotiating and safeguarding an agreement and the ex post costs of maladaptation, haggling and running the governance, and made asset specificity what creates the second. The split by kind is Axiom I. The split by time is the line between Axioms II and III.

**On the component names.** Dahlman's names are canonical in theory prose. The field calls the three costs *search*, *consensus* and *implementation*, and the notation keeps those subscripts, because the field names say what a seller experiences and Dahlman's say what the cost is. [03-glossary-and-notation.md](./03-glossary-and-notation.md) carries the mapping.

---

### Axiom I — The Law of Transaction Cost Composition

> **Using the market costs the buyer three things beyond price: search and information, bargaining and decision, and policing and enforcement. A buyer will not use the market while any one of them exceeds what it will bear, however low the other two, and among costs it will bear, their relative size is where the sale starts.**

*Plain English: buying costs more than money. Finding the right seller, getting your own organization to decide, and making sure the seller delivers are three separate bills. If any one of them is too high, the buyer stays out of the market altogether, and making the other two easier does not bring it back. If all three are bearable, the one closest to too high is the first thing a seller has to pay down.*

*Origin: Coase (1937) for the question, which is whether to use the price mechanism at all, given that using it costs something. Coase (1960) lists the activities. Dahlman (1979) groups them into three.*

**Mechanism.** The decision is the buyer's. The seller reads it to know where the sale starts. Each cost yields to a different seller investment, and B2B software enlarges each in a specific way. The enlargements are this framework's own rather than Dahlman's.

| Cost (field name) | What B2B adds | The buyer's question | What lowers it | What sets its cost floor |
|---|---|---|---|---|
| **Search and information** (search) | Reachability. A buyer can know the category and name five vendors and still be unable to reach the seller without a channel. | Which solutions exist, and does this one fit? | Category definition, education, a channel that reaches the buyer | The information environment: message volume against the buyer's attention, and the category's record |
| **Bargaining and decision** (consensus) | The buyer is a coalition, not an agent. The bargain has two parts: the internal one among the decision roles (Webster and Wind 1972), and contracting, the bargain with the seller over terms through procurement, legal and security review. | Can my organization agree to this? | Mapping each decision role's exposure, and an arrangement each role can say yes to | The buyer's institutions: procurement rules, spend thresholds, required reviews and how decisions get made |
| **Policing and enforcement** (implementation) | The buyer cannot police performance in its own environment until the product is adapted to it, so the question becomes whether it will work *here*. | Will the seller deliver what was promised, and will it work here? | Outside validation: referrals, references, guarantees, a channel with a stake | The measurement environment: whether outcomes can be attributed, what standards exist, how verifiable delivery is |

Negotiating a term is bargaining cost paid today. What the term governs after signature belongs to policing and enforcement, which is Williamson's line between ex ante and ex post, and Buchanan and Tullock (1962) supply the theory of why requiring more agreement costs more. The buyer's adaptation work, the integrations built and the workflows rewired, is not itself the policing cost. It is one of the investments Axiom II says pay it down, and a forward-deployed engineer is the same investment made by the seller.

Dahlman argued that the three reduce to one cost, the resources lost to imperfect information. The framework accepts the common root and keeps the three apart for a different reason: each yields to a different seller investment, so they are separate for the purpose of deciding what to invest in. The three are also coupled, and the coupling runs from exposure into the bargaining cost. A workflow the product must fit and does not raises the policing cost and creates a bargaining cost in the same stroke, because an imposition creates a decision role whose objectives worsen. A buyer also demands broader agreement the more harm a decision can do (Buchanan and Tullock 1962), so its own review rules add approvers as the specific investment grows. And the loop runs back: each role a coalition adds brings requirements, and a requirement the product does not meet is a new divergence. None of this needs a coefficient. The bargaining count is read after exposure, adding each role a divergent step imposes on and each approver the buyer's rules require at that exposure ([02-mathematical-models.md](./02-mathematical-models.md) section 3.5). What the coupling does need is a date. Before fit is verified on the buyer's own workflow, the policing position and the vetoes it will create are both lower bounds, so where the sale starts is a reading taken under Axiom III's gap, not a fact about the deal. A seller who misrepresents fit is exploiting that gap, and the start it hid surfaces after the investment is sunk.

**Mathematical content.** Each cost $F_k$, in fractions of annual contract value, sits against two thresholds of its own: a self-serve threshold $\tau^{self}_k$, below which the buyer can pay the cost down alone, and a participation threshold $\tau^{part}_k$, above which the buyer does not enter the market. Read each cost's position between its own two:

$$r_k = \frac{F_k - \tau^{self}_k}{\tau^{part}_k - \tau^{self}_k}, \qquad k \in \{search,\; consensus,\; implementation\}$$

A cost at $r_k \le 0$ is self-serve. A cost with $r_k$ above zero and at most one is bearable with seller investment. A cost at $r_k > 1$ keeps the buyer out, whatever the other two read. **The sale starts at the largest $r_k$.** Each cost is measured against its own thresholds, so the three are comparable without sharing a scale, and a cost at a small share of the total can still end the deal.

**The costs are non-compensatory.** They add, in the buyer's condition under Axiom II and wherever one payer carries more than one of them, but ease on one never buys back another above its threshold. The costs act separately because different people and budgets pay them. Where a single person or budget pays more than one cost, those costs draw on one capacity, and the participation test applies to their total as well as to each. A one-person buyer approaches a single summed test, and a large coalition approaches three separate ones. Total cost of ownership (Ellram 1993) adds the costs and lets a low one offset a high one. This axiom adds them and forbids the offset.

**Corollaries.**

- **The motion is where the sale starts.** Search-led, consensus-led and implementation-led name the cost a seller pays down first. *Starts* means the first seller investment, not the first stage, since every buyer moves through the same stages. Product-Led and Sales-Led name the seller rather than the cost. [01-motions.md](./01-motions.md) carries the map.
- **Turnkey is a market condition, and it does not last on its own.** Turnkey is the condition under which product-led growth works: every cost self-serve, $r_k \le 0$ for all three, and nothing specific sunk under Axiom III. The condition erodes because of what defines it. A motion that needs little seller investment is cheap to copy, so competitors enter. Entry raises the search cost directly, because every entrant is another alternative to rule out, and it raises the policing cost through pooling, because free trials and identical claims stop separating good sellers from bad. A Turnkey market leaves the condition unless something holds the search cost down as sellers arrive: a de facto standard, a network effect, a dominant brand, or a channel that does the filtering and has a stake in getting it right. Entry raising the search cost is the search cost floor rising, under Axiom II's cost floor corollary. Separation is therefore a condition a market crosses in both directions, not a resting point: entry with signals that automate pools the market, the premium for being told apart then pays for a costlier signal or a shared institution that restores it, and where no affordable signal can, the market saturates ([02-mathematical-models.md](./02-mathematical-models.md) section 5.8).
- **Copying a motion copies another market's costs.** A motion that worked in one market is adopted in another by imitation. Product-led growth where the costs are not all self-serve leaves the buyer holding a cost it cannot pay down alone. Forward-deployed engineering where the policing cost is not what keeps the buyer out pays down an adaptation nobody was worried about. Read the other way, the investment a motion demands is also its defense against entry.
- **A sales organization is a division of labor over the jobs the costs create.** The buyer's stages are the same in every market: awareness, consideration, purchase, and renewal after it. What varies is which costs the buyer cannot get through alone, and each is a job the seller staffs at the stage where it arises. All three matter, and search is the one that keeps the stages from starting. The standard organization gives each stage one owner and one job, business development for search, account executives for bargaining, solutions engineers for policing, so a deal that starts at the policing cost gets its engineer at the demo as support, when the policing job was the one deciding the deal. Each handoff between owners is a seam where a cost gets paid twice, because what one owner learned does not travel, and in a long deal discovery drifts whoever holds it, so the full discovery belongs just before the investment is sunk. [01-motions.md](./01-motions.md) section 9.
- **Addressable market is a property of the motion.** A seller that can pay down only one cost reaches only the buyers whose sale starts there. The rest were never reachable. [05-governance-forms.md](./05-governance-forms.md) section 4.

**What would falsify it.** Four findings. Deals where the seller's first investment went to the cost with the largest $r_k$, read at a stated moment with what had been verified by then, convert no faster than matched deals where it went elsewhere. Buyers facing one cost above any plausible participation threshold enter the market at the same rate as buyers who do not. Large-buyer deals blocked on one cost are rescued by lowering the other two. And for the Turnkey corollary, which is new theory rather than repair: in categories where self-serve selling dominated, a rising vendor count does not come before falling trial-to-paid conversion and the arrival of sales-assist teams.

**Failure modes.** Kept out, mis-sequenced, imitation, Turnkey erosion unread, Akerlof saturation and Jevons collapse. The collected table is in Part III.

---

### Axiom II — The Law of Transaction Investment

> **Each of those costs is paid down by an investment from the buyer, the seller or both, and each party goes ahead only when its own share is covered by its own return.**

*Plain English: someone has to pay to get the deal done, and it does not have to be the buyer. Each side asks whether its own part is worth it, and the deal happens only when both say yes.*

*Origin: Williamson (1985), the ex ante costs of a transaction. The seller's side follows [04-seller-surplus-model.md](./04-seller-surplus-model.md).*

**Mechanism.** The deal has two conditions, one per party, and either party can make the investment that retires a cost. When the seller invests against a cost, the buyer's share of it falls, and it falls by more than the seller spent when the seller does the work more cheaply. The seller's cost of acquiring customers lives here, as the seller's share.

**Mathematical content.** Both conditions are in fractions of annual contract value:

$$S_b = V_{switch}(t) - P - \sum_k I^b_k - L_b \qquad S_s = P - C_{deliver} - \sum_k I^s_k - L_s$$

$V_{switch}(t) = \tilde{V}_{solution} \cdot e^{-\delta t} - V_{next\_best}$ is the buyer's opportunity cost of staying where they are, decaying by the second standing assumption, and $V_{next\_best}$ includes building it internally. It is read on recognized value, because that is what the buyer decides on. $P$ is price over the relationship. $I^b_k$ and $I^s_k$ are what the buyer and the seller invest today against cost $k$. $L_b$ and $L_s$ are each party's expected future loss, from Axiom III. Recurrence enters through $P$ and $C_{deliver}$ summed over expected renewals.

The deal happens when both conditions are positive and Axiom I's gate holds. Added together:

$$S_b + S_s = V_{switch}(t) - C_{deliver} - \sum_k \left(I^b_k + I^s_k\right) - L_b - L_s$$

Price cancels, because price is a transfer. Read on what the deal can produce, the joint condition uses realizable value, and the difference from recognized value is a loss the buyer carries under Axiom III whether or not it priced it at signature. Persuasion moves the buyer's reading and not the joint one.

**Corollaries.**

- **Price is not a transaction cost.** It belongs in both conditions and in neither party's cost of transacting.
- **Moving investment between parties changes the split, not the total,** unless the party taking it on does the work more cheaply or doing it lowers a future loss under Axiom III. A forward-deployed engineer is the case where both hold: the seller's engineers adapt their own product at lower cost, and their presence in use catches misfit while it is cheap. It also creates a future cost for the seller, because the engineering is specific to this buyer.
- **Cost to serve is directional.** The seller's investment falls on whichever cost it pays down, so two markets with the same cost of sale can demand it in different components. A motion is a decision about which cost an organization is built to pay down.
- **Pursuit is the seller's condition asked of a population.** Whether a market is worth entering is whether the buyers' contract value and frequency can recover the investment their costs demand from this seller. A seller that cannot recover it declines the market rather than investing less, for the same reason it declines a deal it cannot amortize. [04-seller-surplus-model.md](./04-seller-surplus-model.md).
- **Every cost has a cost floor.** Part of each cost is set outside the deal, by the information environment for search, the buyer's institutions for bargaining and the measurement environment for policing. Axiom I's table names each. No seller can lower a cost floor within one deal at a return that deal repays, because the return is shared by every deal sitting on it. A cost floor falls only through investment made across deals, such as a marketplace, a certification, an intermediary with a stake or a standard, or is cleared by a signal costly enough to separate the seller from the pool. Otherwise the seller chooses its cost floors when it chooses its market and channel. Cost floors move. The search cost floor rises as the volume of messages outgrows the attention buyers can give them, and cheap seller effort raises it further (Anderson and de Palma 2009, Van Zandt 2004). Information lowers the search cost only where the buyer can check it, and raises it where the buyer cannot. The policing cost floor rises when fit is misrepresented. A buyer that cannot tell good sellers from bad judges each by its estimate of the category (Akerlof 1970), and a misfit it discovers after sinking the investment lowers that estimate for every seller it meets next. One seller's persuasion is spent from a reputation the category shares, and enough of it ends in Akerlof saturation. Williamson (1991) places such parameters in the institutional environment, which the parties to one transaction do not choose. [information-environment.md](../02-research/information-environment.md).

**What would falsify it.** Deals where the seller absorbed part of the buyer's investment close at no higher rate than matched deals where it did not, at equal total cost. For the cost floor corollary: holding deal-level effort fixed, sellers who invest in shared institutions fail in a market as often as equally strong sellers who invest only deal by deal, or buyer search effort per purchase falls as a category's vendor count grows, or buyers who discovered a misrepresented fit in a category require no more verification and no more approvers on their next purchase in it, from a different seller, than matched buyers who did not.

**Failure modes.** Under-invested, over-invested and unamortizable. The collected table is in Part III.

---

### Axiom III — The Law of Future Cost

> **Whatever a party sinks that is worth less outside this relationship exposes it to what it cannot verify or enforce later. That exposure is a future cost, it rebuilds unless maintained, and its allocation must be settled before the investment is sunk.**

*Plain English: once you have spent money that only pays off with this partner, you are exposed to everything you could not check in advance, and to anything the other side can do in plain sight that you cannot prevent. That risk is part of the cost of the deal, it grows back if nobody tends it, and who carries it has to be agreed before anyone spends.*

*Origin: Williamson (1979, 1985), the ex post costs of a transaction and the specificity that creates them. Klein, Crawford and Alchian (1978) for whose exposure it is. Akerlof (1970) and Spence (1973) for why only costly evidence reduces it. Wathne and Heide (2000) for hold-up under full information.*

**Mechanism.** An investment is specific when it loses value outside this relationship. For the buyer, specificity is read as distance from the reference workflow: the further the buyer's version sits from what the product assumes, the more adaptation the deal requires and the less of it survives a failed deal. Once a specific investment is sunk, the party who made it can be held up, because the other side can extract the difference between what it is worth here and what it is worth anywhere else. Klein, Crawford and Alchian named that difference the appropriable quasi-rent and established that the exposure follows the investment rather than the invoice: whoever sinks the specific capital is the exposed party, buyer or seller.

What turns exposure into cost is what the exposed party cannot verify, and what it can see but cannot stop. Each of the three costs runs between its own pair of parties, and each pair's gap is different.

| Cost | Whose uncertainty, about what | What resolves it |
|---|---|---|
| Search and information | The buyer's, about the market. Which alternatives exist and whether this one fits. | Artifacts that travel without the seller: category definition, reference architectures, verifiable proof, a channel with a stake |
| Bargaining and decision | Each decision role's, about its own outcome. What the change does to its budget, headcount and standing. | Mapping who loses what, one role at a time, and answering it in the arrangement. Objections are collected apart before any room convenes, because a room suppresses what only one member knows |
| Policing and enforcement | Bilateral. The seller's, about the buyer's environment. The buyer's, about the seller's capability in it. | Discovery that maps the environment, and demonstrations the seller pays to produce |

The search gap mostly prices today's cost and decides participation under Axiom I. The other two decide the future loss. The buyer's loss runs on the policing gap, whether the seller delivers and the product fits, and on the bargaining gap, whether the coalition holds once the investment is sunk. The seller's loss runs on what it could not map of the buyer's environment and coalition. The bargaining gap is not a conflict of interest that proof could close. Two decision roles with perfect knowledge of each other and opposed interests still disagree. What proof can close is each role's uncertainty about its own exposure.

What can be settled before the investment is sunk is the allocation, and not the adaptation itself. Under uncertainty, parties write deliberately incomplete contracts and adapt afterward (Crocker and Reynolds 1993, Bajari and Tadelis 2001), and the misfits that decide whether a system is used, in roles, controls and culture, surface only in use (Strong and Volkoff 2010). So the share of the arrangement settled in advance, who bears which adaptation risk, staged how, with what right to stop, rises with the imbalance between what the two parties have sunk, net of what each stands to lose at the next boundary. Specificity raises it when one side sinks alone, and two parties sinking evenly need less settled than one sinking alone. The share of the work done in advance can fall as uncertainty rises. [02-mathematical-models.md](./02-mathematical-models.md) sections 5.5 and 5.6 give both forms. Discovery cannot reach what only use reveals, and forcing it produces the over-frictioned failure. [incomplete-contracts.md](../02-research/incomplete-contracts.md) carries the evidence.

What the allocation assigns is residual control (Grossman and Hart 1986, Hart and Moore 1990). Contracts on specific transactions are incomplete as a structural matter, so states arise that nobody specified. What governs those states is the pre-agreed allocation of the right to decide, and a party who expects to be held up in them declines to sink the investment at all. That is why more legal review does not move a stalled specific deal.

**Mathematical content.** Each party's expected future loss is its exposure times the chance the exposure does not come back:

$$L_p = Q_p \cdot \pi_p, \qquad Q_p = C^{p}_{invest} - R^{p}_{redeploy}, \qquad p \in \{b, s\}$$

$L_p$ is a shortfall in the return party $p$ expected from the relationship, through hold-up or through a fit that fails in use, and not a second charge for the investment Axiom II already counted. The quasi-rent $Q_p$ bounds it, because it is the most the other side can extract or a failure can destroy. $\pi_p$ rises with the gaps party $p$ cannot close and has a floor above zero, because some risk survives any amount of proof. It also rises with what the other side can take in plain view at a renegotiation, which is nothing while the imbalance between the two quasi-rents stays within what forcing the renegotiation would cost the side that sank less ([02-mathematical-models.md](./02-mathematical-models.md) section 5.5). Its shape between floor and ceiling is not claimed. Absent maintenance, each gap $\hat{\Delta}_k \in [0, 1]$ rebuilds toward its ceiling:

$$\hat{\Delta}_k(t) = 1 - \left(1 - \hat{\Delta}_k(0)\right) e^{-\gamma_k t}$$

Discovery is a separate, discrete step down that someone pays for. A departed champion is the bargaining gap reopening all at once, and a deal can leave the viable zone with no change in product, price or technical work.

![Two rising curves from a near-zero implementation gap at go-live, against a horizontal line marking where a challenger begins. The unmaintained curve bends toward the challenger line and nearly reaches it within three years. The maintained curve levels off well below it, where maintenance matches the rebuild.](./assets/axiom-3-asymmetry-drift.svg)

A buyer who commits in stages sinks $Q_m$ at gate $m$ against residual uncertainty $x_m$, so the expected loss is $\sum_m Q_m \, \pi(x_m)$ rather than $Q \, \pi(x_0)$. Staging puts the small commitments where the uncertainty is high.

**Corollaries.**

- **The gate.** Where nothing specific is sunk and a trial verifies fit, the future cost is near zero and market terms hold: the buyer verifies by trying and walks away at no cost. Specificity is the master variable for governance, and apparatus applied below it is the over-frictioned failure.
- **Governance form.** With frequency, specificity selects the arrangement that holds the deal. With nothing specific sunk, market terms at any frequency. With specific investment, a one-shot transaction takes a third-party safeguard because neither side will build relational machinery for a single event, a recurring one takes bilateral governance where each repetition safeguards the next, and a continuous relationship of rising specificity eventually takes integration, which for the seller means the buyer builds it. The Mutual Implementation Plan is the bilateral form's instrument. [05-governance-forms.md](./05-governance-forms.md).
- **Frequency is partly the seller's choice, and what it buys is mutual sanction.** A recurrent transaction lets each party sanction the other at the next boundary, and the sanction is credible only when both hold exposure there: the buyer's non-renewal against the seller's delivery commitments, price caps and penalties. Credible commitments are mutual or they are not commitments. A one-sided cheap exit for the buyer does not govern a specific deal. It hands the seller's sunk investment to the buyer to hold up (MacLeod and Malcomson 1989). Restructuring a one-shot sale as a recurring one brings the cooperation condition $\delta_{discount} > (T - R)/(T - P)$ within reach (Axelrod 1984) when both sides carry a stake at each boundary. [05-governance-forms.md](./05-governance-forms.md) section 5.
- **Enforcement governs what verification cannot.** A party that can see the other side refuse to adapt, force a renegotiation or move its best people elsewhere, and cannot stop it, is exposed under full information, and no amount of proof protects it (Wathne and Heide 2000). Two remedies do, and both are settled before the investment is sunk. A hostage is something the other side loses by defecting: a bond, a reciprocal specific investment, fees staged against delivery, the seller's referenceability. An allocated right fixes in advance where a renegotiation starts and who controls it: an option to buy or renew at a preset price, a right to stop at a price agreed up front, or which party makes the last offer (Aghion, Dewatripont and Rey 1994, Nöldeke and Schmidt 1995). Both run in both directions, and each party is entitled to ask what the other loses if it stops trying. They are the remedy for drift after signature, when nobody hides anything and incentives simply move. Mutual sanction at each boundary, above, is a hostage renewed. This is why the framework prefers long-term alignment to a one-off concession. A discount changes the price once and leaves every later incentive where it was. A hostage or an allocated right changes what defection costs at every boundary that follows. [incomplete-contracts.md](../02-research/incomplete-contracts.md).
- **Commitment must be staged.** When an investment is irreversible and the environment uncertain, the right to wait has value, and a contract demanding full commitment at once asks the buyer to destroy it (Dixit and Pindyck 1994). Gating converts one irreversible decision into a sequence, each taken with more information, and a right to stop caps what each gate can lose. The [Milestone Valuation Model](../../practice/milestone-valuation-model.md) is the instrument.
- **Whose exposure.** Both parties'. In a forward-deployed motion the seller sinks the specific investment first, so the seller holds the exposure and needs the safeguard, and the allocation has to be settled before the seller spends, which can be well before signature. [04-seller-surplus-model.md](./04-seller-surplus-model.md).
- **Every party holding exposed rent, or adjudicating it, needs a stake.** The seller is a coalition too, and its representative holds the decision role that reads the deal. The seller sinks on that reading, so it is exposed to what the representative knows and the seller cannot verify, and, once the representative is paid at signature, to attention it can see move elsewhere and cannot stop. Vesting compensation on outcomes that survive signature is the enforcement corollary applied to that role: a clawback is a hostage, a safe harbor is a right allocated in advance, and an expansion share is a stake at the next boundary. The stake required rises with what the seller sinks on the representative's reading and is zero below the gate. A channel adjudicating the buyer's gap is cheap talk by the fourth Friction Allocation Principle, below, unless it loses when a bad signal passes. [05-governance-forms.md](./05-governance-forms.md) section 5.
- **The Friction Allocation Principles.** A mechanism reduces a gap only if its cost cannot be automated away, is borne by the claimant rather than the receiver, scales with the size of the claim, and is adjudicated by someone who loses when a bad signal passes. Violate any one and the mechanism is cheap talk. Spence's single crossing property backs the first three for signals the seller sends. The fourth comes from the theory of certification intermediaries rather than from Spence. The [Friction Allocation Diagnostic](../../practice/friction-allocation-diagnostic.md) tests them.
- **Three levers, and why verification wins.** The seller can discount, which moves price and is a pure transfer. It can take risk back through guarantees and clawbacks, which does up to three things at once. It moves future loss from buyer to seller, which is a transfer. It changes what the seller does, because a seller on the hook works harder to deliver. And it tells the buyer which seller it faces, because only a seller confident of delivering can afford to offer it, which is Spence's separation. The last two lower $\pi$, so a guarantee is part transfer and part verification. Or the seller can verify directly, which lowers $\pi$ and shrinks a cost both sides were carrying. Only what lowers $\pi$ raises the joint surplus, so a resolved gap can close a deal no discount could. What stays empirical is whether a given verification costs less than the loss it removes.
- **Reputation depreciates.** What was verified at $t_0$ is not verified at $t_1$. Credibility must be re-earned with evidence of continued delivery at every level: the seller's, the channel's, the adjudicator's. This is the rebuild clause applied after signature, and the [Sustaining Adoption Review](../../practice/implementation-motion/04-sustaining-adoption-review.md) is where the re-earning happens.
- **Two things drift, and account management is the seller's maintenance.** What was verified goes stale, and the fit itself drifts as either party changes its workflow or its product. Re-verification holds the first down and cannot reach the second, which only re-adaptation, notice of change or a change process allocated before either side moves can govern. Account management is a seller investment justified by the seller's own condition: the seller funds it while the margin it holds at the next boundary covers the cost of keeping pace with the rebuild, funds none below that, and funds none at all where it has no stake at the boundary. [02-mathematical-models.md](./02-mathematical-models.md) sections 5.3 and 5.7.
- **The Decay Clock.** Value decays from the trigger by the second standing assumption while the gaps rebuild by this axiom. Both push the conditions toward zero on a cycle, and a deal viable at $t_0$ is not necessarily viable at $t_1$ without intervention. [02-mathematical-models.md](./02-mathematical-models.md) section 4.

**What would falsify it.** Specific deals with pre-agreed staging and stop rights retain no better than specific deals without them. Or deals where verification closed a gap fail after signature at the same rate as matched deals where it did not. Or, at equal verification, deals where both parties hold something to lose, or where the right to renew or stop was allocated in advance, drift after signature as often as deals where only one side has sunk investment and nothing was allocated.

**Failure modes.** Unallocated, over-frictioned, mis-governed, unhostaged, defection, cheap talk, misallocated friction, the wrong gap closed, reputation hoarding, and option value dominating. The collected table is in Part III.

---

## Part II: Derivations

Everything the repository claims beyond the three axioms is derived from them, and this table says where. A concept missing from it is either a standing assumption, a research file elaborating a source, or a mistake.

| Derivation | From | Stated in |
|---|---|---|
| The motion is where the sale starts | I | [01-motions.md](./01-motions.md) |
| Turnkey as a market condition, and its erosion through entry | I, with II | Part I above |
| Division of sales labor over the three costs | I | Part I above |
| Addressable market is a property of the motion | I | [05-governance-forms.md](./05-governance-forms.md) §4 |
| Two conditions, one per party, and price as a transfer | II | Part I above, [04-seller-surplus-model.md](./04-seller-surplus-model.md) |
| Cost to serve is directional | II | Part I above |
| Pursuit as the seller's condition across a population | II, with I | Part I above, [04-seller-surplus-model.md](./04-seller-surplus-model.md) |
| Separation as a condition a market crosses in both directions | I, with III | [02-mathematical-models.md](./02-mathematical-models.md) §5.8 |
| Account management as the seller's maintenance, and fit drift apart from stale verification | III, with II | [02-mathematical-models.md](./02-mathematical-models.md) §5.3, §5.7 |
| Every cost has a cost floor | II, applied to I | Part I above, [information-environment.md](../02-research/information-environment.md) |
| The gate | III | Part I above |
| Governance form from specificity and frequency | III | [05-governance-forms.md](./05-governance-forms.md) §2 |
| A safeguard inside the buyer where the sale starts at bargaining | III, with I | [05-governance-forms.md](./05-governance-forms.md) §2 |
| Frequency as a commercial choice, buying mutual sanction | III | [05-governance-forms.md](./05-governance-forms.md) §5 |
| Staged commitment | III | [Milestone Valuation Model](../../practice/milestone-valuation-model.md), [real-options.md](../02-research/real-options.md) |
| Enforcement governs what verification cannot | III | Part I above, [05-governance-forms.md](./05-governance-forms.md) |
| Stakes for agents and adjudicators | III, with the decision roles as parties | [05-governance-forms.md](./05-governance-forms.md) §5 |
| Who bears the specificity | III | [04-seller-surplus-model.md](./04-seller-surplus-model.md) |
| Friction Allocation Principles | III | [Friction Allocation Diagnostic](../../practice/friction-allocation-diagnostic.md) |
| Three levers | III, with II | Part I above |
| Reputation depreciation | III | [Sustaining Adoption Review](../../practice/implementation-motion/04-sustaining-adoption-review.md) §4 |
| Decay Clock | III, with the second standing assumption | [02-mathematical-models.md](./02-mathematical-models.md) §4 |
| The two conditions | All three | Part III below |

---

## Part III: The Two Conditions

The three axioms are what the terms of two conditions mean.

$$S_b = V_{switch}(t) - P - \sum_k I^b_k - L_b > 0 \qquad S_s = P - C_{deliver} - \sum_k I^s_k - L_s > 0 \qquad r_k \le 1 \;\; \forall k$$

- The participation clause, $r_k \le 1$ for every cost, is **Axiom I**, and the cost with the largest $r_k$ is where the sale starts.
- The investments $I^b_k$ and $I^s_k$, and the fact that there are two conditions rather than one, are **Axiom II**.
- The future losses $L_b$ and $L_s$, and the rebuild that moves them over time, are **Axiom III**.
- $V_{switch}(t)$ decays by the second standing assumption.

A deal closes when both conditions hold at the moment of decision and no cost keeps the buyer out. It persists when the governance form selected under Axiom III holds every party's weight on the future above the cooperation threshold, and when the gaps are maintained faster than they rebuild.

**Reading a stall.** Walk the terms in axiom order.

1. **Is any cost keeping the buyer out?** Pull it back into range or decline. No amount of work on the other two reaches it. If its cost floor is what holds it there, the remedy is an investment shared across deals or another market. (Axioms I and II.)
2. **Is the seller working on the cost nearest its threshold?** A cost that started there may not be there now. (Axiom I.)
3. **Does each party's share of today's investment fit inside its own return?** If not, move investment to the party that does the work more cheaply or whose doing it lowers a future loss, or decline. (Axiom II.)
4. **Is anything specific being sunk, and was its allocation settled first?** A specific one-shot deal is the case to restructure as recurring or decline, not to run lighter. (Axiom III.)
5. **Which party cannot verify what, and is it rebuilding faster than discovery closes it?** A departed champion lands in the bargaining gap and no amount of technical proof reaches it. (Axiom III.)
6. **Does the buyer accept the case and still defer?** They are pricing the right to wait. Stage the commitment rather than re-arguing the return. (Axiom III.)
7. **Is value decaying faster than the costs fall?** Name a catalyst or close faster. (Second standing assumption.)
8. **Has any party's stake fallen below the threshold, or has any party stopped re-earning credibility?** The relationship decays regardless of the deal's economics. (Axiom III corollaries.)

**Failure modes, collected.**

| Axiom | Failure | Signal |
|---|---|---|
| I | Kept out | A cost above the participation threshold worked as though it were a sales problem |
| I | Mis-sequenced | The seller's first investment went to a cost that was not nearest its threshold |
| I | Imitation | A motion copied from another market, organization built to pay down a cost its buyers do not carry |
| I | Turnkey erosion unread | A self-serve motion kept running while entry raises the search cost |
| I | Akerlof saturation | Telling good sellers from bad costs more than any affordable signal can cover, and the buyer exits |
| I | Jevons collapse | Channel friction was production cost and fell to zero, the search cost floor rises, and the channel stops separating sellers |
| II | Under-invested | The buyer is left holding a cost it cannot pay down alone |
| II | Over-invested | The seller pays down a cost that was not near its threshold |
| II | Unamortizable | The seller's share exceeds what the relationship can return |
| III | Unallocated | Specific investment sunk with no staging or stop rights agreed, buyer signs, fails to deploy, churns |
| III | Over-frictioned | Governance apparatus on a deal where nothing specific is sunk, buyer chooses a lighter competitor |
| III | Mis-governed | Frequency ignored or sanction one-sided, wrong arrangement for the repetition pattern |
| III | Unhostaged | Hold-up under full information met with more verification or a discount, when only a change in what defection costs would stop it |
| III | Defection | A party's weight on the future below threshold, hold-up on either side |
| III | Cheap talk | Signal fails single crossing, no gap moves |
| III | Misallocated friction | Receiver bears the filtering cost |
| III | Wrong gap closed | Effort on a gap that was already low |
| III | Reputation hoarding | Past signals unrefreshed, incumbent coasts |
| III | Option value dominates | Case accepted, commitment deferred, full commitment demanded before uncertainty resolves |

Each mode names one axiom and one place to intervene. A stall matching none of them means the table is incomplete, which is itself worth recording.

---

## Version History

**Current version: 5.1.** The framework's version tracks this document's, and the root README footer must agree, which `check_frontmatter.py` enforces.

<!-- vale TCG.RetiredTerms = NO -->
| Version | Date | Change |
|---|---|---|
| 5.1 | 2026-11 | Axiom III's mechanism states what the share of the arrangement settled in advance rises with: the imbalance between what the two parties have sunk, net of what each stands to lose at the next boundary, and not specificity as such. Two parties sinking evenly need less settled than one sinking alone. The math file gains the bond condition for joint exposure and forms for the allocation required and the work done in advance, and the governance-forms file reads the frequency readings and the build boundary off the bond condition, and adds a safeguard inside the buyer where the sale starts at bargaining. Axiom I's coupling is stated: the bargaining count is read after exposure, and the sale-start reading is dated, a lower bound until fit is verified. The cost floor corollary gains the policing floor a misrepresented fit lowers for the whole category. Drift splits into stale verification and fit drifting apart, account management is the seller's maintenance with a funding threshold, and separation in a market becomes a condition crossed in both directions. The division-of-labor corollary is restated over jobs rather than stages: the buyer's stages are fixed, and each cost it cannot get through alone is a job staffed where it arises. The stakes for the seller's representatives and for channels are derived from Axiom III with the decision roles as parties, and the third standing assumption narrows to saying who the parties are. The axiom statements are unchanged. |
| 5.0 | 2026-11 | The second standing assumption splits value three ways. Realizable value is set by the offer and the buyer's situation and is exogenous to the sale, recognized value is the buyer's estimate, which the seller moves, and realized value is what the buyer captures after go-live. The buyer's condition is read on recognized value, and the gap is exposure under Axiom III. Axiom I's costs become non-compensatory: they add, in the buyer's condition and against one capacity where one payer carries more than one, but ease on one never buys back another above its threshold, which replaces "never summed". Contracting is named as the buyer's bargain with the seller over terms, inside bargaining and decision. Axiom II gains the cost floor corollary, the part of each cost set outside the deal, and Axiom I's table names each cost floor. Axiom III widens from what a party cannot verify to what it cannot verify or enforce, and gains the enforcement corollary, which names hostages and rights allocated in advance as the remedies for hold-up under full information, with the unhostaged failure mode. Open question 20 closes, and items 32 to 36 open in 07-open-questions.md. Follows the 5.0 proposal and three new research files. |
| 4.1 | 2026-10 | The three-levers corollary names a guarantee's selection effect. Taking risk back is part transfer and part verification: the transfer moves future loss without shrinking it, and what the offer reveals about which seller can afford it lowers $\pi$, alongside the incentive effect 4.0 already named. Resolves the conflict with the risk-transfer extension in costly-signals.md, which now states the two limits on that separation. No axiom changed. |
| 4.0 | 2026-10 | The axioms are restated as three decisions in time order: whether to use the market, what it costs today, what it might cost later. Axiom I takes Dahlman's names for the three costs, gains a participation threshold per cost, and replaces "the one that binds selects the motion" with where the sale starts. Policing and enforcement returns to Dahlman's meaning, and the buyer's adaptation work becomes an investment. Axiom II, formerly the Law of Asset Specificity, becomes the Law of Transaction Investment: two conditions, one per party, in which price cancels as a transfer. Axiom III, formerly the Law of Uncertainty Inflation, becomes the Law of Future Cost and takes specificity, the gate and the governance corollaries, with allocation anchored to before the investment is sunk rather than to signature. Turnkey becomes a market condition that erodes through entry, and Structural is retired. The summed level, direction shares, the per-component multiplier and the reduced form $y = a\hat{\Delta}_A^2 + c$ retire from the Constitution. Seat becomes decision role, and market and deal stop being Definitions. Follows three adversarial reviews, recorded in the revision proposal in git history. |
| 3.0 | 2026-09 | Axiom II's second clause changes one word, after three adversarial reviews. The cost of a specific deal must be *allocated* before signature, no longer *paid*: what rises with specificity is the share of the arrangement settled before signing, who bears which adaptation risk and staged how, while the work done before signing can fall as uncertainty rises (Crocker and Reynolds, Bajari and Tadelis, Strong and Volkoff). The exit-cost corollary of 2.4 is withdrawn, because one-sided cheap exit hands the seller's sunk investment to the buyer, and the frequency corollary returns with mutual sanction as its mechanism. Axiom III's bargaining row collects objections apart before any room convenes. First axiom wording change since 2.0. |
| 2.4 | 2026-09 | Corrections after an external review. Axiom II's frequency corollary becomes the exit-cost corollary: what governs a specific deal bilaterally is the buyer's cost of exit at the next boundary, subscription was its vehicle and not the reason subscription won, and frequency is the field's reading of it. The seat definition gains two departure events, vacancy and dissolution. The third standing assumption is marked descriptive against Ghoshal and Moran. tce-empirical-record.md added to the research. No axiom changed. |
| 2.3 | 2026-09 | Definitions added for market, workflow, seat and deal, the units at which the three axioms are read. Three corollaries added: cost to serve is directional (I), a product must name its workflow (II), pursuit is amortizability at market level (II). An organization-level mis-composed failure mode. Two register entries opened: the market reading has no instrument, and the components have no equilibrium statement. 08-from-axioms-to-instruments.md opened as the derivation of what a reader must be able to do, and integration-touchpoints.md added to the research. No axiom changed. |
| 2.2 | 2026-09 | Restructure, step 6. Reference trim. The research files stop carrying quotes and statistics, which move to publishing and the provenance audit. The glossary term index loses every single-file term. The math file's argument about units is compressed. The retired derivation tiers are removed from every support line. No axiom changed. |
| 2.1 | 2026-09 | Restructure, step 5. Coase's component names swept through theory prose, fit verification moved out of the search component and under specificity, the motions and governance files trimmed of material the Constitution now carries, and 07-open-questions.md opened as the register of under-developed areas. No axiom changed. |
| 2.0 | 2026-09 | The axioms are rewritten. Governance stops being an axiom and becomes a corollary of specificity, where Williamson put it. Specificity becomes Axiom II with its own law. Uncertainty Inflation moves from II to III and gains its second clause. Each axiom is stated at the level where a seller meets it, in one sentence, with a falsifier. Three standing assumptions are named above the axioms. The components take Coase's names in theory, with consensus and implementation kept as the field translations. Part II becomes a table. No equation changed. |
| 1.2 | 2026-09 | Restructure, step 3. Three motion files merged into 01-motions.md, the foundation files renumbered, this history reduced to a pointer, the reading guide and glossary trimmed. |
| 1.1 | 2026-09 | Restructure, step 2. Practice flattened to one directory and ten operating-procedure files removed. The vesting claim moved to 05-governance-forms.md section 5. |
| 1.0 | 2026-09 | First release under the name Transaction Cost Growth. The framework was renamed from Implementation-Led Growth, every motion was named after the cost it reduces, and the count restarted. |
<!-- vale TCG.RetiredTerms = YES -->

The nineteen revisions made under the earlier name, and the prose entry for each, are in the git history: `git log -- theory/01-foundation/00-tcg-constitution.md`, then `git show <commit>:theory/01-foundation/00-tcg-constitution.md`. `RetiredTerms.yml` cites those version numbers when it records what each one retired.

---

## Related

**Sibling theory:**
- [01-motions.md](./01-motions.md) — The motions as where the sale starts, and the map onto the incumbent vocabulary.
- [02-mathematical-models.md](./02-mathematical-models.md) — Functional forms behind the variables named here.
- [03-glossary-and-notation.md](./03-glossary-and-notation.md) — Canonical index of every symbol and term, including the Dahlman-to-field name mapping.
- [04-seller-surplus-model.md](./04-seller-surplus-model.md) — The seller's condition under Axiom II, and the seller's exposure under Axiom III.
- [05-governance-forms.md](./05-governance-forms.md) — Axiom III's governance corollaries in full.
- [06-calibration.md](./06-calibration.md) — Every number, with its provenance.
- [07-open-questions.md](./07-open-questions.md) — Where the theory is under-developed, by axiom, and what would settle each gap.
- [08-from-axioms-to-instruments.md](./08-from-axioms-to-instruments.md) — What a reader must be able to do, derived from the axioms.

**Academic backing** (per axiom):
- Axiom I (Composition) → [transaction-cost-economics.md](../02-research/transaction-cost-economics.md), [buying-center-dynamics.md](../02-research/buying-center-dynamics.md), [channel-collapse.md](../02-research/channel-collapse.md), [fear-of-failure.md](../02-research/fear-of-failure.md), [integration-touchpoints.md](../02-research/integration-touchpoints.md), [buyer-cost-neighbors.md](../02-research/buyer-cost-neighbors.md), [adversarial-review-2026-11.md](../02-research/adversarial-review-2026-11.md)
- Axiom II (Investment) → [transaction-cost-economics.md](../02-research/transaction-cost-economics.md), [integration-touchpoints.md](../02-research/integration-touchpoints.md), [process-misfit.md](../02-research/process-misfit.md), [information-environment.md](../02-research/information-environment.md), [adversarial-review-2026-11.md](../02-research/adversarial-review-2026-11.md)
- Axiom III (Future Cost) → [transaction-cost-economics.md](../02-research/transaction-cost-economics.md), [klein-crawford-alchian.md](../02-research/klein-crawford-alchian.md), [incomplete-contracts.md](../02-research/incomplete-contracts.md), [process-misfit.md](../02-research/process-misfit.md), [game-theory-and-nrr.md](../02-research/game-theory-and-nrr.md), [real-options.md](../02-research/real-options.md), [costly-signals.md](../02-research/costly-signals.md), [prospect-theory.md](../02-research/prospect-theory.md), [fear-of-failure.md](../02-research/fear-of-failure.md), [cfir.md](../02-research/cfir.md), [re-aim-framework.md](../02-research/re-aim-framework.md), [tce-empirical-record.md](../02-research/tce-empirical-record.md), [adversarial-review-2026-11.md](../02-research/adversarial-review-2026-11.md)
- Second standing assumption (value) → [value-and-persuasion.md](../02-research/value-and-persuasion.md)

**Field operationalization:**
- Where the sale starts, frequency and governance form → [deal-triage-calculator.md](../../practice/deal-triage-calculator.md)
- Blueprint → [01-discovery-contextual-blueprint.md](../../practice/implementation-motion/01-discovery-contextual-blueprint.md)
- Red Team → [02-validation-red-team-protocol.md](../../practice/implementation-motion/02-validation-red-team-protocol.md)
- MIP → [03-closing-mutual-implementation-plan.md](../../practice/implementation-motion/03-closing-mutual-implementation-plan.md)
- Handoff and reputation refresh → [04-sustaining-adoption-review.md](../../practice/implementation-motion/04-sustaining-adoption-review.md)
