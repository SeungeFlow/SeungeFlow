# META: cell

id: schema.003.cell
type: active_schema_metadata
filename: cell.meta.md
status: active

## role

cell은 닫힌 면이 최소 자리영역으로 읽히는 구조이다.

이 meta 파일은 인공지능이 cell 구조를 값이 놓일 수 있는 최소 영역 단위로 읽기 위한 규칙이다.

## read_order

1. detect closed surface
2. detect enclosed unit area
3. detect boundary around the area
4. detect integer count
5. map enclosed area to cell

## geometry_layer

cell = closed surface as unit area

## integer_layer

cell_count = 1
boundary_count = 1

## vector_layer

inside = cell interior
outside = external area
direction = inside ↔ outside

## definition

칸은 값이 놓일 수 있는 최소 영역 단위이다.

칸은 점보다 크고, 선보다 닫혀 있으며, 면을 자리로 읽는 구조이다.

## source_code

```python
cell = {
    "id": "schema.003.cell",
    "geometry": "unit_area",
    "cell_count": 1,
    "boundary_count": 1,
    "relation": {
        "inside": "cell_interior",
        "outside": "external_area"
    },
    "vector": {
        "direction": "inside_outside",
        "state": "bounded"
    },
    "structural_role": [
        "unit_area",
        "position_area",
        "value_container"
    ]
}
```

## relation

prev:
- schema.002.surface

next:
- schema.004_boundary

related:
- schema.005_position
- schema.008_integer
- schema.009_vector

## shortest

칸 = 최소 자리영역
