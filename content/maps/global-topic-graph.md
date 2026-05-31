---
title: Global Topic Graph
---

# Global Topic Graph

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
  cellular_crystals -->|depends_on| crystal_bases
  cellular_crystals -->|prerequisite_for| localized_crystals
  cellular_crystals -->|related| monoidal_categorification
  crystal_bases -->|parent_of/supports| cellular_crystals
  crystal_bases -->|parent_of| localized_crystals
  crystal_bases -->|depends_on| quantum_groups
  crystal_bases -->|depends_on| root_systems_and_weight_lattices
  determinantial_modules -->|related| monoidal_categorification
  determinantial_modules -->|context_for| quiver_hecke_algebra_localization
  lie_algebras_and_hopf_algebras -->|parent_of/prerequisite_for| quantum_groups
  localized_crystals -->|depends_on| cellular_crystals
  localized_crystals -->|depends_on| crystal_bases
  localized_crystals -->|depends_on| quiver_hecke_algebra_localization
  monoidal_categorification -->|parent_of| determinantial_modules
  monoidal_categorification -->|related| quantum_coordinate_rings
  monoidal_categorification -->|depends_on/related| quiver_hecke_algebra_localization
  quantum_coordinate_rings -->|parent_of| determinantial_modules
  quantum_coordinate_rings -->|parent_of| dual_canonical_bases
  quantum_groups -->|parent_of| crystal_bases
  quantum_groups -->|parent_of| quantum_coordinate_rings
  quantum_groups -->|context_for| quiver_hecke_algebras
  quantum_groups -->|depends_on| root_systems_and_weight_lattices
  quiver_hecke_algebra_localization -->|parent_of/supports| localized_crystals
  quiver_hecke_algebras -->|parent_of| determinantial_modules
  quiver_hecke_algebras -->|context_for| monoidal_categorification
  quiver_hecke_algebras -->|parent_of| quiver_hecke_algebra_localization
  root_systems_and_weight_lattices -->|prerequisite_for/supports| crystal_bases
  root_systems_and_weight_lattices -->|prerequisite_for| quantum_groups
  root_systems_and_weight_lattices -->|prerequisite_for| quiver_hecke_algebras
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
