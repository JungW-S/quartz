# Crystal Bases Rank-Two Example Need Review

Date: 2026-06-01

## Scope

This report reviews whether `content/topics/02-crystal-bases/crystal-bases.md` still needs a rank-two example after the Hong-Kang 2002 finite string crystal example was added.

The only source checked for the possible rank-two example was Kashiwara 1993, Examples 2.2.5-2.2.7.

No topic page was rewritten. No claims were added. No sources were downloaded. No Sage code or images were generated.

## Sources Checked

- Source note: `content/sources/papers/kashiwara93-crystal-base-demazure-character-formula.md`
- Staged PDF: `content/assets/pdfs/kashiwara93-crystal-base-demazure-character-formula.pdf`
- Current topic page: `content/topics/02-crystal-bases/crystal-bases.md`

Exact checked source locations:

- Kashiwara 1993, Section 2.2, Proposition 2.2.3, p.849.
- Kashiwara 1993, Section 2.2, Proposition 2.2.4, p.850.
- Kashiwara 1993, Examples 2.2.5-2.2.7, pp.850-851.

## Decision

Do not add Examples 2.2.5-2.2.7 to the main `Crystal Bases` page now.

After the Hong-Kang finite string example, the page already has:

- abstract crystal examples from Kashiwara 1993,
- the elementary crystal $B_i$,
- and a finite crystal graph coming from an actual finite-dimensional $U_q(\mathfrak{sl}_2)$-module.

Examples 2.2.5-2.2.7 are mathematically useful, but they are not a simple next example for an undergraduate-facing prerequisite page. They describe coordinate embeddings of $B(\infty)$ in rank two, not a small finite crystal graph.

## What The Examples Actually Do

Kashiwara 1993 first uses Theorem 2.2.1 and Proposition 2.2.3 to realize $B(\infty)$ inside tensor products of elementary crystals $B_i$ through maps of the form
$$
\Psi_{i_1,\ldots,i_\ell}:B(\infty)\to B(\infty)\otimes B_{i_1}\otimes\cdots\otimes B_{i_\ell}.
$$

Then Examples 2.2.5-2.2.7 specialize the rank-two cases:

- Example 2.2.5: type $A_2$.
- Example 2.2.6: type $B_2$.
- Example 2.2.7: type $G_2$.

The examples give images of $B(\infty)$ inside tensor products such as
$$
B_1\otimes B_2\otimes B_1
$$
for type $A_2$, and longer alternating products for types $B_2$ and $G_2$, with inequalities on the integer coordinates.

These are coordinate descriptions of an infinite crystal. They depend on the setup of Section 2.2 and are closer to a future topic such as `Rank-Two Coordinates for B(infty)` or an advanced `Cellular Crystals` / tensor-coordinate discussion than to the first `Crystal Bases` study page.

## Reason Not To Add Now

Adding these examples directly to `Crystal Bases` would create three problems:

- It would shift the page from learning the definition and basic graph intuition toward a coordinate model of $B(\infty)$.
- The inequalities in Examples 2.2.5-2.2.7 require more setup than the current page should carry.
- The page now already has a source-backed finite example that connects directly to `Quantum Groups`, so the immediate example gap is closed.

## Deferred Use

The rank-two examples should be kept as future advanced material.

If they are used later, the safer route is:

1. create or approve a focused topic for $B(\infty)$ coordinate models or rank-two crystal coordinates,
2. introduce the embedding $\Psi_{i_1,\ldots,i_\ell}$ first,
3. then use Example 2.2.5 as the smallest concrete case,
4. defer $B_2$ and $G_2$ unless the page specifically needs non-simply-laced rank-two behavior.

## Recommendation

Keep `content/topics/02-crystal-bases/crystal-bases.md` unchanged for now.

Do not add a rank-two example to the main page unless a later task explicitly targets $B(\infty)$ coordinate models or cellular/tensor-coordinate constructions.

## Validation

- `git diff --check` passed.
- `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 52 content files.
- Standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
