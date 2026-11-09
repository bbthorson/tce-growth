---
title: "The Constitution of Transaction Cost Growth (TCG)"
layer: theory
status: active
version: 6.2
---

# The Constitution of Transaction Cost Growth (TCG)

**Version:** 6.2
**Purpose:** To state the three claims from which everything else in this repository derives. Each answers one question at one level: whether a market can exist, what a deal has to pay down at time 0, and what keeps the relationship from churning or contracting at time 1. Each is falsifiable on its own. A claim that cannot be traced to one of them does not belong here.

> [!IMPORTANT]
> **This document states structure and no measured quantity.** The thresholds, rates and band edges that turn its claims into numbers live in [06-calibration.md](./06-calibration.md). None of them is fitted, and a reader can reject any number there without rejecting the claim it sits inside.

Version history is at the end of this document.

---

## Standing assumptions

Three premises sit above the axioms. They are inherited rather than argued, and each is named here so a reader who rejects one knows what falls with it.

1. **Bounded rationality and opportunism** (Williamson 1985). No party can foresee every state the relationship will reach, so every contract is incomplete. And a party will exploit a gap once the other side's position is exposed. The first is why uncertainty has a price. The second is why safeguards exist.
2. **Value is set outside the sale, and it decays.** What a change can be worth to this buyer, its *realizable value* $V_{solution}$, is set by the offer and the buyer's situation: its workflow, its alternatives and what it will invest in adoption. Changing the offer is a product decision, even when a seller makes it inside a deal. Within the sale, the seller moves only the buyer's *recognized value* $\tilde{V}_{solution}$, its current estimate, and what the buyer pays. What the buyer captures after go-live, its *realized value*, rises toward realizable as adoption and delivery proceed. From the triggering event, value decays, $V_{effective}(t) = \tilde{V}_{solution} \cdot e^{-\delta t}$, and the one term in $\delta$ a seller can touch is whether an external catalyst has been named ([02-mathematical-models.md](./02-mathematical-models.md) section 4). The assumption fails if, for the same offer, a claim the buyer cannot check raises realized value after go-live as well as the estimate at signature. [value-and-persuasion.md](../02-research/value-and-persuasion.md) carries the evidence and the objection that survives it.
3. **Every actor acts on their own payoff** (Jensen and Meckling 1976). The parties the axioms reason about are the decision roles on each side and every intermediary between the two firms, and a role's payoff is not its organization's. An actor whose payoff does not depend on the outcome behaves as though the outcome does not matter, whatever their intent. The assumption describes and does not predict bad faith. The instruments build arrangements each party can say yes to, rather than governance designed around opportunism, which can produce the opportunism it assumes. [tce-empirical-record.md](../02-research/tce-empirical-record.md) carries that critique.

---

## Definitions

A *market* is the buyers who call a problem by one name, and a *deal* is one buyer's purchase. Two words carry a narrower meaning.

- **Workflow.** The procedure a product changes. A product encodes a reference workflow, and how far a buyer's version sits from that reference is what makes an investment in the deal specific under Axiom III. A product that cannot name its workflow has no reference to read that distance against.
- **Decision role.** A position in the buyer's organization that holds a veto or an evaluation over the purchase, defined by its relation to the workflow rather than by its occupant: who runs it, who owns it, who pays for it, who polices it. [03-glossary-and-notation.md](./03-glossary-and-notation.md) records what changes when an occupant leaves and when a role dissolves.

---

## The premise

Buying costs more than the price. The buyer has to find a seller it trusts, get its own organization to agree, and make the product work in its own environment. Dahlman (1979) calls these search and information, bargaining and decision, and policing and enforcement. The field calls them *search*, *consensus* and *implementation*, and the notation keeps those as subscripts.

| Cost (field name) | The buyer's question | What lowers it | What sets its cost floor |
|---|---|---|---|
| **Search and information** (search) | Which solutions exist, and does this one fit? | Category definition, education, a channel that reaches the buyer | The information environment: message volume against the buyer's attention, and the category's record |
| **Bargaining and decision** (consensus) | Can my organization agree to this? | Mapping each decision role's exposure, and an arrangement each role can say yes to | The buyer's institutions: procurement rules, spend thresholds, required reviews and how decisions get made |
| **Policing and enforcement** (implementation) | Will the seller deliver what was promised, and will it work here? | Outside validation: references, guarantees, a channel with a stake | The measurement environment: whether outcomes can be attributed and delivery verified |

Bargaining covers agreement among the buyer's decision roles (Webster and Wind 1972) and agreement with the seller on terms. Enforcing those terms after signature is policing. Integrations built and workflows rewired are investments against the policing cost under Axiom II, whichever party makes them.

**The seller can absorb part of each cost.** Sales is the seller absorbing them before the buyer commits, and account management is the seller absorbing them after. A sales organization divides that work by cost: business development absorbs search, the account executive bargaining, the solutions engineer policing, and account management what the relationship costs at time 1 ([01-motions.md](./01-motions.md) section 9).

**Each party acts on what it can check.** So each cost and each value has two readings: what it is, and what a party expects it to be. For a cost, its demand $n_k$ is what the deal asks of the buyer as it is, and $\tilde{n}_k$, the *recognized cost*, is the demand the buyer expects. Before the buyer meets any seller, that expectation is the category's prior. A seller therefore invests twice against a cost: to lower it, and to show it with evidence the buyer can check, such as published terms or a security packet. Only evidence the other side can check changes what the deal is worth to both. A discount changes the split, and persuasion changes only the buyer's reading.

---

## Part I: The Three Axioms

| Axiom | The question | The level |
|---|---|---|
| **I. Law of Transaction Cost Composition** | Can a market exist? | The market, before any deal |
| **II. Law of Transaction Investment** | What has to be paid down at time 0? | The deal, up to signature |
| **III. Law of Future Cost** | What prevents churn and contraction at time 1? | The relationship, after the investment is sunk |

Two sources divide the work. Dahlman classified the costs of using a market by kind, which gives the three costs. Williamson (1985) divided them by time, into the ex ante costs, incurred before the agreement, of drafting, negotiating and safeguarding it, and the ex post costs, incurred after, of maladaptation, haggling and running the governance, and made asset specificity what creates the second. The split by time is the line between Axioms II and III. [transaction-cost-economics.md](../02-research/transaction-cost-economics.md) says why the three stay apart though Dahlman traced them to one root.

---

### Axiom I — The Law of Transaction Cost Composition

> Can a market exist? Each side has a limit. A buyer enters only while every cost it expects, after what the seller and others absorb, sits within what its own people can carry. One cost above that keeps it out, and easing the other two does not bring it back. A seller enters only if the deals it wins there will pay back what it has to build before the first one, the team that absorbs these buyers' costs, and what it spends on the deals it loses. A market exists only where both limits hold. Part of each cost is set outside any deal, by the information environment, the buyer's institutions and how verifiable delivery is. Where that part puts either side past its limit, no single seller's effort opens the market.

*Origin: Coase (1937) for the question, whether to use the price mechanism at all given that using it costs something, and Akerlof (1970) for a market that fails to form. Coase (1960) lists the activities, and Dahlman (1979) groups them into three. The seller's limit follows [04-seller-surplus-model.md](./04-seller-surplus-model.md).*

**The buyer's limit.** Each cost is carried by a payer inside the buyer, named before the outcome: the evaluators carry search, the sponsor bargaining, and the technical and operating owners policing. A cost's *demand* $n_k$ counts what the deal asks of that payer, in its own units. The payer carries up to its capacity $\kappa_k$ alone, the seller or an outside party can move up to $\bar{A}_k$ off it, and nobody can move the rest within the deal, such as a veto that must still be cast. So $\tau^{self}_k = \kappa_k$ and $\tau^{part}_k = \kappa_k + \bar{A}_k$, both read before the outcome and never from whether the buyer bought:

$$r_k = \frac{n_k - \tau^{self}_k}{\tau^{part}_k - \tau^{self}_k}, \qquad k \in \{search,\; consensus,\; implementation\}$$

The position is the share of the movable demand that has to be moved. At $r_k \le 0$ the cost is self-serve, up to one it is bearable once that share is moved, and above one it keeps the buyer out whatever the other two read. No threshold moves with price, though price can add demand, as when a spend threshold adds an approver. What the work costs, $F_k$, is a separate quantity in fractions of annual contract value, and its two parts are the investments in Axiom II's conditions ([02-mathematical-models.md](./02-mathematical-models.md) section 6). The buyer decides on $\tilde{r}_k$, read on the demand it expects, and a buyer with any $\tilde{r}_k > 1$ never enters discovery, so a seller that lowers a cost and does not show it gains nothing with those buyers.

**The costs are non-compensatory.** What the work costs adds, but ease on one never buys back another above its threshold, because each payer's capacity is specific to it: knowledge, authority and skill do not move between payers, and moving people by order is itself work for the sponsor. Costs one payer carries draw on its one capacity and are tested together, so a one-person buyer faces one summed test and a large coalition three. The costs are also coupled: a workflow the product does not fit raises the policing cost and adds decision roles whose objectives worsen, so until fit is verified the policing and bargaining positions are lower bounds ([02-mathematical-models.md](./02-mathematical-models.md) section 3.5).

![Three horizontal bars, one per cost, each ending at that cost's position between its own self-serve threshold at zero and participation threshold at one. Search sits at 0.25, bargaining at 0.83 and policing at 0.44, all within reach of seller investment. A hollow marker shows the buyer expecting policing at 1.22, past the threshold, so it opts out of discovery though the cost itself was within reach.](./assets/axiom-1-where-the-sale-starts.svg)

**The seller's limit.** What a seller builds before any deal, an organization able to absorb the cost these buyers carry, is what no single deal repays. That makes the limit a claim of its own, and not Axiom II's seller condition summed over buyers. The cost of sale is directional: two markets with the same cost of sale can demand it against different costs, so a seller built to absorb one cost reaches only the buyers that cost holds back. Addressable market is a property of what a seller is built to absorb ([05-governance-forms.md](./05-governance-forms.md) section 4).

**Corollaries.**

- **Every cost has a cost floor.** Part of each cost's demand, and a limit on what can be moved off the payer, is set outside the deal, as the premise's table names. Every deal on a floor shares the return from lowering it, so it falls only through investment across deals, such as a marketplace, a certification or a standard, or a seller clears it with a signal costly enough to separate it from the pool. Otherwise a seller chooses its floors with its market and channel. A floor can push either side past its limit, the buyer's participation threshold or the seller's cost of sale. Floors move: the search floor rises as messages outgrow buyers' attention, and the policing floor each time a buyer discovers a misrepresented fit (Akerlof 1970). Each cost also has a category prior, the demand buyers expect before meeting any seller, which follows the floor with a lag. A floor past the participation threshold and a prior past it look alike, since buyers name the problem and buy from no one, and they take different remedies: a shared investment for the floor, a seller showing its own cost for the prior ([information-environment.md](../02-research/information-environment.md), [01-motions.md](./01-motions.md) section 6).
- **Turnkey is a market condition, and it does not last on its own.** Turnkey is the condition under which product-led growth works: every cost self-serve and nothing specific sunk. It is cheap to copy, so competitors enter, and each entrant raises the search floor and blurs good sellers into bad. The market leaves the condition unless a standard, a network effect, a dominant brand or a staked channel holds the search cost down ([02-mathematical-models.md](./02-mathematical-models.md) section 5.8, [01-motions.md](./01-motions.md) section 5.2).

**What would falsify it.** With each cost's payer named and its capacity read from staffing or written authority before any outcome, buyers whose expected demand passes the participation threshold enter discovery as often as matched buyers within it, and buyers measured past it at the decision buy as often. Deals blocked by one payer past its threshold are rescued by lowering a cost another payer carries. [02-mathematical-models.md](./02-mathematical-models.md) section 6 says which readings count as evidence. Sellers who publish evidence the buyer can check of their bargaining and policing costs bring no more buyers into discovery than matched sellers with the same costs who do not. Sellers whose absorbing organization already exists, entering from an adjacent market, enter at contract values no lower than sellers who must build it. Buyer entry rises no faster after a shared investment lowers a market's cost floor than in matched markets where no floor fell. Buyers who discovered a misrepresented fit in a category require no more verification and no more approvers on their next purchase there, from a different seller, than matched buyers who did not. And for Turnkey: in categories where self-serve selling dominated, a rising vendor count does not come before falling trial-to-paid conversion and the arrival of sales-assist teams.

---

### Axiom II — The Law of Transaction Investment

> What has to be paid down at time 0? Every buyer moves through the same stages: awareness, consideration, purchase and renewal. Moving through them is an investment the buyer makes, and from the first stage it prices all three costs, mispricing those it has not reached. The cost it expects nearest its limit decides whether it proceeds at all. The seller absorbs that one first, in fact and in what the buyer can see, so the buyer will invest in the work that lowers both sides' costs. That cost names the motion. Each party goes ahead only if its own share is covered by its own return. Seller spending earns its cost by doing one of two jobs. It raises what the deal creates when the seller does the work more cheaply than the buyer could, or when the work lowers what the relationship will cost at time 1, as discovery does even when it costs more than the buyer would have spent. It lets a deal that creates value go ahead when it shows the buyer, with evidence the buyer can check, a cost lower or a value higher than the buyer expected, including a catalyst it had not named. Spending that does neither only moves cost from one side to the other, as a discount does. The seller recovers its spending through the first contract, renewal, expansion or the deals the relationship unlocks, and spending that nothing repays is a price cut by another name.

*Origin: Williamson (1985), the ex ante costs of a transaction. The seller's side follows [04-seller-surplus-model.md](./04-seller-surplus-model.md).*

**Two conditions, one per party.** Both are in fractions of annual contract value:

$$S_b = V_{switch}(t) - P - \sum_k I^b_k - L_b \qquad S_s = P - C_{deliver} - \sum_k I^s_k - L_s$$

$V_{switch}(t) = \tilde{V}_{solution} \cdot e^{-\delta t} - V_{next\_best}$ is the buyer's opportunity cost of staying where it is, decaying by the second standing assumption, and $V_{next\_best}$ includes building it internally. It is read on recognized value, because that is what the buyer decides on. $P$ is price over the relationship, and $C_{deliver}$ is what delivering costs the seller. $I^b_k$ and $I^s_k$ are what the buyer and the seller invest today against cost $k$. $L_b$ and $L_s$ are each party's expected future loss, from Axiom III. Recurrence enters through $P$ and $C_{deliver}$ summed over expected renewals. Added together:

$$S_b + S_s = V_{switch}(t) - C_{deliver} - \sum_k \left(I^b_k + I^s_k\right) - L_b - L_s$$

Price cancels, because price is a transfer. Read on what the deal can produce, the joint condition uses realizable value, and the difference from recognized value is a loss the buyer carries under Axiom III whether or not it priced it at signature. Persuasion moves the buyer's reading, and the joint condition stays where it was. Hold-up is a transfer too, so it drops out of what the deal creates. It costs both sides through the specific investment a party declines to sink, and where one side fears more hold-up than the other plans, the gap can block a deal that creates value ([02-mathematical-models.md](./02-mathematical-models.md) section 1.3).

![The buyer's surplus falls with price and the seller's rises. Before verification both reach zero at the same price, so no price works and a discount only moves along the axis. After verification lowers each side's expected future loss, a window opens where both say yes.](./assets/axiom-2-price-window.svg)

**The motion is where the sale starts.** The sale starts at the cost with the largest $\tilde{r}_k$ before the buyer enters, and the largest $r_k$ once discovery measures it. The motion is named for that cost: search-led, consensus-led or implementation-led. *Starts* means the seller's first investment, since every buyer moves through the same stages. Product-led and sales-led name the seller rather than the cost. Until fit is verified, the reading understates the policing and bargaining costs, so a seller who misrepresents fit hides where the sale starts until the investment is sunk. [01-motions.md](./01-motions.md) carries the map.

**Corollaries.**

- **Price is not a transaction cost, though its size against the buyer's spend thresholds sets who must approve.** A deal split or ramped under a threshold removes a decision role's veto without settling its exposure, which Axiom III says returns at renewal.
- **Forward-deployed engineering works two ways at once.** The seller's engineers adapt their own product at lower cost, and their presence in use catches misfit while it is cheap. It also creates a future cost for the seller, because the engineering is specific to this buyer.
- **Copying a motion copies another market's costs.** Product-led growth where the costs are not all self-serve leaves the buyer holding a cost it cannot pay down alone, and forward-deployed engineering where policing is not where the sale starts pays for an adaptation nobody needed. Read the other way, the investment a motion demands is its defense against entry.

**What would falsify it.** Deals where the seller's first investment went to the cost with the largest $r_k$, recorded before that investment and never revised, convert no faster than deals by the same representative where it went elsewhere. Deals where the seller absorbed part of the buyer's investment close at no higher rate than matched deals where it did not, at equal total cost. And cost of sale spent on discovery and verification predicts net revenue retention no better than cost of sale spent on persuasion.

---

### Axiom III — The Law of Future Cost

> What prevents churn and contraction at time 1? Whatever a party sinks that pays off only in this relationship exposes it to what it cannot check or stop later. Left alone, that exposure shows up as churn, as contraction at renewal, or as a seller that stops delivering. So time 1 is decided at time 0, before either side sinks anything. What the parties can foresee, they contract for: who carries which exposure, staged how, and what each loses by walking away. What they cannot foresee, they plan for with a standing review that carries rights either side can invoke, such as a quarterly business review that can trigger re-scoping, so drift is caught before renewal. Drift has two sources. What was verified goes stale, and the fit itself moves as either side changes.

*Origin: Williamson (1979, 1985), the ex post costs of a transaction and the specificity that creates them. Klein, Crawford and Alchian (1978) for whose exposure it is. Spence (1973) for why only costly evidence reduces it. Hart and Moore (1988) for hold-up under full information.*

**Specificity.** An investment is specific when it loses value outside this relationship. For the buyer, specificity is read as distance from the reference workflow: the further the buyer's version sits from what the product assumes, the more adaptation the deal requires and the less of it survives a failed deal. Once a specific investment is sunk, the party who made it can be held up, because the other side can extract the difference between what it is worth here and what it is worth anywhere else. Klein, Crawford and Alchian named that difference the appropriable quasi-rent, and the exposure follows the investment rather than the invoice, buyer or seller. Where the seller sinks first, as with forward-deployed engineering, the seller holds the exposure and its allocation has to be settled before the seller spends, which can be well before signature.

**Who cannot check what.** Exposure becomes cost through what the exposed party cannot verify, and what it can see but cannot stop. Each cost runs between its own pair of parties.

| Cost | Whose uncertainty, about what | What resolves it |
|---|---|---|
| Search and information | The buyer's, about the market. Which alternatives exist and whether this one fits. | Artifacts that travel without the seller: category definition, reference architectures, verifiable proof, a channel with a stake |
| Bargaining and decision | Each decision role's, about its own outcome. What the change does to its budget, headcount and standing. | Mapping who loses what, one role at a time, and answering it in the arrangement. Objections are collected apart before any room convenes, because a room suppresses what only one member knows |
| Policing and enforcement | Bilateral. The seller's, about the buyer's environment. The buyer's, about the seller's capability in it. | Discovery that maps the environment, and demonstrations the seller pays to produce |

The search gap mostly prices today's cost and decides participation under Axiom I. The other two decide the future loss. The bargaining gap holds opposed interests that proof cannot reconcile: two decision roles with perfect knowledge of each other can still disagree. What proof can close is each role's uncertainty about its own exposure.

**Contract what can be foreseen, plan for what cannot.** Some misfits surface only in use (Strong and Volkoff 2010), so the parties settle in advance who carries which risk and adapt later (Crocker and Reynolds 1993, Bajari and Tadelis 2001). The more one side sinks relative to the other, the more they must settle first ([02-mathematical-models.md](./02-mathematical-models.md) sections 5.5 and 5.6). Where the contract is silent, whoever holds the right to decide governs (Grossman and Hart 1986). A party that expects to be held up there will not invest, so legal review moves a stalled specific deal only by allocating who owns the integration and the data. For what nobody can foresee, the parties agree a standing review, which the drift corollary below describes.

**Mathematical content.** Each party's expected future loss is its exposure times the chance the exposure does not come back:

$$L_p = Q_p \cdot \pi_p, \qquad Q_p = C^{p}_{invest} - R^{p}_{redeploy}, \qquad p \in \{b, s\}$$

$C^{p}_{invest}$ is what party $p$ sinks in the relationship and $R^{p}_{redeploy}$ what it would recover elsewhere. $L_p$ is a shortfall in the return $p$ expected, through hold-up or through a fit that fails in use, separate from the investment Axiom II already counted. The quasi-rent $Q_p$ bounds it, because it is the most the other side can extract or a failure can destroy. $\pi_p$ rises with the gaps party $p$ cannot close, and with what the other side can take in plain view at a renegotiation ([02-mathematical-models.md](./02-mathematical-models.md) section 5.5). Absent maintenance, each gap in the table above, normalized as $\hat{\Delta}_k \in [0, 1]$, rebuilds toward its ceiling at rate $\gamma_k$:

$$\hat{\Delta}_k(t) = 1 - \left(1 - \hat{\Delta}_k(0)\right) e^{-\gamma_k t}$$

Discovery is a separate, discrete step down, paid for by whoever runs it, and it is where Axiom II's spending pays off here. A departed champion is the bargaining gap reopening all at once, and a deal can leave the viable zone with no change in product, price or technical work.

![Two rising curves from a near-zero implementation gap at go-live, against a horizontal line marking where a challenger begins. The unmaintained curve bends toward the challenger line and nearly reaches it within three years. The maintained curve levels off well below it, where maintenance matches the rebuild.](./assets/axiom-3-asymmetry-drift.svg)

A buyer who commits in stages sinks $Q_m$ at gate $m$ against residual uncertainty $x_m$, so the expected loss is $\sum_m Q_m \, \pi(x_m)$ rather than $Q \, \pi(x_0)$. Staging puts the small commitments where the uncertainty is high. When an investment is irreversible and the environment uncertain, the right to wait has value, and a contract demanding full commitment at once asks the buyer to destroy it (Dixit and Pindyck 1994). The Stage column of the [Enforcement Ledger](../../practice/enforcement-ledger.md) is the instrument.

**Corollaries.**

- **The gate.** Where nothing specific is sunk and a trial verifies fit, the future cost is near zero and market terms hold: the buyer verifies by trying and walks away at no cost. Specificity is the master variable for governance, and apparatus applied below it is the over-frictioned failure.
- **Governance form.** With frequency, specificity selects the arrangement that holds the deal: market terms where nothing specific is sunk, a third-party safeguard for a specific one-shot deal, bilateral governance where each repetition safeguards the next, and eventually integration, which for the seller means the buyer builds it. Recurrence is partly the seller's choice, and what it buys is mutual sanction, credible only when both sides hold exposure at the next boundary. A one-sided cheap exit hands the seller's sunk investment to the buyer to hold up (MacLeod and Malcomson 1989). The Mutual Implementation Plan is the bilateral form's instrument ([05-governance-forms.md](./05-governance-forms.md)).
- **Enforcement governs what verification cannot.** A party that can see the other side refuse to adapt or force a renegotiation, and cannot stop it, is exposed under full information, and no proof protects it (Wathne and Heide 2000). The contract answers with a hostage, something the other side loses by defecting, such as staged fees or a reciprocal specific investment, or with an allocated right, such as an option to renew at a preset price or a right to stop at a price agreed up front. Both run in both directions. A discount changes the price once. A hostage or an allocated right changes what defection costs at every boundary that follows ([incomplete-contracts.md](../02-research/incomplete-contracts.md)).
- **Every party holding exposed rent, or adjudicating it, needs a stake.** That includes the seller's own representative, whose reading of the deal the seller sinks on, and any channel that vouches for a seller. [05-governance-forms.md](./05-governance-forms.md) section 5 derives the stakes.
- **The Friction Allocation Principles.** A mechanism reduces a gap only if its cost cannot be automated away, is borne by the claimant rather than the receiver, scales with the size of the claim, and is adjudicated by someone who loses when a bad signal passes. Violate any one and the mechanism is cheap talk, which informs only as far as the two sides' interests already agree (Crawford and Sobel 1982). Spence's single crossing property, that a signal costs a weak seller more than a strong one, backs the first three for signals the seller sends. The fourth comes from the theory of certification intermediaries. The [Friction Allocation Diagnostic](../../practice/friction-allocation-diagnostic.md) tests them.
- **Three levers, and why verification wins.** A discount moves price and is a pure transfer. A guarantee is part transfer and part verification: it moves future loss to the seller, makes the seller work harder, and tells the buyer which seller it faces, because only a seller confident of delivering can afford it. Direct verification lowers $\pi_p$ outright. Of the three, only verification raises what the deal creates, so a resolved gap can close a deal no discount could. Whether a given verification costs less than the loss it removes stays empirical.
- **Planning for drift is maintenance, and account management is the seller's.** What was verified goes stale, so credibility is re-earned with evidence of continued delivery. Re-verification cannot reach fit drifting as either party changes, which only re-adaptation, notice of change or a change process agreed in advance can govern. The standing review is where both get read before renewal reads them. The seller funds account management while the margin it holds at the next boundary covers keeping pace with the rebuild ([02-mathematical-models.md](./02-mathematical-models.md) sections 5.3 and 5.7, [Sustaining Adoption Review](../../practice/adoption-review.md)).
- **The Decay Clock.** Value decays while the gaps rebuild, so a deal viable at $t_0$ needs intervention to stay viable at $t_1$ ([02-mathematical-models.md](./02-mathematical-models.md) section 4).

**What would falsify it.** Specific deals with pre-agreed staging and stop rights write off no smaller a share of what each side sank than specific deals without them. Deals where verification closed a gap fail after signature at the same rate as matched deals where it did not. At equal verification, deals where both parties hold something to lose, or where the right to renew or stop was allocated in advance, drift after signature as often as deals where only one side has sunk investment and nothing was allocated. And relationships with a review carrying rights either side can invoke, agreed before anything was sunk, keep no more revenue at renewal than matched relationships without one.

---

## Part II: The Two Conditions

The three axioms are what the terms of two conditions mean.

$$S_b = V_{switch}(t) - P - \sum_k I^b_k - L_b > 0 \qquad S_s = P - C_{deliver} - \sum_k I^s_k - L_s > 0 \qquad r_k \le 1 \;\; \forall k$$

- The participation clause, $r_k \le 1$ for every cost, with the costs one payer carries fitting its capacity together, is **Axiom I**, and so is the seller's condition asked of the whole market.
- The investments $I^b_k$ and $I^s_k$, the fact that there are two conditions rather than one, and the cost with the largest $r_k$ as where the sale starts, are **Axiom II**.
- The future losses $L_b$ and $L_s$, and the rebuild that moves them over time, are **Axiom III**.
- $V_{switch}(t)$ decays by the second standing assumption.

A deal closes when both conditions hold at the moment of decision and no cost keeps the buyer out. It persists when the governance form selected under Axiom III holds every party's weight on the future above the cooperation threshold, the point at which keeping faith pays better than defecting ([05-governance-forms.md](./05-governance-forms.md) section 5), and when the gaps are maintained faster than they rebuild.

**Reading a stall.** Ask the three questions in order, because each assumes the one before it holds.

1. **Can this market exist?** Is any cost, as this buyer expects it, past its threshold, or are the costs one payer carries past its capacity together, or does the seller's cost of sale in this market exceed what its contracts return? No work on the other costs reaches it. Pull it back into range, invest across deals if a cost floor holds it there, or decline. (Axiom I.)
2. **Is the deal paying down the right cost at time 0?** Is the seller absorbing the cost nearest its threshold, does each party's share fit inside its own return, and does the seller's spending raise what the deal creates, let it go ahead, or only move cost? (Axiom II.)
3. **Is time 1 contracted and planned?** Was the allocation settled before anything specific was sunk, is a review in place, and is any gap rebuilding faster than discovery closes it? (Axiom III.)

The [Deal Triage Calculator](../../practice/deal-triage-calculator.md) asks the same three questions of a live deal.

**Failure modes, collected.**

| Axiom | Failure | Signal |
|---|---|---|
| I | Kept out | A cost above the participation threshold worked as though it were a sales problem |
| I | Unshown | A cost the seller lowered and never showed, so the buyer's recognized position kept it out of discovery |
| I | Unamortizable | What the seller builds for a market, or spends on one deal, exceeds what the deals it wins return |
| I | Turnkey erosion unread | A self-serve motion kept running while entry raises the search cost |
| I | Akerlof saturation | Telling good sellers from bad costs more than any affordable signal can cover, and the buyer exits |
| I | Jevons collapse | Channel friction was production cost and fell to zero, the search cost floor rises, and the channel stops separating sellers |
| II | Mis-sequenced | The seller's first investment went to a cost that was not nearest its threshold |
| II | Imitation | A motion copied from another market, organization built to pay down a cost its buyers do not carry |
| II | Under-invested | The buyer is left holding a cost it cannot pay down alone |
| II | Over-invested | The seller pays down a cost that was not near its threshold |
| II | Spent as a discount | Seller spending that neither raises what the deal creates nor lets it go ahead, and nothing recovers it |
| III | Unallocated | Specific investment sunk with no staging or stop rights agreed, buyer signs, fails to deploy, churns |
| III | Over-frictioned | Governance apparatus on a deal where nothing specific is sunk, buyer chooses a lighter competitor |
| III | Mis-governed | Frequency ignored or sanction one-sided, wrong arrangement for the repetition pattern |
| III | Unhostaged | Hold-up under full information met with more verification or a discount, when only a change in what defection costs would stop it |
| III | Defection | A party's weight on the future below threshold, hold-up on either side |
| III | Cheap talk | Signal fails single crossing, no gap moves |
| III | Misallocated friction | Receiver bears the filtering cost |
| III | Wrong gap closed | Effort on a gap that was already low |
| III | Unreviewed | No review agreed at time 0, and the first reading of drift is the renewal |
| III | Reputation hoarding | Past signals unrefreshed, incumbent coasts |
| III | Option value dominates | Case accepted, commitment deferred, full commitment demanded before uncertainty resolves |

Each mode names one axiom and one place to intervene. A stall matching none of them means the table is incomplete, which is itself worth recording in [07-open-questions.md](./07-open-questions.md).

---

## Version History

**Current version: 6.2.** The framework's version tracks this document's, and the root README footer must agree, which `check_frontmatter.py` enforces.

<!-- vale TCG.RetiredTerms = NO -->
| Version | Date | Change |
|---|---|---|
| 6.2 | 2026-11 | After the 2026-11-09 research review. The gate reads each cost's demand in its payer's own units, against the payer's capacity and that capacity plus what the seller or others can move off it, read before the outcome. What the work costs is a separate quantity, so no threshold moves with price. Non-compensation follows from capacity specific to each payer, and costs one payer carries are tested together. |
| 6.1 | 2026-11 | After three adversarial reviews and a convergence check. Seller spending does two jobs, raising what the deal creates or letting it go ahead, and is recovered through the relationship or the deals it unlocks. The seller's limit rests on what it builds before any deal. Hold-up is a transfer, costly through deterred investment and a wedge of unshared fear. Seven falsifiers are restated so each can fail. The practice layer was rebuilt from 6.1 by 2026-11-09, and the 5.0, 6.0 and practice rebuild proposals retired to git history (`git show b5b3386:<file>`). |
| 6.0 | 2026-11 | The axioms answer three questions at three levels: market, deal at time 0, relationship at time 1. A premise states the three costs, the seller absorbing them, and that each party acts on what it can check. The seller's limit and cost floor move to Axiom I and the motion to Axiom II. Axiom III contracts what can be foreseen and plans a review for what cannot. The derivations table leaves, and the stall reading moves to the Deal Triage Calculator. |
| 5.2 | 2026-11 | Each cost gains a recognized cost, the buyer's estimate before it meets the seller, and participation is decided on it. The unshown failure mode and the category prior are added. |
| 5.1 | 2026-11 | The share settled in advance rises with the imbalance in what the parties have sunk. Coupling, the two kinds of drift, account management and the stakes for agents are stated. |
| 5.0 | 2026-11 | Value splits three ways, the costs become non-compensatory, the cost floor is added, and Axiom III widens to what a party cannot verify or enforce. |
| 4.1 | 2026-10 | A guarantee is part transfer and part verification. |
| 4.0 | 2026-10 | The axioms are restated as three decisions in time order, with Dahlman's names, a participation threshold per cost, two conditions in which price cancels, and the Law of Future Cost. Turnkey becomes a market condition, and Structural, the summed level and seat retire. |
<!-- vale TCG.RetiredTerms = YES -->

Versions 1.0 to 3.0, and the nineteen revisions made under the earlier name, are in the git history: `git log -- theory/01-foundation/00-tcg-constitution.md`, then `git show <commit>:theory/01-foundation/00-tcg-constitution.md`. `RetiredTerms.yml` cites those version numbers when it records what each one retired.

---

## Related

**Sibling theory:**
- [01-motions.md](./01-motions.md)
- [02-mathematical-models.md](./02-mathematical-models.md)
- [03-glossary-and-notation.md](./03-glossary-and-notation.md)
- [04-seller-surplus-model.md](./04-seller-surplus-model.md)
- [05-governance-forms.md](./05-governance-forms.md)
- [06-calibration.md](./06-calibration.md)
- [07-open-questions.md](./07-open-questions.md)
- [08-from-axioms-to-instruments.md](./08-from-axioms-to-instruments.md)

**Academic backing:** [00-reading-guide.md](../02-research/00-reading-guide.md) maps each research file to the axiom it backs.

**Field operationalization:**
- Whether a buyer can enter, where the sale starts, frequency and governance form → [deal-triage-calculator.md](../../practice/deal-triage-calculator.md)
- Map, Test and Stage (the Blueprint, Red Team and Mutual Implementation Plan) → [enforcement-ledger.md](../../practice/enforcement-ledger.md)
- Bargaining: the decision-role map, the arrangement record and the safeguard inside the buyer → [bargaining-ledger.md](../../practice/bargaining-ledger.md)
- Maintain: the handoff, the standing review and renewal → [adoption-review.md](../../practice/adoption-review.md)
