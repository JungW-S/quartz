# Affine Objects Example Scope Review

Date: 2026-06-03

## Scope

This report checks whether `content/topics/03-category-theory/affine-objects-in-monoidal-categories.md` should add a broader source-backed example beyond the current quiver-Hecke example
$$
L(i)=\langle i\rangle.
$$

Only `inbox/papers/crystal.tex` and the existing topic page were checked. No topic page was edited. No claims were added. No sources were downloaded.

## Current Page State

The topic page already has the needed reader-facing layers:

- the pro-category and graded monoidal setup;
- the definition of affine object in $\operatorname{Pro}^{\mathrm{coh}}(\mathbf k[z],\mathscr C)$;
- the distinction between affine object and affinization;
- the definition of affreal simple object;
- one paper-verified example, namely the quiver-Hecke simple root module $L(i)=\langle i\rangle$.

This is enough for the page's current role as a prerequisite for root objects and localized root operators.

## Source Locations Checked

- `inbox/papers/crystal.tex:1164-1173`: the introduction says that affinizations, R-matrices, and rigidity are needed to define crystal structures on localized categories. It mentions the symmetric quiver-Hecke case where an affinization can be given by $\mathbf k[z]\otimes_{\mathbf k}M$, but this is motivational context rather than a worked example.
- `inbox/papers/crystal.tex:1623-1642`: Definition of affine object and $\operatorname{Aff}(\mathscr C)$.
- `inbox/papers/crystal.tex:1798-1804`: Definition of affinization as an affine object with rational-center data and special fiber $\widehat M/z\widehat M\simeq M$.
- `inbox/papers/crystal.tex:1837-1842`: Definition of real and affreal simple objects.
- `inbox/papers/crystal.tex:2348-2375`: quiver-Hecke affinization definition and the explicit example that $L(i)=\langle i\rangle$ is affreal.
- `inbox/papers/crystal.tex:2976-3022`: localization compatibility for affinizations. This is theorem-level infrastructure, not a basic visible example.
- `inbox/papers/crystal.tex:3546-3553`: root-object definition uses an affinization of degree $2d_L$.
- `inbox/papers/crystal.tex:3654-3657`: the simple-root object $\widetilde Q_i$ has an affinization of degree $2\mathsf d_i$ in the proof that it is a root object or invertible.

## Decision

Do not add a broader visible example to the affine-object page now.

The current $L(i)=\langle i\rangle$ example is the safest basic example because the paper states it explicitly. The broader material in KN25 is better used as connections:

- the symmetric case $\mathbf k[z]\otimes M$ is introductory context, not a developed worked example in the paper;
- localization compatibility is a proposition about how affinizations pass through $Q$, so it belongs in the basic properties/relations layer rather than as an example;
- $\widetilde Q_i$ belongs to root objects and localized root operators, not to the basic affine-object page.

## Proposed Wording

No wording change is recommended. The topic page should remain stable until a separate source-backed worked example is approved.

## Next Step

Move to the next dependency topic in the queue: review `R-Matrix Renormalization` for whether it needs a broader source-backed example beyond the current quiver-Hecke universal R-matrix setup.
