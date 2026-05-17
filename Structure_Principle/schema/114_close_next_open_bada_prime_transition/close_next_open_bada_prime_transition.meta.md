---
id: schema.114.close_next_open_bada_prime_transition
type: active_schema_metadata
filename: close_next_open_bada_prime_transition.meta.md
directory: 114_close_next_open_bada_prime_transition
status: active_draft
root_directory: Structure_Principle
prev: schema.113.badc_ohlc_rotation_mapping_revised
old_101_115: reference_only_batch_old
---

# META: close_next_open_bada_prime_transition

## role
Close가 다음 Open이므로 BADㆍC를 BADㆍA'로 보정한다.

## core
```text
Closeₙ=Openₙ₊₁ / C=A' / BADㆍC→BADㆍA'
```

## definition
C는 현재 Close이면서 다음 A, 즉 다음 Open의 seed가 된다.

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
- schema.113.badc_ohlc_rotation_mapping_revised

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
Closeₙ=Openₙ₊₁ / C=A' / BADㆍC→BADㆍA'
