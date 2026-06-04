# Quantum Groups sl2 Example Support Review

Date: 2026-06-01

## Scope

This report checks whether Hong-Kang 2002 supports a compact source-location-specific $U_q(\mathfrak{sl}_2)$ example for `content/topics/01-quantum-groups/quantum-groups.md`.

No topic page was rewritten. No claims were added. No sources were downloaded. No Sage code or images were generated.

## Sources Checked

- Staged source PDF: `content/assets/pdfs/hong-kang02-introduction-quantum-groups-crystal-bases.pdf`
- Source note: `content/sources/books/hong-kang02-introduction-quantum-groups-crystal-bases.md`
- Current topic page: `content/topics/01-quantum-groups/quantum-groups.md`

The PDF is a scan, so `pdftotext` produced no usable text. The exact pages below were checked from rendered page images.

## Decision

Hong-Kang 2002 does support a compact real example for the `Quantum Groups` page.

The best source location is:

- Hong-Kang 2002, Chapter 4, Section 4.2, Example 4.2.1, p.66.

This example explicitly presents the quantum group $U_q(\mathfrak{sl}_2)=\langle e,f,K^{\pm1}\rangle$, its two-dimensional natural representation
$$
V=\mathbb F(q)v_+\oplus \mathbb F(q)v_-,
$$
and the actions of $e$, $f$, and $K$ on $v_+$ and $v_-$.

The example can later receive the visible verification label `검증: 논문 예시` under the current example policy, even though the approved source is a book rather than a paper.

## Supporting Locations

- Hong-Kang 2002, Chapter 3, Section 3.1, Definition 3.1.1, pp.37-38: general definition of $U_q(\mathfrak g)$ by generators $e_i$, $f_i$, and $q^h$ with Cartan, raising/lowering, and quantum Serre relations.
- Hong-Kang 2002, Chapter 3, Section 3.1, Proposition 3.1.2, p.39: Hopf-algebra structure on $U_q(\mathfrak g)$.
- Hong-Kang 2002, Chapter 4, Section 4.2, Example 4.2.1, p.66: direct $U_q(\mathfrak{sl}_2)$ example with a two-dimensional representation.
- Hong-Kang 2002, Chapter 4, Section 4.3, p.73: finite-dimensional irreducible $U_q(\mathfrak{sl}_2)$-modules $V(m)$ and their crystal bases, useful for connecting the example to the next `Crystal Bases` topic.

## Proposed Later Topic Wording

If the user approves a topic-page edit, add a compact `## 기본 예시` section to `content/topics/01-quantum-groups/quantum-groups.md` along these lines:

```markdown
## 기본 예시

### $U_q(\mathfrak{sl}_2)$와 2차원 natural representation

Hong-Kang의 Example 4.2.1에서는
$$
U_q(\mathfrak{sl}_2)=\langle e,f,K^{\pm1}\rangle
$$
와 2차원 module
$$
V=\mathbb F(q)v_+\oplus \mathbb F(q)v_-
$$
를 사용한다. 작용은
$$
e v_+=0,\qquad e v_-=v_+,
$$
$$
f v_+=v_-,\qquad f v_-=0,
$$
$$
K v_+=qv_+,\qquad K v_-=q^{-1}v_-.
$$

이 예시는 $e$가 weight를 올리고 $f$가 weight를 내리며 $K$가 weight를 기록한다는 가장 작은 quantum-group representation이다. Tensor product $V\otimes V$에서는 obvious tensor basis가 irreducible decomposition과 바로 맞지 않기 때문에, 이후의 crystal-basis theory가 필요한 이유가 보인다.

검증: 논문 예시
```

Add a final `Source notes` line at the same time:

```markdown
- Hong-Kang 2002, Example 4.2.1, p.66: the $U_q(\mathfrak{sl}_2)$ two-dimensional natural representation used in the basic example.
```

## Recommendation

The source support is sufficient. The next safe task is a small topic-page edit that adds only this example and the matching source-note line.

Do not add new claims. Do not broaden the example into a full section on all $U_q(\mathfrak{sl}_2)$ representations. If more representation detail is needed later, use Chapter 4, Section 4.3 separately.

## Validation

- `git diff --check` passed.
- `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 52 content files.
- Standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
