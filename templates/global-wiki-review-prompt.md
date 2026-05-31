# Global Wiki Review Prompt

Use this prompt for a full advisory review of the wiki. The review may report problems and update workflow trackers, but it must not perform gated research actions without separate approval.

## Inputs To Read

- `AGENTS.md`
- `README.md`
- `content/topics/AGENTS.md`
- `content/topics/STYLE_GUIDE.md`
- all topic pages under `content/topics/`
- source notes under `content/sources/`
- registries under `data/`
- roadmap and review reports under `reports/`
- reusable prompts under `templates/`

## Review Scope

Check:

- topic structure and readability
- prohibited workflow/status language in reader-facing pages
- source coverage and exact source locations
- claim registry consistency
- source candidate status and approval gates
- graph edge quality and broken links
- notation consistency and raw notation patterns
- roadmap action size and approval requirements

## Required Outputs

1. Write `reports/reviews/YYYY-MM-DD-global-wiki-review.md`.
2. Update `data/review_backlog.yml` with actionable findings.
3. Update `reports/roadmap/next-actions.md`.

## Report Format

Include:

- scope
- checks run
- findings ordered by severity
- exact files involved
- recommended action
- whether each action requires a new source
- whether each action requires user approval
- residual risks

## Safety Rules

- Do not download, fetch, stage, or intake sources.
- Do not add claims, source notes, graph edges, or topic pages.
- Do not rewrite topic pages.
- Do not treat candidate sources as citations.
- Keep review findings out of reader-facing topic exposition.
