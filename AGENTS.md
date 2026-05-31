# Agent Instructions

This repository is a topic-centered mathematical study wiki built on Quartz and edited as Markdown. It is not a paper-summary archive.

## Repository Model

- `content/` contains authored Markdown for the Quartz site.
- `content/topics/` is for topic pages organized around reusable mathematical concepts.
- `content/sources/` is for concise source/provenance notes, not long summaries.
- `data/` contains YAML registries for metadata and graph information.
- `templates/` contains reusable authoring and intake templates.
- `public/` is generated Quartz output and must not be edited directly.

## Content Rules

- Do not create real mathematical claims without a real source and source location.
- Do not create fake sources, placeholder papers, invented citations, or fabricated metadata.
- Do not turn a paper into a long prose summary. Source notes should support provenance and navigation.
- Keep topic pages concept-centered and reader-facing. They must not read like claim registry views, source-ingestion reports, audit logs, roadmaps, or editorial status notes.
- Topic pages must use the universal article structure: `What it is`, `Why it appears`, `Setup and notation`, `Definition`, `Basic picture`, `Example`, `Main facts`, `Why it matters`, `Connections`, `Source notes`.
- The fourth section may vary by topic type: `Construction` for construction topics, `Statement` for theorem topics, and `Definition of the map` for map or operation topics.
- Do not use `Where they live` or `Toy model` as universal topic-page headings.
- Follow `content/topics/STYLE_GUIDE.md` for reader-facing topic-page prose rules.
- Do not include topic-page sections named `Editorial notes`, `Current limitations`, `Human-review items`, `Human-review needed`, `Source provenance`, `Claim index`, `Roadmap`, or `Next sources needed`.
- Keep claim IDs, status labels, source locations, intake/provenance metadata, and registry metadata out of main topic exposition.
- Topic pages must be readable without knowing that `data/claims.yml` exists.
- Source information may appear only in the final `Source notes` section, preferably collapsed. Keep it short: source name, exact theorem/proposition reference if available, and one sentence explaining what is used.
- Move review tasks, unresolved notation, source-selection notes, and next steps to `reports/roadmap/next-actions.md`, source notes under `content/sources/papers/`, or YAML metadata under `data/`.
- Do not expose wiki-state or editorial-status language in reader-facing topic exposition. Avoid phrases such as "currently this wiki", "currently this page", "safe to say", "not yet imported", "source-poor", "future source work", "needs later source expansion", "notation is not normalized", "current limitations", "editorial notes", "claim metadata", and "source-backed claim".
- Use proper Markdown math delimiters in topic pages: inline `$...$`, displayed `$$...$$`. Replace plain-text notation such as `Cw,v`, `Aw,v`, `K0(Cw,v)`, and `M(w<=k Lambda, v<=k Lambda)` with proper LaTeX.
- Follow `content/glossary/notation.md` for local notation. In reader-facing topic pages, write Grothendieck rings as $K_0(\mathcal C)$ and $K_0(\mathcal C_{w,v})$; reserve source-specific notation such as `K(\mathcal C)` for source notes when needed.
- Mark uncertain or inferred material with `<!-- NEEDS-HUMAN-REVIEW -->`.
- Respect `<!-- USER-APPROVED: do not rewrite without explicit instruction -->` blocks.
- Codex may append under `<!-- CODEX-MANAGED: may append source-backed material here -->` only when material is source-backed.

## Topic Hierarchy Rules

- Every new topic must specify `topic_kind`, `parent_topics`, `prerequisite_topics`, `child_topics`, `related_topics`, and `maturity` in `data/topics.yml`.
- Do not create isolated specialized topics unless they are explicitly marked as `topic_kind: root` or `topic_kind: provisional`.
- Parent topics are broader mathematical concepts under which the current topic sits.
- Prerequisite topics are topics needed to understand the current topic.
- Related topics are not the same as prerequisites, parents, or children.
- If a needed parent topic does not exist, create a source-backed stub parent topic only when the user has approved new topic creation; otherwise add the missing parent to `data/research_queue.yml`.
- When adding or changing hierarchy metadata, keep `parent_topics` and `child_topics` consistent in both directions.

## Research Workflow Gates

Manual user approval is required before any of these actions:

- source download, fetch, staging, or PDF intake;
- source-note creation for a new source;
- claim addition or claim-status promotion;
- topic-page rewrite or source-backed topic expansion;
- new topic-page creation.

The following automation is allowed without separate approval when it does not perform a gated action:

- source candidate suggestion in `data/source_candidates.yml`;
- weekly or dated review report under `reports/reviews/`;
- broken-link check;
- topic maturity audit using `data/topic_maturity.yml`;
- notation audit using `data/notation.yml`;
- readability audit against `content/topics/STYLE_GUIDE.md`.

Automations must not download papers, add claims, rewrite topics, create source notes, or create new topic pages unless a later user prompt explicitly approves that specific action.

## Next-Action Advisor

- End every substantive final response with a short next recommended task. For tiny answers, one concise sentence is enough.
- Prefer one single best next task first. Add up to three alternatives only when they are genuinely useful.
- For each recommended next task, state whether user approval is required and whether a new source is required whenever that affects what can be done next.
- After every research workflow task, paper-intake task, topic-expansion task, review audit, or notation audit, update `reports/roadmap/next-actions.md`.
- Classify each action as exactly one of: `existing-source expansion`, `new-source intake`, `topic-page polishing`, `graph cleanup`, `notation normalization`, or `human-review task`.
- Rank next actions by mathematical importance, current page weakness, dependency value, source availability, and hallucination risk.
- Mark proposed sources as candidates only. Candidate sources are not citations and do not support claims until approved and ingested.
- Do not download, fetch, stage, or intake a new paper without explicit user approval for that specific source.
- Keep next actions small and reviewable, with exact likely files, expected mathematical benefit, approval requirement, new-source requirement, risk level, and an exact prompt the user can paste.
- Never use the roadmap workflow to create unsupported mathematical claims or to turn the wiki into a paper-summary archive.

## Batch Discipline

Implement only the batch explicitly requested by the user. Do not create seed topic pages, validation scripts, source notes, or source-backed content until the relevant later batch is requested.
