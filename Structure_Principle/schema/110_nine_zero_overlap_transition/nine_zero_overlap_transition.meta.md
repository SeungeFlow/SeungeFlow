---
id: schema.110.nine_zero_overlap_transition
type: active_schema_metadata
filename: nine_zero_overlap_transition.meta.md
directory: 110_nine_zero_overlap_transition
status: active_draft
root_directory: Structure_Principle
prev: schema.109.ctp_structure_integer_property_table
old_101_115: reference_only_batch_old
---

# META: nine_zero_overlap_transition

## role
9와 0의 끝·시작 중첩을 정의한다.

## core
```text
9=끝 / 0=시작 / ㆍ=끝과 시작의 방향중첩
```

## definition
9 다음 0은 단절이 아니라 ㆍ자리에서 끝과 시작이 겹치는 자리중첩이다.

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
- schema.109.ctp_structure_integer_property_table

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
9=끝 / 0=시작 / ㆍ=끝과 시작의 방향중첩
