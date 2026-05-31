# Topic Page Instructions

Topic pages are concise, reader-facing mathematical wiki articles. They are not paper summaries, claim registries, source-ingestion reports, audit logs, roadmaps, or editorial status notes.

## Rules

- Topic pages use the learning-order universal article structure:
  `개요`, `준비와 notation`, `정의`, `기본 예시`, `핵심 관점`, `기본 성질`, optional `성질이 작동하는 방식`, `다른 topic들과의 관계`, `더 읽을 topic`, `Source notes`.
- Controlled variants are allowed only for the third section:
  `정의` may become `구성`, `정리의 진술`, or `map의 정의` according to topic type.
- Do not use `Toy model` as a heading.
- If an example is schematic rather than real, use `### 구조 예시` inside `## 기본 예시`.
- `기본 예시` must come immediately after the definition, construction, theorem statement, or map definition.
- `개요` must answer what the topic is, why it appears, and where it is used.
- `준비와 notation` must introduce symbols before they are used heavily.
- `정의`, `구성`, `정리의 진술`, and `map의 정의` must be mathematically clear and complete relative to the approved source and the page level: state the ambient setting, inputs, output object, and required conditions, relations, maps, or universal property.
- Do not use motivation, analogy, slogans, or "acts like" wording as a substitute for the formal definition.
- If source-backed material is insufficient for a complete definition, record the `definition` gap in workflow metadata rather than writing an incomplete pseudo-definition.
- `핵심 관점` should contain the main diagram, slogan, or mental model.
- `기본 성질` should list central properties or theorem-level facts with short explanations.
- Include `## 성질이 작동하는 방식` only when there is a meaningful computation, worked example, or mechanism.
- `다른 topic들과의 관계` must explain the mathematical relation to each linked topic.
- `더 읽을 topic` must include prerequisite topics, parent topics, and natural next topics.
- Follow `content/topics/STYLE_GUIDE.md` for section-by-section writing rules and topic-type variants.
- Use `templates/topic-maturity-audit-prompt.md` and `templates/readability-audit-prompt.md` for audits; audits may update workflow registries but must not rewrite topic pages without separate user approval.
- Do not add theorem statements, definitions, examples, constructions, or notation unless they are source-backed.
- Do not fill any section merely because the template contains that section. This applies to `개요`, `준비와 notation`, `정의` or its variants, `기본 예시`, `핵심 관점`, `기본 성질`, `성질이 작동하는 방식`, `다른 topic들과의 관계`, `더 읽을 topic`, and `Source notes`.
- If the studied/approved material does not support accurate content for a section, leave the visible section body empty or omit the optional section; record the gap in `data/topic_maturity.yml`, `data/research_queue.yml`, `data/review_backlog.yml`, or `reports/roadmap/next-actions.md`.
- Missing definitions, examples, properties, connections, viewpoints, notation setup, navigation links, or source notes should be recorded outside the topic exposition rather than filled with unsupported prose.
- Real examples require an approved source location. Schematic examples must be labeled `구조 예시` and may explain only a general mechanism.
- If no safe example exists, omit visible example content and record the example gap outside the topic exposition.
- User-approved discussion material may guide exposition, motivation, analogies, learning order, or notation decisions, but it must not support theorem-level claims or replace source-backed definitions and examples.
- User-approved discussion material belongs in `data/discussion_notes.yml`, not in paper/book source notes.
- Preserve source distinctions when adding future material.
- Keep category-level statements distinct from Grothendieck-ring-level statements.
- Write main exposition as polished Korean prose with English technical terms where useful.
- Every topic page must have a corresponding `data/topics.yml` entry with parent topics and prerequisite topics unless it is explicitly a root or provisional topic.
- Parent topics are broader mathematical concepts; prerequisite topics are needed before reading the current topic; related topics are useful nearby topics but are not prerequisites.
- Explain hierarchy in `## 다른 topic들과의 관계` as mathematical navigation, not as workflow metadata.
- Do not include topic-page sections named `Editorial notes`, `Current limitations`, `Human-review items`, `Human-review needed`, `Source provenance`, `Claim index`, `Roadmap`, or `Next sources needed`.
- Do not expose wiki-state or editorial-status language in reader-facing exposition. Avoid phrases such as "현재 이 wiki", "현재 page", "currently this wiki", "currently this page", "safe to say", "not yet imported", "source-poor", "future source work", "needs later source expansion", "notation is not normalized", "current limitations", "editorial notes", "claim metadata", and "source-backed claim".
- Topic pages must be readable without knowing that `data/claims.yml` exists.
- Topic pages must also be readable without knowing that `data/topic_maturity.yml`, `data/review_backlog.yml`, or `data/research_queue.yml` exists.
- Keep claim IDs, status labels, intake language, and registry metadata out of visible main exposition.
- Source information may appear only in the final `Source notes` section. Keep it short and collapsible when possible.
- `Source notes` may contain source names, exact theorem/proposition references, and one sentence explaining what is used.
- Move review tasks, unresolved notation, source-selection notes, and next steps to `reports/roadmap/next-actions.md`, source notes under `content/sources/papers/`, or YAML metadata under `data/`.
- Use proper Markdown math delimiters: inline `$...$`, displayed `$$...$$`.
- Replace bad plain-text notation in topic pages: `Cw,v` -> `$\mathcal C_{w,v}$`, `Aw,v` -> `$A_{w,v}$`, `K0(Cw,v)` -> `$K_0(\mathcal C_{w,v})$`, `M(w<=k Lambda, v<=k Lambda)` -> `$M(w_{\le k}\Lambda, v_{\le k}\Lambda)$`.
- Follow `content/glossary/notation.md`; use `$K_0(\mathcal C)$` for Grothendieck rings in topic prose, `$M\circ N$` for convolution products, `$q$-commuting` for q-commutation, and `$R\text{-gmod}$` for the graded quiver-Hecke module category.
