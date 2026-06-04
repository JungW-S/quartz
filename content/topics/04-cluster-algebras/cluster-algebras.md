---
id: cluster-algebras
title: Cluster Algebras
level: core
topic_kind: root
parent_topics: []
prerequisite_topics: []
child_topics:
  - quantum-cluster-algebras
related_topics:
  - monoidal-categorification
maturity: example-ready
---

## 개요

Cluster algebra는 rational function field 안에서 seed를 mutation으로 바꾸어 가며 얻는 cluster variables들이 생성하는 $\mathbb Z$-subalgebra이다. 하나의 고정된 generating set만 쓰는 대신, 서로 mutation으로 연결된 여러 cluster를 통해 같은 algebra를 읽는다.

이 구조는 어떤 variables를 한꺼번에 coordinate처럼 사용할 수 있는지, 그리고 한 cluster에서 다른 cluster로 넘어갈 때 algebra가 어떻게 유지되는지를 기록한다. Representation theory 쪽에서는 monoidal categorification, quantum cluster algebra, 그리고 quantum coordinate ring을 읽기 위한 cluster-algebra-level language로 쓰인다.

Seed, mutation, cluster variables, cluster monomials는 따로 topic으로 쪼개지 않고 이 topic 안에서 함께 읽는다. 이 네 단어가 하나의 mechanism을 이루기 때문이다.

## 준비와 notation

$J$를 finite index set이라고 하고, exchangeable indices와 frozen indices를
$$
J=J_{\mathrm{ex}}\sqcup J_{\mathrm{fr}}
$$
로 나눈다. Exchangeable index는 mutation을 할 수 있는 방향이고, frozen index는 seed 안에 남아 있지만 mutation 방향으로 쓰지 않는 index이다.

초기 변수들을
$$
\{x_i\}_{i\in J}
$$
라고 쓰고, 이들이 rational function field
$$
\mathbb Q(x_i\mid i\in J)
$$
안에서 algebraically independent라고 둔다. Exchange matrix는
$$
\widetilde B=(b_{ij})_{i\in J,\ j\in J_{\mathrm{ex}}}
$$
로 쓴다. Principal part는 $J_{\mathrm{ex}}\times J_{\mathrm{ex}}$ 부분행렬이며, 여기서는 skew-symmetric인 경우를 기본 모델로 둔다.

Seed는 pair
$$
S=(\{x_i\}_{i\in J},\widetilde B)
$$
이다. Seed 안의 변수 집합 $\{x_i\}_{i\in J}$를 cluster라고 부르고, 그 원소를 cluster variables라고 부른다.

## 정의

초기 seed
$$
S_0=(\{x_i\}_{i\in J},\widetilde B)
$$
가 주어졌다고 하자. 이 seed에 mutation을 반복해서 얻는 모든 seed들에 등장하는 모든 cluster variables를 모아, 그들이 생성하는 subalgebra
$$
\mathcal A(S_0)\subset \mathbb Q(x_i\mid i\in J)
$$
를 cluster algebra라고 한다.

Mutation in direction $k\in J_{\mathrm{ex}}$는 seed의 변수 $x_k$를 새 변수 $x_k'$로 바꾼다. 이때
$$
x_k'
=
\frac{
\prod_{b_{ik}\ge 0}x_i^{b_{ik}}
+
\prod_{b_{ik}\le 0}x_i^{-b_{ik}}
}{x_k}.
$$
다른 변수 $x_i$는 $i\ne k$일 때 그대로 둔다.

Exchange matrix도 함께 바뀐다. Mutated matrix $\mu_k(\widetilde B)=(b'_{ij})$는
$$
b'_{ij}
=
\begin{cases}
-b_{ij}, & i=k\text{ or }j=k,\\
b_{ij}+(-1)^{\delta(b_{ik}<0)}\max(b_{ik}b_{kj},0),
& \text{otherwise}
\end{cases}
$$
로 주어진다.

Cluster monomial은 하나의 cluster 안에 동시에 들어 있는 cluster variables들의 monomial이다. 즉 서로 다른 mutation stage에서 따로 나온 변수들을 마음대로 섞은 monomial이 아니라, 한 seed의 cluster 안에서 만들어지는 monomial이다.

## 기본 예시

Rank-two skew-symmetric seed를 보자. 초기 cluster를 $\{x_1,x_2\}$로 두고 exchange matrix를
$$
B=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}
$$
로 둔다. Direction $1$에서 mutation하면 첫 번째 변수는
$$
x_1'
=
\frac{1+x_2}{x_1}
$$
로 바뀌고, 새 cluster는
$$
\{x_1',x_2\}
=
\left\{\frac{1+x_2}{x_1},x_2\right\}
$$
가 된다. Exchange matrix는
$$
B'=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}
$$
로 바뀐다.

이 예시에서 초기 cluster의 cluster monomials는 $x_1^a x_2^b$ 꼴이다. Mutation 뒤 cluster에서 만드는 cluster monomials는
$$
(x_1')^a x_2^b
=
\left(\frac{1+x_2}{x_1}\right)^a x_2^b
$$
꼴이다. 여기서 $a,b$는 nonnegative integers이다. 중요한 점은 $x_1$과 $x_1'$가 서로 다른 cluster에 속한다는 것이다. 따라서 cluster monomial을 말할 때는 어느 cluster 안에서 monomial을 만들고 있는지 함께 보아야 한다.

검증: Sage 계산 `sage scripts/examples/cluster-algebras/rank2_a2_one_mutation.sage`

## 핵심 관점

Cluster algebra의 기본 그림은 다음과 같다.

$$
\text{initial seed}
\xrightarrow{\ \mu_k\ }
\text{new seed}
\xrightarrow{\ \mu_\ell\ }
\text{another seed}
\xrightarrow{\ \cdots\ }
\text{mutation class of seeds}.
$$

각 seed는 algebra를 표현하는 하나의 cluster of variables를 제공한다. Mutation은 한 cluster에서 인접한 cluster로 넘어가는 규칙이고, cluster algebra는 mutation class 전체에서 나타나는 cluster variables가 생성하는 algebra이다.

Monoidal categorification으로 가면 이 그림은 category 안의 object들로 옮겨 간다. Cluster variable은 object의 class $[M]$로 나타나고, cluster monomial은 같은 cluster에 속하는 variables의 product이므로 category side에서는 compatible한 simple objects의 product와 대응한다.

## 기본 성질

**Laurent phenomenon.** Mutation으로 얻은 cluster variables는 초기 cluster variables에 대한 Laurent polynomial로 표현된다.

**Cluster monomial의 제한.** Cluster monomial은 하나의 cluster 안에서 만든 monomial이다. 이 조건 때문에 cluster monomial은 단순히 cluster variables 전체로 만든 임의의 monomial보다 더 제한된 object이다.

**Monoidal categorification에서의 의미.** Monoidal categorification이 주어지면 cluster monomials는 category의 real simple objects의 classes로 나타난다. 따라서 cluster-algebra-level statement를 object-level statement로 들어 올려서 볼 수 있다.

**Quantum 방향.** Quantum cluster algebra는 cluster variables 사이의 commutation을 skew-symmetric matrix로 조절하는 $q$-analogue이다. 이 방향은 [[topics/04-cluster-algebras/quantum-cluster-algebras|Quantum Cluster Algebras]]에서 따로 읽는다.

## 다른 topic들과의 관계

- [[topics/04-cluster-algebras/quantum-cluster-algebras|Quantum Cluster Algebras]]는 cluster algebra의 $q$-deformed version이다. Classical cluster algebra의 seed와 mutation language를 먼저 알아야 quantum seed의 추가 matrix data를 읽을 수 있다.
- [[topics/05-monoidal-categorification/monoidal-categorification|Monoidal Categorification]]은 cluster algebra를 monoidal category의 Grothendieck ring으로 실현한다. 이때 cluster variables와 cluster monomials가 categorical objects의 classes로 바뀐다.
- [[topics/01-quantum-groups/quantum-coordinate-rings|Quantum Coordinate Rings]]에서는 quantum coordinate ring $A_q(\mathfrak n(w))$가 quantum cluster algebra와 isomorphic하게 나타난다. Cluster algebra language는 coordinate-ring-level target을 읽기 위한 algebraic coordinate system 역할을 한다.

## 더 읽을 topic

- 먼저 읽을 것: rational function field, Laurent polynomial, matrix mutation을 다룰 수 있으면 이 topic을 시작할 수 있다.
- 상위 개념: Cluster algebra 학습 경로의 출발점이다.
- 다음에 읽을 것: [[topics/04-cluster-algebras/quantum-cluster-algebras|Quantum Cluster Algebras]]에서 $q$-analogue를 읽고, [[topics/05-monoidal-categorification/monoidal-categorification|Monoidal Categorification]]에서 cluster algebra가 category의 Grothendieck ring으로 나타나는 방식을 읽고, [[topics/01-quantum-groups/quantum-coordinate-rings|Quantum Coordinate Rings]]에서 quantum coordinate ring과의 비교를 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kkko14-monoidal-categorification-cluster-algebras|KKKO14]], Introduction, pp.1-2: cluster algebra as a subalgebra of a rational function field generated by cluster variables grouped into clusters, mutation, cluster monomials, Laurent phenomenon, and the quantum-cluster direction.
- KKKO14, Section 5.1, p.30: recalled definition of a cluster algebra with initial seed, exchange relation for $x_k'$, matrix mutation, and monoidal categorification definition.
- Sage verification script `scripts/examples/cluster-algebras/rank2_a2_one_mutation.sage`: verifies the displayed rank-two one-step mutation \(x_1'=(1+x_2)/x_1\) and \(B'=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\).
- KKKO14, Definition 5.3, p.30: cluster monomials appear as classes of real simple objects under monoidal categorification.
- [[sources/papers/gls11-cluster-structures-quantum-coordinate-rings|GLS11]], Theorem 12.3, pp.43-44: quantum cluster algebra attached to $\mathcal C_w$ is isomorphic to $A_q(\mathfrak n(w))$.

</details>
