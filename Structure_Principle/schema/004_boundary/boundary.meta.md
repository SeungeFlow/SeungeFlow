# META: boundary

id: schema.004.boundary
type: active_schema_metadata
filename: boundary.meta.md
status: active

## role

boundary는 내부와 외부를 구분하는 경계 구조이다.

이 meta 파일은 인공지능이 boundary를 영역 분리와 보호 구조로 읽기 위한 규칙이다.

## read_order

1. detect enclosed cell
2. detect surrounding edge
3. separate inside and outside
4. detect boundary continuity
5. map separation to boundary

## geometry_layer

boundary = edge around cell

## integer_layer

boundary_count = 1
edge_count = variable

## vector_layer

inside → outside separation
direction = bidirectional

## definition

경계는 내부와 외부를 나누는 구조이다.

경계는 단순 선이 아니라, 영역을 구분하고 보호하는 역할을 가진다.

## source_code

```python
boundary = {
    "id": "schema.004.boundary",
    "geometry": "edge_structure",
    "boundary_count": 1,
    "relation": {
        "inside": "internal_region",
        "outside": "external_region"
    },
    "vector": {
        "direction": "inside_outside",
        "state": "separation"
    },
    "structural_role": [
        "separation",
        "protection",
        "interface"
    ]
}
```

## relation

prev:
- schema.003.cell

next:
- schema.005_position

related:
- schema.006_entity
- schema.007_safety

## shortest

경계 = 내부와 외부를 나누는 구조
