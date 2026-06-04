# Quantum Affine Lower-Level Example Source Evaluation

## Scope

This pass evaluates lower-level sources for a compact first example suitable for:

- `content/topics/07-quantum-affine-algebras/quantum-affine-algebras.md`

No paper was downloaded. No claim was added. No topic page was edited. No child topic was created.

Local filename search found no local copy of Akasaka-Kashiwara 1997, Chari-Pressley 1991, or Chari-Pressley 1994. The only local quantum-affine files found were:

- `inbox/papers2/KKMMNN92, Perfect crystals of quantum affine Lie algebras, Duke Math J.pdf`
- `inbox/papers2/KKOP24, PBW theory for quantum affine algebras, JEMS.pdf`
- `inbox/papers2/Tex/KKOP24, PBW theory for quantum affine algebras, JEMS/`

## Verdict

Do not add a `Quantum Affine Algebras` example yet.

The best next source to approve for a narrow source-location review is Akasaka-Kashiwara 1997, because EMS Press provides a legitimate article page with a PDF access option. Chari-Pressley 1991 is mathematically attractive for a first \(U_q(\widehat{\mathfrak{sl}}_2)\) evaluation-representation example, but the official Springer page is subscription/paywalled. Chari-Pressley 1994 is a book and no legitimate open full-text access was found in this pass.

## Candidate 1: Akasaka-Kashiwara 1997

Source:

- Tatsuya Akasaka and Masaki Kashiwara, `Finite-Dimensional Representations of Quantum Affine Algebras`
- *Publications of the Research Institute for Mathematical Sciences* 33 (1997), no. 5, 839-867
- DOI: `10.2977/PRIMS/1195145020`
- Official page: `https://ems.press/journals/prims/articles/3885`

Legal access assessment:

- EMS Press gives an official article page and shows a `Download PDF` action.
- The PDF was not downloaded or staged in this pass.

Mathematical fit:

- The abstract says the paper studies tensor products of fundamental representations of quantized affine algebras and the relation with poles of R-matrices.
- Searchable official text snippets record the standard parameterization: finite-dimensional irreducible representations appear as irreducible subquotients of tensor products of fundamental representations \(V(\varpi_i)_a\) with spectral parameters.
- This is aligned with the current parent page's notation \(V(\varpi_i)\), spectral parameters, and \(R\)-matrices.

Limitation:

- The article is already representation-theoretic and R-matrix oriented.
- No compact first example was verified without reading the PDF.
- It may support a source-backed example of fundamental modules with spectral parameters, but it should be approved for a narrow source-location review before any topic edit.

Proposed wording now:

- None. Do not insert text into the topic page yet.

Possible wording to test in a later approved pass:

```markdown
### 실제 예시: fundamental representation with a spectral parameter

For \(i\in I_0\) and a spectral parameter \(a\), the module \(V(\varpi_i)_a\) is a finite-dimensional \(U_q'(\mathfrak g)\)-module. It is one of the basic building blocks from which finite-dimensional simple modules are organized.

검증: 논문 예시
```

This wording is not approved for insertion yet. It needs exact source-page verification from Akasaka-Kashiwara 1997.

## Candidate 2: Chari-Pressley 1991

Source:

- Vyjayanthi Chari and Andrew Pressley, `Quantum affine algebras`
- *Communications in Mathematical Physics* 142 (1991), no. 2, 261-283
- DOI: `10.1007/BF02102063`
- Official page: `https://link.springer.com/article/10.1007/BF02102063`

Legal access assessment:

- Springer provides the official article page and abstract.
- The page is subscription/paywalled: it asks for institutional login or purchase.
- The PDF was not downloaded or accessed in this pass.

Mathematical fit:

- The abstract states that the paper classifies finite-dimensional irreducible representations of \(U_q(\widehat{\mathfrak{sl}}_2)\).
- The abstract also says it gives an explicit construction of all such representations using Jimbo's evaluation homomorphism
  $$
  U_q(\widehat{\mathfrak{sl}}_2)\to U_q(\mathfrak{sl}_2).
  $$
- This is probably the best mathematical direction for a parent-page first example, because it can relate quantum affine modules back to the already explained \(U_q(\mathfrak{sl}_2)\) representation theory.

Limitation:

- Because no legal full-text access was available, exact source locations inside the article were not verified.
- Do not cite or use it for topic-page text until a legal PDF is supplied or an approved access route is found.

Proposed wording now:

- None. Do not insert text into the topic page yet.

## Candidate 3: Chari-Pressley 1994

Source:

- Vyjayanthi Chari and Andrew Pressley, `A Guide to Quantum Groups`
- Cambridge University Press, 1994

Legal access assessment:

- Public metadata exists through Google Books/Open Library/CiNii-style records.
- No legitimate open full-text access was verified in this pass.
- Unofficial scan sites should not be used.

Mathematical fit:

- The book is likely useful as textbook background, but it is too broad for the current target unless a specific chapter/page location is verified.

Limitation:

- No exact example location was verified.
- Do not use it for claims or examples without a user-provided copy or another legitimate access route.

Proposed wording now:

- None.

## Recommendation

The next approved source task should be narrow:

1. Approve Akasaka-Kashiwara 1997 for a source-location review using the EMS Press open-access PDF.
2. Inspect only for a compact finite-dimensional \(U_q'(\mathfrak g)\)-module example, preferably a fundamental representation with spectral parameter.
3. Do not add claims or edit the topic page until the exact page/statement is selected.

If the user can provide Chari-Pressley 1991, that source may be better for a \(U_q(\widehat{\mathfrak{sl}}_2)\) evaluation-representation example, but it is blocked by legal access in the current environment.
