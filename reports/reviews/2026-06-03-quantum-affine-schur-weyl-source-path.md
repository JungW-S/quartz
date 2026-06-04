# Quantum Affine Schur-Weyl Source Path

## Scope

This report reviews only already ingested or locally staged KKOP24 material for a possible child topic:

- `Quantum Affine Schur-Weyl Duality`

No paper was downloaded. No claim was added. No topic page was created or edited.

Local source inspected:

- `inbox/papers2/Tex/KKOP24, PBW theory for quantum affine algebras, JEMS/source.tex`
- `content/sources/papers/kkop24-pbw-theory-quantum-affine-algebras.md`
- `content/topics/07-quantum-affine-algebras/quantum-affine-algebras.md`
- `content/topics/07-quantum-affine-algebras/hernandez-leclerc-categories.md`

## Verdict

`Quantum Affine Schur-Weyl Duality` is mathematically justified as a separate child topic under `Quantum Affine Algebras`, after `Hernandez-Leclerc Categories`.

It is not ready to be written as a full study article from KKOP24 alone. KKOP24 gives strong source locations for the bridge from symmetric quiver-Hecke module categories to quantum affine module categories, but the exposition depends on several advanced prerequisites:

- symmetric quiver-Hecke module categories;
- R-matrix invariants and affinizations;
- root modules;
- strong duality data;
- Hernandez-Leclerc categories;
- duals in the quantum affine module category.

The safe next use is a small definition-scope child topic. It should explain what the duality functor compares and record the main good properties only under the strong-duality-datum hypotheses. It should not import PBW theory, affine cuspidal modules, or monoidal-categorification consequences yet.

## Source Locations

### Why The Topic Belongs Here

- `source.tex:803-821`: abstract-level scope. KKOP24 works with \(U_q'(\mathfrak g)\), Hernandez-Leclerc's category, duality data, duality functors, strong/complete duality data, and affine cuspidal modules.
- `source.tex:884-896`: introduction-level comparison. Quantum affine Schur-Weyl duality connects quiver-Hecke algebras and quantum affine algebras by a monoidal functor from \(R_{\mathsf C}\)-modules to \(\mathcal C_{\mathfrak g}\).
- `source.tex:945-963`: precise motivation. The paper studies affinizations in both categories so the duality functor can compare R-matrix invariants and induce a Grothendieck-ring-level map under strong hypotheses.

### Definition Layer

- `source.tex:2731-2747`: defines a duality datum \(\mathscr D=\{R_i\}_{i\in J}\) and states that it gives a monoidal functor
  $$
  \mathcal F_{\mathscr D}:R_{\mathsf C}\operatorname{-gmod}\longrightarrow \mathcal C_{\mathfrak g}.
  $$
- `source.tex:2888-2948`: constructs the modified quantum affine Schur-Weyl functor using completed/affinized tensor products of the chosen quantum affine modules and the right action of the quiver-Hecke algebra.
- `source.tex:2952-2971`: Theorem that the modified functor preserves affinizations in the sense needed by the paper.

### Strong Hypothesis Layer

- `source.tex:3226-3249`: defines a strong duality datum and fixes the resulting duality functor
  $$
  \mathcal F_{\mathscr D}:R_{\mathsf C}\operatorname{-gmod}\to \mathcal C_{\mathfrak g}.
  $$
- `source.tex:3482-3485`: under a strong duality datum, the duality functor sends simple modules to simple modules.
- `source.tex:3505-3512`: the same strong setup gives faithfulness and begins the invariant-preservation theorem.
- `source.tex:3512-3522`: the invariant-preservation theorem records preservation/comparison of \(\Lambda\), \(\mathfrak d\), \(\Lambda^\infty\), weights, and dual shifts.
- `source.tex:3593-3612`: corollaries interpret \(\varepsilon_i,\varepsilon_i^*\) through quantum affine invariants and give an injective Grothendieck-ring map.

### Later Material Not For The First Page

- `source.tex:3730-3815`: affine cuspidal modules are defined after strong duality data. This is later PBW machinery, not first-page material.
- `source.tex:3817-3831`: affine cuspidal modules satisfy root-module, strongly-unmixed, normal-sequence, and simple-head properties.
- `source.tex:3856-3895`: type \(A_2^{(1)}\) example with Kirillov-Reshetikhin modules and affine cuspidal modules. This is a possible later paper-verified example, but it is too dense for the first definition-scope page.
- `source.tex:4402-4432`: Q-datum source path. The paper explains the subcategory \(\mathcal C_Q\), the associated duality datum, and the functor \(\mathcal F_Q\).
- `source.tex:4471-4495`: proposition collecting external results that Q-data give affine cuspidal modules and principal duality data.
- `source.tex:4527-4568`: PBW theory for \(\mathcal C^0\) using a complete duality datum begins here. This should be deferred to a later PBW/cuspidal-module topic.

## Proposed Topic Scope

If approved later, create a small child topic:

- id: `quantum-affine-schur-weyl-duality`
- title: `Quantum Affine Schur-Weyl Duality`
- parent topic: `quantum-affine-algebras`
- prerequisite topics:
  - `hernandez-leclerc-categories`
  - `quiver-hecke-module-categories`
  - `r-matrix-renormalization`
  - `affine-objects-in-monoidal-categories`
- related topics:
  - `monoidal-categorification`
  - `quiver-hecke-algebras`

The page should contain only:

- what categories are compared;
- what a duality datum supplies;
- how the duality functor is built at a high level;
- what improves when the duality datum is strong;
- why this is the bridge toward affine cuspidal modules and PBW theory.

The page should not yet contain:

- a full proof of the functor construction;
- the \(A_2^{(1)}\) affine cuspidal module example;
- complete duality data;
- reflections of duality data;
- PBW theorem statements;
- monoidal-categorification conclusions.

## Claim Budget For A Later Intake

If a later approved pass creates the topic page, keep the claim budget small:

1. duality datum and duality functor existence from `source.tex:2731-2747`;
2. modified functor construction and monoidal functor statement from `source.tex:2888-2948`;
3. preservation of affinizations from `source.tex:2952-2971`;
4. strong duality datum plus simple-to-simple/invariant-preservation theorem from `source.tex:3226-3249` and `3482-3522`.

Do not add a visible example unless the dense \(A_2^{(1)}\) example is separately approved for this advanced page.

## Remaining Gaps

- The reader needs a clearer prerequisite path through quiver-Hecke module categories and R-matrix invariants before this page can be comfortable.
- `Root modules` and `Strong Duality Data` could become small intermediate topics later, but they should not be split out unless the Schur-Weyl page becomes too dense.
- KKK18A and KP18 are primary sources for the original functor construction cited by KKOP24. They remain candidate-only unless separately approved.

## Recommended Next Step

Create only a small definition-scope child topic if the user approves new topic creation:

```text
Create a small definition-scope topic page `Quantum Affine Schur-Weyl Duality` under Quantum Affine Algebras using only KKOP24 source locations from reports/reviews/2026-06-03-quantum-affine-schur-weyl-source-path.md. Add at most 4 claims, do not download papers, do not add the A2 affine cuspidal example, and record prerequisite gaps instead of filling unsupported sections.
```
