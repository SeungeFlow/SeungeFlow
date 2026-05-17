# META: orbit_structure

id: schema.036.orbit_structure
type: active_schema_metadata
filename : orbit_structure.meta.md
status: active

## role

orbit_structure는 8방향 구조를 정적인 위치가 아니라 반복되는 이동 경로로 해석하는 구조이다.

이 meta 파일은 인공지능이 방향을 위치로만 보지 않고, 중심을 기준으로 반복되는 흐름(궤)으로 읽기 위한 규칙이다.

## read_order

1. detect center point
2. detect 8 directions (orthogonal + diagonal)
3. detect directional flows
4. detect repetition of movement
5. map repeated flow to orbit
6. interpret structure as orbit system

## geometry_layer

orbit_structure = center + 8 directional paths

## integer_layer

center_count = 1
direction_count = 8
orbit_count = 8

## vector_layer

direction = 8-way
flow = repeated directional movement
state = cyclic

## definition

궤이론은 중심을 기준으로 여러 방향의 흐름이 반복되며 이어지는 구조이다.

8방향은 정적인 위치 기준이고, 8궤는 그 위치를 따라 반복되는 이동 경로이다.

구조이론에서 궤는 벡터가 반복되며 형성되는 경로이다.

## source_code

```python
orbit_structure = {
    "id": "schema.036.orbit_structure",
    "type": "orbit_structure",
    "center_count": 1,
    "direction_count": 8,
    "orbit_count": 8,
    "relation": {
        "center": "reference_point",
        "directions": "8_way_structure",
        "flow": "repeated_movement",
        "orbit": "path_of_repetition"
    },
    "vector": {
        "direction": "8_way",
        "flow": "cyclic",
        "state": "orbiting"
    },
    "structural_role": [
        "orbit",
        "cyclic_flow",
        "movement_path",
        "vector_repetition"
    ]
}
```

## relation

prev:
- schema.018_eight_direction

related:
- schema.009_vector
- schema.019_center_point
- schema.024_operation_axis_judgment

## shortest

8궤 = 8방향의 반복 이동 경로