# Localized Root Operators Source-Location Review

Date: 2026-06-01

Source checked: `inbox/papers/crystal.tex` only.

No topic page was rewritten. No claims were added. No sources were downloaded.

## Source Locations

- Localized category setup: `inbox/papers/crystal.tex:2891-2915`.
  This is where the source defines the localization functors and records rigidity of $\widetilde{\mathcal C}_w$.
- Support set notation: `inbox/papers/crystal.tex:2929-2931`.
  This defines $I_w=\{i\in I\mid w\Lambda_i\ne\Lambda_i\}$.
- Localized simple-root object notation: `inbox/papers/crystal.tex:929`, `inbox/papers/crystal.tex:3715-3725`.
  The source writes $\widetilde Q_i=\Phi_w(\langle i\rangle)$ in local topic notation.
- Root-object prerequisite and caution: `inbox/papers/crystal.tex:3546-3553`, `inbox/papers/crystal.tex:3649-3652`, `inbox/papers/crystal.tex:3702-3708`.
  The localized root operators use $\widetilde Q_i$, but one must not say that every $\widetilde Q_i$ is a root object.
- Modified R-matrix degree: `inbox/papers/crystal.tex:3349-3354`.
  This defines $\widetilde\Lambda(X,Y)=(\Lambda(X,Y)+(\operatorname{wt}X,\operatorname{wt}Y))/2$ for $\Lambda$-definable pairs.
- Localized root-operator definition: `inbox/papers/crystal.tex:3711-3729`.
  This is the exact definition to use for a future topic-page edit.
- Immediate inverse property and crystal-structure theorem: `inbox/papers/crystal.tex:3731-3742`.
  These can support a short `기본 성질` section after approval.
- Compatibility with nonlocalized operators has hypotheses: `inbox/papers/crystal.tex:3784-3806`, `inbox/papers/crystal.tex:3893-3903`, and the warning in `inbox/papers/crystal.tex:3912-3943`.
  These should not be simplified into an unconditional compatibility statement.

## Safe Definition Outline

For $i\in I_w$ and a simple object $X\in\widetilde{\mathcal C}_w$, define
$$
\varepsilon_i(X)=\mathsf d_i^{-1}\widetilde\Lambda(\widetilde Q_i,X),
\qquad
\varepsilon_i^*(X)=\mathsf d_i^{-1}\widetilde\Lambda(X,\widetilde Q_i),
$$
where $\mathsf d_i=(\alpha_i,\alpha_i)/2$ in the source notation.

Then set
$$
\varphi_i(X)=\varepsilon_i(X)+\langle h_i,\operatorname{wt}X\rangle,
\qquad
\varphi_i^*(X)=\varepsilon_i^*(X)+\langle h_i,\operatorname{wt}X\rangle,
$$
and
$$
d_i(X)
=\mathsf d_i^{-1}\mathfrak d(\widetilde Q_i,X)
=\varepsilon_i(X)+\varepsilon_i^*(X)+\langle h_i,\operatorname{wt}X\rangle.
$$

The localized root operators are
$$
\widetilde F_iX
=q_i^{\varepsilon_i(X)}\,\widetilde Q_i\nabla X,
\qquad
\widetilde E_iX
=q_i^{\varphi_i(X)+1}\,X\nabla \mathscr D\widetilde Q_i.
$$

The source also defines the starred operators
$$
\widetilde F_i^*X
=q_i^{\varepsilon_i^*(X)}\,X\nabla\widetilde Q_i,
\qquad
\widetilde E_i^*X
=q_i^{\varphi_i^*(X)+1}\,\mathscr D^{-1}\widetilde Q_i\nabla X.
$$

For $i\notin I_w$, the source sets $\widetilde F_iX=\widetilde E_iX=0$ and $\varepsilon_i(X)=\varepsilon_i^*(X)=d_i(X)=-\infty$.

## Safe Properties To Use Later

- $\widetilde F_i$ and $\widetilde E_i$ are inverse to each other.
- $\widetilde F_i^*$ and $\widetilde E_i^*$ are inverse to each other.
- The data in the localized root-operator definition defines a crystal structure on $\operatorname{Irr}(\widetilde{\mathcal C}_w)$.

## Do Not Write Yet

- Do not state that every $\widetilde Q_i$ is a root object.
- Do not turn the $A_2$ and $A_3$ warnings about $\varepsilon_i(\Phi_w(M))$ into examples of the operators without a separate approved example decision.
- Do not state that $\varepsilon_i(\Phi_w(M))=\varepsilon_i(M)$ holds for all $i$ and all simple $M\in\mathcal C_w$.
- Do not expand the crystal comparison map $\operatorname{CP}$ on this page. That belongs to `content/topics/crystal-comparison-map.md`.
- Do not add proof details from the theorem unless the page is later upgraded beyond definition-ready.

## Proposed Next Edit After Approval

Fill only these sections of `content/topics/localized-root-operators.md`:

- `개요`: one paragraph saying that localized root operators are the maps $\widetilde E_i,\widetilde F_i$ on simple objects of $\widetilde{\mathcal C}_w$ that realize crystal arrows category-theoretically.
- `준비와 notation`: introduce $I_w$, $\operatorname{Irr}(\widetilde{\mathcal C}_w)$, $\widetilde Q_i$, $\mathsf d_i$, $\widetilde\Lambda$, $\mathfrak d$, $\nabla$, and $\mathscr D$.
- `map의 정의`: state the formulas above.
- `기본 성질`: include only the inverse-property and crystal-structure theorem, without proof details.
- `다른 topic들과의 관계`: link root objects, localized crystals, and cellular crystals with level-separated explanations.
- `Source notes`: cite the exact source locations above.

Leave `기본 예시` empty unless the user approves a specific source-backed example.

## Validation

- `git diff --check` passed.
- `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and the internal Quartz build over 51 content files.
- Standalone `npx quartz build` failed with the known Node heap out-of-memory failure.

## Applied Edit

Applied on 2026-06-01 to `content/topics/localized-root-operators.md`: overview, setup/notation, map definition, basic properties, relations, reader navigation, and Source notes were filled from the reviewed source locations. The example and viewpoint sections remain unfilled pending separate source-location review.

Validation after the applied edit: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and the internal Quartz build over 51 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
