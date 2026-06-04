# Head Simplicity Example Review

Date: 2026-06-03

## Scope

This is a report-only review of whether the already ingested KKKO15 or Kashiwara-Nakashima 2025 source material contains a compact verified example suitable for the visible `기본 예시` section of `Head Simplicity of Convolutions`.

Inspected files and local texts:

- `content/topics/06-quiver-hecke-klr-algebras/head-simplicity-of-convolutions.md`
- `content/sources/papers/kkko15-simplicity-heads-socles-tensor-products.md`
- `content/sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category.md`
- `inbox/papers2/Tex/KKKO15, Simplicity of heads and socles of tensor products, Compos Math/source.tex`
- `inbox/papers/crystal.tex`

No paper was downloaded. No claim was added. No topic page, source note, Sage code, image, or example was added.

## Verdict

KKKO15 does not contain a compact worked example for this topic. It supports the theorem statement and the real-simple consequences, but it should not be used as the source of a visible example.

Kashiwara-Nakashima 2025 contains one safe structural example candidate: head convolution with the simple root module \(L(i)\), controlled by \(d_i(M)\). This is not a numerical worked example. If later approved, it should be added only as a `구조 예시`, not as a new theorem expansion.

The current topic page already records the relevant KN25 formulas in `기본 성질`. A later edit should avoid duplicating the whole property list. The example should instead use the smallest readable case \(d_i(M)=0\) to show what head convolution does.

## Source Findings

### KKKO15

KKKO15 Theorem 3.2 states that, under the scalar self R-matrix condition for \(M\) and simplicity of \(N\), both \(M\circ N\) and \(N\circ M\) have simple head and simple socle. The theorem also identifies the images of the two R-matrices with the corresponding heads and socles.

The follow-up corollaries give the real-simple criterion and simplicity of powers \(M^{\circ n}\). These are theorem-level statements and are already appropriate for `정리의 진술` and `기본 성질`.

The KKKO15 TeX file defines an `Example` environment, but no actual `Example` occurrence appears in the source text. Therefore KKKO15 supplies no visible paper example for this page.

### Kashiwara-Nakashima 2025

KN25 Section 4.5 defines
$$
d_i(M)=\varepsilon_i(M)+\varepsilon_i^*(M)+\langle h_i,\operatorname{wt}(M)\rangle
$$
for a simple module \(M\), and then records the head-convolution behavior of \(L(i)\) with \(M\).

The safest example candidate is the \(d_i(M)=0\) case:
$$
L(i)\nabla M\simeq L(i)\circ M\simeq M\circ L(i)\simeq M\nabla L(i)
$$
up to grading shifts. This is useful as a first structural example because it explains when the head convolution does not discard any part of the convolution product.

The \(d_i(M)>0\) and \(L(i^n)\) formulas can remain in `기본 성질`. They are better as properties than as the first visible example.

## Source Locations

- KKKO15 Theorem 3.2: TeX lines 1230-1254, theorem statement for simple heads, simple socles, and R-matrix image identifications.
- KKKO15 proof of Theorem 3.2: TeX lines 1255-1320, proof that the image of \(r_{N,M}\) is the unique simple submodule of \(M\circ N\).
- KKKO15 Corollary 3.3: TeX lines 1328-1336, equivalence between real simplicity, scalar self R-matrix, and scalar endomorphism algebra.
- KKKO15 Corollary 3.4: TeX lines 1338-1347, simplicity of powers \(M^{\circ n}\) for real simple \(M\).
- KN25 Definition 4.13: TeX lines 2508-2511, definition of \(d_i(M)\).
- KN25 Lemma 4.14: TeX lines 2513-2523, relation between \(L(i)\), R-matrix degrees, and \(d_i(M)\).
- KN25 Proposition 4.15: TeX lines 2525-2553, \(d_i(M)=0\), \(d_i(M)>0\), and \(L(i^n)\) head-convolution formulas.
- KN25 Lemma 4.24: TeX lines 2797-2802, simple head and simple socle of \(E_i^{(n)}(M)\).

## Recommended Later Edit

If the user approves a topic edit, add only the following compact structural example under `## 기본 예시`.

```markdown
## 기본 예시

### 구조 예시: \(L(i)\)와 \(d_i(M)=0\)

simple root module \(L(i)\)와 simple module \(M\)을 둔다. \(d_i(M)=0\)이면, grading shift를 제외하고
$$
L(i)\nabla M\simeq L(i)\circ M\simeq M\circ L(i)\simeq M\nabla L(i)
$$
이다.

이 예시는 head convolution \(L(i)\nabla M\)이 항상 새로운 quotient를 만드는 것이 아님을 보여준다. \(d_i(M)=0\)인 경우에는 head를 취해도 전체 convolution product와 같은 simple object가 남는다.

검증: 논문 예시
```

Do not add a new claim. Do not add KKKO15 proof material. Do not add a numerical \(R(\beta)\)-module computation. Do not create Sage code or images for this page in this pass.

## Recommendation

The page can become `example-ready` after a small approved topic edit that adds only the KN25 \(d_i(M)=0\) structural example above and a concise final Source notes line pointing to KN25 Proposition 4.15. If the user wants only numerical or source-labeled example-environment examples, keep the example gap open and move on to the next prerequisite topic.
