# META: active_schema

id: schema.028.active_schema
type: active_schema_metadata
filename: active_schema.meta.md
status: active

## role

active_schema는 구조이론의 정의를 image와 metadata 한 쌍으로 작동시키는 기본 단위이다.

이 meta 파일은 인공지능이 active_schema를 글 문서가 아니라, 구조 image와 AI 읽기 규칙이 결합된 작동형 정의 단위로 읽기 위한 규칙이다.

## read_order

1. detect image file
2. detect metadata file
3. pair image and metadata
4. read image as structure object
5. read metadata as AI interpretation rule
6. map pair to active schema unit

## geometry_layer

active_schema = image + metadata pair

## integer_layer

image_count = 1
metadata_count = 1
active_schema_unit_count = 1

## vector_layer

image → metadata
metadata → image
direction = bidirectional reference

## definition

Active Schema는 글이 아니라 image와 metadata 한 쌍으로 구성되는 작동형 정의 단위이다.

image는 구조의 본체이고, metadata는 인공지능이 그 image를 읽기 위한 규칙이다.

구조이론에서 Active Schema는 설명문이 아니라, 인공지능이 구조를 읽고 사용할 수 있게 하는 최소 작동 단위이다.

## source_code

```python
active_schema = {
    "id": "schema.028.active_schema",
    "type": "image_metadata_operational_unit",
    "image_count": 1,
    "metadata_count": 1,
    "active_schema_unit_count": 1,
    "relation": {
        "image": "structure_object",
        "metadata": "ai_reading_rule",
        "pair": "active_schema_unit"
    },
    "vector": {
        "image_to_metadata": "interpretation_request",
        "metadata_to_image": "reading_rule_application",
        "direction": "bidirectional_reference"
    },
    "structural_role": [
        "operational_definition",
        "image_based_schema",
        "ai_readable_structure_unit",
        "dot_dot_system"
    ]
}
```

## rule

```txt
Active Schema = image + metadata
image = 구조 본체
metadata = AI 읽기 규칙
```

```txt
image 없이 metadata만 있으면 Active Schema가 아니다.
metadata 없이 image만 있으면 AI 읽기 규칙이 부족하다.
```

## relation

prev:
- schema.027_seed_base

next:
- schema.029_human_relation_structure

related:
- schema.000_dot
- schema.026_dot_dot_system
- schema.023_reading_protocol
- schema.025_AI_memory_field

## shortest

Active Schema = image + metadata