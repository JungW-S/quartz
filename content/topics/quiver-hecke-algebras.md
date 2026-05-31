---
id: quiver-hecke-algebras
title: Quiver-Hecke Algebras
level: core
topic_kind: root
parent_topics: []
prerequisite_topics:
  - root-systems-and-weight-lattices
child_topics:
  - quiver-hecke-algebra-localization
  - determinantial-modules
related_topics:
  - monoidal-categorification
  - quantum-groups
maturity: definition-ready
---

# Quiver-Hecke Algebras

## What it is

Quiver-Hecke algebra, 또는 KLR algebra는 quiver와 그 quiver에서 얻는 Cartan datum에 붙는 graded algebra family이다. 하나의 positive root $\alpha\in Q_+$마다 algebra $H_\alpha$가 있고, 이 algebra들의 graded module category가 quantum group의 한쪽 절반과 monoidal categorification을 연결한다.

## Why it appears

Quantum group에는 generators와 Serre relations로 주어지는 algebraic object가 있다. Quiver-Hecke algebra는 이 관계들을 module category 수준에서 실현한다. 그래서 Grothendieck group으로 내려가면 quantum group의 구조가 나타나고, 위에서는 induction과 restriction functors가 multiplication과 comultiplication의 역할을 한다.

Monoidal categorification에서는 algebra multiplication을 module category의 convolution product로 해석한다. Quiver-Hecke algebra의 finite-dimensional graded modules는 real simple modules, commuting families, determinantial modules, 그리고 localized categories가 놓이는 category-level 배경을 제공한다.

## Setup and notation

Loop-free quiver의 finite vertex set을 $I$라고 하자. $m_{ij}$는 directed edges $i\to j$의 개수이고, associated symmetric Cartan matrix는
$$
c_{ii}=2,\qquad c_{ij}=-m_{ij}-m_{ji}\quad (i\ne j)
$$
로 둔다. Simple roots는 $\alpha_i$, root lattice의 positive cone은
$$
Q_+=\bigoplus_{i\in I}\mathbb N\alpha_i
$$
로 쓴다.

$\alpha=\sum_i c_i\alpha_i\in Q_+$의 height는 $\operatorname{ht}(\alpha)=\sum_i c_i$이다. $\operatorname{ht}(\alpha)=n$이면 $\langle I\rangle_\alpha$는 letters $i_1,\ldots,i_n\in I$로 된 words
$$
\mathbf i=i_1\cdots i_n
$$
중에서 $\alpha_{i_1}+\cdots+\alpha_{i_n}=\alpha$를 만족하는 것들의 집합이다. Transposition $t_k\in S_n$은 word의 $k$번째와 $(k+1)$번째 letters를 바꾼다.

Brundan의 notation에서는 quiver-Hecke algebra를 $H_\alpha$로 쓴다. 관련 advanced topic pages에서는 같은 종류의 algebra를 generic하게 $R$로 쓰고, finite-dimensional graded modules의 category를 $R\text{-gmod}$로 쓴다. 두 module object $M,N$의 convolution product는
$$
M\circ N
$$
으로 쓴다.

## Definition

$\alpha\in Q_+$의 height가 $n$일 때, symmetric quiver-Hecke algebra $H_\alpha$는 다음 generators와 relations로 정의되는 associative graded algebra이다.

Generators는 word idempotents, dots, crossings이다.
$$
\{1_{\mathbf i}\mid \mathbf i\in \langle I\rangle_\alpha\},\qquad
x_1,\ldots,x_n,\qquad
\tau_1,\ldots,\tau_{n-1}.
$$

여기서 $1_{\mathbf i}$는 word $\mathbf i$에 해당하는 orthogonal idempotent이고, $x_k$는 $k$번째 strand의 dot처럼 생각할 수 있으며, $\tau_k$는 $k$번째와 $(k+1)$번째 strands의 crossing처럼 생각할 수 있다.

Relations의 핵심은 다음과 같다.

- $1_{\mathbf i}$들은 서로 orthogonal idempotents이고 합은 identity $1_\alpha$이다.
- $x_1,\ldots,x_n$은 서로 commute한다.
- $1_{\mathbf i}x_k=x_k1_{\mathbf i}$이고 $1_{\mathbf i}\tau_k=\tau_k1_{t_k(\mathbf i)}$이다.
- Dot과 crossing은
$$
(\tau_kx_l-x_{t_k(l)}\tau_k)1_{\mathbf i}
=\delta_{i_k,i_{k+1}}(\delta_{k+1,l}-\delta_{k,l})1_{\mathbf i}
$$
를 만족한다.
- Crossing square는
$$
\tau_k^2 1_{\mathbf i}
=q_{i_k,i_{k+1}}(x_k,x_{k+1})1_{\mathbf i}
$$
로 제어된다. Brundan의 symmetric normalization에서는 $i\ne j$일 때
$$
q_{ij}(u,v)=(v-u)^{m_{ij}}(u-v)^{m_{ji}},
$$
이고 $i=j$이면 $q_{ij}=0$이다.
- 멀리 떨어진 crossings는 commute하고, 인접한 세 crossings는 quiver data에 따라 correction term이 붙은 braid relation을 만족한다.

Grading은
$$
\deg 1_{\mathbf i}=0,\qquad \deg x_j=2,\qquad
\deg(\tau_k1_{\mathbf i})=-\alpha_{i_k}\cdot\alpha_{i_{k+1}}
$$
로 주어진다.

## Basic picture

Quiver-Hecke algebra의 generators는 diagram으로 읽을 수 있다. Word $\mathbf i=i_1\cdots i_n$는 색깔이 붙은 $n$개의 strands이고, $x_k$는 $k$번째 strand 위의 dot, $\tau_k$는 인접한 두 strands의 crossing이다.

Vertical concatenation은 morphism composition이고, horizontal concatenation은 tensor product이다. 이 diagrammatic picture 때문에 algebra relation을 braid-like diagrams의 local move로 볼 수 있다.

$$
H_\alpha
\quad\leadsto\quad
\operatorname{Rep}(H_\alpha)
\quad\leadsto\quad
\text{Grothendieck group}
\quad\leadsto\quad
\text{half of a quantum group}
$$

Algebra $H_\alpha$ 자체는 object-level input이다. Module category와 induction product는 category-level structure이고, Grothendieck group은 quantum-group-level structure를 회복하는 곳이다.

## Example

### Concrete example

한 vertex $i$만 반복되는 경우를 보자. $\alpha=n\alpha_i$이면 Brundan의 normalization에서 $H_{n\alpha_i}$는 nil Hecke algebra $NH_n$의 copy가 된다. 이 경우에는 idempotent가 하나뿐이고, generators $x_1,\ldots,x_n$과 $\tau_1,\ldots,\tau_{n-1}$가 nil Hecke relations를 만족한다.

Type $A_2$의 quiver underlying graph가 $1-2$이고 $\alpha=\alpha_1+\alpha_2$일 때도 작은 그림을 볼 수 있다. 이 경우 irreducible graded $H_\alpha$-modules는 degree shift를 제외하면 one-dimensional modules $L(12)$와 $L(21)$ 두 개이고, Brundan은 이 algebra가 two-vertex quiver의 path algebra와 polynomial algebra $K[x]$의 tensor product로 나타난다고 설명한다.

이 예시는 $H_\alpha$가 단순히 추상적인 presentation이 아니라, 작은 root에서는 path algebra와 modules로 직접 볼 수 있는 algebra임을 보여 준다.

## Main facts

### Theorem

Brundan의 basis theorem에 따르면, reduced expressions를 하나씩 고정하면 monomials
$$
x_1^{m_1}\cdots x_n^{m_n}\tau_w1_{\mathbf i}
$$
가 $H_\alpha$의 basis를 이룬다. 여기서 $\mathbf i\in\langle I\rangle_\alpha$, $w\in S_n$, $m_1,\ldots,m_n\ge 0$이다. 따라서 generators와 relations는 실제 계산 가능한 basis model을 준다.

### Theorem

Khovanov-Lauda categorification theorem은 Lusztig algebra $f$의 integral form과 quiver-Hecke projective modules의 Grothendieck group 사이에 twisted bialgebra isomorphism이 있음을 말한다.
$$
f_{\mathbb Z[q,q^{-1}]}\cong [\operatorname{Proj}(H)].
$$
Generator $\theta_i$는 projective module class $[H_{\alpha_i}]$로 간다. 이 명제는 quiver-Hecke algebra가 quantum group의 절반을 categorify한다는 정확한 형태이다.

### Interpretation

Finite-dimensional graded $H_\alpha$-modules의 categories를 모으면 induction과 restriction을 통해 multiplication과 comultiplication을 갖는다. 이 구조가 $R\text{-gmod}$, real simple modules, determinantial modules, localized categories를 다룰 때 쓰이는 category-level 배경이다.

## Why it matters

Quiver-Hecke algebras는 root-system data와 quantum-group data를 module categories로 바꾸는 장치이다. 그래서 algebra-level presentation, category-level induction product, Grothendieck-ring-level categorification을 한 줄로 연결한다.

Advanced topics에서는 이 전체 machinery가 자주 압축되어 나타난다. Determinantial modules는 quiver-Hecke module category 안의 특별한 simple modules이고, quiver-Hecke algebra localization은 그런 category 안에서 특정 objects를 invertible하게 만드는 construction이다. 따라서 $H_\alpha$의 기본 definition을 이해하면 localized crystals와 monoidal categorification의 category-level 문장을 읽을 준비가 된다.

## Connections

- [[topics/root-systems-and-weight-lattices|Root Systems and Weight Lattices]]: $I$, $\alpha_i$, $Q_+$, height, Cartan matrix notation을 제공한다.
- [[topics/quantum-groups|Quantum Groups]]: quiver-Hecke projective modules의 Grothendieck group이 categorify하는 algebraic target이다.
- [[topics/quiver-hecke-algebra-localization|Quiver-Hecke Algebra Localization]]: determinantial objects를 invertible하게 만들어 이 module-category setting을 특수화한다.
- [[topics/determinantial-modules|Determinantial Modules]]: quiver-Hecke categories 안의 distinguished module objects이다.
- [[topics/monoidal-categorification|Monoidal Categorification]]: monoidal module categories를 사용해 cluster-algebra structures를 실현한다.
- [[topics/localized-crystals|Localized Crystals]]: $\mathcal C_w$에서 만든 localized category를 사용한다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/brundan13-quiver-hecke-algebras-categorification|Brundan 2013]], Section 2: symmetric quiver-Hecke algebra $H_\alpha$, its generators and relations, diagrammatic interpretation, nil-Hecke special case, and basis theorem. Section 3: Grothendieck-group categorification theorem.
- [[sources/papers/kkko14-monoidal-categorification-cluster-algebras|KKKO14]], Definitions 1.7 and 2.12, and Proposition 2.13: real simple modules, commuting simple modules, and convolution products in the symmetric quiver-Hecke algebra setting.
- [[sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category|Kashiwara-Nakashima 2025]], Sections 5.1-5.2: $\mathcal C_w\subset R\text{-gmod}$ and its localization.

</details>
