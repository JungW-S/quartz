# Ordinary PBW Parametrization Prerequisite Review

Date: 2026-06-04

## Scope

This is a report-only review for deciding whether ordinary PBW parametrization should become a separate prerequisite before adding examples or proof-level background to `Localized PBW Parametrizations`.

Files inspected:

- `content/topics/08-localization-of-categories/localized-pbw-parametrizations.md`
- `reports/reviews/2026-06-04-localized-pbw-parametrizations-source-location-review.md`
- `content/topics/02-crystal-bases/string-parametrizations-of-demazure-crystals.md`
- `content/topics/01-quantum-groups/quantum-coordinate-rings.md`
- `content/topics/01-quantum-groups/quantum-unipotent-coordinate-rings.md`
- `content/sources/papers/gls11-cluster-structures-quantum-coordinate-rings.md`
- `data/topic_maturity.yml`
- `data/research_queue.yml`
- `reports/roadmap/next-actions.md`

No paper was downloaded. No topic page, claim, example, theorem statement, source note, Sage code, image, or new topic was added.

## Verdict

Yes. Ordinary PBW parametrization should become a separate prerequisite before `Localized PBW Parametrizations` receives examples, proof-level background, PBW/string comparison formulas, or localized coordinate examples.

However, it should not be created as a definition-ready page from JP25 alone. JP25 records the ordinary PBW input used for the localized construction, but it explicitly treats ordinary PBW theory as background. A safe next step is an exact source-location review for ordinary PBW parametrization using already ingested GLS11/Kashiwara-side material and, if needed, a later approved source such as Lusztig or Kimura.

## Reasoning

### 1. The localized page currently carries two mathematical layers

`Localized PBW Parametrizations` now explains both:

- ordinary PBW coordinates on \(B(w)\), read through upper global basis elements;
- the localized extension obtained by adding integer frozen directions \(P_i\).

These are different levels. The first is a coordinate-ring/basis-level construction. The second is a localized-crystal construction. Keeping both in one page is acceptable for a bounded definition, but it becomes too compressed once examples or proof-level explanations are added.

### 2. PBW is not parallel to string parametrization at the same source level

The new `String Parametrizations of Demazure Crystals` topic could be created narrowly because JP25 gives a direct recursive formula using \(\varepsilon_i\) and Kashiwara operators. That definition lives entirely in ordinary crystal language.

PBW parametrization is different. In the inspected material, JP25 defines
$$
\operatorname{PBW}_{\mathbf i}(b)
:=
\operatorname{PBW}_{\mathbf i}\bigl(G^{\mathrm{up}}(b)\bigr)
$$
for \(b\in B(w)\). This already uses:

- the upper global basis element \(G^{\mathrm{up}}(b)\);
- PBW coordinates for basis elements in the quantum unipotent coordinate-ring setting;
- the reduced-expression-dependent PBW root-vector construction.

Those ingredients are not explained in the current crystal-bases chapter.

### 3. The right parent area is quantum coordinate rings, not pure crystal bases

Ordinary string parametrization belongs naturally under `Crystal Bases` and `Demazure Crystals`, because it is extracted by crystal operators.

Ordinary PBW parametrization should instead sit near:

- `Quantum Coordinate Rings`;
- `Quantum Unipotent Coordinate Rings`;
- `Dual Canonical Bases`;
- `The Crystal B(infinity)`.

It is a bridge from basis-level labels \(b\in B(w)\) to coordinate-ring-level PBW data, not just an abstract-crystal operation.

### 4. Current prerequisite pages are not yet enough for examples

`Quantum Coordinate Rings` is definition-ready, but `Quantum Unipotent Coordinate Rings` is still stub-level. The localized PBW page also points to `Quantum Minors and Frozen Variables`, which remains a prerequisite gap for understanding frozen PBW directions.

Therefore, before visible examples are added to `Localized PBW Parametrizations`, the wiki needs either:

- a small ordinary PBW prerequisite topic with carefully reviewed source locations; or
- a stronger `Quantum Unipotent Coordinate Rings` page that explicitly contains the necessary PBW coordinate layer.

The first option is cleaner for reading order.

## Recommended Future Topic

Recommended title:

```text
PBW Parametrizations of Quantum Unipotent Coordinate Rings
```

Recommended topic id:

```text
pbw-parametrizations-of-quantum-unipotent-coordinate-rings
```

Recommended placement:

- parent topics: `quantum-unipotent-coordinate-rings`, `dual-canonical-bases`
- prerequisite topics: `quantum-coordinate-rings`, `quantum-unipotent-coordinate-rings`, `dual-canonical-bases`, `b-infinity-crystal`
- next topic: `localized-pbw-parametrizations`

This title is preferable to `PBW Parametrizations of Demazure Crystals` because the construction is not defined purely by crystal operators. The crystal label \(b\in B(w)\) is read through an upper global basis element and PBW coordinates in a quantum unipotent coordinate-ring setting.

## Safe Next Step

Before creating the topic, run an exact source-location review for ordinary PBW parametrization.

Safe review scope:

- identify whether GLS11 already gives enough precise source support for PBW root vectors and \(U_q(\mathfrak n(w))\);
- identify whether JP25 only records the map on \(B(w)\), rather than teaching ordinary PBW theory;
- decide whether a Lusztig/Kimura source must be approved before a definition-ready page can be written;
- do not add claims, examples, topic pages, source notes, Sage code, images, or theorem statements.

## What Should Stay Out For Now

Do not import into a future ordinary PBW prerequisite yet:

- localized frozen directions \(P_i\);
- JP25 Theorem 3.2 formulas;
- PBW/string comparison map \(\psi_{\mathbf i}\);
- \(g\)-vector formulas;
- the JP25 type \(A_2\) localized coordinate example;
- proof-level global-basis material;
- source-specific Lusztig notation unless the source is explicitly reviewed.

## Next Step

Recommended prompt:

```text
Review only: identify exact existing-source locations for ordinary PBW parametrization suitable for a future `PBW Parametrizations of Quantum Unipotent Coordinate Rings` prerequisite topic. Do not edit topic pages, add claims, examples, source notes, Sage code, images, or new topics.
```
