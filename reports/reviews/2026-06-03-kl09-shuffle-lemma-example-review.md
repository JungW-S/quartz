# KL09 Shuffle Lemma Example Review

## Scope

This was a report-only source-location review for `Shuffle Lemmas for Quiver-Hecke Modules`.

The user-provided local KL09 PDF and TeX source were inspected. No paper was downloaded. No topic page, claim, source note, repository PDF, Sage code, image, or example was added.

## Source Checked

- Candidate source: `khovanov-lauda09-diagrammatic-categorification-quantum-groups-i`.
- Local PDF: `inbox/papers2/KL09, A diagrammatic approach to categorification of quantum groups I, Represent Theory, arxiv ver.pdf`.
- Local TeX: `inbox/papers2/Tex/KL09, A diagrammatic approach to categorification of quantum groups I, Represent Theory, arxiv ver/paper.tex`.
- Candidate metadata already records arXiv `0803.4121` and DOI `10.1090/S1088-4165-09-00346-X`.

## Lemma 2.20 Location

KL09 Section 2.6, `Induction and restriction`, contains the relevant shuffle setup.

Exact local TeX locations:

- `paper.tex`, lines 1727-1746: induction and restriction for the inclusion
  $R(\nu)\otimes R(\nu')\subset R(\nu+\nu')$.
- `paper.tex`, lines 1784-1817: Proposition 2.18, the Mackey-type bimodule filtration.
- `paper.tex`, lines 1824-1838: definition of a shuffle of two sequences and a generic diagram illustrating the shuffle.
- `paper.tex`, lines 1842-1854: Proposition 2.19, restriction of projectives as a direct sum over shuffle decompositions.
- `paper.tex`, lines 1856-1862: definition of the quantum shuffle product.
- `paper.tex`, lines 1864-1870: Lemma 2.20, stating
  $$
  \operatorname{ch}\bigl(\operatorname{Ind}_{\nu,\nu'}(M\otimes N)\bigr)
  =
  \operatorname{ch}(M)\shuffle \operatorname{ch}(N).
  $$

The extracted PDF text places the same material around lines 1569-1708 of `/tmp/kl09.txt`.

## Worked Example Finding

No suitable worked low-rank shuffle calculation was found.

The source does contain:

- a generic diagram illustrating how a shuffle sequence $\mathbf k$ contains subsequences corresponding to $\mathbf i$ and $\mathbf j$;
- the direct-sum formula for projective restrictions in Proposition 2.19;
- the character identity in Lemma 2.20.

However, it does not give a concrete small example with specified labels, an explicit degree computation, and an evaluated character shuffle product. Later examples in Section 3.5 concern tight monomials, indecomposable projectives, and canonical-basis behavior; they are not worked examples of Lemma 2.20.

## Proposed Example Wording

None.

KL09 Lemma 2.20 verifies the general character-shuffle mechanism, but it does not supply a real worked example suitable for the visible `기본 예시` section of `Shuffle Lemmas for Quiver-Hecke Modules`.

## Recommended Next Step

Keep `Shuffle Lemmas for Quiver-Hecke Modules` definition-ready and do not force an example.

If the page must become example-ready, use a separate approved source search for a paper-verified low-rank KLR induction/restriction calculation, or build a Sage/code-checked example only if the required KLR module computation can actually be implemented and verified.
