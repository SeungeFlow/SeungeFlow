# META: vector

id: schema.009.vector
type: active_schema_metadata
filename: vector.meta.md
status: active

## role

vector는 점에서 시작되는 방향 구조이다.

이 meta 파일은 인공지능이 vector를 값의 크기만이 아니라, 점에서 시작되어 다른 자리로 향하는 방향 관계로 읽기 위한 규칙이다.

## read_order

1. detect origin point
2. detect target position
3. detect direction from origin to target
4. detect magnitude if given
5. map point-based direction to vector

## geometry_layer

vector = origin point + direction

## integer_layer

origin_count = 1
direction_count = 1
target_count = 1

## vector_layer

origin = point
direction = origin → target
magnitude = optional

## definition

벡터는 점에서 시작되는 방향이다.

벡터는 단순한 화살표가 아니라, 한 자리에서 다른 자리로 향하는 관계 구조이다.

구조이론에서 벡터는 점이 방향을 얻은 상태로 읽는다.

## source_code

```python
vector = {
    "id": "schema.009.vector",
    "geometry": "origin_direction",
    "origin_count": 1,
    "direction_count": 1,
    "target_count": 1,
    "relation": {
        "origin": "point",
        "target": "position",
        "direction": "origin_to_target",
        "magnitude": "optional"
    },
    "structural_role": [
        "direction",
        "movement_basis",
        "relation_flow"
    ]
}
```

## relation

prev:
- schema.008_integer

next:
- schema.010_sequence_structure

related:
- schema.000_dot
- schema.001_line
- schema.005_position
- schema.011_swap

## shortest

벡터 = 점에서 시작되는 방향