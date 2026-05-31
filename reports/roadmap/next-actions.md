# Next Actions

This roadmap is advisory. It does not authorize source download, source intake, claim addition, topic rewrite, or new topic creation.

## Current Workflow State

- Kashiwara-Nakashima 2025 was ingested from `inbox/papers/crystal.tex`; a local PDF was compiled and staged under `content/assets/pdfs/`.
- `localized-crystals` is now a source-backed study article centered on $\operatorname{Irr}(\widetilde{\mathcal C}_w)$.
- `quiver-hecke-algebra-localization` now explains the localized category $\widetilde{\mathcal C}_w$ used by the crystal construction.
- `cellular-crystals` was created as the prerequisite target crystal page for $\mathcal B_w$.
- The remaining undergraduate-accessibility gap is a general prerequisite page for crystal bases and crystal graphs.

## Single Safest Next Task

### Evaluate a general crystal-bases prerequisite source

- Action type: `new-source intake`
- New source required: yes.
- User approval required: yes before any download, intake, claim addition, or new page creation.
- Why it matters: both `localized-crystals` and `cellular-crystals` rely on ordinary crystal terminology that is still not introduced by a lower-level prerequisite page.
- Likely files to change:
  - `data/source_candidates.yml`
  - `data/research_queue.yml`
  - `data/review_backlog.yml`
  - `reports/roadmap/next-actions.md`
- Expected mathematical benefit: gives undergraduates a path from basic crystal graphs to localized and cellular crystals without overloading the advanced pages.
- Risk level: medium
- Exact prompt to paste:

```text
Evaluate candidate sources for a general crystal-bases prerequisite topic, especially Kashiwara 1993 and related crystal-background sources already listed in data/source_candidates.yml. Update candidate and queue metadata only. Do not download, ingest, add claims, create source notes, or create the topic page until I approve a specific source.
```

## Alternatives

### 1. Add a concrete example from Kashiwara-Nakashima 2025 Example 9.6

- Action type: `existing-source expansion`
- New source required: no.
- User approval required: yes before topic-page edits.
- Why it matters: `localized-crystals` and `quiver-hecke-algebra-localization` mention the $A_3$ example only at a high level.
- Likely files to change:
  - `content/topics/localized-crystals.md`
  - `content/topics/quiver-hecke-algebra-localization.md`
  - `data/claims.yml`
  - `reports/roadmap/next-actions.md`
- Expected mathematical benefit: makes the localized simple-object to cellular-coordinate comparison more concrete.
- Risk level: medium
- Exact prompt to paste:

```text
Using only Kashiwara-Nakashima 2025 Example 9.6, propose one small concrete example expansion for localized crystals or quiver-Hecke localization. Do not edit topic pages until I approve the exact paragraph and source location.
```

### 2. Evaluate the KKOP localization series

- Action type: `new-source intake`
- New source required: yes.
- User approval required: yes before download or intake.
- Why it matters: Kashiwara-Nakashima 2025 cites KKOP21, KKOP22, and KKOP23 for the formal localization machinery, but this intake only used the statements needed for topic orientation.
- Likely files to change:
  - `data/source_candidates.yml`
  - `data/research_queue.yml`
  - `reports/roadmap/next-actions.md`
- Expected mathematical benefit: supports a more reliable prerequisite path for category localization.
- Risk level: medium
- Exact prompt to paste:

```text
Evaluate KKOP21, KKOP22, and KKOP23 as candidate sources for formal quiver-Hecke category localization. Update data/source_candidates.yml and reports/roadmap/next-actions.md only; do not download, ingest, add claims, or rewrite pages.
```

### 3. Run a notation audit for localized crystal notation

- Action type: `notation normalization`
- New source required: no.
- User approval required: no for the audit; yes for page rewrites.
- Why it matters: the new pages introduce $\widetilde{\mathcal C}_w$, $\operatorname{Irr}(\widetilde{\mathcal C}_w)$, $\mathcal B_w$, and $\widetilde E_i,\widetilde F_i$.
- Likely files to change:
  - `data/notation.yml`
  - `data/review_backlog.yml`
  - `reports/reviews/YYYY-MM-DD-notation-audit.md`
  - `reports/roadmap/next-actions.md`
- Expected mathematical benefit: reduces notation drift between category-level and crystal-level pages.
- Risk level: low
- Exact prompt to paste:

```text
Run templates/notation-audit-prompt.md for localized-crystal notation, focusing on content/topics/localized-crystals.md, content/topics/cellular-crystals.md, and content/topics/quiver-hecke-algebra-localization.md. Do not rewrite pages; update data/notation.yml and data/review_backlog.yml only if needed.
```

## Candidate Sources

These are candidates only. They are not citations and do not support claims until approved, downloaded if needed, ingested, and recorded with source locations.

- `kashiwara93-crystal-base-demazure-character-formula`: candidate source for crystal and Demazure-crystal prerequisites.
- `kanakubo-nakashima23-half-potential-geometric-crystals`: candidate background for cellular crystals and connectedness.
- `nakashima22-categorified-crystal-localized-quantum-coordinate-rings`: candidate predecessor or companion source for localized quantum coordinate-ring crystals.
- `kkop21-localizations-quiver-hecke-algebras`, `kkop22-localizations-quiver-hecke-algebras-ii`, `kkop23-localizations-quiver-hecke-algebras-iii`: candidate sources for formal localization machinery.

## Ranking Basis

- Mathematical importance: crystal prerequisites now block undergraduate readability more than additional advanced localized-category detail.
- Current page weakness: `localized-crystals` and `cellular-crystals` are source-backed but assume basic crystal graph vocabulary.
- Dependency value: a crystal-bases prerequisite page would support multiple advanced topics.
- Source availability: Kashiwara-Nakashima 2025 is local; other crystal and localization sources remain candidates only.
- Hallucination risk: formal localization and general crystal theory should come from approved source-location-specific intake.

<!-- NEEDS-HUMAN-REVIEW -->

Do not expand the new localized-crystal pages into proof notes. Keep future work focused on prerequisite exposition and small source-backed examples.
