---
title: "The Bargaining Ledger"
layer: practice
status: active
version: 1.0
operationalizes: [axiom-1, axiom-2, axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# The Bargaining Ledger

Version: 1.0
Goal: On one deal, close the bargaining gap one decision role at a time, and settle an arrangement that holds each exposed role once the investment is sunk. The ledger is two documents: a **private decision-role map**, filled one to one and never shared, and a **shared arrangement record**, which lists terms and names no role. Where the sale starts at bargaining, it adds a safeguard inside the buyer, because no contract between the two firms binds the role whose budget the change cuts.

**Canonical reference:** [Constitution 6.1](../theory/01-foundation/00-tcg-constitution.md). Axiom III's bargaining row: map who loses what, one role at a time, and collect objections apart before any room convenes. Axiom I for the count and the spend thresholds that add approvers. The derivation is [08-from-axioms-to-instruments.md](../theory/01-foundation/08-from-axioms-to-instruments.md) sections 2.2, 4 and 5, the safeguard is [05-governance-forms.md](../theory/01-foundation/05-governance-forms.md) section 2, and the functional forms are [02-mathematical-models.md](../theory/01-foundation/02-mathematical-models.md) section 3.

| | |
|---|---|
| **Inputs** | A [Deal Triage Calculator](./deal-triage-calculator.md) reading. The [Enforcement Ledger](./enforcement-ledger.md)'s rows, where the deal has specific exposure. |
| **Outputs** | The decision-role map, the bargaining gap, the size of the bargaining cost and its band, the arrangement record, and the safeguard inside the buyer where one is needed. |
| **Next step** | The arrangement's terms go into the Enforcement Ledger's Stage column or the contract. The map is re-read in the [Sustaining Adoption Review](./adoption-review.md). |
| **Owner** | The account executive, staked on retention as [05-governance-forms.md](../theory/01-foundation/05-governance-forms.md) section 5 derives, or a reviewer who is. The map stays with the seller's account team. |

> [!IMPORTANT]
> **Two documents, never merged.** An occupant will state a reservation one to one and will not write it where a peer can find it, and a probe of private vulnerability reads as opportunism however it is framed ([buying-center-dynamics.md](../theory/02-research/buying-center-dynamics.md)). So the map is private, and the shared record lists terms without saying whom they answer. An occupant's uncertainty about their own outcome closes when they receive the answer, not when they state the concern.

**When to run it.** Whenever the triage reads the bargaining position as needing investment, and on every deal with specific exposure.

---

## The rows: decision roles

A row is a decision role, a position defined by its relation to the workflow and not by its occupant: who runs a step, owns it, pays for it, or polices it. Count the role that can stop the deal even if its occupant never attends a meeting. Security and data protection are the roles most often missed.

**Build the list from three sources.**

1. **The steps.** For each row of the Enforcement Ledger, the roles that run, own, pay for and police it. The touchpoint type predicts who polices it: writeback brings whoever owns the record and whoever polices it, enrollment brings whoever owns the operation, foundational sync brings whoever owns master data, and shared context brings security. Add whoever pays.
2. **The impositions.** Each divergent step that forces a practice on whoever runs it adds that role, because it objects. A divergence the buyer accepts or works around adds exposure and no veto.
3. **The buyer's rules.** The formal bodies its rules require at this deal's size and exposure: procurement above a spend threshold, security review above a data class, legal, a board above a commitment. Each counts through its occupant, the analyst or manager who runs it, with its lead time recorded. Record each threshold. Splitting or ramping a deal under one removes the body's veto and leaves the exposure behind it, so the role stays a row with its reservation open.

**Read it after exposure, and again.** Each role added brings requirements, and a requirement the product does not meet is a new divergent row in the Enforcement Ledger, which may impose on a further role. Repeat until a pass adds no role ([02-mathematical-models.md](../theory/01-foundation/02-mathematical-models.md) section 3.5).

---

## The decision-role map (private)

| Column | Filled with |
|---|---|
| Role | The position, and the steps it runs, owns, pays for or polices |
| Occupant | Who holds it now |
| Reached by | Directly, or through the champion |
| Measured on | What the occupant's own review measures: the budget, headcount, metric or control the change touches |
| Reservation | What the occupant says, one to one, the change does to that, or their confirmation that it costs them nothing |
| Direction | Gains, no effect, or loses, read from the measure and checked against the reservation: +1, 0 or −1. Where the two disagree, record both. |
| Answer | The term that answers the reservation, the date the occupant received it, and their response in their own words |
| Bond | Whether what the role gains, staged with adoption, covers what it loses |
| Mandate | Whether the sponsorship and capital behind the role still stand |
| Re-statement | The new occupant's reservation, at each occupant change |

**One to one, and never in a room.** Before any group session, collect each role's objections apart, in writing. Ask what the occupant is measured on and what the change does to it, and let them state the reservation.

**The champion.** Name the occupant who gets the seller to each role and tells it what the room will not. A role reached only through the champion is mapped second-hand, and its gap stays open until its own occupant states.

**Record a reservation and its answer, never a verdict on the person.** An occupant whose direction reads −1 is optimizing a measure the seller has not yet answered. A role whose mandate dissolves is a different event from an occupant change: the first changes the coalition, the second reopens what the new occupant cannot verify.

---

## The bargaining gap

$$\hat{\Delta}_{consensus} = 1 - \frac{\text{roles whose occupant has stated their exposure and received the answer}}{\text{roles that can say no}}$$

A role counts as closed when its occupant has stated one to one and has received either a term that answers them or the written decision that their reservation will not be answered. A confirmation that the change costs them nothing counts as a statement only where their measure agrees. The gap feeds each party's chance of future loss ([02-mathematical-models.md](../theory/01-foundation/02-mathematical-models.md) section 2.4). It is a different quantity from the variance below, which is how far apart the roles' interests actually sit.

---

## The size of the cost, and what it calls for

$$F_{consensus} = \alpha \cdot N^{\beta} \cdot (1 + \text{Var}) \cdot (1 + \gamma \cdot TO)$$

$N$ is the roles that can say no. Var is the variance of the Direction column across them, read from the measure. Where no role reads −1, compute it as though one more unstated role read −1, because the casualty has not been met. $TO$, from 1 to 5, scores how far the technical evaluators diverge on architecture: 1 is shared standards, 3 is disagreement on integration pattern or hosting, 5 is a split philosophy such as cloud against strict on-premises. It is the one ordinal rating left in the field instruments, so read it as a rank. [06-calibration.md](../theory/01-foundation/06-calibration.md) declares $\alpha$, $\beta$, $\gamma$ and the band edges as chosen.

| $F_{consensus}$ | Reading | What it calls for |
|---|---|---|
| **Under 10** | Low | One champion can carry it. Fill the map for every role with a veto anyway. |
| **10 to 25** | Medium | The deal drifts rather than dies. Agree written decision criteria and a decision sequence before pricing. |
| **Above 25** | High | No decision is the likely outcome, not a competitive loss. Add the safeguard inside the buyer before any specific investment. |

**Lower the variance, not the headcount.** The return on reducing it scales with $N^{\beta}$. Answering a reservation in the arrangement lowers it, and more meetings do not.

---

## The arrangement record (shared)

| Column | Filled with |
|---|---|
| Term | What changed in the plan, the scope, the sequence, or the commercial terms |
| Owners | One on each side |
| Signed in | The contract or Stage row that carries it |

**The record names no role.** Which role a term answers lives only in the private map, so a term such as a headcount commitment does not tell the committee whose reservation it was.

**What a term may be.** It changes the plan, the scope or the sequence, or moves money between the two firms in the contract the buyer's procurement signs. It never pays a role or its budget outside that contract, which would buy an agent's assent around its principal. A reservation the role's measure does not show is recorded and not answered, or every occupant gains by stating one.

**Done when** every reservation in the map has an answer or a written decision not to answer it, and every term is signed where it binds.

---

## The safeguard inside the buyer

A Mutual Implementation Plan binds the buyer that signs it, not the role whose budget the change cuts. So where the sale starts at bargaining, or the size reads High, the deal needs a safeguard inside the buyer ([05-governance-forms.md](../theory/01-foundation/05-governance-forms.md) section 2):

- **A staked sponsor:** an executive whose own measure rides on the initiative.
- **A bonded arrangement:** every role whose direction reads −1 holds terms under which what it gains, staged with adoption, covers what it loses, so defecting after the investment is sunk costs it something. Consent records agreement, and the staging is the bond. Where no term can answer a role, the safeguard closes only on a written overrule from whoever holds authority over that role, and the role stays an open exposure in the buyer's chance of loss.
- **Commitments written against roles, not people,** so a successor inherits each term and states again.

**Maintain it.** Re-read the map at every occupant change, reorganization and budget cycle. A departed champion reopens the bargaining gap all at once, and no technical proof reaches it.

---

## Scoring sheet

| Field | Value |
|---|---|
| Roles that can say no, by source: steps, impositions, the buyer's rules, with each body's lead time | |
| Spend thresholds, and any deal structured under one | |
| The champion, and roles reached only through them | |
| Roles closed, of roles | |
| $\hat{\Delta}_{consensus}$ | |
| Directions: gains, no effect, loses, and where measure and statement disagree. Var | |
| $TO$, and $F_{consensus}$ with its band | |
| Reservations answered, declined, open | |
| Terms signed, of terms | |
| Safeguard: sponsor named, −1 roles bonded or overruled, commitments written against roles | |
| Mandate standing (yes / no) | |
| Date, and by whom | |

---

## Related

- **Theory:** [Constitution](../theory/01-foundation/00-tcg-constitution.md), Axioms I and III. [05-governance-forms.md](../theory/01-foundation/05-governance-forms.md) sections 2 and 5.
- **Derivation:** [08-from-axioms-to-instruments.md](../theory/01-foundation/08-from-axioms-to-instruments.md) sections 2.2, 4 and 5.
- **Functional forms:** [02-mathematical-models.md](../theory/01-foundation/02-mathematical-models.md) sections 2.4 and 3.
- **Research:** [buying-center-dynamics.md](../theory/02-research/buying-center-dynamics.md), [tce-empirical-record.md](../theory/02-research/tce-empirical-record.md).
- **Beside it:** the [Enforcement Ledger](./enforcement-ledger.md), whose rows seed this one, and the [Deal Triage Calculator](./deal-triage-calculator.md).
