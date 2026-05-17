# META: crossing_point

id: schema.020.crossing_point
type: active_schema_metadata
filename: crossing_point.meta.md
status: active

## role

crossing_point는 선, 칸, 벡터 흐름이 서로 교차하는 지점이다.

이 meta 파일은 인공지능이 crossing_point를 단순한 교차 표시가 아니라, 서로 다른 방향 흐름이 같은 자리를 통과하며 관계를 만드는 구조로 읽기 위한 규칙이다.

## read_order

1. detect at least two lines or flows
2. detect intersection position
3. detect shared position
4. detect crossing directions
5. map crossing to relation point

## geometry_layer

crossing_point = intersection of lines or flows

## integer_layer

crossing_count = 1
minimum_flow_count = 2
shared_position_count = 1

## vector_layer

flow_a = direction A
flow_b = direction B
intersection = shared position
state = crossing

## definition

교차점은 둘 이상의 선 또는 흐름이 같은 자리를 통과하는 지점이다.

교차점은 단순히 선이 겹친 표시가 아니라, 서로 다른 방향이 한 자리에서 관계를 만드는 구조이다.

구조이론에서 교차점은 선 개념과 칸 개념이 만나는 핵심 지점이다.

## source_code

```python
crossing_point = {
    "id": "schema.020.crossing_point",
    "type": "intersection_position",
    "crossing_count": 1,
    "minimum_flow_count": 2,
    "shared_position_count": 1,
    "relation": {
        "flow_a": "direction_A",
        "flow_b": "direction_B",
        "intersection": "shared_position",
        "state": "crossing"
    },
    "vector": {
        "flow_a": "A_direction",
        "flow_b": "B_direction",
        "interaction": "same_position_crossing"
    },
    "structural_role": [
        "intersection",
        "shared_position",
        "relation_point",
        "line_cell_bridge"
    ]
}
```

## relation

prev:
- schema.019_center_point

next:
- schema.021_fold_unfold

related:
- schema.001_line
- schema.003_cell
- schema.005_position
- schema.009_vector
- schema.018_eight_direction

## shortest

교차점 = 서로 다른 흐름이 같은 자리를 통과하는 관계점