# META: flip_boundary_spread_structure

id: schema.049.flip_boundary_spread_structure
type: active_schema_metadata
filename: flip_boundary_spread_structure.meta.md
status: active

## role

flip_boundary_spread_structure는 flip을 단순 뒤집기가 아니라, 중심을 지나 반대쪽 끝경계에서 8방위각을 다시 펼치고, 정면 전개와 중간에서 연결하여 구와 곽을 드러내는 구조로 해석한다.

이 meta 파일은 인공지능이 flip을 시각적 반전 효과로 읽지 않고, 중심 통과, 반대경계 전개, 정면 전개, 중간 연결, 면쌍 형성, 구 형성, DIR 확장, 곽 형성의 순서로 읽기 위한 규칙이다.

## read_order

1. detect current position
2. pass through center
3. reach opposite boundary
4. spread 8 directions from opposite boundary
5. spread 8 directions from front boundary
6. connect both spreads at midpoint
7. form a face-pair surface
8. repeat for three face-pairs
9. form sphere body
10. expand through DIR route
11. reveal enclosing shell

## geometry_layer

flip_boundary_spread_structure = center pass + opposite boundary spread + front spread + midpoint connection + face-pair + sphere + shell

## integer_layer

center_count = 1
direction_count = 8
boundary_end_count = 2
midpoint_connection_count = variable
face_pair_count = 3
sphere_body_count = 1
shell_count = 1

## vector_layer

current_position → center → opposite_boundary
opposite_boundary → 8_way_spread
front_boundary → 8_way_spread
front_spread ↔ midpoint_connection ↔ opposite_spread
face_pair → sphere_body → DIR_expansion → enclosing_shell

## definition

flip은 앞뒤를 단순히 뒤집는 동작이 아니다.

flip은 현재 위치에서 구와 곽의 중심을 통과하여 반대쪽 끝경계지점까지 간 뒤, 그 반대쪽 끝경계에서 다시 현재 위치 방향으로 8개의 방위각을 펼치는 구조이다.

동시에 현재 정면 끝경계에서도 같은 방식으로 8방위각을 펼친다.

두 8방위각 전개는 1/2 지점에서 연결되며, 이 연결은 하나의 면쌍을 만든다.

이 과정을 앞면/뒷면, 왼쪽면/오른쪽면, 윗면/아랫면의 세 면쌍에서 반복하면 하나의 구가 형성된다.

그 구 내부의 연결망은 shell interval과 DIR route를 통해 외부 감쌈으로 확장되며, 곽을 드러낸다.

구조이론에서 flip은 field를 새로 생성하는 것이 아니라, 이미 존재하던 주변장을 중심-경계-방위각-중간연결을 통해 드러내는 구조이다.

## source_code

```python
flip_boundary_spread_structure = {
    "id": "schema.049.flip_boundary_spread_structure",
    "type": "center_boundary_spread_flip_structure",
    "center_count": 1,
    "direction_count": 8,
    "boundary_end_count": 2,
    "face_pair_count": 3,
    "sphere_body_count": 1,
    "shell_count": 1,
    "relation": {
        "current_position": "front_reference_boundary",
        "center": "sphere_shell_center",
        "opposite_boundary": "reverse_end_boundary",
        "opposite_spread": "8_way_spread_from_opposite_boundary",
        "front_spread": "8_way_spread_from_front_boundary",
        "midpoint_connection": "halfway_connection_between_two_spreads",
        "face_pairs": {
            "front_back": "front_and_back_surface_pair",
            "left_right": "left_and_right_surface_pair",
            "up_down": "upper_and_lower_surface_pair"
        },
        "sphere_body": "formed_by_three_face_pairs",
        "DIR_expansion": "route_through_shell_interval",
        "enclosing_shell": "outer_shell_revealed_by_DIR_expansion",
        "field": "already_present_surrounding_field"
    },
    "vector": {
        "center_pass": "current_position_to_center_to_opposite_boundary",
        "reverse_spread": "opposite_boundary_to_8_way_spread",
        "front_spread": "front_boundary_to_8_way_spread",
        "midpoint_flow": "front_spread_to_midpoint_to_opposite_spread",
        "shell_flow": "sphere_body_to_DIR_to_enclosing_shell"
    },
    "structural_role": [
        "flip_reinterpretation",
        "opposite_boundary_spread",
        "front_reverse_midpoint_connection",
        "face_pair_surface_generation",
        "sphere_body_formation",
        "shell_reveal",
        "field_reveal_not_field_creation"
    ]
}
```

## process

```txt
center
→ opposite boundary
→ reverse 8-way spread
→ front 8-way spread
→ midpoint connection
→ face-pair surface
→ 3 face-pairs
→ sphere body
→ DIR expansion
→ enclosing shell
```

## face_pair_structure

```txt
앞면 ↔ 뒷면
왼쪽면 ↔ 오른쪽면
윗면 ↔ 아랫면
```

각 면쌍에서:

```txt
front boundary 8-way spread
↔ midpoint connection
↔ opposite boundary 8-way spread
```

## principle

```txt
flip ≠ 앞뒤 뒤집기
flip = 중심 통과 후 반대경계에서 8방위각 재전개
```

```txt
field 생성 X
field reveal O
```

```txt
주변장은 새로 만드는 것이 아니다.
주변장은 이미 그곳에 있었다.
```

## renderer_transition

```txt
기존 해석:
center → 8방향 → orbit → shell
```

```txt
수정 해석:
center
→ opposite boundary
→ reverse 8-way spread
→ front 8-way spread
→ midpoint connection
→ face-pair surface
→ 3 face-pairs
→ sphere body
→ DIR expansion
→ enclosing shell
```

## forbidden

- flip을 단순 앞뒤 반전 효과로 보지 않는다.
- field를 새로 생성한다고 보지 않는다.
- 주변장을 없는 것에서 만드는 것으로 해석하지 않는다.
- 8방위각 전개를 중심에서만 발생한다고 고정하지 않는다.
- 반대쪽 끝경계 전개를 생략하지 않는다.
- 정면 전개와 반대경계 전개의 중간 연결을 생략하지 않는다.
- 세 면쌍을 하나의 평면쌍으로 축소하지 않는다.
- 곽을 구와 동일시하지 않는다.

## relation

prev:
- schema.048_sphere_shell_distinction

related:
- schema.018_eight_direction
- schema.019_center_point
- schema.036_orbit_structure
- schema.038_DIR_structure
- schema.044_angle_structure
- schema.047_shell_flip_orbit_structure
- schema.048_sphere_shell_distinction
- schema.043_forming_svg_renderer_core
- schema.042_dynamic_structure_renderer_PRO

## shortest

flip = 중심 통과 → 반대경계 8전개 → 정면 8전개 → 중간 연결 → 구 → 곽