# $\mathcal C_w$ and $\mathcal C_{w,v}$ Definition Verification

Date: 2026-06-01

## Scope

This report verifies the exact source locations and safe later wording for the definitions of $\mathcal C_w$, $\mathcal C_{*,v}$, $\mathcal C_{w,v}$, and the localization input $\widetilde{\mathcal C}_w$.

No topic pages were edited. No claims were added. No sources were downloaded.

## Sources Checked

- KKOP18, `Monoidal Categories Associated with Strata of Flag Manifolds`, local TeX source:
  `inbox/papers2/Tex/KKOP18, Monoidal categories associated with strata of flag manifolds, Adv Math, arxiv ver/source.tex`.
- Kashiwara-Nakashima 2025, `Crystal Structure of Localized Quantum Unipotent Coordinate Category`, local TeX source:
  `inbox/papers/crystal.tex`.

## Verified Definition Data

KKOP18 defines the auxiliary sets, for an $R(\beta)$-module $M$,

$$
\mathsf W(M)=\{\gamma\in Q_+\cap(\beta-Q_+)\mid e(\gamma,\beta-\gamma)M\ne0\},
$$

and

$$
\mathsf W^*(M)=\{\gamma\in Q_+\cap(\beta-Q_+)\mid e(\beta-\gamma,\gamma)M\ne0\}.
$$

The same notation is repeated in Kashiwara-Nakashima 2025, Section 5.1.

KKOP18 defines $\mathcal C_w$ as a full subcategory of $R\text{-gmod}$ by the cone condition

$$
\mathsf W(M)\subset \operatorname{Cone}(\Delta_+\cap w\Delta_-).
$$

It defines $\mathcal C_{*,v}$ by

$$
\mathsf W^*(M)\subset \operatorname{Cone}(\Delta_+\cap v\Delta_+).
$$

It then records the equivalent lattice conditions

$$
M\in\mathcal C_w
\Longleftrightarrow
\mathsf W(M)\subset Q_+\cap wQ_-,
$$

and

$$
M\in\mathcal C_{*,v}
\Longleftrightarrow
\mathsf W^*(M)\subset Q_+\cap vQ_+.
$$

Finally, KKOP18 defines $\mathcal C_{w,v}$ as the full subcategory of $R\text{-gmod}$ whose objects lie in both $\mathcal C_w$ and $\mathcal C_{*,v}$.

Kashiwara-Nakashima 2025 uses the equivalent lattice version for $\mathcal C_w$:

$$
\mathcal C_w=\{M\in R\text{-gmod}\mid \mathsf W(M)\subset Q_+\cap wQ_-\}.
$$

This is consistent with the equivalence stated in KKOP18.

## Verified Properties

KKOP18 Proposition 2.16 states that $\mathcal C_w$, $\mathcal C_{*,v}$, and $\mathcal C_{w,v}$ are stable under subquotients, extensions, convolution products, and grading shifts. Hence their Grothendieck groups are $\mathbb Z[q,q^{-1}]$-algebras.

KKOP18 Theorem 2.20 identifies, under the Grothendieck-ring isomorphism $K_0(R\text{-gmod})\simeq A_q(\mathfrak n)$,

$$
K_0(\mathcal C_w)=A_w,\qquad
K_0(\mathcal C_{*,v})=A_{*,v},\qquad
K_0(\mathcal C_{w,v})=A_{w,v}.
$$

Kashiwara-Nakashima 2025 Section 5.2 uses $\mathcal C_w$ as the input category for the localization $\Phi_w:\mathcal C_w\to\widetilde{\mathcal C}_w$ by the real commuting family of determinantial-module left braiders attached to $\mathsf M(w\Lambda_i,\Lambda_i)$.

## Source Locations

| Item | Source location |
| --- | --- |
| Definitions of $\mathsf W(M)$ and $\mathsf W^*(M)$ | KKOP18 introduction lines 488-492; KKOP18 Definition lines 1470-1476; KN25 Section 5.1 lines 2821-2826 |
| Definition of $\mathcal C_w$ | KKOP18 Section 2.2 lines 1888-1891; equivalent condition lines 1905-1911; KN25 Section 5.1 lines 2835-2841 |
| Definition of $\mathcal C_{*,v}$ | KKOP18 Section 2.2 lines 1892-1895; equivalent condition lines 1905-1911 |
| Definition of $\mathcal C_{w,v}$ | KKOP18 Section 2.2 lines 1915-1916 |
| Stability of the subcategories | KKOP18 Proposition 2.16, lines 1918-1922 |
| Grothendieck-ring comparison | KKOP18 Theorem 2.20, lines 2076-2110 |
| Localization input $\mathcal C_w\to\widetilde{\mathcal C}_w$ | KN25 Section 5.2 lines 2870-2902; Theorem 5.3 lines 2907-2917 |

## Proposed Later Topic Wording

The following wording is safe for a later approved edit of `content/topics/quiver-hecke-subcategories.md`. It is not applied in this report-only pass.

```markdown
`$\mathcal C_w$`는 Weyl group 원소 `$w$`에 붙는 `$R\text{-gmod}$`의 full monoidal subcategory이다. `$M\in R(\beta)\text{-gmod}$`에 대해

$$
\mathsf W(M)=\{\gamma\in Q_+\cap(\beta-Q_+)\mid e(\gamma,\beta-\gamma)M\ne0\}
$$

로 둔다. 또

$$
\mathsf W^*(M)=\{\gamma\in Q_+\cap(\beta-Q_+)\mid e(\beta-\gamma,\gamma)M\ne0\}
$$

로 둔다. Kashiwara-Nakashima 2025와 KKOP18의 동치 조건에 따라

$$
\mathcal C_w=\{M\in R\text{-gmod}\mid \mathsf W(M)\subset Q_+\cap wQ_-\}
$$

이다. KKOP18의 원래 정의는 같은 조건을 positive-root cone
`$\operatorname{Cone}(\Delta_+\cap w\Delta_-)$`로 표현한다.

마찬가지로

$$
\mathcal C_{*,v}=\{M\in R\text{-gmod}\mid \mathsf W^*(M)\subset Q_+\cap vQ_+\}
$$

이고, `$\mathcal C_{w,v}$`는 `$\mathcal C_w$`와 `$\mathcal C_{*,v}$`에 동시에 속하는 object들로 이루어진 full subcategory이다.
```

For `content/topics/quiver-hecke-category-localization.md`, a later approved edit may say that $\widetilde{\mathcal C}_w$ is the localization of $\mathcal C_w$ by the real commuting family of determinantial-module left braiders attached to $\mathsf M(w\Lambda_i,\Lambda_i)$, with $\Phi_w$ denoting the localization functor.

## Remaining Gap

The source-location gap is closed. The topic page `content/topics/quiver-hecke-subcategories.md` has not yet been updated, so its maturity should remain below `definition-ready` until the verified definition is applied in a separate approved topic-page edit.
