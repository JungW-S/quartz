# Determinantial Modules Example Review

Date: 2026-06-03

## Scope

- Topic reviewed: `content/topics/06-quiver-hecke-klr-algebras/determinantial-modules.md`
- Source used: `kkop18-monoidal-categories-strata-flag-manifolds`
- Local source files:
  - `inbox/papers/KKOP18, Monoidal categories associated with strata of flag manifolds, Adv Math, arxiv ver.pdf`
  - `inbox/papers2/Tex/KKOP18, Monoidal categories associated with strata of flag manifolds, Adv Math, arxiv ver/source.tex`
- No paper was downloaded.
- No claim, topic page, source note, Sage code, or image was added.

## Question

Find one source-location-specific real example suitable for the visible `기본 예시` section of `Determinantial Modules`, without importing unsupported quantum-minor comparison or conjectural cluster-seed material.

## Finding

KKOP18 does not contain a standalone small numerical example for determinantial modules. The safest visible example is therefore not a finite-type worked computation, but a paper-backed construction example: the initial case `\mu=\Lambda` in Section 4, specialized to a one-step reduced expression.

For `\Lambda\in P_+` and `\lambda=w\Lambda`, KKOP18 defines
$$
\mathsf M(\lambda,\Lambda)
=
F_{i_1}^{\Lambda(m_1)}\cdots F_{i_l}^{\Lambda(m_l)}\mathbf 1
$$
from a reduced expression `w=s_{i_1}\cdots s_{i_l}`. In the one-step specialization `w=s_i`, this becomes
$$
\mathsf M(s_i\Lambda,\Lambda)
=
F_i^{\Lambda(\langle h_i,\Lambda\rangle)}\mathbf 1.
$$

This is safe as a construction example because it only specializes the source definition. It should be presented as an object-level example of how a determinantial module is produced, not as a worked coordinate-ring computation.

## Source Locations

- KKOP18 Section 4, PDF p.37; TeX lines 2618-2635: definition of `\mathsf M(\lambda,\Lambda)` from a reduced expression, with simplicity, self-duality, and reduced-expression independence.
- KKOP18 Proposition 4.1, PDF p.37; TeX lines 2638-2665: existence and uniqueness of the self-dual simple module `\mathsf M(\lambda,\mu)`.
- KKOP18 Proposition 4.2, PDF pp.37-38; TeX lines 2674-2686: realness and convolution behavior of determinantial modules.
- KKOP18 equations (4.2)-(4.3) and Proposition 4.8, PDF pp.40-41; TeX lines 2908-2938: definition of `w_{\le k}`, `v_{\le k}` and membership `\mathsf M(w_{\le k}\Lambda,v_{\le k}\Lambda)\in\mathcal C_{w,v}`.
- KKOP18 Theorem 4.10, PDF pp.41-42; TeX lines 3004-3047: strong commutation of the indexed determinantial-module family.

## Do Not Use Yet

Do not use KKOP18 Section 5, Conjecture 5.5, or Remark 5.6 as the basic example for this topic. Those passages discuss a monoidal categorification/initial-seed picture involving additional assumptions and references. They are useful for future comparison work, but they are too conditional and too far downstream for the first visible example on `Determinantial Modules`.

Do not add new quantum-minor comparison prose to the visible example. The page already states the class comparison in the definition/basic context. Expanding that comparison should remain a separate human-reviewed task.

## Proposed Wording If Later Approved

```markdown
## 기본 예시

### 실제 예시: one-step construction

$\Lambda\in P_+$를 dominant weight라고 하고, simple reflection $s_i$를 하나 고른다. $w=s_i$이면 reduced expression의 길이가 $1$이므로 Section 4의 construction은
$$
\mathsf M(s_i\Lambda,\Lambda)
=
F_i^{\Lambda(\langle h_i,\Lambda\rangle)}\mathbf 1
$$
을 준다.

이 예시는 determinantial module이 coordinate function 자체가 아니라, functor $F_i^\Lambda$를 통해 trivial module에서 만들어지는 object-level module임을 보여준다. Grothendieck-ring class와 quantum minor의 비교는 이 example의 목적이 아니라, 뒤의 basic properties와 Source notes에서 다루는 별도 level의 statement이다.

검증: 논문 예시
```

## Recommendation

If the user approves a topic edit, add only the one-step construction example above. Do not add claims, source notes, Section 5 cluster-seed material, new quantum-minor comparison, or any invented finite-type computation.
