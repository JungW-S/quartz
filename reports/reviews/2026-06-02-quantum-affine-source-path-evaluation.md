# Quantum Affine Source Path Evaluation

## Scope

This pass evaluates source options for the title-only topic `Quantum Affine Algebras`.

No paper was downloaded. No claim was added. No topic page was rewritten.

Files inspected:

- `content/topics/07-quantum-affine-algebras/quantum-affine-algebras.md`
- `data/source_candidates.yml`
- `data/sources.yml`
- `data/topic_maturity.yml`
- `inbox/papers2/KKOP24, PBW theory for quantum affine algebras, JEMS.pdf`
- `inbox/papers2/Tex/KKOP24, PBW theory for quantum affine algebras, JEMS/source.tex`
- `content/sources/books/hong-kang02-introduction-quantum-groups-crystal-bases.md`

## Verdict

The best immediate source path is:

1. Use already ingested Hong-Kang 2002 only as prerequisite background for ordinary quantum groups, root/weight notation, weight modules, and highest-weight representation language.
2. If the user approves a new intake, use the local KKOP24 paper `PBW theory for quantum affine algebras` only for its preliminary quantum-affine material.
3. Defer Chari-Pressley and Hernandez-Leclerc original sources until a later source-evaluation pass, because no local CP91/CP94/HL10 PDF was found by filename search.

This means the compact parent page should not be filled from memory and should not be filled from Hong-Kang alone. Hong-Kang supports the prerequisite quantum-group language, but the actual quantum-affine representation category, spectral parameters, fundamental representations, R-matrices, and Hernandez-Leclerc category route need a quantum-affine source.

## Local Source Found

### `kkop24-pbw-theory-quantum-affine-algebras`

Local files:

- PDF: `inbox/papers2/KKOP24, PBW theory for quantum affine algebras, JEMS.pdf`
- TeX: `inbox/papers2/Tex/KKOP24, PBW theory for quantum affine algebras, JEMS/source.tex`

PDF metadata reports 65 pages and keywords including `Hernandez-Leclerc category`, `Quantum affine algebra`, `Quiver Hecke algebra`, and `PBW theory`.

Useful source locations in the TeX:

- `source.tex:1360-1453`: quantum affine algebra setup, affine Cartan matrix, imaginary root, central element, classical weight lattice, definition of $U_q(\mathfrak g)$ for affine Cartan datum, the subalgebra $U_q'(\mathfrak g)$, the category $\mathscr C_{\mathfrak g}$ of finite-dimensional integrable $U_q'(\mathfrak g)$-modules, fundamental representations.
- `source.tex:1460-1629`: R-matrices on $U_q'(\mathfrak g)$-modules, affinizations, spectral parameter, normalized and renormalized R-matrices, basic head/socle facts.
- `source.tex:1641-1676`: Hernandez-Leclerc category $\mathscr C_{\mathfrak g}^0$ as a full subcategory generated from fundamental representations in a connected component of the spectral-parameter quiver.
- `source.tex:4979-5083`: bibliography entries for Akasaka-Kashiwara, Chari-Pressley, Hernandez-Leclerc, KKK/KKOP quantum-affine sources.

Recommended use:

- Use only the preliminaries to make a compact parent page.
- Do not import PBW theory, affine cuspidal modules, duality datum, or full monoidal categorification statements into the parent page.
- Later split detailed material into separate topics if needed: finite-dimensional integrable modules over $U_q'(\mathfrak g)$, spectral parameters and affinizations, quantum affine R-matrices, Hernandez-Leclerc categories, and quantum affine Schur-Weyl duality.

Risk:

- KKOP24 is mathematically aligned with the current KKOP/HL direction, but it is not a low-level textbook source.
- The first intake must be tightly scoped to avoid turning the parent page into a PBW-theory or monoidal-categorification page.
- CP91/CP94/HL10 are cited by KKOP24 and may be better canonical background for later details, but they were not locally available in this pass.

## Existing Approved Source

### Hong-Kang 2002

The already ingested Hong-Kang source supports:

- Cartan datum, roots, weights, Weyl group notation.
- Quantum group $U_q(\mathfrak g)$ for Kac-Moody background.
- Hopf algebra structure.
- Weight modules, highest-weight modules, characters, quantum category $\mathcal O^q$, and Verma modules.

Recommended use:

- Keep Hong-Kang as prerequisite support for links from the quantum-affine page back to `Quantum Groups`, `Weight Modules`, `Highest-Weight Modules`, and `Characters of Representations`.
- Do not use Hong-Kang alone as the source for quantum affine algebras unless a later source-location review verifies the affine-specific wording needed for the page.

## Not Found Locally

Filename search did not find local copies of:

- Chari-Pressley, `Quantum affine algebras`, Comm. Math. Phys. 142 (1991), 261-283.
- Chari-Pressley, `A Guide to Quantum Groups`, Cambridge University Press, 1994.
- Hernandez-Leclerc, `Cluster algebras and quantum affine algebras`, Duke Math. J. 154 (2010), 265-341.

These should remain candidates only. They should not be cited or used for claims until approved and ingested from a legitimate source or user-provided local file.

## Recommended Next Intake Scope

If approved, run a narrow local-source intake for `kkop24-pbw-theory-quantum-affine-algebras`.

Limit the intake to:

- source note creation;
- staging the already local PDF under `content/assets/pdfs/`;
- at most 6 claims;
- one compact parent-page update for `Quantum Affine Algebras`;
- no examples unless the paper contains a compact source-backed example that is directly appropriate for the parent page;
- no PBW-theory expansion;
- no Hernandez-Leclerc theorem expansion beyond orientation and links to future topics.

The parent page should aim for `definition-ready`, not `study-ready`.

## Proposed Child Topics For Later

Do not create these yet. They are useful later splits if the parent page becomes too dense:

- `Finite-Dimensional Quantum Affine Modules`
- `Spectral Parameters and Affinizations`
- `Quantum Affine R-Matrices`
- `Hernandez-Leclerc Categories`
- `Quantum Affine Schur-Weyl Duality`

## Result

The source path is clear enough for a next approved intake:

Use local KKOP24 preliminaries for the first compact `Quantum Affine Algebras` page, with Hong-Kang as prerequisite context. Treat CP91/CP94/HL10 as later candidate sources, not current citations.
