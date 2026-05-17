---
id: schema.105.radius_center_diagonal_right_angle_crossing
type: active_schema_metadata
filename: radius_center_diagonal_right_angle_crossing.meta.md
directory: 105_radius_center_diagonal_right_angle_crossing
status: active_draft
root_directory: Structure_Principle
prev: schema.104.inscribed_circumscribed_boundary_relation
old_101_115: reference_only_batch_old
---

# META: radius_center_diagonal_right_angle_crossing

## role
반지름·정중심·대각·직각·교차를 원·사각·삼각·칸의 연결 구조어로 정의한다.

## core
```text
정중심→반지름→boundary / 사각→대각→교차점 / 직각=축교차
```

## definition
반지름은 정중심과 boundary의 관계선이고, 사각 대각 교차점은 칸의 대표 정중심점이다.

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
- schema.104.inscribed_circumscribed_boundary_relation

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
정중심→반지름→boundary / 사각→대각→교차점 / 직각=축교차
