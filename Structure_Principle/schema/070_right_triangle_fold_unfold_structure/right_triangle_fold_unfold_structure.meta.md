---
id: schema.070.right_triangle_fold_unfold_structure
type: active_schema_metadata
filename: right_triangle_fold_unfold_structure.meta.md
directory: 070_right_triangle_fold_unfold_structure
status: active_draft
prev: schema.069.ddx_right_triangle_transition
---

# META: right_triangle_fold_unfold_structure

## role
right_triangle_fold_unfold_structure는 45-45-90 직각삼각이 fold/unfold를 통해 하나의 칸 공을 형성하는 구조를 정의하는 schema이다.

이 meta 파일은 인공지능이 삼각을 단순 면적 조각으로만 보지 않고, 한 칸 공을 점유하는 자리상태로 읽기 위한 기준이다.

## core

```text
현재 삼각 = 45-45-90 직각삼각
정삼각 = 60도 삼각대칭
직각삼각 1/2 + 직각삼각 1/2 = 한 칸 공
```

## definition

현재 구조원리에서 사용되는 삼각은 정삼각이 아니라 45-45-90 직각삼각의 fold_unfold 구조다.

수학적 도형개념에서는 직각삼각이 사각의 절반 면적일 수 있다.

하지만 자리개념에서는 삼각이 사각의 일부 공간을 차지하더라도, 그 삼각이 놓인 공간영역은 한 칸 공 전체를 사용 중일 수 있다.

## fold_unfold_flow

```text
사각칸
→ fold
→ 직각삼각 1/2 + 직각삼각 1/2
```

```text
직각삼각 1/2 + 직각삼각 1/2
→ unfold
→ 사각칸
```

## distinction

```text
정삼각 = 60도 삼각대칭
현재 삼각 = 45-45-90 직각삼각
```

```text
도형론 = 면적 분할
자리론 = 한 칸 공의 점유상태
```

## place_judgment

삼각은 사각의 일부 공간을 차지한다.

그러나 자리론에서는 그 삼각이 한 칸 공 전체를 사용 중인 상태일 수 있다.

즉 삼각은 “면적의 절반”이면서 동시에 “한 칸 공을 점유한 자리상태”일 수 있다.

## geometry_layer

```text
square_cell
→ diagonal_fold
→ two_right_triangles
→ unfold
→ square_cell
```

## integer_layer

```text
right_triangle_count = 2
square_cell_count = 1
half_unit_count = 2
```

## vector_layer

```text
fold = square_to_triangle
unfold = triangle_to_square
overlap = boundary sharing
```

## relation

prev:
- schema.069_ddx_right_triangle_transition

related:
- schema.064_place_overlap_structure
- schema.071_three_to_two_place_overlap_principle
- schema.072_two_to_one_triangle_overlap_principle
- schema.045_warp_weft_DIR_structure
- schema.049_flip_boundary_spread_structure

## forbidden

- 현재 삼각을 정삼각으로 고정하지 않는다.
- 직각삼각을 단순 면적 1/2로만 보지 않는다.
- 자리론과 도형면적론을 혼동하지 않는다.
- fold_unfold를 단순 시각효과로 보지 않는다.
- 직각삼각의 자리 점유성을 삭제하지 않는다.

## pending

- 2칸ㆍ1칸 원리와의 관계는 schema.072에서 보강한다.
- 마름모 수열과의 관계는 후속 source index에서 보존한다.
- 직각삼각 쌍대칭의 실제 렌더링은 renderer 후보로 남긴다.

## shortest

직각삼각 fold_unfold = 한 칸 공 형성 / 자리론≠도형면적
