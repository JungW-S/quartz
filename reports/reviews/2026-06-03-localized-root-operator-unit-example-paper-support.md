# Localized Root Operator Unit Example Paper-Support Check

Date: 2026-06-03

## Scope

This was a report-only source-location cross-check for the proposed type $A_3$ unit-to-simple-root example in `Localized Root Operators`.

Only local Kashiwara-Nakashima 2025 `inbox/papers/crystal.tex` and the existing plan `reports/reviews/2026-06-03-localized-root-operator-sage-verification-plan.md` were used. No Sage code was written or run. No topic page, claim, source note, image, or generated artifact was added.

## Decision

Do not proceed to Sage verification as a topic-example route yet.

The source contains strong support for the general localized-root-operator framework and for the type $A_3$ Example 9.6 comparison-map setting. It does not explicitly supply all category-level statements needed to turn the proposed Sage cellular calculation into a visible localized-root-operator example.

The proposed example should remain blocked until the missing paper support is supplied by a direct source location or replaced by a different source-backed example.

## Source Locations Checked

### General monoidal-unit and localization support

- `inbox/papers/crystal.tex`, lines 1648-1657: the ambient graded monoidal category assumptions include that the unit object $\mathbf 1$ is simple and that tensor product is compatible with grading shifts.
- `inbox/papers/crystal.tex`, lines 1672-1685: the duality definition uses the unit isomorphisms $X\simeq X\otimes\mathbf 1$ and $\mathbf 1\otimes X\simeq X$.
- `inbox/papers/crystal.tex`, lines 1038-1058: the localization of a monoidal category produces a monoidal category and a monoidal functor.
- `inbox/papers/crystal.tex`, lines 2898-2902: $\Phi_w$ and $\mathsf Q$ are the localization functors in the $\mathcal C_w$ and $R\text{-gmod}$ diagram.
- `inbox/papers/crystal.tex`, lines 2907-2915: $\widetilde{\mathcal C}_w$ is rigid, and simple objects survive localization as simple or zero objects.

These locations support treating $\mathbf 1$ as part of the monoidal-category framework, but they do not by themselves identify the proposed unit example inside Example 9.6.

### Localized-root-operator framework

- `inbox/papers/crystal.tex`, line 929: source macro defines $\widetilde Q_i$ as $\mathsf Q(\langle i\rangle)$.
- `inbox/papers/crystal.tex`, lines 3715-3728: Definition `def:rootop` defines $\varepsilon_i(X)$ and
  $$
  \widetilde F_iX=q_i^{\varepsilon_i(X)}\widetilde Q_i\nabla X.
  $$
- `inbox/papers/crystal.tex`, lines 3731-3742: the operators are inverse pairs and define a crystal structure on $\operatorname{Irr}(\widetilde{\mathcal C}_w)$.
- `inbox/papers/crystal.tex`, lines 3893-3902: under the descent hypothesis $s_iw<w$, the source gives
  $$
  \widetilde F_i(\mathsf Q(M))\simeq \mathsf Q(\widetilde F_i(M)),
  \qquad
  \varepsilon_i(\mathsf Q(M))=\varepsilon_i(M).
  $$

These locations are close to the desired unit-to-simple-root computation. However, the source does not instantiate this lemma with $M=\mathbf 1$ and $i=1$ in Example 9.6.

### Ordinary quiver-Hecke simple-root support

- `inbox/papers/crystal.tex`, lines 2081-2086: the trivial $R(0)$-module is introduced.
- `inbox/papers/crystal.tex`, lines 2119-2126: convolution product of quiver-Hecke modules is defined.
- `inbox/papers/crystal.tex`, lines 2144-2147: $M\nabla N$ is the head of $M\circ N$.
- `inbox/papers/crystal.tex`, lines 2160-2165: $L(i)=\langle i\rangle$ is the simple $R(\alpha_i)$-module.
- `inbox/papers/crystal.tex`, lines 2194-2198: ordinary crystal operator $\widetilde F_i(M)$ is defined using $\langle i\rangle\nabla M$.

These locations support the formal expectation that the ordinary operator sends the unit to $\langle i\rangle$, but the paper does not spell out the unit case as a worked example.

### Cellular comparison-map support

- `inbox/papers/crystal.tex`, lines 4114-4128: $\operatorname{CP}$ is defined by recursively applying starred operators and recording coordinates in $\mathcal B_{\underline w}$.
- `inbox/papers/crystal.tex`, lines 4218-4258: Main Theorem and corollary say that $\operatorname{CP}$ is a crystal morphism.
- `inbox/papers/crystal.tex`, lines 4774-4776: $\operatorname{CP}:\operatorname{Irr}(\widetilde{\mathcal C}_w)\to\mathcal B_w$ is an isomorphism of crystals.

These locations support transferring verified cellular arrows back to the localized crystal only after the relevant objects and coordinates are correctly identified.

### Example 9.6 support

- `inbox/papers/crystal.tex`, lines 4819-4829: Example 9.6 sets $\mathfrak g=A_3$, $w=s_2w_0=s_1s_2s_3s_2s_1$, $\mathcal C_w=\{M\in R\text{-gmod}\mid E_2M\simeq0\}$, names frozen variables, and shows the four-cluster square.
- `inbox/papers/crystal.tex`, lines 4831-4840: the example gives four explicit $\operatorname{CP}$ formulas for cluster monomial charts.
- `inbox/papers/crystal.tex`, lines 4842-4847: the example records frozen-variable coordinate checks from the zero coordinate:
  $$
  \langle321\rangle=\widetilde F_3\widetilde F_2\widetilde F_1\mathbf 1
  \longleftrightarrow
  \widetilde f_3\widetilde f_2\widetilde f_1(0,0,0,0,0),
  $$
  and the analogous checks for $\langle132\rangle$ and $\langle123\rangle$.

These lines strongly indicate the intended base coordinate $(0,0,0,0,0)$ and ordinary root-operator behavior in Example 9.6, but they still do not explicitly isolate the one-step localized-root-operator calculation $\widetilde F_1(\mathbf 1)\simeq\widetilde Q_1$.

## Required Statements And Status

### 1. $\mathbf 1$ is a valid simple object of $\widetilde{\mathcal C}_w$

Status: mostly supported, but not in the exact Example 9.6 phrasing.

The general monoidal-category assumptions include a simple unit, and the localization construction is monoidal. This is enough for background, but a visible example should still avoid pretending the source has singled out $\mathbf 1$ as the first worked localized object in Example 9.6.

### 2. $\widetilde Q_1\nabla\mathbf 1\simeq\widetilde Q_1$

Status: formal, but not explicitly checked in the source.

The monoidal-unit laws and head-convolution definition make this the expected result once $\widetilde Q_1$ is simple. The paper does not state this as a localized-root-operator example.

### 3. $\varepsilon_1(\mathbf 1)=0$

Status: blocker.

The source gives the definition of $\varepsilon_i(X)$ and a compatibility lemma under $s_iw<w$, but it does not explicitly instantiate $\varepsilon_1(\mathbf 1)=0$ in the type $A_3$ Example 9.6 setting. This is the main blocker for using the displayed formula
$$
\widetilde F_1\mathbf 1
=q_1^{\varepsilon_1(\mathbf 1)}\widetilde Q_1\nabla\mathbf 1
$$
as a fully verified topic-page example.

### 4. $\langle1\rangle$ in Example 9.6 is $\widetilde Q_1=\mathsf Q(\langle1\rangle)$

Status: supported after notation translation, but not explicitly spelled out in Example 9.6.

The source macro defines $\widetilde Q_i=\mathsf Q(\langle i\rangle)$, and Example 9.6 uses $\langle1\rangle$ as a cluster variable. A topic-page example would still need to say that this is being read through the localization functor, not as an unlocalized object.

### 5. $\operatorname{CP}$ transfers the cellular arrow back to the localized operator

Status: supported at theorem level.

The source proves that $\operatorname{CP}$ is a crystal isomorphism. If the cellular computation and object identification are verified, this theorem supports transferring the arrow back to $\operatorname{Irr}(\widetilde{\mathcal C}_w)$.

## Blockers

The current source support is not enough for a visible example labeled `검증: Sage 계산`.

Remaining blockers:

- no explicit source instantiation of $\varepsilon_1(\mathbf 1)=0$ in the localized type $A_3$ setting;
- no explicit one-step statement $\widetilde F_1(\mathbf 1)\simeq\widetilde Q_1$ in Example 9.6;
- no source-level sentence identifying the $C_1$ chart variable $\langle1\rangle$ as the localized simple-root object in the exact operator-definition notation;
- Sage would still verify only the cellular arrow, not the category-level head-convolution formula.

## Recommendation

Do not write Sage code for this example yet.

Keep `Localized Root Operators` definition-ready with its visible example omitted. If a visible example is still essential, the safer route is to find a direct paper example or a source statement that explicitly computes the unit-to-simple-root localized operator.
