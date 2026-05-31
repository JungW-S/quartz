# Next Actions

This roadmap is advisory. It does not authorize source download, source intake, claim addition, topic rewrite, or new topic creation.

## Current Workflow State

- The 2026-06-01 global wiki review was completed and recorded at `reports/reviews/2026-06-01-global-wiki-review.md`.
- The 2026-06-01 notation audit was completed and recorded at `reports/reviews/2026-06-01-notation-audit.md`.
- The universal topic template, style guide, and audit prompts use the Korean learning-order structure.
- All 12 topic pages under `content/topics/*.md` have been migrated to the Korean learning-order structure: `개요`, `준비와 notation`, `정의` or `구성`, `기본 예시`, `핵심 관점`, `기본 성질`, `다른 topic들과의 관계`, `더 읽을 topic`, and final `Source notes`.
- A 2026-06-01 definition-completeness pass strengthened `정의` and `구성` sections where approved sources already supported complete data, relations, maps, or construction formulas.
- Follow-up correction: `cellular-crystals` now uses an explicit `정의` section rather than the construction variant, and `crystal-bases` states the abstract crystal axioms as formal conditions.
- The no-forced-completion policy now applies to every topic-page section: unsupported section bodies should remain empty or optional sections should be omitted, with gaps recorded outside reader-facing prose.
- The migration did not download sources, add claims, or add unsupported mathematical statements.
- The 2026-06-01 all-topic unsupported-content pass removed unsupported schematic examples and interpretive wording. The `기본 예시` sections in `quantum-groups`, `quantum-coordinate-rings`, `monoidal-categorification`, and `determinantial-modules` are intentionally empty until exact source-backed examples are approved.
- The determinantial-module definition-depth gap is closed: `determinantial-modules` now includes the KKOP18 Proposition 4.1 recursive construction of $M(\lambda,\mu)$.
- Remaining registry cleanup: none known after replacing the Marberg lecture candidate target with `root-systems-and-weight-lattices`.

## Single Safest Next Task

### Review intentionally empty example sections

- Action type: `existing-source expansion`
- New source required: no.
- User approval required: yes before any topic-page edits.
- Why it matters: the migrated pages now leave unsupported example content blank; exact source locations are needed before these sections can be filled.
- Likely files to inspect:
  - `content/topics/quantum-groups.md`
  - `content/topics/quantum-coordinate-rings.md`
  - `content/topics/monoidal-categorification.md`
  - `content/topics/determinantial-modules.md`
  - existing source notes for Hong-Kang 2002, GLS11, KKKO14, KKOP18, and Kashiwara-Nakashima 2025
- Expected mathematical benefit: fills blank example sections only where an approved source gives a precise safe example.
- Risk level: medium
- Exact prompt to paste:

```text
Review the intentionally empty example sections in quantum-groups, quantum-coordinate-rings, monoidal-categorification, and determinantial-modules using only already ingested source notes. Report candidate exact source locations and proposed wording only; do not edit topic pages, add claims, or download papers.
```

## Alternatives

### 1. Review the coordinate-ring notation bridge

- Action type: `human-review task`
- New source required: no.
- User approval required: yes before any topic-page edits.
- Why it matters: determinantial modules use $\mathcal C_{w,v}$, $K_0(\mathcal C_{w,v})$, and $A_{w,v}$, while quantum-coordinate-ring pages use $A_q(\mathfrak n(w))$. These should not be merged without a source-location review.
- Likely files to inspect:
  - `content/topics/determinantial-modules.md`
  - `content/topics/quantum-coordinate-rings.md`
  - `content/topics/monoidal-categorification.md`
  - `content/sources/papers/kkop18-monoidal-categories-strata-flag-manifolds.md`
  - `content/sources/papers/gls11-cluster-structures-quantum-coordinate-rings.md`
  - `data/notation.yml`
- Expected mathematical benefit: prevents object-level, Grothendieck-ring-level, and coordinate-ring-level notation from collapsing during future exposition.
- Risk level: medium
- Exact prompt to paste:

```text
Review the notation bridge between $A_{w,v}$ and $A_q(\mathfrak n(w))$ using only already ingested KKOP18 and GLS11 source material. Do not rewrite topic pages, add claims, or download papers. Produce a short decision note saying whether a later topic-page edit may add level-separated bridge prose.
```

### 2. Canonical-source cross-check for quiver-Hecke definitions

- Action type: `new-source intake`
- New source required: yes.
- User approval required: yes.
- Why it matters: the quiver-Hecke page is definition-ready from Brundan 2013, but a later cross-check against Khovanov-Lauda 2009 would reduce normalization risk before upgrading it toward reviewed.
- Likely files to change after approval:
  - `content/sources/papers/`
  - `data/sources.yml`
  - `data/claims.yml`
  - `content/topics/quiver-hecke-algebras.md`
  - `data/topic_maturity.yml`
- Expected mathematical benefit: confirms generators, relations, grading, and categorification notation against a canonical source.
- Risk level: medium
- Exact prompt to paste:

```text
I approve source candidate `khovanov-lauda09-diagrammatic-categorification-quantum-groups-i` for a canonical-source cross-check of content/topics/quiver-hecke-algebras.md. Use only the user-provided local PDF in inbox/papers2, add at most 4 claims, and do not expand beyond the definition-ready level.
```

### 3. Audit generated topic maps after hierarchy migration

- Action type: `graph cleanup`
- New source required: no.
- User approval required: no, if no topic prose is changed.
- Why it matters: the topic hierarchy and maps were regenerated after the migration; a graph-only audit can check that parent/prerequisite/related links read correctly.
- Likely files to inspect:
  - `content/maps/topic-hierarchy.md`
  - `content/maps/representation-theory-map.md`
  - `content/maps/crystal-bases-map.md`
  - `content/maps/quiver-hecke-algebras-map.md`
  - `data/topics.yml`
  - `data/edges.yml`
- Expected mathematical benefit: keeps study navigation coherent after the page-structure migration.
- Risk level: low
- Exact prompt to paste:

```text
Run a graph-only audit of generated topic maps and hierarchy metadata. Do not rewrite topic pages, add claims, or download sources. Report inconsistent parent/prerequisite/related-topic links and update data/review_backlog.yml if needed.
```

## Ranking Basis

- Mathematical importance: real examples are now the main remaining readability gap after the learning-order migration.
- Current page weakness: topic pages now share the same learning-order shape; the largest remaining prose gaps are intentionally empty example sections that require source-location review.
- Dependency value: better examples improve undergraduate study paths without changing definitions.
- Source availability: existing ingested sources may contain suitable examples, but exact locations must be checked.
- Hallucination risk: the recommended task is report-only and forbids page edits or claim additions.

<!-- NEEDS-HUMAN-REVIEW -->

Keep future work focused on small, source-backed topic improvements and clearly recorded gaps.
