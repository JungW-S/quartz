---
id: quantum-groups
title: Quantum Groups
level: core
topic_kind: root
parent_topics: []
prerequisite_topics:
  - universal-enveloping-algebras
  - root-systems-and-weight-lattices
child_topics:
  - category-o
  - root-of-unity-quantum-groups
  - integral-forms-of-quantum-groups
  - universal-r-matrix
  - crystal-bases
  - quantum-coordinate-rings
related_topics:
  - yang-baxter-equation
  - dual-canonical-bases
maturity: study-ready
---

## Introduction and Historical Background

Quantum group은 Lie-theoretic representation theory를 $q$-deformation과 Hopf algebra의 언어로 다루기 위해 등장한 algebraic object이다. 가장 기본적인 모델은 Drinfeld-Jimbo quantum group $U_q(\mathfrak g)$이다. 여기서 $\mathfrak g$는 Kac-Moody algebra이고, $q$는 classical enveloping algebra $U(\mathfrak g)$를 변형하는 parameter이다.

역사적으로 quantum group은 integrable system과 [[topics/01-quantum-groups/yang-baxter-equation|Yang-Baxter equation]]에서 나온 구조를 Lie theory의 language로 정리하는 과정에서 나타났다. 그래서 이 topic의 중심 질문은 하나이다. 어떤 algebra $U_q(\mathfrak g)$를 정의하면, 그 representation theory가 classical Lie theory, tensor product, braid-type symmetry, 그리고 crystal combinatorics를 동시에 설명하는가?

이 글은 $U_q(\mathfrak g)$를 먼저 algebra로 정의하고, 그 다음 Hopf algebra structure가 tensor product representations를 만드는 이유를 설명한다. 그 뒤에 representation theory, [[topics/02-crystal-bases/crystal-bases|Crystal Bases]], [[topics/01-quantum-groups/universal-r-matrix|Universal R-Matrix]]로 이어지는 주요 방향을 짧게 배치한다.

## Definition of Quantum Group

### Mathematical definition

Cartan matrix $A=(a_{ij})_{i,j\in I}$를 갖는 symmetrizable Kac-Moody algebra $\mathfrak g$를 고정한다. 각 $i\in I$에 대해 standard symmetrized convention에 따라 $q_i$를 쓴다. Compact $k_i$-presentation에서 quantum group $U_q(\mathfrak g)$는 $\mathbb Q(q)$ 위의 unital associative algebra이고, generators는
$$
e_i,\qquad f_i,\qquad k_i^{\pm1}\qquad (i\in I)
$$
이다. Relations는 다음과 같다.

Cartan generators는 서로 commute하고 invertible이다.
$$
k_i k_j=k_jk_i,\qquad k_i k_i^{-1}=k_i^{-1}k_i=1.
$$

Cartan generators는 raising/lowering generators에 Cartan matrix를 통해 작용한다.
$$
k_i e_j k_i^{-1}=q_i^{a_{ij}}e_j,
$$
$$
k_i f_j k_i^{-1}=q_i^{-a_{ij}}f_j.
$$

기본 commutator relation은
$$
[e_i,f_j]
=
\delta_{ij}\frac{k_i-k_i^{-1}}{q_i-q_i^{-1}}.
$$
이다.

$i\ne j$일 때 quantum Serre relations는
$$
\sum_{r=0}^{1-a_{ij}}
(-1)^r
\begin{bmatrix}1-a_{ij}\\r\end{bmatrix}_{q_i}
e_i^{\,1-a_{ij}-r}e_j e_i^r
=0,
$$
$$
\sum_{r=0}^{1-a_{ij}}
(-1)^r
\begin{bmatrix}1-a_{ij}\\r\end{bmatrix}_{q_i}
f_i^{\,1-a_{ij}-r}f_j f_i^r
=0.
$$

이 relations가 $U_q(\mathfrak g)$를 정의한다. Cartan action에 대해 $e_i$는 simple root $\alpha_i$에 해당하는 양의 weight를 갖고, $f_i$는 $-\alpha_i$에 해당하는 음의 weight를 갖는다. Quantum Serre relations는 서로 다른 simple root generators 사이의 relations를 Cartan matrix의 off-diagonal entries로부터 정한다.

Hong-Kang은 Cartan part에 $q^h$ notation을 쓴다. 이 notation에서 $k_i$는 simple coroot에 대응하는 Cartan generator로 볼 수 있다.

### The rank-one example $U_q(\mathfrak{sl}_2)$

$\mathfrak g=\mathfrak{sl}_2$이면 simple-root direction이 하나뿐이다. 이 경우 quantum group $U_q(\mathfrak{sl}_2)$는
$$
E,\qquad F,\qquad K^{\pm1}
$$
로 generated되고, relations는
$$
KK^{-1}=K^{-1}K=1,
$$
$$
KEK^{-1}=q^2E,
$$
$$
KFK^{-1}=q^{-2}F,
$$
$$
[E,F]=\frac{K-K^{-1}}{q-q^{-1}}.
$$
이다. Rank one에서는 nontrivial quantum Serre relation이 없다.

Hong-Kang의 two-dimensional natural representation은 basis $v_+,v_-$를 갖고, action은
$$
E v_+=0,\qquad E v_-=v_+,
$$
$$
F v_+=v_-,\qquad F v_-=0,
$$
$$
K v_+=qv_+,\qquad K v_-=q^{-1}v_-.
$$
이다. 따라서 $v_+$와 $v_-$는 $K$-eigenvectors이고, $E$는 $v_-$를 $v_+$로 보내며, $F$는 $v_+$를 $v_-$로 보낸다.

### Classical limit

Quantum group $U_q(\mathfrak g)$는 universal enveloping algebra $U(\mathfrak g)$의 $q$-deformation이다. 적절한 specialization 또는 formal limit에서 $q\to1$로 보내면 defining relations가 classical enveloping-algebra behavior를 회복한다.

$U_q(\mathfrak g)$의 multiplication은 일반적으로 noncommutative이고, Hopf algebra coproduct는 일반적으로 cocommutative하지 않다. 이 non-cocommutativity가 tensor product representations의 순서 문제와 R-matrix structure를 만든다.

## Hopf Algebra Structure

Hopf algebra structure는 coproduct, counit, antipode로 주어진다. 위의 convention에서 coproduct는
$$
\Delta(e_i)=e_i\otimes 1+k_i\otimes e_i,
$$
$$
\Delta(f_i)=f_i\otimes k_i^{-1}+1\otimes f_i,
$$
$$
\Delta(k_i)=k_i\otimes k_i.
$$

Counit은
$$
\varepsilon(e_i)=0,\qquad \varepsilon(f_i)=0,\qquad \varepsilon(k_i)=1.
$$
를 만족한다.

Antipode는
$$
S(k_i)=k_i^{-1},\qquad S(e_i)=-k_i^{-1}e_i,\qquad S(f_i)=-f_i k_i.
$$
이다.

$V$와 $W$가 $U_q(\mathfrak g)$-modules이고 $x\in U_q(\mathfrak g)$이면, tensor product module $V\otimes W$의 action은
$$
x\cdot(v\otimes w)
=
(\rho_V\otimes\rho_W)(\Delta(x))(v\otimes w)
$$
로 정의된다. 여기서 $\rho_V$와 $\rho_W$는 각각 $V$와 $W$의 representation maps이다.

## Representation Theory

$U_q(\mathfrak g)$의 representation은 vector space $V$와 algebra homomorphism
$$
U_q(\mathfrak g)\longrightarrow \operatorname{End}(V).
$$
로 이루어진다. 동치로, generators $e_i$, $f_i$, $k_i^{\pm1}$가 $V$ 위에 작용하고 위의 defining relations를 만족한다.

기본 class들은 다음과 같다.

- **Lie algebra representations.** [[topics/01-quantum-groups/lie-algebra-representations|Lie Algebra Representations]]는 Lie algebra homomorphism $\mathfrak g\to\mathfrak{gl}(V)$와 $U(\mathfrak g)$-module language를 제공한다.
- **Weight modules.** [[topics/01-quantum-groups/weight-modules|Weight Modules]]는 module이 weight spaces로 분해되는 경우이다. 이때 $k_i$는 weight를 측정하고, $e_i$와 $f_i$는 weights를 simple roots만큼 바꾼다.
- **Highest-weight modules.** [[topics/01-quantum-groups/highest-weight-modules|Highest-Weight Modules]]는 weight vector $v$가 모든 $i\in I$에 대해 $e_i v=0$을 만족하고, module이 $v$로 generated되는 경우이다. [[topics/01-quantum-groups/category-o|Quantum Category O]]와 [[topics/01-quantum-groups/verma-modules|Verma Modules]]는 이 class에 붙은 더 세부적인 topics이다.
- **Tensor product representations.** Coproduct $\Delta$는 두 representations $V,W$로부터 tensor product representation $V\otimes W$를 만든다.
- **Characters.** [[topics/01-quantum-groups/characters-of-representations|Characters of Representations]]는 weight multiplicities를 formal sum으로 기록한다.
- **Crystal bases.** Crystal base는 $q\to0$에서 module의 raising/lowering operators가 남기는 combinatorial structure이다. [[topics/02-crystal-bases/highest-weight-crystals|Highest Weight Crystals]]와 [[topics/02-crystal-bases/crystal-bases|Crystal Bases]]가 이 object를 다룬다.
- **Specialization at roots of unity.** $q$를 root of unity로 specialize하면 generic $q$의 representation theory와 다른 module categories가 나타난다. 이 현상은 [[topics/01-quantum-groups/root-of-unity-quantum-groups|Root-of-Unity Quantum Groups]]와 [[topics/01-quantum-groups/integral-forms-of-quantum-groups|Integral Forms of Quantum Groups]]에 속한다.

## Crystal Bases and Canonical Bases

Crystal bases는 $q\to0$ limit에서 $U_q(\mathfrak g)$-module의 combinatorial structure를 남기는 basis theory이다.

Module-level formulation에서는 pair $(L,B)$를 사용한다. 여기서 $L$은 $A_0$-lattice이고, $B$는 $L/qL$의 basis이다. Kashiwara operators $\widetilde e_i$, $\widetilde f_i$는 $B\cup\{0\}$ 위에 작용한다. 이 data는 colored directed graph를 정의한다.

Abstract crystal axioms는 [[topics/02-crystal-bases/abstract-crystals|Abstract Crystals]]에 있고, tensor product rule은 [[topics/02-crystal-bases/tensor-products-of-crystals|Tensor Products of Crystals]]에 있다.

Canonical bases와 global crystal bases는 quantum group representations와 quantum coordinate rings에 붙는 basis theories이다. Coordinate-ring side의 basis language는 [[topics/01-quantum-groups/dual-canonical-bases|Dual Canonical Bases]]와 [[topics/01-quantum-groups/quantum-coordinate-rings|Quantum Coordinate Rings]]에 속한다.

## Quasitriangular Structure and R-matrix

R-matrix theory는 tensor product representations $V\otimes W$와 $W\otimes V$ 사이의 intertwiners를 다룬다.

Quasitriangular Hopf algebra에서는 universal R-matrix가 representation category의 braiding을 유도한다. Representation-level R-matrices는 [[topics/01-quantum-groups/yang-baxter-equation|Yang-Baxter Equation]]과 braid group actions에 연결된다.

Quantum-group R-matrix theory와 quiver-Hecke module theory의 specialized R-matrix technology는 서로 다른 levels의 objects를 다룬다. Quiver-Hecke 쪽 construction은 [[topics/06-quiver-hecke-klr-algebras/r-matrix-renormalization|R-Matrix Renormalization]]에 속한다.

## Relations to Other Topics

- [[topics/01-quantum-groups/universal-enveloping-algebras|Universal Enveloping Algebras]]: $U_q(\mathfrak g)$는 $U(\mathfrak g)$의 $q$-deformation이다.
- [[topics/01-quantum-groups/root-systems-and-weight-lattices|Root Systems and Weight Lattices]]: Cartan matrix, simple roots, coroots, weights가 $U_q(\mathfrak g)$의 generators, relations, weight decompositions에 들어간다.
- [[topics/01-quantum-groups/lie-algebra-representations|Lie Algebra Representations]]: Lie algebra representations provide the classical action language before the $q$-deformation.
- [[topics/01-quantum-groups/weight-modules|Weight Modules]], [[topics/01-quantum-groups/highest-weight-modules|Highest-Weight Modules]], and [[topics/01-quantum-groups/characters-of-representations|Characters of Representations]]: these topics contain the representation-theoretic prerequisites for crystal bases and character formulas.
- [[topics/02-crystal-bases/crystal-bases|Crystal Bases]]: crystal bases는 suitable $U_q(\mathfrak g)$-modules에 붙는 basis data이다.
- [[topics/01-quantum-groups/quantum-coordinate-rings|Quantum Coordinate Rings]]: quantum coordinate rings는 quantum group theory의 coordinate-ring side이다.
- [[topics/01-quantum-groups/category-o|Quantum Category O]]와 [[topics/01-quantum-groups/verma-modules|Verma Modules]]: quantum category $\mathcal O^q$와 Verma modules는 highest-weight module theory에 속한다.
- [[topics/01-quantum-groups/universal-r-matrix|Universal R-Matrix]]: universal R-matrix는 quasitriangular Hopf algebra structure와 representation category의 braiding에 관련된다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/books/hong-kang02-introduction-quantum-groups-crystal-bases|Hong-Kang 2002]], Chapter 2, Section 2.1 and Definition 2.1.1: Cartan datum, weight lattice, simple roots, and simple coroots.
- Hong-Kang 2002, Chapter 1, Definition 1.2.3 and Definition 1.5.3: universal enveloping algebra and Hopf algebra prerequisites.
- Hong-Kang 2002, Definition 2.1.3: Kac-Moody algebra associated with a Cartan datum.
- Hong-Kang 2002, Definition 3.1.1: definition of $U_q(\mathfrak g)$.
- Hong-Kang 2002, Proposition 3.1.2: Hopf algebra structure on $U_q(\mathfrak g)$.
- Hong-Kang 2002, Section 3.2: weight modules, maximal vectors, and characters.
- Hong-Kang 2002, Example 4.2.1, p.66: the $U_q(\mathfrak{sl}_2)$ two-dimensional natural representation used in the basic example.
- Kashiwara 1993 and Hong-Kang 2002 support the crystal-base reading path used here; the detailed crystal axioms are kept in the Crystal Bases chapter.
- Drinfeld 1986 and Jimbo 1985 are the standard historical references for the Drinfeld-Jimbo quantum group and the Yang-Baxter motivation.

</details>
