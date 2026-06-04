# KKKO18 Final Access Shuffle Example Review

## Scope

This was a report-only legal-access and source-location review for `Shuffle Lemmas for Quiver-Hecke Modules`.

No topic page, claim, source note, Sage code, image, or repository PDF was added. The arXiv source and PDF for `1801.05145` were inspected only under `/tmp`.

## Access Finding

The legitimate open-access version is:

- arXiv: `1801.05145`
- Title: `Monoidal categorification of cluster algebras (merged version)`
- Authors: Seok-Jin Kang, Masaki Kashiwara, Myungho Kim, Se-jin Oh
- arXiv submitted date: 2018-01-16
- arXiv page comment: 91 pages, merged version of `arXiv:1412.8106` and `arXiv:1502.06714`; this version is published in Journal of the American Mathematical Society.
- Journal metadata cross-check: Journal of the American Mathematical Society 31 no. 2 (2018), 349-426, DOI `10.1090/JAMS/895`.

## Proposition 10.1.5 Location

The `/tmp` PDF text extraction confirms:

- Extracted PDF text lines 3565-3583: the end of the Chevalley/Kashiwara operator definition, including $E_i$, $E_i^*$, $\varepsilon_i$, $\varepsilon_i^*$, $\widetilde E_i$, and $L(i^n)$.
- Extracted PDF text lines 3594-3694: Propositions 10.1.2 and 10.1.3, giving the braid-word homomorphism setup leading into the divided restriction functors.
- Extracted PDF text lines 3695-3709: definition of $E_i^{(n)}$ and $E_i^{*(n)}$.
- Extracted PDF text lines 3728-3735: Proposition 10.1.5.
- Extracted PDF text lines 3736-3741: Corollaries 10.1.6 and 10.1.7 as immediate consequences.

The TeX source location is `/tmp/kkko18-merged.tex`, lines 5835-5853. The proposition is labeled `\label{prop: Econv}`.

## Worked Example Finding

No worked example suitable for the visible `기본 예시` section was found.

Searches in the merged TeX source found no `example` environment beyond the theorem declaration. The only lower-case `example` occurrences are prose-level mentions in the introduction and a generic reference to another definition source.

Proposition 10.1.5 itself is a general statement:

- It gives an isomorphism for $E_i^{(m+n)}(M\circ N)$ under vanishing hypotheses on $E_i^{m+1}M$ and $E_i^{n+1}N$.
- It gives the analogous isomorphism for $E_i^{*(m+n)}(M\circ N)$.
- Its proof says the assertions follow from the shuffle lemma, cited as KL09 Lemma 2.20.

Therefore this source confirms the exact proposition behind KN25 Section 4.7, but it still does not provide a compact worked example.

## Proposed Example Wording

None.

Do not add a visible example from KKKO18 Proposition 10.1.5. The result can support source-location verification of the theorem statement, but the example gap remains.

## Recommended Next Step

Keep `Shuffle Lemmas for Quiver-Hecke Modules` at definition-ready. The lowest-risk next task is sentence-flow polishing only, without adding an example.

If a real example is still required, evaluate KL09 Lemma 2.20 or another approved source specifically for a worked low-rank shuffle calculation before editing the topic page.
