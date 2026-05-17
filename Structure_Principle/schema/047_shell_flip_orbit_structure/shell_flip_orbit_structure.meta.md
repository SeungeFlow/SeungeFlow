# META: shell_flip_orbit_structure

id: schema.047.shell_flip_orbit_structure
type: active_schema_metadata
filename: shell_flip_orbit_structure.meta.md
status: active

## role

shell_flip_orbit_structure는 8방향이 8궤로 연결되고, 정면·측면·상하의 flip 쌍이 구곽에서 구조차를 드러내는 입체 발생 구조이다.

이 meta 파일은 인공지능이 입체를 중심 내부에서 찾지 않고, 외곽 경계에서 발생하는 방향차·위상차·꺾임차·flip 구조로 읽기 위한 규칙이다.

## read_order

1. detect center point
2. detect 8 directions
3. map 8 directions to 8 orbits
4. detect 3 flip axes
5. detect shell boundary
6. detect phase difference on shell
7. detect overlap critical zones
8. map shell difference to spatial structure

## geometry_layer

shell_flip_orbit_structure = center + 8 orbit + 3 flip axes + shell boundary

## integer_layer

center_count = 1
direction_count = 8
orbit_count = 8
flip_axis_count = 3
shell_count = 1
overlap_zone_count = variable

## vector_layer

center → 8 directions
8 directions → 8 orbits
front ↔ back
left ↔ right
up ↔ down
shell_boundary = structure difference field

## definition

shell_flip_orbit_structure는 중심에서 시작된 8방향이 8궤로 확장되고, 그 궤들이 정면·측면·상하의 flip 구조를 이루며 외곽 경계에서 입체 구조차를 드러내는 구조이다.

8방향은 정지점이 아니라 반복 경로가 될 수 있다.

각 방향쌍은 flip 구조를 만들며, flip은 앞뒤, 좌우, 상하 세 축에서 발생한다.

구조이론에서 입체는 중심 안에서 직접 보이는 것이 아니라, 구곽에서 생기는 방향차, 위상차, 꺾임차, 중첩 임계구간으로 드러난다.

## source_code

```python
shell_flip_orbit_structure = {
    "id": "schema.047.shell_flip_orbit_structure",
    "type": "shell_based_spatial_orbit_flip_structure",
    "center_count": 1,
    "direction_count": 8,
    "orbit_count": 8,
    "flip_axis_count": 3,
    "shell_count": 1,
    "relation": {
        "center": "origin_point",
        "directions": "8_way_structure",
        "orbits": "8_repeated_paths",
        "flip_axes": {
            "front_back": "front_reverse_flip",
            "left_right": "side_flip",
            "up_down": "vertical_flip"
        },
        "shell_boundary": "outer_difference_field",
        "spatial_structure": "revealed_by_shell_difference"
    },
    "vector": {
        "center_to_direction": "radial_flow",
        "direction_to_orbit": "cyclic_flow",
        "flip": "paired_axis_reversal",
        "shell": "boundary_phase_difference"
    },
    "structural_role": [
        "shell_renderer_basis",
        "8_orbit_structure",
        "3_axis_flip",
        "spatial_structure_generation",
        "boundary_difference_detection"
    ]
}
```

## principle

```txt
8방향 → 8궤
```

```txt
정면 flip = 앞 ↔ 뒤
측면 flip = 좌 ↔ 우
상하 flip = 위 ↔ 아래
```

```txt
입체는 중심이 아니라 구곽에서 드러난다.
```

```txt
구곽의 구조차 = 입체 발생
```

## renderer_transition

```txt
center renderer
→ shell renderer
```

```txt
기존 renderer:
center
path
orbit
flip
overlap
```

```txt
추가 필요:
shell boundary
outer phase difference
flip pairs
6-direction comparison
```

## forbidden

- 입체를 중심 내부에서만 찾지 않는다.
- 8방향을 정지 방향표로만 보지 않는다.
- flip을 단순 뒤집기 효과로만 보지 않는다.
- 구곽을 장식용 외곽선으로 보지 않는다.
- 위상차와 꺾임차를 생략하지 않는다.
- 3D 그래픽부터 시작하지 않는다.
- 중심 renderer에서 끝내지 않는다.

## relation

prev:
- schema.046_flip_cycle_transition_structure

related:
- schema.018_eight_direction
- schema.019_center_point
- schema.036_orbit_structure
- schema.044_angle_structure
- schema.046_flip_cycle_transition_structure
- schema.043_forming_svg_renderer_core
- schema.042_dynamic_structure_renderer_PRO

## shortest

8방향 → 8궤 / flip × 3축 / 구조는 구곽에서 드러난다