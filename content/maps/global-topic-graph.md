---
title: Global Topic Graph
---

```mermaid
flowchart TD
  affine_objects_in_monoidal_categories["Affine Objects in Monoidal Categories"]
  category_localization["Category Localization"]
  cellular_crystals["Cellular Crystals"]
  crystal_bases["Crystal Bases"]
  crystal_comparison_map["Crystal Comparison Map"]
  demazure_subcategories_of_quiver_hecke_modules["Demazure Subcategories of Quiver-Hecke Modules"]
  determinantial_modules["Determinantial Modules"]
  dual_canonical_bases["Dual Canonical Bases"]
  graded_monoidal_categories["Graded Monoidal Categories"]
  head_simplicity_of_convolutions["Head Simplicity of Convolutions"]
  localized_crystals["Localized Crystals"]
  localized_root_operators["Localized Root Operators"]
  monoidal_categorification["Monoidal Categorification"]
  normal_sequences["Normal Sequences"]
  pro_categories["Pro-Categories"]
  quantum_coordinate_rings["Quantum Coordinate Rings"]
  quantum_groups["Quantum Groups"]
  quasi_rigid_monoidal_categories["Quasi-Rigid Monoidal Categories"]
  quiver_hecke_algebras["Quiver-Hecke Algebras"]
  quiver_hecke_category_localization["Quiver-Hecke Category Localization"]
  quiver_hecke_module_categories["Quiver-Hecke Module Categories"]
  quiver_hecke_subcategories["Quiver-Hecke Subcategories"]
  r_matrix_renormalization["R-Matrix Renormalization"]
  reverse_equivalence_of_localized_categories["Reverse Equivalence of Localized Categories"]
  root_objects_in_localized_categories["Root Objects in Localized Categories"]
  root_systems_and_weight_lattices["Root Systems and Weight Lattices"]
  shuffle_lemmas_for_quiver_hecke_modules["Shuffle Lemmas for Quiver-Hecke Modules"]
  universal_enveloping_algebras["Universal Enveloping Algebras"]
  affine_objects_in_monoidal_categories -->|prerequisite_for| normal_sequences
  affine_objects_in_monoidal_categories -->|prerequisite_for| root_objects_in_localized_categories
  category_localization -->|parent_of/prerequisite_for| quiver_hecke_category_localization
  cellular_crystals -->|depends_on| crystal_bases
  cellular_crystals -->|prerequisite_for| crystal_comparison_map
  cellular_crystals -->|prerequisite_for| localized_crystals
  cellular_crystals -->|related| monoidal_categorification
  crystal_bases -->|parent_of/supports| cellular_crystals
  crystal_bases -->|prerequisite_for| demazure_subcategories_of_quiver_hecke_modules
  crystal_bases -->|parent_of| localized_crystals
  crystal_bases -->|depends_on| quantum_groups
  crystal_bases -->|depends_on| root_systems_and_weight_lattices
  determinantial_modules -->|related| monoidal_categorification
  determinantial_modules -->|context_for| quiver_hecke_category_localization
  graded_monoidal_categories -->|parent_of| affine_objects_in_monoidal_categories
  graded_monoidal_categories -->|parent_of| quasi_rigid_monoidal_categories
  graded_monoidal_categories -->|parent_of| r_matrix_renormalization
  head_simplicity_of_convolutions -->|context_for| localized_root_operators
  localized_crystals -->|depends_on| cellular_crystals
  localized_crystals -->|depends_on| crystal_bases
  localized_crystals -->|parent_of| crystal_comparison_map
  localized_crystals -->|parent_of| localized_root_operators
  localized_crystals -->|depends_on| quiver_hecke_category_localization
  localized_root_operators -->|prerequisite_for| crystal_comparison_map
  monoidal_categorification -->|parent_of| determinantial_modules
  monoidal_categorification -->|parent_of| graded_monoidal_categories
  monoidal_categorification -->|related| quantum_coordinate_rings
  monoidal_categorification -->|depends_on/related| quiver_hecke_category_localization
  normal_sequences -->|parent_of| head_simplicity_of_convolutions
  normal_sequences -->|context_for| localized_root_operators
  normal_sequences -->|context_for| root_objects_in_localized_categories
  normal_sequences -->|prerequisite_for| shuffle_lemmas_for_quiver_hecke_modules
  pro_categories -->|parent_of| affine_objects_in_monoidal_categories
  quantum_coordinate_rings -->|parent_of| determinantial_modules
  quantum_coordinate_rings -->|parent_of| dual_canonical_bases
  quantum_groups -->|parent_of| crystal_bases
  quantum_groups -->|parent_of| quantum_coordinate_rings
  quantum_groups -->|context_for| quiver_hecke_algebras
  quantum_groups -->|depends_on| root_systems_and_weight_lattices
  quasi_rigid_monoidal_categories -->|parent_of| root_objects_in_localized_categories
  quiver_hecke_algebras -->|context_for| monoidal_categorification
  quiver_hecke_algebras -->|parent_of/prerequisite_for| quiver_hecke_module_categories
  quiver_hecke_category_localization -->|prerequisite_for| crystal_comparison_map
  quiver_hecke_category_localization -->|parent_of/supports| localized_crystals
  quiver_hecke_category_localization -->|parent_of| reverse_equivalence_of_localized_categories
  quiver_hecke_category_localization -->|parent_of| root_objects_in_localized_categories
  quiver_hecke_module_categories -->|prerequisite_for| graded_monoidal_categories
  quiver_hecke_module_categories -->|parent_of| head_simplicity_of_convolutions
  quiver_hecke_module_categories -->|prerequisite_for| monoidal_categorification
  quiver_hecke_module_categories -->|parent_of/prerequisite_for| quiver_hecke_subcategories
  quiver_hecke_module_categories -->|parent_of| r_matrix_renormalization
  quiver_hecke_module_categories -->|parent_of| shuffle_lemmas_for_quiver_hecke_modules
  quiver_hecke_subcategories -->|parent_of| demazure_subcategories_of_quiver_hecke_modules
  quiver_hecke_subcategories -->|parent_of/prerequisite_for| determinantial_modules
  quiver_hecke_subcategories -->|parent_of/prerequisite_for| quiver_hecke_category_localization
  r_matrix_renormalization -->|prerequisite_for| head_simplicity_of_convolutions
  r_matrix_renormalization -->|prerequisite_for| localized_root_operators
  r_matrix_renormalization -->|parent_of/prerequisite_for| normal_sequences
  r_matrix_renormalization -->|prerequisite_for| quasi_rigid_monoidal_categories
  r_matrix_renormalization -->|prerequisite_for| root_objects_in_localized_categories
  root_objects_in_localized_categories -->|parent_of| localized_root_operators
  root_systems_and_weight_lattices -->|prerequisite_for/supports| crystal_bases
  root_systems_and_weight_lattices -->|prerequisite_for| quantum_groups
  root_systems_and_weight_lattices -->|prerequisite_for| quiver_hecke_algebras
  universal_enveloping_algebras -->|parent_of/prerequisite_for| quantum_groups
```

## Topics

- [[topics/affine-objects-in-monoidal-categories|Affine Objects in Monoidal Categories]]
- [[topics/category-localization|Category Localization]]
- [[topics/cellular-crystals|Cellular Crystals]]
- [[topics/crystal-bases|Crystal Bases]]
- [[topics/crystal-comparison-map|Crystal Comparison Map]]
- [[topics/demazure-subcategories-of-quiver-hecke-modules|Demazure Subcategories of Quiver-Hecke Modules]]
- [[topics/determinantial-modules|Determinantial Modules]]
- [[topics/dual-canonical-bases|Dual Canonical Bases]]
- [[topics/graded-monoidal-categories|Graded Monoidal Categories]]
- [[topics/head-simplicity-of-convolutions|Head Simplicity of Convolutions]]
- [[topics/localized-crystals|Localized Crystals]]
- [[topics/localized-root-operators|Localized Root Operators]]
- [[topics/monoidal-categorification|Monoidal Categorification]]
- [[topics/normal-sequences|Normal Sequences]]
- [[topics/pro-categories|Pro-Categories]]
- [[topics/quantum-coordinate-rings|Quantum Coordinate Rings]]
- [[topics/quantum-groups|Quantum Groups]]
- [[topics/quasi-rigid-monoidal-categories|Quasi-Rigid Monoidal Categories]]
- [[topics/quiver-hecke-algebras|Quiver-Hecke Algebras]]
- [[topics/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]
- [[topics/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]
- [[topics/quiver-hecke-subcategories|Quiver-Hecke Subcategories]]
- [[topics/r-matrix-renormalization|R-Matrix Renormalization]]
- [[topics/reverse-equivalence-of-localized-categories|Reverse Equivalence of Localized Categories]]
- [[topics/root-objects-in-localized-categories|Root Objects in Localized Categories]]
- [[topics/root-systems-and-weight-lattices|Root Systems and Weight Lattices]]
- [[topics/shuffle-lemmas-for-quiver-hecke-modules|Shuffle Lemmas for Quiver-Hecke Modules]]
- [[topics/universal-enveloping-algebras|Universal Enveloping Algebras]]
