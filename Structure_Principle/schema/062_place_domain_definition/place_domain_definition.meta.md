---
id: schema.062.place_domain_definition
type: active_schema_metadata
filename: place_domain_definition.meta.md
directory: 062_place_domain_definition
status: active_draft
prev: schema.061.vector_unlock
---

# META: place_domain_definition

## role
place_domain_definition은 구조원리에서 “자리”를 단순 위치나 좌표가 아니라, 두 대상 사이에 형성되는 시공간 사이범위 영역으로 정의하는 schema이다.

## core
```text
자리 = between
자리 = A와 C 사이의 B
자리 = 관계가 발생하는 시공간 사이범위 영역
```

## definition
자리란 관측자 기준에서 두 대상 사이에 형성되는 시공간 사이범위 영역이다.

자리는 단순 위치가 아니다. 자리는 공도 아니고 완전한 무도 아니다. 자리는 두 대상 사이에서 관계가 발생할 수 있는 between-domain이다.

## structure
```text
A B C

A = 대상
B = 자리
C = 대상
```

```text
position
→ place
→ empty_place
→ placed_state
→ entity
```

## layer_distinction
```text
position = 넓은 위치 field
place = position 안에서 상태가 놓일 수 있는 자리
empty_place = 아직 상태가 놓이지 않은 자리
placed_state = 자리에 실제로 놓인 상태
entity = boundary와 place/state를 가진 분리독립 존재
```

## relation
prev:
- schema.061_vector_unlock

related:
- schema.005_position
- schema.006_entity
- schema.007_safety
- schema.059_empty_place_present_understanding
- schema.060_coherency
- schema.063_boundary_place_requirement
- schema.064_place_overlap_structure
- schema.068_ctp_vector_coordinate_x_dx_ddx

## forbidden
- 자리를 단순 좌표점으로 보지 않는다.
- 자리를 공 또는 무와 동일시하지 않는다.
- 자리를 단순 empty space로 보지 않는다.
- place와 position을 혼동하지 않는다.
- empty_place와 placed_state를 혼동하지 않는다.
- path를 place identity로 보지 않는다.

## pending
- 자리와 공의 관계는 schema.059를 참조한다.
- 자리와 boundary의 필수관계는 schema.063에서 분리 정의한다.
- 자리이동은 Ctp 계열 schema에서 별도 정의한다.
- C=tp에서 p와 C의 관계는 별도 schema에서 보강한다.

## shortest
자리 = between / A B C에서 B / 관계가 발생하는 시공간 사이범위 영역
