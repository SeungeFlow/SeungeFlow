---
id: schema.104.inscribed_circumscribed_boundary_relation
type: active_schema_metadata
filename: inscribed_circumscribed_boundary_relation.meta.md
directory: 104_inscribed_circumscribed_boundary_relation
status: active_draft
root_directory: Structure_Principle
prev: schema.103.circle_definition_structure
old_101_115: reference_only_batch_old
---

# META: inscribed_circumscribed_boundary_relation

## role
내접과 외접을 원 boundary와 다른 구조의 안쪽/바깥쪽 접촉 relation으로 정의한다.

## core
```text
내접=안쪽 접촉 / 외접=바깥쪽 접촉 / 접촉≠침범
```

## definition
내접·외접은 기준 객체를 명시해야 하며 boundary 접촉과 침범, 중첩을 구분한다.

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
- schema.103.circle_definition_structure

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
내접=안쪽 접촉 / 외접=바깥쪽 접촉 / 접촉≠침범
