---
title: "The Constitution of Transaction Cost Growth (TCG)"
layer: theory
status: active
version: 7.0
---

# The Constitution of Transaction Cost Growth (TCG)

**Version:** 7.0
**Purpose:** To state the twelve claims everything else in this repository derives from. A buyer and a seller make three decisions in order: whether to enter a market, whether to sign, and whether to renew. Each axiom covers one of those times and asks one question of each party. Each claim carries a test that could fail. A claim that cannot be traced to one of the twelve does not belong here.

> [!IMPORTANT]
> **This document states structure and no measured quantity.** It holds no equation, threshold or rate. The one piece of accounting it relies on, that price is a transfer between the two parties, is in [02-mathematical-models.md](./02-mathematical-models.md) sections 1.1 to 1.4.

> [!NOTE]
> **The rest of the repository was rewritten around 7.0** in the trim of 2026-11-10. Where a file and this document disagree, this document governs. The proposal that set out the trim is in git history: `git show 59ab41e:TRIM-PROPOSAL.md`.

Version history is at the end of this document.

---

## Standing assumptions

Three premises sit above the axioms. They are inherited and not argued here, and each is named so a reader who rejects one knows what falls with it.

1. **Bounded rationality and opportunism** (Williamson 1985). No party can foresee every state a relationship will reach, so every contract is incomplete. And a party may exploit a gap once the other side cannot easily leave. The first is why uncertainty has a price. The second is why safeguards exist.
2. **Value is set outside the sale, and it fades.** What a change can be worth to a buyer is set by the offer and the buyer's situation. Changing the offer is a product decision, even when a seller makes it inside a deal. Within the sale the seller changes what the buyer knows and what the buyer pays. A buyer's reason to act fades with time unless a dated event holds it in place. [value-and-persuasion.md](../02-research/value-and-persuasion.md) carries the evidence and the objection that survives it.
3. **Every actor acts on their own payoff** (Jensen and Meckling 1976). The parties are the decision roles on each side and every intermediary between the two firms, and a role's payoff is not its organization's. The assumption describes and does not predict bad faith.

---

## Definitions

A *market* is the buyers who call a problem by one name, and a *deal* is one buyer's purchase.

- **Workflow.** The procedure a product changes. It has two readings. How *settled* it is: written down, followed, with its exceptions known. How *entangled* it is: how much else changes when it changes.
- **Decision role.** A position in the buyer's organization that can stop or must approve the purchase, defined by its relation to the workflow and not by its occupant: who runs it, who owns it, who pays for it, who polices it.
- **Plug-in and built-in.** A *plug-in* purchase works on arrival. The buyer can try it on its own work, and can walk away having stranded nothing. A *built-in* purchase has the buyer, the seller or both build something that is worth less anywhere else: integrations, changed workflows, training. Economists call such an investment *specific* (Williamson 1985), and the research files keep that word.
- **Motion.** What a seller does, and is organized to do, to carry part of a buyer's cost. A seller is *built for* a cost when a named person or team does each piece of that motion's work today. [01-motions.md](./01-motions.md) section 3 lists the work.
- **Turnkey.** A market where buyers can carry every cost alone and the purchase is plug-in.

---

## The premise

Buying costs more than the price. The buyer has to find a seller it trusts, get its own organization to agree, and make the product work in its own environment. This document calls those three costs *search*, *consensus* and *implementation*.

They descend from the three costs of using a market that Dahlman (1979) named: search and information, bargaining and decision, and policing and enforcement. They differ from his in two places. Consensus is the buyer's own people reaching agreement, which is one half of his bargaining and decision. Implementation covers making the product work in the buyer's environment as well as checking that the seller kept its terms, which is wider than his policing and enforcement. His three run in the same order as the three times here, with search before the bargain and policing after it.

Implementation has three parts: the buyer's doubt that the product will fit, the work of making it fit, and checking that the seller delivered. Williamson would count the work as a cost of production. It sits here because the buyer weighs it in the same decision, because either party can do it, and because all three parts grow with what has to be built. A plug-in purchase has almost none of the three. So these are the buyer's costs of buying, which is wider than transaction costs in the economists' sense.

| Cost | The buyer's question | Home time | What lowers it |
|---|---|---|---|
| **Search** | Which solutions exist, and which seller can I trust? | Time0 | A named category, a channel that reaches the buyer, a signal that costs the seller something |
| **Consensus** | Can my organization agree to this? | Time1 | Each decision role's concern answered in the arrangement |
| **Implementation** | Will it work here, and will the seller deliver? | Time2 | Discovery, proof in the buyer's own environment, a plan both sides hold |

**A cost is named for the buyer's question, and not for when the buyer asks it.** A trial answers the implementation question before signature, and it settles it only for a plug-in purchase. Consensus is about who must agree. Implementation is about what must work. Before signature the work has not started, so the buyer holds only a fear of it, and each role holds its own: that the product will not work, or that the change will cost the role its budget, headcount or standing. Either fear reaches the deal as a role that will not agree. So at Time1 implementation acts as consensus, which is claim 7, and a buyer that looks and decides nothing has stopped at consensus whichever fear lies behind it.

**The seller can carry part of each cost.** Sales is the seller carrying it before the buyer commits, and account management is the seller carrying it after. That pays when the seller does the work more cheaply than the buyer could, usually because it has done the work many times and the buyer is doing it once. A seller funded from outside the market can carry a cost at a loss that no deal repays. The market then looks easier to sell into than it is, and the cost returns when the funding stops.

**Each party acts on what it can check.** A buyer decides on the cost it expects, which can differ from the cost it would meet. Before it meets any seller, that expectation is what the category has taught it. A seller that lowers a cost and never shows it gains nothing with buyers who never look. Only evidence the other side can check changes what it expects.

**The costs are not independent, and they are not walls.** The work of the three mostly runs in the order of their home times. Two things run side by side at Time1: the organization reaching agreement, and the buyer checking whether the product will work here. Conditions run forward: the market shapes the deal, and the deal shapes what the relationship has to manage. Expectations run backward: a buyer prices a later cost when it makes an earlier decision. A cost can stop a deal, and a large enough gain or someone else doing the work can offset it. A buyer that knows its organization is hard to move looks only for a change it cannot deny or for a seller who will do the legwork. One exception. A rule that forbids a purchase outright is a wall, and no gain offsets it. A rule that adds work can be offset like any other cost, and claim 4 says who can lower it.

---

## Part I: The Three Axioms

| Axiom | Time | The buyer asks | The seller asks |
|---|---|---|---|
| **I. Law of Transaction Cost Composition** | Time0, the market | Buy, build or do nothing? | Can I serve these buyers at a profit? |
| **II. Law of Transaction Investment** | Time1, contracting | Can my organization agree, and what will this take? | Is this deal worth what it takes? |
| **III. Law of Future Cost** | Time2, renewal | Did it work here, and am I free to leave? | Does the relationship pay? |

Two sources divide the work. Dahlman classified the costs of using a market by kind, which gives the three costs. Williamson (1985) divided them by time, into the costs of reaching an agreement and the costs of living under it. That split is the line between Time1 and Time2. [transaction-cost-economics.md](../02-research/transaction-cost-economics.md) carries both.

---

### Axiom I: The Law of Transaction Cost Composition

> At Time0 the buyer decides whether to buy, build or do nothing, and the seller decides whether it can serve these buyers at a profit. Which cost stands in the buyer's way is a fact about the market, and a seller can read it before any deal. It decides how the product has to be sold, what the seller has to be built to do, and what the seller pays its people for.

*Origin: Coase (1937) for the insight that using a market costs something. Dahlman (1979) for the three costs. Akerlof (1970) for a market that fails to form. Attewell (1992) is the nearest ancestor of claim 1: one barrier, the know-how to implement, set how business computing was bought.*

**Claim 1. The kind of cost in the way decides how to sell.** A motion is named for the cost it carries: search-led, consensus-led or implementation-led. Product-led and sales-led name the seller's tool and say nothing about the buyer. Leaders often pick a motion because it is in fashion. They hire forward-deployed engineers where implementation is not what stops their buyers, or add outbound email where the market is already too loud to hear it. The relay model gives each funnel stage one role and one fixed playbook and pays on bookings. It is the right motion for a Turnkey market and the wrong one elsewhere. [01-motions.md](./01-motions.md) maps the incumbent names.

*Fails if*, in a market where most stopped buyers stop in one place, sellers built for the cost at that place win and keep buyers no better than sellers in the same market built for another. Where buyers stop is read from sellers' records and from a survey of buyers no seller has met, and not from claim 2's reading. It also fails if a seller that adds one motion's work sees its win rate and retention rise no more among buyers who were stopping at that cost than among buyers who were stopping elsewhere.

**Claim 2. Two things a leader can see predict that cost before any deal.** Both are read across the buyers in a market. Buyers stop in three places, one for each cost: they never look, they look and decide nothing, or they sign and fail to adopt. Each reading names the place where more buyers stop.

| What the leader can see | What it predicts | Where more buyers stop | What selling has to do |
|---|---|---|---|
| The workflow is not settled | The buyer cannot yet name what it is buying | They never look | Teach, by giving the buyer a hypothesis about its own workflow |
| The workflow is settled and stands alone | Little is in the way | Nowhere more than elsewhere | Let the buyer try it |
| The workflow is settled and entangled | A change has knock-on effects | They sign and fail to adopt | Prove it will work here, and carry the change |
| The buyer's organization is complex | More roles can say no, and more has to change | They look and decide nothing | Bring the organization to a decision |

A buyer that expects a later cost can stop earlier. So each row compares markets, and it does not place every buyer.

*Fails if* any of three orderings is absent across markets read before any deal. Fewer of a market's buyers start an evaluation with any seller where the workflow is not settled than where it is. More of the buyers who look decide nothing where the organization is complex than where it is simple. More of the buyers who sign fail to adopt where the workflow is entangled than where it stands alone.

**Claim 3. A claim that costs nothing to make raises every buyer's search cost.** Where buyers cannot tell good sellers from bad, they assume the worst and many buy from no one (Akerlof 1970). Each seller's message also adds to a volume that no seller pays for, so more outreach into a loud market lowers the response to every sender ([channel-collapse.md](../02-research/channel-collapse.md)). A buyer believes a seller for what it gave up: a published price, a capped customer load, a guarantee. Such a signal informs only when it costs a weak seller more than a strong one (Spence 1973). Insight given away works the same way. It helps rivals too, and it is believed because it cost something. The same test applies to whoever recommends a seller. A channel, marketplace or analyst paid on referral loses nothing when a bad recommendation passes, so its word is cheap too. The [Friction Allocation Diagnostic](../../practice/friction-allocation-diagnostic.md) tests a signal. A Turnkey market does not stay Turnkey on its own, because a market that is cheap to enter fills with sellers whose claims all sound alike.

*Fails if* sellers who publish a commitment that costs them bring no more buyers into a first conversation than matched sellers who make the same claim without one. It also fails if response to every sender holds steady while message volume per buyer rises in a category.

**Claim 4. Rules set a floor that no single deal lowers, and the floor favors whoever has already paid it.** A *floor* is the part of a cost set outside any deal: the volume of messages against the buyer's attention, the buyer's procurement and compliance rules, and whether anyone can attribute an outcome. No work inside one deal lowers it, because no single deal repays the work. It falls only through something shared across deals. Where a market shares that, as a standard, a mandate or a marketplace, the floor falls for every seller. Where one seller holds it, as a certification or a pre-approved contract, the floor falls for that seller's deals alone. So a seller that has already paid stands on a lower floor than its rivals, and a new rule moves a market toward the sellers that had paid beforehand. Paying gives a seller permission to sell and brings it no customers. Where no seller has paid, buyers at a floor mostly stop. The ones with the most to gain get through, unless the rule forbids the purchase outright. [information-environment.md](../02-research/information-environment.md) carries the evidence.

*Fails if* buyers enter no faster after a shared investment lowers a market's floor than in matched markets where no floor fell. It also fails if, after a rule raises a floor, share does not move toward sellers that had paid it beforehand.

**Claim 5. A seller reaches only the buyers whose cost it is built to carry, and it pays its people for work on that cost.** What a seller builds before its first deal, the people and methods that carry one kind of cost, is something no single deal repays. Its addressable market is therefore set by what it is built to do. Deals that die at the same stage for the same reason are usually outside that reach, and coaching representatives harder does not bring them in. Pay follows the same cost. Where little is in the way, pay rewards fast movement from search to contract. Where implementation is in the way, part of the pay waits until the implementation confirms the scope. That holds only where the seller has defined what a complete discovery is. Where it has not, the representative is not paid on an outcome they cannot affect.

*Fails if* sellers entering from an adjacent market, with the organization already built, enter at contract values no lower than sellers who must build it. It also fails if, where discovery is defined, representatives paid partly on confirmed scope produce as many scope changes after signature as representatives paid on bookings alone.

---

### Axiom II: The Law of Transaction Investment

> At Time1 the buyer decides whether its organization can agree and what the purchase will take, and the seller decides whether the deal is worth what it takes. Both invest before signature. What matters is what the investment buys: a buyer that knows what it will face, or money moved from one side to the other with the cost left where it was.

*Origin: Williamson (1985), the costs of reaching an agreement. Webster and Wind (1972) for the buyer as a coalition. Walton and McKersie (1965) for bargaining that creates value against bargaining that divides it. Dixon and McKenna (2022) for limited and reversible commitments as the remedy for indecision.*

**Claim 6. A purchase is plug-in or built-in.** Three tests make it plug-in, and all three must hold. The buyer can run the product on its real work without the seller's engineers. A bad fit costs it days. Walking away strands no spend and no data. A plug-in purchase needs standard terms and a trial, and discovery workshops and joint plans laid over it lose the buyer to a lighter competitor. A built-in purchase needs the rest of this axiom. The [Deal Triage Calculator](../../practice/deal-triage-calculator.md) asks the three tests of a live deal.

*Fails if* discovery, staging and a joint plan before signature raise close rates and renewal as much for plug-in purchases as for built-in ones.

**Claim 7. Implementation is a fear at Time1, and it acts through the buyer's own people.** The work comes at Time2. At Time1 the buyer holds only an expectation of it, and each decision role asks what the change does to its own budget, headcount and standing. A buyer that cannot buy alone looks for the reasons its colleagues will say no, and a demonstration aimed at one person hands it more of them. So the seller invites the organization's scrutiny. It collects each role's objection apart, before any room convenes, and it walks the buyer through how the project would fail before anyone signs. Some deals die under that scrutiny. Each death counts against the practice, which has to earn it back in what the surviving deals keep. An agreement between the two firms binds the buyer that signs it. It does not bind the role whose budget the change cuts. So the arrangement answers each role by its position, which a successor inherits, and a sponsor with something riding on the outcome holds it together. [buying-center-dynamics.md](../02-research/buying-center-dynamics.md) carries the evidence, and the [Bargaining Ledger](../../practice/bargaining-ledger.md) is the instrument.

*Fails if* roles at buyers that cannot buy alone, asked one to one, object to what the change does to their own budget, headcount or standing no more often on built-in purchases than on plug-in ones. It also fails if, among buyers that cannot buy alone, deals where the seller collected each role's objection before a group demonstration keep no more revenue at first renewal, per deal opened, than deals led with the demonstration.

**Claim 8. A discount moves money and lowers no cost.** Price is a transfer: what leaves the buyer arrives at the seller, and the work of buying is the same size afterward. There is one exception. A price taken under a spend threshold removes an approver, and that role's concern comes back at renewal. A discount can also tell the buyer the wrong thing about the seller, and customers acquired on deeper discounts have been found to buy again less (Lewis 2006). What lowers the buyer's fear is a commitment the seller would not make if it expected to fail: capped overages, remediation hours written into the contract, a guarantee tied to the buyer's own environment. The seller trades such a commitment for what the buyer knows about that environment.

![The buyer's surplus falls with price and the seller's rises. Before verification both reach zero at the same price, so no price works and a discount only moves along the axis. After verification lowers each side's expected future loss, a window opens where both say yes.](./assets/axiom-2-price-window.svg)

*Fails if* stalled deals offered a discount that takes the price under none of the buyer's approval thresholds reach signature more often than matched stalled deals offered nothing. It also fails if a commitment whose largest possible cost to the seller is no more than a discount's brings no more stalled built-in deals to signature than that discount does.

**Claim 9. Work skipped at Time1 moves to Time2 and grows.** Discovery left out of the sale comes back during implementation as scope changes, missed dates and a delivery team working to make the contract fit the environment. Work pulled forward has a cost too. The seller spends it whether or not the deal closes, and the relationship repays it, so a seller that tests the work against the first contract alone turns away deals a renewal would justify. The buyer pays for it through a price averaged across all the seller's deals, so buyers with easy implementations overpay and a lighter rival can win them. A seller therefore pulls forward the work its market's buyers need, by claim 2, and no more.

*Fails if* built-in deals with discovery done before signature show as many scope changes after signature as matched deals without it. It also fails if buyers with simple implementations choose a seller that prices in heavy engineering before signature as often as buyers with hard ones do.

---

### Axiom III: The Law of Future Cost

> At Time2 the buyer decides whether the product worked here and whether it is free to leave, and the seller decides whether the relationship pays. Most of what decides both was settled at Time1.

*Origin: Williamson (1979, 1985), the costs of living under an agreement and the specific investment that creates them. Klein, Crawford and Alchian (1978) for whose exposure it is. Grossman and Hart (1986) for who decides where the contract is silent.*

**Claim 10. Whether the product worked here decides renewal.** Some misfits surface only in use (Strong and Volkoff 2010), and what the two sides verified before signature goes stale as either side changes. Account management is the seller carrying that cost after signature, and a review held before the renewal is where both sides read it. A buyer that built more stays longer on a failing fit, so failure shows first as stalled use and contraction and only later as an exit. Exits caused by an event outside the relationship, such as the buyer's own failure or an acquirer's contract, are out of scope. The [Sustaining Adoption Review](../../practice/adoption-review.md) is the instrument.

*Fails if* accounts whose outcome measure, signed under claim 12, had moved toward the number signed by the last review before renewal renew and expand at the same rate as accounts where it had not, with outside exits held out by a rule fixed before the outcome. Where no outcome measure was signed or no review is held, as on a plug-in purchase, use of the steps that carry the value stands in, read before the renewal decision.

**Claim 11. Lock-in earned by building something together holds. Lock-in made by control is hold-up.** Hold-up is one side squeezing the other once it cannot leave (Klein, Crawford and Alchian 1978). A buyer that has built workflows with a seller stays because what they built is worth more here than anywhere else. It also stays because the seller already knows its environment and a challenger would have to learn it, which holds only while the seller keeps that knowledge current. A buyer kept by restricted access to its own data, or by terms that make leaving costly, stays until a rule or a rival removes the restriction. A buyer that sees lock-in coming prices it before it signs, so what holds a buyer at renewal costs the seller at signature. Control has a limit too. The buyer can build the function itself, building gets cheaper as patterns standardize, and a seller that takes more than building would cost teaches the buyer to build.

The exposure follows the investment, buyer or seller. Whoever built more of what cannot be reused elsewhere has more to lose. A connector the seller ships to every later customer is not exposed, and a mapping to one hospital's schema is. [incomplete-contracts.md](../02-research/incomplete-contracts.md) and [transaction-cost-economics.md](../02-research/transaction-cost-economics.md) carry the evidence.

*Fails if*, after a rule opens access that sellers had restricted, sellers whose buyers built workflows with them lose buyers as fast as sellers whose retention rested on the restriction.

**Claim 12. Where both sides build something specific, a contract built for partnership does what a discount cannot.** No contract foresees everything, and proof before signature shows what a seller can do without binding what either side does once the other cannot easily leave. So before either side builds, the two settle who carries which risk, in stages, with a point at each stage where either can stop at a known price. The stages run in both directions: the buyer's payments follow proof, and the seller's engineering follows a commitment from the buyer. They also sign one outcome measure, a number in the buyer's own terms, and agree a standing review for what nobody can foresee. A plan of that kind gives both sides something to lose by walking away, and a discount changes the price once. The plan rests on a renewal that either side can decline. A built-in purchase that happens once has none, so the seller finds a structure that recurs, or the safeguard comes from outside the pair as fixed scope, acceptance a third party judges, or escrow. Contract terms are one layer beside trust and the norms of the relationship, and the layers mostly work together (Poppo and Zenger 2002). None of this belongs on a plug-in purchase. The [Enforcement Ledger](../../practice/enforcement-ledger.md) builds the plan.

*Fails if* built-in deals whose staged plan and stop points were agreed before anything was built keep no more revenue at renewal than matched built-in deals without one. The comparison keeps each deal in the arm it was agreed into.

---

## Part II: Reading a stall

Ask in order, because each question assumes the one before it.

1. **Does the buyer pay for the problem today?** Staff time on a workaround, an incumbent tool or a consultant shows the change is worth something to it. Count spend on the problem under any name, so a category nobody has named still passes where buyers pay for a workaround. Without that, no cost reading applies, and teaching does not supply it, by the second standing assumption. A buyer with no people free differs from a purchase with no priority. The test is the seller taking the named work off the buyer. A buyer with no people free then commits a date or a sponsor's time, and a purchase with no priority gets neither. The [Market Reading](../../practice/00-market-reading.md) and the [Deal Triage Calculator](../../practice/deal-triage-calculator.md) ask it first, and the reading is untested ([07-open-questions.md](./07-open-questions.md) item 66).
2. **Time0. Which cost is in the way in this market, and is the seller built for it?** Claims 1 to 5.
3. **Time1. Is the purchase plug-in or built-in, has the organization's scrutiny been invited, and is the seller's spending showing the buyer what it will face?** Claims 6 to 9.
4. **Time2. Did it work here, and what did the two sides settle before they built?** Claims 10 to 12.

**Failure modes, one per claim.**

| Claim | Failure | Signal |
|---|---|---|
| 1 | Imitation | A motion copied from another market, and an organization built to carry a cost its buyers do not have |
| 2 | Unread market | The playbook chosen before anyone read the workflow or the buyer's organization |
| 3 | Cheap talk | Claims any seller could make, and more of them sent |
| 4 | Floor worked as a sales problem | Deal effort spent on a cost that no single deal lowers |
| 5 | Paid for the wrong work | Bookings pay where implementation is the cost, or pay tied to an outcome the representative cannot affect |
| 6 | Over-built or under-built | Workshops and joint plans on a plug-in purchase, or a trial offered on a built-in one |
| 7 | Sold to one person | A champion convinced and an organization never asked |
| 8 | Spent as a discount | A price cut where the buyer's fear was the obstacle |
| 9 | Deferred work | Discovery skipped to close, and the delivery team paying for it |
| 10 | Unreviewed | The renewal is the first time anyone reads whether it worked |
| 11 | Control mistaken for a moat | Retention resting on what the buyer cannot take with it |
| 12 | Unallocated | Something specific built with no stages or stop points agreed |

A stall that matches none of these means the table is incomplete, which is worth recording in [07-open-questions.md](./07-open-questions.md).

---

## Version History

**Current version: 7.0.** The framework's version tracks this document's, and the root README footer must agree, which `check_frontmatter.py` enforces.

<!-- vale TCG.RetiredTerms = NO -->
| Version | Date | Change |
|---|---|---|
| 7.0 | 2026-11 | Rewritten around twelve claims the author holds, at three times with both parties at each: Time0 the market, Time1 contracting, Time2 renewal. Earlier versions called the deal "time 0" and the relationship "time 1". Each cost gains a home time. Conditions run forward and expectations run backward. Plug-in and built-in name the two kinds of purchase. Pay follows the cost in the way. Retired: positions, the two thresholds per cost, the gate, the two conditions as equations in this document, the three-way split of value, drift rates, the bond condition, the governance forms as a table, and all but one failure mode per claim. The trim proposal records the reasoning (`git show 59ab41e:TRIM-PROPOSAL.md`), and 6.4 is in git history. Amended on 2026-11-10, when the seller surplus model, the governance forms and the derivation file were folded in: claims 3, 5, 7, 9, 11 and 12 each gained the sentences from those files that the claim needs. Amended on 2026-11-11: the tests of claims 1 and 2 were restated around where buyers stop, claim 2's text and table gained the place where more buyers stop under each reading, *built for* was defined, and Part II's first question gained the two statements open question 66 owed. The tests of claims 7, 8 and 10 were restated the same day. Claim 7 now tests what a role's objection is about and counts the deals that die under scrutiny. Claim 8 tests a discount against the buyer's approval thresholds, and drops the test on renewal after a discount. Claim 10 reads the signed outcome measure where it read the implementation plan. The premise gained four statements on how the costs relate: fit in the buyer's own environment is implementation, implementation has three parts and is wider than a transaction cost, consensus is who must agree and implementation is what must work, and the work runs in the order of the home times. Claim 4 gained one definition of a floor, which no single deal lowers and which falls for every seller or for one seller's deals. The premise gained a rule that forbids as the one wall, and outside funding as a reason a market looks easier to sell into than it is. A second review the same day found contradictions in the new wording, and they were fixed. The premise now says both fears reach the deal before signature as a role that will not agree, so implementation acts as consensus at Time1. Claim 8's first test compares a discount that crosses no approval threshold with no offer. Claim 12 states the outcome measure that claim 10's test reads. Claim 4 says buyers stop at a floor where no seller has paid it. Claim 10's test reads use before the renewal decision where no outcome measure was signed or no review is held. |
| 6.4 | 2026-11 | The research review's fourth response. Exposure sets what a failure costs and makes leaving costly, so a buyer's failing fit shows as stalled use and contraction before churn. Hold-up grows once one side's exposure outgrows the other's stake. Outside exits are out of scope, contracts are one layer beside trust and norms, and maintenance goes where it moves an account most. Two falsifiers restated, open questions 62 to 65 filed. Amended on 2026-11-09 for the review's fifth and sixth responses: default edges frozen for tests that read them, Coase credited with the cost of using the market and the participation question with Akerlof and search theory, and Attewell, Walton and McKersie, Bagwell, Hauser and Wernerfelt, and Dixon and McKenna credited. |
| 6.3 | 2026-11 | The research review's third response. The tightest cost is where the sale starts and names the motion. Which cost the seller works first is a separate rule, with the tightest first as its default special case, and Axiom II's first falsifier tests the rule's unit-cost term. Persuasion costs the joint condition what it spends, and price cancels in each deal but changes which deals occur. Open question 61 is filed. |
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
- [06-calibration.md](./06-calibration.md)
- [07-open-questions.md](./07-open-questions.md)

**Academic backing:** [00-reading-guide.md](../02-research/00-reading-guide.md) maps each research file to what it backs.

**Field operationalization:**
- Time0, reading a market → [00-market-reading.md](../../practice/00-market-reading.md)
- Time1, reading a deal → [deal-triage-calculator.md](../../practice/deal-triage-calculator.md), [bargaining-ledger.md](../../practice/bargaining-ledger.md), [enforcement-ledger.md](../../practice/enforcement-ledger.md)
- Time2, the handoff, the review and renewal → [adoption-review.md](../../practice/adoption-review.md)
