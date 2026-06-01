---
title: Crystal Bases Map
---

```mermaid
flowchart TD
  affine_objects_in_monoidal_categories["Affine Objects in Monoidal Categories"]
  category_localization["Category Localization"]
  cellular_crystals["Cellular Crystals"]
  crystal_bases["Crystal Bases"]
  crystal_comparison_map["Crystal Comparison Map"]
  demazure_subcategories_of_quiver_hecke_modules["Demazure Subcategories of Quiver-Hecke Modules"]
  graded_monoidal_categories["Graded Monoidal Categories"]
  localized_crystals["Localized Crystals"]
  localized_root_operators["Localized Root Operators"]
  normal_sequences["Normal Sequences"]
  pro_categories["Pro-Categories"]
  quantum_groups["Quantum Groups"]
  quasi_rigid_monoidal_categories["Quasi-Rigid Monoidal Categories"]
  quiver_hecke_category_localization["Quiver-Hecke Category Localization"]
  quiver_hecke_subcategories["Quiver-Hecke Subcategories"]
  r_matrix_renormalization["R-Matrix Renormalization"]
  reverse_equivalence_of_localized_categories["Reverse Equivalence of Localized Categories"]
  root_objects_in_localized_categories["Root Objects in Localized Categories"]
  root_systems_and_weight_lattices["Root Systems and Weight Lattices"]
  universal_enveloping_algebras["Universal Enveloping Algebras"]
  affine_objects_in_monoidal_categories -->|prereq| normal_sequences
  affine_objects_in_monoidal_categories -->|prereq| quasi_rigid_monoidal_categories
  affine_objects_in_monoidal_categories -->|related| r_matrix_renormalization
  affine_objects_in_monoidal_categories -->|prereq/related| root_objects_in_localized_categories
  category_localization -->|parent/prereq| quiver_hecke_category_localization
  cellular_crystals -->|prereq| crystal_comparison_map
  cellular_crystals -->|prereq/related| localized_crystals
  crystal_bases -->|parent/prereq| cellular_crystals
  crystal_bases -->|prereq| demazure_subcategories_of_quiver_hecke_modules
  crystal_bases -->|parent/prereq| localized_crystals
  crystal_comparison_map -->|related| crystal_bases
  demazure_subcategories_of_quiver_hecke_modules -->|related| cellular_crystals
  demazure_subcategories_of_quiver_hecke_modules -->|prereq| crystal_comparison_map
  demazure_subcategories_of_quiver_hecke_modules -->|related| localized_crystals
  graded_monoidal_categories -->|parent/prereq| affine_objects_in_monoidal_categories
  graded_monoidal_categories -->|related| localized_crystals
  graded_monoidal_categories -->|parent| quasi_rigid_monoidal_categories
  graded_monoidal_categories -->|parent/prereq| r_matrix_renormalization
  localized_crystals -->|parent| crystal_comparison_map
  localized_crystals -->|parent| localized_root_operators
  localized_root_operators -->|related| cellular_crystals
  localized_root_operators -->|prereq| crystal_comparison_map
  normal_sequences -->|context_for/related| localized_root_operators
  normal_sequences -->|context_for/related| root_objects_in_localized_categories
  pro_categories -->|parent/prereq| affine_objects_in_monoidal_categories
  pro_categories -->|related| category_localization
  quantum_groups -->|parent/prereq| crystal_bases
  quasi_rigid_monoidal_categories -->|related| localized_crystals
  quasi_rigid_monoidal_categories -->|parent| root_objects_in_localized_categories
  quiver_hecke_category_localization -->|prereq| crystal_comparison_map
  quiver_hecke_category_localization -->|parent/prereq| localized_crystals
  quiver_hecke_category_localization -->|prereq| localized_root_operators
  quiver_hecke_category_localization -->|parent/prereq| reverse_equivalence_of_localized_categories
  quiver_hecke_category_localization -->|parent/prereq| root_objects_in_localized_categories
  quiver_hecke_subcategories -->|parent/prereq| demazure_subcategories_of_quiver_hecke_modules
  quiver_hecke_subcategories -->|parent/prereq| quiver_hecke_category_localization
  r_matrix_renormalization -->|related| affine_objects_in_monoidal_categories
  r_matrix_renormalization -->|prereq| localized_root_operators
  r_matrix_renormalization -->|parent/prereq| normal_sequences
  r_matrix_renormalization -->|prereq| quasi_rigid_monoidal_categories
  r_matrix_renormalization -->|prereq/related| root_objects_in_localized_categories
  reverse_equivalence_of_localized_categories -->|related| localized_crystals
  root_objects_in_localized_categories -->|related| localized_crystals
  root_objects_in_localized_categories -->|parent/prereq| localized_root_operators
  root_systems_and_weight_lattices -->|prereq| cellular_crystals
  root_systems_and_weight_lattices -->|prereq/related| crystal_bases
  root_systems_and_weight_lattices -->|prereq/related| quantum_groups
  root_systems_and_weight_lattices -->|related| universal_enveloping_algebras
  universal_enveloping_algebras -->|parent/prereq| quantum_groups
  universal_enveloping_algebras -->|related| root_systems_and_weight_lattices
```

## Topics

- [[topics/affine-objects-in-monoidal-categories|Affine Objects in Monoidal Categories]]
- [[topics/category-localization|Category Localization]]
- [[topics/cellular-crystals|Cellular Crystals]]
- [[topics/crystal-bases|Crystal Bases]]
- [[topics/crystal-comparison-map|Crystal Comparison Map]]
- [[topics/demazure-subcategories-of-quiver-hecke-modules|Demazure Subcategories of Quiver-Hecke Modules]]
- [[topics/graded-monoidal-categories|Graded Monoidal Categories]]
- [[topics/localized-crystals|Localized Crystals]]
- [[topics/localized-root-operators|Localized Root Operators]]
- [[topics/normal-sequences|Normal Sequences]]
- [[topics/pro-categories|Pro-Categories]]
- [[topics/quantum-groups|Quantum Groups]]
- [[topics/quasi-rigid-monoidal-categories|Quasi-Rigid Monoidal Categories]]
- [[topics/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]
- [[topics/quiver-hecke-subcategories|Quiver-Hecke Subcategories]]
- [[topics/r-matrix-renormalization|R-Matrix Renormalization]]
- [[topics/reverse-equivalence-of-localized-categories|Reverse Equivalence of Localized Categories]]
- [[topics/root-objects-in-localized-categories|Root Objects in Localized Categories]]
- [[topics/root-systems-and-weight-lattices|Root Systems and Weight Lattices]]
- [[topics/universal-enveloping-algebras|Universal Enveloping Algebras]]
