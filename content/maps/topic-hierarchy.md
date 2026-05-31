---
title: Topic Hierarchy
---

# Topic Hierarchy

```mermaid
flowchart TD
  cellular_crystals["Cellular Crystals"]
  crystal_bases["Crystal Bases and Crystal Graphs"]
  determinantial_modules["Determinantial Modules"]
  dual_canonical_bases["Dual Canonical Bases"]
  lie_algebras_and_hopf_algebras["Lie Algebras and Hopf Algebras"]
  localized_crystals["Localized Crystals"]
  monoidal_categorification["Monoidal Categorification"]
  quantum_coordinate_rings["Quantum Coordinate Rings"]
  quantum_groups["Quantum Groups"]
  quiver_hecke_algebra_localization["Quiver-Hecke Algebra Localization"]
  quiver_hecke_algebras["Quiver-Hecke Algebras"]
  root_systems_and_weight_lattices["Root Systems and Weight Lattices"]
  crystal_bases -->|parent| cellular_crystals
  crystal_bases -->|parent| localized_crystals
  lie_algebras_and_hopf_algebras -->|parent| quantum_groups
  monoidal_categorification -->|parent| determinantial_modules
  quantum_coordinate_rings -->|parent| determinantial_modules
  quantum_coordinate_rings -->|parent| dual_canonical_bases
  quantum_groups -->|parent| crystal_bases
  quantum_groups -->|parent| quantum_coordinate_rings
  quiver_hecke_algebra_localization -->|parent| localized_crystals
  quiver_hecke_algebras -->|parent| determinantial_modules
  quiver_hecke_algebras -->|parent| quiver_hecke_algebra_localization
```

## Topics

- [[topics/cellular-crystals|Cellular Crystals]]
- [[topics/crystal-bases|Crystal Bases and Crystal Graphs]]
- [[topics/determinantial-modules|Determinantial Modules]]
- [[topics/dual-canonical-bases|Dual Canonical Bases]]
- [[topics/lie-algebras-and-hopf-algebras|Lie Algebras and Hopf Algebras]]
- [[topics/localized-crystals|Localized Crystals]]
- [[topics/monoidal-categorification|Monoidal Categorification]]
- [[topics/quantum-coordinate-rings|Quantum Coordinate Rings]]
- [[topics/quantum-groups|Quantum Groups]]
- [[topics/quiver-hecke-algebra-localization|Quiver-Hecke Algebra Localization]]
- [[topics/quiver-hecke-algebras|Quiver-Hecke Algebras]]
- [[topics/root-systems-and-weight-lattices|Root Systems and Weight Lattices]]
