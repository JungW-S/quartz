# Type A Segment Convolution Example Source Review

## Scope

This is a report-only review of whether KKK18A or an already staged related source contains a compact paper-verified worked two-segment convolution example for `Type A Segment Module Convolutions`.

Inspected files and local texts:

- `content/topics/06-quiver-hecke-klr-algebras/type-a-segment-module-convolutions.md`
- `content/sources/papers/kang-kashiwara-kim18-symmetric-quiver-hecke-algebras-r-matrices.md`
- `content/sources/papers/kkko15-simplicity-heads-socles-tensor-products.md`
- `content/sources/papers/brundan13-quiver-hecke-algebras-categorification.md`
- local staged PDF text for KKK18A, KKKO15, and Brundan13

No paper was downloaded. No claim was added. No topic page, source note, example, localization material, or Grothendieck-ring comparison was added.

## Verdict

Do not add a visible example to `Type A Segment Module Convolutions` yet.

KKK18A has the correct theorem-level material for the page, but it does not contain a compact standalone numerical worked example for a pair

$$
L(a,b)\circ L(a',b').
$$

The closest staged-source candidate is Brundan13's type \(A_2\) character-level calculation for \(L(1)\circ L(2)\) and \(L(2)\circ L(1)\). It is useful background for low-rank quiver-Hecke convolution, but it is not a direct KKK18A interval-position example for Proposition 4.2.3 and does not by itself state the exact-sequence/head-socle mechanism used on the current topic page.

Therefore the example gap should remain open.

## KKK18A Findings

KKK18A Section 4.2 gives strong source support for the current topic:

- segment modules \(L(a,b)\);
- Proposition 4.2.3 for two-segment R-matrix and convolution cases;
- Proposition 4.2.5 for ordered multisegment classification;
- Lemma 4.2.6 for ordered-convolution head/socle comparison.

But the relevant pages are theorem/proof material, not a worked example. Proposition 4.2.3 gives general cases and exact sequences. The proof expands morphisms such as \(\xi_{a,c,b}\) and renormalized R-matrix maps. It does not select a small pair of concrete intervals and work through the convolution as a reader-facing example.

Instantiating arbitrary intervals from Proposition 4.2.3 would be a theorem instance chosen by the editor, not a paper example. Under the wiki example policy, that should not be presented as `검증: 논문 예시` unless the source itself provides the instance or a separate computation verifies it.

## Related Staged Sources

### KKKO15

KKKO15 supports general head/socle behavior for convolution with a real simple module. It does not contain a compact type \(A\) segment-module example in the KKK18A notation \(L(a,b)\circ L(a',b')\). It is useful for the broader `Head Simplicity of Convolutions` topic, not for filling this particular example gap.

### Brundan13

Brundan13 contains a compact type \(A_2\) calculation with convolution characters:

$$
\operatorname{Ch}(L(1)\circ L(2))=12+q21,
$$

$$
\operatorname{Ch}(L(2)\circ L(1))=21+q12.
$$

It also later explains the multisegment interpretation in type \(A\). This is the best staged-source candidate for a low-level quiver-Hecke convolution example.

However, it should not be inserted directly into `Type A Segment Module Convolutions` in the current pass:

- it is character-level, not the KKK18A Proposition 4.2.3 interval-position exact-sequence statement;
- it uses Brundan's survey notation and finite type \(A_2\) setup, not the KKK18A type \(A_\infty\) segment-module setup;
- it does not by itself identify the R-matrix image with the head/socle statement used on the current page.

If used later, it should first receive a small bridge review deciding whether it belongs on a lower-level page such as `Quiver-Hecke Module Categories` or as a cautious character-level note in `Type A KLR Segment Modules`.

## Recommended Handling

Keep `Type A Segment Module Convolutions` at `definition-ready` and keep the visible example omitted.

The next low-risk task is not to force an example. It is to polish the interval-position explanation already supported by KKK18A, so the page is more readable without adding unsupported numerical computations.

## Recommended Next Action

```text
Polish only the interval-position explanation in Type A Segment Module Convolutions. Do not add claims, examples, sources, theorem statements, localization material, or Grothendieck-ring comparison.
```
