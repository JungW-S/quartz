# Example Source-Location Tightening

Date: 2026-06-01

## Scope

This report checks the five visible examples that were marked "needs review before labeling" in `reports/reviews/2026-06-01-example-verification-label-audit.md`.

No topic page was rewritten. No claims were added. No sources were downloaded. No Sage code or images were generated.

## Decision

All five checked examples can later receive the visible label `검증: 논문 예시`, provided the topic-page edit also adds concise exact provenance in final `Source notes`.

No Sage verification is needed for these five examples. None of the five examples needs to be emptied on source-coverage grounds.

The two structural examples should keep the `### 구조 예시` heading. Their label should mean "this mechanism is explicitly supported by the approved paper source," not "this is a separate concrete category example."

## Per-Topic Results

### Cellular Crystals

Current example:

- $w=s_i$ gives $\mathcal B_{s_i}=B_i$.

Decision:

- Label-ready as `검증: 논문 예시`.
- This is an immediate one-letter specialization of the cellular-crystal definition, not an independent computed example.

Source support:

- `inbox/papers/crystal.tex:1413-1430`: defines the elementary crystal $B_i$.
- `inbox/papers/crystal.tex:1458-1461`: defines the cellular crystal associated with a reduced expression as $B_{i_1}\otimes\cdots\otimes B_{i_k}$.
- `inbox/papers/crystal.tex:1473-1480`: records the tensor-coordinate notation for $\mathcal B_w$.

Recommended later edit:

- Add `검증: 논문 예시` directly below the example.
- In final `Source notes`, add that the $w=s_i$ example is the length-one specialization of the KN25 cellular-crystal definition together with the elementary-crystal definition.

### Graded Monoidal Categories

Current example:

- `구조 예시` for
  $$
  q(X\otimes Y)\simeq(qX)\otimes Y\simeq X\otimes(qY).
  $$

Decision:

- Label-ready as `검증: 논문 예시`.
- Keep the heading `### 구조 예시`; this is a source-supported mechanism, not a concrete category example.

Source support:

- `inbox/papers/crystal.tex:1550-1577`: finite-length graded category assumptions, grading shift $q$, and graded HOM.
- `inbox/papers/crystal.tex:1646-1658`: graded monoidal category assumptions and the compatibility formula for $q$ and tensor product.
- `inbox/papers/crystal.tex:1665-1669`: identifies $q$ with the invertible central object $q\mathbf 1$ and extends the monoidal structure to $\operatorname{Pro}(\mathscr C)$.

Recommended later edit:

- Add `검증: 논문 예시` directly below the structural example.
- The existing Source notes already contain the key line ranges; no mathematical rewrite is needed.

### Pro-Categories

Current example:

- `구조 예시` for recovering $\widehat M$ from the quotient system
  $$
  \widehat M/z\widehat M,\quad
  \widehat M/z^2\widehat M,\quad
  \widehat M/z^3\widehat M,\ldots
  $$

Decision:

- Label-ready as `검증: 논문 예시`.
- Keep the heading `### 구조 예시`; this is the $A=\mathbf k[z]$ completion mechanism used in the affine-object setup, not a broad pro-category example.

Source support:

- `inbox/papers/crystal.tex:1526-1548`: defines pro-objects and $\operatorname{Pro}(\mathscr C)$.
- `inbox/papers/crystal.tex:1578-1621`: defines $\operatorname{Pro}^{\mathrm{coh}}(A,\mathscr C)$ using quotient and completion conditions.
- `inbox/papers/crystal.tex:1623-1630`: specializes to $A=\mathbf k[z]$ and writes the recovery condition $\widehat M\simeq\varprojlim_n\widehat M/z^n\widehat M$.

Recommended later edit:

- Add `검증: 논문 예시` directly below the structural example.
- In final `Source notes`, add the affine-object specialization lines `1623-1630` if they are not already recorded.

### Quiver-Hecke Algebras

Current example:

- The nil-Hecke special case $H_{n\alpha_i}\simeq NH_n$.
- The type $A_2$ case with irreducible modules $L(12)$ and $L(21)$ and the path-algebra description.

Decision:

- Label-ready as `검증: 논문 예시`.
- The current example combines two Brundan examples. A single label is acceptable if Source notes record both exact locations.

Source support:

- Brundan 2013, Section 2, arXiv pp.5-6: defines $NH_n$, its generators, relations, polynomial representation, and basis theorem.
- Brundan 2013, Section 2, arXiv p.7: states that if $\alpha=n\alpha_i$, then $H_{n\alpha_i}$ is a copy of $NH_n$ and has one irreducible graded left module up to degree shift.
- Brundan 2013, Section 3, arXiv p.18, "Some examples": for type $A_2$ and $\alpha=\alpha_1+\alpha_2$, records the characters of $L(1)\circ L(2)$ and $L(2)\circ L(1)$, the one-dimensional modules $L(12)$ and $L(21)$, and the isomorphism with $A\otimes K[x]$ where $A$ is the path algebra of the two-vertex quiver in (3.11).

Recommended later edit:

- Add `검증: 논문 예시` directly below the example.
- Tighten final `Source notes` to include Brundan 2013 Section 2 arXiv pp.5-7 and Section 3 arXiv p.18 for the visible example.

### Quiver-Hecke Module Categories

Current example:

- Type $A_2$ has irreducible graded $H_\alpha$-modules $L(12)$ and $L(21)$ up to degree shift.

Decision:

- Label-ready as `검증: 논문 예시`.
- No Sage verification is needed.

Source support:

- Brundan 2013, Section 3, arXiv p.18, "Some examples": for the type $A_2$ highest root $\alpha=\alpha_1+\alpha_2$, the source states that the irreducible graded $H_\alpha$-modules up to isomorphism and degree shift are the one-dimensional modules $L(12)$ and $L(21)$.

Recommended later edit:

- Add `검증: 논문 예시` directly below the example.
- Tighten final `Source notes` to include Brundan 2013 Section 3 arXiv p.18.

## Summary Table

| Topic | Decision | Sage needed? | Later topic edit |
| --- | --- | --- | --- |
| `cellular-crystals` | label-ready as a length-one specialization of the source definition | no | add label and source note lines |
| `graded-monoidal-categories` | label-ready as a source-supported structural mechanism | no | add label only, source notes already adequate |
| `pro-categories` | label-ready as a source-supported structural mechanism | no | add label and affine-object specialization lines |
| `quiver-hecke-algebras` | label-ready from Brundan 2013 examples | no | add label and exact Brundan source lines |
| `quiver-hecke-module-categories` | label-ready from Brundan 2013 type $A_2$ example | no | add label and exact Brundan source line |

## Recommended Follow-Up

With explicit topic-page edit approval, add `검증: 논문 예시` labels to these five examples and add concise provenance lines in final `Source notes` where needed.

Do not change the mathematics of the examples. Do not add claims. Do not download sources. Do not generate Sage code or images.

## Validation

Validation is recorded in `reports/roadmap/next-actions.md`.
