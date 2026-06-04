# Ordinary PBW Source-Location Review

Date: 2026-06-04

## Scope

This is a report-only source-location review for a future prerequisite topic:

```text
PBW Parametrizations of Quantum Unipotent Coordinate Rings
```

Files inspected:

- `reports/reviews/2026-06-04-ordinary-pbw-parametrization-prerequisite-review.md`
- `reports/reviews/2026-06-04-localized-pbw-parametrizations-source-location-review.md`
- `content/sources/papers/gls11-cluster-structures-quantum-coordinate-rings.md`
- `content/sources/papers/jp25-crystals-quantum-twist-automorphisms.md`
- `content/topics/01-quantum-groups/quantum-coordinate-rings.md`
- `content/topics/01-quantum-groups/quantum-unipotent-coordinate-rings.md`
- `data/source_candidates.yml`

Local source text inspected:

- `content/assets/pdfs/gls11-cluster-structures-quantum-coordinate-rings.pdf`, pp. 11-12 and 21-23 via local PDF text extraction.
- `inbox/papers2/Tex/JP25, Crystals and quantum twist automorphisms, arXiv/CT.tex`, lines 1559-1596.

No paper was downloaded. No topic page, claim, source note, example, theorem statement, Sage code, image, or new topic was added.

## Verdict

Existing sources are enough for an orientation-level prerequisite explaining:

- \(A_q(\mathfrak n)\) and \(A_q(\mathfrak n(w))\);
- Lusztig quantum root vectors \(E(\beta_k)\);
- the PBW basis \(\mathcal P_{\mathbf i}\) of \(U_q(\mathfrak n(w))\);
- the dual PBW basis \(\mathcal P_{\mathbf i}^*\) identified with a basis of \(A_q(\mathfrak n(w))\);
- the fact that JP25 uses ordinary PBW coordinates of \(G^{\mathrm{up}}(b)\) for \(b\in B(w)\).

Existing sources are not enough for a definition-ready ordinary PBW parametrization page that fully explains the map
$$
\operatorname{PBW}_{\mathbf i}:B(w)\to \mathcal P_{\mathbf i}(w)
$$
as a bijection from crystal labels to nonnegative PBW coordinate data. JP25 records this map but cites Lusztig, Chapter 40, for the ordinary PBW parametrization. GLS11 gives the PBW basis/root-vector layer but not a beginner-facing derivation of the crystal-label parametrization.

## Exact Existing Source Locations

### Coordinate-ring ambient object

- GLS11 Section 4.2, pp. 11-12: defines \(A_q(\mathfrak n)\) as the graded dual of \(U_q(\mathfrak n)\) and gives its multiplication.
- GLS11 Proposition 4.1, p. 12: records that
  $$
  \Psi:U_q(\mathfrak n)\to A_q(\mathfrak n)
  $$
  is an algebra isomorphism.

These locations support the ambient coordinate-ring side used before defining \(A_q(\mathfrak n(w))\).

### Quantum root vectors and PBW basis

- GLS11 Section 7.1, p. 21: fixes \(w\), defines \(\Delta_w^+\), and introduces the quantum unipotent subgroup direction.
- GLS11 Section 7.1, pp. 21-22: introduces Lusztig braid group operators \(T_i\), fixes a reduced decomposition \(w=s_{i_r}\cdots s_{i_1}\), defines
  $$
  \beta_k=s_{i_1}\cdots s_{i_{k-1}}(\alpha_{i_k}),
  \qquad
  E(\beta_k)=T_{i_1}\cdots T_{i_{k-1}}(e_{i_k}),
  $$
  and defines
  $$
  E(a)=E(\beta_1)^{(a_1)}\cdots E(\beta_r)^{(a_r)}.
  $$
- GLS11 Section 7.1, p. 22: records that the span of the \(E(a)\) is independent of the reduced word and is denoted \(U_q(\mathfrak n(w))\); it also names
  $$
  \mathcal P_{\mathbf i}:=\{E(a)\mid a\in\mathbb N^r\}
  $$
  as the PBW basis attached to \(\mathbf i\).

These locations support an orientation-level definition of the PBW basis attached to a reduced expression.

### Quantum unipotent coordinate ring and dual PBW basis

- GLS11 Section 7.2, p. 23: defines
  $$
  A_q(\mathfrak n(w)):=\Psi(U_q(\mathfrak n(w)))
  $$
  as a subalgebra of \(A_q(\mathfrak n)\).
- GLS11 Section 7.2, p. 23: records orthogonality of the PBW basis and defines the dual PBW basis
  $$
  E^*(a)=\frac{1}{(E(a),E(a))}E(a),
  \qquad a\in\mathbb N^r,
  $$
  which is identified via \(\Psi\) with the basis of \(A_q(\mathfrak n(w))\) dual to the PBW basis.

These locations support the coordinate-ring-level PBW/dual PBW basis layer.

### Ordinary PBW input used by JP25

- JP25 `CT.tex:1559-1563`: fixes a reduced expression
  $$
  \mathbf i=(i_1,\ldots,i_m)\in R(w)
  $$
  and announces PBW and string parametrizations of the localized crystal.
- JP25 `CT.tex:1569-1573`: for \(b\in B(w)\), defines
  $$
  \operatorname{PBW}_{\mathbf i}(b)
  :=
  \operatorname{PBW}_{\mathbf i}(G^{\mathrm{up}}(b))
  $$
  and records the bijective map
  $$
  \operatorname{PBW}_{\mathbf i}:B(w)\to \mathcal P_{\mathbf i}(w),
  \qquad
  \mathcal P_{\mathbf i}(w)\subset\mathbb Z_{\ge0}^{[1,m]}.
  $$
  JP25 cites Lusztig, Chapter 40, for this ordinary PBW parametrization.

This is the exact JP25 location for the ordinary PBW input. It is safe to cite as “JP25 uses this ordinary PBW parametrization,” but not as a standalone source for teaching ordinary PBW theory.

### Localized layer to exclude from the ordinary prerequisite

- JP25 `CT.tex:1575-1596`: defines frozen PBW vectors \(P_j\), extends the coordinate map to \(\mathcal B(w)\), defines \(\widetilde{\mathcal P}_{\mathbf i}(w)\), and names the localized PBW parametrization.

This belongs to `Localized PBW Parametrizations`, not the ordinary prerequisite.

## What Existing Sources Can Support

An orientation-only future topic can safely explain:

- why reduced expressions produce ordered quantum roots \(\beta_k\);
- how Lusztig quantum root vectors \(E(\beta_k)\) give monomials \(E(a)\);
- that GLS11 calls the resulting set a PBW basis of \(U_q(\mathfrak n(w))\);
- how \(\Psi\) moves this basis layer to \(A_q(\mathfrak n(w))\);
- that JP25 reads \(b\in B(w)\) through \(G^{\mathrm{up}}(b)\) and then through PBW coordinates.

This would be useful as an orientation page, but it should not claim to fully prove or develop ordinary PBW parametrization.

## What Existing Sources Do Not Yet Support

The current ingested sources do not safely support:

- a full definition-ready treatment of the bijection \(B(w)\to\mathcal P_{\mathbf i}(w)\);
- a proof or explanation of nonnegativity of the PBW coordinate image \(\mathcal P_{\mathbf i}(w)\);
- a beginner-facing account of how upper global basis elements expand in the PBW basis;
- a concrete ordinary PBW example;
- frozen PBW vector formulas beyond the JP25 recorded fact.

For these, the future workflow should evaluate or approve an exact ordinary PBW source. JP25 points to Lusztig, Chapter 40. The existing `kimura10-quantum-unipotent-subgroup-dual-canonical-basis` candidate may also be relevant, but it is not ingested and cannot yet support claims.

## Recommendation

Do not create a definition-ready `PBW Parametrizations of Quantum Unipotent Coordinate Rings` page yet.

Two safe options remain:

1. Create only an orientation page using GLS11 Sections 4.2, 7.1, 7.2 and JP25 lines 1569-1573, with the exact limitation that ordinary PBW parametrization is recorded but not developed.
2. First evaluate a Lusztig/Kimura source for the ordinary PBW parametrization and then create a definition-ready prerequisite page.

The second option is mathematically better if the goal is to make `Localized PBW Parametrizations` genuinely readable before localized examples.

## Next Step

Recommended prompt:

```text
Evaluate a focused source for ordinary PBW parametrization, preferably Lusztig Chapter 40 or Kimura's quantum unipotent subgroup source, before creating `PBW Parametrizations of Quantum Unipotent Coordinate Rings`. Do not download or ingest until the exact source is approved or already legally available.
```
