# Crystal Bases sl2 Example Support Review

Date: 2026-06-01

## Scope

This report checks whether Hong-Kang 2002 supports a compact `Crystal Bases` example using finite-dimensional $U_q(\mathfrak{sl}_2)$-modules.

No topic page was rewritten. No claims were added. No sources were downloaded. No Sage code or images were generated.

## Sources Checked

- Staged source PDF: `content/assets/pdfs/hong-kang02-introduction-quantum-groups-crystal-bases.pdf`
- Source note: `content/sources/books/hong-kang02-introduction-quantum-groups-crystal-bases.md`
- Current topic page: `content/topics/crystal-bases.md`
- Prior bridge report: `reports/reviews/2026-06-01-quantum-groups-sl2-example-support.md`

The PDF is a scan, so the relevant pages were checked from rendered page images.

## Decision

Hong-Kang 2002 supports a real source-backed example suitable for the `Crystal Bases` page.

The best source route is:

- Hong-Kang 2002, Chapter 4, Section 4.2, Example 4.2.6, pp.68-69.
- Hong-Kang 2002, Chapter 4, Section 4.3, p.73.

Example 4.2.6 defines the $(m+1)$-dimensional irreducible $U_q(\mathfrak{sl}_2)$-module $V(m)$, its crystal lattice $\mathcal L(m)$, its crystal basis $\mathcal B(m)$, and the finite line crystal graph. Section 4.3 then reuses the same $\mathcal L(m)$ and $\mathcal B(m)$ to study finite-dimensional $U_q(\mathfrak{sl}_2)$-modules and records the weight, $\varepsilon$, and $\varphi$ values on the vertices.

The example can later receive the visible verification label `검증: 논문 예시`.

## Supported Mathematical Content

The source supports the following compact example content:

- For $m\in\mathbb Z_{\ge 0}$, $V(m)$ is the $(m+1)$-dimensional irreducible $U_q(\mathfrak{sl}_2)$-module with highest weight vector $u$.
- The crystal lattice and crystal basis are
  $$
  \mathcal L(m)=\bigoplus_{k=0}^m A_0 f^{(k)}u,
  \qquad
  \mathcal B(m)=\{\overline u,\overline{fu},\ldots,\overline{f^{(m)}u}\}.
  $$
- The crystal graph is the finite line
  $$
  \overline u\longrightarrow \overline{fu}\longrightarrow \overline{f^{(2)}u}
  \longrightarrow\cdots\longrightarrow \overline{f^{(m)}u}.
  $$
- On the vertex $\overline{f^{(k)}u}$, Section 4.3 records
  $$
  \operatorname{wt}(\overline{f^{(k)}u})=m-2k,\qquad
  \varepsilon(\overline{f^{(k)}u})=k,\qquad
  \varphi(\overline{f^{(k)}u})=m-k.
  $$

This is mathematically distinct from the current elementary-crystal example on `Crystal Bases`: $B_i$ is an infinite elementary crystal, while $\mathcal B(m)$ is a finite string coming from an actual finite-dimensional $U_q(\mathfrak{sl}_2)$-module.

## Proposed Later Topic Wording

If the user approves a topic-page edit, add a second real example after the existing $T_\lambda$ and $B_i$ example in `content/topics/crystal-bases.md`:

```markdown
### $U_q(\mathfrak{sl}_2)$의 finite string crystal

$m\in\mathbb Z_{\ge 0}$에 대해 $V(m)$을 highest weight $m$을 갖는 $(m+1)$-dimensional irreducible $U_q(\mathfrak{sl}_2)$-module이라고 하자. Highest weight vector를 $u$라고 쓰면 Hong-Kang의 Example 4.2.6은
$$
\mathcal L(m)=\bigoplus_{k=0}^m A_0 f^{(k)}u,
\qquad
\mathcal B(m)=\{\overline u,\overline{fu},\ldots,\overline{f^{(m)}u}\}
$$
를 crystal basis로 둔다.

이 crystal graph는 finite line이다.
$$
\overline u\longrightarrow \overline{fu}\longrightarrow
\overline{f^{(2)}u}\longrightarrow\cdots\longrightarrow
\overline{f^{(m)}u}.
$$

Section 4.3에서는 각 vertex에 대해
$$
\operatorname{wt}(\overline{f^{(k)}u})=m-2k,\qquad
\varepsilon(\overline{f^{(k)}u})=k,\qquad
\varphi(\overline{f^{(k)}u})=m-k
$$
가 된다고 기록한다. 따라서 $\varepsilon$는 왼쪽으로 얼마나 올라갈 수 있는지, $\varphi$는 오른쪽으로 얼마나 내려갈 수 있는지를 세는 함수로 보인다.

검증: 논문 예시
```

Add final `Source notes` lines at the same time:

```markdown
- Hong-Kang 2002, Example 4.2.6, pp.68-69: the finite-dimensional $U_q(\mathfrak{sl}_2)$ module $V(m)$, the lattice $\mathcal L(m)$, the crystal basis $\mathcal B(m)$, and the finite line graph.
- Hong-Kang 2002, Section 4.3, p.73: the weight, $\varepsilon$, and $\varphi$ values on $\mathcal B(m)$.
```

## Recommendation

The source support is sufficient. The next safe task is a small topic-page edit that adds only this example and the matching source-note lines.

Do not replace the current Kashiwara 1993 examples. Add this as a representation-origin example, because it explains how a finite crystal string arises from a finite-dimensional $U_q(\mathfrak{sl}_2)$-module.

Do not import Theorems 4.3.1-4.3.2 or the uniqueness proof in this example pass.

## Validation

- `git diff --check` passed.
- `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 52 content files.
- Standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
