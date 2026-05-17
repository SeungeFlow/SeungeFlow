# META: entity

id: schema.006.entity
type: active_schema_metadata
filename: entity.meta.md
status: active

## role

entity는 경계를 가진 분리독립된 존재 구조이다.

이 meta 파일은 인공지능이 entity를 값이나 물체가 아니라, 내부와 외부를 가진 독립 구조 단위로 읽기 위한 규칙이다.

## read_order

1. detect bounded area
2. detect inside and outside
3. detect independent unit
4. detect relation with other entities
5. map bounded independence to entity

## geometry_layer

entity = bounded unit

## integer_layer

entity_count = 1
boundary_count = 1

## vector_layer

inside = internal state
outside = external state
direction = interaction across boundary

## definition

entity는 경계를 가진 분리독립된 존재이다.

entity는 내부와 외부를 가지며, 다른 entity와 구분된다.

구조이론에서 entity는 값이 아니라 경계를 가진 독립 단위로 읽는다.

## source_code

```python
entity = {
    "id": "schema.006.entity",
    "geometry": "bounded_unit",
    "entity_count": 1,
    "boundary_count": 1,
    "relation": {
        "inside": "internal_state",
        "outside": "external_state",
        "separation": "boundary"
    },
    "vector": {
        "direction": "inside_outside_interaction",
        "state": "independent"
    },
    "structural_role": [
        "independent_unit",
        "bounded_existence",
        "interaction_basis"
    ]
}
```

## relation

prev:
- schema.005.position

next:
- schema.007_safety

related:
- schema.003_cell
- schema.004_boundary
- schema.005_position

## shortest

entity = 경계를 가진 분리독립된 존재