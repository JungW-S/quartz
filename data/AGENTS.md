# Metadata Registry Instructions

The YAML files in `data/` are the canonical metadata registries for the wiki.

## Rules

- Do not add fake sources, fake claims, or invented graph edges.
- Empty lists are valid before source intake.
- Keep IDs lowercase and hyphenated.
- Keep registry paths relative to the repository root.
- Claims must have real source provenance before they are added.
- Edges should describe meaningful relationships and must not theoremize analogies.
- Mark uncertain future entries in adjacent notes or reports with `<!-- NEEDS-HUMAN-REVIEW -->` while keeping YAML schema values valid.
