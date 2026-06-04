---
id: determinantial-modules
title: Determinantial Modules
level: advanced
topic_kind: object-family
parent_topics:
  - quiver-hecke-subcategories
  - monoidal-categorification
  - quantum-coordinate-rings
prerequisite_topics:
  - quiver-hecke-subcategories
  - monoidal-categorification
  - quantum-coordinate-rings
child_topics: []
related_topics:
  - quiver-hecke-category-localization
maturity: example-ready
---

## 개요

Determinantial modules는 quiver Hecke algebra의 module category에서 나타나는 distinguished module objects로, monoidal categorification에서 determinant-type coordinate data를 category 안에서 다루게 해 주는 family이다. 이름의 determinantial은 그 class가 unipotent quantum minor $D(\lambda,\mu)$와 비교된다는 점을 가리키지만, module object 자체가 coordinate function인 것은 아니다.

이 modules는 먼저 $\mathcal C_{w,v}$ 안의 objects로 놓인다. 그 다음 Grothendieck ring으로 내려가 classes를 만들고, 이 classes를 $A_{w,v}$와 비교하면서 coordinate-ring side의 정보를 읽는다.

따라서 이 topic에서 가장 중요한 구분은 object-level module, Grothendieck-ring-level class, coordinate-ring-level element의 구분이다.

## 준비와 notation

$v \leq w$인 Weyl group elements를 고정하고, $w$의 reduced expression
$$
w=s_{i_1}\cdots s_{i_\ell}
$$
을 하나 고른다. Index $k$는 이 reduced expression을 따라 읽는다.

- $\mathcal C_{w,v}$는 determinantial modules가 놓이는 ambient monoidal category이다.
- $K_0(\mathcal C_{w,v})$는 $\mathcal C_{w,v}$의 Grothendieck ring이다.
- $A_{w,v}$는 $K_0(\mathcal C_{w,v})$와 비교되는 coordinate-ring side의 algebra이다.
- $M(w_{\le k}\Lambda, v_{\le k}\Lambda)$는 chosen reduced expression과 weight parameter $\Lambda$에 붙은 determinantial-module family의 한 member를 나타낸다.
- $M(\lambda,\mu)$는 self-dual simple module로, class가 unipotent quantum minor $D(\lambda,\mu)$에 대응한다.

Reduced expression에서
$$
w_{\le k}=s_{i_1}\cdots s_{i_k},\qquad w_{\le 0}=\operatorname{id}
$$
로 둔다. $v_{\le k}$는 $v_{\le0}=\operatorname{id}$에서 시작하여
$$
v_{\ge k}=(v_{\le k-1})^{-1}v,
$$
$$
v_{\le k}=
\begin{cases}
v_{\le k-1}s_{i_k}, & s_{i_k}v_{\ge k}<v_{\ge k},\\
v_{\le k-1}, & s_{i_k}v_{\ge k}>v_{\ge k}
\end{cases}
$$
로 재귀적으로 정한다.

## 정의

### General determinantial module

먼저 $\Lambda\in P_+$와 $\lambda,\mu\in W\Lambda$가 $\lambda\preceq\mu$를 만족한다고 하자. Determinantial module $M(\lambda,\mu)$는 self-dual simple module로 구성되며, 그 class는
$$
[M(\lambda,\mu)]=D(\lambda,\mu)
$$
를 만족한다. 이 조건은 $M(\lambda,\mu)$의 isomorphism class를 결정한다.

### Initial case

$\mu=\Lambda$인 경우에는 reduced expression $\lambda=w\Lambda$, $w=s_{i_1}\cdots s_{i_l}$를 골라
$$
M(\lambda,\Lambda)
=
F_{i_1}^{\Lambda(m_1)}\cdots F_{i_l}^{\Lambda(m_l)}1
$$
로 둔다. 여기서
$$
m_k=\langle h_{i_k},s_{i_{k+1}}\cdots s_{i_l}\Lambda\rangle.
$$

### Recursive step

일반적인 $\mu=u\Lambda$에 대해서는 $u'=s_i u<u$, $\mu'=u'\Lambda$, $n=\langle h_i,\mu'\rangle$를 택하고, 이미 구성한 $M(\lambda,\mu')$에서
$$
M(\lambda,\mu):=E_i^{*(n)}M(\lambda,\mu')
$$
로 재귀적으로 정의한다.

### Indexed family in $\mathcal C_{w,v}$

고정된 $v \leq w$, chosen reduced expression $w=s_{i_1}\cdots s_{i_\ell}$, 그리고 dominant weight $\Lambda\in P_+$에 대해 여기서 다루는 determinantial modules는 indexed family
$$
M(w_{\le k}\Lambda, v_{\le k}\Lambda),
\qquad k=0,1,\ldots,\ell
$$
로 나타난다.

여기서 각 $M(w_{\le k}\Lambda, v_{\le k}\Lambda)$는 위의 $M(\lambda,\mu)$를 $\lambda=w_{\le k}\Lambda$, $\mu=v_{\le k}\Lambda$로 특수화한 것이다. 이 modules는 $\mathcal C_{w,v}$의 objects이고, 이 indexed family는 strongly commute한다.

## 기본 예시

### 실제 예시: 한 단계 construction

$\Lambda\in P_+$를 dominant weight라고 하고, simple reflection $s_i$를 하나 고른다. $\lambda=s_i\Lambda$인 경우에는 reduced expression의 길이가 $1$이므로 determinantial module construction은
$$
M(s_i\Lambda,\Lambda)
=
F_i^{\Lambda(\langle h_i,\Lambda\rangle)}1
$$
을 준다.

이 예시는 determinantial module이 coordinate function 자체가 아니라, $F_i^{\Lambda(\langle h_i,\Lambda\rangle)}$를 trivial module에 적용해서 만들어지는 object-level module임을 보여준다. Grothendieck-ring class와 quantum minor의 비교는 이 example의 목적이 아니라, 뒤의 기본 성질에서 다루는 별도 level의 statement이다.

검증: 논문 예시

## 핵심 관점

$$
M(w_{\le k}\Lambda, v_{\le k}\Lambda)\in \mathcal C_{w,v}
\;\longrightarrow\;
\bigl[M(w_{\le k}\Lambda, v_{\le k}\Lambda)\bigr]\in K_0(\mathcal C_{w,v})
\;\longrightarrow\;
A_{w,v}
$$

왼쪽은 module object이고, 가운데는 그 Grothendieck-ring class이다. 오른쪽은 coordinate-ring side와의 comparison으로 도달하는 algebra이다.

이 diagram은 determinantial module 자체, 그 class, 그리고 coordinate-ring element를 같은 것으로 취급하지 않도록 해 준다.

## 기본 성질

### Category-level placement

$M(w_{\le k}\Lambda, v_{\le k}\Lambda)$는 $\mathcal C_{w,v}$ 안에 놓인다. 이 사실은 determinantial modules를 coordinate-ring expression이 아니라 category 안의 concrete module objects로 다루게 해 준다.

### Strong commutation

관련 indexed family는 strongly commute한다. 이 사실은 family의 convolution products를 Grothendieck-ring classes와 비교할 때 필요한 monoidal compatibility를 제공한다.

### Grothendieck-ring comparison

$K_0(\mathcal C_{w,v})$는 $A_{w,v}$와 비교된다. 이 사실은 module objects에서 coordinate-ring side의 algebra로 이동하는 통로를 만든다.

## 다른 topic들과의 관계

**Quiver-Hecke subcategories.** [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-subcategories|Quiver-Hecke Subcategories]]는 determinantial modules가 놓이는 category $\mathcal C_{w,v}$를 제공한다.

**Monoidal categorification.** [[topics/05-monoidal-categorification/monoidal-categorification|Monoidal Categorification]]은 object-level modules를 Grothendieck ring으로 보낸 뒤 coordinate-ring data와 비교하는 관점을 제공한다.

**Quantum coordinate rings.** [[topics/01-quantum-groups/quantum-coordinate-rings|Quantum Coordinate Rings]]는 coordinate-ring side를 제공한다. $A_{w,v}$는 determinantial modules의 classes를 비교하는 algebra이다.

**Localization.** [[topics/08-localization-of-categories/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]에서는 특정 determinantial objects가 localized category 안에서 invertible하게 쓰인다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-subcategories|Quiver-Hecke Subcategories]]에서 $\mathcal C_{w,v}$를 읽고, [[topics/05-monoidal-categorification/monoidal-categorification|Monoidal Categorification]]에서 Grothendieck ring 관점을 읽고, [[topics/01-quantum-groups/quantum-coordinate-rings|Quantum Coordinate Rings]]에서 coordinate-ring comparison을 읽는다.
- 상위 개념: [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-subcategories|Quiver-Hecke Subcategories]], [[topics/05-monoidal-categorification/monoidal-categorification|Monoidal Categorification]], [[topics/01-quantum-groups/quantum-coordinate-rings|Quantum Coordinate Rings]]가 이 object family가 놓이는 세 가지 더 넓은 배경이다.
- 다음에 읽을 것: [[topics/08-localization-of-categories/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]에서는 determinantial objects가 invertible하게 쓰이는 construction을 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kkop18-monoidal-categories-strata-flag-manifolds|KKOP18]], Proposition 4.1: source-defined modules $M(\lambda,\mu)$ as self-dual simple modules with classes $D(\lambda,\mu)$.
- KKOP18, equations (4.2)-(4.3), Proposition 4.8, and Theorem 4.10: the indexed family $M(w_{\le k}\Lambda,v_{\le k}\Lambda)$ lies in $\mathcal C_{w,v}$ and strongly commutes.
- KKOP18, Section 2.2 and Proposition 2.16: $\mathcal C_{w,v}$ is the ambient category used here.
- KKOP18, Theorem 2.20(ii)(c): $K_0(\mathcal C_{w,v})$ is compared with $A_{w,v}$.

</details>
