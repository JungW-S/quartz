# Nakashima 2022 Localized-Root-Operator Example Search

Date: 2026-06-01

Scope: report-only evaluation of source candidate `nakashima22-categorified-crystal-localized-quantum-coordinate-rings` for a concrete worked example suitable for `content/topics/localized-root-operators.md`.

## Source Checked

- Local PDF: `inbox/papers2/N22, Categorified crystal structure on localized quantum coordinate rings, arXiv.pdf`
- No network download was needed. The local file is an arXiv PDF for `arXiv:2208.08396v2`.
- Text extraction was used only for source-location review. No source note, claim, topic page, Sage code, image, or visible example was added.

## Decision

Nakashima 2022 should not be used as the visible `Localized Root Operators` basic example.

The paper gives a crystal structure on localized quantum coordinate rings and contains a concrete type $A_2$-style computation in Example 9.6, but the computation is about the inverse operation for the additive group structure on the localized crystal. It is not a worked example of the Kashiwara-Nakashima 2025 localized root-operator formulas involving $\widetilde Q_i$, head convolution, and the localized operator formulas on $\operatorname{Irr}(\widetilde{\mathcal C}_w)$.

Therefore `content/topics/localized-root-operators.md` should keep its `## 기본 예시` section empty until either a direct source-backed operator computation or a separately approved Sage/code verification workflow is available.

## Useful Source Locations

- Extracted text lines 1578-1585: Section 7 announces a crystal structure on localized quantum coordinate rings and on self-dual simple modules in the localized category.
- Extracted text lines 1642-1715: the paper defines Kashiwara operators on objects represented as $C_\Lambda \circ S$ and states Theorem 7.4, which says the resulting data form a crystal.
- Extracted text lines 2216-2258: the paper verifies compatibility of the localized crystal operators with the cellular crystal isomorphism, via formulas comparing $\widetilde\Psi(\widetilde F_i(C_\Lambda\circ S))$ with $\widetilde f_i\widetilde\Psi(C_\Lambda\circ S)$ and similarly for $\widetilde E_i$.
- Extracted text lines 2368-2384: Example 9.6 computes the inverse of $L(1)$ under the reduced-word-dependent operation $\oplus_{\mathbf i}$ in type $\mathfrak{sl}_3$:
  - for $\mathbf i=121$, $L(1)^{\ominus_{\mathbf i}} \simeq C_{-\Lambda_1}\circ L(2)$;
  - for $\mathbf i'=212$, $L(1)^{\ominus_{\mathbf i'}} \simeq C_{-\Lambda_2}\circ L(2)$.
- Extracted text lines 2400-2402: the paper poses a conjectural extension to arbitrary localized $\mathcal C_w$, so this location should not be used as a theorem-level source for topic exposition.

## Why This Does Not Fill The Example Gap

- The localized operators in Section 7 are formulated through $C_\Lambda\circ S$ and ordinary crystal operators on $S$.
- The current `Localized Root Operators` page follows the Kashiwara-Nakashima 2025 notation with localized simple-root objects $\widetilde Q_i$ and operator formulas using the simple head $\nabla$.
- Example 9.6 is a valid concrete localized-crystal computation, but it is not a computation of $\widetilde E_i X$ or $\widetilde F_i X$ using the KN25 localized root-operator formulas.
- Using Example 9.6 on the operator page would blur the distinction between a localized crystal-level additive operation and the specific localized root operators.

## Recommended Routing

Do not add a visible example to `content/topics/localized-root-operators.md`.

If Nakashima 2022 is later approved for intake, Example 9.6 may be worth routing to a broader page such as `content/topics/localized-crystals.md` or a future page about reduced-word-dependent additive operations on localized crystals. That should be a separate approval-gated task because the source is still only a candidate and has not been ingested into the source registry.

## Next Best Task

Design a report-only Sage/code verification plan for a localized-root-operator example. This should still not write code or generate images yet; it should first specify the mathematical object, convention translation, and which category-level statement still needs paper support.
