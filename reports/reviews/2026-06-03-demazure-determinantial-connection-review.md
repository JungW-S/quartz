# Demazure Subcategory Determinantial-Module Connection Review

Date: 2026-06-03

Scope:
- Topic reviewed: `content/topics/06-quiver-hecke-klr-algebras/demazure-subcategories-of-quiver-hecke-modules.md`
- Related topic: `content/topics/06-quiver-hecke-klr-algebras/determinantial-modules.md`
- Source checked: Kashiwara-Nakashima 2025 `inbox/papers/crystal.tex`, especially lines 3196-3200.

No topic page, claim registry, source note, downloaded source, Sage code, image, or generated example was changed in this review.

## Source Facts

### Generalized determinantial modules

- `inbox/papers/crystal.tex:2586-2589` defines a weight `\lambda` to be `w`-dominant.
- `inbox/papers/crystal.tex:2591-2624` states the existence and uniqueness properties of
  $$
  \mathsf M_w(w\lambda,\lambda),
  $$
  and calls it a generalized determinantial module.
- `inbox/papers/crystal.tex:2620-2621` records the special case
  $$
  \mathsf M_w(w\Lambda,\Lambda)\simeq\mathsf M(w\Lambda,\Lambda)
  $$
  for dominant integral weights $\Lambda$.

### Membership in the Demazure subcategory

- `inbox/papers/crystal.tex:3102-3128` defines $\mathfrak B_w$ through the equivalent Demazure-side conditions on simple subquotients.
- `inbox/papers/crystal.tex:3196-3200` states:
  $$
  \mathsf M_w(w\lambda,\lambda)\in\mathfrak B_w
  $$
  for any `w`-dominant $\lambda$.

This is a valid source-backed connection from generalized determinantial modules to $\mathfrak B_w$.

## Decision

Do not add this as a visible `기본 예시`.

Reason: the source statement is a membership lemma, not a worked example. It does not compute a concrete module or show a low-rank calculation. Under the wiki example policy, it is better treated as a connection paragraph or a basic-property supplement, not as example content.

It is safe to add one connection paragraph to `Demazure Subcategories of Quiver-Hecke Modules`, preferably in `## 다른 topic들과의 관계`, if the user approves a topic edit.

The wording must distinguish three layers:

- $\mathsf M_w(w\lambda,\lambda)$: generalized determinantial module in KN25.
- $\mathsf M(w\Lambda,\Lambda)$: ordinary determinantial-module special case when $\Lambda$ is dominant integral.
- $M(w_{\le k}\Lambda,v_{\le k}\Lambda)$: the indexed $\mathcal C_{w,v}$ family used on the current `Determinantial Modules` page.

The edit should not identify these as the same family.

## Proposed Wording

Recommended location: add one bullet to `## 다른 topic들과의 관계` in `content/topics/06-quiver-hecke-klr-algebras/demazure-subcategories-of-quiver-hecke-modules.md`.

```markdown
- [[topics/06-quiver-hecke-klr-algebras/determinantial-modules|Determinantial Modules]]는 quiver-Hecke category 안의 distinguished simple modules를 설명한다. $w$-dominant $\lambda$에 붙은 generalized determinantial module $\mathsf M_w(w\lambda,\lambda)$는 $\mathfrak B_w$ 안에 놓이므로, determinantial-type objects는 localized category에서 invertible하게 쓰이는 것과 별도로 Demazure subcategory의 simple-object side에도 나타난다. 여기서 $\mathsf M_w(w\lambda,\lambda)$는 $\mathcal C_{w,v}$의 indexed family $M(w_{\le k}\Lambda,v_{\le k}\Lambda)$와 같은 notation layer가 아니므로 두 family를 동일시하지 않는다.
```

Recommended source-note addition if the paragraph is later applied:

```markdown
- Kashiwara-Nakashima 2025, lines 2586-2624 and 3196-3200: generalized determinantial modules $\mathsf M_w(w\lambda,\lambda)$ and their membership in $\mathfrak B_w$ for $w$-dominant $\lambda$.
```

## Not Recommended

Do not add a new example section from this source location.

Do not rewrite the `Determinantial Modules` page from this review alone. That page currently focuses on KKOP18 determinantial modules and the $\mathcal C_{w,v}$ indexed family. A broader generalized-determinantial-module subsection would need a separate approved source-backed edit.

Do not add a claim now. The current review only proposes a small reader-facing connection; a claim would be unnecessary unless the wiki later needs this membership lemma as reusable theorem-level infrastructure.

