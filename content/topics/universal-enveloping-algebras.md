---
id: universal-enveloping-algebras
title: Universal Enveloping Algebras
level: core
topic_kind: root
parent_topics: []
prerequisite_topics: []
child_topics:
  - quantum-groups
related_topics:
  - root-systems-and-weight-lattices
maturity: study-ready
---

## 개요

Universal enveloping algebra $U(L)$는 Lie algebra $L$의 bracket relation을 associative algebra 안의 commutator relation으로 실현하는 algebra이다. [[topics/quantum-groups|Quantum Groups]]의 $U_q(\mathfrak g)$는 enveloping algebra $U(\mathfrak g)$의 $q$-deformation으로 읽히기 때문에, $U(L)$는 quantum group을 읽기 위한 가장 낮은 algebra prerequisite이다.

이 topic에서는 Lie algebra $L$을 input으로 두고 $U(L)$를 만드는 방법을 중심으로 읽는다. Hopf algebra language는 이 page의 중심 topic이 아니라, $U(L)$와 $U_q(\mathfrak g)$가 tensor product representations를 다룰 수 있게 해 주는 추가 구조로 사용된다.

## 준비와 notation

$\mathbb F$를 characteristic zero field라고 하자. Lie algebra는 보통 $L$로 쓰고, bracket은
$$
[-,-]:L\times L\to L
$$
로 쓴다.

Lie algebra $L$의 universal enveloping algebra는 $U(L)$로 쓴다. Hopf algebra는 $\mathcal H$로 쓰고, 구조 maps는
$$
\mu:\mathcal H\otimes\mathcal H\to\mathcal H,\qquad
\Delta:\mathcal H\to\mathcal H\otimes\mathcal H,
$$
$$
\iota:\mathbb F\to\mathcal H,\qquad
\varepsilon:\mathcal H\to\mathbb F,\qquad
S:\mathcal H\to\mathcal H
$$
로 쓴다. 여기서 $\mu$는 multiplication, $\Delta$는 comultiplication, $\iota$는 unit, $\varepsilon$은 counit, $S$는 antipode이다.

## 정의

### Lie algebra

Lie algebra $L$은 $\mathbb F$-vector space와 bilinear bracket
$$
[-,-]:L\times L\to L
$$
로 이루어지며, 모든 $x,y,z\in L$에 대해
$$
[x,x]=0
$$
와 Jacobi identity
$$
[x,[y,z]]+[y,[z,x]]+[z,[x,y]]=0
$$
를 만족한다. 첫 조건은 bracket이 anti-commutative가 되게 하고, Jacobi identity는 bracket이 Lie algebra structure를 이루게 하는 핵심 조건이다.

### Universal enveloping algebra

Universal enveloping algebra $U(L)$는 $L$을 포함하는 associative algebra로, $x,y\in L$에 대해
$$
xy-yx=[x,y]
$$
라는 관계를 만족하도록 만든다. 동등하게, $L$에서 임의의 associative algebra $A$의 commutator Lie algebra로 가는 Lie algebra homomorphism은 $U(L)$에서 $A$로 가는 algebra homomorphism으로 유일하게 연장된다.

### Hopf algebra structure

Hopf algebra language를 사용할 때는 다음 구조를 뜻한다. Hopf algebra $\mathcal H$는 algebra $(\mathcal H,\mu,\iota)$와 coalgebra $(\mathcal H,\Delta,\varepsilon)$를 동시에 갖는 object이다. 여기서 $\Delta$와 $\varepsilon$는 algebra maps로서 multiplication/unit과 호환된다. Antipode $S:\mathcal H\to\mathcal H$는
$$
\mu(S\otimes \operatorname{id})\Delta
=
\iota\varepsilon
=
\mu(\operatorname{id}\otimes S)\Delta
$$
를 만족한다. 이 식이 multiplication, comultiplication, unit, counit, antipode를 하나의 Hopf algebra structure로 묶는 조건이다.

## 기본 예시

### 실제 예시

$\mathfrak{sl}_2(\mathbb F)$는 basis $h,e,f$를 갖는 three-dimensional Lie algebra로 볼 수 있고, bracket relations는
$$
[h,e]=2e,\qquad [h,f]=-2f,\qquad [e,f]=h
$$
이다.

Universal enveloping algebra $U(\mathfrak{sl}_2)$에서는 같은 relations가 associative algebra 안의 commutator relations로 바뀐다.
$$
he-eh=2e,\qquad hf-fh=-2f,\qquad ef-fe=h.
$$

검증: 논문 예시

## 핵심 관점

Lie algebra에서 quantum group으로 가는 가장 기본적인 흐름은 다음과 같다.

$$
L
\longrightarrow
U(L)
\leadsto
U_q(\mathfrak g)
$$

$L$은 bracket을 가진 infinitesimal object이고, $U(L)$은 $L$의 representations를 associative algebra representations로 다룰 수 있게 만든다. Hopf algebra structure는 $U(L)$-modules의 tensor products와 duals를 다루게 해 주며, quantum group에서도 같은 역할을 한다.

## 기본 성질

### 정의적 사실

- Lie algebra $L$의 representation on $V$는 Lie algebra homomorphism $L\to\mathfrak{gl}(V)$이다.
- $L$-module은 compatible $L$-action을 가진 vector space이다. 이 module language가 $U(L)$로 넘어가기 전의 representation language이다.
- Universal enveloping algebra $U(L)$는 $L$이 생성하고 $xy-yx=[x,y]$ relation을 만족하는 associative algebra이다.

### 정리

- Poincare-Birkhoff-Witt theorem은 $L$의 ordered basis에서 만든 ordered monomials가 $U(L)$의 basis를 이룬다고 말한다.

### 구조

- Universal enveloping algebra $U(L)$는 Hopf algebra structure를 갖고, $x\in L$에 대해
  $$
  \Delta(x)=x\otimes 1+1\otimes x,\qquad
  \varepsilon(x)=0,\qquad
  S(x)=-x
  $$
  가 성립한다.

## 다른 topic들과의 관계

**Quantum groups.** [[topics/quantum-groups|Quantum Groups]]는 enveloping algebra picture를 처음부터 대체하지 않고 $q$-deform한다. $U_q(\mathfrak g)$의 generators $e_i$, $f_i$, Cartan terms는 $U(\mathfrak{sl}_2)$에서 $e$, $f$, $h$가 어떻게 작용하는지 본 뒤에 읽는 것이 자연스럽다.

**Root systems and weight lattices.** [[topics/root-systems-and-weight-lattices|Root Systems and Weight Lattices]]는 quantum group을 정의하기 전에 필요한 root와 weight data를 정리한다.

**Crystal bases.** [[topics/crystal-bases|Crystal Bases]]는 quantum group modules에서 combinatorial structure를 뽑아낸다. Hopf algebra language는 representation의 tensor product가 왜 자연스럽게 배경에 들어오는지 설명한다.

## 더 읽을 topic

- 먼저 읽을 것: 이 page를 algebra prerequisite의 출발점으로 읽는다.
- 상위 개념: 별도의 상위 topic 없이 enveloping algebra 쪽의 출발점으로 읽는다.
- 다음에 읽을 것: [[topics/quantum-groups|Quantum Groups]]에서는 $q$-deformed enveloping algebra를 읽고, [[topics/root-systems-and-weight-lattices|Root Systems and Weight Lattices]]에서는 Lie-theoretic representation에 붙는 root와 weight data를 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/books/hong-kang02-introduction-quantum-groups-crystal-bases|Hong-Kang 2002]], Chapter 1, Definition 1.1.1, pp.1-2: Lie algebra definition.
- Hong-Kang 2002, Chapter 1, Definition 1.2.1, p.3: representations and $L$-modules.
- Hong-Kang 2002, Chapter 1, Definition 1.2.3 and Theorem 1.2.4, pp.4-5: universal enveloping algebra and PBW theorem.
- Hong-Kang 2002, Chapter 1, Section 1.3, p.6: $\mathfrak{sl}_2$ basis and relations.
- Hong-Kang 2002, Chapter 1, Definition 1.5.3 and Example 1.5.4(3), pp.17-18: Hopf algebra definition and $U(L)$ as a Hopf algebra.

</details>
