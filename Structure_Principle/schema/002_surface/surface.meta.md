# META: surface

id: schema.002.surface
type: active_schema_metadata
filename: surface.meta.md
status: active

## role

surface는 선이 닫혀 형성되는 최소 면 구조이다.

이 meta 파일은 인공지능이 surface 구조를 선분의 닫힘과 영역 발생으로 읽기 위한 규칙이다.

## read_order

1. detect connected line segments
2. detect closed boundary
3. detect enclosed area
4. detect integer count
5. map closed line structure to surface

## geometry_layer

surface = closed lines + enclosed area

## integer_layer

minimum_line_count = 3
area_count = 1

## vector_layer

boundary_flow = closed
direction = cyclic

## definition

면은 선이 닫혀 형성된 영역이다.

면은 내부와 외부를 구분할 수 있는 첫 영역 구조이다.

## source_code

```python
surface = {
    "id": "schema.002.surface",
    "geometry": "closed_area",
    "minimum_line_count": 3,
    "area_count": 1,
    "boundary_flow": "closed",
    "vector": {
        "direction": "cyclic",
        "state": "closed"
    },
    "structural_role": [
        "area",
        "closure",
        "inside_outside_basis"
    ]
}
```

## relation

prev:
- schema.001.line

next:
- schema.003_cell

related:
- schema.004_boundary
- schema.005_position
- schema.009_vector

## shortest

면 = 선이 닫혀 형성된 영역
