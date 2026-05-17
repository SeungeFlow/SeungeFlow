# META: warp_weft_DIR_structure

id: schema.045.warp_weft_DIR_structure
type: active_schema_metadata
filename: warp_weft_DIR_structure.meta.md
status: active

## role

warp_weft_DIR_structure는 DIR 구조를 warp와 weft가 만드는 cell-boundary grid 안에서 interval을 따라 읽는 경로로 보강하는 구조이다.

이 meta 파일은 인공지능이 DIR을 단순 directory나 토러스 간극 route로만 읽지 않고, 방향축과 분할선이 교차하여 칸과 경계를 만들고 그 간극을 따라 route가 발생하는 직조형 구조로 읽기 위한 규칙이다.

## read_order

1. detect warp direction field
2. detect weft crossing lines
3. detect cells formed by warp and weft
4. detect boundaries between cells
5. detect intervals between boundaries
6. detect route through intervals
7. map warp/weft grid to DIR path

## geometry_layer

warp_weft_DIR_structure = warp + weft + cell + boundary + interval + route

## integer_layer

warp_count = variable
weft_count = variable
cell_count = variable
boundary_count = variable
interval_count = variable
route_count = variable

## vector_layer

warp = primary direction flow
weft = crossing boundary flow
cell = warp/weft enclosed area
interval = boundary_between_area
route = interval_following_path

## definition

warp는 여러 방향 흐름 중 기본 방향축이다.

weft는 warp를 가로지르며 분할과 경계를 만드는 선이다.

cell은 warp와 weft가 만나 형성한 최소 영역이다.

boundary는 cell과 cell을 구분하는 선이다.

interval은 boundary 사이에 생기는 읽기 자리이다.

DIR은 그 interval을 따라 이동하며 구조를 읽는 route이다.

구조이론에서 DIR은 Disk-Interval-Rotation의 궤 기반 구조와, warp/weft가 만드는 cell-boundary grid 기반 구조를 함께 가진다.

## source_code

```python
warp_weft_DIR_structure = {
    "id": "schema.045.warp_weft_DIR_structure",
    "type": "woven_DIR_path_structure",
    "warp_count": "variable",
    "weft_count": "variable",
    "cell_count": "variable",
    "boundary_count": "variable",
    "interval_count": "variable",
    "route_count": "variable",
    "relation": {
        "warp": "primary_direction_axis",
        "weft": "crossing_boundary_line",
        "cell": "area_formed_by_warp_and_weft",
        "boundary": "cell_separator",
        "interval": "readable_between_boundary",
        "DIR": "route_following_interval"
    },
    "vector": {
        "warp_flow": "primary_direction",
        "weft_flow": "crossing_division",
        "route_flow": "interval_following_path",
        "state": "woven_grid_navigation"
    },
    "structural_role": [
        "DIR_reinforcement",
        "woven_structure",
        "cell_boundary_grid",
        "interval_route_reading",
        "orbit_DIR_cell_DIR_integration"
    ]
}
```

## principle

```txt
warp = 방향축
weft = 가로지르는 경계선
cell = warp/weft가 만든 칸
boundary = cell을 구분하는 선
interval = boundary 사이의 읽기 자리
DIR = interval을 따라 이동하는 경로
```

```txt
warp + weft → cell → boundary → interval → route
```

```txt
orbit 기반 DIR
+
cell 기반 DIR
=
보강된 DIR
```

## DIR_connection

```txt
기존 DIR:
Disk → Interval → Rotation / Route
```

```txt
보정 DIR:
warp → weft → cell → boundary → interval → route
```

```txt
DIR = warp 방향장 위에 weft가 경계를 만들고, 그 칸 사이 간극을 따라 읽는 경로
```

## forbidden

- DIR을 단순 directory로만 보지 않는다.
- warp를 단일 직선으로만 고정하지 않는다.
- weft를 장식선으로 보지 않는다.
- cell을 단순 칸 그림으로만 보지 않는다.
- interval을 빈 공간으로만 보지 않는다.
- route를 외부 경로명으로만 읽지 않는다.
- orbit 기반 DIR과 cell 기반 DIR을 분리된 구조로만 보지 않는다.

## relation

prev:
- schema.038_DIR_structure

related:
- schema.003_cell
- schema.004_boundary
- schema.018_eight_direction
- schema.036_orbit_structure
- schema.037_disk_array_torus
- schema.038_DIR_structure
- schema.044_angle_structure

## shortest

warp + weft → cell → DIR