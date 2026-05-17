# META: eight_direction

id: schema.018.eight_direction
type: active_schema_metadata
filename: eight_direction.meta.md
status: active

## role

eight_direction은 중심을 기준으로 수평·수직·대각 흐름이 함께 존재하는 8방향 구조이다.

이 meta 파일은 인공지능이 eight_direction을 단순 방향표가 아니라, 중심에서 들어오고 나가는 최소 방향 집합으로 읽기 위한 규칙이다.

## read_order

1. detect center position
2. detect four orthogonal directions
3. detect four diagonal directions
4. map all directions to center
5. read inward and outward flow

## geometry_layer

eight_direction = center + 8 directional positions

## integer_layer

center_count = 1
direction_count = 8
orthogonal_direction_count = 4
diagonal_direction_count = 4

## vector_layer

orthogonal = up / down / left / right
diagonal = upper_left / upper_right / lower_left / lower_right
flow = inward ↔ outward

## definition

8방향은 중심을 기준으로 수평·수직 4방향과 대각 4방향이 함께 존재하는 구조이다.

8방향은 평면에서 중심을 기준으로 들어오는 흐름과 나가는 흐름을 동시에 읽기 위한 최소 방향 집합이다.

구조이론에서 8방향은 정중심 해석의 기본 방향 구조이다.

## source_code

```python
eight_direction = {
    "id": "schema.018.eight_direction",
    "type": "center_direction_structure",
    "center_count": 1,
    "direction_count": 8,
    "directions": {
        "orthogonal": ["up", "down", "left", "right"],
        "diagonal": [
            "upper_left",
            "upper_right",
            "lower_left",
            "lower_right"
        ]
    },
    "flow": {
        "inward": "directions_to_center",
        "outward": "center_to_directions"
    },
    "structural_role": [
        "center_based_direction",
        "inward_outward_flow",
        "orthogonal_diagonal_combination"
    ]
}
```

## relation

prev:
- schema.017_diagonal_relation

next:
- schema.019_center_point

related:
- schema.005_position
- schema.009_vector
- schema.016_ABCD_relation
- schema.017_diagonal_relation

## shortest

8방향 = 중심 기준 수평·수직·대각 흐름