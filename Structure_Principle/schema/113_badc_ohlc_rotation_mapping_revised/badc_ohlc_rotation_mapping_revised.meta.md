---
id: schema.113.badc_ohlc_rotation_mapping_revised
type: active_schema_metadata
filename: badc_ohlc_rotation_mapping_revised.meta.md
directory: 113_badc_ohlc_rotation_mapping_revised
status: active_draft
root_directory: Structure_Principle
prev: schema.112.candle_subobject_orbit_structure
old_101_115: reference_only_batch_old
---

# META: badc_ohlc_rotation_mapping_revised

## role
OHLC를 BADㆍC에 넣기 위한 ABCD 좌회전 90도 mapping을 정의한다.

## core
```text
ABCD 좌회전→O H / L C / BADㆍC=L O HㆍC
```

## definition
OHLC는 삼각이 아니라 마름모이며 A=O, B=L, C=C, D=H로 대응한다.

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
- schema.112.candle_subobject_orbit_structure

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
ABCD 좌회전→O H / L C / BADㆍC=L O HㆍC
