# Book-Like Readability Check

## Scope

This report checks whether the current topic wiki reads like a study book rather than a registry of pages. No paper was downloaded, no claim was added, and no topic page was rewritten in this pass.

Files inspected:

- `content/topics/03-category-theory/index.md`
- `content/topics/03-category-theory/category-theory.md`
- `content/topics/03-category-theory/pro-categories.md`
- `content/topics/03-category-theory/graded-monoidal-categories.md`
- `content/topics/02-crystal-bases/index.md`
- `content/topics/02-crystal-bases/crystal-bases.md`
- `content/topics/02-crystal-bases/abstract-crystals.md`
- `content/topics/04-cluster-algebras/index.md`
- `content/topics/04-cluster-algebras/cluster-algebras.md`
- `content/topics/04-cluster-algebras/quantum-cluster-algebras.md`
- `content/topics/08-localization-of-categories/category-localization.md`

## Verdict

The wiki is not yet fully book-like.

Some individual pages now read like compact study articles, especially `Cluster Algebras`, `Quantum Cluster Algebras`, `Abstract Crystals`, and several crystal prerequisite pages. They have learning-order sections, definitions before examples, verified examples, relation explanations, and final source notes.

The larger reading experience still has two major weaknesses:

1. Chapter landing pages are mostly lists, not chapter introductions.
2. `Category Theory` is still title-only, while later pages already use functors, Yoneda, pro-objects, monoidal categories, duals, exactness, and universal properties.

So the current state is closer to a well-organized course notebook than a finished textbook chapter sequence.

## Strong Parts

### Crystal Bases chapter

The sequence

```text
Crystal Bases
Abstract Crystals
Tensor Products of Crystals
Highest Weight Crystals
The Crystal B(infinity)
Demazure Crystals
Cellular Crystals
```

is mathematically sensible. The pages now separate ordinary crystal language from cellular/localized comparison. `Abstract Crystals` is especially readable: it introduces symbols, states the axioms clearly, gives paper-verified examples, and explains graph intuition.

Remaining readability issue:

- `Crystal Bases` and `Abstract Crystals` still overlap. The parent page repeats enough of the abstract-crystal definition that a reader may feel they are reading the same definition twice. For a book-like chapter, `Crystal Bases` should become more of an overview and motivation page, while `Abstract Crystals` should carry the full axiom list.

### Cluster Algebra shelf

`Cluster Algebras` is compact and readable. It correctly keeps seed, mutation, cluster variables, and cluster monomials together rather than over-splitting them. The Sage-verified rank-two example is placed at the right point.

`Quantum Cluster Algebras` is also logically ordered: classical seed first, then quantum torus notation, compatible pair, quantum seed, mutation, and a Sage-verified rank-two quantum example.

Remaining readability issue:

- The shelf page `content/topics/04-cluster-algebras/index.md` is still just a short list. A book chapter needs a short preface explaining what changes from classical to quantum and why the reader should next go to monoidal categorification.

## Weak Parts

### Category Theory shelf

This is the largest readability blocker. `Category Theory` is still a title-only page, but `Pro-Categories` starts with Yoneda-style embedding language and `Graded Monoidal Categories` starts from a finite-length graded monoidal setting.

That is mathematically honest for the later papers, but not book-like for an undergraduate reader. A book would first explain:

- what a category is;
- what objects and morphisms are;
- what composition and identity mean;
- what functors do;
- what natural transformations compare;
- why universal properties are a useful way to define objects.

Only after that should it send the reader to pro-categories, monoidal categories, and localization.

### Chapter landing pages

The large shelf pages are not yet real chapter pages. They mostly say one sentence and then list links. This is useful navigation, but it does not yet function like a table of contents in a textbook.

A better chapter landing page should include:

- what the chapter is for;
- what the reader should already know;
- the recommended reading order;
- one sentence per subtopic explaining why it comes next;
- what is intentionally not covered yet.

This can be done without adding mathematical claims.

### Reader-facing wording

Several pages still use phrases such as `이 page` or English labels such as `Definition-level fact`, `Theorem-level fact`, and `Categorification viewpoint` in the main exposition. This is not mathematically wrong, but it feels like internal authoring language.

For book-like prose, these should be changed to Korean reader-facing labels such as:

- `정의에서 바로 따라오는 사실`
- `정리 수준의 사실`
- `categorification 관점`
- `coordinate-ring 관점`

This is a polish task, not a source-intake task.

## Priority Fixes

1. Fill `Category Theory` from an approved low-level source.
   - Best candidate: `leinster14-basic-category-theory`.
   - This is the only fix here that needs new source intake.

2. Rewrite chapter landing pages as reading guides.
   - Start with `Category Theory`, `Crystal Bases`, and `Cluster Algebras`.
   - No mathematical claims need to be added.

3. Reduce duplication between `Crystal Bases` and `Abstract Crystals`.
   - Keep the full axiom list in `Abstract Crystals`.
   - Make `Crystal Bases` explain why the axiom package exists and how the chapter unfolds.

4. Polish reader-facing labels.
   - Replace internal English labels in main exposition where they make the page feel like notes rather than a study article.

## Answer To The User's Question

Not yet.

The current wiki is much better organized than before, and several individual pages are already readable as study articles. But the whole site does not yet read like a book because the chapter introductions are too list-like and the basic category-theory entry point is still missing.

The safest next step is to approve Leinster for a narrow `Category Theory` intake, then do a no-new-claims polish pass on the chapter landing pages.
