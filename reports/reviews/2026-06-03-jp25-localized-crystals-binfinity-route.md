# JP25 Localized Crystals B(infinity) Route Review

Date: 2026-06-03

## Scope

This is a report-only source-location review of the local JP25 files:

- `inbox/papers2/JP25, Crystals and quantum twist automorphisms, arXiv.pdf`
- `inbox/papers2/Tex/JP25, Crystals and quantum twist automorphisms, arXiv/CT.tex`

No paper was downloaded. No claim was added. No source note was created. No topic page was edited.

The question was whether JP25 supports describing localized crystals using $B(\infty)$.

## Verdict

Yes. JP25 gives a direct $B(\infty)$-based route to localized crystals.

The safe mathematical reading is:

- start with $B(w)\subset B(\infty)$, selected by the condition that $\mathbf G^{\mathrm{up}}(b)$ lies in the quantum unipotent coordinate ring $A_q(\mathfrak n(w))$;
- choose frozen crystal elements $\mathfrak z_i^w\in B(\infty)$ corresponding to the quantum unipotent minors $\Delta(w\Lambda_i,\Lambda_i)$;
- form a localized crystal $\mathcal B(w)$ by localizing $B(w)$ with respect to those frozen elements;
- identify this localized crystal with both the upper global basis of the localized quantum coordinate ring and the simple objects of the localized quiver-Hecke category;
- define the permutation $\mathfrak D_w$ on the localized crystal so that it corresponds to the quantum twist automorphism $\eta_w$ and to the right dual functor on the localized category.

This is useful for the wiki, but it should not be inserted immediately into `Localized Crystals` as a full rewrite. The better later use is a narrow JP25 intake that adds a compact bridge:

$$
B(\infty)\supset B(w)
\quad\longrightarrow\quad
\mathcal B(w)
\quad\longleftrightarrow\quad
\widetilde{\mathbf G}^{\mathrm{up}}(w),\ \widetilde{\mathbf G}^{\mathrm s}(w)
$$

and then explains that $\mathfrak D_w$ is the crystal-level counterpart of $\eta_w$ and the right dual functor.

## Source Locations

### Introduction-Level Support

- `CT.tex:987-991`: states that the paper studies the quantum twist automorphism $\eta_w$ from the viewpoint of crystals, for arbitrary symmetrizable Kac-Moody types, and gives a crystal-theoretic description.
- `CT.tex:995-1008`: explains the localized crystal construction at introduction level. It says that $B(w)$ is the crystal basis of $A_q(\mathfrak n(w))$, that the elements $\mathfrak z_i^w$ correspond to the frozen quantum unipotent minors, and that inverting these elements gives $\mathcal B(w)$. It also records the one-to-one correspondences with $\widetilde{\mathbf G}^{\mathrm{up}}(w)$ and with localized simple objects.
- `CT.tex:1011-1019`: says that the paper studies the bijections among $\mathcal B(w)$, $\widetilde{\mathbf G}^{\mathrm{up}}(w)$, and $\widetilde{\mathbf G}^{\mathrm s}(w)$, and that this gives the crystal-theoretic counterpart of $\eta_w^{-1}$ and the right dual functor.

### Definition Layer

- `CT.tex:1480-1486`: defines
  $$
  B(w)=\{b\in B(\infty)\mid \mathbf G^{\mathrm{up}}(b)\in A_q(\mathfrak n(w))\}
  $$
  and defines the frozen crystal elements $\mathfrak z_i^w$ through the quantum unipotent minors.
- `CT.tex:1490-1500`: defines the equivalence relation on $B(w)\times\mathbb Z^{\oplus I}$ and the localized set
  $$
  \mathcal B(w)=B(w)\times\mathbb Z^{\oplus I}/\sim.
  $$
- `CT.tex:1508-1510`: names $\mathcal B(w)$ the localized crystal of $B(w)$ by the elements $\{\mathfrak z_i\}_{i\in I}$.
- `CT.tex:1513-1517`: relates this definition to Nakashima's localized crystals/cellular crystals in finite type, while presenting JP25's definition as an abstraction of that result.

### Basis And Category Avatars

- `CT.tex:1525-1532`: defines the element $\widetilde{\mathbf G}^{\mathrm{up}}(x)$ for $x\in\mathcal B(w)$ and states the bijection
  $$
  \widetilde{\mathbf G}^{\mathrm{up}}(w)=
  \{\widetilde{\mathbf G}^{\mathrm{up}}(x)\mid x\in\mathcal B(w)\}.
  $$
- `CT.tex:1534-1541`: defines $L(x)$ in the localized category and states
  $$
  \widetilde{\mathbf G}^{\mathrm s}(w)=\{[L(x)]\mid x\in\mathcal B(w)\}.
  $$
- `CT.tex:1546-1555`: defines the permutation $\mathfrak D_w$ by a commutative diagram connecting $\mathcal B(w)$, $\widetilde{\mathbf G}^{\mathrm{up}}(w)$, $\widetilde{\mathbf G}^{\mathrm s}(w)$, $\eta_w$, and the right dual functor.

### Parametrization Layer

- `CT.tex:1569-1596`: extends PBW parametrization from $B(w)$ to $\mathcal B(w)$ by adding integer multiples of frozen PBW vectors.
- `CT.tex:1600-1675`: defines string parametrization for $B(w)$ and extends it to $\mathcal B(w)$.
- `CT.tex:1691-1695`: defines the bijection
  $$
  \psi_{\mathbf i}:\widetilde{\mathcal P}_{\mathbf i}(w)\to
  \widetilde{\mathcal S}_{\mathbf i}(w)
  $$
  between localized PBW and string parametrizations.

### Twist-Automorphism Formula Layer

- `CT.tex:1830-1836`: displays the diagram of bijections among $\mathcal B(w)$, localized PBW data, localized string data, and left/right $g$-vectors.
- `CT.tex:1838-1852`: Theorem 3.2 gives formulas for $\mathfrak D_w$ in PBW, string, and $g$-vector coordinates.
- `CT.tex:1853-1859`: proof explains that $\mathfrak D_w$ is the crystal-theoretic counterpart of the right dual functor in the localized category.
- `CT.tex:1863-1885`: warns that the nonlinearity of $\psi_{\mathbf i}$ prevents some tempting linear sign formulas. This warning is important if the wiki later explains coordinate formulas.

### Example Candidate

- `CT.tex:1888-1947`: gives a type $A_2$ example for $\mathcal B(\infty)$, including frozen elements, localized PBW/string parametrizations, the explicit piecewise-linear map $\psi_{\mathbf i}$, and the matrices $N_{\mathbf i}$ and $M_{\mathbf i}$.

This example is source-backed, but it should not be added as a visible `Localized Crystals` example yet. It is a coordinate example for the JP25 twist-automorphism route, not a first basic example of localized categories. It would fit better after a narrow JP25 intake and a small subsection explaining PBW/string coordinates.

## Recommended Future Use

If approved later, JP25 can support a compact expansion of `Localized Crystals` and possibly a short cross-link from `The Crystal B(infinity)`.

Recommended topic-page scope:

- Add a short `핵심 관점` or `기본 성질` paragraph to `Localized Crystals` explaining that JP25 also realizes localized crystals by localizing $B(w)\subset B(\infty)$ at frozen crystal elements.
- Add a relation paragraph connecting `The Crystal B(infinity)` to `Localized Crystals`.
- Mention that $\mathfrak D_w$ is the crystal-level counterpart of the quantum twist automorphism and right dual functor, but defer formulas to a future advanced subsection.

Do not add yet:

- the full Theorem 3.2 formula;
- minuscule Young diagram material;
- periodicity conjectures;
- SageMath periodicity computations;
- a visible type $A_2$ example, unless the user separately approves a coordinate-example pass.

## Claim Budget For A Later Intake

If the user approves a narrow JP25 intake, keep the claim budget small:

1. $B(w)\subset B(\infty)$ and the localized crystal $\mathcal B(w)$ definition from `CT.tex:1480-1510`;
2. bijection between $\mathcal B(w)$ and $\widetilde{\mathbf G}^{\mathrm{up}}(w)$ from `CT.tex:1525-1532`;
3. bijection between $\mathcal B(w)$ and localized simple objects from `CT.tex:1534-1541`;
4. definition/role of $\mathfrak D_w$ as the crystal-level counterpart of $\eta_w$ and right duality from `CT.tex:1546-1555`;
5. optional formula-level claim from Theorem 3.2, only if an advanced coordinate subsection is approved.

## Recommended Next Step

Approve a narrow JP25 intake only if the wiki should now add the $B(\infty)$ route to `Localized Crystals`:

```text
I approve JP25 for narrow intake. Use only the local JP25 PDF/TeX. Create a concise source note, add at most 4 claims, and update only Localized Crystals and The Crystal B(infinity) with a compact B(infinity)-route paragraph. Do not add examples, minuscule material, periodicity material, Sage computations, or the full Theorem 3.2 formulas.
```
