# META: position

id: schema.005.position
type: active_schema_metadata
filename: position.meta.md
status: active

## role

position은 값이나 구조가 놓이는 자리이다.

이 meta 파일은 인공지능이 position을 값 자체가 아니라 값이 놓이는 위치 구조로 읽기 위한 규칙이다.

## read_order

1. detect cell or point
2. detect occupied location
3. separate value from position
4. detect relation with neighboring positions
5. map location to position

## geometry_layer

position = point or cell as locatable place

## integer_layer

position_count = 1

## vector_layer

origin = position
direction = relational

## definition

자리는 값이 놓이는 위치이다.

값은 변할 수 있지만, 자리는 관계를 유지한다.

구조이론에서 자리는 값보다 먼저 읽는다.

## source_code

```python
position = {
    "id": "schema.005.position",
    "geometry": "locatable_place",
    "position_count": 1,
    "value_state": "variable",
    "relation": {
        "value": "may_change",
        "position": "structural_reference"
    },
    "vector": {
        "origin": "position",
        "direction": "relational"
    },
    "structural_role": [
        "location",
        "reference",
        "value_holder"
    ]
}
```

## relation

prev:
- schema.004.boundary

next:
- schema.006_entity

related:
- schema.000.dot
- schema.003_cell
- schema.008_integer
- schema.009_vector
- schema.011_swap

## shortest

자리 = 값이 놓이는 위치