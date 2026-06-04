# Wiki-codex

Minimal Quartz-based wiki repository.

## Setup

```zsh
npm i
npx quartz plugin install --from-config
npm run build
```

## Viewing the wiki locally

Markdown files in `content/` are the canonical source for this wiki. The generated HTML pages are the intended reading interface for study.

Use the local Quartz preview server:

```zsh
npm run dev
```

The local preview serves the site at http://localhost:8080.

On macOS, `open-wiki.command` can be double-clicked to start the preview server and open the wiki home page after the local server is actually listening. If needed, make it executable once:

```zsh
chmod +x open-wiki.command
```

## Content

Markdown files in `content/` are the authored source for this wiki.

Generated Quartz output is written to `public/`. Do not edit generated HTML manually; rebuild it from the Markdown sources.

Quartz configuration lives in `quartz.config.yaml`. The current local bootstrap keeps `baseUrl: localhost:8080`.

## Research Workflow

This wiki uses an approval-gated research loop. Codex may suggest source candidates, run readability or notation audits, update topic maturity metadata, and write review reports. Codex must not download sources, intake papers, add claims, rewrite topic pages, or create new topic pages without explicit user approval for that specific action.

Primary workflow files:

- `data/source_candidates.yml`: candidate sources only; candidates are not citations.
- `data/topic_maturity.yml`: topic maturity, missing components, source coverage, readability, and notation status.
- `data/topic_polish_log.yml`: per-topic polish counts used by the `topic 수정` / `토픽수정` trigger.
- `data/research_queue.yml`: prioritized safest next tasks for topics.
- `data/review_backlog.yml`: actionable audit issues.
- `data/notation.yml`: canonical notation and raw-pattern audit registry.
- `reports/roadmap/next-actions.md`: one safest next task, alternatives, approval gates, and pasteable prompts.
- `reports/reviews/`: dated global, readability, notation, and topic-maturity reports.
- `templates/`: reusable prompts for source discovery, approved source intake, and audits.

Preferred prompt entry points:

- `templates/source-discovery-prompt.md`
- `templates/approved-source-intake-prompt.md`
- `templates/topic-maturity-audit-prompt.md`
- `templates/global-wiki-review-prompt.md`
- `templates/readability-audit-prompt.md`
- `templates/notation-audit-prompt.md`
- `templates/topic-polish-trigger-prompt.md`

## Topic polish trigger

Say `topic 수정` or `토픽수정` to run one bounded reader-facing polish pass. The workflow selects a topic with one of the lowest recorded polish counts, judges whether sentence or structure edits are rational, updates exactly one existing topic page when safe, and increments `data/topic_polish_log.yml`.

## Checks

The Python validation scripts use PyYAML for YAML registries and Markdown frontmatter:

```zsh
python3 -m pip install PyYAML
npm run check
```
