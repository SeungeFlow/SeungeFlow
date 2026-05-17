---
id: schema.069.ddx_right_triangle_transition
type: active_schema_metadata
filename: ddx_right_triangle_transition.meta.md
directory: 069_ddx_right_triangle_transition
status: active_draft
prev: schema.068.ctp_vector_coordinate_x_dx_ddx
---

# META: ddx_right_triangle_transition

## role
ddx_right_triangle_transition은 직각삼각형의 꺾임점에서 ddx가 경사·대각·전이값으로 드러나는 구조를 정의하는 schema이다.

이 meta 파일은 인공지능이 ddx를 단순 계산값으로만 보지 않고, 피타고라스층 / 도형층 / 자리층에서 다르게 읽히는 전환값으로 이해하기 위한 기준이다.

## core

```text
ddx = 꺾임점의 전이값
```

```text
피타고라스층 = 계산값
도형론층 = 분할·배분값
자리론층 = 자리중첩·자리전이값
```

## definition

ddx는 직각삼각형에서 수평 dx와 수직 dx가 만나는 꺾임점에서 드러나는 경사·대각·전이값이다.

ddx는 하나의 층위에서만 고정되지 않는다.

같은 ddx라도 계산층에서는 길이값, 도형층에서는 분할·배분값, 자리층에서는 자리중첩과 자리전이의 표시가 될 수 있다.

## right_triangle_example

```text
(0,0)ㆍ(1,0)ㆍ(1,1)
```

```text
(0,0) → (1,0) = 수평 dx
(1,0) → (1,1) = 수직 dx
(1,0) = 꺾임점 / ddx 발생점
```

## layer_reading

### pythagorean_layer

피타고라스층에서 ddx는 계산값으로 읽힌다.

예를 들어 수평 1, 수직 1이면 대각 길이는 sqrt(2)로 계산될 수 있다.

### geometry_layer

도형론층에서 ddx는 꺾인 선분, 삼각 발생, 면의 절반, 분할, 배분, 경계, 방향 전환으로 읽힌다.

### place_layer

자리론층에서 ddx는 자리중첩, 3칸→2칸 전환, 공유 boundary, 꺾임점의 전이로 읽힌다.

## structure

```text
x → dx → ddx
```

```text
기준축 → 자리전이 → 꺾임 / 경사 / 삼각 발생
```

## relation

prev:
- schema.068_ctp_vector_coordinate_x_dx_ddx

related:
- schema.062_place_domain_definition
- schema.064_place_overlap_structure
- schema.065_oplus_common_operator
- schema.070_right_triangle_fold_unfold_structure
- schema.071_three_to_two_place_overlap_principle
- schema.072_two_to_one_triangle_overlap_principle

## forbidden

- ddx를 계산값 하나로 고정하지 않는다.
- ddx를 도형 분할값으로만 고정하지 않는다.
- ddx를 자리중첩과 분리해서만 보지 않는다.
- 직각삼각을 정삼각으로 오해하지 않는다.
- 경사를 단순 시각적 사선으로만 보지 않는다.
- 피타고라스 계산층과 자리론 층을 섞지 않는다.

## pending

- ddx가 실제 Ctp 연산에서 어떻게 호출되는지는 후속 연산화 문서에서 검토한다.
- 직각삼각 fold_unfold 구조는 schema.070에서 분리한다.
- 3칸ㆍ2칸 원리와의 관계는 schema.071에서 분리한다.

## shortest

ddx=꺾임점 / 피타고라스층=계산값 / 도형층=분할값 / 자리층=중첩·전이값
