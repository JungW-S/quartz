# Topic Publishability Polish

Date: 2026-06-01

Scope: first batch of topic-page polishing and public readiness display.

## Topics Polished

- `Root Systems and Weight Lattices`
- `Universal Enveloping Algebras`
- `Quantum Groups`
- `Crystal Bases`
- `Quiver-Hecke Algebras`

## What Changed

- Korean learning-order prose was tightened.
- English explanatory sentences were converted to Korean prose while preserving English mathematical terms.
- Prerequisite links were made more explicit where a topic mentioned another topic-level concept.
- Level distinctions were clarified, especially object-level algebra, category-level module categories, and Grothendieck-group-level categorification.
- Unsupported example gaps remained unfilled.

## Public Readiness Dashboard

The public dashboard is generated at `content/maps/topic-status.md`.

Current status counts:

- Publishable: 10
- Incomplete: 18

The dashboard is separate from topic-page exposition, so topic pages remain reader-facing mathematical articles.

## Validation

- `git diff --check` passed.
- `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and the internal Quartz build over 51 content files.
- Standalone `npx quartz build` failed with the known Node heap out-of-memory failure.

## Non-actions

- No sources were downloaded.
- No claims were added.
- No unsupported examples were added.
- No status badges were inserted into topic pages.
