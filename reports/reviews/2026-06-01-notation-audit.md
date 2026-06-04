# 2026-06-01 Notation Audit

This report is advisory. It does not authorize source download, source intake, claim additions, or topic-page rewrites.

This is a same-day follow-up notation audit after the `crystal.tex` topic-slot work and the localized-operator topic expansions. No topic pages were rewritten, no claims were added, and no papers were downloaded.

## Scope

Reviewed:

- `content/glossary/notation.md`
- `data/notation.yml`
- reader-facing topic pages under `content/topics/`
- source notes under `content/sources/`
- maturity metadata in `data/topic_maturity.yml`
- review backlog and roadmap entries
- recent review reports that introduce Kashiwara-Nakashima 2025 notation

## Searches Run

- Deprecated raw forms: `Cw,v`, `Aw,v`, `K0(Cw,v)`, `K0(`, `K(\mathcal C)`, `M(w<=k Lambda, v<=k Lambda)`, `R-gmod`, `q commuting`
- Grothendieck-ring forms: `K(\mathcal C)`, `K0(`, `K_0(C`
- Coordinate-ring bridge terms: `$A_{w,v}$`, `$A_q(\mathfrak n(w))$`, `$K_0(\mathcal C_{w,v})$`, `$\mathcal C_{w,v}$`
- Crystal and localization operators: `\widetilde e_i`, `\widetilde f_i`, `\widetilde E_i`, `\widetilde F_i`
- Kashiwara-Nakashima source macros and local aliases: `\tCw`, `\Irr(\tCw)`, `\Bw`, `\CBw`, `\mathcal C_{\mathcal B_w}`
- New localized-category notation: `\widetilde Q_i`, `\mathsf d_i`, `\widetilde\Lambda`, `\mathfrak d`, `\nabla`, `\Phi_w`, `\operatorname{CP}`, `\psi_*`

## Summary

- No deprecated raw notation was found in reader-facing topic pages.
- Source-specific shorthand such as `K(\mathcal C)`, `Cw,v`, `K0(Cw,v)`, `Aw,v`, and `\tCw` appears only in glossary, registry, policy, source-note, or report contexts.
- The coordinate-ring bridge between $A_{w,v}$ and $A_q(\mathfrak n(w))$ remains separated in topic prose.
- The unsupported alias $\mathcal C_{\mathcal B_w}$ no longer appears in reader-facing topic pages; it remains only in older review reports that document the correction.
- New issue: `content/topics/08-localization-of-categories/localized-crystals.md` still uses older operator formula notation that is not aligned with `content/topics/08-localization-of-categories/localized-root-operators.md`.
- New issue: `data/notation.yml` and `content/glossary/notation.md` do not yet cover several Kashiwara-Nakashima 2025 symbols now used by topic pages.

## Findings

### High: Localized Crystals uses older localized-operator notation

File involved:

- `content/topics/08-localization-of-categories/localized-crystals.md`

Issue: the `Localized Crystals` construction section still uses older shorthand:

- `$d_i$` for the scalar root-direction degree, while `Localized Root Operators` uses $\mathsf d_i$;
- `$d_i(X)$` and `$d(\widetilde Q_i,X)$`, which blur the scalar $\mathsf d_i$ with the function $d_i(X)$ and the R-matrix invariant $\mathfrak d$;
- `$\Lambda(\widetilde Q_i,X)$` and `$\Lambda(X,\widetilde Q_i)$`, while the dedicated operator page uses the localized modified degree $\widetilde\Lambda$;
- `$D\widetilde Q_i$`, while newer localized-category pages use the duality functor $\mathscr D$;
- `$q^{\varepsilon_i(X)}$`, while the operator page uses $q_i^{\varepsilon_i(X)}$.

Proposed fix: in a separately approved topic-page edit, align `Localized Crystals` with `Localized Root Operators` by using $\mathsf d_i$, $\widetilde\Lambda$, $\mathfrak d$, $\mathscr D$, and $q_i$ in the setup and construction formulas. Do not add new claims; this is a notation-normalization edit using already reviewed source locations and the existing child topic page.

Requires new source: no.

Requires user approval: yes, before topic-page edits.

Backlog id: `review-2026-06-01-localized-crystals-operator-notation-normalization`.

### Medium: Kashiwara-Nakashima notation registry coverage is incomplete

Files involved:

- `data/notation.yml`
- `content/glossary/notation.md`
- topic pages using Kashiwara-Nakashima 2025 notation

Issue: the topic pages now use several source-sensitive symbols that are not yet represented in the notation registry or public notation glossary:

- $\mathfrak B_w$ for the Demazure subcategory;
- $\widetilde Q_i$ for localized simple-root objects;
- $\mathsf d_i$, $\widetilde\Lambda$, and $\mathfrak d$ for localized R-matrix degree data;
- $\nabla$ for simple heads of convolution products;
- $\Phi_w$ for the localization functor;
- $\operatorname{CP}$ for the comparison map;
- $\psi_*$ for the reverse monoidal equivalence.

Proposed fix: add registry/glossary entries before further Kashiwara-Nakashima topic expansion. The entries should be translation guides only; they should not add theorem-level content or change topic pages.

Requires new source: no.

Requires user approval: no for registry/glossary documentation; yes before topic-page edits.

Backlog id: `review-2026-06-01-kn25-notation-registry-coverage`.

### Medium: Coordinate-ring bridge remains review-sensitive

Files involved:

- `content/topics/06-quiver-hecke-klr-algebras/determinantial-modules.md`
- `content/topics/06-quiver-hecke-klr-algebras/quiver-hecke-subcategories.md`
- `content/topics/01-quantum-groups/quantum-coordinate-rings.md`
- `content/topics/05-monoidal-categorification/monoidal-categorification.md`
- `data/review_backlog.yml`

Issue: topic pages correctly keep the levels separated:

- module objects live in $\mathcal C_{w,v}$;
- classes live in $K_0(\mathcal C_{w,v})$;
- $A_{w,v}$ is the KKOP18 coordinate-ring-side comparison target;
- $A_q(\mathfrak n(w))$ is the GLS11 quantum coordinate-ring target.

The risk is future prose that might identify $A_{w,v}$ with $A_q(\mathfrak n(w))$ without a reviewed comparison.

Proposed fix: keep `review-2026-05-31-determinantial-quantum-minor-bridge` open. Before adding bridge prose, review KKOP18 Theorem 2.20(ii)(c) and GLS11 Theorem 12.3 together, and write any comparison with explicit object-level, Grothendieck-ring-level, and coordinate-ring-level separation.

Requires new source: no.

Requires user approval: yes, before topic-page edits.

Backlog id: `review-2026-05-31-determinantial-quantum-minor-bridge`.

### Low: Deprecated raw notation is contained

Reader-facing topic pages did not contain raw forms such as `Cw,v`, `Aw,v`, `K0(Cw,v)`, `M(w<=k Lambda, v<=k Lambda)`, `R-gmod`, `q commuting`, `\tCw`, or `\Bw`.

The raw strings occur only as audit patterns, glossary warnings, source translation notes, policy examples, registry entries, or historical review-report references.

Proposed fix: none for topic pages. Keep raw strings in registry and audit contexts so future scans can detect them.

### Low: Demazure notation alias remains only as archival review text

The unsupported alias $\mathcal C_{\mathcal B_w}$ does not appear in reader-facing topic pages. It remains in older source-location reports that document why the page now uses $\mathfrak B_w$.

Proposed fix: no topic-page edit. When adding notation-registry coverage, add $\mathfrak B_w$ as the canonical reader-facing form and record $\mathcal C_{\mathcal B_w}$ as a deprecated local alias to avoid reintroducing it.

## Backlog Updates

- Added `review-2026-06-01-localized-crystals-operator-notation-normalization`.
- Added `review-2026-06-01-kn25-notation-registry-coverage`.
- Kept `review-2026-05-31-determinantial-quantum-minor-bridge` open.
- Marked the refreshed notation audit itself as done.

## Validation

- `git diff --check`: passed.
- `python3 scripts/run_all_checks.py`: passed, including frontmatter, claims, topics, edges, generated maps, generated topic status, link validation, and the internal Quartz build over 51 content files.
- `npx quartz build`: failed with the known standalone Node heap out-of-memory failure. The Quartz build inside `run_all_checks.py` passed.
