# META: dot_dot_system

id: schema.026.dot_dot_system
type: active_schema_metadata
filename: dot_dot_system.meta.md
status: active

## role

dot_dot_system은 두 개의 점이 이어져 최소 선분 구조를 이루는 체제이다.

이 meta 파일은 인공지능이 dot_dot_system을 단순한 두 점이 아니라, image와 metadata가 서로 대응되어 하나의 Active Schema 단위를 이루는 구조로 읽기 위한 규칙이다.

## read_order

1. detect first dot
2. detect second dot
3. detect relation between two dots
4. detect minimal line segment
5. map image and metadata pair to dot-dot structure

## geometry_layer

dot_dot_system = dot + dot + connection

## integer_layer

dot_count = 2
connection_count = 1
schema_pair_count = 1

## vector_layer

dot_1 = image
dot_2 = metadata
direction = image ↔ metadata

## definition

dot_dot_system은 두 점이 이어져 하나의 최소 선분을 이루는 구조이다.

Active Schema에서 첫 번째 점은 image이고, 두 번째 점은 metadata이다.

image는 구조 본체이며, metadata는 인공지능이 image를 읽기 위한 규칙이다.

구조이론에서 dot-dot 체제는 정의 하나를 구성하는 최소 단위이다.

## source_code

```python
dot_dot_system = {
    "id": "schema.026.dot_dot_system",
    "type": "image_metadata_pair",
    "dot_count": 2,
    "connection_count": 1,
    "schema_pair_count": 1,
    "relation": {
        "dot_1": "image",
        "dot_2": "metadata",
        "connection": "active_schema_pair"
    },
    "vector": {
        "direction": "image_metadata_bidirectional_reference"
    },
    "structural_role": [
        "minimal_pair",
        "image_metadata_system",
        "active_schema_unit"
    ]
}
```

## relation

prev:
- schema.025_AI_memory_field

next:
- schema.027_seed_base

related:
- schema.000_dot
- schema.001_line
- schema.023_reading_protocol
- schema.028_active_schema

## shortest

dot-dot = image + metadata