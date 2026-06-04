# Quantum Cluster Rank-Two Example Verification

## Scope

This report records the verification basis for the rank-two quantum seed mutation example added to `Quantum Cluster Algebras` on 2026-06-02. No source was downloaded and no generated image was created.

## Example

### quantum-rank2-one-mutation

- Topic id: `quantum-cluster-algebras`
- Verification type: `Sage 계산`
- Sage script: `scripts/examples/cluster-algebras/quantum_rank2_one_mutation.sage`
- Sage command: `sage scripts/examples/cluster-algebras/quantum_rank2_one_mutation.sage`
- Page updated: `content/topics/04-cluster-algebras/quantum-cluster-algebras.md`
- Content verified: for
  $$
  B=
  \begin{pmatrix}
  0&1\\
  -1&0
  \end{pmatrix},
  \qquad
  L=
  \begin{pmatrix}
  0&-1\\
  1&0
  \end{pmatrix},
  $$
  the script checks $LB=I$, mutation in direction $1$, the mutated matrices
  $$
  L'=
  \begin{pmatrix}
  0&1\\
  -1&0
  \end{pmatrix},
  \qquad
  B'=
  \begin{pmatrix}
  0&-1\\
  1&0
  \end{pmatrix},
  $$
  the mutation exponents $a'=(-1,0)$, $a''=(-1,1)$, and the mutated commutation relation
  $$
  X_1'X_2=qX_2X_1'.
  $$
- Source support for the mutation definitions: KKKO14, Section 4.1, Section 4.2, and Definition 4.2, pp.27-29.
- Omitted details: no quantum exchange graph, quantum coordinate-ring example, or Berenstein-Zelevinsky-specific notation was added.
