---
id: schema.109.ctp_structure_integer_property_table
type: active_schema_metadata
filename: ctp_structure_integer_property_table.meta.md
directory: 109_ctp_structure_integer_property_table
status: active_draft
root_directory: Structure_Principle
prev: schema.108.inside_left_reference_condition
old_101_115: reference_only_batch_old
---

# META: ctp_structure_integer_property_table

## role
Ctp_당연한이론의 구조정수론 0~10 성질표를 보존한다.

## core
```text
0=정중심 / 1=차이 / 2=평면 / 3=공간 / 4=이동 / 5=변위 / 6=reset / 7=안정 / 8=포화 / 9=문턱 / 10=9+1dx
```

## definition
숫자는 수량이 아니라 구조가 도달한 자리성질값이다.

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
- schema.108.inside_left_reference_condition

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
0=정중심 / 1=차이 / 2=평면 / 3=공간 / 4=이동 / 5=변위 / 6=reset / 7=안정 / 8=포화 / 9=문턱 / 10=9+1dx
