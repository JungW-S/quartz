---
id: b-infinity-crystal
title: The Crystal B(infinity)
level: core
topic_kind: object-family
parent_topics:
  - crystal-bases
prerequisite_topics:
  - abstract-crystals
  - tensor-products-of-crystals
  - quantum-groups
child_topics:
  - demazure-crystals
related_topics:
  - highest-weight-crystals
maturity: example-ready
---

## 개요

$B(\infty)$는 quantum group $U_q(\mathfrak g)$의 negative half $U_q^-(\mathfrak g)$의 crystal base에서 얻는 crystal이다. 여기서는 algebra $U_q^-(\mathfrak g)$ 자체가 아니라, 그 crystal base에서 얻어지는 weight, root operators, string functions의 combinatorial object를 다룬다.

[[topics/02-crystal-bases/highest-weight-crystals|Highest Weight Crystals]]가 하나의 highest weight module에서 나오는 crystal이라면, $B(\infty)$는 highest weight를 하나 고정하지 않고 negative half 전체에서 나오는 crystal이다. 그래서 $B(\infty)$는 여러 highest weight crystals를 비교할 때 공통 기준점 역할을 한다.

이 topic은 [[topics/02-crystal-bases/demazure-crystals|Demazure Crystals]]와 [[topics/02-crystal-bases/cellular-crystals|Cellular Crystals]]로 넘어가기 전에 필요하다. Demazure crystal은 $B(\lambda)$ 안에서도 나타나지만, $B(\infty)$ 안의 부분 crystal로도 나타나기 때문에 $B(\infty)$를 먼저 분리해 두어야 한다.

## 준비와 notation

$\mathfrak g$를 Kac-Moody algebra라고 하고, $U_q(\mathfrak g)$를 그 quantum group이라고 하자. 그 negative half를
$$
U_q^-(\mathfrak g)
$$
라고 쓴다.

$B(\infty)$는 $U_q^-(\mathfrak g)$의 crystal base에 대응하는 crystal이다. Root operators와 string functions는 [[topics/02-crystal-bases/abstract-crystals|Abstract Crystals]]의 notation을 따른다.
$$
\widetilde e_i,\widetilde f_i,
\qquad
\varepsilon_i,\varphi_i,
\qquad
\operatorname{wt}.
$$

Weight $0$을 갖는 distinguished element는
$$
u_\infty\in B(\infty)
$$
로 쓴다.

또한 $\lambda\in P_+$에 대해 $B(\lambda)$는 [[topics/02-crystal-bases/highest-weight-crystals|highest weight crystal]]이고, $T_\lambda$는 weight $\lambda$를 갖는 one-element crystal이다.

## 정의

$B(\infty)$는 $U_q^-(\mathfrak g)$의 crystal base에서 얻는 crystal이다. 즉 $U_q^-(\mathfrak g)$의 crystal base의 underlying crystal을
$$
B(\infty)
$$
라고 쓴다.

$b\in B(\infty)$에 대해 string function $\varepsilon_i$는
$$
\varepsilon_i(b)
=
\max\{k\ge 0\mid \widetilde e_i^k b\ne 0\}
$$
으로 주어진다. 그리고
$$
\varphi_i(b)
=
\varepsilon_i(b)+\langle h_i,\operatorname{wt}(b)\rangle
$$
로 둔다.

$B(\infty)$에서 weight $0$인 unique element를
$$
u_\infty
$$
라고 쓴다.

## 기본 예시

### 실제 예시: type $A_2$의 rank-two coordinate model

$\mathfrak g$가 type $A_2$이고 $I=\{1,2\}$라고 하자. 이 경우
$$
\langle h_1,\alpha_2\rangle
=
\langle h_2,\alpha_1\rangle
=-1
$$
이다.

Rank-two coordinate model에서는 $B(\infty)$가
$$
B_1\otimes B_2\otimes B_1
$$
안에 full subcrystal로 들어간다. 이 embedding은
$$
u_\infty
\longmapsto
b_1\otimes b_2\otimes b_1
$$
을 만족한다. 여기서 $b_i$는 elementary crystal $B_i$의 원점 $b_i(0)$이다.

이 embedding의 image는 다음 원소들로 주어진다.
$$
\left\{
\widetilde f_1^{\,n}b_1
\otimes
\widetilde f_2^{\,m}b_2
\otimes
\widetilde f_1^{\,\ell}b_1
\ \middle|\
0\le n\le m,\ 0\le \ell
\right\}.
$$

이 예시는 $B(\infty)$가 추상적인 negative-half crystal로만 존재하는 것이 아니라, rank two에서는 elementary crystals의 tensor product 안에서 부등식으로 잘린 coordinate model로 보일 수 있음을 보여 준다.

검증: 논문 예시

## 핵심 관점

$B(\infty)$는 highest weight를 하나 고정한 crystal이 아니라, negative half의 crystal이다. 그래서 $B(\lambda)$와 비교할 때에는 $B(\lambda)$를 $B(\infty)$ 자체 안에 넣는 것이 아니라, one-element crystal $T_\lambda$를 붙인 tensor product 안으로 보낸다.

구체적으로 $\lambda\in P_+$에 대해
$$
B(\lambda)\longrightarrow B(\infty)\otimes T_\lambda
$$
라는 full embedding이 존재하며,
$$
u_\lambda\longmapsto u_\infty\otimes t_\lambda
$$
를 만족한다. 이 embedding은 모든 $\widetilde e_i$와 commute한다.

이 관점에서 $B(\infty)$는 highest weight crystals를 비교하는 공통 기준점으로 작동한다. 이후 Demazure crystal을 볼 때도 $B(\lambda)$ 쪽과 $B(\infty)$ 쪽의 두 version이 함께 등장한다.

Localized crystal을 읽을 때 필요한 $B(\infty)$ 쪽 출발점은 다음 부분 crystal이다. Weyl group element $w$가 주어지면
$$
B(w)=\{b\in B(\infty)\mid \mathbf G^{\mathrm{up}}(b)\in A_q(\mathfrak n(w))\}
$$
이다. 이후 [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]에서는 quantum unipotent minor에 대응하는 frozen crystal elements $\mathfrak z_i^w$를 invert하여 $B(w)$를 localized crystal $\mathcal B(w)$로 확장한다. 따라서 $B(\infty)$는 localized crystal의 전체 vertex set이 아니라, 그 construction이 시작되는 ambient crystal이다.

## 기본 성질

### Crystal-level 대상

$B(\infty)$는 $U_q^-(\mathfrak g)$의 crystal base에서 나오는 crystal이다. 따라서 $B(\infty)$의 원소는 negative half의 crystal-level basis elements로 생각할 수 있다.

### 기준 원소

$B(\infty)$에는 weight $0$인 unique element $u_\infty$가 있다. 이 element는 highest weight crystal의 $u_\lambda$와 비교되는 기준 vertex이다.

### Upper normality 성질

$B(\infty)$는 upper normal이지만 lower normal은 아니다. 즉 $\varepsilon_i$는 $\widetilde e_i$를 최대로 적용할 수 있는 횟수를 기록하지만, 일반적으로 $\varphi_i$가 $\widetilde f_i$를 최대로 적용할 수 있는 횟수를 기록하는 normal crystal은 아니다.

### Highest weight crystal로부터의 embedding

$\lambda\in P_+$에 대해 $B(\lambda)$에서 $B(\infty)\otimes T_\lambda$로 가는 full embedding이 존재한다. 이 embedding은 $u_\lambda$를 $u_\infty\otimes t_\lambda$로 보내고, 모든 $\widetilde e_i$와 commute한다.

## 다른 topic들과의 관계

**Abstract Crystals.** [[topics/02-crystal-bases/abstract-crystals|Abstract Crystals]]는 $B(\infty)$가 갖는 $\operatorname{wt}$, $\varepsilon_i$, $\varphi_i$, $\widetilde e_i$, $\widetilde f_i$의 axioms를 제공한다.

**Tensor Products of Crystals.** [[topics/02-crystal-bases/tensor-products-of-crystals|Tensor Products of Crystals]]는 $B(\infty)\otimes T_\lambda$를 읽기 위해 필요한 tensor product convention을 제공한다.

**Highest Weight Crystals.** [[topics/02-crystal-bases/highest-weight-crystals|Highest Weight Crystals]]는 $B(\lambda)$와 $u_\lambda$를 제공한다. $B(\infty)$와 $B(\lambda)$의 관계는 $B(\lambda)\to B(\infty)\otimes T_\lambda$ embedding으로 나타난다.

**Demazure Crystals.** [[topics/02-crystal-bases/demazure-crystals|Demazure Crystals]]는 $B(\lambda)$와 $B(\infty)$ 안에서 Weyl group element가 정하는 부분 crystal을 다룬다.

**Cellular Crystals.** [[topics/02-crystal-bases/cellular-crystals|Cellular Crystals]]는 $B(\infty)$와 Demazure crystal 쪽 언어를 사용해 더 구체적인 coordinate model로 넘어간다.

**Localized Crystals.** [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]는 $B(w)\subset B(\infty)$에서 시작하는 crystal-level route와 localized quiver-Hecke category의 simple-object route가 만나는 곳이다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/02-crystal-bases/abstract-crystals|Abstract Crystals]]에서 crystal axioms를 읽고, [[topics/02-crystal-bases/tensor-products-of-crystals|Tensor Products of Crystals]]에서 tensor product convention을 읽는다.
- 상위 개념: [[topics/02-crystal-bases/crystal-bases|Crystal Bases]]는 $B(\infty)$가 crystal base theory 안에서 어떤 역할을 하는지 설명한다.
- 다음에 읽을 것: [[topics/02-crystal-bases/demazure-crystals|Demazure Crystals]]에서 $B(\lambda)$와 $B(\infty)$ 안의 Demazure 부분을 읽고, 그 다음 [[topics/02-crystal-bases/cellular-crystals|Cellular Crystals]]와 [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]로 넘어간다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara93-crystal-base-demazure-character-formula|Kashiwara 1993]], Example 1.2.8, p.843: $B(\infty)$ as the crystal associated with the crystal base of $U_q^-(\mathfrak g)$.
- Kashiwara 1993, Example 1.2.8, p.843: the formulas for $\varepsilon_i$ and $\varphi_i$ on $B(\infty)$, the element $u_\infty$, and the statement that $B(\infty)$ is upper normal but not lower normal.
- Kashiwara 1993, Example 1.2.8, p.843: the full embedding $B(\lambda)\to B(\infty)\otimes T_\lambda$ sending $u_\lambda$ to $u_\infty\otimes t_\lambda$ and commuting with all $\widetilde e_i$.
- Kashiwara 1993, Example 2.2.5, p.850: type $A_2$ full embedding of $B(\infty)$ into $B_1\otimes B_2\otimes B_1$ and its image inequalities.
- Kashiwara 1993, Propositions 3.2.3 and 3.2.5, pp.854-855: Demazure crystal subsets inside $B(\lambda)$ and $B(\infty)$.
- [[sources/papers/jp25-crystals-quantum-twist-automorphisms|Jung-Park 2025]], local TeX lines 1480-1510: \(B(w)\subset B(\infty)\), frozen crystal elements \(\mathfrak z_i^w\), and the localized crystal \(\mathcal B(w)\).

</details>
