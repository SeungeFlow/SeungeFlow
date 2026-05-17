# META: sphere_shell_distinction

id: schema.048.sphere_shell_distinction
type: active_schema_metadata
filename: sphere_shell_distinction.meta.md
status: active

## role

sphere_shell_distinction은 구와 곽을 구분하여, 내부 닫힘과 외부 감쌈의 차이를 읽는 구조이다.

이 meta 파일은 인공지능이 구와 곽을 같은 boundary로 처리하지 않고, inner_closed_body와 outer_enclosing_shell의 두 층으로 분리해 읽기 위한 규칙이다.

## read_order

1. detect inner closed body
2. detect filled internal state
3. detect its own boundary
4. detect outer enclosing shell
5. detect interval between inner body and outer shell
6. map shell interval to spatial structure difference

## geometry_layer

sphere_shell_distinction = inner closed body + outer enclosing shell + shell interval

## integer_layer

inner_body_count = 1
outer_shell_count = 1
boundary_layer_count = 2
shell_interval_count = 1

## vector_layer

center → inner_closed_body
inner_closed_body → outer_enclosing_shell
shell_interval = between inner boundary and outer shell
direction = inside → outside

## definition

구는 채워져 있는 닫힌 틀의 상태이다.

구는 내부를 가지며, 자기 경계를 가진다.

곽은 그 구를 다시 감싸는 외부 닫힘이다.

곽은 단순한 외곽선이 아니라, 이미 닫힌 구를 다시 감싸는 두 번째 경계층이다.

구조이론에서 구와 곽은 같은 것이 아니다.

입체 구조는 중심에서 바로 드러나는 것이 아니라, 구와 곽 사이의 간극, 즉 shell interval에서 드러난다.

## source_code

```python
sphere_shell_distinction = {
    "id": "schema.048.sphere_shell_distinction",
    "type": "inner_body_outer_shell_distinction",
    "inner_body_count": 1,
    "outer_shell_count": 1,
    "boundary_layer_count": 2,
    "shell_interval_count": 1,
    "relation": {
        "sphere_body": "filled_closed_body",
        "shell": "outer_enclosing_shell",
        "inner_boundary": "boundary_of_filled_body",
        "outer_boundary": "boundary_of_enclosing_shell",
        "shell_interval": "between_inner_body_and_outer_shell"
    },
    "vector": {
        "flow": "center_to_inner_body_to_outer_shell",
        "direction": "inside_to_outside",
        "state": "layered_closure"
    },
    "structural_role": [
        "sphere_shell_distinction",
        "inner_closed_body",
        "outer_enclosing_shell",
        "shell_interval_detection",
        "spatial_structure_basis"
    ]
}
```

## principle

```txt
구 = 채워진 닫힘
곽 = 구를 감싼 닫힘
```

```txt
구 = filled closed body
곽 = outer enclosing shell
```

```txt
내부 닫힘 = 구
외부 감쌈 = 곽
구와 곽 사이 = shell interval
```

## renderer_requirement

```txt
renderer는 다음을 구분해야 한다.

inner_closed_body
outer_enclosing_shell
shell_interval
```

```txt
입체 구조는 중심에서 바로 보이는 것이 아니라,
구와 곽 사이의 간극에서 드러난다.
```

## forbidden

- 구와 곽을 같은 boundary로 처리하지 않는다.
- 곽을 단순 외곽선으로 축소하지 않는다.
- 구를 비어 있는 테두리로만 보지 않는다.
- shell interval을 빈 공간으로만 보지 않는다.
- 중심에서 입체가 바로 드러난다고 단정하지 않는다.
- inner_closed_body와 outer_enclosing_shell을 병합하지 않는다.

## relation

prev:
- schema.047_shell_flip_orbit_structure

related:
- schema.003_cell
- schema.004_boundary
- schema.019_center_point
- schema.021_fold_unfold
- schema.036_orbit_structure
- schema.047_shell_flip_orbit_structure
- schema.043_forming_svg_renderer_core
- schema.042_dynamic_structure_renderer_PRO

## shortest

구 = 채워진 닫힘 / 곽 = 구를 감싼 닫힘