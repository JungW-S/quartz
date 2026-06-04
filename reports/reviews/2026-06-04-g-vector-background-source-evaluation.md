# g-Vector Background Source Evaluation

Date: 2026-06-04

## Scope

This is a report-only evaluation of possible background sources for cluster-theoretic \(g\)-vectors, pointed/copointed elements, dominance order, and triangular-basis language needed before `Left and Right g-Vectors` can move beyond orientation level.

Files inspected:

- `content/topics/04-cluster-algebras/cluster-algebras.md`
- `content/topics/04-cluster-algebras/quantum-cluster-algebras.md`
- `content/topics/08-localization-of-categories/left-and-right-g-vectors.md`
- `reports/reviews/2026-06-04-left-right-g-vectors-source-location-review.md`
- `reports/reviews/2026-06-04-jp25-type-a2-coordinate-example-review.md`
- `data/source_candidates.yml`
- `data/research_queue.yml`
- `data/topic_maturity.yml`
- `reports/roadmap/next-actions.md`

No paper was downloaded. No topic page, claim, source note, theorem statement, coordinate formula, example, Sage code, image, or new topic was added.

## Verdict

The best next approved-source intake should be `qin17-triangular-bases-quantum-cluster-algebras`, but it should not be used alone as a first undergraduate-facing introduction to \(g\)-vectors.

The reason is structural:

- JP25 uses \(g\)-vectors through pointed/copointed bases and dominance order.
- Qin 2017 is the focused source that matches that language most directly.
- Fomin-Zelevinsky 2007 is the lower-level source for cluster-algebra \(g\)-vector background, but it does not by itself supply the pointed/copointed basis layer needed in JP25.
- The wiki already has readable `Cluster Algebras` and `Quantum Cluster Algebras` pages, but neither page currently explains \(g\)-vectors, pointed/copointed elements, or dominance order.

Therefore the safest path is:

1. first approve Qin 2017 as the exact source for a focused intake;
2. during intake, use only the sections needed for dominance order, pointed/copointed elements, degree/codegree language, and triangular bases;
3. keep Fomin-Zelevinsky 2007 as a backup candidate if the \(g\)-vector definition needs a lower-level classical prerequisite paragraph.

## Candidate Assessment

### Qin 2017

Candidate id:

- `qin17-triangular-bases-quantum-cluster-algebras`

This is the strongest match for the immediate JP25 gap. ArXiv and author metadata identify it as Fan Qin, *Triangular bases in quantum cluster algebras and monoidal categorification conjectures*, Duke Math. J. 166 (2017), 2337-2442, arXiv:1501.04085, DOI 10.1215/00127094-2017-0006.

Useful scope for a later approved intake:

- dominance order;
- pointed and copointed elements/sets;
- degree and codegree language for basis elements;
- triangular basis terminology;
- relation to monoidal categorification conjectures.

Risks:

- It is advanced and should not be allowed to turn `Quantum Cluster Algebras` into a paper-specific technical page.
- It may use conventions that need translation before comparison with JP25 and the wiki's existing KKKO/GLS-adjacent notation.
- It is suitable for definitions and source notes only after explicit intake approval; as a candidate, it does not support claims yet.

### Fomin-Zelevinsky 2007

Candidate id added:

- `fomin-zelevinsky07-cluster-algebras-iv-coefficients`

This is the better low-level backup for ordinary cluster-algebra \(g\)-vector background. ArXiv metadata identifies it as Sergey Fomin and Andrei Zelevinsky, *Cluster algebras IV: Coefficients*, arXiv:math/0602259, with journal version in Compositio Mathematica 143 (2007), 112-164.

Useful scope for a later approved intake:

- principal coefficients;
- coefficient dynamics;
- \(g\)-vector style multi-grading background;
- classical cluster-algebra prerequisites before quantum/pointed basis language.

Risks:

- It does not directly provide the pointed/copointed basis and dominance-order language that JP25 invokes.
- It is better as a prerequisite supplement than as the main source for `Left and Right g-Vectors`.

## Recommended Intake Boundary

If Qin 2017 is approved later, the intake should remain narrow.

Allowed for a later approved intake:

- add a source note for Qin 2017;
- add at most a small number of claims about definitions actually used by JP25;
- update `Quantum Cluster Algebras` only with a short \(g\)-vector/dominance-order prerequisite paragraph if source locations are exact;
- update `Left and Right g-Vectors` only enough to make the cluster-theoretic definition boundary clear;
- keep JP25 Theorem 3.2 formulas out unless separately approved.

Not allowed without separate approval:

- downloading or ingesting Fomin-Zelevinsky 2007 together with Qin 2017;
- importing triangular-basis theorems not needed for the local \(g\)-vector prerequisite;
- importing examples without paper-verified or Sage-verified support;
- adding the JP25 type \(A_2\) coordinate example;
- adding coordinate matrices or theorem formulas.

## Prerequisite Gaps

The following gaps remain after this evaluation:

- `Quantum Cluster Algebras` does not explain \(g\)-vectors, dominance order, or pointed/copointed elements.
- `Left and Right g-Vectors` does not yet have a complete definition section.
- `Coordinate Formulas for Quantum Twist on Localized Crystals` remains blocked by the missing \(g\)-vector definition layer.
- If Qin 2017 proves too compressed for exposition, Fomin-Zelevinsky 2007 should be evaluated as a separate lower-level intake, not silently mixed into the same source note.

## Recommended Next Step

Ask for exact source approval for Qin 2017 before downloading or ingesting it.

Recommended prompt:

```text
I approve source intake for qin17-triangular-bases-quantum-cluster-algebras only. Use it narrowly for dominance order, pointed/copointed elements, degree/codegree language, and triangular-basis terminology needed for Left and Right g-Vectors. Do not download or ingest any other source. Add at most 8 claims and update at most 3 topic pages.
```
