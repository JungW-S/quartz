---
id: coordinate-formulas-for-quantum-twist-on-localized-crystals
title: Coordinate Formulas for Quantum Twist on Localized Crystals
level: advanced
topic_kind: theorem
parent_topics:
  - quantum-twist-automorphisms
prerequisite_topics:
  - quantum-twist-automorphisms
  - localized-crystals
  - localized-pbw-parametrizations
  - localized-string-parametrizations
  - left-and-right-g-vectors
child_topics: []
related_topics:
  - quantum-coordinate-rings
maturity: example-ready
---

## 개요

Coordinate formulas for quantum twist on localized crystals는 quantum twist automorphism을 localized crystal $\widetilde B(w)$ 위의 coordinate languages로 읽는 theorem-level statement이다. 이 statement는 [[topics/08-localization-of-categories/quantum-twist-automorphisms|Quantum Twist Automorphisms]]의 coordinate-ring-level operation을 [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]의 crystal-level permutation과 비교한다.

여기서 비교되는 coordinate languages는 localized PBW coordinates, localized string coordinates, left $g$-vectors, right $g$-vectors이다. 따라서 이 statement는 새로운 object를 정의하기보다, 이미 준비된 네 coordinate descriptions가 quantum twist와 어떻게 만나는지를 설명한다.

읽는 순서는 quantum twist와 localized crystal을 먼저 고정한 뒤, localized PBW coordinates, localized string coordinates, left/right $g$-vectors를 차례로 읽는 것이 좋다. 이 글은 그 네 coordinate languages를 한곳에서 비교하는 마지막 단계이다.

## 준비와 notation

읽기 전에 다음 topic들이 필요하다.

- [[topics/08-localization-of-categories/quantum-twist-automorphisms|Quantum Twist Automorphisms]]: coordinate-ring-level operation.
- [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]: $\widetilde B(w)$와 crystal-level permutation이 놓이는 대상.
- [[topics/08-localization-of-categories/localized-pbw-parametrizations|Localized PBW Parametrizations]]: PBW-coordinate language.
- [[topics/08-localization-of-categories/localized-string-parametrizations|Localized String Parametrizations]]: string-coordinate language.
- [[topics/08-localization-of-categories/left-and-right-g-vectors|Left and Right g-Vectors]]: seed-dependent left/right degree language.

$w$는 Weyl group element이고, $\mathbf i$는 $w$의 reduced expression이다. 이 reduced expression은 localized PBW parametrization, localized string parametrization, left/right $g$-vector data를 동시에 고정한다.

$\widetilde B(w)$는 localized crystal이다. Quantum twist automorphism은 coordinate-ring side의 operation이고, 이 operation의 crystal-level shadow는 $\widetilde B(w)$ 위의 permutation으로 읽힌다.

이 statement에서 쓰는 maps는 다음과 같다.

- $\mathfrak D_w:\widetilde B(w)\to\widetilde B(w)$는 quantum twist automorphism의 crystal-level counterpart이다.
- $\operatorname{PBW}_{\mathbf i}:\widetilde B(w)\to\mathcal P_{\mathbf i}(w)$는 localized PBW coordinate map이다.
- $\operatorname{STR}_{\mathbf i}:\widetilde B(w)\to\mathcal S_{\mathbf i}(w)$는 localized string coordinate map이다.
- $\psi_{\mathbf i}:\mathcal P_{\mathbf i}(w)\to\mathcal S_{\mathbf i}(w)$는 PBW coordinates에서 string coordinates로 가는 bijection이다.
- $\mathrm g^{\mathrm L}_{\mathbf i}$와 $\mathrm g^{\mathrm R}_{\mathbf i}$는 left and right $g$-vector maps이다.
- $\mathcal M_{\mathbf i}$와 $\mathcal N_{\mathbf i}$는 string/PBW coordinates와 left/right $g$-vector coordinates를 비교하는 linear maps이다.

## 정리의 진술

이 coordinate formula theorem은 quantum twist의 crystal-level permutation $\mathfrak D_w$가 localized PBW coordinates, localized string coordinates, left $g$-vectors, right $g$-vectors에서 어떻게 표현되는지를 말한다.

$w\in W$, $\mathbf i\in R(w)$, $b\in\widetilde B(w)$라고 하자. Parameter-set identifications
$$
\mathcal G^{\mathrm L}_{\mathbf i}(w)
=
\mathbb Z^{[1,m]}
=
\mathcal G^{\mathrm R}_{\mathbf i}(w),
\qquad
\mathcal S_{\mathbf i}(w)
=
\mathbb Z^{[1,m]}
=
\mathcal P_{\mathbf i}(w)
$$
아래에서 다음이 성립한다.

$$
\mathrm g^{\mathrm L}_{\mathbf i}(b)
=
\mathcal M_{\mathbf i}^{-1}
\circ
\psi_{\mathbf i}
\circ
\mathcal N_{\mathbf i}^{-1}
\bigl(\mathrm g^{\mathrm R}_{\mathbf i}(b)\bigr).
$$

$$
\mathrm g^{\mathrm L}_{\mathbf i}\bigl(\mathfrak D_w(b)\bigr)
=
-
\mathcal N_{\mathbf i}
\circ
\psi_{\mathbf i}^{-1}
\circ
\mathcal M_{\mathbf i}
\bigl(\mathrm g^{\mathrm L}_{\mathbf i}(b)\bigr).
$$

$$
\mathrm g^{\mathrm R}_{\mathbf i}\bigl(\mathfrak D_w(b)\bigr)
=
\mathcal N_{\mathbf i}
\circ
\psi_{\mathbf i}^{-1}
\circ
\mathcal M_{\mathbf i}
\bigl(-\mathrm g^{\mathrm R}_{\mathbf i}(b)\bigr).
$$

$$
\operatorname{PBW}_{\mathbf i}\bigl(\mathfrak D_w(b)\bigr)
=
\psi_{\mathbf i}^{-1}
\circ
\mathcal M_{\mathbf i}
\circ
\mathcal N_{\mathbf i}
\bigl(-\operatorname{PBW}_{\mathbf i}(b)\bigr).
$$

$$
\operatorname{STR}_{\mathbf i}\bigl(\mathfrak D_w(b)\bigr)
=
-
\mathcal M_{\mathbf i}
\circ
\mathcal N_{\mathbf i}
\circ
\psi_{\mathbf i}^{-1}
\bigl(\operatorname{STR}_{\mathbf i}(b)\bigr).
$$

이 statement는 coordinate systems 사이의 comparison을 먼저 기록한다. 아래 기본 예시는 $\mathcal M_{\mathbf i}$, $\mathcal N_{\mathbf i}$의 matrix entries와 PBW-string bijection이 실제 좌표 계산에 어떻게 들어가는지를 보여준다.

## 기본 예시

### Type \(A_2\), \(\mathbf i=(1,2,1)\)

검증: 논문 예시

이 예시는 type \(A_2\)에서 \(w=w_\circ\)이고 \(\mathbf i=(1,2,1)\in R(w_\circ)\)인 경우를 보여준다. \(b\in\widetilde B(\infty)\)에 대해 네 coordinate를
$$
\operatorname{PBW}_{\mathbf i}(b)=(a_1,a_2,a_3),
\quad
\operatorname{STR}_{\mathbf i}(b)=(t_1,t_2,t_3),
$$
$$
\mathrm g^{\mathrm R}_{\mathbf i}(b)=(r_1,r_2,r_3),
\quad
\mathrm g^{\mathrm L}_{\mathbf i}(b)=(l_1,l_2,l_3)
$$
로 쓴다.

첫 단계는 frozen directions를 확인하는 것이다. 이 예시에서 frozen basis elements는
$$
G^{\mathrm{up}}(z_1)=\Delta_3,
\qquad
G^{\mathrm{up}}(z_2)=\Delta_2
$$
이다. 이 두 frozen elements의 PBW와 string coordinates는
$$
P_1=\operatorname{PBW}_{\mathbf i}(z_1)=(1,0,1),
\qquad
P_2=\operatorname{PBW}_{\mathbf i}(z_2)=(0,1,0),
$$
$$
S_1=\operatorname{STR}_{\mathbf i}(z_1)=(0,1,1),
\qquad
S_2=\operatorname{STR}_{\mathbf i}(z_2)=(1,1,0)
$$
이다. 따라서 localized parameter sets는 ordinary parameter set에 frozen directions를 더해
$$
\widetilde{\mathcal P}_{\mathbf i}(\infty)
=
\mathcal P_{\mathbf i}(\infty)+\mathbb ZP_1+\mathbb ZP_2,
\qquad
\widetilde{\mathcal S}_{\mathbf i}(\infty)
=
\mathcal S_{\mathbf i}(\infty)+\mathbb ZS_1+\mathbb ZS_2
$$
로 나타난다. 이 예시에서는
$$
\mathcal P_{\mathbf i}(\infty)=\mathbb Z_{\ge0}^3,
\qquad
\mathcal S_{\mathbf i}(\infty)
=
\{(x,y,z)\mid x\ge0,\ y\ge z\ge0\},
$$
그리고
$$
\widetilde{\mathcal P}_{\mathbf i}(\infty)
=
\widetilde{\mathcal S}_{\mathbf i}(\infty)
=
\mathbb Z^3
$$
이다.

다음 단계는 PBW coordinates에서 string coordinates로 가는 map이다. 이 경우
$$
\psi_{\mathbf i}(a_1,a_2,a_3)
=
\bigl(
a_1+a_2-\min\{a_1,a_3\},
a_2+a_3,
\min\{a_1,a_3\}
\bigr).
$$
이 map은 \(\mathbb Z\)-linear가 아니다. 하지만 frozen directions에 대해서는
$$
\psi_{\mathbf i}(x+aP_1+bP_2)
=
\psi_{\mathbf i}(x)+aS_1+bS_2
\qquad
(a,b\in\mathbb Z)
$$
를 만족한다.

마지막 단계는 \(g\)-vector comparison maps이다. 이 예시에서 matrices는
$$
N_{\mathbf i}
=
\begin{pmatrix}
1&0&-1\\
0&1&0\\
0&0&1
\end{pmatrix},
\qquad
M_{\mathbf i}
=
\begin{pmatrix}
1&1&0\\
0&1&1\\
0&0&1
\end{pmatrix}
$$
이고, 따라서
$$
\mathcal N_{\mathbf i}(a_1,a_2,a_3)
=
(a_1-a_3,a_2,a_3),
\qquad
\mathcal M_{\mathbf i}(l_1,l_2,l_3)
=
(l_1+l_2,l_2+l_3,l_3).
$$
또한
$$
N_{\mathbf i}^{-1}
=
\begin{pmatrix}
1&0&1\\
0&1&0\\
0&0&1
\end{pmatrix},
\qquad
M_{\mathbf i}^{-1}
=
\begin{pmatrix}
1&-1&1\\
0&1&-1\\
0&0&1
\end{pmatrix}.
$$

이제 \(b\in\widetilde B(\infty)\)에 대해
$$
\mathrm g^{\mathrm R}_{\mathbf i}(b)=(r_1,r_2,r_3)
$$
라고 쓰면, 이 type \(A_2\) 예시에서는
$$
\mathrm g^{\mathrm L}_{\mathbf i}(b)
=
\bigl(
r_1,\,
r_2-\min\{r_1,0\},\,
r_3+\min\{r_1,0\}
\bigr).
$$

## 핵심 관점

이 theorem-level topic의 핵심은 하나의 localized crystal element를 네 방식으로 읽는 것이다.

1. PBW-coordinate language로 읽는다.
2. String-coordinate language로 읽는다.
3. Left $g$-vector language로 읽는다.
4. Right $g$-vector language로 읽는다.

Quantum twist automorphism은 이 네 coordinate languages를 서로 섞어서 설명된다. 특히 PBW와 string 사이의 비교, 그리고 left/right $g$-vector 사이의 비교가 같은 crystal-level permutation을 중심으로 만난다.

## 기본 성질

### Same localized crystal

네 coordinate languages는 서로 다른 objects를 parametrizing하는 것이 아니다. 모두 같은 localized crystal $\widetilde B(w)$의 elements를 다른 coordinate systems로 읽는다.

### Reduced-expression dependence

이 비교는 reduced expression $\mathbf i$를 고정한 뒤 이루어진다. PBW coordinates, string coordinates, $g$-vectors가 모두 이 choice에 의존하기 때문이다.

### Nonlinear bridge

PBW coordinates와 string coordinates 사이의 bridge는 단순한 linear change of coordinates로 취급하면 안 된다. 이 점 때문에 theorem-level statement를 쓰려면 notation과 prerequisite가 먼저 안정되어야 한다.

### Formula boundary

Theorem statement는 $\mathfrak D_w$의 coordinate behavior를 다섯 formula로 기록한다. 하지만 이 formula들은 $\mathcal M_{\mathbf i}$, $\mathcal N_{\mathbf i}$의 explicit matrix entries를 표시하지 않는다. 따라서 worked example을 읽으려면 matrix entries와 PBW-string bijection을 별도로 준비해야 한다.

## 다른 topic들과의 관계

[[topics/08-localization-of-categories/quantum-twist-automorphisms|Quantum Twist Automorphisms]]는 coordinate-ring side의 automorphism을 제공한다. 이 topic은 그 automorphism이 localized crystal coordinate languages에서 어떻게 읽히는지를 다룬다.

[[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]는 비교가 일어나는 underlying crystal $\widetilde B(w)$를 제공한다.

[[topics/08-localization-of-categories/localized-pbw-parametrizations|Localized PBW Parametrizations]]와 [[topics/08-localization-of-categories/localized-string-parametrizations|Localized String Parametrizations]]는 같은 crystal을 두 coordinate languages로 읽는 준비 단계이다.

[[topics/08-localization-of-categories/left-and-right-g-vectors|Left and Right g-Vectors]]는 PBW/string coordinates와 quantum twist comparison 사이의 $g$-vector layer를 제공한다.

[[topics/01-quantum-groups/quantum-coordinate-rings|Quantum Coordinate Rings]]는 quantum twist automorphism이 작용하는 coordinate-ring-level background이다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/08-localization-of-categories/quantum-twist-automorphisms|Quantum Twist Automorphisms]], [[topics/08-localization-of-categories/localized-pbw-parametrizations|Localized PBW Parametrizations]], [[topics/08-localization-of-categories/localized-string-parametrizations|Localized String Parametrizations]], [[topics/08-localization-of-categories/left-and-right-g-vectors|Left and Right g-Vectors]].
- 상위 개념: [[topics/08-localization-of-categories/quantum-twist-automorphisms|Quantum Twist Automorphisms]].
- 다음에 읽을 것: [[topics/08-localization-of-categories/localized-root-operators|Localized Root Operators]], [[topics/02-crystal-bases/cellular-crystals|Cellular Crystals]].

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/jp25-crystals-quantum-twist-automorphisms|JP25]], local TeX lines 1826-1836: comparison diagram among localized crystal elements, localized PBW parameters, localized string parameters, and left/right \(g\)-vector parameter sets.
- JP25, local TeX lines 1838-1852: Theorem 3.2, the five displayed coordinate formulas.
- JP25, local TeX lines 1853-1860: proof of the theorem. Proof 내용은 본문에 넣지 않았다.
- JP25, local TeX lines 1888-1947: type \(A_2\) worked example used in `## 기본 예시`.

</details>
