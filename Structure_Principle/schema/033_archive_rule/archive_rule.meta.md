# META: archive_rule

id: schema.033.archive_rule
type: active_schema_metadata
filename: archive_rule.meta.md
status: active

## role

archive_rule은 과거 자료를 본류 schema에 강제로 섞지 않고, 필요 시 보존·참조하는 규칙이다.

이 meta 파일은 인공지능이 archive를 삭제 공간이 아니라, 본류와 분리된 압축 보존 영역으로 읽기 위한 규칙이다.

## read_order

1. detect current core schema
2. detect old or external material
3. do not merge into main schema immediately
4. classify as archive if needed
5. preserve reference without forcing integration
6. map archive to separated preservation layer

## geometry_layer

archive_rule = core layer + separated archive layer

## integer_layer

core_schema_count = variable
archive_record_count = variable
forced_merge_state = 0

## vector_layer

core_flow = current schema order
archive_flow = old material → separated preservation
reference_flow = archive → core only if needed

## definition

archive는 삭제 공간이 아니다.

archive는 과거 자료, 보류 자료, 확장 자료를 본류 schema와 분리하여 보존하는 영역이다.

구조이론에서 archive는 본류를 흐리지 않기 위한 분리 보존 규칙이다.

## source_code

```python
archive_rule = {
    "id": "schema.033.archive_rule",
    "type": "separated_preservation_rule",
    "core_schema_count": "variable",
    "archive_record_count": "variable",
    "forced_merge_state": False,
    "relation": {
        "core": "current_active_schema_order",
        "archive": "separated_preservation_layer",
        "old_material": "do_not_force_merge",
        "reference": "allowed_if_needed"
    },
    "vector": {
        "core_flow": "current_schema_order",
        "archive_flow": "old_material_to_archive",
        "reference_flow": "archive_to_core_when_needed"
    },
    "structural_role": [
        "archive",
        "noise_reduction",
        "core_preservation",
        "separated_memory_layer"
    ]
}
```

## principle

```txt
archive = 삭제가 아니라 분리 보존
core = 현재 작동하는 본류
old material = 즉시 병합 금지
reference = 필요할 때만 연결
```

## forbidden

- 과거 자료를 본류 schema에 강제로 섞지 않는다.
- archive를 삭제 또는 폐기와 동일시하지 않는다.
- 오래된 자료를 현재 기준보다 우선하지 않는다.
- 본류 흐름을 흐리게 만드는 장문 원자료를 직접 삽입하지 않는다.

## relation

prev:
- schema.032_local_linux_role

next:
- schema.034_final_readme_index

related:
- schema.023_reading_protocol
- schema.031_github_as_DB
- schema.034_final_readme_index

## shortest

archive = 본류와 분리된 압축 보존 영역