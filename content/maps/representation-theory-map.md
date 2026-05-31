---
title: Representation Theory Map
---

# Representation Theory Map

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
  cellular_crystals -->|prereq/related| localized_crystals
  crystal_bases -->|parent/prereq| cellular_crystals
  crystal_bases -->|related| dual_canonical_bases
  crystal_bases -->|parent/prereq| localized_crystals
  determinantial_modules -->|prereq/context_for/related| quiver_hecke_algebra_localization
  dual_canonical_bases -->|related| crystal_bases
  lie_algebras_and_hopf_algebras -->|parent/prereq| quantum_groups
  lie_algebras_and_hopf_algebras -->|related| root_systems_and_weight_lattices
  localized_crystals -->|related| monoidal_categorification
  monoidal_categorification -->|parent/prereq| determinantial_modules
  monoidal_categorification -->|related| localized_crystals
  monoidal_categorification -->|prereq/related| quiver_hecke_algebra_localization
  monoidal_categorification -->|related| quiver_hecke_algebras
  quantum_coordinate_rings -->|parent/prereq| determinantial_modules
  quantum_coordinate_rings -->|parent/prereq| dual_canonical_bases
  quantum_coordinate_rings -->|prereq/related| monoidal_categorification
  quantum_coordinate_rings -->|related| quiver_hecke_algebra_localization
  quantum_groups -->|parent/prereq| crystal_bases
  quantum_groups -->|prereq/related| dual_canonical_bases
  quantum_groups -->|parent/prereq| quantum_coordinate_rings
  quantum_groups -->|context_for| quiver_hecke_algebras
  quiver_hecke_algebra_localization -->|parent/prereq| localized_crystals
  quiver_hecke_algebra_localization -->|related| quantum_coordinate_rings
  quiver_hecke_algebras -->|parent/prereq| determinantial_modules
  quiver_hecke_algebras -->|context_for/related| monoidal_categorification
  quiver_hecke_algebras -->|related| quantum_groups
  quiver_hecke_algebras -->|parent/prereq| quiver_hecke_algebra_localization
  root_systems_and_weight_lattices -->|prereq| cellular_crystals
  root_systems_and_weight_lattices -->|prereq/related| crystal_bases
  root_systems_and_weight_lattices -->|related| lie_algebras_and_hopf_algebras
  root_systems_and_weight_lattices -->|prereq| quantum_coordinate_rings
  root_systems_and_weight_lattices -->|prereq/related| quantum_groups
  root_systems_and_weight_lattices -->|prereq/related| quiver_hecke_algebras
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
