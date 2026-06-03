# S2_dimension_structure.md

## Formula

```text
S₂ = Axis Selection → Boundary Selection → Dimension Split
```

## Inner formula

```text
S₂_inner(ㆍ, ㅇ | A) = Coord_A(ㅇ - ㆍ)
```

## State table

```text
A = ∅  → difficult
A ≠ ∅ → difference
B = ∅  → same dimension
B ≠ ∅ → inside / outside → dimension split
```

## Role

S₂는 Y_Branch의 핵심 차원구조연산식이다.

11회차 Brake Test에서 가장 안정적으로 통과했다.

## Guard

Axis와 boundary를 혼동하지 않는다.

```text
A = 차이를 드러내는 기준축
B = inside/outside를 나누는 경계
```
