# Crystal Comparison Map Source-Location Review

Date: 2026-06-01

Source checked: `inbox/papers/crystal.tex` only.

No topic page was rewritten. No claims were added. No sources were downloaded.

## Source Locations

- Cellular crystal setup: `inbox/papers/crystal.tex:1458-1471`.
  For a reduced expression $\underline w=s_{i_1}\cdots s_{i_\ell}$, the source defines the cellular crystal $\mathcal B_{\underline w}$ as $B_{i_1}\otimes\cdots\otimes B_{i_\ell}$ and records braid-type isomorphisms for different reduced words.
- Cellular crystal coordinates and operators: `inbox/papers/crystal.tex:1473-1516`.
  These lines give the coordinate notation and explicit formulas for weight, $\varepsilon_i$, $\varphi_i$, and crystal operators.
- Category-level input: `inbox/papers/crystal.tex:3091-3145`.
  The source defines the category $\mathcal B_w$-side subcategory $\mathcal C_{\mathcal B_w}$ and identifies $\operatorname{Irr}(\mathcal C_{\mathcal B_w})$ with the Demazure crystal $B_w(\infty)$.
- Localized category setup: `inbox/papers/crystal.tex:2870-2915`.
  This gives $\widetilde{\mathcal C}_w$ and the localization functors used before passing to $\operatorname{Irr}(\widetilde{\mathcal C}_w)$.
- Localized root operators and crystal structure: `inbox/papers/crystal.tex:3711-3742`.
  These are prerequisites for reading $\operatorname{Irr}(\widetilde{\mathcal C}_w)$ as a crystal.
- Definition of $\operatorname{CP}$ on $\operatorname{Irr}(\mathcal C_{\mathcal B_w})$: `inbox/papers/crystal.tex:4114-4128`.
  This is the recursive coordinate definition using $\varepsilon^*_{i_k}$ and $\widetilde E^*_{i_k}$.
- Extension of $\operatorname{CP}$ to $\operatorname{Irr}(\widetilde{\mathcal C}_w)$: `inbox/papers/crystal.tex:4129-4148`.
  The source first obtains $\operatorname{Irr}(\mathcal C_w)\to\mathcal B_{\underline w}$ and then extends it to localized simple objects by subtracting the determinantial-object coordinate.
- Recursive truncation relation for $\operatorname{CP}$: `inbox/papers/crystal.tex:4201-4210`.
  This relates $\operatorname{CP}_{\underline w}(X)$ to $\operatorname{CP}_{\underline w'}(\mathbb E^*(X))$ and the final coordinate.
- Main theorem controlling crystal compatibility: `inbox/papers/crystal.tex:4215-4254`.
  This gives the detailed formulas from which the crystal morphism statement follows.
- Crystal morphism corollary: `inbox/papers/crystal.tex:4256-4320`.
  This states that $\operatorname{CP}:\operatorname{Irr}(\widetilde{\mathcal C}_w)\to\mathcal B_{\underline w}$ is a morphism of crystals.
- Bijectivity and crystal isomorphism: `inbox/papers/crystal.tex:4680-4777`.
  Proposition `prop:bij` gives bijectivity, and the following main theorem states that $\operatorname{CP}$ is an isomorphism of crystals.
- Example: `inbox/papers/crystal.tex:4819-4873`.
  This gives an $A_3$ cluster-style example of $\operatorname{CP}$ on families of simple objects, but it should not be used until separately approved as a topic-page example.

## Safe Definition Outline

Fix a reduced expression
$$
\underline w=s_{i_1}\cdots s_{i_\ell}
$$
of $w\in W$. The target cellular crystal is
$$
\mathcal B_{\underline w}=B_{i_1}\otimes\cdots\otimes B_{i_\ell}.
$$

For a simple object $M$ in the category-level input $\mathcal C_{\mathcal B_w}$, define a sequence by
$$
M_\ell=M,\qquad
c_k=\varepsilon^*_{i_k}(M_k),\qquad
M_{k-1}=(\widetilde E^*_{i_k})^{c_k}(M_k)
$$
for $1\le k\le\ell$. Then
$$
\operatorname{CP}(M)=(c_1,\ldots,c_\ell),
$$
regarded as an element of $\mathcal B_{\underline w}$ by
$$
(c_1,\ldots,c_\ell)
\longmapsto
\widetilde f_{i_1}^{c_1}(0)_{i_1}\otimes\cdots\otimes
\widetilde f_{i_\ell}^{c_\ell}(0)_{i_\ell}.
$$

The source then extends this map from $\operatorname{Irr}(\mathcal C_w)$ to localized simples. In local topic notation, if a localized simple is represented as
$$
\widetilde C_\Lambda^{-1}\circ\Phi_w(M),
$$
then the extended map is
$$
\operatorname{CP}(\widetilde C_\Lambda^{-1}\circ\Phi_w(M))
=\operatorname{CP}(M)-\operatorname{CP}(\widetilde C_\Lambda).
$$

Thus the comparison map has the form
$$
\operatorname{CP}:
\operatorname{Irr}(\widetilde{\mathcal C}_w)
\longrightarrow
\mathcal B_{\underline w}.
$$

## Safe Theorem Statement

With the localized crystal structure on $\operatorname{Irr}(\widetilde{\mathcal C}_w)$ and the cellular crystal structure on $\mathcal B_{\underline w}$, the source proves:

1. $\operatorname{CP}$ is a morphism of crystals.
2. $\operatorname{CP}$ is bijective.
3. Therefore $\operatorname{CP}$ is an isomorphism of crystals.

The source proves the morphism statement through a recursive reduction along the last simple reflection in the chosen reduced expression, using the auxiliary map $\mathbb E^*$ and the formulas in the main theorem.

## Hypotheses To State Before Any Topic-Page Edit

- A Weyl group element $w$ and a reduced expression $\underline w=s_{i_1}\cdots s_{i_\ell}$ are fixed.
- The target is the cellular crystal $\mathcal B_{\underline w}$ attached to that reduced expression.
- The domain is $\operatorname{Irr}(\widetilde{\mathcal C}_w)$, simple objects of the localized category up to grading shifts.
- The localized root operators on $\operatorname{Irr}(\widetilde{\mathcal C}_w)$ must already be defined.
- The map depends on the chosen reduced expression at the coordinate level; different reduced expressions are related by crystal isomorphisms, not by literal equality of coordinate systems.

## Do Not Write Yet

- Do not claim that $\operatorname{CP}$ is independent of the reduced expression as a coordinate map.
- Do not turn the $A_3$ cluster example into a visible topic-page example without a separate approval.
- Do not collapse the category-level map $\Phi_w$, the coordinate map $\operatorname{CP}$, and the localized root operators into one construction.
- Do not quote the detailed recursive main theorem formulas in a definition-ready topic page unless the page is explicitly being upgraded beyond definition-ready.
- Do not state the connectedness of $\mathcal B_{\underline w}$ on this page unless the page explicitly includes the later application from `inbox/papers/crystal.tex:4780-4816`.

## Proposed Next Edit After Approval

Fill only these sections of `content/topics/crystal-comparison-map.md`:

- `개요`: one paragraph saying that $\operatorname{CP}$ compares localized simple objects with cellular-crystal coordinates.
- `준비와 notation`: introduce $\underline w$, $\mathcal B_{\underline w}$, $\operatorname{Irr}(\widetilde{\mathcal C}_w)$, $\Phi_w$, $\widetilde C_\Lambda$, and $\widetilde E_i^*$.
- `map의 정의`: state the recursive coordinate definition and the localization-extension formula.
- `핵심 관점`: include only the level-separated diagram $\operatorname{Irr}(\widetilde{\mathcal C}_w)\to\mathcal B_{\underline w}$, not proof details.
- `기본 성질`: include only crystal morphism, bijectivity, and crystal isomorphism.
- `다른 topic들과의 관계`: link localized root operators, cellular crystals, localized crystals, and quiver-Hecke category localization.
- `Source notes`: cite the exact source locations above.

Leave `기본 예시` empty unless the $A_3$ example is separately approved.

## Applied Edit

The approved edit was applied to `content/topics/crystal-comparison-map.md`:

- Filled `개요`, `준비와 notation`, `map의 정의`, `핵심 관점`, `기본 성질`, `다른 topic들과의 관계`, `더 읽을 topic`, and `Source notes`.
- Left `기본 예시` empty because the $A_3$ example still needs separate review before visible page use.
- Updated the topic hierarchy, maturity tracker, research queue, review backlog, source note, and generated maps/status metadata.
- Added `quiver-hecke-category-localization` as an explicit prerequisite for the map page.

## Validation

- After applying the topic-page edit, `git diff --check` passed.
- `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and the internal Quartz build over 51 content files.
- Standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
