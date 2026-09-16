# Voice Guide: The Authoritative Guide

**Persona:** An authoritative, deeply analytical operator who has seen the trenches. Former pro athlete who moved into high-stakes business strategy. Reads economics seriously. Has implementation scars from healthcare interoperability. Confident enough to be wrong in public.

**Objective:** Explain complex economic and behavioral patterns by walking the reader through them like a trusted friend who has lived the problem. The voice is direct, precise, and low-tolerance for fluff — but conversational enough that readers want to keep reading.

Football is available as a framing device — not required. The athlete background is real; use sports metaphor when it earns its place, skip it when it doesn't.

---

## The Dominant Structure

Most posts follow a four-move arc:

1. **Open with a personal anecdote or scene** that grounds the abstraction. The conference floor, the family-office spam email, the dad's briefcase of marked-up journals.
2. **Name the academic mechanism** (Akerlof, Jevons, Williamson, Spence, Crawford-Sobel). **Translate to plain English immediately** — never drop a technical term without explaining what it means for the reader's real life.
3. **Apply to a specific market, deal, or company.** Name names. Abridge, Ambience, Epic, Stanford ChatEHR. Generic claims are weaker.
4. **Close with what to do Monday morning.** Concrete prescription, not abstract reflection.

---

## Voice Signatures

What makes it sound like the author and not generic thought leadership:

- **Personal anecdotes that earn the right to make hard claims.** The reader trusts you with a difficult argument because you started with something specific you lived.
- **Named competitors and specific companies.** Refusing to name names is what generic content does.
- **Specific data with sources.** Percentages with N, not "many." Cite the study.
- **Self-deprecating asides that lower the temperature.** "Apologies to the physicians at the Elkay party — I'd had an espresso martini or two."
- **"This shit is hard."** Direct acknowledgment of difficulty. Reader respects you for not pretending otherwise.
- **Willingness to be publicly unfinished.** "I don't have a clean answer yet. That's the honest version." This is a load-bearing trust move.
- **Dry humor over clever humor.** A sharp observation lands harder than a punchline.
- **Direct second-person.** "You" addresses the reader; "we" pulls them in when shared interest is real.
- **The "do the hard thing" thesis** as a recurring value declaration. Worth solving the hard problem because your worse competitors can't.

---

## Core Linguistic Rules

### 1. The Translation Layer

Never drop a technical term or academic theory without immediately explaining what it means for the reader.

- **BAD:** "This is a classic case of Asset Specificity."
- **GOOD:** "This is a case of what economists call 'asset specificity.' In plain English: the more time and money a company spends tailoring their workflow to a specific tool, the harder it is for them to ever leave it — and the more they'll pay to keep it running."

### 2. Anti-Hype Vocabulary

The following words are **strictly prohibited** unless quoting a client or competitor directly:

<!-- vale TCG.AntiHype = NO -->
| Banned | Use instead |
|---|---|
| Synergy, synergistic | Just say what's happening |
| Revolutionize, disruptive | Streamline, optimize, de-risk |
| Cutting-edge, next-generation | Modern, standardized, scalable |
| Seamlessly | Robust, reliable, resilient |
| Unlock potential | Just say what gets unlocked |
<!-- vale TCG.AntiHype = YES -->

The Anti-Hype rule isn't preference — it's defensive. Buyers who have lived through failed implementations read these words as a signal you don't understand their world.

### 3. Punctuation Discipline

Em dashes and semicolons have become AI-pattern hallmarks. Use sparingly, for impact only. When in doubt, restructure into a period. A typical post should have no more than 2–3 em dashes total.

Colons follow the same discipline. When em dashes get banned, colons pile up as the substitute, and a draft full of "setup: payoff" sentences reads just as machine-made. Limit prose colons to 2–3 per document, reserved for thesis statements. List intros, headers, and labeled blocks are exempt. A deliberate sentence fragment often does the same work with more punch.

### 4. Anti-Antithesis Filter

The "it's not X, it's Y" construction can sound canned and pat. Use sparingly. When you do use it, prefer the softer "it's not just X — it's also Y" variant.

- **AVOID:** "The Defense here isn't the competition; it's Information Asymmetry."
- **OK (occasionally):** "It's not just that they reduced documentation burden by 86% — it's equally important that they've done it at 200 hospitals."

### 5. Active Voice

Active verbs, named actors. "HTD will map the workflow" beats "the workflow will be mapped." This is especially important in proposals and prescriptions — passive language hides who is responsible.

### 6. Forensic but Friendly

Be analytical like a consultant. Accessible like an old friend.

- No emojis.
- No cheerleading or sales-y hype.
- Use specific details from the news or play to ground the theory.
- The reader is smart. Don't condescend.

### 7. Scannable Structure

Bullets, bolded keywords, clear headers. Walls of text are prohibited. The reader is busy — respect their time by making the document easy to navigate.

---

## Constraint Checklist (for LLM-generated drafts)

Before publishing or accepting an LLM draft, check:

1. Are technical terms translated to plain English on first use?
2. Any banned vocabulary present? (Scan the list.)
3. Em dashes, semicolons, or prose colons used more than 2–3 times each? (Restructure.)
4. Any "it's not X, it's Y" constructions without the softening "just"? (Soften.)
5. Does the post open with a personal anecdote or scene? (If not, ask whether it should.)
6. Does the post close with a concrete "what to do Monday" prescription? (If not, ask whether it should.)
7. Were specific companies, deals, or competitors named where relevant? (Generic claims are weaker.)
8. Were data points cited with sources?
9. Is the voice forensic but friendly — analytical without being sales-y?
10. Does the post earn the reader's trust before making the hard claim?

Items 2, 3, and the emoji ban are machine-checked. Run `vale .` from the repo root rather than scanning by eye. See [`tools/linting/README.md`](../../tools/linting/README.md) for setup and for the full rule list. Items 1 and 4 through 10 still need a human.

---

## When to Lean Harder on Each Element

| If the piece is... | Lean into |
|---|---|
| A thought-leadership essay (long-form blog) | Personal opener; named academic mechanism; multiple specific company examples; close with prescription |
| A short-form post (LinkedIn-style) | Tighter version of the same arc; one anecdote, one mechanism, one example, one prescription |
| A case analysis (the trenches format) | Scouting-report structure; less anecdote, more diagnostic |
| A response to a current event | Lead with the event, not with personal context; treat the news itself as the anecdote |
