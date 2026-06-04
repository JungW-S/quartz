# Quiver-Hecke Subcategories Optional Example Decision

Date: 2026-06-01

## Scope

This report decides whether `content/topics/06-quiver-hecke-klr-algebras/quiver-hecke-subcategories.md` should add the KN25 non-example or the KKOP18 determinantial-module family after the first type $A_2$ example.

Only already ingested KKOP18 and Kashiwara-Nakashima 2025 material was used. No topic pages were edited. No claims were added. No sources were downloaded.

## Decision

Add the KN25 non-example in a later approved topic-page edit.

Do not add the KKOP18 determinantial-module family to the `기본 예시` section of `Quiver-Hecke Subcategories` for now. That family is already the central object-family of `Determinantial Modules`, and the subcategory page already mentions it in `기본 성질` and links to the determinantial page. Repeating it as a basic example would make the first example section notation-heavy.

## Reasoning

The page now has a source-backed extreme example:

$$
\text{type } A_2,\quad w=s_1s_2s_1,\quad \mathcal C_w=R\text{-gmod}.
$$

This shows that $\mathcal C_w$ can be the whole ambient category. What is still useful for learning is the opposite behavior: an object that looks natural from determinantial-module notation but is filtered out by the $\mathcal C_w$ membership condition.

Kashiwara-Nakashima 2025 supplies exactly such a non-example. In type $A_2$, for

$$
w=s_1s_2,\qquad \lambda=s_1\Lambda_1,
$$

the source gives

$$
\mathsf M_w(w\lambda,\lambda)\simeq \langle 2\rangle
\notin \mathcal C_w,
$$

because $\alpha_2\notin\Delta_+\cap w\Delta_-$.

This is compact enough to fit after the current type $A_2$ example, provided the page explains that $\langle 2\rangle$ is source-specific simple-module notation.

## Source Locations

- KN25 local TeX lines 2858-2866: type $A_2$ non-example for $\mathcal C_w$.
- KKOP18 Proposition 4.8, local TeX lines 2929-2937: determinantial-module family in $\mathcal C_{w,v}$; not recommended for the subcategory page's basic example section at this point.
- `content/topics/06-quiver-hecke-klr-algebras/determinantial-modules.md`: already explains the family $M(w_{\le k}\Lambda,v_{\le k}\Lambda)$ in its definition and basic properties.

## Proposed Later Topic Wording

The following wording is safe for a later approved edit. It is not applied in this report-only pass.

```markdown
같은 source는 membership condition이 실제로 object를 걸러내는 경우도 준다. Type \(A_2\)에서 \(w=s_1s_2\), \(\lambda=s_1\Lambda_1\)로 두면

$$
\mathsf M_w(w\lambda,\lambda)\simeq \langle 2\rangle
\notin \mathcal C_w
$$

이다. 여기서 \(\langle 2\rangle\)는 source의 simple-module notation이다. 이 non-example은 \(\alpha_2\notin\Delta_+\cap w\Delta_-\)이므로 \(\mathcal C_w\)의 root-cone condition을 통과하지 못한다는 점을 보여 준다.
```

## Not Recommended For This Page Section

Do not add the KKOP18 family

$$
M(w_{\le k}\Lambda,v_{\le k}\Lambda)\in\mathcal C_{w,v}
$$

to `기본 예시` right now. It is better kept in `Determinantial Modules`, with `Quiver-Hecke Subcategories` linking there as the next topic.
