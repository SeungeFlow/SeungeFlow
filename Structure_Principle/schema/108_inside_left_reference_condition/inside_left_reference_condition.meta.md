---
id: schema.108.inside_left_reference_condition
type: active_schema_metadata
filename: inside_left_reference_condition.meta.md
directory: 108_inside_left_reference_condition
status: active_draft
root_directory: Structure_Principle
prev: schema.107.triangle_vector_point_distinction
old_101_115: reference_only_batch_old
---

# META: inside_left_reference_condition

## role
안쪽과 왼쪽의 조건부 대응을 정의한다.

## core
```text
안쪽≠왼쪽 / 기준점이 왼쪽이고 boundary가 막힐 때만 왼쪽=안쪽 역할
```

## definition
벡터원리에서는 대응 가능하지만 도형론에서는 안쪽은 중심, 왼쪽은 4방위 중 하나다.

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
- schema.107.triangle_vector_point_distinction

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
안쪽≠왼쪽 / 기준점이 왼쪽이고 boundary가 막힐 때만 왼쪽=안쪽 역할
