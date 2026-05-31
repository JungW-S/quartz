# 2026-06-01 Notation Audit

## Scope

This audit checked reader-facing topic pages, source notes, the notation registry, maturity metadata, and the review backlog. No topic pages were rewritten, no claims were added, and no papers were downloaded.

## Searches Run

- Deprecated raw forms: `Cw,v`, `Aw,v`, `K0(Cw,v)`, `K0(`, `K(\mathcal C)`, `M(w<=k Lambda, v<=k Lambda)`, `R-gmod`, `q commuting`
- Grothendieck-ring forms: `K(\mathcal C)`, `K0(`, `K_0(C`
- Coordinate-ring bridge terms: `$A_{w,v}$`, `$A_q(\mathfrak n(w))$`, `$K_0(\mathcal C_{w,v})$`, `$\mathcal C_{w,v}$`
- Crystal and localization operators: `\widetilde e_i`, `\widetilde f_i`, `\widetilde E_i`, `\widetilde F_i`

## Summary

- No deprecated raw notation was found in reader-facing topic pages.
- Source-specific notation such as `K(\mathcal C)` appears only in the notation glossary and source notes where it is explicitly marked as source notation.
- Grothendieck-ring notation is normalized in topic prose as $K_0(\mathcal C)$ or $K_0(\mathcal C_{w,v})$.
- Ordinary crystal operators $\widetilde e_i,\widetilde f_i$ and localized-category operators $\widetilde E_i,\widetilde F_i$ remain distinguishable.
- The main notation-sensitive risk remains the cross-source bridge between $A_{w,v}$ and $A_q(\mathfrak n(w))$.

## Findings

### No Raw Deprecated Notation In Topic Pages

Reader-facing topic pages did not contain raw forms such as `Cw,v`, `Aw,v`, `K0(Cw,v)`, `M(w<=k Lambda, v<=k Lambda)`, `R-gmod`, or `q commuting`.

The raw strings occur only as audit patterns or translation examples in:

- `data/notation.yml`
- `content/glossary/notation.md`
- `content/topics/AGENTS.md`
- `content/sources/papers/kkko14-monoidal-categorification-cluster-algebras.md`

Proposed fix: none. Keep these raw strings in registry and source-translation contexts so later audits can detect them.

### Source-Specific Grothendieck Notation Is Contained

`K(\mathcal C)` appears in the KKKO14 source note and glossary as source notation. Topic pages use $K_0(\mathcal C)$ or $K_0(\mathcal C_{w,v})$.

Proposed fix: none. Continue using $K_0(\mathcal C)$ in topic prose and reserve `K(\mathcal C)` for source notes.

### Coordinate-Ring Target Comparison Remains Review-Sensitive

The topic pages do not identify $A_{w,v}$ with $A_q(\mathfrak n(w))$. The current pages keep the levels separated:

- `determinantial-modules.md` separates module objects, Grothendieck classes, and $A_{w,v}$.
- `quantum-coordinate-rings.md` treats $A_q(\mathfrak n(w))$ as the GLS11 quantum coordinate-ring target.
- `monoidal-categorification.md` cites the KKOP18 and GLS11 source notes separately.

This is correct for the current page state, but future expansion could easily collapse source-specific coordinate-ring notation.

Proposed fix: keep `review-2026-05-31-determinantial-quantum-minor-bridge` open. Before adding bridge prose, review KKOP18 Theorem 2.20(ii)(c) and GLS11 Theorem 12.3 together, and write any comparison with explicit object-level, Grothendieck-ring-level, and coordinate-ring-level separation.

### KLR Category Notation Is Controlled

`quiver-hecke-algebras.md` uses Brundan's $H_\alpha$ for the definition and explains that later advanced pages use $R\text{-gmod}$ generically. No raw `R-gmod` appeared in reader-facing topic pages.

Proposed fix: no immediate edit. If the Khovanov-Lauda normalization cross-check is later approved, review $H_\alpha$, $R(\beta)$, and $R\text{-gmod}$ naming before adding examples.

### Crystal Tensor Convention Is Still Properly Flagged

Crystal pages use ordinary Kashiwara operators $\widetilde e_i,\widetilde f_i$, while localized crystal pages use $\widetilde E_i,\widetilde F_i$ for category-level operators. The notation registry and glossary still record that Schilling/SageMath tensor-product formulas must be translated before use.

Proposed fix: no immediate edit. Keep the existing Schilling/Sage convention warning in place for future source intake.

## Backlog Updates

- Linked `review-2026-05-31-determinantial-quantum-minor-bridge` to this report.

## Recommended Next Action

Perform a human-review task for the $A_{w,v}$ versus $A_q(\mathfrak n(w))$ bridge before any topic-page expansion involving determinantial modules, quantum minors, or quantum coordinate rings.
