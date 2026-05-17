---
id: schema.068.ctp_vector_coordinate_x_dx_ddx
type: active_schema_metadata
filename: ctp_vector_coordinate_x_dx_ddx.meta.md
directory: 068_ctp_vector_coordinate_x_dx_ddx
status: active_draft
prev: schema.067.meta_relation_boundary_bridge
---

# META: ctp_vector_coordinate_x_dx_ddx

## role
ctp_vector_coordinate_x_dx_ddx는 Ctp_당연한이론에서 지속적으로 갱신되어 온 벡터공간좌표 표기방식 `(x, dx, ddx)`를 정의하는 schema이다.

이 meta 파일은 인공지능이 x, dx, ddx를 단순 미분기호나 계산기호로만 읽지 않고, 기준축 / 자리전이 / 경사·꺾임의 구조 좌표로 읽기 위한 기준이다.

## core

```text
x = 기준축
dx = 자리전이 / ㅡ 또는 ㅣ / 첫 변위
ddx = 경사 / 꺾임 / 변위의 변화
```

## definition

`(x, dx, ddx)`는 Ctp_당연한이론에서 자리전이를 읽기 위한 벡터공간좌표 표기방식이다.

x는 현재 자리의 기준축이다.

dx는 x축이 다음 자리로 전이될 때 생기는 첫 차이 또는 변위이다.

ddx는 dx가 다시 변화하며 경사, 꺾임, 대각, 2차 전이를 드러내는 자리이다.

## structure

```text
x
→ dx
→ ddx
```

```text
기준축
→ 축변환 / 자리전이
→ 경사 / 꺾임
```

## axis_mapping

```text
x = 현재 기준축
dx = ㅡ / ㅣ
ddx = 경사 / 사선 / diagonal transition
```

ㅡ는 수평 자리전이이다.

ㅣ은 수직 자리전이이다.

ddx는 ㅡ과 ㅣ만으로는 설명되지 않는 기울기, 경사, 꺾임, 변위의 변위이다.

## ctp_place_transition_relation

Ctp_자리이동식과 연결하면 다음이다.

```text
Cₙ₊₁ = Cₙ ⊕ Tₙ(Pₙ → Pₙ₊₁)
```

여기서:

```text
Pₙ = 현재 자리
Pₙ₊₁ = 다음 자리
dx = Pₙ에서 Pₙ₊₁로 이동하며 생긴 차이
ddx = 그 차이가 방향을 바꾸거나 기울기를 만들 때 생기는 2차 변화
```

## geometry_layer

```text
x = axis
dx = horizontal_or_vertical_displacement
ddx = slope_or_bend
```

## integer_layer

```text
x_count = 1 기준축
dx_count = variable 변위
ddx_count = variable 꺾임 / 경사
```

## vector_layer

```text
x_axis
→ displacement_axis
→ slope_transition
```

## relation

prev:
- schema.067_meta_relation_boundary_bridge

related:
- schema.062_place_domain_definition
- schema.063_boundary_place_requirement
- schema.065_oplus_common_operator
- schema.069_ddx_right_triangle_transition
- schema.070_right_triangle_fold_unfold_structure
- Ctp_자리이동식_source
- Ctp_당연한이론

## forbidden

- x, dx, ddx를 기존 미분기호로만 고정하지 않는다.
- dx를 단순 숫자 차이로만 보지 않는다.
- ddx를 단순 2차 미분값으로만 보지 않는다.
- x를 고정좌표값으로만 보지 않는다.
- ㅡ/ㅣ/경사 층위를 섞지 않는다.
- Ctp_당연한이론의 좌표표기와 벡터연산기법을 동일시하지 않는다.

## pending

- dx의 세부 유형은 후속 자리전이 schema에서 확장한다.
- ddx와 직각삼각 꺾임의 관계는 schema.069에서 분리한다.
- 실제 수학적 형식화는 아직 보류한다.

## shortest

x=기준축 / dx=자리전이·ㅡㅣ / ddx=경사·꺾임
