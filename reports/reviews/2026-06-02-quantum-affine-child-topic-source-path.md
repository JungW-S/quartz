# Quantum Affine Child-Topic Source Path

## Scope

Target parent topic:

- `content/topics/07-quantum-affine-algebras/quantum-affine-algebras.md`

Question:

- Which child topic should come first under `Quantum Affine Algebras`?
- Is the already ingested KKOP24 material enough, or should HL10 be approved first?

No paper was downloaded. No claim was added. No topic page was created or edited.

## Verdict

The first child topic should be:

- `Hernandez-Leclerc Categories`

Reason:

- It is the first category-level refinement already named in the parent page.
- It directly connects quantum affine representation categories to cluster algebra and monoidal categorification.
- It sits before more specialized topics such as quantum affine Schur-Weyl duality, strong duality data, affine cuspidal modules, and PBW theory for quantum affine algebras.

Existing KKOP24 material is enough for a report-only source path and for a very small definition skeleton, but not enough for a good reader-facing study article. Before creating the child page, approve HL10 for a source-location review.

## Candidate Child Topics

### 1. Hernandez-Leclerc Categories

Status: best first child topic.

Existing source support:

- KKOP24 Section 2.5, local TeX lines 1641-1676, defines:
  - the spectral-parameter quiver \(\sigma\);
  - the connected component \(\sigma_0\);
  - the full subcategory \(\mathcal C_{\mathfrak g}^0\);
  - closure under subquotients, extensions, and tensor products;
  - the fact that in symmetric affine types this category was introduced in HL10.
- KKOP24 introduction, local TeX lines 845-847, says Hernandez and Leclerc introduced a monoidal full subcategory \(\mathcal C^0\) and later \(\mathcal C_Q\)-type subcategories.
- KKOP24 local TeX lines 923-929 connect later interval categories and Grothendieck-ring statements back to HL10/HL15.

Limit:

- KKOP24 uses the Hernandez-Leclerc category as background for PBW theory and duality data. It does not give a low-level study exposition of why \(\mathcal C_{\mathfrak g}^0\) is the right cluster-theoretic category.
- It does not provide a compact first example suitable for a child page.
- It cites HL10 for the original construction and for Section 3.7/3.8-style details.

Decision:

- Approve HL10 for a narrow source-location review before creating the child page.
- Use KKOP24 as bridge/provenance support, not as the sole study source.

### 2. Quantum Affine Schur-Weyl Duality

Status: defer.

Reason:

- KKOP24 has substantial material on duality functors and duality data, but this is already more advanced than the first child page.
- A reader needs `Hernandez-Leclerc Categories` and quiver-Hecke module categories in place before this topic can read like a study article.

Decision:

- Do not create this as the first child topic.

### 3. Quantum-Affine R-Matrices

Status: defer.

Reason:

- The parent page already links to `Universal R-Matrix`, and the quiver-Hecke side already has `R-Matrix Renormalization`.
- A quantum-affine-specific R-matrix child page risks duplicating those pages unless its exact role is first scoped.
- It is useful later, but not the best first chapter step after the parent page.

Decision:

- Defer until Hernandez-Leclerc and/or quantum affine Schur-Weyl topics clarify what R-matrix facts are needed.

## HL10 Access Status

HL10 is available as an arXiv abstract page:

- arXiv:0903.1452
- Title: `Cluster algebras and quantum affine algebras`
- Authors: David Hernandez, Bernard Leclerc
- Journal reference: Duke Math. J. 154, no. 2 (2010), 265-341
- Related DOI: `10.1215/00127094-2010-040`

The arXiv abstract says it introduces monoidal subcategories \(\mathcal C_\ell\) of the category of finite-dimensional representations of a simply-laced quantum affine algebra and studies their Grothendieck rings using cluster algebras.

No PDF was downloaded in this pass.

## Validation

- `git diff --check` passed.
- YAML parsing passed for `data/source_candidates.yml`, `data/research_queue.yml`, `data/topic_maturity.yml`, and `data/review_backlog.yml`.
- `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 83 content files.
- Standalone `npx quartz build` failed with the known Node heap out-of-memory failure.

## Recommended Next Task

Approve HL10 for a narrow source-location review:

```text
I approve `hernandez-leclerc10-cluster-algebras-quantum-affine-algebras` for a source-location review using only the official arXiv version. Do not add claims, download/stage the PDF, or create a topic page yet. Report exact locations for the definition of the Hernandez-Leclerc category, the first cluster-algebra connection statement, and any compact example suitable for a future `Hernandez-Leclerc Categories` child topic.
```

After that review, create the child page only if exact source locations are adequate.
