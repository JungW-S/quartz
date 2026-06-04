# HL10 Type A3 Example Review

## Scope

Target topic:

- `content/topics/07-quantum-affine-algebras/hernandez-leclerc-categories.md`

Source:

- `content/assets/pdfs/hernandez-leclerc10-cluster-algebras-quantum-affine-algebras.pdf`

This was a report-only review. No topic page was edited. No claim was added. No source was downloaded.

## Verdict

HL10 Example 4.8 is useful, but it should not be imported in full.

Reason:

- The full example lists 12 prime simple objects, 14 clusters, dimensions, and one exchange relation.
- That is too dense for the first version of `Hernandez-Leclerc Categories`.
- The example becomes readable only if it is reduced to one point: in type \(A_3\), the conjectural \(\mathcal C_1\)-cluster correspondence turns cluster combinatorics into a finite list of prime simple objects and tensor-factorization patterns.

Recommended action:

- Do not replace the current \(\mathcal C_0\) basic example.
- If an advanced example is desired, add a short optional subsection after `기본 성질`, not inside the first `기본 예시`.
- Do not include the full 14-cluster list.

## Source Locations

- Sections 4.1.1-4.1.4, printed pp.10-11: define \(S(-\alpha_i)\), \(S(\alpha_i)\), \(S(\beta)\) for positive roots, and frozen objects \(F_i\).
- Example 4.1 and Example 4.2, printed p.11: fix the type \(A_3\) quiver and exchange matrix setup.
- Example 4.3 and Example 4.5, printed p.12: list the almost positive roots and polynomial formulas for the cluster variables.
- Conjecture 4.6 and Corollary 4.7, printed pp.12-13: state the \(\mathcal C_1\) monoidal-categorification conjecture and its consequences for prime simple objects and tensor products.
- Example 4.8, printed p.13: gives the type \(A_3\) list of prime simple objects, identifies the first six as fundamental representations and \(F_1,F_2,F_3\) as Kirillov-Reshetikhin modules, records the 14 clusters, and gives the exchange-relation tensor-product consequence.

## Proposed Compact Wording

If imported later, use a short advanced example like this:

```markdown
### 고급 예시: type \(A_3\)에서 \(\mathcal C_1\)

Type \(A_3\)에서 \(I_0=\{1,3\}\), \(I_1=\{2\}\)로 잡으면 \(\Phi_{\ge -1}\)는 세 negative simple roots와 여섯 positive roots로 이루어진다. HL10의 \(\mathcal C_1\) picture에서는 이 almost positive roots에 대응하는 objects
$$
S(\beta)\qquad(\beta\in\Phi_{\ge -1})
$$
와 frozen objects \(F_1,F_2,F_3\)가 prime simple objects의 finite list를 이룬다.

이 예시의 핵심은 cluster 하나가 tensor product를 허용하는 prime simple objects의 compatible family를 지정한다는 점이다. 예를 들어 exchange relation
$$
x[-\alpha_2]x[\alpha_2]=f_2+x[-\alpha_1]x[-\alpha_3]
$$
은 Grothendieck ring에서 \(S(-\alpha_2)\otimes S(\alpha_2)\)의 composition factors가 \(F_2\)와 \(S(-\alpha_1)\otimes S(-\alpha_3)\) 쪽으로 나타나는 현상을 보여 준다.

검증: 논문 예시
```

## What To Omit

Omit these parts from the topic page unless a later page is devoted to this example:

- the full 14-cluster list;
- the complete dimension list;
- the full polynomial formulas from Example 4.3 and Example 4.5;
- the statement that every simple object of \(\mathcal C_1\) is exactly one of the full tensor products over the 14 clusters, unless the page also explains compatible roots and cluster expansion.

## Mathematical Risk

The compact wording is safe only if it is explicitly marked as an advanced example. It depends on Conjecture 4.6 and Corollary 4.7, so the page must not present the \(\mathcal C_1\) comparison as a proved theorem for all types.

The type \(A_3\) case is later proved in type \(A_n\) in HL10, but importing that proof status would require a separate review of Section 10. For the current page, it is safer to keep the example tied to HL10's stated conjectural framework and Example 4.8.

## Decision

Best next step:

- Apply only the compact advanced example above if the page needs a more concrete \(\ell=1\) illustration.

Do not add the full Example 4.8 data to the topic page.

## Validation

- `git diff --check` passed.
- YAML parsing passed for `data/review_backlog.yml` and `data/research_queue.yml`.
- `python3 scripts/validate_topics.py`, `python3 scripts/validate_claims.py`, and `python3 scripts/validate_edges.py` passed.
- `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 85 content files.
- Standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
