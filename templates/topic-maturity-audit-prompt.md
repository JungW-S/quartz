# Topic Maturity Audit Prompt

Use this prompt to audit every topic page against the canonical maturity levels and the learning-order universal article structure. This audit may update workflow registries, but it must not rewrite topic pages unless separately approved.

## Inputs To Read

- `content/topics/AGENTS.md`
- `content/topics/STYLE_GUIDE.md`
- all topic pages under `content/topics/`
- `data/topics.yml`
- `data/topic_maturity.yml`
- `data/research_queue.yml`
- `data/source_candidates.yml`
- `data/review_backlog.yml`
- `reports/roadmap/next-actions.md`

## Maturity Levels

Allowed `maturity` values:

- `stub`
- `orientation`
- `definition-ready`
- `example-ready`
- `study-ready`
- `reviewed`

Allowed `missing_components` values:

- `definition`
- `setup and notation`
- `basic picture`
- `example`
- `main facts`
- `source notes`
- `connections`

Interpret these stable registry values against the Korean learning-order headings:

- `definition`: missing `정의`, `구성`, `정리의 진술`, or `map의 정의`, or the visible definition is not mathematically complete from approved sources.
- `setup and notation`: missing `준비와 notation`.
- `basic picture`: missing `핵심 관점`.
- `example`: missing `기본 예시`.
- `main facts`: missing `기본 성질`.
- `source notes`: missing final `Source notes`.
- `connections`: missing `다른 topic들과의 관계` or `더 읽을 topic`.

An intentionally empty section body counts as missing for maturity purposes unless the gap is explicitly recorded in workflow metadata. Empty optional `성질이 작동하는 방식` should not count as missing.

## Audit Checks

- Does the title identify the central topic rather than a loose bundle of prerequisites?
- Does the title avoid forced `and` constructions unless the joined terms are a standard tightly coupled study unit?
- Does the title match the mathematical level of the page, such as category-level versus algebra-level or object-level versus Grothendieck-ring-level?
- Does the topic follow the learning-order universal structure?
- Is the third section an allowed variant: `정의`, `구성`, `정리의 진술`, or `map의 정의`?
- Does every non-empty section contain only source-backed material, established hierarchy metadata, or explicit user-approved exposition?
- If a section lacks accurate support, is the visible section body empty or the optional section omitted, with the gap recorded outside the topic page?
- Is the definition/construction mathematically complete relative to the approved source and page level, with ambient setting, inputs, output object, and required conditions, relations, maps, or universal property?
- Does the page avoid using motivation, analogy, or "acts like" prose as a replacement for the formal definition?
- Does `개요` answer what the topic is, why it appears, and where it is used?
- Does `준비와 notation` introduce symbols before heavy use?
- Does `기본 예시` come immediately after the definition, construction, theorem statement, or map definition?
- Does every non-empty `기본 예시` have one visible verification label: `검증: 논문 예시`, `검증: Sage 계산`, or `검증: 논문 그림`?
- If the example is schematic, is it labeled `### 구조 예시` and still paper- or Sage-verified?
- If the example uses a visual asset, is it captured/converted from an approved source figure/table/page or generated from checked Sage code stored under `scripts/examples/<topic-id>/`?
- Are generated example images stored under `content/assets/images/examples/<topic-id>/`?
- Does the page avoid LLM-generated mathematical examples and LLM-generated mathematical figures unless independently source- or Sage-verified?
- Does `핵심 관점` provide only a supported main diagram, slogan, formula, or mental model?
- Does `기본 성질` list only source-backed central properties or theorem-level facts with short explanations?
- Is `성질이 작동하는 방식` omitted unless there is a source-backed meaningful computation, worked example, or mechanism?
- Does `다른 topic들과의 관계` explain only source-backed, hierarchy-backed, or user-approved mathematical relations to linked topics?
- Does `더 읽을 topic` include only prerequisite topics, parent topics, and natural next topics established in hierarchy metadata or recorded decisions?
- Are source notes present and visually secondary?
- Are definitions and main facts source-supported, and are examples either source-supported or Sage-verified?
- Does the page separate object-level, class-level, and algebra-level statements where relevant?
- Does the page expose workflow state or editorial status in reader-facing prose?
- Does the page use local notation from `content/glossary/notation.md` and `data/notation.yml`?
- Existing pages that still use the old English structure should be marked as needing topic-page polishing, with any rewrite marked approval-required.

## Allowed Outputs

- Update `data/topic_maturity.yml`.
- Update `data/research_queue.yml`.
- Add or update `data/review_backlog.yml` items.
- Update `reports/roadmap/next-actions.md`.
- Optionally write `reports/reviews/YYYY-MM-DD-topic-maturity-audit.md`.

## Safety Rules

- Do not rewrite topic pages during the audit.
- Do not add claims, source notes, or graph edges.
- Do not download or intake sources.
- Mark topic rewrites, claim additions, and source intake as approval-required actions.
