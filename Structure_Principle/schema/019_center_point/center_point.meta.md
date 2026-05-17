# META: center_point

id: schema.019.center_point
type: active_schema_metadata
filename: center_point.meta.md
status: active

## role

center_point는 여러 방향의 흐름이 모이고 다시 펼쳐지는 정중심 구조이다.

이 meta 파일은 인공지능이 center_point를 단순한 가운데 점이 아니라, 수평·수직·대각 흐름이 모이는 기준점으로 읽기 위한 규칙이다.

## read_order

1. detect center position
2. detect surrounding directions
3. detect inward flow
4. detect outward flow
5. map center to balance point

## geometry_layer

center_point = central position of directional structure

## integer_layer

center_count = 1
connected_direction_count = 8

## vector_layer

inward = directions → center
outward = center → directions
state = balanced

## definition

정중심점은 여러 방향의 흐름이 모이는 기준점이다.

정중심점은 결측이 아니라, 방향 흐름이 모이고 다시 펼쳐지는 자리이다.

구조이론에서 정중심점은 8방향 구조의 기준점이며, 균형 판정의 시작점이다.

## source_code

```python
center_point = {
    "id": "schema.019.center_point",
    "type": "center_balance_position",
    "center_count": 1,
    "connected_direction_count": 8,
    "relation": {
        "inward": "directions_to_center",
        "outward": "center_to_directions",
        "state": "balanced"
    },
    "vector": {
        "inward_flow": "external_to_center",
        "outward_flow": "center_to_external",
        "direction_state": "bidirectional"
    },
    "structural_role": [
        "center",
        "balance_point",
        "direction_convergence",
        "direction_expansion"
    ]
}
```

## relation

prev:
- schema.018_eight_direction

next:
- schema.020_crossing_point

related:
- schema.005_position
- schema.009_vector
- schema.018_eight_direction

## shortest

정중심점 = 8방향 흐름이 모이고 펼쳐지는 기준점