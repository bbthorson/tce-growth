# Tools

**Content generation and AI personas for writing about TCG publicly.** A voice guide, three short protocols, two multi-phase content generators, and a library of published examples used as style references.

Parent: [publishing/](../) · Sibling: [01-cases/](../01-cases/)

This is *not* where the instruments live (see [`../../practice/`](../../practice/)). This is the writer's toolkit.

## Files

### Voice and protocols

- **[voice-guide.md](./voice-guide.md)**: the "Conversational Intellectual" voice. Four linguistic rules plus the constraint checklist the linter enforces.
- **[source-quotes.md](./source-quotes.md)**: citable passages from every research file, grouped by source. Numbers are not here. They live in the provenance audit with their verification status.
- **[writing-protocols.md](./writing-protocols.md)**: three protocols in one file. The AI persona for an LLM acting as a CSO-level deal analyst, the context request check run before drafting, and the four-step trenches analysis that every case in [`../01-cases/`](../01-cases/) follows.

### Generators (multi-phase content workflows)

- **[long-form-blog-generator.md](./long-form-blog-generator.md)**: three-phase workflow for long-form strategic posts of about 5,000 words.
- **[short-form-trenches-generator.md](./short-form-trenches-generator.md)**: three-phase workflow for 200 to 500 word LinkedIn-style posts.

### Style references

Published examples. Use them to calibrate voice and structure, not to copy. They are kept verbatim as the record of what went out, so the linter's anti-hype and retired-term rules are off inside this directory.

- **[style-references/blog-posts/](./style-references/blog-posts/)**: three long-form pieces (TCE and sales, the ACCESS model, competing on value).
- **[style-references/short-form-posts/](./style-references/short-form-posts/)**: seven short-form pieces, including the archived `bridge-v-toaster`.

## Workflow

```
publishing/README.md          (pick the content pillar)
        ↓
voice-guide.md                (calibrate voice)
        ↓
writing-protocols.md          (pre-flight context check)
        ↓
{long-form | short-form}-generator.md   (multi-phase workflow)
        ↓
style-references/             (sanity-check against published examples)
```

For trenches and case analyses specifically, the output drops into [`../01-cases/`](../01-cases/).
