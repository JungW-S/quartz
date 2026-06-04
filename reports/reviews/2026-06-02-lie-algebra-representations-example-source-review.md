# Lie Algebra Representations Example Source Review

Date: 2026-06-02

## Scope

This report checks Hong-Kang 2002 Chapter 1 for a compact real example suitable for `content/topics/01-quantum-groups/lie-algebra-representations.md`.

No source was downloaded. No claim was added. No topic page was edited.

## Source Checked

Local PDF:

`content/assets/pdfs/hong-kang02-introduction-quantum-groups-crystal-bases.pdf`

The PDF is an image scan, so text search does not work. The relevant pages were checked from rendered local PDF pages 23-24, corresponding to printed pp.3-4.

## Relevant Source Locations

### Definition 1.2.1

Hong-Kang 2002, Chapter 1, Definition 1.2.1, printed p.3 supports the current definition page:

- a representation of a Lie algebra \(L\) on a vector space \(V\) as a Lie algebra homomorphism
  $$
  L\to\mathfrak{gl}(V),
  $$
- an \(L\)-module as a vector space with compatible bilinear action
  $$
  L\times V\to V.
  $$

### Example 1.2.2(1)

Hong-Kang 2002, Chapter 1, Example 1.2.2(1), printed p.4 gives the best compact example:

- take
  $$
  L=\mathfrak{gl}(n,\mathbb F),
  \qquad
  V=\mathbb F^n,
  $$
- define the action by matrix multiplication
  $$
  (x,v)\longmapsto xv,
  $$
- then \(V\) is an \(L\)-module,
- this representation is called the vector representation or natural representation of \(\mathfrak{gl}(n,\mathbb F)\).

This is the safest first example for the topic page because it directly matches the definition: a Lie algebra element is realized as a linear operator on a vector space.

### Example 1.2.2(2)

Hong-Kang 2002, Chapter 1, Example 1.2.2(2), printed p.4 gives a second candidate:

- for any Lie algebra \(L\), define
  $$
  \operatorname{ad}:L\to\mathfrak{gl}(L),
  \qquad
  \operatorname{ad}x(y)=[x,y],
  $$
- then \(\operatorname{ad}\) is a Lie algebra homomorphism,
- this is the adjoint representation of \(L\).

This is useful but should be secondary on the first prerequisite page because it uses the Lie bracket itself as the action and is less concrete than matrix multiplication.

## Recommendation

Use Example 1.2.2(1) as the visible `기본 예시` for `Lie Algebra Representations`.

Keep the example compact:

- do not introduce classification of representations,
- do not discuss irreducibility,
- do not add weight spaces,
- do not use this example to expand universal enveloping algebras.

Example 1.2.2(2), the adjoint representation, can be mentioned later as an optional second example or in `기본 성질`, but it should not be the first visible example.

## Proposed Later Topic Wording

If approved for a topic-page edit, add only this compact example:

```markdown
## 기본 예시

### 실제 예시: natural representation of \(\mathfrak{gl}(n,\mathbb F)\)

\(L=\mathfrak{gl}(n,\mathbb F)\)이고 \(V=\mathbb F^n\)이라고 하자. Hong-Kang Example 1.2.2(1)은 \(L\)이 \(V\) 위에 matrix multiplication으로 작용한다고 둔다.
$$
(x,v)\longmapsto xv.
$$

따라서 각 \(x\in\mathfrak{gl}(n,\mathbb F)\)는 \(V\) 위의 linear operator로 작용하고, representation map은
$$
\rho:\mathfrak{gl}(n,\mathbb F)\longrightarrow\mathfrak{gl}(V),
\qquad
\rho(x)(v)=xv
$$
로 볼 수 있다. 이 representation은 \(\mathfrak{gl}(n,\mathbb F)\)의 vector representation 또는 natural representation이다.

검증: 논문 예시
```

Add this source-note line at the same time:

```markdown
- Hong-Kang 2002, Chapter 1, Example 1.2.2(1), p.4: the natural representation of \(\mathfrak{gl}(n,\mathbb F)\) on \(V=\mathbb F^n\) by matrix multiplication.
```

## Validation

- `git diff --check` passed.
- `npx tsc --noEmit` passed.
- `python3 scripts/run_all_checks.py` passed, including generated maps, topic status, link validation, and its internal Quartz build over 80 content files.
- Standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
