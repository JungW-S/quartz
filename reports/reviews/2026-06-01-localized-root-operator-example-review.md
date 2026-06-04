# Localized Root Operator Example Review

Date: 2026-06-01

## Scope

This is a report-only review of whether `content/topics/08-localization-of-categories/localized-root-operators.md` can receive a concrete source-backed example from Kashiwara-Nakashima 2025.

Only local `inbox/papers/crystal.tex` and existing review reports were checked. No topic page was rewritten. No claims were added. No source was downloaded. No Sage code or image artifact was created.

## Decision

Do not fill the visible `## 기본 예시` section from Kashiwara-Nakashima 2025 alone.

The checked source gives the operator formulas, inverse property, crystal-structure theorem, compatibility lemmas, and several warning examples. It does not give a clean concrete worked example of the form "for this explicit localized simple object $X$, $\widetilde F_iX$ is this explicit localized simple object" that is suitable as a basic example for the topic page.

Safe conclusion:

- `content/topics/08-localization-of-categories/localized-root-operators.md` should keep `## 기본 예시` empty for now.
- The type $A_2$ and type $A_3$ computations in the source should not be used as positive localized-root-operator examples.
- A later visible example should come from either an approved source with an explicit worked operator computation or a separately verified Sage/code pipeline.

## Source Locations Checked

### Operator definition and immediate theorem

- `inbox/papers/crystal.tex:3711-3729`: Definition `def:rootop` defines $\widetilde F_i$, $\widetilde E_i$, $\widetilde F_i^*$, $\widetilde E_i^*$ using $\widetilde Q_i$, $\widetilde\Lambda$, $\mathfrak d$, and head convolution.
- `inbox/papers/crystal.tex:3731-3742`: proposition and theorem state inverse properties and the crystal structure on $\operatorname{Irr}(\widetilde{\mathcal C}_w)$.
- `inbox/papers/crystal.tex:3744-3762`: the proof records the mechanism that $\widetilde F_i$ changes the crystal data in the expected $i$-direction, but this is not a concrete worked example with an explicit object.

### Conditional compatibility statements

- `inbox/papers/crystal.tex:3784-3805`: if $M\in\mathfrak B_w$ and $\widetilde E_iM\ne0$, then localization commutes with the corresponding $\widetilde E_i$ operation. This is a useful compatibility lemma, not a standalone example.
- `inbox/papers/crystal.tex:3859-3881`: under the hypothesis $ws_i<w$, the source gives conditional commutation behavior involving $\widetilde F_i$ and starred operators. This is theorem-level behavior, not a basic example.
- `inbox/papers/crystal.tex:3893-3903`: under descent hypotheses, $\widetilde F_i(\Phi_w(M))\simeq\Phi_w(\widetilde F_iM)$ or the starred analogue. This can explain compatibility after prerequisites are clear, but it still does not supply an explicit worked localized object.

### Warning examples not suitable for positive examples

- `inbox/papers/crystal.tex:3702-3708`: the type $A_3$ remark shows that $\widetilde Q_i$ may be neither a root object nor invertible. This is a caution about the root-object input, not a positive localized-root-operator example.
- `inbox/papers/crystal.tex:3912-3943`: the type $A_2$ and type $A_3$ computations show that $\varepsilon_i(\Phi_w(M))=\varepsilon_i(M)$ need not hold in general. These are useful warnings about compatibility with nonlocalized operators, not examples of computing $\widetilde E_i$ or $\widetilde F_i$ as a positive worked example.

### Main theorem proof branches

- `inbox/papers/crystal.tex:4567-4573`: in the case $\mathsf d_i(X)=0$, the source uses commutation of $\widetilde Q_i$ with $X$ and obtains $\widetilde F_i(X)=\widetilde F_i^*(X)$.
- `inbox/papers/crystal.tex:4581-4594`: in the case $\mathsf d_i(X)>0$, the source uses that $\widetilde Q_i$ is a root object and reduces a compatibility statement for $\operatorname{Est}(\widetilde F_iX)$.

These are safe source-backed mechanisms, but they are proof branches rather than concrete basic examples.

## Proposed Topic-Page Wording

### Do not add to `## 기본 예시`

No visible example paragraph should be added from this review. Keeping the section empty is more accurate than presenting a proof branch or warning computation as an example.

### Optional `## 핵심 관점` wording after approval

The following wording is safe as a later topic-page polishing edit. It should not be added together with a visible example unless a concrete example is separately approved.

```markdown
Localized root operator의 핵심은 crystal graph의 arrow를 localized category 안의 head convolution으로 구현하는 것이다. Ordinary crystal에서는 $\widetilde f_i$가 vertex를 다른 vertex로 보내는 combinatorial map이지만, 여기서는 vertex가 $\widetilde{\mathcal C}_w$의 simple object이므로, $\widetilde Q_i$와 convolution의 simple head를 이용해 새 simple object를 만든다.

정의에서 $\varepsilon_i(X)$와 $\varepsilon_i^*(X)$는 $\widetilde Q_i$가 $X$의 왼쪽 또는 오른쪽에서 얼마나 강하게 상호작용하는지를 modified R-matrix degree로 측정한다. 그 값이 grading shift와 head convolution에 들어가면서 $\widetilde F_iX$와 $\widetilde F_i^*X$가 만들어진다. $\widetilde E_i$와 $\widetilde E_i^*$는 duality functor $\mathscr D$를 사용해 반대 방향으로 돌아가는 operators이다.

따라서 localized root operator는 단순히 object를 하나 더 tensoring하는 조작이 아니다. R-matrix degree, duality, head convolution이 함께 맞아야 crystal axiom에 맞는 arrow가 되며, source의 inverse property와 crystal-structure theorem은 바로 이 data가 실제 crystal structure를 만든다는 사실을 보장한다.
```

## What Not To Add

- Do not use the type $A_2$ or type $A_3$ warning computations as positive examples.
- Do not claim that localization preserves ordinary crystal operators without the hypotheses stated in the source.
- Do not add a Sage-generated example unless the Sage code is written, run, and recorded as a verification artifact.
- Do not add a visible example merely to fill the template.

## Recommendation

The next safe edit is to apply only the `핵심 관점` wording above, leaving `## 기본 예시` empty and recording the example gap in the queue/backlog. A real visible example requires either a different approved source with an explicit worked computation or a separate Sage-verification workflow.
