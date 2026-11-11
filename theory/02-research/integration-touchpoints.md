---
title: "Integration Touchpoints"
layer: theory
status: active
operationalizes: [axiom-1, axiom-2, axiom-3]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# Integration Touchpoints

**Sources:**
- Keeler, B. "The Integration Illusion: Why Connecting to EHRs Is About Value, Not Standards." HTD Health. Practitioner source. The taxonomy below is his. URL to be added.
- Keeler, B. "How to Win Friends and Integrate Systems." *Health API Guy.* [Link](https://healthapiguy.substack.com/i/69081661/what-does-your-user-need). Source of the claim that workflow drives dataflow.
- Keeler, B. "The Only Three Ways to Integrate." *Health API Guy.* [Link](https://healthapiguy.substack.com/p/the-only-three-ways-to-integrate). Source of the claim that almost any workflow is technically reachable, so the binding constraint is value rather than access.

**Abstract.** A product that attaches to a buyer's system of record meets it at a small number of points, and the points come in types. Keeler's argument, made about electronic health records, is that the questions sellers ask first, which standard and whether to build or buy, are downstream of a question they skip: which workflow the product changes, and therefore which touchpoints it needs. Three types are core. *Enrollment* is how an entity enters the product's scope. *Supplementation* is what the product reads about it. *Writeback* is what the product writes back to close the loop. Two more are usually phased in later: *foundational synchronization*, the reference data the two systems must agree on, and *shared context*, how identity and session are shared. The smallest set of touchpoints that lets a buyer verify value is the minimum viable integration, and it goes live first. Integration depth then follows value. A buyer invests in deeper touchpoints in proportion to what the product is worth to them, and a product with a light value proposition gets a shallow integration and a low place on the priority list, whatever the standard.

**The types are general.** The vocabulary is healthcare's and the structure is not. Any product that attaches to a system of record has the same five kinds of touchpoint, and the framework states them as its own with Keeler as the source of the taxonomy.

| Type | Question it answers | On an electronic health record | On an enterprise resource planning system | On a customer relationship management system |
|---|---|---|---|---|
| **Enrollment** | What brings an entity into the product's scope | Scheduled visits in a department, an order for a procedure | Invoices over a threshold, a new vendor | Leads meeting a rule, opportunities at a stage |
| **Supplementation** | What the product reads about it | Medications, allergies, results | Cost centers, payment terms, vendor master | Contacts, account history, activity |
| **Writeback** | What the product writes back | A note, a result, a rescheduled visit | A posted journal entry, an approval | Call notes, a stage change, a task |
| **Foundational synchronization** | What reference data must agree | Provider and location lists | Chart of accounts | Picklists, the user list |
| **Shared context** | How identity and session are shared | The clinician's login and active patient | Single sign-on into the ledger | Embedded in the record view |

What is healthcare-specific is the weight on each type. Writeback into a chart carries a legal record's governance and brings clinical informatics to the table, and foundational data in healthcare is unusually fragmented. Those are facts about decision roles and divergence in one market, and they are what the [Market Reading](../../practice/00-market-reading.md) counts per type. The taxonomy is general and the distribution is local.

**Key claims:**
- The standards question is downstream of the workflow question. Which standard to use and whether to build or buy cannot be answered until the product's workflow, and so its touchpoints, are named.
- Almost any workflow is technically reachable by some route, so the common cause of a failed integration sale is a light value proposition rather than blocked access.
- Integration depth follows value. Buyers invest in deeper touchpoints in proportion to what the product is worth to them.
- Three touchpoint types are core and two are usually phased in later.
- The minimum viable integration is the smallest touchpoint set that lets the buyer verify value, and building only it reduces rework and lets later touchpoints be validated by customer need.
- Applications that are live with integration stay live at a higher rate.
- A product with no confident answer to what differentiated value it delivers should validate without integration rather than carry the debt of unused touchpoints.

**Supports in TCG:**
- **Definitions, workflow.** A product is an encoded reference workflow. The touchpoint list is the part of that workflow that meets the buyer's system, and "workflow drives dataflow" is the same claim stated from the integration side. A product that cannot name its touchpoints has not named its workflow, and has nothing to read a buyer's workflow against.
- **Claim 2.** Touchpoints are how entangled a workflow is, in countable form. The decision roles follow the type: whoever owns the record polices writeback, whoever owns the operation polices enrollment, whoever owns master data polices synchronization, and security polices shared context. So the roles a workflow brings can be partly derived from its touchpoint types before any buyer is met, which is what row O1 of the [Market Reading](../../practice/00-market-reading.md) needs.
- **Claim 6.** A touchpoint built for one buyer is worth less anywhere else, so a purchase that needs one is built-in. A connector the seller reuses across customers is not, by claim 11. "Integration depth follows value" is the buyer's side of it: a buyer builds in proportion to what the product is worth to it.
- **Claims 9 and 12.** The minimum viable integration is the first stage of a staged plan. It is the smallest touchpoint set that lets the buyer check the value, and the two later types arrive as later stages.
- **Claim 11.** That integrated applications stay live at a higher rate is consistent with lock-in earned by building together. Persistence alone cannot tell that from lock-in made by control, and Keeler gives no figure.
- **Enforcement Ledger.** The reference workflow's touchpoints are the ledger's rows, and the Map column fills per typed touchpoint.
- **Reading an adjacent market.** Two workflows share a step only if the steps are typed the same way. Touchpoint types are that typing, and they are what lets an adjacent market inherit rows of the Market Reading by count and not by judgment.

**Status.** The taxonomy is a practitioner's own, and it is recorded as such. The generalization beyond healthcare is the framework's claim, shown on three systems of record and tested on none.
