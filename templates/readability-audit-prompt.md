# Readability Audit Prompt

Use this prompt to audit topic pages against `content/topics/STYLE_GUIDE.md`. This audit detects reader-facing prose issues and workflow leakage, but it does not rewrite pages unless the user separately approves edits.

## Inputs To Read

- `content/topics/AGENTS.md`
- `content/topics/STYLE_GUIDE.md`
- topic pages under `content/topics/`
- `data/topic_maturity.yml`
- `data/review_backlog.yml`
- `reports/roadmap/next-actions.md`

## Checks

- The learning-order universal section structure is present:
  `개요`, `준비와 notation`, `정의` or an allowed variant, `기본 예시`, `핵심 관점`, `기본 성질`, optional `성질이 작동하는 방식`, `다른 topic들과의 관계`, `더 읽을 topic`, and final `Source notes`.
- The third section is `정의`, `구성`, `정리의 진술`, or `map의 정의`.
- `개요` answers what the topic is, why it appears, and where it is used.
- `준비와 notation` introduces symbols before they are used heavily.
- Every section body contains only source-backed material or explicit user-approved exposition; unsupported sections are empty or optional sections are omitted, with the gap recorded outside the topic page.
- The definition/construction section is mathematically clear and complete relative to the approved source and page level: it states the ambient setting, input data, output object, and required conditions, relations, maps, or universal property.
- Motivation, analogy, or "acts like" prose is not used as a substitute for the formal definition.
- `기본 예시` comes immediately after the definition, construction, theorem statement, or map definition.
- Schematic examples are labeled `### 구조 예시`, not `Toy model`.
- `핵심 관점` contains the main diagram, slogan, or mental model only when the page has enough source-backed or user-approved material.
- `기본 성질` lists only source-backed central properties or theorem-level facts with short explanations.
- `성질이 작동하는 방식` appears only when there is a source-backed meaningful computation, worked example, or mechanism.
- `다른 topic들과의 관계` explains only source-backed, hierarchy-backed, or user-approved mathematical relations to linked topics.
- `더 읽을 topic` includes prerequisite topics, parent topics, and natural next topics only when established in hierarchy metadata or recorded decisions.
- Reader-facing prose does not mention workflow state, claim registries, source intake, editorial status, or roadmap language.
- The page does not include prohibited sections such as `Editorial notes`, `Current limitations`, `Human-review items`, `Human-review needed`, `Source provenance`, `Claim index`, `Roadmap`, or `Next sources needed`.
- Source notes are last and secondary.
- Paragraphs are short and symbols are introduced before heavy use.
- Topic pages use proper Markdown math delimiters.
- Existing pages that still use the old English structure should be reported as needing a future migration pass. Do not rewrite them during the audit.
- Empty sections are acceptable when the missing content is recorded in `data/topic_maturity.yml`, `data/review_backlog.yml`, `data/research_queue.yml`, or `reports/roadmap/next-actions.md`; placeholder prose inside empty sections should be flagged.

## Prohibited Phrase Scan

Flag phrases such as:

- "현재 이 wiki"
- "현재 page"
- "currently this wiki"
- "currently this page"
- "safe to say"
- "not yet imported"
- "source-poor"
- "future source work"
- "needs later source expansion"
- "notation is not normalized"
- "current limitations"
- "editorial notes"
- "claim metadata"
- "source-backed claim"

## Allowed Outputs

- Write `reports/reviews/YYYY-MM-DD-readability-audit.md` when requested.
- Update `data/review_backlog.yml`.
- Update `data/topic_maturity.yml` readability notes.
- Update `reports/roadmap/next-actions.md`.

## Safety Rules

- Do not rewrite topic pages during the audit.
- Do not add claims or source notes.
- Do not make mathematical assertions from readability findings.
- Mark any page rewrite as approval-required.
