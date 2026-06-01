---
title: Status Taxonomy
---

`status`는 claim이나 extracted unit의 provenance 상태를 표시하는 편집용 값입니다. Citation을 대신하지 않습니다.

- `draft`: source-backed 정리가 끝나지 않은 작업 상태입니다.
- `needs_source`: source location이 필요합니다.
- `sourced`: source와 source location이 기록되어 있습니다.
- `verified`: human editor가 source와 대조했습니다.
- `deprecated`: 유지할 수는 있지만 현재 preferred form은 아닙니다.

`NEEDS-HUMAN-REVIEW`는 schema status가 아니라 review marker입니다. YAML status 값으로 쓰지 않습니다.

<!-- NEEDS-HUMAN-REVIEW -->

첫 validation schema가 확정되면 이 taxonomy와 registry vocabulary를 다시 맞춥니다.
