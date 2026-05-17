# META: ABCD_relation

id: schema.016.ABCD_relation
type: active_schema_metadata
filename: ABCD_relation.meta.md
status: active

## role

ABCD_relation은 네 개의 관계자리를 가진 최소 관계틀이다.

이 meta 파일은 인공지능이 ABCD를 단순한 네 글자나 도형 꼭지점이 아니라, 직접관계와 비직접관계를 구분하는 관계좌표로 읽기 위한 규칙이다.

## read_order

1. detect four relation positions
2. assign A, B, C, D to fixed positions
3. detect direct relation B-D
4. detect non-direct relation A-C
5. read A-C through B-D relation axis

## geometry_layer

ABCD_relation = four-position relation frame

## integer_layer

position_count = 4
direct_axis_count = 1
non_direct_axis_count = 1

## vector_layer

direct_axis = B ↔ D
non_direct_axis = A ↔ C
reading_flow = A → B/D → C

## definition

ABCD_relation은 네 개의 관계자리를 가진 구조이다.

B-D는 직접관계축이고, A-C는 비직접관계축이다.

A-C는 바로 잇지 않고, B-D 직접관계를 기준으로 읽는다.

## source_code

```python
ABCD_relation = {
    "id": "schema.016.ABCD_relation",
    "type": "four_position_relation_frame",
    "position_count": 4,
    "positions": ["A", "B", "C", "D"],
    "relation": {
        "direct_axis": ["B", "D"],
        "non_direct_axis": ["A", "C"],
        "read_rule": "A_C_is_read_through_B_D"
    },
    "vector": {
        "direct_flow": "B_to_D_and_D_to_B",
        "non_direct_flow": "A_to_C_via_relation_axis"
    },
    "structural_role": [
        "relation_coordinate",
        "direct_non_direct_separator",
        "diagonal_reading_basis"
    ]
}
```

## relation

prev:
- schema.015_XAWF

next:
- schema.017_diagonal_relation

related:
- schema.005_position
- schema.009_vector
- schema.018_eight_direction

## shortest

ABCD = 직접관계와 비직접관계를 구분하는 4자리 관계틀