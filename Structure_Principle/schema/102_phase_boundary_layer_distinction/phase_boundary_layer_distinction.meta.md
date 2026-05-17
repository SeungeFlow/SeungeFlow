---
id: schema.102.phase_boundary_layer_distinction
type: active_schema_metadata
filename: phase_boundary_layer_distinction.meta.md
directory: 102_phase_boundary_layer_distinction
status: active_draft
root_directory: Structure_Principle
prev: schema.101.three_dot_reading_mode_structure
old_101_115: reference_only_batch_old
---

# META: phase_boundary_layer_distinction

## role
같은 raw structure를 어디까지 같은 위상으로 볼지, 어디서 boundary로 나눌지 판정한다.

## core
```text
층위분리 / 위상판정 / 경계설정
```

## definition
기준점·축·방향·경계·닫힘·순서·관측자·해석목적이 바뀌면 위상 경계를 세운다.

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
- schema.101.three_dot_reading_mode_structure

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
층위분리 / 위상판정 / 경계설정
