# AK97 Quantum Affine Example Source-Location Review

## Scope

Approved source:

- Tatsuya Akasaka and Masaki Kashiwara, `Finite-Dimensional Representations of Quantum Affine Algebras`
- *Publications of the Research Institute for Mathematical Sciences* 33 (1997), no. 5, 839-867
- DOI: `10.2977/PRIMS/1195145020`
- Official EMS page: `https://ems.press/journals/prims/articles/3885`

Only the official EMS PDF was inspected. It was downloaded temporarily to `/tmp` for review and was not staged under `content/assets/pdfs/`.

No claim was added. No topic page was edited. No source note was created. No child topic was created.

Target page for a later approved edit:

- `content/topics/07-quantum-affine-algebras/quantum-affine-algebras.md`

## Verdict

AK97 can support a compact first example for `Quantum Affine Algebras`, but the safest visible example should be modest:

- use the family \(V(\varpi_i)_z\) of fundamental representations with spectral parameter as the object-level example;
- for a concrete type, use type \(A_{n-1}^{(1)}\) and \(V(\varpi_1)_z\);
- mention only the source-backed crystal labeling by singleton subsets if a visual cue is useful;
- do not import the R-matrix denominator formulas, pole computations, or type \(C_n^{(1)}\) appendix into the parent page.

This is enough to fill a short `기본 예시` section later, after a minimal source intake is approved.

## Exact Source Locations

### General spectral-parameter setup

- Introduction, p.839: finite-dimensional irreducible modules are organized through tensor products of fundamental representations \(V(\pi_i)_{a}\), where the \(a\)'s are spectral parameters.
- Section 1.2, p.843: for a \(U_q'(\mathfrak g)\)-module \(M\), the twist \(M_z\) is defined using the automorphism \(\varphi(z)\); it also records compatibility with tensor products.
- Section 1.3, pp.843-844: \(V(\pi_i)\) is introduced as the \(i\)-th fundamental representation, with uniqueness and global crystal base.
- Theorem 1.2, p.844: every finite-dimensional irreducible \(U_q'(\mathfrak g)\)-module over an algebraically closed field appears as the unique irreducible subquotient of a tensor product of \(V(\pi_i;z)\)'s containing the indicated extremal weight.

### R-matrix context

- Section 2, p.848: the normalized R-matrix between \(V(\pi_i)_x\otimes V(\pi_j)_y\) and \(V(\pi_j)_y\otimes V(\pi_i)_x\) is introduced, normalized on dominant extremal vectors, and treated as a rational function of spectral parameters.
- Corollary 2.4, p.850: poles of the normalized R-matrix are tied to reducibility of a two-factor tensor product.

Use these only as context in the parent page. They are too advanced for the first example.

### Concrete type \(A_{n-1}^{(1)}\) support

- Appendix B.1, pp.858-859: for type \(A_{n-1}^{(1)}\), the crystal basis \(B_k\) of the fundamental representation \(V(\pi_k)\), \(1\le k<n\), is labeled by \(k\)-element subsets of \(\mathbb Z/n\mathbb Z\), with explicit crystal operator rules.

For a compact parent-page example, specialize this only to \(k=1\). The visible statement should not reproduce the full operator rules unless a separate crystal-oriented example is approved.

## Proposed Wording For Later Approval

Do not insert this yet. It is proposed wording for a later minimal intake/edit pass.

```markdown
## 기본 예시

### 실제 예시: type \(A_{n-1}^{(1)}\)의 \(V(\varpi_1)_z\)

Affine type \(A_{n-1}^{(1)}\)에서 \(V(\varpi_1)\)은 fundamental representation의 한 예이다. Spectral parameter \(z\in\Bbbk^\times\)를 넣으면 같은 vector space 위에 action을 twist한 \(U_q'(\mathfrak g)\)-module
$$
V(\varpi_1)_z
$$
를 얻는다.

이 예시는 quantum affine algebra에서 spectral parameter가 어떻게 나타나는지를 보여 준다. Algebra \(U_q'(\mathfrak g)\)는 같지만, parameter \(z\)가 module structure에 들어가면서 \(V(\varpi_1)_z\)들이 하나의 parameter family를 이룬다. Akasaka-Kashiwara의 type \(A_{n-1}^{(1)}\) description에 따르면 \(V(\varpi_k)\)의 crystal basis는 \(k\)-element subsets of \(\mathbb Z/n\mathbb Z\)로 labeled된다. 따라서 \(k=1\)에서는 singleton subsets가 \(V(\varpi_1)\)의 crystal-level labels가 된다.

검증: 논문 예시
```

## Why This Is Safe

- The example stays at object-level and category-level: a concrete finite-dimensional module \(V(\varpi_1)_z\) inside the quantum affine module category.
- It uses the source's own fundamental-representation notation and spectral-parameter construction.
- It avoids theorem-level claims about classification, tensor-product irreducibility, and R-matrix poles in the visible example.
- It does not require creating a separate child topic before the parent page gets a first example.

## What Not To Add Yet

- Do not add the full Theorem 1.2 classification/subquotient statement to the example section.
- Do not add Corollary 2.4 or R-matrix pole-reducibility statements to the example section.
- Do not add Appendix C type \(C_n^{(1)}\) formulas.
- Do not copy the full Appendix B crystal operator rules unless a later crystal-oriented example pass is approved.

## Recommended Next Edit

Run a minimal approved AK97 intake:

1. stage the official EMS PDF under `content/assets/pdfs/`;
2. create a concise source note under `content/sources/papers/`;
3. add AK97 to `data/sources.yml`;
4. add at most one reusable claim for the \(V(\varpi_i)_z\) fundamental-representation family and type \(A_{n-1}^{(1)}\) crystal-label example;
5. insert only the proposed `기본 예시` into `Quantum Affine Algebras`;
6. update topic maturity from `definition-ready` to `example-ready` only if the example is inserted.

## Validation

- `git diff --check`: passed.
- YAML parsing for the touched registries: passed.
- `python3 scripts/run_all_checks.py`: passed, including validators, generated maps/status, link validation, and its internal Quartz build over 82 content files.
- Standalone `npx quartz build`: failed with the known Node heap out-of-memory failure.

## Follow-Up Intake

The minimal AK97 intake was completed later on 2026-06-02. The official EMS PDF was staged, a concise source note was created, one claim was added, and only the type \(A_{n-1}^{(1)}\) fundamental-representation example was inserted into `Quantum Affine Algebras`.
