# META: human_relation_structure

id: schema.029.human_relation_structure
type: active_schema_metadata
filename: human_relation_structure.meta.md
status: active

## role

human_relation_structure는 인간관계를 감정 설명이 아니라 entity, boundary, distance, flow의 구조로 읽는 예시 구조이다.

이 meta 파일은 인공지능이 human_relation_structure를 인간 심리 해석이 아니라, 관계의 자리·경계·거리·흐름·충돌 구조로 읽기 위한 규칙이다.

## read_order

1. detect each person as entity
2. detect boundary of each entity
3. detect relation distance
4. detect flow between entities
5. detect boundary contact or boundary violation
6. map relation state to structure interpretation

## geometry_layer

human_relation_structure = entity + boundary + distance + relation flow

## integer_layer

entity_count = variable
boundary_count = variable
relation_count = variable
distance_count = variable

## vector_layer

self = entity_A
other = entity_B
flow = self ↔ other
distance = relation spacing

## definition

인간관계는 감정 자체로 먼저 읽지 않는다.

구조이론에서 인간관계는 entity와 entity 사이의 경계, 거리, 흐름, 접촉, 침범, 복귀 가능성으로 읽는다.

관계의 문제는 감정 이전에 서로의 경계와 거리, 중심, 흐름을 다르게 해석하는 데서 발생할 수 있다.

## source_code

```python
human_relation_structure = {
    "id": "schema.029.human_relation_structure",
    "type": "relation_structure_example",
    "entity_count": "variable",
    "boundary_count": "variable",
    "relation_count": "variable",
    "distance_count": "variable",
    "relation": {
        "entity_A": "self_or_person_A",
        "entity_B": "other_or_person_B",
        "boundary_A": "entity_A_boundary",
        "boundary_B": "entity_B_boundary",
        "distance": "relation_spacing",
        "flow": "interaction_between_entities",
        "violation": "boundary_crossing_without_alignment"
    },
    "vector": {
        "A_to_B": "interaction_flow",
        "B_to_A": "response_flow",
        "state": "mutual_or_unbalanced"
    },
    "structural_role": [
        "human_relation_example",
        "boundary_distance_reading",
        "interaction_flow",
        "relation_misalignment_detection"
    ]
}
```

## principle

```txt
사람 = entity
관계 = entity 사이의 흐름
거리 = entity 사이의 칸수
경계 = 허용범위
충돌 = 경계 해석 불일치
복귀 = 관계 안정 상태로 돌아갈 수 있는 조건
```

## forbidden

- 인간관계를 감정 단어로만 해석하지 않는다.
- 상대를 선악으로 즉시 판정하지 않는다.
- 보호와 구속을 같은 것으로 고정하지 않는다.
- 경계 침범을 관계 깊이로 오해하지 않는다.
- 거리 조정을 관계 단절로 단정하지 않는다.

## relation

prev:
- schema.028_active_schema

next:
- schema.030_Naiad_Thalassa_73_69

related:
- schema.004_boundary
- schema.006_entity
- schema.007_safety
- schema.019_center_point
- schema.023_reading_protocol

## shortest

인간관계 = entity 사이의 경계·거리·흐름 구조