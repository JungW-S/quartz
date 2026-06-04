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
- Topic titles must name the central mathematical object, construction, theorem, map, or category of the page. Avoid titles joined by `and` unless the joined terms form a standard tightly coupled concept for this wiki, such as root-system and weight-lattice prerequisites.
- If a page bundles multiple prerequisite notions, choose the central notion as the title and explain supporting notions inside the page, or split the page when no central notion exists.
- Titles must match the mathematical level of the content: do not title a category localization as an algebra localization when the construction localizes a module category rather than the algebra itself.
- Do not fill any section merely because the template contains that section. Unsupported exposition, notation, definitions, examples, viewpoints, properties, mechanisms, connections, navigation, or source notes must not be invented.
- If the studied/approved material does not support accurate content for a section, leave the visible section body empty or omit the optional section; do not add caveats, placeholders, apology text, or workflow language in the topic page.
- Missing source-backed material must be recorded in `data/topic_maturity.yml`, `data/research_queue.yml`, `data/review_backlog.yml`, or `reports/roadmap/next-actions.md`, not patched over in reader-facing prose.
- Topic pages must use the learning-order universal article structure: `개요`, `준비와 notation`, `정의`, `기본 예시`, `핵심 관점`, `기본 성질`, optional `성질이 작동하는 방식`, `다른 topic들과의 관계`, `더 읽을 topic`, `Source notes`.
- The third section may vary by topic type: `구성` for construction topics, `정리의 진술` for theorem topics, and `map의 정의` for map or operation topics.
- `개요` must answer what the topic is, why it appears, and where it is used.
- `준비와 notation` must introduce symbols before they are used heavily.
- `정의`, `구성`, `정리의 진술`, and `map의 정의` sections must be mathematically clear and complete relative to the approved source and page level. They must state the ambient context, input data, object or construction being defined, and the required conditions, relations, maps, or universal properties. Do not substitute slogans, analogies, or "acts like" prose for the formal definition.
- If a complete definition cannot be written from approved sources, leave the visible definition section empty rather than writing a pseudo-definition, and record the `definition` gap in `data/topic_maturity.yml`, `data/review_backlog.yml`, or `reports/roadmap/next-actions.md`.
- `기본 예시` must come immediately after the definition, construction, statement, or map definition. Examples are allowed only when they are verified by an approved source location or by checked Sage code stored in this repository. If no verified example exists, omit visible example content and record the gap in workflow metadata.
- `핵심 관점` should contain the main diagram, slogan, or mental model only when it is supported by approved sources or user-approved exposition.
- `기본 성질` should list central properties or theorem-level facts with short explanations only when they are source-backed.
- Include `성질이 작동하는 방식` only when there is a meaningful computation, worked example, or mechanism.
- `다른 topic들과의 관계` must explain only mathematical relations that are supported by approved sources, established hierarchy metadata, or user-approved exposition.
- `더 읽을 topic` must include prerequisite topics, parent topics, and natural next topics only when the relationship is established in hierarchy metadata or recorded workflow decisions.
- Do not use `Toy model` as a topic-page heading.
- Follow `content/topics/STYLE_GUIDE.md` for reader-facing topic-page prose rules.
- Do not include topic-page sections named `Editorial notes`, `Current limitations`, `Human-review items`, `Human-review needed`, `Source provenance`, `Claim index`, `Roadmap`, or `Next sources needed`.
- Keep claim IDs, status labels, source locations, intake/provenance metadata, and registry metadata out of main topic exposition.
- Topic pages must be readable without knowing that `data/claims.yml` exists.
- Source information may appear only in the final `Source notes` section, preferably collapsed, except for the short verification label required directly under visible examples. Keep source notes short: source name, exact theorem/proposition reference if available, and one sentence explaining what is used.
- Move review tasks, unresolved notation, source-selection notes, and next steps to `reports/roadmap/next-actions.md`, source notes under `content/sources/papers/`, or YAML metadata under `data/`.
- Do not expose wiki-state or editorial-status language in reader-facing topic exposition. Avoid phrases such as "현재 이 wiki", "현재 page", "currently this wiki", "currently this page", "safe to say", "not yet imported", "source-poor", "future source work", "needs later source expansion", "notation is not normalized", "current limitations", "editorial notes", "claim metadata", and "source-backed claim".
- Use proper Markdown math delimiters in topic pages: inline `$...$`, displayed `$$...$$`. Replace plain-text notation such as `Cw,v`, `Aw,v`, `K0(Cw,v)`, and `M(w<=k Lambda, v<=k Lambda)` with proper LaTeX.
- Follow `content/glossary/notation.md` for local notation. In reader-facing topic pages, write Grothendieck rings as $K_0(\mathcal C)$ and $K_0(\mathcal C_{w,v})$; reserve source-specific notation such as `K(\mathcal C)` for source notes when needed.
- Mark uncertain or inferred material with `<!-- NEEDS-HUMAN-REVIEW -->`.
- Respect `<!-- USER-APPROVED: do not rewrite without explicit instruction -->` blocks.
- Codex may append under `<!-- CODEX-MANAGED: may append source-backed material here -->` only when material is source-backed.

## Example Verification Rules

- Allowed visible examples are exactly:
  - `검증: 논문 예시` for an example, computation, figure, table, or page explicitly present in an approved source.
  - `검증: Sage 계산` for an example verified by a Sage script stored under `scripts/examples/<topic-id>/<example-id>.sage`.
  - `검증: 논문 그림` for a visual example captured or converted from an approved source figure, table, or page.
- Put a short verification label directly under each visible example. Put detailed source location, PDF path, Sage command, code path, generated image path, and reproduction notes in final `Source notes`.
- Do not use LLM-generated mathematical examples or LLM-generated mathematical figures as topic-page examples unless they have been independently verified by an approved source or by checked Sage code.
- Sage-based examples must separate mathematical verification from drawing: first construct and check the mathematical object, then generate the image from the checked data.
- Store Sage example code under `scripts/examples/<topic-id>/`, generated example images under `content/assets/images/examples/<topic-id>/`, and optional verification reports under `reports/examples/`.
- Schematic examples are allowed only when the schematic mechanism is itself source-supported or Sage-verified, and they must still be labeled `### 구조 예시` plus one of the verification labels above.
- If no paper-verified or Sage-verified example exists, leave `## 기본 예시` empty and record the example gap in `data/topic_maturity.yml`, `data/research_queue.yml`, `data/review_backlog.yml`, or `reports/roadmap/next-actions.md`.

## User Discussion Notes

- User discussions may support exposition, motivation, learning order, analogy, and notation decisions.
- User discussions must not support theorem-level claims, definitions, real examples, source-backed facts, or claim additions.
- Store user-approved discussion material separately from paper, book, and lecture sources in `data/discussion_notes.yml`.
- Use discussion labels such as `user-approved-exposition`, `user-approved-interpretation`, `notation-decision`, and `learning-order-decision`.
- Discussion notes are auxiliary writing guidance, not citations and not provenance for mathematical claims.

## Topic Hierarchy Rules

- Every new topic must specify `topic_kind`, `parent_topics`, `prerequisite_topics`, `child_topics`, `related_topics`, and `maturity` in `data/topics.yml`.
- Every topic registry entry must also specify `sidebar_group`, `sidebar_order`, and `conceptual_role`. These fields control Explorer grouping and study navigation; they do not replace the mathematical DAG fields.
- Allowed large sidebar groups are `category-theory`, `quantum-groups`, `crystal-bases`, `quantum-affine-algebras`, `quiver-hecke-klr-algebras`, `cluster-algebras`, `monoidal-categorification`, and `localization-of-categories`.
- Keep the `cluster-algebras` group coarse: use `Cluster Algebras` and `Quantum Cluster Algebras` as the main pages unless a later source-backed need justifies another topic.
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

## Topic Polish Trigger

- The exact user messages `topic 수정` and `토픽수정` trigger one bounded topic-page polishing pass.
- This trigger counts as explicit approval to rewrite exactly one existing topic page for reader-facing clarity and structure. It does not approve source downloads, source intake, claim additions, new examples, new mathematical facts, or new topic creation.
- Start the trigger by running `python3 scripts/select_topic_for_polish.py`.
- Choose one topic among the lowest `polish_count` entries in `data/topic_polish_log.yml`, preferring a page that already has visible source-backed prose and can be improved without new sources.
- If the selected topic is a title-only stub, lacks enough source-backed material for safe prose edits, or needs new mathematical content rather than polishing, skip it and choose the next lowest-count rational candidate.
- Before editing, identify concrete sentence or structure fixes and judge whether each one improves undergraduate readability, preserves the mathematical meaning, and avoids unsupported material.
- After a successful polish, increment that topic's `polish_count` in `data/topic_polish_log.yml`, update `last_polished`, `last_summary`, and append a `history` item.
- Topic polish passes may update `data/topic_maturity.yml` readability metadata and `reports/roadmap/next-actions.md`; they must keep maturity/backlog/roadmap language out of the topic page itself.
- Use `templates/topic-polish-trigger-prompt.md` as the operational checklist.

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
- End-of-task roadmap updates should list intentionally unfilled components when a section was left empty or deferred because no safe source-backed material exists.
- Never use the roadmap workflow to create unsupported mathematical claims or to turn the wiki into a paper-summary archive.

## Batch Discipline

Implement only the batch explicitly requested by the user. Do not create seed topic pages, validation scripts, source notes, or source-backed content until the relevant later batch is requested.
