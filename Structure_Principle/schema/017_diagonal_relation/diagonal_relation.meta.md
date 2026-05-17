# META: diagonal_relation

id: schema.017.diagonal_relation
type: active_schema_metadata
filename: diagonal_relation.meta.md
status: active

## role

diagonal_relation은 직접 이어지지 않는 관계를 대각으로 읽는 구조이다.

이 meta 파일은 인공지능이 diagonal_relation을 단순한 사선이나 기울어진 선이 아니라, 직접관계가 아닌 두 자리 사이의 관계해석으로 읽기 위한 규칙이다.

## read_order

1. detect two non-adjacent positions
2. detect that they are not directly connected
3. detect mediating axis or relation
4. read the relation as diagonal
5. do not collapse diagonal into direct line

## geometry_layer

diagonal_relation = non-direct relation between separated positions

## integer_layer

endpoint_count = 2
mediating_axis_count = 1
direct_connection_state = 0

## vector_layer

start = position A
end = position C
direction = A ⇄ C
path = through relation axis

## definition

대각관계는 직접 이어지지 않는 두 자리 사이의 관계이다.

대각관계는 두 점을 무조건 직선으로 합치는 것이 아니라, 사이에 있는 관계축을 통해 읽는다.

구조이론에서 대각관계는 차이를 합치는 방식이 아니라, 자리 사이의 관계를 해석하는 방식이다.

## source_code

```python
diagonal_relation = {
    "id": "schema.017.diagonal_relation",
    "type": "non_direct_relation",
    "endpoint_count": 2,
    "mediating_axis_count": 1,
    "direct_connection_state": False,
    "relation": {
        "start": "A",
        "end": "C",
        "direct": False,
        "mediated_by": "B_D_axis",
        "read_rule": "do_not_collapse_into_direct_line"
    },
    "vector": {
        "direction": "A_to_C_and_C_to_A",
        "path": "through_relation_axis"
    },
    "structural_role": [
        "non_direct_relation",
        "diagonal_reading",
        "relation_interpretation"
    ]
}
```

## relation

prev:
- schema.016_ABCD_relation

next:
- schema.018_eight_direction

related:
- schema.005_position
- schema.009_vector
- schema.016_ABCD_relation

## shortest

대각관계 = 직접 잇지 않고 관계축으로 읽는 비직접 관계