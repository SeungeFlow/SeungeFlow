---
id: schema.103.circle_definition_structure
type: active_schema_metadata
filename: circle_definition_structure.meta.md
directory: 103_circle_definition_structure
status: active_draft
root_directory: Structure_Principle
prev: schema.102.phase_boundary_layer_distinction
old_101_115: reference_only_batch_old
---

# META: circle_definition_structure

## role
원의 정의를 닫힘·boundary·return·같은 위상 범위로 정의한다.

## core
```text
원=닫힘+경계+복귀+같은 위상 범위
```

## definition
원은 시작점과 끝점이 relation으로 다시 만나는 닫힌 순환구조이며 위상 경계의 근본 기준이다.

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
- schema.102.phase_boundary_layer_distinction

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
원=닫힘+경계+복귀+같은 위상 범위
