---
id: schema.106.cell_center_segment_connection_rule
type: active_schema_metadata
filename: cell_center_segment_connection_rule.meta.md
directory: 106_cell_center_segment_connection_rule
status: active_draft
root_directory: Structure_Principle
prev: schema.105.radius_center_diagonal_right_angle_crossing
old_101_115: reference_only_batch_old
---

# META: cell_center_segment_connection_rule

## role
칸에서 도형론으로 넘어갈 때 선분은 칸의 정중심점끼리 연결한다.

## core
```text
칸의 정중심점=사각 대각 교차점 / 선분=정중심점끼리 연결
```

## definition
칸 외곽선이 아니라 각 칸의 대각 교차점을 대표점으로 잡아 선분을 생성한다.

## structure
```text
raw_structure
→ phase_check
→ boundary_check
→ relation_mapping
→ active_schema_or_reference_only
```

## relation
prev:
- schema.105.radius_center_diagonal_right_angle_crossing

related:
- schema.063_boundary_place_requirement
- schema.067_meta_relation_boundary_bridge
- schema.099_document_sorting_index
- schema.100_understanding_flow


## forbidden
- relation을 merge로 보지 않는다.
- source trace를 final authority로 보지 않는다.
- 비유를 과학·역사·언어학 확정문으로 승격하지 않는다.
- old 101~115를 그대로 active schema로 채택하지 않는다.
- Structure_Theory 명칭을 신규 기준으로 사용하지 않는다. 신규 기준은 Structure_Principle이다.

## pending
- active_navimap에서 세부 relation edge를 정리한다.
- 필요 시 old 101~115 reference_only_batch_old에서 source trace를 연결한다.
- 실제 renderer/prototype 적용은 후속 단계에서 검토한다.

## shortest
칸의 정중심점=사각 대각 교차점 / 선분=정중심점끼리 연결
