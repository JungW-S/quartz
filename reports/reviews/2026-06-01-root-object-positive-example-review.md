# Root Object Positive Example Review

Date: 2026-06-01

## Scope

This report checks whether `content/topics/root-objects-in-localized-categories.md` can receive a positive source-backed example of a root object.

Only `inbox/papers/crystal.tex` from Kashiwara-Nakashima 2025 was checked. No topic page was edited. No claim was added. No source was downloaded.

## Decision

The page can receive a small conditional positive example, but not a clean low-rank standalone example from the checked source.

Safe conclusion:

- Kashiwara-Nakashima 2025 explicitly uses a situation in which the localized simple-root object
  $$
  \widetilde Q_i=Q_w(\langle i\rangle)
  $$
  is a root object.
- The usable condition is the positive-interaction branch where a simple object $X\in\widetilde{\mathcal C}_w$ satisfies
  $$
  \mathsf d_i(X)>0.
  $$
- This should be presented as a conditional example, not as a blanket statement that every $\widetilde Q_i$ is a root object.

Do not present the type $A_3$ remark as a positive example. That remark is a warning that $\widetilde Q_i$ may be neither a root object nor invertible.

## Source Locations

### Root-or-invertible dichotomy

- `inbox/papers/crystal.tex:3649-3657`: Proposition `prop:simpleroot`.
  If $i$ satisfies either $s_iw<w$ or $ws_i<w$, then $\widetilde Q_i$ is a root object or invertible. The proof uses that $\widetilde Q_i$ has an affinization of degree $2\mathsf d_i$ and checks the R-matrix degree inequality.

This is not yet a positive example because it leaves two possibilities: root object or invertible.

### Positive branch where $\widetilde Q_i$ is root

- `inbox/papers/crystal.tex:4576-4585`: in the proof of the main theorem, under the case
  $$
  \mathsf d_i(X)>0,
  $$
  the paper states that $\widetilde Q_i$ is a root object by Proposition `prop:simpleroot` and Lemma `lem:inv`.

This is the safest positive source location for a later example paragraph.

### Earlier use of the same root-object branch

- `inbox/papers/crystal.tex:3857-3871`: Lemma `lem:iistar` assumes $ws_i<w$ and studies the case $\mathsf d_i(X)>0$; the text notes that in part (i), $\widetilde Q_i$ is a root object.

This supports the same conditional example, but the later main-theorem proof is more direct.

### Invertible branch and warning

- `inbox/papers/crystal.tex:3529-3544`: Lemma `lem:inv` says that an invertible simple object strongly commutes with every simple object.
- `inbox/papers/crystal.tex:3702-3708`: the type $A_3$ remark says that, in general, $\widetilde Q_i$ may be neither a root object nor invertible, and gives explicit expressions for $\widetilde Q_i$ and $\mathscr D^{-1}\widetilde Q_i$ in that warning example.

These locations explain why the example must remain conditional.

## Proposed Topic-Page Wording

If a later approved edit fills `## 기본 예시`, use wording close to the following and do not add stronger claims.

```markdown
### 조건부 예시

$i\in I_w$이고 $X$가 $\widetilde{\mathcal C}_w$의 simple object라고 하자. $\widetilde Q_i=Q_w(\langle i\rangle)$에 대해
$$
\mathsf d_i(X)>0
$$
인 branch에서는 $\widetilde Q_i$가 root object로 작동한다.

이 예시는 root object가 localized simple-root object와 만나는 방식을 보여 준다. $\widetilde Q_i$는 항상 root object인 것은 아니지만, $\mathsf d_i(X)>0$인 branch에서는 invertible case가 아니라 root-object case에 놓이고, localized root operator의 convolution input으로 쓰인다.
```

The wording intentionally says "branch" and does not claim a concrete low-rank example.

## What Not To Add

- Do not write "$\widetilde Q_i$ is a root object for all $i\in I_w$."
- Do not write the type $A_3$ warning as a positive root-object example.
- Do not add the localized root-operator formulas to the root-object page as part of this example.
- Do not upgrade the page to `example-ready` until the conditional-example wording is actually applied and the relation sections are checked.

## Recommended Later Edit

After approval, update only:

- `content/topics/root-objects-in-localized-categories.md`
- `data/topic_maturity.yml`
- `data/research_queue.yml`
- `data/review_backlog.yml`
- `reports/roadmap/next-actions.md`

The edit should add the conditional example above, keep theorem-level details out of the example, and avoid any claim additions.

## Validation

- `git diff --check`: passed.
- `python3 scripts/run_all_checks.py`: passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 51 content files.
- `npx quartz build`: failed with the known standalone Node heap out-of-memory failure.
