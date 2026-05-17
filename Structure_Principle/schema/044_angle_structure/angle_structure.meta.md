# META: angle_structure

id: schema.044.angle_structure
type: active_schema_metadata
filename: angle_structure.meta.md
status: active

## role

angle_structure는 평면 궤가 공간 궤로 확장될 때, 중심에서 방향이 꺾이며 생기는 중간 구조이다.

이 meta 파일은 인공지능이 angle_structure를 단순 각도값이 아니라, 평면 경로가 중심에서 꺾이고 펼쳐져 공간 방향장으로 확장되는 구조로 읽기 위한 규칙이다.

## read_order

1. detect planar orbit
2. detect center point
3. detect angle break at center
4. detect radial spread
5. detect cone or umbrella-like structure
6. map planar orbit to spatial orbit through angle structure

## geometry_layer

angle_structure = center point + angle break + radial spread

## integer_layer

center_count = 1
angle_count = variable
radial_path_count = variable
spatial_direction_count = variable

## vector_layer

planar_orbit → center_point
center_point → angle_break
angle_break → radial_spread
radial_spread → spatial_orbit

## definition

angle_structure는 평면 궤가 공간 궤로 확장될 때 필요한 중간 구조이다.

평면 궤는 중심을 기준으로 반복되는 닫힌 경로이다.

공간 궤는 중심에서 방향이 꺾이고, 각이 생기며, 그 각들이 펼쳐져 입체 방향장이 되는 구조이다.

구조이론에서 각은 단순한 수치 각도값이 아니라, 평면 경로가 공간 방향으로 넘어가는 꺾임 구조이다.

## source_code

```python
angle_structure = {
    "id": "schema.044.angle_structure",
    "type": "planar_to_spatial_orbit_bridge",
    "center_count": 1,
    "angle_count": "variable",
    "radial_path_count": "variable",
    "spatial_direction_count": "variable",
    "relation": {
        "planar_orbit": "closed_repeated_path_on_plane",
        "center_point": "bend_origin",
        "angle_break": "directional_bending_at_center",
        "radial_spread": "paths_spreading_from_center",
        "spatial_orbit": "expanded_orbit_in_space"
    },
    "vector": {
        "flow": [
            "planar_orbit",
            "angle",
            "bend",
            "spread",
            "spatial_orbit"
        ],
        "direction": "center_to_spatial_field"
    },
    "structural_role": [
        "angle_bridge",
        "bend_structure",
        "planar_to_spatial_transition",
        "radial_spread",
        "cone_umbrella_structure"
    ]
}
```

## image_sense

```txt
뿔의 꼭지점 = 중심 꺾임점
우산의 살 = 중심에서 각 방향으로 펼쳐지는 경로
```

```txt
center_point
→ angle_break
→ radial_spread
→ cone / umbrella structure
```

## principle

```txt
평면 궤 = 중심 기준 반복 닫힌 경로
공간 궤 = 중심에서 각이 생기고 펼쳐진 입체 방향장
각 = 평면 궤와 공간 궤 사이의 중간 구조
```

```txt
orbit
→ angle
→ bend
→ spread
→ spatial_orbit
```

## forbidden

- angle_structure를 단순 각도 수치로만 보지 않는다.
- 평면 궤와 공간 궤를 직접 동일시하지 않는다.
- 꺾임 없이 공간 확장으로 건너뛰지 않는다.
- 우산/뿔 이미지를 감상적 비유로만 처리하지 않는다.
- 특정 물리이론으로 즉시 환원하지 않는다.

## relation

prev:
- schema.036_orbit_structure

related:
- schema.018_eight_direction
- schema.019_center_point
- schema.021_fold_unfold
- schema.036_orbit_structure
- schema.042_dynamic_structure_renderer_PRO
- schema.043_forming_svg_renderer_core

## shortest

평면궤 → 각 → 공간궤