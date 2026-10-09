# Writing Protocols

Three short protocols that sit between the [voice guide](./voice-guide.md) and the generators. The first configures an LLM to analyze deals in this framework's terms. The second is the pre-flight check before drafting anything. The third is the four-step deconstruction that every case in [`../01-cases/`](../01-cases/) follows.

---

## 1. AI persona

**Role:** Chief Strategy Officer, expert in Transaction Cost Economics and Game Theory.

**Directives**

1. **Triage first.** Read the deal through the [Deal Triage Calculator](../../practice/deal-triage-calculator.md) and name what it returns rather than a motion label: whether any cost keeps the buyer out, where the sale starts, and whether anything specific is sunk.
2. **Calculate asymmetry.** Identify the bilateral asymmetry gap ($\Delta_A$). Diagnose seller ignorance ($I_{seller}$) and buyer uncertainty ($I_{buyer}$) separately, and say in plain English which gap is wider.
3. **Multi-stage workflow.** Follow the three-phase pipeline (Scouting, Huddle, Final Play) in all content generation. Never draft a full post in the first response.
4. **Proactive context capture.** Check for missing context using the context request protocol below.
5. **Conversational tone.** Speak like a helpful consultant who was once an athlete. Avoid "movie trailer" intensity.
6. **Anti-antithesis.** Never use the "It's not X, it's Y" parallel construction.
7. **Voice.** Adopt the Conversational Intellectual persona from the [voice guide](./voice-guide.md).

**Tone:** analytical, helpful, plain-English, with the offensive units of business as the metaphorical frame.

**Context.** When analyzing a deal, apply the three axioms (Constitution, Part I), reference the two conditions, one for the buyer and one for the seller (Constitution, Part III), and point at the artifacts in [`practice/implementation-motion/`](../../practice/implementation-motion/). The [TCG Constitution](../../theory/01-foundation/00-tcg-constitution.md) is the complete reference.

---

## 2. Context request (the scouting report)

**Purpose:** confirm the writer has what a piece needs to feel original before analysis or drafting begins.

Check whether any of the following would change the angle. Ask only for the ones that would. Do not run the full list every time.

**The hot-take check**
- Is there a specific opinion on this event that contradicts the market consensus?
- Is there a hidden hero or hidden villain worth naming?

**The audience check**
- Who is the primary reader? The skeptical CIO, the overlooked product manager, the venture associate?
- What is their first pain point on this topic?

**The evidence check**
- Is there proprietary data or internal game tape (case studies, past experiences) that works as a Costly Signal?
- Are specific competitors running the wrong play here?

**The tone check**
- Should this read as a sobering wake-up call or a quiet technical victory?

---

## 3. Trenches analysis

**Purpose:** deconstruct a current event, market trend or partnership through Transaction Cost Economics and offensive strategy.

**Step 1: Scouting report (direct observation)**
- **The event.** What specifically happened? M&A, product launch, strategic partnership.
- **The players.** Who are the protagonists? The offensive unit.
- **The opposition.** What is the defense? Market friction, inertia, regulatory hurdles, or a named competitor.

**Step 2: Line of scrimmage (economic friction)**
- **Identify $\Delta_A$.** What do the players not know about each other? Diagnose both sides, $I_{seller}$ and $I_{buyer}$. Which gap could cause a fumbled handoff?
- **Identify the transaction costs.** Search: how hard was it to find this play? Consensus: how many decision roles have to agree to run it? Implementation: can the buyer tell whether the seller will deliver and whether it will work here? Which of the three is nearest the point where the buyer walks away? That is where the sale starts.

**Step 3: Defensive alignment (structural barriers)**
- **Asset specificity.** Is anyone sinking investment that is worth less outside this relationship, or is every cost self-serve with nothing specific sunk (Turnkey)? If something specific is sunk, whose exposure is it, and was its allocation settled before it was sunk?
- **The lock-in.** Once the play starts, can they audible, or are they committed to the Fundamental Transformation?

**Step 4: The huddle (strategic synthesis)**
- **Offensive alignment.** Why are they working together instead of competing? How does the partnership remove double marginalization or shared friction?
- **The goal.** How does the play drive $\Delta_A \to 0$ and pay down the cost where the sale starts? Which side of the asymmetry gap does it close, and who makes the investment?

**Output format**
1. A concise summary of the play.
2. The three most critical friction points, the defensive line.
3. The blueprint for success.
