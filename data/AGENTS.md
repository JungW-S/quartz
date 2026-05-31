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
- `data/discussion_notes.yml` stores user-approved exposition, interpretation, notation, and learning-order notes separately from mathematical sources.
- Discussion notes must not be used as source provenance for theorem-level claims, real examples, definitions, or claim additions.
- Keep discussion labels to `user-approved-exposition`, `user-approved-interpretation`, `notation-decision`, or `learning-order-decision` unless the schema is explicitly updated.
