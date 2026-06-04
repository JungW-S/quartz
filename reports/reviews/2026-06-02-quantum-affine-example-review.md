# Quantum Affine Example Review

## Scope

This report reviews only the already local KKOP24 TeX/PDF for a compact example suitable for:

- `content/topics/07-quantum-affine-algebras/quantum-affine-algebras.md`

No paper was downloaded. No claim was added. No topic page was edited. No child topic was created.

Local source inspected:

- `inbox/papers2/Tex/KKOP24, PBW theory for quantum affine algebras, JEMS/source.tex`
- `content/sources/papers/kkop24-pbw-theory-quantum-affine-algebras.md`
- `content/topics/07-quantum-affine-algebras/quantum-affine-algebras.md`

## Verdict

Do not add a visible example to the `Quantum Affine Algebras` parent page from KKOP24.

The source supports the definition-ready parent page, but it does not provide a compact undergraduate-facing first example of a quantum affine algebra or a finite-dimensional \(U_q'(\mathfrak g)\)-module in the preliminary sections. The actual examples in KKOP24 occur after additional machinery has been introduced, so using them as the first example would make the parent page less readable.

The page should remain `definition-ready` and `incomplete` because the verified example gap is real.

## Exact Source Locations Checked

### Preliminary Sections

- `source.tex:1360-1454`: affine Cartan setup, \(U_q(\mathfrak g)\), \(U_q'(\mathfrak g)\), \(\mathcal C_{\mathfrak g}\), dominant extremal weights, and fundamental representations.
- `source.tex:1465-1512`: affinizations, spectral parameter \(M_x\), universal and renormalized R-matrices.
- `source.tex:1641-1676`: spectral-parameter quiver \(\sigma(\mathfrak g)\) and the Hernandez-Leclerc category \(\mathcal C_{\mathfrak g}^0\).

These sections contain definitions and setup, but no concrete example environment.

### Example Environments In The Source

- `source.tex:2170-2173`: example that any fundamental module \(V(\varpi_i)_a\) is a root module, using denominators for fundamental modules.
- `source.tex:3856-3900`: affine type \(A_2^{(1)}\), a Hernandez-Leclerc category, Kirillov-Reshetikhin modules, a strong duality datum, and affine cuspidal modules for two reduced expressions.
- `source.tex:4237-4270`: reflection of the duality datum from the \(A_2^{(1)}\) example and resulting affine cuspidal modules.
- `source.tex:4514-4523`: Q-datum completeness comparison for the same \(A_2\) setup.
- `source.tex:4952-4967`: comparison between interval categories \(\mathcal C_{[a,b]}\) and Hernandez-Leclerc categories \(\mathcal C_l\).

## Suitability Assessment

### Rejected For Parent Page

The example at `source.tex:2170-2173` is too compressed for the parent page. It depends on:

- root modules;
- the invariant \(\Lambda(L,L)\);
- denominators of normalized R-matrices for fundamental modules;
- an external appendix in another KKOP source.

It is useful later for an R-matrix/root-module topic, but it is not a basic example of `Quantum Affine Algebras`.

The examples at `source.tex:3856-3900`, `4237-4270`, `4514-4523`, and `4952-4967` are also not suitable for the parent page. They depend on:

- Hernandez-Leclerc categories;
- Kirillov-Reshetikhin modules;
- duality data;
- quantum affine Schur-Weyl duality functors;
- affine cuspidal modules;
- reduced expressions and PBW theory.

These examples belong, if anywhere, in later specialized pages such as `Hernandez-Leclerc Categories`, `Quantum Affine R-Matrices`, or `Quantum Affine Schur-Weyl Duality`.

## Proposed Wording

No wording should be inserted into the parent topic page now.

If a future child topic on Hernandez-Leclerc categories is approved, the following source-backed advanced example may be considered there, not on the parent page:

```markdown
### 실제 예시: affine type \(A_2^{(1)}\)의 Hernandez-Leclerc category

KKOP24 Example 4.1 fixes \(U_q'(\mathfrak g)\) of affine type \(A_2^{(1)}\) and uses the connected component
$$
\sigma_0=\{(1,(-q)^{2k}),(2,(-q)^{2k+1})\mid k\in\mathbb Z\}.
$$
In that component, the fundamental modules \(V(1)\) and \(V(1)_{(-q)^2}\) form the initial duality datum used to compare quiver-Hecke modules with objects of \(\mathcal C_{\mathfrak g}^0\).

검증: 논문 예시
```

This proposed wording is intentionally marked as advanced-child-topic material. It should not be used as the first example for the `Quantum Affine Algebras` parent page.

## Recommended Next Step

Evaluate a lower-level source for a first example of a finite-dimensional quantum affine module, preferably before adding any visible example to the parent page.

Best candidates from the KKOP24 bibliography:

- Akasaka-Kashiwara, `Finite-dimensional representations of quantum affine algebras`, Publ. RIMS 33 (1997), 839-867.
- Chari-Pressley, `Quantum affine algebras`, Comm. Math. Phys. 142 (1991), no. 2, 261-283.
- Chari-Pressley, `A guide to quantum groups`, Cambridge University Press, 1994.

The next pass should first report legal access and exact example locations. It should not download, add claims, or edit the topic page until an exact source and example are approved.
