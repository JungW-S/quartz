# Brundan13 Induction And Restriction Source-Location Review

## Scope

This is a report-only review of exact Brundan13 source locations for a short induction/restriction paragraph suitable for `Quiver-Hecke Module Categories`.

Inspected local files:

- `content/assets/pdfs/brundan13-quiver-hecke-algebras-categorification.pdf`
- `content/sources/papers/brundan13-quiver-hecke-algebras-categorification.md`
- `content/topics/06-quiver-hecke-klr-algebras/quiver-hecke-module-categories.md`

No paper was downloaded. No claim was added. No source note or topic page was edited.

## Verdict

Brundan13 supports a compact reader-facing paragraph explaining that induction is the source of the convolution product, while restriction gives the corresponding Grothendieck-group comultiplication.

The safe level for the topic page is:

- define the algebra embedding \(H_\beta\otimes H_\gamma\hookrightarrow H_{\beta+\gamma}\);
- state the induced functors \(\operatorname{Ind}_{\beta,\gamma}^{\beta+\gamma}\) and \(\operatorname{Res}_{\beta,\gamma}^{\beta+\gamma}\);
- explain that \(X\circ Y\) is induction applied to \(X\boxtimes Y\);
- say that this gives monoidal products on \(\operatorname{Rep}(H)\) and \(\operatorname{Proj}(H)\), hence algebra structures on Grothendieck groups;
- say that restriction gives the coalgebra side.

The unsafe level for this page is importing the full Mackey-filtration formula or the twisted bialgebra formula. Those belong in a later, more technical topic if needed.

## Source Locations

Brundan13 Section 3, arXiv p.12:

- The subsection `Induction and restriction` defines the non-unital algebra embedding
  \[
  H_\beta\otimes H_\gamma\hookrightarrow H_{\beta+\gamma}.
  \]
- It defines the idempotent \(1_{\beta,\gamma}\).
- It defines
  \[
  \operatorname{Res}_{\beta,\gamma}^{\beta+\gamma}U := 1_{\beta,\gamma}U,
  \]
  and
  \[
  \operatorname{Ind}_{\beta,\gamma}^{\beta+\gamma}V
  := H_{\beta+\gamma}1_{\beta,\gamma}\otimes_{H_\beta\otimes H_\gamma}V.
  \]
- It states that both functors are exact, with exactness of induction following from the basis theorem.

Brundan13 Theorem 3.6, arXiv pp.12-13:

- The Mackey filtration describes how restriction interacts with induction.
- This theorem is important source support for the compatibility behind later Grothendieck-group structures.
- The full filtration formula is too technical for the current prerequisite page.

Brundan13 Section 3, arXiv p.13:

- For a graded left \(H_\beta\)-module \(X\) and a graded left \(H_\gamma\)-module \(Y\), Brundan defines
  \[
  X\circ Y := \operatorname{Ind}_{\beta,\gamma}^{\beta+\gamma}(X\boxtimes Y).
  \]
- The text states that this operation defines tensor product operations on \(\operatorname{Rep}(H)\) and \(\operatorname{Proj}(H)\), making them monoidal categories.
- Consequently, \([\operatorname{Rep}(H)]\) and \([\operatorname{Proj}(H)]\) become \(\mathbb Z[q,q^{-1}]\)-algebras.

Brundan13 Corollary 3.7, arXiv p.14:

- The Shuffle Lemma states
  \[
  \operatorname{Ch}(X\circ Y)=\operatorname{Ch}(X)\circ\operatorname{Ch}(Y).
  \]
- This supports the existing type \(A_2\) character-level convolution example.

Brundan13 Corollary 3.8 and surrounding paragraph, arXiv p.14:

- Restriction induces maps
  \[
  [\operatorname{Rep}(H)]\to
  [\operatorname{Rep}(H)]\otimes_{\mathbb Z[q,q^{-1}]}
  [\operatorname{Rep}(H)]
  \]
  and similarly for projectives.
- The Grothendieck groups become twisted bialgebras.
- The multiplication on \([\operatorname{Rep}(H)]\) is dual to the comultiplication on \([\operatorname{Proj}(H)]\), and vice versa.

## Proposed Later Paragraph

If approved, the following can be added to `Quiver-Hecke Module Categories` under `기본 성질` or `핵심 관점`.

```markdown
Brundan의 construction에서 $\beta,\gamma\in Q_+$에 대해 horizontal composition은 non-unital algebra embedding
$$
H_\beta\otimes H_\gamma\hookrightarrow H_{\beta+\gamma}
$$
을 준다. 이 embedding에서 오는 idempotent를 사용하면 $\operatorname{Ind}_{\beta,\gamma}^{\beta+\gamma}$와 $\operatorname{Res}_{\beta,\gamma}^{\beta+\gamma}$가 정의된다. 두 graded modules $X\in H_\beta\text{-gmod}$, $Y\in H_\gamma\text{-gmod}$에 대해 convolution product는
$$
X\circ Y=\operatorname{Ind}_{\beta,\gamma}^{\beta+\gamma}(X\boxtimes Y)
$$
이다. 그래서 induction은 module category의 monoidal product를 만들고, restriction은 Grothendieck group에서 그 product와 짝을 이루는 comultiplication을 만든다.
```

## Do Not Add Yet

Do not add the full Mackey-filtration formula to the topic page. It is source-backed, but it would make the prerequisite page too technical and would shift the page away from its role as a category-level bridge.

Do not add a new claim for this paragraph unless a later intake task explicitly asks to track this as reusable claim metadata.

## Recommended Next Action

```text
Using reports/reviews/2026-06-03-brundan13-induction-restriction-source-location-review.md, add only the proposed compact induction/restriction paragraph to Quiver-Hecke Module Categories. Do not add claims, source notes, new topic pages, Mackey-filtration formulas, localization material, or Grothendieck-ring comparison beyond the paragraph.
```
