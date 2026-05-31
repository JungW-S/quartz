# Next Actions

This roadmap is advisory. It does not authorize source download, source intake, claim addition, topic rewrite, or new topic creation.

## Current Workflow State

- Hong-Kang 2002 Chapter 1 was used to create `lie-algebras-and-hopf-algebras` as a small prerequisite page for `quantum-groups`.
- The Lie/Hopf prerequisite gap under `quantum-groups` is resolved at the introductory level.
- Lower-level quiver-Hecke/KLR source evaluation was completed on 2026-05-31.
- Brundan 2013 was approved, downloaded from arXiv, and used to move `quiver-hecke-algebras` from orientation to definition-ready.
- Canonical backup or cross-check source: `khovanov-lauda09-diagrammatic-categorification-quantum-groups-i`, already present as a user-provided local PDF in `inbox/papers2/`.
- Remaining undergraduate-accessibility gaps: `quiver-hecke-algebras` has the basic definition but still needs a fuller low-rank worked example and a canonical-source normalization check before study-ready; `quiver-hecke-algebra-localization` still needs a category-localization prerequisite source.

## Single Safest Next Task

### Cross-check the KLR definition against Khovanov-Lauda 2009

- Action type: `new-source intake`
- New source required: yes, but a user-provided local PDF is already available.
- User approval required: yes before source intake, claim addition, or topic expansion.
- Why it matters: `quiver-hecke-algebras` is now definition-ready from Brundan 2013. A narrow KL09 cross-check would reduce normalization risk before expanding examples, symmetric quiver-Hecke notation, or localization links.
- Likely files to change:
  - `content/assets/pdfs/khovanov-lauda09-diagrammatic-categorification-quantum-groups-i.pdf`
  - `content/sources/papers/khovanov-lauda09-diagrammatic-categorification-quantum-groups-i.md`
  - `content/topics/quiver-hecke-algebras.md`
  - `data/claims.yml`
  - `data/topic_maturity.yml`
  - `reports/roadmap/next-actions.md`
- Expected mathematical benefit: anchors the Brundan-based exposition in the original diagrammatic KLR construction without turning the page into proof notes.
- Risk level: medium
- Exact prompt to paste:

```text
I approve source candidate `khovanov-lauda09-diagrammatic-categorification-quantum-groups-i` for a canonical-source cross-check of content/topics/quiver-hecke-algebras.md. Use only the user-provided local PDF in inbox/papers2, add at most 4 claims, and do not expand beyond the definition-ready level.
```

## Alternatives

### 1. Add one fuller Brundan low-rank example

- Action type: `existing-source expansion`
- New source required: no.
- User approval required: yes before topic-page edits.
- Why it matters: the page has a short nil-Hecke and type \(A_2\) example, but not yet a slow undergraduate-facing worked calculation.
- Likely files to change:
  - `content/topics/quiver-hecke-algebras.md`
  - `data/claims.yml`
  - `data/topic_maturity.yml`
- Expected mathematical benefit: moves the page toward example-ready while staying inside the already ingested Brundan source.
- Risk level: medium
- Exact prompt to paste:

```text
Using only Brundan 2013, propose one additional low-rank example paragraph for content/topics/quiver-hecke-algebras.md; do not edit the page until I approve the exact wording and source location.
```

### 2. Align symmetric quiver-Hecke notation with KKK sources

- Action type: `new-source intake`
- New source required: yes.
- User approval required: yes before download or intake.
- Why it matters: later KKKO/KKOP material uses symmetric quiver-Hecke conventions; this should be aligned only after the basic KLR definition is present.
- Likely files to change:
  - `content/assets/pdfs/kang-kashiwara-kim18-symmetric-quiver-hecke-algebras-r-matrices.pdf`
  - `content/sources/papers/kang-kashiwara-kim18-symmetric-quiver-hecke-algebras-r-matrices.md`
  - `content/topics/quiver-hecke-algebras.md`
  - `data/notation.yml`
  - `data/topic_maturity.yml`
- Expected mathematical benefit: prevents notation drift between the parent page and advanced localization/categorification pages.
- Risk level: high
- Exact prompt to paste:

```text
I approve source candidate `kang-kashiwara-kim18-symmetric-quiver-hecke-algebras-r-matrices` for notation alignment after the basic KLR definition is already present. Download only arXiv:1304.0323 and do not add localization details.
```

### 3. Evaluate the KKOP localization series

- Action type: `new-source intake`
- New source required: yes.
- User approval required: yes before download or intake.
- Why it matters: the category-localization prerequisite path below localized crystals still depends on candidate sources.
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

## Candidate Sources

These are candidates only. They are not citations and do not support claims until approved, downloaded if needed, ingested, and recorded with source locations.

- `brundan13-quiver-hecke-algebras-categorification`: downloaded and ingested as the first definition-ready source for `quiver-hecke-algebras`.
- `khovanov-lauda09-diagrammatic-categorification-quantum-groups-i`: canonical original source; user-provided local PDF is available.
- `rouquier11-quiver-hecke-algebras-2-lie-algebras`: foundational 2-representation companion, but not the first undergraduate-facing definition source.
- `kang-kashiwara-kim18-symmetric-quiver-hecke-algebras-r-matrices`: notation-alignment source for the symmetric quiver-Hecke setting used by later KKKO/KKOP material.
- `kleshchev-ram10-homogeneous-representations-khovanov-lauda-algebras`: later example/representation source, not recommended for the first definition pass.
- `kkop21-localizations-quiver-hecke-algebras`, `kkop22-localizations-quiver-hecke-algebras-ii`, `kkop23-localizations-quiver-hecke-algebras-iii`: candidate sources for formal localization machinery.

## Ranking Basis

- Mathematical importance: the quantum-group prerequisite chain now has Lie/Hopf and root/weight pages; the quiver-Hecke side is the weakest remaining parent topic.
- Current page weakness: `quiver-hecke-algebras` is definition-ready, but it still needs a slower worked example and a canonical-source normalization check before study-ready.
- Dependency value: a stronger quiver-Hecke prerequisite would support determinantial modules, monoidal categorification, quiver-Hecke localization, and localized crystals.
- Source availability: Brundan 2013 has been downloaded and ingested; Khovanov-Lauda 2009, Rouquier 2011, and Kang-Kashiwara-Kim 2018 have legitimate arXiv records; KL09 and KR10 also have user-provided local PDFs.
- Hallucination risk: do not add more relations, examples, or symmetric quiver-Hecke notation without a source-location-specific pass.

<!-- NEEDS-HUMAN-REVIEW -->

Keep future work focused on prerequisite exposition and small source-backed examples.
