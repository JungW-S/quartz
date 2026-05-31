---
title: Crystal Bases Map
---

# Crystal Bases Map

```mermaid
flowchart TD
  cellular_crystals["Cellular Crystals"]
  crystal_bases["Crystal Bases and Crystal Graphs"]
  lie_algebras_and_hopf_algebras["Lie Algebras and Hopf Algebras"]
  localized_crystals["Localized Crystals"]
  quantum_groups["Quantum Groups"]
  quiver_hecke_algebra_localization["Quiver-Hecke Algebra Localization"]
  root_systems_and_weight_lattices["Root Systems and Weight Lattices"]
  cellular_crystals -->|prereq/related| localized_crystals
  crystal_bases -->|parent/prereq| cellular_crystals
  crystal_bases -->|parent/prereq| localized_crystals
  lie_algebras_and_hopf_algebras -->|parent/prereq| quantum_groups
  lie_algebras_and_hopf_algebras -->|related| root_systems_and_weight_lattices
  quantum_groups -->|parent/prereq| crystal_bases
  quiver_hecke_algebra_localization -->|parent/prereq| localized_crystals
  root_systems_and_weight_lattices -->|prereq| cellular_crystals
  root_systems_and_weight_lattices -->|prereq/related| crystal_bases
  root_systems_and_weight_lattices -->|related| lie_algebras_and_hopf_algebras
  root_systems_and_weight_lattices -->|prereq/related| quantum_groups
```

## Topics

- [[topics/cellular-crystals|Cellular Crystals]]
- [[topics/crystal-bases|Crystal Bases and Crystal Graphs]]
- [[topics/lie-algebras-and-hopf-algebras|Lie Algebras and Hopf Algebras]]
- [[topics/localized-crystals|Localized Crystals]]
- [[topics/quantum-groups|Quantum Groups]]
- [[topics/quiver-hecke-algebra-localization|Quiver-Hecke Algebra Localization]]
- [[topics/root-systems-and-weight-lattices|Root Systems and Weight Lattices]]
