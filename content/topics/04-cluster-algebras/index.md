---
id: topic-shelf-cluster-algebras
title: Cluster Algebras
level: overview
---

이 장은 cluster algebra language를 큰 단위로 정리한다. Seed, mutation, cluster variables, cluster monomials는 따로 잘게 쪼개지 않고 [[topics/04-cluster-algebras/cluster-algebras|Cluster Algebras]] 한 page 안에서 먼저 읽는다. 그 다음 $q$-commuting variables와 quantum seed가 필요한 곳에서 [[topics/04-cluster-algebras/quantum-cluster-algebras|Quantum Cluster Algebras]]로 넘어간다.

## 읽는 순서

1. [[topics/04-cluster-algebras/cluster-algebras|Cluster Algebras]]

   Cluster algebra의 기본 object는 seed이고, mutation은 seed를 바꾸는 operation이다. 이 page에서 cluster variables, exchange matrix, mutation, cluster monomials를 한 번에 읽는다.

2. [[topics/04-cluster-algebras/quantum-cluster-algebras|Quantum Cluster Algebras]]

   Classical cluster variables가 commutative variables라면, quantum cluster algebra에서는 variables가 prescribed powers of $q$만큼 skew-commute한다. Quantum seed와 quantum mutation은 monoidal categorification과 quantum coordinate rings를 읽기 전에 필요한 language이다.

## 다른 장으로 넘어가는 길

- [[topics/05-monoidal-categorification/monoidal-categorification|Monoidal Categorification]]에서는 cluster variables를 monoidal category의 simple objects와 연결한다.
- [[topics/01-quantum-groups/quantum-coordinate-rings|Quantum Coordinate Rings]]에서는 quantum cluster algebra가 quantum coordinate ring과 만나는 대표적인 방향을 읽는다.
- [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]에서는 monoidal categorification의 categorical objects가 실제로 놓이는 module category를 읽는다.

## 지금은 나누지 않는 내용

Seeds, mutation, cluster monomials는 cluster algebra를 처음 읽는 데 필요한 하나의 묶음이다. 따라서 이 장에서는 이들을 별도 topic으로 나누지 않고, classical page 안에서 먼저 익힌다. 더 세밀한 분리는 나중에 예시나 계산이 충분히 쌓였을 때 하는 것이 낫다.
