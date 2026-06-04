# Root Objects Source-Location Review

Date: 2026-06-01

Source checked: `inbox/papers/crystal.tex` only.

No topic page was rewritten. No claims were added. No sources were downloaded.

## Source Locations

- Setup for the localized category: `inbox/papers/crystal.tex:2891-2915`.
  This is where the paper defines the localization functors and records rigidity of $\widetilde{\mathcal C}_w$.
- Support set notation: `inbox/papers/crystal.tex:2929-2931`.
  This defines $I_w$.
- Simple-root object notation: `inbox/papers/crystal.tex:929`, `inbox/papers/crystal.tex:2244-2245`.
  The paper uses $\widetilde Q_i=\mathrm Q(\langle i\rangle)$ and identifies $\langle i\rangle$ with $L(i)$.
- Affine objects and affinizations: `inbox/papers/crystal.tex:1623-1640`, `inbox/papers/crystal.tex:1777-1802`.
  These are prerequisite definitions for the root-object condition.
- Real and affreal simple objects: `inbox/papers/crystal.tex:1837-1841`.
  Root objects are defined only after this real/affinization language is available.
- R-matrix degree functions: `inbox/papers/crystal.tex:1731-1746`, `inbox/papers/crystal.tex:3349-3354`.
  These define $\Lambda$, $\mathfrak d$, and $\widetilde\Lambda$ notation used around the root-object definition.
- Root-object definition: `inbox/papers/crystal.tex:3546-3553`.
  This is the exact definition to use for the future topic page.
- Immediate root-object facts: `inbox/papers/crystal.tex:3556-3571`, `inbox/papers/crystal.tex:3573-3600`, `inbox/papers/crystal.tex:3602-3644`.
  These are candidates for a later `기본 성질` section after approval.
- Localized simple-root object caution: `inbox/papers/crystal.tex:3649-3652`, `inbox/papers/crystal.tex:3702-3708`.
  The paper does not allow us to say that every $\widetilde Q_i$ is a root object.
- Dependency of localized root operators on $\widetilde Q_i$: `inbox/papers/crystal.tex:3715-3725`.

## Safe Definition Outline

The future page can safely say, after approval, that a root object is a real simple object $L$ of $\widetilde{\mathcal C}_w$ satisfying two extra conditions:

1. $L$ has an affinization $(\widehat L,z)$ with $\deg(z)=2d_L$ for some $d_L\in\mathbb Z_{>0}$.
2. The R-matrix degree invariant satisfies
   $$
   \mathfrak d(L,\mathscr D^{-1}L)=d_L.
   $$

The setup must first explain $\widetilde{\mathcal C}_w$, real simple objects, affinizations, the duality functor $\mathscr D^{-1}$, and the invariant $\mathfrak d(-,-)$.

## Safe Properties To Use Later

- If $L$ is a root object, then $\mathscr D L$ and $\mathscr D^{-1}L$ are again root objects.
- If $L$ is a root object, then the source gives formulas for $\Lambda(L,\mathscr D L)$ and $\Lambda(\mathscr D L,L)$.
- If $L$ is a root object and $M$ is simple, the paper controls the head convolutions $L\mathbin{\nabla}M$ and $M\mathbin{\nabla}L$ through R-matrix degree formulas.
- Under the stated descent condition on $i$, $\widetilde Q_i$ is either a root object or invertible.

## Do Not Write Yet

- Do not state that every $\widetilde Q_i$ is a root object.
- Do not use the $A_3$ remark as a positive example of a root object; it is a warning that $\widetilde Q_i$ can be neither root nor invertible.
- Do not fill a visible `기본 예시` section until a genuine source-backed positive example is selected.
- Do not state the localized root-operator formulas on the root-object page unless the page explicitly separates the general root-object definition from the special objects $\widetilde Q_i$.

## Proposed Next Edit After Approval

Fill only these sections of `content/topics/08-localization-of-categories/root-objects-in-localized-categories.md`:

- `개요`: one paragraph explaining that root objects are the affine-real simple objects used to control localized crystal operators.
- `준비와 notation`: introduce $\widetilde{\mathcal C}_w$, $\mathscr D$, $\mathfrak d(-,-)$, affinization, and $\widetilde Q_i$.
- `정의`: state the two-condition definition above.
- `기본 성질`: include only dual-closure and the caution about $\widetilde Q_i$.
- `Source notes`: cite the exact source locations above.

Leave `기본 예시` empty unless the user approves a specific positive example.

## Applied Edit

Applied on 2026-06-01 to `content/topics/08-localization-of-categories/root-objects-in-localized-categories.md`: overview, setup/notation, definition, basic properties, and Source notes were filled from the reviewed source locations. The example, viewpoint, and relation sections remain unfilled pending separate source-location review.

Validation after the applied edit: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including its internal Quartz build over 51 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
