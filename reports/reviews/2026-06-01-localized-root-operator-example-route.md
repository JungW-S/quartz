# Localized Root Operator Example Route Decision

Date: 2026-06-01

## Scope

This is a report-only decision on whether the next visible example for `content/topics/08-localization-of-categories/localized-root-operators.md` should come from a new approved source or from a Sage/code verification workflow.

No source was downloaded. No Sage code was written. No topic page was edited. No claims were added.

## Decision

Use a new-source evaluation route first. Do not start with Sage/code verification.

The needed example is category-level: it should show a localized simple object $X$ and compute an operator such as
$$
\widetilde F_iX
=q_i^{\varepsilon_i(X)}\,\widetilde Q_i\nabla X
$$
or the corresponding $\widetilde E_i$, $\widetilde F_i^*$, or $\widetilde E_i^*$ in a way that identifies the resulting localized simple object. That requires source control over the localized category, $\widetilde Q_i$, head convolution, and R-matrix degree conventions.

Sage can be useful later for checking ordinary combinatorial crystal behavior, but Sage/Schilling conventions are not the wiki's Kashiwara convention by default. More importantly, Sage does not by itself verify the category-level head-convolution statement in $\widetilde{\mathcal C}_w$. A Sage example without a source-level dictionary would risk producing only a combinatorial shadow, not a verified localized-root-operator example.

## Candidate Route

### Preferred next source candidate

Evaluate `nakashima22-categorified-crystal-localized-quantum-coordinate-rings` first.

Reason:

- The candidate is already recorded in `data/source_candidates.yml`.
- Its target topics include localized crystals and localized quantum coordinate rings, so it is closer to localized-root-operator examples than general crystal texts.
- It is a predecessor or companion candidate for the Kashiwara-Nakashima 2025 setting, so it is more likely than general crystal sources to use the same category-level objects.

What the evaluation should look for:

- an explicit low-rank or named localized simple object $X$;
- an explicit computation of $\widetilde F_iX$, $\widetilde E_iX$, $\widetilde F_i^*X$, or $\widetilde E_i^*X$;
- enough notation to translate into the wiki's Kashiwara-style convention;
- exact source locations supporting the example.

### Lower-priority source candidates

- KKOP localization papers may be better for formal localization properties than for a first undergraduate-facing worked operator example.
- Marberg, Hong-Kang, Kashiwara 1993, and Bump-Schilling are useful for ordinary crystal prerequisites but do not target localized category-level operators.
- SageMath should be deferred until the mathematical object and notation dictionary are fixed by an approved source.

## Sage/Code Route

A Sage/code route should only be used after a separate plan answers all of the following:

- Which ordinary crystal or combinatorial model is being computed?
- How does the computed object correspond to a localized simple object in $\widetilde{\mathcal C}_w$?
- Which convention translation is being applied from Sage/Schilling notation to the wiki's Kashiwara notation?
- Which part of the example is verified by code, and which part still requires a paper source?

Without those answers, Sage can verify an ordinary crystal arrow but not the category-level formula involving $\widetilde Q_i\nabla X$.

## Recommendation

The next safest task is to approve and evaluate `nakashima22-categorified-crystal-localized-quantum-coordinate-rings` only for a report-only search for concrete localized-root-operator examples. If the source has no worked example, keep `## 기본 예시` empty and then decide whether a Sage/code plan is worth designing.

## Next Prompt

```text
I approve source candidate `nakashima22-categorified-crystal-localized-quantum-coordinate-rings` for a report-only search for concrete localized-root-operator examples. Download only from a legitimate open-access source such as arXiv if available. Do not add claims, do not rewrite topic pages, do not create Sage code or images, and do not add a visible example. Produce a source-location report and update backlog/roadmap only.
```
