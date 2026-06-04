# Reverse Equivalence Example Review

Date: 2026-06-03

## Scope

This was a report-only review for `Reverse Equivalence of Localized Categories`.

Only the local Kashiwara-Nakashima 2025 TeX source `inbox/papers/crystal.tex` was checked. No paper was downloaded. No topic page, claim, source note, repository PDF, Sage code, image, or example was added.

## Source Checked

- Source: `kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category`.
- Local TeX: `inbox/papers/crystal.tex`.
- Target topic page: `content/topics/08-localization-of-categories/reverse-equivalence-of-localized-categories.md`.

## Source Locations

The source gives theorem-level reverse-equivalence material, but not a small worked example.

- `inbox/papers/crystal.tex`, lines 3040-3049: introduces the reverse monoidal category setup and the target category associated with $w^{-1}$.
- `inbox/papers/crystal.tex`, lines 3052-3065: defines the anti-automorphism $\psi$ on quiver-Hecke algebras and the induced monoidal equivalence
  $$
  \psi_* : (R\text{-gmod})^{\mathrm{rev}} \simeq R\text{-gmod}.
  $$
- `inbox/papers/crystal.tex`, lines 3068-3073: Lemma 5.6 records determinantial-module compatibility under $\psi_*$:
  $$
  \psi_*\bigl(M_w(w\lambda,\lambda)\bigr)
  \simeq
  M_{w^{-1}}(-\lambda,-w\lambda).
  $$
- `inbox/papers/crystal.tex`, lines 3076-3084: Theorem 5.7 gives the reverse monoidal equivalence between $(\widetilde{\mathcal C}_w)^{\mathrm{rev}}$ and $\widetilde{\mathcal C}_{w^{-1}}$.
- `inbox/papers/crystal.tex`, lines 3811-3828: a later lemma uses $\psi_*$ to rewrite a determinantial-module expression in the localized-root-operator proof.
- `inbox/papers/crystal.tex`, lines 3847-3852: a commutation statement is transferred from $w^{-1}$ to $w$ by applying $\psi_*$.
- `inbox/papers/crystal.tex`, lines 3907-3909: a starred-operator compatibility statement follows from the corresponding ordinary statement for $w^{-1}$ by applying $\psi_*$.
- `inbox/papers/crystal.tex`, lines 4791-4795: the connectedness proof uses Theorem 5.7 to get a crystal isomorphism via $\psi_*$ between the ordinary localized operators on $\operatorname{Irr}(\widetilde{\mathcal C}_w)$ and starred operators on $\operatorname{Irr}(\widetilde{\mathcal C}_{w^{-1}})$.

## Example Finding

No suitable visible example was found in Kashiwara-Nakashima 2025.

The checked source supplies:

- the definition of the anti-automorphism $\psi$;
- the induced reverse monoidal equivalence $\psi_*$;
- determinantial-module compatibility;
- theorem-level applications of $\psi_*$ inside localized-root-operator arguments;
- the crystal-level ordinary/starred comparison in the connectedness proof.

However, it does not give a compact worked example of the form "for this explicit object, $\psi_*$ sends it to this explicit object" or a concrete low-rank reverse-equivalence computation suitable for the visible `기본 예시` section.

## Proposed Topic-Page Wording

None.

The determinantial-module formula in Lemma 5.6 is already theorem-level structural content. It is useful source support for the statement of the page, but it should not be repackaged as a basic example unless a later source or verified computation supplies concrete objects.

## Recommendation

Keep `Reverse Equivalence of Localized Categories` definition-ready and leave its visible example omitted.

If an example is considered essential, the next pass should be a separate source search for a concrete low-rank computation of $\psi_*$ or a report-only Sage/code verification plan. Do not add an example from the theorem-level material alone.
