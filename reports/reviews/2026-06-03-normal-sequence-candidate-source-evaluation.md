# Normal Sequence Candidate Source Evaluation

Date: 2026-06-03

## Scope

This report evaluates whether the `Normal Sequences` topic can receive a paper-verified low-rank example from already local or already staged sources.

No paper was downloaded. No topic page was edited. No claim, source note, Sage code, image, or generated example was added.

## Standard Used

A visible example for `Normal Sequences` should give named simple objects and a verified normality check. A theorem family or proof mechanism is not enough unless it can be presented as a clearly labeled `구조 예시` without pretending to be a low-rank computation.

## Sources Checked

### KN25 and KKKO15

The earlier report `reports/reviews/2026-06-03-normal-sequences-example-scope-review.md` already checked:

- Kashiwara-Nakashima 2025, `inbox/papers/crystal.tex`;
- KKKO15, local TeX/PDF for simplicity of heads and socles.

That report found definitions, recognition criteria, and head/socle background, but no compact concrete normal-sequence example.

### Kang-Kashiwara-Kim 2018

Local source:

- `content/assets/pdfs/kang-kashiwara-kim18-symmetric-quiver-hecke-algebras-r-matrices.pdf`;
- `content/sources/papers/kang-kashiwara-kim18-symmetric-quiver-hecke-algebras-r-matrices.md`.

Relevant locations:

- Section 4.2 defines segment modules \(L(a,b)\).
- Proposition 4.2.3 gives two-segment R-matrix and convolution cases.
- Lemma 4.2.6 compares heads of ordered segment convolutions with shifted socles of reversed convolutions.
- Proposition 4.2.7 states that for a simple module with associated ordered multisegment, the composed R-matrix
  \[
  r:=r_{L_1,\ldots,L_t}:L_1\circ\cdots\circ L_t\to q^d L_t\circ\cdots\circ L_1
  \]
  has image isomorphic to that simple module, and its proof says the morphism does not vanish.

Evaluation:

This is the closest currently available source for a future structural example. It gives a concrete family in type \(A\) segment-module language and a nonvanishing composed R-matrix. However, Section 4.2 does not present this as a low-rank normal-sequence example, and the terminology is not the same as the `Normal Sequences` page. It should not be inserted immediately as a visible example.

If later approved, the safe route is a wording-only review for a clearly labeled `구조 예시`, using the already developed `Type A Segment Module Convolutions` prerequisite page. The wording must not call it a paper-provided low-rank example.

### KK19

Local source:

- `inbox/papers2/KK19, Laurent phenomenon and simple modules of quiver Hecke algebras, Compos Math, arxiv ver.pdf`;
- `inbox/papers2/Tex/KK19, Laurent phenomenon and simple modules of quiver Hecke algebras, Compos Math, arxiv ver/source.tex`.

Relevant locations:

- local TeX lines 1707-1728 define normal sequences of real simple modules and record the head/socle consequence;
- local TeX lines 1731-1830 give recursive normality criteria;
- local TeX lines 1835-1840 prove that the sequence
  \[
  (S_l^{\circ a_l},S_{l-1}^{\circ a_{l-1}},\ldots,S_1^{\circ a_1},
  M_1^{\circ b_1},M_2^{\circ b_2},\ldots,M_l^{\circ b_l})
  \]
  is normal.

Evaluation:

This is the most direct source using the words `normal sequence`. But the displayed family depends on monoidal seeds, cluster variables, and the \(S_k,M_k\) notation. It is useful for a later monoidal-categorification route, not for the first example on the prerequisite `Normal Sequences` page.

### KKOP24

Local source:

- `content/assets/pdfs/kkop24-pbw-theory-quantum-affine-algebras.pdf`;
- `inbox/papers2/Tex/KKOP24, PBW theory for quantum affine algebras, JEMS/source.tex`;
- `content/sources/papers/kkop24-pbw-theory-quantum-affine-algebras.md`.

Relevant locations:

- local TeX lines 1878-1900 define normal sequences and record the head/socle consequence;
- local TeX lines 3818-3830 state that ordered tensor products of affine cuspidal modules form normal sequences and have simple heads;
- local TeX lines 3876-3897 give a type \(A_2^{(1)}\) affine cuspidal module example.

Evaluation:

This is a valid advanced source path, but it belongs to affine cuspidal modules, PBW theory, and quantum affine categories. It is too far downstream for the first `Normal Sequences` example.

### KP18

Local source:

- `inbox/papers2/KP18, Affinizations and R-matrices for quiver Hecke algebras, JEMS.pdf`;
- `inbox/papers2/Tex/KP18, Affinizations and R-matrices for quiver Hecke algebras, JEMS/source.tex`.

Relevant locations:

- local TeX lines 1174-1255 define affinizations and give examples/non-examples of affinizations;
- local TeX lines 1457-1702 discuss R-matrices for affinizations and convolution products;
- local TeX lines 1767-1837 give strong affinization examples for powers/root modules.

Evaluation:

KP18 is useful background for affinizations and R-matrices, but it does not provide a compact normal-sequence example for the current page.

## Decision

Do not add a visible `기본 예시` to `Normal Sequences` now.

No compact paper-verified low-rank normal-sequence calculation was found. The page should remain `definition-ready` and incomplete only because the example is intentionally absent.

## Candidate Ranking

1. KKK18A: best future structural-example candidate, because ordered multisegments and composed R-matrices are already connected to existing type \(A\) KLR topic pages.
2. KK19: most direct normal-sequence terminology, but too dependent on monoidal seed and cluster-categorification notation for the first example.
3. KKOP24: valid but too advanced; save for affine cuspidal modules or PBW theory.
4. KP18: not a normal-sequence example source.

## Recommended Next Action

If the strict requirement is a low-rank paper or Sage calculation, keep the example omitted.

If a structural example is acceptable, run a separate wording-only review:

```text
Using reports/reviews/2026-06-03-normal-sequence-candidate-source-evaluation.md, draft proposed wording only for a clearly labeled 구조 예시 in Normal Sequences based on KKK18A Proposition 4.2.7. Do not edit topic pages, add claims, or call it a low-rank paper example; explicitly state the terminology and affreal-condition caveats.
```
