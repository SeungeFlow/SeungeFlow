# META: operation_axis_judgment

id: schema.024.operation_axis_judgment
type: active_schema_metadata
filename: operation_axis_judgment.meta.md
status: active

## role

operation_axis_judgment는 운용/해석 축 전체가 구조적으로 성립하는지 판정하는 최종 메타 구조이다.

이 meta 파일은 인공지능이 XAWF, ABCD, 대각관계, 8방향, 정중심, 교차점, 접힘·펼침, 스케일 변화를 하나의 운용축으로 연결해 읽기 위한 규칙이다.

## read_order

1. detect XAWF reading coordinate
2. detect ABCD relation frame
3. detect direct and non-direct relation
4. detect diagonal relation
5. detect eight-direction structure
6. detect center point
7. detect crossing point
8. detect fold/unfold operation
9. detect scale change
10. judge operation axis consistency

## geometry_layer

operation_axis_judgment = interpretation axis + relation frame + center flow + operation change

## integer_layer

axis_count = variable
relation_count = variable
direction_count = 8
center_count = 1
judgment_state = 1

## vector_layer

flow = XAWF → ABCD → diagonal → eight_direction → center → crossing → fold_unfold → scale_change
direction = ordered operation axis

## definition

운용축 판정은 구조를 읽는 방법이 일관되게 유지되는지를 확인하는 것이다.

정의축은 무엇인지 정한다.

운용축은 그것을 어떻게 읽고 움직일지 정한다.

구조이론에서 운용축은 XAWF 좌표, ABCD 관계틀, 대각관계, 8방향, 정중심, 교차점, 접힘·펼침, 스케일 변화를 하나의 순서로 연결한다.

## source_code

```python
operation_axis_judgment = {
    "id": "schema.024.operation_axis_judgment",
    "type": "operation_axis_final_judgment",
    "axis_count": "variable",
    "direction_count": 8,
    "center_count": 1,
    "judgment_state": True,
    "flow": [
        "XAWF",
        "ABCD_relation",
        "diagonal_relation",
        "eight_direction",
        "center_point",
        "crossing_point",
        "fold_unfold",
        "scale_change"
    ],
    "rule": {
        "preserve_reading_order": True,
        "preserve_center_reference": True,
        "do_not_collapse_non_direct_relation": True,
        "do_not_replace_operation_axis_with_external_theory": True
    },
    "judgment": {
        "valid_if": [
            "reading_coordinate_is_fixed",
            "direct_and_non_direct_relations_are_separated",
            "center_point_is_preserved",
            "operation_flow_is_ordered",
            "scale_change_is_read_as_mapping_change"
        ]
    },
    "structural_role": [
        "operation_axis_judgment",
        "reading_consistency",
        "center_reference_preservation",
        "interpretation_flow_control"
    ]
}
```

## judgment_condition

```txt
XAWF = 위치 고정
ABCD = 관계틀
대각관계 = 비직접 관계
8방향 = 중심 기준 방향 집합
정중심 = 기준점
교차점 = 흐름 관계점
접힘·펼침 = 배치 변화
스케일 변화 = 칸수와 값의 대응 변화
```

## relation

prev:
- schema.023_reading_protocol

related:
- schema.015_XAWF
- schema.016_ABCD_relation
- schema.017_diagonal_relation
- schema.018_eight_direction
- schema.019_center_point
- schema.020_crossing_point
- schema.021_fold_unfold
- schema.022_scale_change
- schema.023_reading_protocol

## shortest

운용축 판정 = 구조를 읽는 순서와 중심 기준의 일관성 확인