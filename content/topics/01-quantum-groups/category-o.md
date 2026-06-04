---
id: category-o
title: Quantum Category O
level: advanced
topic_kind: category
parent_topics:
  - quantum-groups
  - weight-modules
prerequisite_topics:
  - quantum-groups
  - weight-modules
  - highest-weight-modules
child_topics:
  - verma-modules
related_topics:
  - highest-weight-modules
  - root-of-unity-quantum-groups
maturity: example-ready
---

## 개요

Quantum Category O는 Hong-Kang의 notation에서 $\mathcal O^q$로 쓰는 category이다. 이 category는 $U_q(\mathfrak g)$-modules 중에서 weight-space decomposition을 갖고, 각 weight space가 finite-dimensional이며, weights가 유한 개의 downward regions 안에 들어가는 modules를 모은다.

따라서 $\mathcal O^q$는 모든 weight modules보다 좁고, highest-weight modules와 Verma modules를 다루기에 충분히 안정적인 category-level setting이다. 여기서는 classical BGG category $\mathcal O$ 전체가 아니라, Hong-Kang의 quantum-group category $\mathcal O^q$를 다룬다.

이 topic은 [[topics/01-quantum-groups/weight-modules|Weight Modules]] 다음에 온다. Weight module은 decomposition만 요구하지만, $\mathcal O^q$는 finite-dimensional weight spaces와 boundedness condition을 추가한다. [[topics/01-quantum-groups/verma-modules|Verma Modules]]는 이 setting에서 가장 중요한 universal highest-weight modules로 들어온다.

## 준비와 notation

$U_q(\mathfrak g)$를 quantum group이라고 하자. Weight lattice는 $P$로 쓰고, dual weight lattice는 $P^\vee$로 쓴다. $V^q$는 $U_q(\mathfrak g)$-module이다.

$V^q$가 weight module이면
$$
V^q=\bigoplus_{\mu\in P}V^q_\mu
$$
이고,
$$
V^q_\mu
=
\{v\in V^q\mid q^h v=q^{\mu(h)}v
\text{ for all }h\in P^\vee\}
$$
이다.

Weights의 set은
$$
\operatorname{wt}(V^q)
=
\{\mu\in P\mid V^q_\mu\ne0\}
$$
로 쓴다.

$\lambda\in P$에 대해 Hong-Kang은
$$
D(\lambda)=\{\mu\in P\mid \mu\le \lambda\}
$$
를 사용한다. 여기서 $\le$는 weight lattice 위의 standard root order이다.

## 정의

Category $\mathcal O^q$의 objects는 다음 조건을 만족하는 $U_q(\mathfrak g)$-modules $V^q$이다.

- $V^q$는 weight module이다.
- 모든 weight space $V^q_\mu$는 finite-dimensional이다.
- 어떤 유한 개의 weights $\lambda_1,\ldots,\lambda_s\in P$가 존재해서
  $$
  \operatorname{wt}(V^q)
  \subset
  D(\lambda_1)\cup\cdots\cup D(\lambda_s)
  $$
  를 만족한다.

즉 $\mathcal O^q$는 weight spaces가 finite-dimensional이고, weights가 유한 개의 downward regions 안에 들어가는 $U_q(\mathfrak g)$-modules를 모은 category이다.

Hong-Kang은 같은 section에서 integrable subcategory
$$
\mathcal O^q_{\mathrm{int}}
$$
도 정의한다. $V^q\in\mathcal O^q_{\mathrm{int}}$라는 것은 $V^q$가 위의 $\mathcal O^q$ 조건을 만족하고, 모든 $i\in I$에 대해 $e_i$와 $f_i$가 $V^q$ 위에서 locally nilpotent로 작용한다는 뜻이다.

## 기본 예시

### 실제 예시: highest-weight modules

Hong-Kang은 $\mathcal O^q$ 안의 중요한 examples로 highest-weight modules를 둔다. Highest weight $\lambda$를 갖는 highest-weight module $V^q$에는 nonzero vector $v_\lambda$가 있어서
$$
e_i v_\lambda=0\quad(i\in I),
\qquad
q^h v_\lambda=q^{\lambda(h)}v_\lambda\quad(h\in P^\vee),
$$
그리고
$$
V^q=U_q(\mathfrak g)v_\lambda
$$
가 성립한다.

Hong-Kang은 이 경우
$$
\dim V^q_\lambda=1,\qquad
\dim V^q_\mu<\infty,
\qquad
V^q=\bigoplus_{\mu\le \lambda}V^q_\mu
$$
를 기록한다. 따라서 weights는 $D(\lambda)$ 안에 있고, $V^q$는 $\mathcal O^q$의 object가 된다.

검증: 논문 예시

## 핵심 관점

$\mathcal O^q$의 condition은 weight module을 category-level로 다루기 위한 finiteness condition이다.

- Weight condition은 Cartan part의 eigenvalue decomposition을 요구한다.
- Finite-dimensional weight-space condition은 각 weight에서 multiplicity가 finite임을 요구한다.
- Boundedness condition은 weights가 유한 개의 upper bounds 아래에 놓이도록 제한한다.

이 세 조건 때문에 $\mathcal O^q$는 arbitrary $U_q(\mathfrak g)$-modules보다 좁고, highest-weight modules와 Verma modules를 다루기에 적합한 category가 된다.

## 기본 성질

### Weight module 조건의 안정성

- Hong-Kang Proposition 3.2.1은 $U_q(\mathfrak g)$ 위의 weight module의 submodule도 다시 weight module이라고 말한다.
- Hong-Kang의 highest-weight modules는 $\mathcal O^q$ 안에 놓인다.
- $\mathcal O^q_{\mathrm{int}}$는 $\mathcal O^q$ 안의 integrable $U_q(\mathfrak g)$-modules로 이루어진다.

### Integrable subcategory $\mathcal O^q_{\mathrm{int}}$

Hong-Kang Definition 3.2.3은 $\mathcal O^q$ 조건에 모든 $e_i$와 $f_i$의 local nilpotence를 추가해서 $\mathcal O^q_{\mathrm{int}}$를 정의한다. Hong-Kang은 $\mathcal O^q_{\mathrm{int}}$가 finite direct sums와 tensor products에 대해 닫혀 있다고 기록한다.

## 다른 topic들과의 관계

**Weight Modules.** [[topics/01-quantum-groups/weight-modules|Weight Modules]]는 $\mathcal O^q$ 정의에 필요한 weight-space decomposition과 character notation을 제공한다.

**Highest-Weight Modules.** [[topics/01-quantum-groups/highest-weight-modules|Highest-Weight Modules]]는 $\mathcal O^q$ 안에 들어가는 기본 example class를 제공한다.

**Verma Modules.** [[topics/01-quantum-groups/verma-modules|Verma Modules]]는 이 representation-theoretic setting 안의 universal highest-weight module $M^q(\lambda)$를 다루는 topic이다.

**Quantum Groups.** [[topics/01-quantum-groups/quantum-groups|Quantum Groups]]는 ambient module category를 만드는 algebra $U_q(\mathfrak g)$를 정의한다.

**Root-of-Unity Quantum Groups.** [[topics/01-quantum-groups/root-of-unity-quantum-groups|Root-of-Unity Quantum Groups]]는 generic category $\mathcal O^q$가 아니라 $q$를 root of unity로 specialize한 뒤의 representation theory를 다룬다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/01-quantum-groups/weight-modules|Weight Modules]]에서 weight-space decomposition을 읽고, [[topics/01-quantum-groups/highest-weight-modules|Highest-Weight Modules]]에서 highest-weight vector와 highest-weight module의 기본 형태를 읽는다.
- 상위 개념: [[topics/01-quantum-groups/quantum-groups|Quantum Groups]]는 ambient algebra $U_q(\mathfrak g)$를 제공하고, [[topics/01-quantum-groups/weight-modules|Weight Modules]]는 $\mathcal O^q$가 추가로 제한하는 더 큰 module class이다.
- 다음에 읽을 것: [[topics/01-quantum-groups/verma-modules|Verma Modules]]에서 $\mathcal O^q$ 안의 universal highest-weight module을 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/books/hong-kang02-introduction-quantum-groups-crystal-bases|Hong-Kang 2002]], Section 3.2, printed p.43: definition of \(\mathcal O^q\), the sets \(D(\lambda)\), weight-space finiteness, boundedness of weights, and Proposition 3.2.1.
- Hong-Kang 2002, Section 3.2, printed pp.43-44: highest-weight modules as the main examples in \(\mathcal O^q\).
- Hong-Kang 2002, Definition 3.2.3, printed p.45: definition of \(\mathcal O^q_{\mathrm{int}}\), local nilpotence of \(e_i,f_i\), and closure under finite direct sums and tensor products.

</details>
