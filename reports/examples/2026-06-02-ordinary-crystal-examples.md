# Ordinary Crystal Examples Verification

## Scope

This report records the verification basis for the ordinary crystal examples added on 2026-06-02. No source was downloaded, no Sage computation was used, and no generated image was created.

## Examples

### tensor-products-one-element-crystal

- Topic id: `tensor-products-of-crystals`
- Verification type: `논문 예시`
- Source: Kashiwara 1993, Example 1.3.2, p.845.
- Page updated: `content/topics/02-crystal-bases/tensor-products-of-crystals.md`
- Content verified: tensor products \(b\otimes t_\lambda\) and \(t_\lambda\otimes b\), including the weight, \(\varepsilon_i\), and \(\varphi_i\) formulas.

### b-infinity-a2-coordinate-model

- Topic id: `b-infinity-crystal`
- Verification type: `논문 예시`
- Source: Kashiwara 1993, Example 2.2.5, p.850.
- Page updated: `content/topics/02-crystal-bases/b-infinity-crystal.md`
- Content verified: type \(A_2\) full embedding \(B(\infty)\hookrightarrow B_1\otimes B_2\otimes B_1\), image condition \(0\le n\le m,\ 0\le \ell\), and \(u_\infty\mapsto b_1\otimes b_2\otimes b_1\).
- Omitted details: type \(B_2\) and \(G_2\) coordinate models from Examples 2.2.6-2.2.7 remain omitted because they are too large for the first \(B(\infty)\) example.

### demazure-simple-reflection

- Topic id: `demazure-crystals`
- Verification type: `논문 예시`
- Source: Kashiwara 1993, Propositions 3.2.3 and 3.2.5, pp.854-855, specialized to \(w=s_i\).
- Page updated: `content/topics/02-crystal-bases/demazure-crystals.md`
- Content verified: the simple-reflection cases \(B_{s_i}(\infty)=\{\widetilde f_i^k u_\infty\mid k\ge0,\ \widetilde f_i^k u_\infty\ne0\}\) and \(B_{s_i}(\lambda)=\{\widetilde f_i^k u_\lambda\mid k\ge0,\ \widetilde f_i^k u_\lambda\ne0\}\).
- Omitted details: no non-simple Weyl group element example was added.
