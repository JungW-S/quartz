import { loadQuartzConfig, loadQuartzLayout } from "./quartz/plugins/loader/config-loader"
import { componentRegistry } from "./quartz/components/registry"
import * as ExternalPlugin from "./.quartz/plugins"

interface ExplorerNode {
  slugSegment?: string
  displayName?: string
  isFolder: boolean
}

interface FolderPageEntry {
  slug?: string
  dates?: {
    created?: Date
    modified?: Date
    published?: Date
  }
  frontmatter?: {
    title?: string
  }
}

const topicOrder: Record<string, number> = {
  "quantum-groups": 10,
  "universal-enveloping-algebras": 20,
  "root-systems-and-weight-lattices": 30,
  "lie-algebra-representations": 40,
  "weight-modules": 50,
  "highest-weight-modules": 60,
  "characters-of-representations": 70,
  "quantum-coordinate-rings": 80,
  "dual-canonical-bases": 90,
  "category-o": 100,
  "verma-modules": 110,
  "root-of-unity-quantum-groups": 120,
  "integral-forms-of-quantum-groups": 130,
  "universal-r-matrix": 140,
  "yang-baxter-equation": 145,
  "crystal-bases": 110,
  "abstract-crystals": 120,
  "tensor-products-of-crystals": 130,
  "highest-weight-crystals": 140,
  "b-infinity-crystal": 150,
  "demazure-crystals": 160,
  "cellular-crystals": 170,
  "category-theory": 210,
  "pro-categories": 220,
  "graded-monoidal-categories": 230,
  "affine-objects-in-monoidal-categories": 240,
  "quasi-rigid-monoidal-categories": 250,
  "cluster-algebras": 310,
  "quantum-cluster-algebras": 320,
  "monoidal-categorification": 410,
  "quiver-hecke-algebras": 510,
  "quiver-hecke-module-categories": 520,
  "quiver-hecke-subcategories": 530,
  "demazure-subcategories-of-quiver-hecke-modules": 540,
  "determinantial-modules": 550,
  "r-matrix-renormalization": 560,
  "normal-sequences": 570,
  "head-simplicity-of-convolutions": 580,
  "shuffle-lemmas-for-quiver-hecke-modules": 590,
  "quantum-affine-algebras": 610,
  "category-localization": 710,
  "quiver-hecke-category-localization": 720,
  "localized-crystals": 730,
  "localized-root-operators": 740,
  "root-objects-in-localized-categories": 750,
  "reverse-equivalence-of-localized-categories": 760,
}

function slugSegment(slug?: string): string {
  return (slug ?? "").replace(/\/index$/, "").split("/").at(-1) ?? ""
}

function entryDateTime(entry: FolderPageEntry): number | undefined {
  const date = entry.dates?.modified ?? entry.dates?.published ?? entry.dates?.created
  return date?.getTime()
}

function sortTopicEntries(a: FolderPageEntry, b: FolderPageEntry): number {
  const aSegment = slugSegment(a.slug)
  const bSegment = slugSegment(b.slug)
  const aNumbered = aSegment.match(/^(\d+)-/)
  const bNumbered = bSegment.match(/^(\d+)-/)
  const aTopicOrder = topicOrder[aSegment]
  const bTopicOrder = topicOrder[bSegment]

  if (aNumbered && bNumbered) {
    const byNumber = Number(aNumbered[1]) - Number(bNumbered[1])
    if (byNumber !== 0) {
      return byNumber
    }
  }

  if (aNumbered || bNumbered) {
    return aNumbered ? -1 : 1
  }

  if (aTopicOrder !== undefined && bTopicOrder !== undefined) {
    const byTopicOrder = aTopicOrder - bTopicOrder
    if (byTopicOrder !== 0) {
      return byTopicOrder
    }
  }

  if (aTopicOrder !== undefined || bTopicOrder !== undefined) {
    return aTopicOrder !== undefined ? -1 : 1
  }

  const aTime = entryDateTime(a)
  const bTime = entryDateTime(b)

  if (aTime !== undefined && bTime !== undefined) {
    const byDate = bTime - aTime
    if (byDate !== 0) {
      return byDate
    }
  }

  if (aTime !== undefined || bTime !== undefined) {
    return aTime !== undefined ? -1 : 1
  }

  return (a.frontmatter?.title ?? "").localeCompare(b.frontmatter?.title ?? "", undefined, {
    numeric: true,
    sensitivity: "base",
  })
}

componentRegistry.setOptionOverrides("folder-page", {
  sort: sortTopicEntries,
})

ExternalPlugin.Explorer({
  sortFn: (a: ExplorerNode, b: ExplorerNode) => {
    if (a.isFolder !== b.isFolder) {
      return a.isFolder ? -1 : 1
    }

    const aSegment = a.slugSegment ?? ""
    const bSegment = b.slugSegment ?? ""
    const aNumbered = aSegment.match(/^(\d+)-/)
    const bNumbered = bSegment.match(/^(\d+)-/)
    const topicOrder: Record<string, number> = {
      "quantum-groups": 10,
      "universal-enveloping-algebras": 20,
      "root-systems-and-weight-lattices": 30,
      "lie-algebra-representations": 40,
      "weight-modules": 50,
      "highest-weight-modules": 60,
      "characters-of-representations": 70,
      "quantum-coordinate-rings": 80,
      "dual-canonical-bases": 90,
      "category-o": 100,
      "verma-modules": 110,
      "root-of-unity-quantum-groups": 120,
      "integral-forms-of-quantum-groups": 130,
      "universal-r-matrix": 140,
      "yang-baxter-equation": 145,
      "crystal-bases": 110,
      "abstract-crystals": 120,
      "tensor-products-of-crystals": 130,
      "highest-weight-crystals": 140,
      "b-infinity-crystal": 150,
      "demazure-crystals": 160,
      "cellular-crystals": 170,
      "category-theory": 210,
      "pro-categories": 220,
      "graded-monoidal-categories": 230,
      "affine-objects-in-monoidal-categories": 240,
      "quasi-rigid-monoidal-categories": 250,
      "cluster-algebras": 310,
      "quantum-cluster-algebras": 320,
      "monoidal-categorification": 410,
      "quiver-hecke-algebras": 510,
      "quiver-hecke-module-categories": 520,
      "quiver-hecke-subcategories": 530,
      "demazure-subcategories-of-quiver-hecke-modules": 540,
      "determinantial-modules": 550,
      "r-matrix-renormalization": 560,
      "normal-sequences": 570,
      "head-simplicity-of-convolutions": 580,
      "shuffle-lemmas-for-quiver-hecke-modules": 590,
      "quantum-affine-algebras": 610,
      "category-localization": 710,
      "quiver-hecke-category-localization": 720,
      "localized-crystals": 730,
      "localized-root-operators": 740,
      "root-objects-in-localized-categories": 750,
      "reverse-equivalence-of-localized-categories": 760,
    }
    const aTopicOrder = topicOrder[aSegment]
    const bTopicOrder = topicOrder[bSegment]

    if (aNumbered && bNumbered) {
      const byNumber = Number(aNumbered[1]) - Number(bNumbered[1])
      if (byNumber !== 0) {
        return byNumber
      }
    }

    if (aNumbered || bNumbered) {
      return aNumbered ? -1 : 1
    }

    if (aTopicOrder !== undefined && bTopicOrder !== undefined) {
      const byTopicOrder = aTopicOrder - bTopicOrder
      if (byTopicOrder !== 0) {
        return byTopicOrder
      }
    }

    if (aTopicOrder !== undefined || bTopicOrder !== undefined) {
      return aTopicOrder !== undefined ? -1 : 1
    }

    return (a.displayName ?? "").localeCompare(b.displayName ?? "", undefined, {
      numeric: true,
      sensitivity: "base",
    })
  },
})

const config = await loadQuartzConfig()
export default config
export const layout = await loadQuartzLayout()
