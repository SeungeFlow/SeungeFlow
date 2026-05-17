---
id: schema.111.angle_grid_resolution_structure
type: active_schema_metadata
filename: angle_grid_resolution_structure.meta.md
directory: 111_angle_grid_resolution_structure
status: active_draft
root_directory: Structure_Principle
prev: schema.110.nine_zero_overlap_transition
old_101_115: reference_only_batch_old
---

# META: angle_grid_resolution_structure

## role
45도 12칸, 90도 24칸의 각도 해상도 기준격자를 정의한다.

## core
```text
45도=12칸 / 90도=24칸 / 한 칸=3.75도
```

## definition
직각삼각 쌍대칭과 OHLC 마름모를 같은 각도 해상도에서 읽는다.

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
- schema.110.nine_zero_overlap_transition

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
45도=12칸 / 90도=24칸 / 한 칸=3.75도
