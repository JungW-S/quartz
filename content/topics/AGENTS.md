# Topic Page Instructions

Topic pages are concise, reader-facing mathematical wiki articles. They are not paper summaries, claim registries, source-ingestion reports, audit logs, roadmaps, or editorial status notes.

## Rules

- Topic pages use the universal article structure:
  `What it is`, `Why it appears`, `Setup and notation`, `Definition`, `Basic picture`, `Example`, `Main facts`, `Why it matters`, `Connections`, `Source notes`.
- Controlled variants are allowed only for the fourth section:
  `Definition` may become `Construction`, `Statement`, or `Definition of the map` according to topic type.
- Do not use `Where they live` or `Toy model` as top-level headings.
- If needed, use `### Schematic example` or `### Concrete example` inside `## Example`.
- Follow `content/topics/STYLE_GUIDE.md` for section-by-section writing rules and topic-type variants.
- Use `templates/topic-maturity-audit-prompt.md` and `templates/readability-audit-prompt.md` for audits; audits may update workflow registries but must not rewrite topic pages without separate user approval.
- Do not add theorem statements, definitions, examples, constructions, or notation unless they are source-backed.
- Preserve source distinctions when adding future material.
- Keep category-level statements distinct from Grothendieck-ring-level statements.
- Write main exposition as polished Korean prose with English technical terms where useful.
- Every topic page must have a corresponding `data/topics.yml` entry with parent topics and prerequisite topics unless it is explicitly a root or provisional topic.
- Parent topics are broader mathematical concepts; prerequisite topics are needed before reading the current topic; related topics are useful nearby topics but are not prerequisites.
- Explain hierarchy in `## Connections` as mathematical navigation, not as workflow metadata.
- Do not include topic-page sections named `Editorial notes`, `Current limitations`, `Human-review items`, `Human-review needed`, `Source provenance`, `Claim index`, `Roadmap`, or `Next sources needed`.
- Do not expose wiki-state or editorial-status language in reader-facing exposition. Avoid phrases such as "currently this wiki", "currently this page", "safe to say", "not yet imported", "source-poor", "future source work", "needs later source expansion", "notation is not normalized", "current limitations", "editorial notes", "claim metadata", and "source-backed claim".
- Topic pages must be readable without knowing that `data/claims.yml` exists.
- Topic pages must also be readable without knowing that `data/topic_maturity.yml`, `data/review_backlog.yml`, or `data/research_queue.yml` exists.
- Keep claim IDs, status labels, intake language, and registry metadata out of visible main exposition.
- Source information may appear only in the final `Source notes` section. Keep it short and collapsible when possible.
- `Source notes` may contain source names, exact theorem/proposition references, and one sentence explaining what is used.
- Move review tasks, unresolved notation, source-selection notes, and next steps to `reports/roadmap/next-actions.md`, source notes under `content/sources/papers/`, or YAML metadata under `data/`.
- Use proper Markdown math delimiters: inline `$...$`, displayed `$$...$$`.
- Replace bad plain-text notation in topic pages: `Cw,v` -> `$\mathcal C_{w,v}$`, `Aw,v` -> `$A_{w,v}$`, `K0(Cw,v)` -> `$K_0(\mathcal C_{w,v})$`, `M(w<=k Lambda, v<=k Lambda)` -> `$M(w_{\le k}\Lambda, v_{\le k}\Lambda)$`.
- Follow `content/glossary/notation.md`; use `$K_0(\mathcal C)$` for Grothendieck rings in topic prose, `$M\circ N$` for convolution products, `$q$-commuting` for q-commutation, and `$R\text{-gmod}$` for the graded quiver-Hecke module category.
