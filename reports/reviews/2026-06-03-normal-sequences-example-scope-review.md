# Normal Sequences Example Scope Review

Date: 2026-06-03

## Scope

This report checks whether `content/topics/06-quiver-hecke-klr-algebras/normal-sequences.md` can receive a compact paper-verified normal-sequence example from the already approved sources:

- Kashiwara-Nakashima 2025, `inbox/papers/crystal.tex`;
- KKKO15, `content/assets/pdfs/kkko15-simplicity-heads-socles-tensor-products.pdf` and its local TeX file.

No topic page was edited. No claims were added. No sources were downloaded.

## Current Page State

The topic page is definition-ready and intentionally has no visible example. It already contains:

- the definition of almost affreal sequence;
- the definition of normal sequence via nonvanishing composed R-matrix;
- the head/socle consequence for almost affreal normal sequences;
- recursive and triple recognition criteria;
- the KKKO15 real-simple head/socle theorem as background.

The missing component is not theorem-level structure. The missing component is a concrete reader-facing example with named simple objects and a verified normality check.

## Source Locations Checked

### Kashiwara-Nakashima 2025

- `inbox/papers/crystal.tex:2396-2415`: Definition 4.8 defines almost affreal and normal sequence.
- `inbox/papers/crystal.tex:2417-2422`: Lemma 4.9 gives the simple image/head/socle consequence.
- `inbox/papers/crystal.tex:2425-2443`: Lemma 4.10 gives recursive normality tests using an affreal end term and a $\Lambda$ equality.
- `inbox/papers/crystal.tex:2445-2483`: Lemma 4.11 gives triple criteria involving commuting objects and duality.
- `inbox/papers/crystal.tex:2486-2490`: Proposition 4.12 gives a sufficient condition for triples in $R\text{-gmod}$ using $\widetilde\Lambda(L,N)=0$.
- `inbox/papers/crystal.tex:3484-3485`: uses a normal sequence inside a proof about subcategory membership. This is not a standalone example.
- `inbox/papers/crystal.tex:3830-3890`: proves a commuting lemma for $\widetilde Q_i$ objects and then uses normality to prove compatibility of localized operators. This belongs downstream.
- `inbox/papers/crystal.tex:4031-4039`: uses normality in a proof involving $\Delta$-type objects and $\langle i\rangle$. This is proof-level material, not a compact example.

### KKKO15

- Local TeX lines `757-880`: defines intertwiners, universal R-matrices, spectral parameters, and renormalized R-matrices for symmetric KLR algebras.
- Local TeX lines `1322-1347`: records real simple self-convolution criteria and simplicity of iterated powers.
- Local TeX lines `1386-1498`: proves head/socle and injectivity consequences for convolution with a real simple factor.
- Local TeX lines `1627-1665`: gives corollaries on simplicity and commuting for convolution with a real simple factor.
- The local TeX file does not use the term "normal sequence" in the KN25 sense and does not provide a compact normal-sequence example.

## Decision

Do not add a visible `기본 예시` to `Normal Sequences` from these sources now.

The nearest candidates are not suitable examples:

- Lemma 4.11 and Proposition 4.12 in KN25 are recognition criteria. They are already represented in `기본 성질`, and rewriting them as examples would blur theorem-level criteria with concrete examples.
- The normal-sequence occurrences in later KN25 proofs involve $\Delta$-type objects or localized objects such as $\widetilde Q_i$. They depend on downstream notation and would make the prerequisite page harder, not easier.
- KKKO15 supports the pair-level real-simple head/socle theorem but does not define or exemplify normal sequences.

The example section should remain omitted until a paper or Sage route gives a genuinely concrete low-rank normal-sequence calculation.

## Proposed Wording

No topic-page wording is recommended. Keep the visible example section omitted.

## Next Step

Move to the next dependency topic: review the quasi-rigid axiom source location and dependency role before using quasi-rigidity further in root-object exposition.
