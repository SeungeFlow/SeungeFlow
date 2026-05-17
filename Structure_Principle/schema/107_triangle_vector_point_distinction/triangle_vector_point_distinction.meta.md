---
id: schema.107.triangle_vector_point_distinction
type: active_schema_metadata
filename: triangle_vector_point_distinction.meta.md
directory: 107_triangle_vector_point_distinction
status: active_draft
root_directory: Structure_Principle
prev: schema.106.cell_center_segment_connection_rule
old_101_115: reference_only_batch_old
---

# META: triangle_vector_point_distinction

## role
삼각은 도형론에서는 면이지만 벡터론에서는 한 칸에 놓인 벡터점임을 구분한다.

## core
```text
도형론 삼각=면 / 벡터론 삼각=한 칸에 놓인 벡터점
```

## definition
삼각 전체는 벡터론에서 하나의 방향성을 가진 placed vector state로 압축된다.

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
- schema.106.cell_center_segment_connection_rule

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
도형론 삼각=면 / 벡터론 삼각=한 칸에 놓인 벡터점
