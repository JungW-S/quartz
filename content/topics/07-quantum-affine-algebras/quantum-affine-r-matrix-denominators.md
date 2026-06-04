---
id: quantum-affine-r-matrix-denominators
title: Quantum Affine R-Matrix Denominators
level: advanced
topic_kind: concept
parent_topics:
  - quantum-affine-algebras
prerequisite_topics:
  - quantum-affine-algebras
  - r-matrix-renormalization
  - affine-objects-in-monoidal-categories
child_topics: []
related_topics:
  - quantum-affine-schur-weyl-duality
  - quiver-hecke-module-categories
  - type-a-klr-segment-modules
maturity: example-ready
---

## 개요

Quantum affine R-matrix denominator는 quantum affine module category에서 normalized R-matrix의 singularity를 spectral-parameter ratio의 polynomial data로 기록한다. KKK18A의 quantum affine Schur-Weyl construction에서는 이 denominator의 zero order가 symmetric quiver-Hecke algebra 쪽 Cartan data와 KLR parameters를 정한다.

[[topics/07-quantum-affine-algebras/quantum-affine-schur-weyl-duality|Quantum Affine Schur-Weyl Duality]]에서는 quantum affine category와 quiver-Hecke module category를 functor로 비교한다. 그 전에 denominator data가 어떻게 quiver-Hecke input으로 바뀌는지를 따로 보아야 한다. Type $A$ 예시에서는 이 input이 [[topics/06-quiver-hecke-klr-algebras/type-a-klr-segment-modules|Type A KLR Segment Modules]]의 segment modules로 이어진다. 여기서는 functor 자체나 type $A$ localization을 다루지 않는다.

## 준비와 notation

$U_q'(\mathfrak g)$를 quantum affine algebra의 derived part라고 하자. $\mathcal C_{\mathfrak g}$는 finite-dimensional integrable $U_q'(\mathfrak g)$-modules의 category이다.

KKK18A construction에서는 각 $i\in J$에 대해 두 가지를 고른다.

- good $U_q'(\mathfrak g)$-module $V_{S(i)}$;
- spectral parameter $X(i)$.

선택된 두 modules 사이의 normalized R-matrix denominator를
$$
d_{V_{S(i)},V_{S(j)}}(z)
$$
로 쓴다. 여기서 $z$는 두 spectral parameters의 ratio를 넣는 변수이다.

## 정의

$i,j\in J$가 주어졌다고 하자. KKK18A construction에서 $d_{ij}$는 denominator
$$
d_{V_{S(i)},V_{S(j)}}(z_2/z_1)
$$
가 special ratio
$$
z_2/z_1=X(j)/X(i)
$$
에서 갖는 zero order이다.

이 수 $d_{ij}$는 $i$와 $j$ 사이의 interaction을 측정한다. KKK18A는 이 zero-order data로부터 KLR polynomial $Q_{ij}(u,v)$, Cartan matrix, 그리고 quiver $\Gamma_J$를 정한다.

중심 방향은 다음과 같다.

$$
\text{normalized R-matrix denominator}
\quad\rightsquigarrow\quad
d_{ij}
\quad\rightsquigarrow\quad
Q_{ij}(u,v),\ \Gamma_J.
$$

즉 quantum affine side의 R-matrix pole data가 quiver-Hecke side의 algebra input으로 변환된다.

## 기본 예시

### 문헌 검증 예시: type $A_{N-1}^{(1)}$

이 예시는 KKK18A Section 4.1에 근거한다. $\mathfrak g=\widehat{\mathfrak{sl}}_N$이고
$$
V=V(\varpi_1)
$$
를 $U_q'(\widehat{\mathfrak{sl}}_N)$의 fundamental representation이라고 하자. KKK18A는 $V_z\otimes V_{z'}$ 위의 normalized R-matrix denominator가
$$
d_{V,V}(z'/z)=z'/z-q^2
$$
임을 계산한다.

이제 index set을 $J=\mathbb Z$로 두고 모든 vertex에 같은 module $V$를 붙이며,
$$
X(j)=q^{2j}
$$
로 spectral parameter를 고른다. 그러면 $i,j\in\mathbb Z$에 대해
$$
\frac{X(j)}{X(i)}=q^{2(j-i)}.
$$
Denominator $z'/z-q^2$는 ratio가 $q^2$일 때 정확히 한 번 사라진다. 따라서
$$
d_{ij}=\delta(j=i+1).
$$

즉 vertex $i$에서 바로 다음 vertex $i+1$로 가는 인접성만 denominator zero order에 나타난다. 이 data가 만드는 Cartan data는 type $A_\infty$이고, 대응하는 quiver-Hecke algebra도 type $A_\infty$ KLR algebra가 된다.

## 핵심 관점

Quantum affine Schur-Weyl functor를 만들려면 source side에 quiver-Hecke algebra가 있어야 한다. KKK18A construction에서는 그 quiver-Hecke algebra를 임의로 고르는 것이 아니라, quantum affine category의 chosen modules와 R-matrix denominators에서 읽어 낸다.

그림으로는 다음과 같다.

$$
\{(V_{S(i)},X(i))\}_{i\in J}
\quad\leadsto\quad
\{d_{ij}\}_{i,j\in J}
\quad\leadsto\quad
R^J(\beta).
$$

여기서 $R^J(\beta)$는 denominator data에서 나온 KLR parameters를 사용하는 quiver-Hecke algebra이다. 따라서 denominator data는 quantum affine category에서 quiver-Hecke algebra input을 추출하는 첫 단계이다.

## 기본 성질

**KLR input 생성.** 선택된 good modules $V_s$와 spectral parameters $X(i)$가 주어지면, denominator의 zero order $d_{ij}$가 KLR polynomial $Q_{ij}(u,v)$, Cartan matrix, quiver $\Gamma_J$를 정한다.

**Zero order의 의미.** $d_{ij}$는 선택된 두 quantum affine modules 사이의 normalized R-matrix denominator가 선택된 spectral-parameter ratio에서 몇 차로 사라지는지를 측정한다. 이 수가 quiver-Hecke side에서는 vertices $i,j$ 사이의 algebraic interaction으로 바뀐다.

**범위의 경계.** 이 denominator-to-KLR-data step은 Schur-Weyl functor의 입력을 만드는 단계이다. Type $A_\infty$ KLR input 위의 concrete modules는 [[topics/06-quiver-hecke-klr-algebras/type-a-klr-segment-modules|Type A KLR Segment Modules]]에서 읽고, completed tensor bimodule, tensor functor $F_\beta$, exactness theorem은 [[topics/07-quantum-affine-algebras/quantum-affine-schur-weyl-duality|Quantum Affine Schur-Weyl Duality]]에서 다룬다.

## 다른 topic들과의 관계

**Quantum Affine Algebras.** [[topics/07-quantum-affine-algebras/quantum-affine-algebras|Quantum Affine Algebras]]는 $U_q'(\mathfrak g)$, finite-dimensional module category, spectral parameter, R-matrix language를 제공한다.

**R-Matrix Renormalization.** [[topics/06-quiver-hecke-klr-algebras/r-matrix-renormalization|R-Matrix Renormalization]]은 R-matrix와 degree/renormalization language를 제공한다.

**Affine Objects in Monoidal Categories.** [[topics/03-category-theory/affine-objects-in-monoidal-categories|Affine Objects in Monoidal Categories]]는 spectral parameter와 affinization을 category-level로 읽는 배경을 제공한다.

**Quiver-Hecke Module Categories.** [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]는 denominator data에서 나온 KLR parameters가 module category의 algebra input이 되는 방향을 제공한다.

**Type A KLR Segment Modules.** [[topics/06-quiver-hecke-klr-algebras/type-a-klr-segment-modules|Type A KLR Segment Modules]]는 type $A_\infty$ KLR input 위에서 Schur-Weyl functor에 넣을 segment modules를 제공한다.

**Quantum Affine Schur-Weyl Duality.** [[topics/07-quantum-affine-algebras/quantum-affine-schur-weyl-duality|Quantum Affine Schur-Weyl Duality]]는 이 denominator data로 만들어진 quiver-Hecke algebra와 quantum affine category를 functor로 비교한다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/07-quantum-affine-algebras/quantum-affine-algebras|Quantum Affine Algebras]], [[topics/06-quiver-hecke-klr-algebras/r-matrix-renormalization|R-Matrix Renormalization]], [[topics/03-category-theory/affine-objects-in-monoidal-categories|Affine Objects in Monoidal Categories]].
- 상위 개념: [[topics/07-quantum-affine-algebras/quantum-affine-algebras|Quantum Affine Algebras]].
- 다음에 읽을 것: type $A$ 예시 흐름을 따라가려면 먼저 [[topics/06-quiver-hecke-klr-algebras/type-a-klr-segment-modules|Type A KLR Segment Modules]]에서 $L(a,b)$를 읽고, 그 다음 [[topics/07-quantum-affine-algebras/quantum-affine-schur-weyl-duality|Quantum Affine Schur-Weyl Duality]]에서 $F(L(a,b))$가 어떻게 fundamental representation으로 가는지 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kang-kashiwara-kim18-symmetric-quiver-hecke-algebras-r-matrices|Kang-Kashiwara-Kim 2018]], Section 3.1, arXiv PDF pp.26-27, lines 2088-2134: chosen good $U_q'(\mathfrak g)$-modules, spectral parameters, denominator zero orders $d_{ij}$, KLR parameters, Cartan matrix, and quiver $\Gamma_J$.
- Kang-Kashiwara-Kim 2018, Section 4.1, arXiv PDF p.35: type $A_{N-1}^{(1)}$ fundamental-representation example with $d_{V,V}(z'/z)=z'/z-q^2$, $X(j)=q^{2j}$, $d_{ij}=\delta(j=i+1)$, and the resulting type $A_\infty$ KLR data.

</details>
