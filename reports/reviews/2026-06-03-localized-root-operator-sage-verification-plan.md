# Localized Root Operator Sage Verification Plan

Date: 2026-06-03

## Scope

This is a report-only verification plan for a possible future visible example in `Localized Root Operators`.

No Sage code was written or run. No topic page was edited. No claim, source note, image, or generated artifact was added. No paper was downloaded.

## Current Decision

Do not add a visible example yet.

Kashiwara-Nakashima 2025 and Nakashima 2022 have already been checked for a direct worked localized-root-operator example. Neither source gives a compact computation of the form
$$
\widetilde F_iX
=q_i^{\varepsilon_i(X)}\,\widetilde Q_i\nabla X
\simeq Y
$$
with explicit localized simple objects $X,Y$ suitable for the topic page.

A Sage/code route can only verify the combinatorial crystal side. It cannot, by itself, verify the category-level head-convolution statement in $\widetilde{\mathcal C}_w$. Therefore a future Sage example must be paired with exact paper support for the dictionary from localized simple objects to cellular-crystal coordinates.

## Best Candidate Object

The safest candidate is the unit-to-simple-root computation inside the type $A_3$ Example 9.6 setting of Kashiwara-Nakashima 2025.

Use:

- $\mathfrak g=A_3$;
- $w=s_2w_0=s_1s_2s_3s_2s_1$;
- reduced word $\underline w=(1,2,3,2,1)$;
- source category
  $$
  \mathcal C_w=\{M\in R\text{-gmod}\mid E_2M\simeq0\};
  $$
- localized simple object $X=\mathbf 1$, the monoidal unit in $\widetilde{\mathcal C}_w$;
- direction $i=1$;
- expected target $\widetilde Q_1=\Phi_w(\langle1\rangle)$, represented in Example 9.6 by the $C_1$ chart monomial with $x=1$ and $y=a=b=c=0$.

The intended future example would be:
$$
\operatorname{CP}(\mathbf 1)=(0,0,0,0,0),
$$
and, after verifying the cellular crystal convention,
$$
\widetilde f_1(0,0,0,0,0)=(0,0,0,0,1).
$$
Example 9.6 identifies
$$
\operatorname{CP}(\langle1\rangle)=(0,0,0,0,1),
$$
so the paper-level crystal isomorphism would then justify
$$
\widetilde F_1(\mathbf 1)\simeq \Phi_w(\langle1\rangle)=\widetilde Q_1
$$
up to the grading-shift convention used in $\operatorname{Irr}(\widetilde{\mathcal C}_w)$.

This candidate is intentionally minimal. It avoids the type $A_2$ and type $A_3$ warning computations previously rejected as positive examples.

## Required Convention Translation

The wiki follows Kashiwara tensor-product convention. SageMath crystal code commonly follows the opposite Schilling/Sage convention.

A future Sage script must therefore do one of the following:

1. implement the Kashiwara tensor product rule directly for the elementary crystal
   $$
   B_1\otimes B_2\otimes B_3\otimes B_2\otimes B_1,
   $$
   using the rule stated in `content/topics/02-crystal-bases/tensor-products-of-crystals.md`; or
2. use Sage's crystal objects only after explicitly translating factor order and equality-case convention back to Kashiwara convention.

Before computing the candidate operator, the script must reproduce the source's three frozen-variable checks from Example 9.6:
$$
\Delta_{\Lambda_1}=\langle321\rangle
\longleftrightarrow
(0,0,1,1,1),
$$
$$
\Delta_{\Lambda_2}=\langle132\rangle
\longleftrightarrow
(1,0,1,1,0),
$$
$$
\Delta_{\Lambda_3}=\langle123\rangle
\longleftrightarrow
(1,1,1,0,0).
$$
If these three checks fail, the Sage convention translation is wrong and no topic-page example should be added.

## What Sage Can Verify

A later approved Sage script can verify only the combinatorial side:

- the cellular-crystal coordinate model for $\mathcal B_{\underline w}$;
- the Kashiwara-convention action of $\widetilde f_1$ on $(0,0,0,0,0)$;
- the matching between the output coordinate and the $C_1$ monomial formula with $x=1$, $y=a=b=c=0$;
- optionally, membership of the output coordinate in the source's $C_1$ region.

The expected repository locations for a later approved implementation would be:

- Sage verification script: `scripts/examples/localized-root-operators/a3_unit_to_simple_root.sage`;
- verification report: `reports/examples/2026-06-03-localized-root-operators-a3-unit.md`;
- no image artifact is needed for the first pass.

## What Still Needs Paper Support

The following category-level statements must be supported by source locations before a visible example can be added:

1. The monoidal unit $\mathbf 1$ is a valid simple object of $\widetilde{\mathcal C}_w$ up to grading shift.
2. The head convolution with the unit behaves as expected:
   $$
   \widetilde Q_1\nabla\mathbf 1\simeq\widetilde Q_1.
   $$
3. The R-matrix degree convention gives $\varepsilon_1(\mathbf 1)=0$, so the grading shift in
   $$
   \widetilde F_1\mathbf 1
   =
   q_1^{\varepsilon_1(\mathbf 1)}\,\widetilde Q_1\nabla\mathbf 1
   $$
   is trivial.
4. The object $\langle1\rangle$ in Example 9.6 is the same localized simple-root object used for $\widetilde Q_1=\Phi_w(\langle1\rangle)$ in Definition `def:rootop`.
5. The crystal isomorphism theorem applies exactly as needed to transfer the Sage-verified cellular arrow back to the localized root operator.

Some of these are likely formal consequences of the definitions, but they should still be checked against the source before the example is made visible.

## Source Locations Already Supporting The Plan

- `inbox/papers/crystal.tex`, lines 3715-3728: Definition `def:rootop` defines $\varepsilon_i$, $\widetilde F_i$, $\widetilde E_i$, and starred operators.
- `inbox/papers/crystal.tex`, lines 3731-3742: inverse property and crystal-structure theorem for the localized operators.
- `inbox/papers/crystal.tex`, lines 4114-4128: definition of $\operatorname{CP}$ and the embedding into the cellular crystal $\mathcal B_{\underline w}$.
- `inbox/papers/crystal.tex`, lines 4218-4258: Main Theorem and corollary that $\operatorname{CP}$ is a morphism of crystals.
- `inbox/papers/crystal.tex`, lines 4774-4776: $\operatorname{CP}:\operatorname{Irr}(\widetilde{\mathcal C}_w)\to\mathcal B_w$ is an isomorphism of crystals.
- `inbox/papers/crystal.tex`, lines 4819-4847: Example 9.6 gives the type $A_3$ setup, the $C_1$ chart formula, and the frozen-variable coordinate checks.

## Proposed Future Visible Example

Do not add this yet. It is only the target form if the paper-support cross-check and Sage verification both pass.

```markdown
### 실제 예시: unit object에서 simple-root object로 가는 arrow

Kashiwara-Nakashima의 type $A_3$ Example 9.6에서
$$
w=s_2w_0=s_1s_2s_3s_2s_1
$$
라고 하자. Monoidal unit $\mathbf 1$은 comparison map에서
$$
\operatorname{CP}(\mathbf 1)=(0,0,0,0,0)
$$
으로 간다.

Kashiwara convention의 cellular crystal 계산은
$$
\widetilde f_1(0,0,0,0,0)=(0,0,0,0,1)
$$
을 준다. Example 9.6의 $C_1$ chart formula에서 이 좌표는 $\langle1\rangle$에 해당한다. 따라서 $\operatorname{CP}$가 crystal isomorphism이라는 정리를 사용하면, localized category 쪽에서는
$$
\widetilde F_1(\mathbf 1)\simeq\Phi_w(\langle1\rangle)=\widetilde Q_1
$$
로 읽힌다.

검증: Sage 계산
```

The final label may need to be `검증: Sage 계산` with Source notes citing Kashiwara-Nakashima 2025, because Sage verifies only the cellular arrow while the category-level dictionary is paper-backed.

## Recommended Next Step

Before writing any Sage code, run a paper-support cross-check for the five category-level statements listed above.

If that cross-check succeeds, then a later task can implement the Sage script. If it fails, keep the `Localized Root Operators` example section empty and search for a direct paper example instead.
