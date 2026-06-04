# Ordinary String Parametrization Prerequisite Review

Date: 2026-06-04

## Scope

This is a report-only review for deciding whether ordinary string parametrization should become a separate prerequisite before adding examples or proof-level background to `Localized String Parametrizations`.

Files inspected:

- `content/topics/08-localization-of-categories/localized-string-parametrizations.md`
- `reports/reviews/2026-06-04-localized-string-parametrizations-source-location-review.md`
- `content/topics/02-crystal-bases/index.md`
- `content/topics/02-crystal-bases/abstract-crystals.md`
- `content/topics/02-crystal-bases/demazure-crystals.md`
- `data/topic_maturity.yml`
- `data/research_queue.yml`
- `reports/roadmap/next-actions.md`

No paper was downloaded. No topic page, claim, example, theorem statement, source note, Sage code, image, or new topic was added.

## Verdict

Yes. Ordinary string parametrization should become a separate prerequisite topic before `Localized String Parametrizations` receives examples or proof-level background.

The localized page can stay `definition-ready` as a bounded JP25-backed construction, but it should not be made `example-ready` or `study-ready` until readers can first learn the ordinary string-coordinate construction outside the localized setting.

## Reasoning

### 1. The localized page currently carries two constructions

`Localized String Parametrizations` now has to explain both:

- ordinary string coordinates on the non-localized crystal \(B(w)\);
- the extension to the localized crystal \(\mathcal B(w)\) by adding frozen integer directions.

These are different conceptual levels. The first is ordinary crystal-level coordinate theory. The second is localized-crystal coordinate theory. Keeping both in one page is acceptable for a bounded definition, but it becomes too dense once examples, proof background, or PBW/string comparison are added.

### 2. The ordinary construction is a reusable prerequisite

The ordinary recursive definition
$$
t_k
=
\varepsilon_{i_k}
\bigl(
\widetilde e_{i_{k-1}}^{t_{k-1}}
\cdots
\widetilde e_{i_1}^{t_1}(b)
\bigr)
$$
uses only ordinary crystal language, a reduced expression, and the crystal \(B(w)\). This should be learned after `Abstract Crystals`, `The Crystal B(infinity)`, and `Demazure Crystals`, before localized frozen directions are introduced.

### 3. Examples need the ordinary layer first

The JP25 type \(A_2\) coordinate example involves ordinary PBW/string coordinates, frozen directions, \(g\)-vectors, and twist formulas. If ordinary string coordinates are not readable first, that example will read like a list of formulas rather than a study example.

### 4. The current crystal-bases chapter has no slot for this

The `Crystal Bases` shelf currently goes:

1. `Crystal Bases`
2. `Abstract Crystals`
3. `Tensor Products of Crystals`
4. `Highest Weight Crystals`
5. `The Crystal B(infinity)`
6. `Demazure Crystals`
7. `Cellular Crystals`

There is no ordinary coordinate-parametrization topic between `Demazure Crystals` and the advanced cellular/localized pages. That is exactly where ordinary string parametrization belongs.

## Recommended Future Topic

Recommended title:

```text
String Parametrizations of Demazure Crystals
```

Recommended topic id:

```text
string-parametrizations-of-demazure-crystals
```

Recommended placement:

- parent topics: `crystal-bases`, `demazure-crystals`
- prerequisite topics: `abstract-crystals`, `b-infinity-crystal`, `demazure-crystals`
- child or next topic: `localized-string-parametrizations`

Recommended initial maturity:

- `definition-ready` if the next pass uses only the already reviewed JP25 lines plus existing Kashiwara/Hong-Kang source notes for ordinary crystal notation;
- otherwise `orientation` if exact ordinary-source locations are reviewed first but not imported.

## Safe Initial Scope

A first topic page should explain only:

- why a reduced expression \(\mathbf i=(i_1,\ldots,i_m)\) is fixed;
- how \(\varepsilon_i\) and the Kashiwara operators extract string coordinates;
- what the coordinate tuple \((t_1,\ldots,t_m)\) records;
- why the construction depends on the reduced expression;
- how this ordinary coordinate system prepares localized string parametrization.

It should not include:

- JP25 Theorem 3.2 formulas;
- PBW/string comparison formulas;
- \(g\)-vector formulas;
- the type \(A_2\) localized coordinate example;
- proof of bijectivity;
- Sage-generated or hand-generated examples.

## Next Step

Create the new prerequisite topic only after explicit approval for new topic creation. The safest next implementation task is small: create the topic at reader-facing definition level, update hierarchy metadata, and keep the example section empty unless a source-verified ordinary example is selected.

Recommended prompt:

```text
Create the prerequisite topic `String Parametrizations of Demazure Crystals` using only already ingested sources and the existing JP25 source-location review. Do not add claims, examples, theorem statements, Sage code, images, or proof-level background. Update hierarchy, maturity, research queue, and roadmap.
```
