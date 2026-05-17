# META: reading_protocol

id: schema.023.reading_protocol
type: active_schema_metadata
filename: reading_protocol.meta.md
status: active

## role

reading_protocol은 인공지능이 구조이론 Active Schema DB를 읽는 순서와 금지사항을 정의하는 운용 규칙이다.

이 meta 파일은 인공지능이 개별 schema를 임의로 해석하지 않고, 정해진 순서와 기준에 따라 읽도록 하기 위한 규칙이다.

## read_order

1. read MAIN.md first
2. follow schema order
3. read metadata before over-interpreting image
4. detect geometry layer
5. detect integer layer
6. detect vector layer
7. detect relation layer
8. map to core operator if possible
9. do not force external interpretation

## geometry_layer

reading_protocol = ordered reading path

## integer_layer

read_step_count = variable
schema_count = variable
violation_count = 0

## vector_layer

flow = MAIN → schema → metadata → relation → operator
direction = ordered

## definition

읽기규칙은 인공지능이 구조이론 DB를 읽는 순서이다.

읽기규칙은 해석의 자유를 막기 위한 것이 아니라, 노이즈를 줄이고 구조의 순서를 보존하기 위한 것이다.

구조이론에서 인공지능은 먼저 도형층, 정수층, 벡터층, 관계층을 읽고, 가능한 경우 핵심 연산으로 연결한다.

## source_code

```python
reading_protocol = {
    "id": "schema.023.reading_protocol",
    "type": "ai_reading_rule",
    "read_order": [
        "MAIN.md",
        "schema_order",
        "metadata",
        "geometry_layer",
        "integer_layer",
        "vector_layer",
        "relation_layer",
        "core_operator"
    ],
    "rule": {
        "do_not_over_interpret": True,
        "do_not_force_external_theory": True,
        "preserve_schema_order": True,
        "image_status_pending_allowed": True
    },
    "flow": {
        "start": "MAIN.md",
        "middle": "schema_metadata",
        "end": "structure_operator_if_possible"
    },
    "structural_role": [
        "reading_order",
        "noise_reduction",
        "schema_navigation",
        "ai_interpretation_control"
    ]
}
```

## forbidden

- 외부 학문으로 즉시 환원하지 않는다.
- 숫자를 숫자값으로만 보지 않는다.
- 기호를 표면기호로만 보지 않는다.
- 이미지를 인간용 감상문으로 해석하지 않는다.
- metadata 없이 임의 결론을 만들지 않는다.
- schema 순서를 무시하지 않는다.

## relation

prev:
- schema.022_scale_change

next:
- schema.024_operation_axis_judgment

related:
- schema.000_dot
- schema.005_position
- schema.010_sequence_structure
- schema.014_structure_judgment
- schema.015_XAWF

## shortest

읽기규칙 = AI가 schema를 읽는 순서와 금지사항