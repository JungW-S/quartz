# Crystal Comparison Map A3 Example Review

Date: 2026-06-01

## Scope

This report reviews whether the $A_3$ example in Kashiwara-Nakashima 2025 can safely fill the empty `기본 예시` section of `content/topics/02-crystal-bases/crystal-comparison-map.md`.

Only `inbox/papers/crystal.tex` lines 4819-4873 were checked. No topic page was edited. No claims were added. No sources were downloaded.

## Source Locations

- `inbox/papers/crystal.tex:4819-4827`: starts the example, sets $\mathfrak g=A_3$, $w=s_2w_0=s_1s_2s_3s_2s_1$, and identifies
  $$
  \mathcal C_w=\{M\in R\text{-gmod}\mid E_2M\simeq 0\}.
  $$
  It also names the three frozen variables $\langle321\rangle$, $\langle132\rangle$, and $\langle123\rangle$.
- `inbox/papers/crystal.tex:4828-4829`: displays the four-cluster square with cluster labels $C_1,C_2,C_3,C_4$.
- `inbox/papers/crystal.tex:4831-4840`: gives four explicit $\operatorname{CP}$ formulas for cluster monomials.
- `inbox/papers/crystal.tex:4842-4847`: records the cellular-crystal coordinates corresponding to the three frozen variables.
- `inbox/papers/crystal.tex:4849-4851`: states $x,y\in\mathbb Z_{\ge0}$, $a,b,c\in\mathbb Z$, and that each $C_k$ is a commuting family of simple modules.
- `inbox/papers/crystal.tex:4853-4865`: describes the images $\operatorname{CP}(C_k)$ as regions in the five-coordinate cellular crystal, cut out by two linear inequalities.
- `inbox/papers/crystal.tex:4866-4872`: draws the two-inequality region picture for the four clusters.

## Decision

The example is safe to use as a real source-backed example for `Crystal Comparison Map`, but only in a compact form.

The recommended first visible example should include:

- the type $A_3$ setup,
- the source's reduced word $w=s_2w_0=s_1s_2s_3s_2s_1$,
- the subcategory condition $\mathcal C_w=\{M\mid E_2M\simeq0\}$,
- one explicit $\operatorname{CP}$ formula for a cluster monomial,
- the parameter conditions $x,y\ge0$ and $a,b,c\in\mathbb Z$,
- a short sentence that the remaining clusters give the other three regions in $\mathcal B_{\underline w}$.

The first edit should not reproduce the full four-cluster region partition. That partition is source-backed, but it requires explaining the cluster chart and the two inequalities, so it is better kept for a later mechanism-oriented expansion.

## Proposed Later Topic Wording

The following wording is safe for a later approved edit to the `기본 예시` section of `content/topics/02-crystal-bases/crystal-comparison-map.md`. It is not applied in this report-only pass.

```markdown
### 실제 예시: type $A_3$

Kashiwara-Nakashima 2025의 $A_3$ example에서는
$$
w=s_2w_0=s_1s_2s_3s_2s_1
$$
이고
$$
\mathcal C_w=\{M\in R\text{-gmod}\mid E_2M\simeq0\}
$$
이다. 이때 localized category $\widetilde{\mathcal C}_w$는 네 개의 clusters를 갖는 cluster algebra의 monoidal categorification으로 나타난다.

Source notation에서 한 cluster의 monomial은
$$
\langle1\rangle^x\circ
\langle3\rangle^y\circ
\langle321\rangle^a\circ
\langle132\rangle^b\circ
\langle123\rangle^c
$$
처럼 쓸 수 있다. 여기서 $x,y\in\mathbb Z_{\ge0}$이고 $a,b,c\in\mathbb Z$이다. 이 monomial에 대해 comparison map은
$$
\operatorname{CP}(
\langle1\rangle^x\circ
\langle3\rangle^y\circ
\langle321\rangle^a\circ
\langle132\rangle^b\circ
\langle123\rangle^c)
=(c+b,c,y+a+b+c,a+b,x+a)
$$
를 준다.

따라서 이 example에서는 category 안의 localized cluster monomial이 five-coordinate cellular-crystal point로 바뀐다. 같은 source는 나머지 세 clusters에 대해서도 analogous formulas를 주고, 네 clusters의 images를 $\mathcal B_{\underline w}$ 안의 네 regions로 나타낸다.
```

## Do Not Add Yet

- Do not add all four $\operatorname{CP}$ formulas in the first example edit unless the page is explicitly being upgraded beyond a basic example.
- Do not reproduce the two-inequality region diagram until the page has enough cluster-algebra and monoidal-categorification setup to explain what the regions mean.
- Do not use the example to claim a general cluster-atlas theorem beyond the stated $A_3$ case.
- Do not replace the abstract definition of $\operatorname{CP}$ with this example; the example only illustrates the already stated definition.

## Recommendation

Use the proposed compact wording as the next approved edit. After that edit, `content/topics/02-crystal-bases/crystal-comparison-map.md` can be moved from `definition-ready` to `example-ready`, while still leaving the full four-cluster region mechanism for a later expansion.

## Applied Edit

The compact example was applied to `content/topics/02-crystal-bases/crystal-comparison-map.md`:

- Added only one type $A_3$ cluster-monomial formula to `기본 예시`.
- Moved the topic from `definition-ready` to `example-ready`.
- Updated topic maturity, research queue, review backlog, source note, and roadmap metadata.
- Deferred the full four-cluster region partition to a later mechanism-oriented review.

## Validation

- `git diff --check` passed.
- `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and the internal Quartz build over 51 content files.
- Standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
