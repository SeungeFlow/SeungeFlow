# META: forming_svg_renderer_core

id: schema.043.forming_svg_renderer_core
type: active_schema_metadata
filename: forming_svg_renderer_core.meta.md
status: active

## role

forming_svg_renderer_core는 구조가 완성된 결과를 그리는 렌더러가 아니라, field 안에서 node가 놓이고, path가 형성되고, 후보 경로가 선택되며, 복귀 조건과 history에 의해 현재 visible 상태가 결정되는 과정을 SVG 상태층으로 표시하는 최소 실행 코어이다.

이 meta 파일은 인공지능이 forming_svg_renderer_core를 PNG 생성기나 정적 다이어그램이 아니라, meta.md + recipe.svg 기반의 dynamic SVG state renderer로 읽기 위한 규칙이다.

## read_order

1. detect field
2. detect node
3. detect forming_path
4. detect candidate_path
5. detect weight_state
6. detect selected_path
7. detect return_loop
8. detect judgment_state
9. detect weighted_visible
10. detect history
11. map all states to dynamic SVG rendering cycle

## geometry_layer

forming_svg_renderer_core = field + node + forming_path + candidate_path + selected_path + return_loop

## integer_layer

field_count = 1
node_count = variable
forming_path_count = variable
candidate_path_count = variable
selected_path_count = variable
return_loop_count = variable
cycle_count = variable

## vector_layer

field → node
node → forming_path
forming_path → candidate_path
candidate_path → weight_state
weight_state → selected_path
selected_path → return_loop
return_loop → judgment_state
judgment_state → weighted_visible
weighted_visible → history
history → field

## state_flow

```txt
field
→ node
→ forming_path
→ candidate_path
→ weight_state
→ selected_path
→ return_loop
→ judgment_state
→ weighted_visible
→ history
```

## definition

forming_svg_renderer_core는 Dynamic Structure Renderer PRO의 하위 실행 코어이다.

이 코어는 완성된 구조를 그리는 것이 아니라, 구조가 형성되고 선택되고 복귀 판정을 거쳐 현재 visible 상태가 되는 과정을 표시한다.

forming_svg_renderer_core는 PNG 생성기가 아니다.

forming_svg_renderer_core는 SVG recipe를 사용하여 상태층을 표현하는 dynamic SVG state renderer이다.

구조이론에서 forming_svg_renderer_core의 목적은 formed 결과를 표시하는 것이 아니라, forming 과정을 표시하는 것이다.

## layer_structure

SVG 내부 layer는 다음 최소 구조를 가진다.

```txt
view_layer
field_layer
node_layer
forming_layer
candidate_layer
selected_layer
return_layer
history_layer
judgment_layer
relation_layer
```

## layer_definition

```txt
view_layer = 전체 SVG 표시 영역
field_layer = 가능성 장 / 여백 / 구조가 발생할 공간
node_layer = 고정점 / 기준점
forming_layer = 아직 확정되지 않은 형성 중 경로
candidate_layer = 선택 후보 경로들
selected_layer = 현재 선택된 경로
return_layer = 복귀 조건을 확인하는 루프
history_layer = 이전 선택 이력
judgment_layer = 복귀/보존 판정 결과
relation_layer = node와 path 사이의 관계 표시
```

## candidate_selected_rule

candidate_path와 selected_path는 시각 효과가 아니라 구조 상태로 구분한다.

```txt
candidate_path = 아직 선택되지 않은 가능한 경로
selected_path = weight_state와 judgment_state를 통과한 현재 경로
```

```txt
candidate_path는 복수일 수 있다.
selected_path는 한 cycle 안에서 단일 또는 제한된 집합이다.
candidate_path는 history에 직접 기록되지 않는다.
selected_path는 weighted_visible을 거쳐 history에 기록될 수 있다.
```

## return_loop_rule

return_loop는 단순 원형 화살표가 아니다.

return_loop는 구조 유지 조건이다.

return_loop가 가져야 할 최소 판정값은 다음이다.

```txt
return_state: true / false
preservation_state: true / false
closure_state: true / false
```

최소 판정식은 다음이다.

```txt
return_loop_valid =
return_state
AND preservation_state
AND closure_state
```

## weighted_visible_rule

weighted_visible은 최종 출력이 아니다.

weighted_visible은 다음 history가 되기 직전의 현재 상태이다.

```txt
selected_path
→ judgment_state
→ weighted_visible
→ history
```

```txt
weighted_visible = 현재 보이는 상태 + 다음 history 후보
```

## source_code

```python
forming_svg_renderer_core = {
    "id": "schema.043.forming_svg_renderer_core",
    "type": "dynamic_svg_state_renderer_core",
    "parent": "schema.042.dynamic_structure_renderer_PRO",
    "recipe": "forming_svg_renderer_core.recipe.svg",
    "image_status": "not_required",
    "recipe_status": "active",
    "state_flow": [
        "field",
        "node",
        "forming_path",
        "candidate_path",
        "weight_state",
        "selected_path",
        "return_loop",
        "judgment_state",
        "weighted_visible",
        "history"
    ],
    "layers": {
        "view_layer": "svg_view_area",
        "field_layer": "possibility_field",
        "node_layer": "fixed_reference_nodes",
        "forming_layer": "paths_in_formation",
        "candidate_layer": "possible_paths",
        "selected_layer": "currently_selected_path",
        "return_layer": "return_condition_loop",
        "history_layer": "previous_selection_records",
        "judgment_layer": "return_preservation_closure_judgment",
        "relation_layer": "node_path_relation_mapping"
    },
    "state_definition": {
        "field": "structure_generation_space",
        "node": "fixed_reference_point",
        "forming_path": "path_in_formation",
        "candidate_path": "possible_unselected_path",
        "weight_state": "candidate_weight_condition",
        "selected_path": "current_path_after_weight_and_judgment",
        "return_loop": "structure_maintenance_condition",
        "judgment_state": "return_preservation_closure_result",
        "weighted_visible": "current_visible_state_before_history",
        "history": "record_of_selected_visible_state"
    },
    "return_loop_condition": {
        "return_state": "boolean",
        "preservation_state": "boolean",
        "closure_state": "boolean",
        "valid_if": [
            "return_state == True",
            "preservation_state == True",
            "closure_state == True"
        ]
    },
    "structural_role": [
        "forming_renderer",
        "dynamic_svg_state_renderer",
        "path_selection_engine",
        "history_weighted_visible_engine",
        "minimum_execution_core"
    ]
}
```

## svg_recipe_minimum_structure

`forming_svg_renderer_core.recipe.svg`는 다음 layer id를 가져야 한다.

```xml
<svg id="forming_svg_renderer_core" xmlns="http://www.w3.org/2000/svg">
  <g id="view_layer"></g>
  <g id="field_layer"></g>
  <g id="node_layer"></g>
  <g id="forming_layer"></g>
  <g id="candidate_layer"></g>
  <g id="selected_layer"></g>
  <g id="return_layer"></g>
  <g id="history_layer"></g>
  <g id="judgment_layer"></g>
  <g id="relation_layer"></g>
</svg>
```

## file_structure

```txt
schema/043_forming_svg_renderer_core/
├── forming_svg_renderer_core.meta.md
└── forming_svg_renderer_core.recipe.svg
```

## principle

```txt
formed X
forming O
```

```txt
PNG X
SVG recipe O
```

```txt
static diagram X
dynamic state renderer O
```

```txt
field → node → forming_path → candidate_path
→ weight_state → selected_path
→ return_loop → judgment_state
→ weighted_visible → history
```

## forbidden

- PNG 중심 구조를 넣지 않는다.
- 3D 그래픽부터 시작하지 않는다.
- 예쁜 시각화 목적을 우선하지 않는다.
- 정적 다이어그램으로 끝내지 않는다.
- 일반 그래프 이론으로 환원하지 않는다.
- 특정 과학 이론으로 환원하지 않는다.
- formed 결과만 표시하지 않는다.
- candidate와 selected를 색상 차이로만 구분하지 않는다.
- return_loop를 장식용 화살표로 처리하지 않는다.
- history 없이 매 cycle을 독립 실행하지 않는다.

## relation

prev:
- schema.042_dynamic_structure_renderer_PRO

parent:
- schema.042_dynamic_structure_renderer_PRO

related:
- schema.010_sequence_structure
- schema.012_matrix_product
- schema.013_return_preservation
- schema.014_structure_judgment
- schema.018_eight_direction
- schema.019_center_point
- schema.025_AI_memory_field
- schema.041_dynamic_structure_engine_gpu_hbm_ocf
- schema.042_dynamic_structure_renderer_PRO

## shortest

forming SVG = path가 선택되는 과정