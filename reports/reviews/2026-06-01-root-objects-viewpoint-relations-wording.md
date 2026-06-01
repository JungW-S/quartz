# Root Objects Viewpoint And Relations Wording

Date: 2026-06-01

## Scope

This is a report-only wording proposal for `content/topics/root-objects-in-localized-categories.md`.

No topic page was rewritten. No claims were added. No papers were downloaded. The proposed wording below should be applied only after explicit approval for a topic-page edit.

## Source Basis

Only existing review reports were used:

- `reports/reviews/2026-06-01-root-objects-source-location-review.md`
- `reports/reviews/2026-06-01-affine-r-matrix-prerequisite-source-location-review.md`
- `reports/reviews/2026-06-01-localized-root-operators-source-location-review.md`

The proposal uses these already reviewed points:

- A root object is a real simple object $L\in\widetilde{\mathcal C}_w$ with an affinization $(\widehat L,z)$ satisfying $\deg z=2d_L$ and $\mathfrak d(L,\mathscr D^{-1}L)=d_L$.
- Affinization data measures a deformation degree, while $\mathfrak d(-,-)$ is built from R-matrix degrees.
- Localized root operators use localized simple-root objects $\widetilde Q_i$ and head convolution, but one must not state that every $\widetilde Q_i$ is a root object.
- The root-object page should not duplicate the full localized-root-operator formulas.

## Proposed Wording

### `## 핵심 관점`

```markdown
Root object의 핵심은 crystal의 simple root 방향을 localized category 안에서 object-level로 다룰 수 있게 만드는 것이다. Crystal graph에서는 $i$-arrow가 combinatorial operation으로 주어지지만, $\widetilde{\mathcal C}_w$에서는 그 방향이 simple object와 head convolution을 통해 표현된다. 따라서 어떤 simple object가 root direction처럼 작동하려면, 단순히 real simple object인 것만으로는 부족하고 affinization과 R-matrix degree가 서로 맞아야 한다.

정의의 두 조건은 같은 object $L$을 두 방식으로 측정한다. Affinization $(\widehat L,z)$는 $L$을 positive-degree parameter $z$로 들어 올렸을 때의 deformation degree를 준다. 반면 $\mathfrak d(L,\mathscr D^{-1}L)$은 $L$과 duality로 옮긴 object 사이의 R-matrix degree 정보를 기록한다. Root object 조건은 이 두 측정값이 같은 정수 $d_L$로 정렬된다는 요구이다.

이 관점에서 root object는 localized root operator의 입력을 준비하는 중간 개념이다. 특히 $\widetilde Q_i$ 같은 localized simple-root object가 등장하지만, 모든 $\widetilde Q_i$가 root object인 것은 아니다. Root object 조건은 어떤 경우에 simple-root object가 실제 root-direction object로 쓰일 수 있는지를 가르는 검증 조건으로 읽어야 한다.
```

### `## 다른 topic들과의 관계`

```markdown
- [[topics/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]은 root object가 사는 ambient category $\widetilde{\mathcal C}_w$를 제공한다. Root object의 정의는 이 localized category 안의 real simple object에서 시작한다.
- [[topics/affine-objects-in-monoidal-categories|Affine Objects in Monoidal Categories]]는 $(\widehat L,z)$와 $\deg z$를 설명하는 prerequisite이다. Root object의 첫 번째 조건은 $L$이 degree $2d_L$의 affinization을 가져야 한다는 조건이다.
- [[topics/r-matrix-renormalization|R-Matrix Renormalization]]은 $\Lambda(-,-)$와 $\mathfrak d(-,-)$의 의미를 제공한다. Root object의 두 번째 조건은 $L$과 $\mathscr D^{-1}L$ 사이의 R-matrix degree invariant를 사용한다.
- [[topics/localized-root-operators|Localized Root Operators]]는 root object가 쓰이는 다음 단계이다. Root object page에서는 operator formula를 반복하기보다, root object가 $\widetilde E_i,\widetilde F_i$를 정의하기 전에 필요한 object-level 조건이라는 점만 설명한다.
- [[topics/localized-crystals|Localized Crystals]]는 이 object-level 조건들이 모여 crystal structure로 해석되는 상위 construction이다. Root object는 그 construction에서 simple root 방향을 category 안의 object와 연결하는 역할을 한다.
```

## What Not To Add In The Topic Page

- Do not add localized-root-operator formulas to the root-object page.
- Do not claim that every $\widetilde Q_i$ is a root object.
- Do not add proof details about inverse properties or the full crystal-structure theorem.
- Do not add a new visible example in this edit.

## Recommendation

The proposed wording is safe to apply as a compact topic-page polishing edit after user approval. It should not change claims, source notes, examples, or topic hierarchy metadata.
