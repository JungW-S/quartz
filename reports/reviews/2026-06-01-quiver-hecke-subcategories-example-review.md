# Quiver-Hecke Subcategories Example Review

Date: 2026-06-01

## Scope

This report reviews whether `content/topics/06-quiver-hecke-klr-algebras/quiver-hecke-subcategories.md` can safely add a real source-backed example or non-example of $\mathcal C_w$ or $\mathcal C_{w,v}$.

Only already ingested KKOP18 and Kashiwara-Nakashima 2025 material was checked. No topic pages were edited. No claims were added. No sources were downloaded.

## Sources Checked

- KKOP18, `Monoidal Categories Associated with Strata of Flag Manifolds`, local TeX source:
  `inbox/papers2/Tex/KKOP18, Monoidal categories associated with strata of flag manifolds, Adv Math, arxiv ver/source.tex`.
- Kashiwara-Nakashima 2025, `Crystal Structure of Localized Quantum Unipotent Coordinate Category`, local TeX source:
  `inbox/papers/crystal.tex`.

## Candidate Examples

### 1. Preferred basic example: $\mathcal C_w=R\text{-gmod}$ in type $A_2$

Kashiwara-Nakashima 2025 gives a simple type $A_2$ case:

$$
w=s_1s_2s_1
\quad\Longrightarrow\quad
\mathcal C_w=R\text{-gmod}.
$$

This is the safest first example for the topic page because it uses only the already introduced notation $\mathcal C_w$ and $R\text{-gmod}$, and it shows an extreme case where the subcategory is the whole ambient module category.

Source location: KN25 local TeX lines 3990-3995.

### 2. Useful non-example: a natural object not lying in $\mathcal C_w$

Kashiwara-Nakashima 2025 also gives a type $A_2$ non-example. For

$$
w=s_1s_2,\qquad \lambda=s_1\Lambda_1,
$$

the source states that

$$
\mathsf M_w(w\lambda,\lambda)\simeq \langle 2\rangle
\notin \mathcal C_w,
$$

because $\alpha_2\notin \Delta_+\cap w\Delta_-$.

This is useful because it shows that a natural determinantial-style object need not belong to $\mathcal C_w$. It is less suitable as the first example than Candidate 1 because it requires explaining the source's $\langle 2\rangle$ and $\mathsf M_w$ notation.

Source location: KN25 local TeX lines 2858-2866.

### 3. $\mathcal C_{w,v}$ family example from determinantial modules

KKOP18 gives a reusable family of objects in $\mathcal C_{w,v}$. For $v\le w$, a dominant integral weight $\Lambda$, and a fixed reduced expression

$$
w=s_{i_1}\cdots s_{i_\ell},
$$

the determinantial modules

$$
M(w_{\le k}\Lambda,v_{\le k}\Lambda)
$$

lie in $\mathcal C_{w,v}$ for $k=0,1,\ldots,\ell$.

This is a genuine source-backed family example, but it should probably be placed after the type $A_2$ example or linked to `Determinantial Modules`, because it depends on determinantial-module notation.

Source locations:

- KKOP18 local TeX lines 2749-2753 for $M(w\Lambda,v\Lambda)\in\mathcal C_{w,v}$.
- KKOP18 Proposition 4.8, local TeX lines 2929-2937, for $M(w_{\le k}\Lambda,v_{\le k}\Lambda)\in\mathcal C_{w,v}$.

## Recommended Later Topic Wording

The following is safe for a later approved edit to the `기본 예시` section of `content/topics/06-quiver-hecke-klr-algebras/quiver-hecke-subcategories.md`. It is not applied in this report-only pass.

```markdown
Type \(A_2\)에서 \(w=s_1s_2s_1\)이면 Kashiwara-Nakashima 2025의 example에 따라

$$
\mathcal C_w=R\text{-gmod}
$$

이다. 이 경우 \(\mathcal C_w\)는 ambient finite-dimensional graded quiver-Hecke module category 전체와 같다.

반대로 같은 type \(A_2\)에서 \(w=s_1s_2\), \(\lambda=s_1\Lambda_1\)로 두면

$$
\mathsf M_w(w\lambda,\lambda)\simeq \langle 2\rangle
\notin \mathcal C_w
$$

이다. 이 non-example은 \(\mathcal C_w\)의 membership condition이 실제로 object를 걸러낸다는 점을 보여준다.
```

If the page should also show a $\mathcal C_{w,v}$ example, add only a short family statement and point to `Determinantial Modules`:

```markdown
또한 KKOP18의 determinantial-module family는 \(\mathcal C_{w,v}\) 안의 source-backed object family를 제공한다. \(v\le w\)이고 \(w=s_{i_1}\cdots s_{i_\ell}\)를 고정하면, \(k=0,\ldots,\ell\)에 대해

$$
M(w_{\le k}\Lambda,v_{\le k}\Lambda)\in\mathcal C_{w,v}
$$

이다.
```

## Recommendation

Use Candidate 1 as the first visible basic example. Add Candidate 2 only if the page briefly explains the source notation $\langle 2\rangle$ and $\mathsf M_w$. Add Candidate 3 only as a bridge to `Determinantial Modules`, not as a substitute for a small basic example.

The example gap remains open until a later approved topic-page edit applies one or more of these candidates.
