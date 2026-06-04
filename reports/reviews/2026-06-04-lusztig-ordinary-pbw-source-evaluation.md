# Lusztig Ordinary PBW Source Evaluation

Date: 2026-06-04

## Scope

This is a report-only evaluation of a focused source for a future prerequisite topic:

```text
PBW Parametrizations of Quantum Unipotent Coordinate Rings
```

Source evaluated:

- George Lusztig, *Introduction to Quantum Groups*, reprint of the 1994 edition, Modern Birkhauser Classics, 2010.
- Local file: `inbox/papers/(Modern Birkhäuser Classics) George Lusztig (auth.) - Introduction to Quantum Groups-Birkhäuser Basel (2010).pdf`

No paper was downloaded. The book PDF was not copied into `content/assets/pdfs/`. No topic page, claim, source note, example, theorem statement, Sage code, image, or new topic was added.

## Verdict

The local Lusztig book is a suitable focused source for a definition-ready ordinary PBW prerequisite, provided the later intake is narrowly scoped.

The safest source boundary is:

- Chapter 40.1-40.2 for the braid-group root-vector construction and the PBW-type bases of \(U^+(w,e)\);
- Chapter 41.1 for the integral form and the relation with the canonical basis;
- Chapter 42.1 only as optional finite simply-laced context for reduced-word changes and piecewise-linear reparametrization.

This source should not be used to import localized PBW coordinates, frozen PBW vectors, JP25 Theorem 3.2, or quantum-twist coordinate formulas. Those remain JP25-localized material.

## Exact Source Locations

### Positive root-vector factors

- Chapter 40, Lemma 40.1.2, p. 320: proves that the braid-group transforms of simple positive generators land in \(U^+\) under the reduced-expression length condition.
- Chapter 40, Proposition 40.1.3, p. 320: for a reduced expression \(s_{i_1}\cdots s_{i_n}\), records that the successive braid-group transforms of the generators \(E_{i_k}\) lie in \(U^+\).

These locations support the ordered positive root-vector factors used to build PBW monomials.

### PBW-type basis attached to a reduced expression

- Chapter 40, Proposition 40.2.1, p. 321: for \(w\in W\), \(e=\pm1\), and a reduced expression \(s_{i_1}\cdots s_{i_n}=w\), constructs basis elements indexed by \(c=(c_1,\ldots,c_n)\in\mathbb N^n\). These elements form a basis of a subspace \(U^+(w,e)\), and the subspace does not depend on the chosen reduced expression.
- Chapter 40, Corollary 40.2.2, pp. 321-322: in finite type, for \(w_0\), the corresponding \(U^+(w_0,e)\) is all of \(U^+\), so the same construction gives a basis of \(U^+\).

These locations are the main source for the PBW-basis layer.

### Integral form and canonical-basis connection

- Chapter 41, Proposition 41.1.4, p. 325: gives the integral version of Proposition 40.2.1, producing an \(A\)-basis for the integral submodule attached to \(U^+(w,e)\).
- Chapter 41, Proposition 41.1.6, p. 325: for each reduced-expression datum and exponent vector \(c\), identifies a unique canonical-basis element congruent to the corresponding PBW-type element modulo the \(v^{-1}\)-part.
- Chapter 41, Proposition 41.1.7, p. 326: in finite type, the integral submodule for \(w_0\) is the full positive integral form.

These locations support the bridge from PBW monomials to canonical-basis parametrization. They are the most useful source locations for a definition-ready ordinary PBW prerequisite.

### Reduced-word changes and piecewise-linear reparametrization

- Chapter 42, Section 42.1, pp. 328-334: in the simply-laced finite-type case, describes reduced expressions for \(w_0\), elementary moves between reduced expressions, and the corresponding piecewise-linear maps on \(\mathbb N^n\).
- Chapter 42, Lemma 42.1.9, p. 332: gives the bijective parametrization by equivalence classes of reduced-expression/exponent-vector data.
- Chapter 42, Theorem 42.1.10, p. 332: identifies the canonical-basis lift from the mod-\(v^{-1}\) data.
- Chapter 42, 42.1.14, p. 333: records the resulting combinatorial parametrization of the canonical basis.

This is useful explanatory background for reparametrization between reduced expressions, but it is finite simply-laced context. It should not be presented as the general JP25 setup without qualification.

## What This Source Can Support

A later approved intake can safely support a compact prerequisite page explaining:

- a reduced expression \(w=s_{i_1}\cdots s_{i_n}\);
- the ordered positive factors obtained by applying Lusztig braid-group symmetries to \(E_{i_k}\);
- exponent vectors \(c\in\mathbb N^n\);
- the PBW-type monomial basis of \(U^+(w,e)\);
- the integral PBW basis and its relation to canonical-basis elements modulo \(v^{-1}\);
- why changing the reduced expression changes coordinates by controlled reparametrization in finite simply-laced type.

The page should be written as an ordinary prerequisite for `Localized PBW Parametrizations`, not as a source summary of Lusztig's book.

## What This Source Should Not Support Alone

Do not use this source alone for:

- the quantum unipotent coordinate ring \(A_q(\mathfrak n(w))\), which is already better handled through GLS11;
- the upper global basis notation \(G^{\mathrm{up}}(b)\) as used by JP25;
- frozen PBW vectors \(P_j\) and localized integer directions;
- the localized PBW parameter set \(\widetilde{\mathcal P}_{\mathbf i}(w)\);
- a worked example unless a later pass verifies one carefully from the book or with Sage;
- any public PDF link or copied PDF asset without separate legal redistribution approval.

The future topic should combine source boundaries:

- GLS11 for the coordinate-ring and dual PBW-basis language;
- Lusztig for the ordinary PBW/canonical-basis parametrization mechanism;
- JP25 only for the later localized extension.

## Recommendation

The next safe task is a narrow approved-source intake using the local Lusztig book, restricted to Chapter 40.2 and Chapter 41.1, with optional Chapter 42.1 context. Because this is a book PDF in `inbox/`, do not copy it into public site assets unless legal redistribution is explicitly approved.

Recommended prompt:

```text
Run a narrow approved-source intake for the local Lusztig book `inbox/papers/(Modern Birkhäuser Classics) George Lusztig (auth.) - Introduction to Quantum Groups-Birkhäuser Basel (2010).pdf`, restricted to Chapter 40.2, Proposition 41.1.4, Proposition 41.1.6, and optional Chapter 42.1 reduced-word transition context. Do not copy the PDF to `content/assets/pdfs/` unless legal redistribution is explicitly approved. Create a concise source note, add at most 4 claims, and create at most one new topic: `PBW Parametrizations of Quantum Unipotent Coordinate Rings`. Do not add examples, Sage code, images, localized PBW formulas, frozen-vector formulas, or JP25 Theorem 3.2 material.
```
