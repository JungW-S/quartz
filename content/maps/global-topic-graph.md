---
title: Global Topic Graph
---

```mermaid
flowchart TD
  abstract_crystals["Abstract Crystals"]
  affine_cuspidal_modules["Affine Cuspidal Modules"]
  affine_objects_in_monoidal_categories["Affine Objects in Monoidal Categories"]
  b_infinity_crystal["The Crystal B(infinity)"]
  category_localization["Localization of Categories"]
  category_o["Quantum Category O"]
  category_theory["Category Theory"]
  cellular_crystals["Cellular Crystals"]
  characters_of_representations["Characters of Representations"]
  cluster_algebras["Cluster Algebras"]
  coordinate_formulas_for_quantum_twist_on_localized_crystals["Coordinate Formulas for Quantum Twist on Localized Crystals"]
  crystal_bases["Crystal Bases"]
  demazure_crystals["Demazure Crystals"]
  demazure_subcategories_of_quiver_hecke_modules["Demazure Subcategories of Quiver-Hecke Modules"]
  determinantial_modules["Determinantial Modules"]
  dual_canonical_bases["Dual Canonical Bases"]
  graded_monoidal_categories["Graded Monoidal Categories"]
  grothendieck_rings_of_monoidal_categories["Grothendieck Rings of Monoidal Categories"]
  head_simplicity_of_convolutions["Head Simplicity of Convolutions"]
  hernandez_leclerc_categories["Hernandez-Leclerc Categories"]
  highest_weight_crystals["Highest Weight Crystals"]
  highest_weight_modules["Highest-Weight Modules"]
  integral_forms_of_quantum_groups["Integral Forms of Quantum Groups"]
  left_and_right_g_vectors["Left and Right g-Vectors"]
  lie_algebra_representations["Lie Algebra Representations"]
  localized_crystals["Localized Crystals"]
  localized_pbw_parametrizations["Localized PBW Parametrizations"]
  localized_root_operators["Localized Root Operators"]
  localized_string_parametrizations["Localized String Parametrizations"]
  monoidal_categorification["Monoidal Categorification"]
  normal_sequences["Normal Sequences"]
  pbw_parametrizations_of_quantum_unipotent_coordinate_rings["PBW Parametrizations of Quantum Unipotent Coordinate Rings"]
  pbw_theory_for_quantum_affine_algebras["PBW Theory for Quantum Affine Algebras"]
  pro_categories["Pro-Categories"]
  q_characters_and_l_weights["q-Characters and l-Weights"]
  quantum_affine_algebras["Quantum Affine Algebras"]
  quantum_affine_r_matrix_denominators["Quantum Affine R-Matrix Denominators"]
  quantum_affine_schur_weyl_duality["Quantum Affine Schur-Weyl Duality"]
  quantum_cluster_algebras["Quantum Cluster Algebras"]
  quantum_coordinate_rings["Quantum Coordinate Rings"]
  quantum_groups["Quantum Groups"]
  quantum_minors_and_frozen_variables["Quantum Minors and Frozen Variables"]
  quantum_twist_automorphisms["Quantum Twist Automorphisms"]
  quantum_unipotent_coordinate_rings["Quantum Unipotent Coordinate Rings"]
  quasi_rigid_monoidal_categories["Quasi-Rigid Monoidal Categories"]
  quiver_hecke_algebras["Quiver-Hecke Algebras"]
  quiver_hecke_category_localization["Quiver-Hecke Category Localization"]
  quiver_hecke_module_categories["Quiver-Hecke Module Categories"]
  quiver_hecke_subcategories["Quiver-Hecke Subcategories"]
  r_matrix_renormalization["R-Matrix Renormalization"]
  reverse_equivalence_of_localized_categories["Reverse Equivalence of Localized Categories"]
  root_objects_in_localized_categories["Root Objects in Localized Categories"]
  root_of_unity_quantum_groups["Root-of-Unity Quantum Groups"]
  root_systems_and_weight_lattices["Root Systems and Weight Lattices"]
  shuffle_lemmas_for_quiver_hecke_modules["Shuffle Lemmas for Quiver-Hecke Modules"]
  string_parametrizations_of_demazure_crystals["String Parametrizations of Demazure Crystals"]
  tensor_products_of_crystals["Tensor Products of Crystals"]
  type_a_klr_segment_modules["Type A KLR Segment Modules"]
  type_a_segment_module_convolutions["Type A Segment Module Convolutions"]
  universal_enveloping_algebras["Universal Enveloping Algebras"]
  universal_r_matrix["Universal R-Matrix"]
  verma_modules["Verma Modules"]
  weight_modules["Weight Modules"]
  yang_baxter_equation["Yang-Baxter Equation"]
  abstract_crystals -->|prerequisite_for| string_parametrizations_of_demazure_crystals
  abstract_crystals -->|prerequisite_for| tensor_products_of_crystals
  affine_objects_in_monoidal_categories -->|prerequisite_for| normal_sequences
  affine_objects_in_monoidal_categories -->|prerequisite_for| quantum_affine_r_matrix_denominators
  affine_objects_in_monoidal_categories -->|prerequisite_for| quantum_affine_schur_weyl_duality
  affine_objects_in_monoidal_categories -->|prerequisite_for| root_objects_in_localized_categories
  b_infinity_crystal -->|parent_of/prerequisite_for| demazure_crystals
  b_infinity_crystal -->|prerequisite_for| string_parametrizations_of_demazure_crystals
  category_localization -->|parent_of/prerequisite_for| quiver_hecke_category_localization
  category_o -->|parent_of/context_for| verma_modules
  category_theory -->|parent_of| category_localization
  category_theory -->|parent_of| graded_monoidal_categories
  category_theory -->|parent_of| pro_categories
  cellular_crystals -->|depends_on| crystal_bases
  cellular_crystals -->|prerequisite_for| localized_crystals
  cellular_crystals -->|related| monoidal_categorification
  cluster_algebras -->|prerequisite_for| hernandez_leclerc_categories
  cluster_algebras -->|prerequisite_for| monoidal_categorification
  cluster_algebras -->|parent_of| quantum_cluster_algebras
  crystal_bases -->|parent_of| abstract_crystals
  crystal_bases -->|parent_of| b_infinity_crystal
  crystal_bases -->|parent_of/supports| cellular_crystals
  crystal_bases -->|parent_of| demazure_crystals
  crystal_bases -->|parent_of| highest_weight_crystals
  crystal_bases -->|context_for| localized_crystals
  crystal_bases -->|depends_on| quantum_groups
  crystal_bases -->|depends_on| root_systems_and_weight_lattices
  crystal_bases -->|parent_of| string_parametrizations_of_demazure_crystals
  crystal_bases -->|parent_of| tensor_products_of_crystals
  demazure_crystals -->|prerequisite_for| cellular_crystals
  demazure_crystals -->|prerequisite_for| demazure_subcategories_of_quiver_hecke_modules
  demazure_crystals -->|parent_of/prerequisite_for| string_parametrizations_of_demazure_crystals
  demazure_subcategories_of_quiver_hecke_modules -->|prerequisite_for| localized_crystals
  determinantial_modules -->|prerequisite_for| left_and_right_g_vectors
  determinantial_modules -->|related| monoidal_categorification
  determinantial_modules -->|context_for| quiver_hecke_category_localization
  dual_canonical_bases -->|prerequisite_for| quantum_minors_and_frozen_variables
  graded_monoidal_categories -->|parent_of| affine_objects_in_monoidal_categories
  graded_monoidal_categories -->|context_for| monoidal_categorification
  graded_monoidal_categories -->|parent_of| quasi_rigid_monoidal_categories
  graded_monoidal_categories -->|context_for| quiver_hecke_module_categories
  graded_monoidal_categories -->|parent_of| r_matrix_renormalization
  head_simplicity_of_convolutions -->|context_for| localized_root_operators
  head_simplicity_of_convolutions -->|prerequisite_for| shuffle_lemmas_for_quiver_hecke_modules
  hernandez_leclerc_categories -->|prerequisite_for| quantum_affine_schur_weyl_duality
  hernandez_leclerc_categories -->|context_for| quiver_hecke_module_categories
  highest_weight_modules -->|prerequisite_for| verma_modules
  left_and_right_g_vectors -->|prerequisite_for| coordinate_formulas_for_quantum_twist_on_localized_crystals
  localized_crystals -->|depends_on| cellular_crystals
  localized_crystals -->|prerequisite_for| coordinate_formulas_for_quantum_twist_on_localized_crystals
  localized_crystals -->|depends_on| crystal_bases
  localized_crystals -->|prerequisite_for| left_and_right_g_vectors
  localized_crystals -->|parent_of| localized_root_operators
  localized_crystals -->|depends_on| quiver_hecke_category_localization
  localized_pbw_parametrizations -->|prerequisite_for| coordinate_formulas_for_quantum_twist_on_localized_crystals
  localized_pbw_parametrizations -->|prerequisite_for| left_and_right_g_vectors
  localized_string_parametrizations -->|prerequisite_for| coordinate_formulas_for_quantum_twist_on_localized_crystals
  localized_string_parametrizations -->|prerequisite_for| left_and_right_g_vectors
  monoidal_categorification -->|parent_of| determinantial_modules
  monoidal_categorification -->|context_for| hernandez_leclerc_categories
  monoidal_categorification -->|related| quantum_coordinate_rings
  monoidal_categorification -->|depends_on/related| quiver_hecke_category_localization
  normal_sequences -->|parent_of| head_simplicity_of_convolutions
  normal_sequences -->|context_for| localized_root_operators
  normal_sequences -->|context_for| root_objects_in_localized_categories
  normal_sequences -->|prerequisite_for| shuffle_lemmas_for_quiver_hecke_modules
  pbw_parametrizations_of_quantum_unipotent_coordinate_rings -->|prerequisite_for| localized_pbw_parametrizations
  pbw_parametrizations_of_quantum_unipotent_coordinate_rings -->|child_of| quantum_unipotent_coordinate_rings
  pro_categories -->|parent_of| affine_objects_in_monoidal_categories
  quantum_affine_algebras -->|parent_of/prerequisite_for| hernandez_leclerc_categories
  quantum_affine_algebras -->|context_for| monoidal_categorification
  quantum_affine_algebras -->|parent_of/prerequisite_for| quantum_affine_r_matrix_denominators
  quantum_affine_algebras -->|parent_of/prerequisite_for| quantum_affine_schur_weyl_duality
  quantum_affine_algebras -->|context_for| quiver_hecke_module_categories
  quantum_affine_r_matrix_denominators -->|prerequisite_for| quantum_affine_schur_weyl_duality
  quantum_affine_r_matrix_denominators -->|context_for| type_a_klr_segment_modules
  quantum_affine_schur_weyl_duality -->|context_for| monoidal_categorification
  quantum_cluster_algebras -->|prerequisite_for| left_and_right_g_vectors
  quantum_cluster_algebras -->|prerequisite_for| monoidal_categorification
  quantum_cluster_algebras -->|context_for| quantum_coordinate_rings
  quantum_cluster_algebras -->|context_for| quantum_minors_and_frozen_variables
  quantum_coordinate_rings -->|parent_of| determinantial_modules
  quantum_coordinate_rings -->|parent_of| dual_canonical_bases
  quantum_coordinate_rings -->|parent_of| quantum_unipotent_coordinate_rings
  quantum_groups -->|parent_of| crystal_bases
  quantum_groups -->|prerequisite_for| quantum_affine_algebras
  quantum_groups -->|parent_of| quantum_coordinate_rings
  quantum_groups -->|context_for| quiver_hecke_algebras
  quantum_groups -->|depends_on| root_systems_and_weight_lattices
  quantum_minors_and_frozen_variables -->|prerequisite_for| localized_pbw_parametrizations
  quantum_minors_and_frozen_variables -->|child_of| quantum_unipotent_coordinate_rings
  quantum_twist_automorphisms -->|prerequisite_for| coordinate_formulas_for_quantum_twist_on_localized_crystals
  quantum_unipotent_coordinate_rings -->|parent_of| pbw_parametrizations_of_quantum_unipotent_coordinate_rings
  quantum_unipotent_coordinate_rings -->|child_of| quantum_coordinate_rings
  quantum_unipotent_coordinate_rings -->|parent_of/prerequisite_for| quantum_minors_and_frozen_variables
  quasi_rigid_monoidal_categories -->|parent_of| root_objects_in_localized_categories
  quiver_hecke_algebras -->|context_for| monoidal_categorification
  quiver_hecke_algebras -->|parent_of/prerequisite_for| quiver_hecke_module_categories
  quiver_hecke_algebras -->|prerequisite_for| type_a_klr_segment_modules
  quiver_hecke_category_localization -->|parent_of/supports| localized_crystals
  quiver_hecke_category_localization -->|parent_of| reverse_equivalence_of_localized_categories
  quiver_hecke_category_localization -->|parent_of| root_objects_in_localized_categories
  quiver_hecke_module_categories -->|parent_of| head_simplicity_of_convolutions
  quiver_hecke_module_categories -->|prerequisite_for| monoidal_categorification
  quiver_hecke_module_categories -->|prerequisite_for| quantum_affine_schur_weyl_duality
  quiver_hecke_module_categories -->|parent_of/prerequisite_for| quiver_hecke_subcategories
  quiver_hecke_module_categories -->|parent_of| r_matrix_renormalization
  quiver_hecke_module_categories -->|parent_of| shuffle_lemmas_for_quiver_hecke_modules
  quiver_hecke_module_categories -->|parent_of/prerequisite_for| type_a_klr_segment_modules
  quiver_hecke_module_categories -->|prerequisite_for| type_a_segment_module_convolutions
  quiver_hecke_subcategories -->|parent_of| demazure_subcategories_of_quiver_hecke_modules
  quiver_hecke_subcategories -->|parent_of/prerequisite_for| determinantial_modules
  quiver_hecke_subcategories -->|parent_of/prerequisite_for| quiver_hecke_category_localization
  r_matrix_renormalization -->|prerequisite_for| head_simplicity_of_convolutions
  r_matrix_renormalization -->|prerequisite_for| localized_root_operators
  r_matrix_renormalization -->|parent_of/prerequisite_for| normal_sequences
  r_matrix_renormalization -->|prerequisite_for| quantum_affine_r_matrix_denominators
  r_matrix_renormalization -->|prerequisite_for| quantum_affine_schur_weyl_duality
  r_matrix_renormalization -->|prerequisite_for| quasi_rigid_monoidal_categories
  r_matrix_renormalization -->|prerequisite_for| root_objects_in_localized_categories
  r_matrix_renormalization -->|prerequisite_for| type_a_segment_module_convolutions
  root_objects_in_localized_categories -->|parent_of| localized_root_operators
  root_systems_and_weight_lattices -->|prerequisite_for/supports| crystal_bases
  root_systems_and_weight_lattices -->|prerequisite_for| quantum_groups
  root_systems_and_weight_lattices -->|prerequisite_for| quiver_hecke_algebras
  string_parametrizations_of_demazure_crystals -->|prerequisite_for| localized_string_parametrizations
  tensor_products_of_crystals -->|prerequisite_for| b_infinity_crystal
  tensor_products_of_crystals -->|prerequisite_for| highest_weight_crystals
  type_a_klr_segment_modules -->|prerequisite_for| quantum_affine_schur_weyl_duality
  type_a_klr_segment_modules -->|parent_of/prerequisite_for| type_a_segment_module_convolutions
  type_a_segment_module_convolutions -->|context_for| head_simplicity_of_convolutions
  universal_enveloping_algebras -->|parent_of/prerequisite_for| quantum_groups
  weight_modules -->|prerequisite_for| category_o
  weight_modules -->|prerequisite_for| quantum_affine_algebras
```

## Topics

- [[topics/02-crystal-bases/abstract-crystals|Abstract Crystals]]
- [[topics/07-quantum-affine-algebras/affine-cuspidal-modules|Affine Cuspidal Modules]]
- [[topics/03-category-theory/affine-objects-in-monoidal-categories|Affine Objects in Monoidal Categories]]
- [[topics/02-crystal-bases/b-infinity-crystal|The Crystal B(infinity)]]
- [[topics/08-localization-of-categories/category-localization|Localization of Categories]]
- [[topics/01-quantum-groups/category-o|Quantum Category O]]
- [[topics/03-category-theory/category-theory|Category Theory]]
- [[topics/02-crystal-bases/cellular-crystals|Cellular Crystals]]
- [[topics/01-quantum-groups/characters-of-representations|Characters of Representations]]
- [[topics/04-cluster-algebras/cluster-algebras|Cluster Algebras]]
- [[topics/08-localization-of-categories/coordinate-formulas-for-quantum-twist-on-localized-crystals|Coordinate Formulas for Quantum Twist on Localized Crystals]]
- [[topics/02-crystal-bases/crystal-bases|Crystal Bases]]
- [[topics/02-crystal-bases/demazure-crystals|Demazure Crystals]]
- [[topics/06-quiver-hecke-klr-algebras/demazure-subcategories-of-quiver-hecke-modules|Demazure Subcategories of Quiver-Hecke Modules]]
- [[topics/06-quiver-hecke-klr-algebras/determinantial-modules|Determinantial Modules]]
- [[topics/01-quantum-groups/dual-canonical-bases|Dual Canonical Bases]]
- [[topics/03-category-theory/graded-monoidal-categories|Graded Monoidal Categories]]
- [[topics/05-monoidal-categorification/grothendieck-rings-of-monoidal-categories|Grothendieck Rings of Monoidal Categories]]
- [[topics/06-quiver-hecke-klr-algebras/head-simplicity-of-convolutions|Head Simplicity of Convolutions]]
- [[topics/07-quantum-affine-algebras/hernandez-leclerc-categories|Hernandez-Leclerc Categories]]
- [[topics/02-crystal-bases/highest-weight-crystals|Highest Weight Crystals]]
- [[topics/01-quantum-groups/highest-weight-modules|Highest-Weight Modules]]
- [[topics/01-quantum-groups/integral-forms-of-quantum-groups|Integral Forms of Quantum Groups]]
- [[topics/08-localization-of-categories/left-and-right-g-vectors|Left and Right g-Vectors]]
- [[topics/01-quantum-groups/lie-algebra-representations|Lie Algebra Representations]]
- [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]
- [[topics/08-localization-of-categories/localized-pbw-parametrizations|Localized PBW Parametrizations]]
- [[topics/08-localization-of-categories/localized-root-operators|Localized Root Operators]]
- [[topics/08-localization-of-categories/localized-string-parametrizations|Localized String Parametrizations]]
- [[topics/05-monoidal-categorification/monoidal-categorification|Monoidal Categorification]]
- [[topics/06-quiver-hecke-klr-algebras/normal-sequences|Normal Sequences]]
- [[topics/01-quantum-groups/pbw-parametrizations-of-quantum-unipotent-coordinate-rings|PBW Parametrizations of Quantum Unipotent Coordinate Rings]]
- [[topics/07-quantum-affine-algebras/pbw-theory-for-quantum-affine-algebras|PBW Theory for Quantum Affine Algebras]]
- [[topics/03-category-theory/pro-categories|Pro-Categories]]
- [[topics/07-quantum-affine-algebras/q-characters-and-l-weights|q-Characters and l-Weights]]
- [[topics/07-quantum-affine-algebras/quantum-affine-algebras|Quantum Affine Algebras]]
- [[topics/07-quantum-affine-algebras/quantum-affine-r-matrix-denominators|Quantum Affine R-Matrix Denominators]]
- [[topics/07-quantum-affine-algebras/quantum-affine-schur-weyl-duality|Quantum Affine Schur-Weyl Duality]]
- [[topics/04-cluster-algebras/quantum-cluster-algebras|Quantum Cluster Algebras]]
- [[topics/01-quantum-groups/quantum-coordinate-rings|Quantum Coordinate Rings]]
- [[topics/01-quantum-groups/quantum-groups|Quantum Groups]]
- [[topics/01-quantum-groups/quantum-minors-and-frozen-variables|Quantum Minors and Frozen Variables]]
- [[topics/08-localization-of-categories/quantum-twist-automorphisms|Quantum Twist Automorphisms]]
- [[topics/01-quantum-groups/quantum-unipotent-coordinate-rings|Quantum Unipotent Coordinate Rings]]
- [[topics/03-category-theory/quasi-rigid-monoidal-categories|Quasi-Rigid Monoidal Categories]]
- [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-algebras|Quiver-Hecke Algebras]]
- [[topics/08-localization-of-categories/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]
- [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]
- [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-subcategories|Quiver-Hecke Subcategories]]
- [[topics/06-quiver-hecke-klr-algebras/r-matrix-renormalization|R-Matrix Renormalization]]
- [[topics/08-localization-of-categories/reverse-equivalence-of-localized-categories|Reverse Equivalence of Localized Categories]]
- [[topics/08-localization-of-categories/root-objects-in-localized-categories|Root Objects in Localized Categories]]
- [[topics/01-quantum-groups/root-of-unity-quantum-groups|Root-of-Unity Quantum Groups]]
- [[topics/01-quantum-groups/root-systems-and-weight-lattices|Root Systems and Weight Lattices]]
- [[topics/06-quiver-hecke-klr-algebras/shuffle-lemmas-for-quiver-hecke-modules|Shuffle Lemmas for Quiver-Hecke Modules]]
- [[topics/02-crystal-bases/string-parametrizations-of-demazure-crystals|String Parametrizations of Demazure Crystals]]
- [[topics/02-crystal-bases/tensor-products-of-crystals|Tensor Products of Crystals]]
- [[topics/06-quiver-hecke-klr-algebras/type-a-klr-segment-modules|Type A KLR Segment Modules]]
- [[topics/06-quiver-hecke-klr-algebras/type-a-segment-module-convolutions|Type A Segment Module Convolutions]]
- [[topics/01-quantum-groups/universal-enveloping-algebras|Universal Enveloping Algebras]]
- [[topics/01-quantum-groups/universal-r-matrix|Universal R-Matrix]]
- [[topics/01-quantum-groups/verma-modules|Verma Modules]]
- [[topics/01-quantum-groups/weight-modules|Weight Modules]]
- [[topics/01-quantum-groups/yang-baxter-equation|Yang-Baxter Equation]]
