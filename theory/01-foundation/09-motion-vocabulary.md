---
title: "Motion Vocabulary"
layer: theory
status: active
version: 1.1
operationalizes: [axiom-1]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# Motion Vocabulary

**Version:** 1.1
**Purpose:** To map this framework's motion names onto the vocabulary the industry already uses, and to say precisely where the older terms mislead. Everyone arriving here knows what Product-Led Growth means. Nobody should have to guess whether it means the same thing as Turnkey.

> [!NOTE]
> **This is a translation reference, not a derivation.** Nothing here is used to decide anything. [01-motion-taxonomy.md](./01-motion-taxonomy.md) is the taxonomy and this file exists so that a reader holding the incumbent vocabulary can find their way into it.

---

<!-- vale TCG.RetiredTerms = NO -->
<!--
  The retired-term rule is off for the rest of this file. Naming retired terms
  is what this document is for, so the rule would fire on every row of every
  map below and the fix would be to stop doing the job. The trade is that a
  genuinely stale term here goes uncaught, which is accepted because this file
  is the one place in the repository where an old name is the subject rather
  than a mistake. Every other file keeps the rule on.
-->

## 1. Why the incumbent names do not form a set

Product-Led Growth, Sales-Led Growth and Implementation-Led Growth are named on three different axes. That is the whole problem, and it is why the set feels incomplete without ever being obviously wrong.

| Term | Named after | The axis |
|---|---|---|
| Product-Led Growth | the product doing the selling | the **instrument** |
| Sales-Led Growth | salespeople doing the selling | the **actor** |
| Implementation-Led Growth | implementation cost | the **cost component** |

Only the third names a cost. Which means the obvious extensions, Search-Led Growth and Consensus-Led Growth, have no natural place in that list: they would be named on an axis that only one of the three existing members uses.

This framework names every motion after the cost it spends to reduce, because that is what the theory says a motion is. The set then closes: three costs, three motions, plus one reading for the case where no cost is large enough to warrant instruments.

---

## 2. The map

| This framework | Closest incumbent term | Relationship |
|---|---|---|
| **Turnkey** | Product-Led Growth | Overlapping, not equal. See section 3. |
| **Search-led** | Sales-Led Growth, category creation, evangelical selling | Search-led is wider. It also covers channel and trial, which Sales-Led does not. |
| **Consensus-led** | No established term. Closest neighbours are MEDDPICC-style qualification and "multithreading" | The incumbent practice exists as qualification discipline rather than as a named motion. |
| **Implementation-led** | Implementation-Led Growth, forward-deployed engineering, solution selling | Direct. This framework was called ILG before the theory outgrew the name. |
| **Composed** | No established term | The industry treats motions as exclusive, so the case where two costs are comparable has no name. |

---

## 3. Turnkey is not Product-Led Growth, and the conflation costs something

This is the most common confusion and it is worth being exact about.

**Turnkey is a reading on one deal.** It says this deal's friction vector is short: no component is large enough to repay instruments built to reduce it. It is a measurement, it applies to a single opportunity, and the same company can have Turnkey deals and Structural deals in the same quarter.

**Product-Led Growth is a company-level strategy.** It says the product is the primary acquisition instrument. It describes how a business is built rather than what one deal costs.

They coincide often enough to be confused, because a business built on self-service tends to attract short-vector deals. They come apart in the case that matters most.

**A Product-Led company moving upmarket is running Structural deals.** Security review arrives, the buying committee grows, integration depth increases, and the level crosses the boundary. The deals are Structural and the company still calls its motion Product-Led, because that is the company's identity. So the enterprise deals get worked with instruments built for short vectors, plus whatever the first enterprise rep improvises.

That pattern is usually diagnosed as "we need to build an enterprise motion." Under this framework it has a sharper description: **the deals rotated into a different region and the instrument set did not follow.** Calling the company Product-Led is accurate and calling those deals Turnkey is not, and the single word doing both jobs is what hides the gap.

Keeping the level as a per-deal reading is what makes the transition visible while it is happening rather than after churn reports it.

---

## 4. Product-Led and Sales-Led are instruments for the same cost

This one is counterintuitive and it falls directly out of the decomposition.

The search component's three blockers are specified in [01-motion-taxonomy.md](./01-motion-taxonomy.md) section 2, and the mapping onto the incumbent vocabulary is what matters here. *Category Unnamed* is what the industry calls Sales-Led or evangelical selling. *Fit Unverified* is what it calls Product-Led. *Vendor Unreachable* is usually called channel strategy and is rarely treated as a motion at all.

**So the industry treats Product-Led and Sales-Led as opposites, and they are instruments for the same component.** One resolves a buyer who does not know the category exists. The other resolves a buyer who knows the category and cannot verify this particular fit. Both are spending against search, at different points inside it.

What separates them in practice is level rather than kind. A trial cannot resolve a six-month integration question, so self-service works where the other two components are also small. Education can run at any level, which is why it survives upmarket and trials often do not.

Treating them as rival philosophies produces an argument that cannot resolve, because the two sides are describing different blockers inside one cost and each is right about their own.

---

## 5. What this framework is not competing with

Go-to-market vocabulary mixes three tiers of thing, and confusing them produces arguments that go nowhere.

| Tier | What it decides | Examples |
|---|---|---|
| **Theory of transaction cost** | Which costs a deal carries, and therefore which instruments can reduce them | This framework |
| **Qualification framework** | Deal inspection, pipeline hygiene, forecasting. What must be true before a deal is called committed | MEDDPICC, BANT |
| **Conversational methodology** | Rep dialogue, discovery technique, how a perspective gets reframed in the room | Challenger, SPIN |

**The tiers compose.** A team using this framework still needs a qualification standard, and MEDDPICC works as well inside an implementation-led motion as inside any other. What changes is what the qualification evidence *is*: the economic buyer is confirmed in the Blueprint, the decision criteria are the Red Team's surfaced failure modes, and the champion is tested by whether they commit resources to the MIP.

A rep still needs conversational technique, and commercial teaching suits the Blueprint interview well.

The distinction matters most when someone says their team already does this because they run MEDDPICC on complex deals. Qualification tells you whether a deal is real. It does not tell you which of three costs is blocking it, and it does not reduce any of them.

---

## 6. On dropping the acronyms

This framework uses "search-led", "consensus-led" and "implementation-led" rather than three-letter forms, for three reasons worth stating once.

**SLG would collide.** Search-Led Growth abbreviates to the same three letters as Sales-Led Growth while meaning something wider. A term that silently means two things in one conversation is worse than an unfamiliar term.

**The field is already crowded with them.** Adding three more is the kind of move the [voice guide](../../publishing/02-tools/voice-guide.md) exists to prevent.

**The names match the instrument's output.** The [Deal Triage Calculator](../../practice/deal-triage-calculator.md) emits `search-dominant`, `consensus-dominant` or `implementation-dominant`. When the motion name is the same word as the reading, nothing has to be translated, and translation layers are where field errors accumulate.

"Implementation-Led Growth" and "ILG" still appear in analyses written before the rename. They named this framework and then named one motion inside it, which is the ambiguity the rename resolved.

---

<!-- vale TCG.RetiredTerms = YES -->

## Related

- [01-motion-taxonomy.md](./01-motion-taxonomy.md) — The taxonomy itself, and what each motion contains.
- [06-friction-vector.md](./06-friction-vector.md) — Why a motion is a region rather than a label, and the three search blockers section 4 depends on.
- [04-glossary-and-notation.md](./04-glossary-and-notation.md) — Canonical definitions for every term used here.
- [channel-collapse.md](../02-research/channel-collapse.md) — The reachability blocker, which most frameworks do not name as a cost.
