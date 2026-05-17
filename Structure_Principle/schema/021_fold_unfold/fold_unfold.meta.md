# META: fold_unfold

id: schema.021.fold_unfold
type: active_schema_metadata
filename: fold_unfold.meta.md
status: active

## role

fold_unfold는 같은 구조를 접거나 펼쳐서 다른 배치로 읽는 운용 구조이다.

이 meta 파일은 인공지능이 fold_unfold를 형태 변화가 아니라, 중심경계를 유지한 상태에서 배치가 달라지는 구조로 읽기 위한 규칙이다.

## read_order

1. detect original structure
2. detect hidden or folded area
3. detect boundary preservation
4. unfold hidden area if needed
5. compare folded and unfolded structure
6. map change to layout transformation

## geometry_layer

fold_unfold = folded structure + unfolded structure

## integer_layer

structure_count = 1
layout_state_count = 2
boundary_preservation_state = 1

## vector_layer

fold = outside → inside
unfold = inside → outside
state = layout_change

## definition

접힘·펼침은 구조의 내용을 바꾸는 것이 아니라, 같은 구조를 다른 배치로 읽는 방식이다.

접혀 있을 때 보이지 않던 영역은 펼치면 경계 위에 놓인다.

구조이론에서 접힘·펼침은 중심경계를 유지한 상태에서 배치와 해석 위치가 달라지는 운용 구조이다.

## source_code

```python
fold_unfold = {
    "id": "schema.021.fold_unfold",
    "type": "layout_transformation",
    "structure_count": 1,
    "layout_state_count": 2,
    "boundary_preservation_state": True,
    "relation": {
        "folded": "hidden_area_inside_structure",
        "unfolded": "hidden_area_on_boundary",
        "boundary": "preserved",
        "content": "same_structure"
    },
    "vector": {
        "fold": "outside_to_inside",
        "unfold": "inside_to_outside",
        "state": "layout_change"
    },
    "structural_role": [
        "folding",
        "unfolding",
        "hidden_area_reading",
        "boundary_preservation",
        "layout_transformation"
    ]
}
```

## relation

prev:
- schema.020_crossing_point

next:
- schema.022_scale_change

related:
- schema.002_surface
- schema.003_cell
- schema.004_boundary
- schema.019_center_point
- schema.020_crossing_point

## shortest

접힘·펼침 = 중심경계를 유지한 배치 변화