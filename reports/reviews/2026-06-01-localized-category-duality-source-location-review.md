# Reverse Equivalence of Localized Categories Source-Location Review

Date: 2026-06-01

## Scope

This report reviews exact source locations for the formerly title-only topic `content/topics/localized-category-duality.md`, now retitled and moved to `content/topics/reverse-equivalence-of-localized-categories.md`.

Only `inbox/papers/crystal.tex` was checked. No topic page was edited. No claims were added. No sources were downloaded.

## Main Source Locations

### 1. Object duality and rigidity background

- `inbox/papers/crystal.tex:1672-1689`: defines right dual, left dual, the notation $\mathscr D(X)$ and $\mathscr D^{-1}(X)$, and rigid monoidal category.
- `inbox/papers/crystal.tex:2907-2917`: Theorem 5.3 states that $\widetilde{\mathcal C}_w$ is rigid, so every object of $\widetilde{\mathcal C}_w$ has a left dual and a right dual.
- `inbox/papers/crystal.tex:1178-1182`: the introduction uses this rigidity as part of the setup for defining the crystal structure on $\operatorname{Irr}(\widetilde{\mathcal C}_w)$.

This is object-level duality inside one localized monoidal category. It should not be confused with the reverse-category equivalence below.

### 2. Reverse monoidal category setup

- `inbox/papers/crystal.tex:3040-3049`: Section heading and setup for the equivalence between $(\widetilde{\mathcal C}_w)^{\mathrm{rev}}$ and $\widetilde{\mathcal C}_{w^{-1}}$.
  The source recalls that for a monoidal category $(\mathscr C,\otimes)$, the reverse monoidal category $\mathscr C^{\mathrm{rev}}$ has tensor product
  $$
  M\otimes_{\mathrm{rev}}N:=N\otimes M.
  $$

### 3. The anti-automorphism $\psi$ and ambient equivalence

- `inbox/papers/crystal.tex:3052-3065`: defines the ring automorphism $\psi:R(\beta)\to R(\beta)$ by reversing idempotent words, sending $x_k$ to $x_{n+1-k}$, and sending $\tau_l$ to $-\tau_{n-l}$.
- `inbox/papers/crystal.tex:3062-3065`: this $\psi$ induces a monoidal equivalence
  $$
  \psi_*:(R\text{-gmod})^{\mathrm{rev}}\simeq R\text{-gmod}.
  $$

### 4. Determinantial modules under $\psi_*$

- `inbox/papers/crystal.tex:3068-3073`: Lemma 5.6 states that for $w\in W$ and any $w$-dominant $\lambda\in P$,
  $$
  \psi_*\bigl(\mathsf M_w(w\lambda,\lambda)\bigr)
  \simeq
  \mathsf M_{w^{-1}}(-\lambda,-w\lambda).
  $$

This explains why the localization data for $w$ is compatible with the localization data for $w^{-1}$ after reversing the tensor product.

### 5. Main reverse-equivalence theorem

- `inbox/papers/crystal.tex:3076-3084`: Theorem 5.7 states that there is an equivalence of monoidal categories
  $$
  (\widetilde{\mathcal C}_w)^{\mathrm{rev}}
  \simeq
  \widetilde{\mathcal C}_{w^{-1}}.
  $$
  More precisely, the source gives a quasi-commutative diagram
  $$
  \begin{array}{ccc}
  (R\text{-gmod})^{\mathrm{rev}} & \xrightarrow{\ \psi_*\ } & R\text{-gmod}\\
  \downarrow Q && \downarrow Q_{w^{-1}}\\
  (\widetilde{\mathcal C}_w)^{\mathrm{rev}} & \xrightarrow{\ \psi_*\ } & \widetilde{\mathcal C}_{w^{-1}}.
  \end{array}
  $$

This is the safest central statement for the topic page.

### 6. Later use in crystal connectedness

- `inbox/papers/crystal.tex:4791-4795`: in the connectedness proof, the source uses Theorem 5.7 to identify
  $$
  \psi_*:
  \bigl(\operatorname{Irr}(\widetilde{\mathcal C}_w),\{\widetilde E_i,\widetilde F_i\}_{i\in I}\bigr)
  \simeq
  \bigl(\operatorname{Irr}(\widetilde{\mathcal C}_{w^{-1}}),\{\widetilde E_i^*,\widetilde F_i^*\}_{i\in I}\bigr)
  $$
  as a crystal isomorphism.

This is safe to mention as a consequence or use, but it should not replace the category-level theorem.

### 7. Separate localization equivalence used in bijectivity proof

- `inbox/papers/crystal.tex:4715-4728`: the bijectivity proof recalls a different equivalence from KKOP23:
  $$
  \Phi:\widetilde{\mathcal C}_{w'}\xrightarrow{\sim}\widetilde{\mathcal C}_{w,s_i}
  $$
  where $w'=ws_i<w$, and the right-hand localization uses a commuting family of right braiders
  $$
  \{\mathsf M(w\Lambda,s_i\Lambda)\mid \Lambda\in P_+\}
  $$
  in $\mathcal C_w$.

This is related to the inductive proof of bijectivity of $\operatorname{CP}$, but it is not the main reverse-equivalence statement of Section 5.3.

## Safe Page Scope

The future topic page should distinguish three levels:

- object-level duals inside a rigid localized category: $\mathscr D(X)$ and $\mathscr D^{-1}(X)$;
- category-level reverse equivalence:
  $$
  (\widetilde{\mathcal C}_w)^{\mathrm{rev}}\simeq\widetilde{\mathcal C}_{w^{-1}};
  $$
- crystal-level consequence:
  $\psi_*$ exchanges the localized crystal operators with the starred localized crystal operators.

The main definition/statement should be the reverse monoidal equivalence, not a vague "duality" slogan.

## Title Recommendation

The original title `Localized Category Duality` was ambiguous, because the source distinguishes object duality from reverse-category equivalence. The applied topic title is:

- `Reverse Equivalence of Localized Categories`

This title names the main theorem rather than the broader duality vocabulary.

## Applied Edit

The approved edit was applied to `content/topics/reverse-equivalence-of-localized-categories.md`:

- Retitled `Localized Category Duality` to `Reverse Equivalence of Localized Categories`.
- Filled `개요`, `준비와 notation`, `정리의 진술`, `핵심 관점`, `기본 성질`, `다른 topic들과의 관계`, `더 읽을 topic`, and `Source notes`.
- Left `기본 예시` empty because no small source-backed example of $\psi_*$ has been separately reviewed.
- Updated hierarchy, maturity, research queue, review backlog, source note, and map-generation metadata.

## Do Not Write Yet

- Do not call $\mathscr D^{\pm1}$ and $\psi_*$ the same construction.
- Do not state a general duality theorem for arbitrary localized monoidal categories.
- Do not use the KKOP23 equivalence $\widetilde{\mathcal C}_{w'}\simeq\widetilde{\mathcal C}_{w,s_i}$ as the definition of this topic.
- Do not add a visible example until a specific $\psi_*$ example has been reviewed.

## Validation

- `git diff --check` passed.
- `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and the internal Quartz build over 51 content files.
- Standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
