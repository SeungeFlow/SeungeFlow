---
id: schema.072.two_to_one_triangle_overlap_principle
type: active_schema_metadata
filename: two_to_one_triangle_overlap_principle.meta.md
directory: 072_two_to_one_triangle_overlap_principle
status: active_draft
prev: schema.071.three_to_two_place_overlap_principle
---

# META: two_to_one_triangle_overlap_principle

## role
two_to_one_triangle_overlap_principle은 두 칸 사이의 역삼각 자리겹침이 하나의 완전한 칸을 형성하는 원리를 정의하는 schema이다.

이 meta 파일은 인공지능이 직각삼각 1/2, 역삼각 1/2, 사각칸, 자리겹침을 단순 면적 계산으로만 읽지 않도록 하는 기준이다.

## core

```text
두 직각삼각은 하나의 완전한 칸을 형성한다.
```

```text
역삼각이 들어오면 자리겹침이 발생하고,
겹친 1/2 + 1/2이 완전사각을 만든다.
```

## definition

2칸ㆍ1칸 원리는 두 칸 사이에 역삼각이 들어와 양쪽 직각삼각의 1/2 자리와 겹치면서 하나의 완전한 칸 공을 형성하는 구조이다.

이때 삼각은 수학적 면적 일부이지만, 자리론에서는 한 칸 공 전체를 사용 중인 자리상태일 수 있다.

## symbolic_structure

```text
(+[1/2][1/2])
+
(-[1/2][1/2])
+
(+[1/2][1/2])
```

가운데 `-` 구조는 역삼각 또는 대칭삼각이다.

양쪽 `+` 구조의 1/2과 가운데 대칭 구조의 1/2이 겹치며 완전사각을 만든다.

## triangle_type

```text
정삼각 = 60도 삼각대칭
현재 삼각 = 45-45-90 직각삼각의 fold_unfold 구조
```

## place_layer

```text
직각삼각의 1/2 자리
+
역삼각의 1/2 자리
=
완전한 한 칸
```

## geometry_layer

```text
right_triangle
+
inverse_right_triangle
→ square_cell
```

## integer_layer

```text
half_triangle_count = 2
square_cell_count = 1
overlap_half_count = variable
```

## vector_layer

```text
positive_triangle_direction
↔ inverse_triangle_direction
→ shared square cell
```

## relation

prev:
- schema.071_three_to_two_place_overlap_principle

related:
- schema.064_place_overlap_structure
- schema.065_oplus_common_operator
- schema.069_ddx_right_triangle_transition
- schema.070_right_triangle_fold_unfold_structure
- schema.045_warp_weft_DIR_structure
- schema.083_waxf_vowel_rhombus_structure

## forbidden

- 현재 삼각을 정삼각으로 해석하지 않는다.
- 1/2을 단순 산술분수로만 보지 않는다.
- 자리겹침을 자리중첩과 무조건 동일시하지 않는다.
- 역삼각을 빈틈 채우기만으로 보지 않는다.
- 사각칸 형성을 단순 도형합성으로만 보지 않는다.

## pending

- 자리겹침과 자리중첩의 용어 구분은 별도 schema에서 보강한다.
- 2칸ㆍ1칸 구조와 화학 결합 구조의 relation은 아직 보류한다.

## shortest

2칸 사이 겹침이 1칸을 만든다 / 직각삼각 1/2 + 역삼각 1/2 = 완전사각
