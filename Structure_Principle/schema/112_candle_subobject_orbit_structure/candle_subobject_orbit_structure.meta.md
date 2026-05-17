---
id: schema.112.candle_subobject_orbit_structure
type: active_schema_metadata
filename: candle_subobject_orbit_structure.meta.md
directory: 112_candle_subobject_orbit_structure
status: active_draft
root_directory: Structure_Principle
prev: schema.111.angle_grid_resolution_structure
old_101_115: reference_only_batch_old
---

# META: candle_subobject_orbit_structure

## role
하나의 캔들을 상위 장 안의 하위 움직임들의 궤도합으로 읽는다.

## core
```text
캔들=하위 움직임들의 합 / OHLC=4방위 끝점
```

## definition
큰 캔들은 parent-field이고 내부 하위 움직임들은 그 안의 orbit trace로 읽힌다.

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
- schema.111.angle_grid_resolution_structure

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
캔들=하위 움직임들의 합 / OHLC=4방위 끝점
