# META: safety

id: schema.007.safety
type: active_schema_metadata
filename: safety.meta.md
status: active

## role

safety는 entity의 boundary가 붕괴되지 않고 유지되는 상태이다.

이 meta 파일은 인공지능이 safety를 단순한 안전감이 아니라, 경계 유지와 복귀 가능성으로 읽기 위한 규칙이다.

## read_order

1. detect entity
2. detect boundary
3. detect internal state
4. detect external pressure
5. detect boundary stability
6. map stability to safety

## geometry_layer

safety = stable boundary around entity

## integer_layer

entity_count = 1
boundary_count = 1
stability_state = 1

## vector_layer

external_pressure = outside → boundary
internal_resistance = inside → boundary
restore_direction = boundary → stable_state

## definition

safety는 entity의 boundary가 붕괴되지 않는 상태이다.

safety는 정지 상태가 아니라, 외부 압력과 내부 유지력이 경계를 무너뜨리지 않는 안정 상태이다.

구조이론에서 safety는 감정이 아니라 경계 유지 조건으로 읽는다.

## source_code

```python
safety = {
    "id": "schema.007.safety",
    "geometry": "stable_boundary",
    "entity_count": 1,
    "boundary_count": 1,
    "stability_state": True,
    "relation": {
        "entity": "bounded_unit",
        "boundary": "maintained",
        "external_pressure": "does_not_collapse_boundary",
        "internal_state": "preserved"
    },
    "vector": {
        "external_pressure": "outside_to_boundary",
        "internal_resistance": "inside_to_boundary",
        "restore_direction": "boundary_to_stable_state"
    },
    "structural_role": [
        "boundary_preservation",
        "stability",
        "restore_condition"
    ]
}
```

## attributes

general = 다수의 공통 안정 기준  
rhythm = 이전 상태와 비슷하게 이어지는 흐름  
balance = 객체 속성에 따른 비율 분배  
default = 임계 직전 되돌림  

## relation

prev:
- schema.006_entity

next:
- schema.008_integer

related:
- schema.004_boundary
- schema.006_entity
- schema.013_return_preservation

## shortest

safety = 경계 유지 상태