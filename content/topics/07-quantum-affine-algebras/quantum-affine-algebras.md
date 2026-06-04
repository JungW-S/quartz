---
id: quantum-affine-algebras
title: Quantum Affine Algebras
level: core
topic_kind: root
parent_topics: []
prerequisite_topics:
  - quantum-groups
  - weight-modules
child_topics:
  - q-characters-and-l-weights
  - quantum-affine-r-matrix-denominators
  - hernandez-leclerc-categories
  - quantum-affine-schur-weyl-duality
  - affine-cuspidal-modules
  - pbw-theory-for-quantum-affine-algebras
related_topics:
  - quiver-hecke-algebras
  - monoidal-categorification
maturity: example-ready
---

## 개요

Quantum affine algebra는 affine Cartan datum에서 정의되는 Drinfeld-Jimbo type quantum group이다. 이 글에서 다루는 중심 object는 affine Kac-Moody algebra $\mathfrak g$에 붙는 algebra $U_q(\mathfrak g)$이다.

Representation theory에서는 $U_q(\mathfrak g)$ 전체보다 subalgebra $U_q'(\mathfrak g)$의 finite-dimensional integrable modules를 모은 category
$$
\mathcal C_{\mathfrak g}
$$
가 핵심 무대가 된다. 이 category 안에서 tensor product, spectral parameter, R-matrix가 함께 나타난다.

Quantum affine algebra가 중요한 이유는 이 representation category가 Hernandez-Leclerc category, quantum affine Schur-Weyl duality, quiver-Hecke algebra와의 비교, monoidal categorification으로 이어지기 때문이다. 따라서 여기서는 algebra 정의, module category notation, spectral parameter가 들어간 첫 예시를 고정한다.

## 준비와 notation

$A=(a_{ij})_{i,j\in I}$를 affine Cartan matrix라고 하자. 이에 대응하는 affine Kac-Moody algebra를 $\mathfrak g$로 쓴다. $I$는 affine Dynkin diagram의 vertex set이고, affine vertex를 $0$으로 고정한 뒤
$$
I_0=I\setminus\{0\}
$$
로 둔다.

$P$와 $P^\vee$를 각각 weight lattice와 coweight lattice라고 하자. Simple roots와 simple coroots는
$$
\alpha_i\in P,\qquad h_i\in P^\vee\qquad (i\in I)
$$
로 쓴다. 또한
$$
\Pi=\{\alpha_i\mid i\in I\},
\qquad
\Pi^\vee=\{h_i\mid i\in I\}
$$
로 둔다. Affine case에는 imaginary root $\delta$와 central element $c\in P^\vee$가 나타난다. Classical weight lattice는
$$
P_{\mathrm{cl}}=P/(P\cap\mathbb Q\delta)
$$
이다.

$q$는 indeterminate이고,
$$
q_i=q^{(\alpha_i,\alpha_i)/2}
$$
로 둔다. 계수체는 $\mathbb C(q)$를 포함하는 algebraically closed field $\Bbbk$로 둔다. $d$는 모든 $i\in I$에 대해
$$
d\frac{(\alpha_i,\alpha_i)}{2}\in\mathbb Z
$$
가 되게 하는 가장 작은 양의 정수이다.

Quantum integers는
$$
[n]_i=\frac{q_i^n-q_i^{-n}}{q_i-q_i^{-1}},
\qquad
[n]_i!=\prod_{k=1}^n[k]_i
$$
로 쓴다.

Divided powers는
$$
e_i^{(k)}=\frac{e_i^k}{[k]_i!},
\qquad
f_i^{(k)}=\frac{f_i^k}{[k]_i!}
$$
로 쓴다. Cartan generator의 짧은 표기는
$$
K_i=q_i^{h_i}
$$
이다.

## 정의

Affine Cartan datum $(A,P,\Pi,P^\vee,\Pi^\vee)$가 주어졌다고 하자. Quantum affine algebra $U_q(\mathfrak g)$는 $\Bbbk$ 위의 unital associative algebra이다. Generators는
$$
e_i,\quad f_i\quad (i\in I),
\qquad
q^h\quad (h\in d^{-1}P^\vee)
$$
이고, defining relations는 다음과 같다.

먼저 $q^h$들은 lattice law를 따른다.
$$
q^0=1,\qquad q^h q^{h'}=q^{h+h'}.
$$

$q^h$의 conjugation은 $e_i$와 $f_i$의 weights를 측정한다.
$$
q^h e_i q^{-h}=q^{\langle h,\alpha_i\rangle}e_i,
\qquad
q^h f_i q^{-h}=q^{-\langle h,\alpha_i\rangle}f_i.
$$

Raising and lowering generators의 commutator는
$$
e_i f_j-f_j e_i
=
\delta_{ij}\frac{K_i-K_i^{-1}}{q_i-q_i^{-1}},
\qquad K_i=q_i^{h_i}
$$
이다.

$i\ne j$이면 quantum Serre relations는
$$
\sum_{k=0}^{1-a_{ij}}
(-1)^k e_i^{(1-a_{ij}-k)}e_j e_i^{(k)}
=0,
$$
$$
\sum_{k=0}^{1-a_{ij}}
(-1)^k f_i^{(1-a_{ij}-k)}f_j f_i^{(k)}
=0.
$$

표현론에서는 다음 subalgebra를 자주 쓴다.
$$
U_q'(\mathfrak g)
$$
이것은 모든 $i\in I$에 대한 $e_i$, $f_i$, $K_i^{\pm1}$로 generated되는 subalgebra이다. 아래의 finite-dimensional module category는 이 $U_q'(\mathfrak g)$ 위에서 정의된다.

## 기본 예시

### 실제 예시: type $A_{n-1}^{(1)}$의 $V(\varpi_1)_z$

Affine type $A_{n-1}^{(1)}$에서 $V(\varpi_1)$은 fundamental representation의 한 예이다. Spectral parameter $z\in\Bbbk^\times$를 넣으면 같은 vector space 위의 action을 twist한 $U_q'(\mathfrak g)$-module
$$
V(\varpi_1)_z
$$
를 얻는다.

이 예시는 quantum affine algebra에서 spectral parameter가 module structure에 들어가는 방식을 보여 준다. Algebra $U_q'(\mathfrak g)$는 고정되어 있지만, parameter $z$가 action에 들어가면서 $V(\varpi_1)_z$들이 하나의 parameter family를 이룬다.

Akasaka-Kashiwara는 이 fundamental representation을 $V(\pi_k)$로 쓴다. 이 글에서는 같은 object를 $V(\varpi_k)$로 표기한다. Type $A_{n-1}^{(1)}$에서 $V(\varpi_k)$의 crystal basis는 $k$-element subsets of $\mathbb Z/n\mathbb Z$로 labeled된다. 특히 $k=1$이면 singleton subsets가 $V(\varpi_1)$의 crystal-level labels가 된다.

검증: 논문 예시

## 핵심 관점

### Algebra level

Algebra-level에서는 $U_q(\mathfrak g)$가 affine Cartan datum의 generators and relations로 결정된다. 여기서 affine feature는 index set에 affine vertex가 들어가고, classical weight lattice $P_{\mathrm{cl}}$와 $U_q'(\mathfrak g)$가 representation theory에 나타난다는 점이다.

### Object level

Object-level에서 $\mathcal C_{\mathfrak g}$의 object는 $P_{\mathrm{cl}}$-weight decomposition을 갖는 finite-dimensional integrable $U_q'(\mathfrak g)$-module이다. Decomposition은
$$
M=\bigoplus_{\lambda\in P_{\mathrm{cl}}}M_\lambda
$$
이고,
$$
M_\lambda
=
\{u\in M\mid K_i u=q_i^{\langle h_i,\lambda\rangle}u
\text{ for all }i\in I\}
$$
이다.

Fundamental representations $V(\varpi_i)$와 spectral-parameter shifts $V(\varpi_i)_x$는 이 category 안의 기본 object family이다.

### Category level

Category-level에서는 $U_q'(\mathfrak g)$의 finite-dimensional integrable modules를 모아
$$
\mathcal C_{\mathfrak g}
$$
를 만든다. Tensor product는 $\mathcal C_{\mathfrak g}$에 monoidal category structure를 주며, 이 category는 dual objects를 갖는다. Module $M$의 right dual과 left dual은 각각
$$
M^*,\qquad {}^*M
$$
로 쓸 수 있다.

Spectral parameter와 R-matrix는 이 category에서 tensor product를 연구할 때 나타난다. Module $M$의 affinization $M^{\mathrm{aff}}$와 automorphism $z_M$을 사용하여
$$
M_x=M^{\mathrm{aff}}/(z_M-x)M^{\mathrm{aff}}
$$
를 만들며, 여기서 $x$가 spectral parameter이다. R-matrix는 적절한 renormalization과 specialization을 거쳐 tensor product의 순서를 바꾸는 nonzero morphism
$$
r_{M,N}:M\otimes N\longrightarrow N\otimes M
$$
으로 나타난다.

## 기본 성질

### Finite-dimensional integrable module category

$\mathcal C_{\mathfrak g}$는 finite-dimensional integrable $U_q'(\mathfrak g)$-modules의 category이다. Tensor product에 대해 monoidal category이고, dual objects를 갖는 rigid monoidal category이다.

### Fundamental representations

Simple module $L\in\mathcal C_{\mathfrak g}$에는 dominant extremal weight가 붙는다. $i\in I_0$에 대해 $i$-th fundamental representation은
$$
V(\varpi_i)
$$
로 쓴다. Spectral parameter를 넣은 $V(\varpi_i)_x$들은 quantum affine representation theory에서 기본 building blocks로 쓰인다.

### Hernandez-Leclerc category의 출발점

Fundamental representations $V(\varpi_i)_x$의 spectral parameters를 vertices로 하는 quiver $\sigma$를 만든다. 하나의 connected component를 $\sigma_0$라고 하자. Hernandez-Leclerc category는 $\mathcal C_{\mathfrak g}$의 full subcategory
$$
\mathcal C_{\mathfrak g}^0
$$
로 정의된다. 이 category는 $(i,x)\in\sigma_0$인 fundamental representations $V(\varpi_i)_x$를 포함하고, subquotients, extensions, tensor products에 대해 닫혀 있는 가장 작은 full subcategory이다.

이 정의는 cluster algebra와 quantum affine module category를 연결하는 이후 topic들의 출발점이다.

## 다른 topic들과의 관계

- [[topics/01-quantum-groups/quantum-groups|Quantum Groups]]: quantum affine algebra는 affine Cartan datum에 붙는 quantum group이다. $U_q(\mathfrak g)$의 generators, Cartan action, quantum Serre relations는 quantum group 정의의 affine version이다.
- [[topics/01-quantum-groups/weight-modules|Weight Modules]]: $\mathcal C_{\mathfrak g}$의 object는 $P_{\mathrm{cl}}$-weight decomposition을 갖는다.
- [[topics/01-quantum-groups/universal-r-matrix|Universal R-Matrix]]: quantum affine module category에서 R-matrix는 tensor product의 순서를 바꾸는 morphism으로 사용된다.
- [[topics/07-quantum-affine-algebras/quantum-affine-r-matrix-denominators|Quantum Affine R-Matrix Denominators]]: normalized R-matrix denominator의 pole data가 quiver-Hecke algebra input으로 바뀌는 중간 단계를 설명한다.
- [[topics/07-quantum-affine-algebras/hernandez-leclerc-categories|Hernandez-Leclerc Categories]]: fundamental representations와 spectral parameters를 제한해서 cluster algebra와 비교하기 좋은 더 작은 monoidal subcategories를 만든다.
- [[topics/07-quantum-affine-algebras/quantum-affine-schur-weyl-duality|Quantum Affine Schur-Weyl Duality]]: quantum affine module category와 quiver-Hecke module category를 monoidal functor로 비교한다.
- [[topics/05-monoidal-categorification/monoidal-categorification|Monoidal Categorification]]: Hernandez-Leclerc category는 quantum affine algebra representation category 안에서 monoidal categorification과 연결되는 주요 category이다.
- [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]: quantum affine Schur-Weyl duality는 quiver-Hecke module category와 quantum affine module category를 비교하는 연결이다.

## 더 읽을 topic

먼저 [[topics/01-quantum-groups/quantum-groups|Quantum Groups]]에서 Drinfeld-Jimbo quantum group의 generators, relations, Hopf algebra structure를 읽는 것이 좋다. Weight decomposition이 익숙하지 않다면 [[topics/01-quantum-groups/weight-modules|Weight Modules]]를 먼저 읽어야 한다.

다음으로는 [[topics/07-quantum-affine-algebras/quantum-affine-r-matrix-denominators|Quantum Affine R-Matrix Denominators]]에서 R-matrix denominator가 quiver-Hecke input을 정하는 방식을 읽고, [[topics/07-quantum-affine-algebras/hernandez-leclerc-categories|Hernandez-Leclerc Categories]]에서 $\mathcal C_{\mathfrak g}$ 안의 더 작은 monoidal subcategories와 Grothendieck ring의 cluster algebra 연결을 읽는다.

그 다음에는 [[topics/07-quantum-affine-algebras/quantum-affine-schur-weyl-duality|Quantum Affine Schur-Weyl Duality]]에서 quantum affine category와 quiver-Hecke module category를 비교하는 functor를 읽는다. Tensor product와 braiding-type structure는 [[topics/01-quantum-groups/universal-r-matrix|Universal R-Matrix]]와 [[topics/06-quiver-hecke-klr-algebras/r-matrix-renormalization|R-Matrix Renormalization]]으로 이어진다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kkop24-pbw-theory-quantum-affine-algebras|Kashiwara-Kim-Oh-Park 2024]], Section 2.3, local TeX lines 1360-1454: affine Cartan setup, $U_q(\mathfrak g)$, $U_q'(\mathfrak g)$, $\mathcal C_{\mathfrak g}$, dominant extremal weights, and fundamental representations.
- Kashiwara-Kim-Oh-Park 2024, Section 2.4, local TeX lines 1465-1512: affinizations, spectral parameters, universal and renormalized R-matrices, and $r_{M,N}$.
- Kashiwara-Kim-Oh-Park 2024, Section 2.5, local TeX lines 1641-1676: spectral-parameter quiver $\sigma$ and the Hernandez-Leclerc category $\mathcal C_{\mathfrak g}^0$.
- [[sources/papers/akasaka-kashiwara97-finite-dimensional-representations-quantum-affine-algebras|Akasaka-Kashiwara 1997]], Section 1.2, Section 1.3, and Appendix B.1: spectral-parameter twists, fundamental representations, and the type $A_{n-1}^{(1)}$ crystal-basis labels used in the example.
- [[sources/books/hong-kang02-introduction-quantum-groups-crystal-bases|Hong-Kang 2002]] remains the prerequisite source for ordinary quantum group and weight-module background.

</details>
