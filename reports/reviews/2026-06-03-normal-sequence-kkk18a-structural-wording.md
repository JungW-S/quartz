# Normal Sequence KKK18A Structural Wording Review

Date: 2026-06-03

## Scope

This report drafts possible wording for a clearly labeled `구조 예시` on `Normal Sequences`, based only on Kang-Kashiwara-Kim 2018 Proposition 4.2.7.

No topic page was edited. No claim, source note, paper download, Sage code, image, or generated example was added.

## Source Basis

Already staged source:

- `content/assets/pdfs/kang-kashiwara-kim18-symmetric-quiver-hecke-algebras-r-matrices.pdf`
- `content/sources/papers/kang-kashiwara-kim18-symmetric-quiver-hecke-algebras-r-matrices.md`

Source locations:

- KKK18A Section 4.2, arXiv PDF p.36: type \(A\) segment modules \(L(a,b)\).
- KKK18A Proposition 4.2.5, arXiv PDF p.39: ordered multisegment classification by heads of ordered segment-module convolutions.
- KKK18A Lemma 4.2.6, arXiv PDF pp.39-41: ordered convolution head and reversed convolution socle comparison.
- KKK18A Proposition 4.2.7, arXiv PDF p.43: for a simple module \(M\) with associated ordered multisegment, the composed R-matrix
  \[
  r:=r_{L_1,\ldots,L_t}:L_1\circ\cdots\circ L_t\to q^d L_t\circ\cdots\circ L_1
  \]
  has \(M\simeq\operatorname{Im}(r)\); the proof says \(r\) does not vanish.

## Mathematical Caveats

This is not a low-rank worked calculation. It is a theorem-family structural example.

KKK18A does not present Proposition 4.2.7 using the exact `Normal Sequences` terminology of Kashiwara-Nakashima 2025. Therefore the wording should say that it shows the key mechanism behind a normal-sequence condition, not that KKK18A labels this family as a normal sequence.

The wording should also not invoke the almost-affreal head/socle theorem from KN25 Lemma 4.9. KKK18A has its own head/socle comparison through Lemma 4.2.6 and Proposition 4.2.7.

## Proposed Topic-Page Wording

If approved, insert this under `## 기본 예시` in `content/topics/06-quiver-hecke-klr-algebras/normal-sequences.md`.

```markdown
### 구조 예시: ordered multisegment에서 나오는 composed R-matrix

Type $A$ quiver-Hecke category에서 segment module $L(a,b)$들을 생각하자. Ordered multisegment
$$
(a_1,b_1)\ge \cdots \ge (a_t,b_t)
$$
가 simple module $M$에 대응한다고 하자. 각 $k$에 대해
$$
L_k=L(a_k,b_k)
$$
로 놓으면, KKK18A Proposition 4.2.7은 composed R-matrix
$$
r_{L_1,\ldots,L_t}:
L_1\circ\cdots\circ L_t
\longrightarrow
q^d L_t\circ\cdots\circ L_1
$$
의 image가 $M$과 isomorphic임을 말한다. 특히 이 composed R-matrix는 $0$이 아니다.

이 예시는 normal sequence 정의에서 중요한 조건이 실제로 어떤 모습인지 보여 준다. Pairwise R-matrix들을 합성해 convolution product의 순서를 뒤집고, 그 image가 ordered product에서 나오는 simple object를 잡는다. Segment module과 ordered multisegment의 정의는 [[topics/06-quiver-hecke-klr-algebras/type-a-klr-segment-modules|Type A KLR Segment Modules]]에서 읽고, 두 segment의 R-matrix behavior는 [[topics/06-quiver-hecke-klr-algebras/type-a-segment-module-convolutions|Type A Segment Module Convolutions]]에서 읽는다.

검증: KKK18A Proposition 4.2.7, together with Lemma 4.2.6.
```

## Proposed Source Notes Addition

If the example is later inserted, add one final source-note bullet:

```markdown
- [[sources/papers/kang-kashiwara-kim18-symmetric-quiver-hecke-algebras-r-matrices|Kang-Kashiwara-Kim 2018]], Lemma 4.2.6 and Proposition 4.2.7, arXiv PDF pp.39-43: ordered segment-module convolutions, reversed convolution socles, and nonvanishing composed R-matrix image for the simple module attached to an ordered multisegment.
```

## Do Not Add

Do not call this a low-rank example.

Do not say that KKK18A itself calls the ordered multisegment sequence a normal sequence.

Do not use this wording to prove the KN25 almost-affreal normal-sequence theorem.

Do not add new claims or a new source note solely for this wording unless the topic page edit is explicitly approved.

## Recommendation

The wording is safe as a `구조 예시` if the user accepts a theorem-family example. It should move `Normal Sequences` from `definition-ready` toward `example-ready`, but not all the way to `study-ready`.

If the user insists on a low-rank paper/Sage calculation, keep the example section omitted.
