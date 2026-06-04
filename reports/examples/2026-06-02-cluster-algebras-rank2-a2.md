# Cluster Algebras Rank-Two Example Verification

## Scope

This report records the verification basis for the rank-two seed mutation example added to `Cluster Algebras` on 2026-06-02. No source was downloaded and no generated image was created.

## Example

### rank2-a2-one-mutation

- Topic id: `cluster-algebras`
- Verification type: `Sage 계산`
- Sage script: `scripts/examples/cluster-algebras/rank2_a2_one_mutation.sage`
- Sage command: `sage scripts/examples/cluster-algebras/rank2_a2_one_mutation.sage`
- Page updated: `content/topics/04-cluster-algebras/cluster-algebras.md`
- Content verified: for the rank-two exchange matrix
  $$
  B=
  \begin{pmatrix}
  0&1\\
  -1&0
  \end{pmatrix},
  $$
  mutation in direction \(1\) gives
  $$
  x_1'=\frac{1+x_2}{x_1},
  \qquad
  B'=
  \begin{pmatrix}
  0&-1\\
  1&0
  \end{pmatrix}.
  $$
- Source support for the mutation formula: KKKO14, Section 5.1, p.30.
- Omitted details: no exchange graph, cluster complex, or finite-type classification was added.
