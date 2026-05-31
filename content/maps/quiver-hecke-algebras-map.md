---
title: Quiver-Hecke Algebras Map
---

# Quiver-Hecke Algebras Map

```mermaid
flowchart TD
  determinantial_modules["Determinantial Modules"]
  localized_crystals["Localized Crystals"]
  monoidal_categorification["Monoidal Categorification"]
  quantum_coordinate_rings["Quantum Coordinate Rings"]
  quiver_hecke_algebra_localization["Quiver-Hecke Algebra Localization"]
  quiver_hecke_algebras["Quiver-Hecke Algebras"]
  determinantial_modules -->|prereq/context_for/related| quiver_hecke_algebra_localization
  localized_crystals -->|related| monoidal_categorification
  monoidal_categorification -->|parent/prereq| determinantial_modules
  monoidal_categorification -->|related| localized_crystals
  monoidal_categorification -->|prereq/related| quiver_hecke_algebra_localization
  monoidal_categorification -->|related| quiver_hecke_algebras
  quantum_coordinate_rings -->|parent/prereq| determinantial_modules
  quantum_coordinate_rings -->|prereq/related| monoidal_categorification
  quantum_coordinate_rings -->|related| quiver_hecke_algebra_localization
  quiver_hecke_algebra_localization -->|parent/prereq| localized_crystals
  quiver_hecke_algebra_localization -->|related| quantum_coordinate_rings
  quiver_hecke_algebras -->|parent/prereq| determinantial_modules
  quiver_hecke_algebras -->|context_for/related| monoidal_categorification
  quiver_hecke_algebras -->|parent/prereq| quiver_hecke_algebra_localization
```

## Topics

- [[topics/determinantial-modules|Determinantial Modules]]
- [[topics/localized-crystals|Localized Crystals]]
- [[topics/monoidal-categorification|Monoidal Categorification]]
- [[topics/quantum-coordinate-rings|Quantum Coordinate Rings]]
- [[topics/quiver-hecke-algebra-localization|Quiver-Hecke Algebra Localization]]
- [[topics/quiver-hecke-algebras|Quiver-Hecke Algebras]]
