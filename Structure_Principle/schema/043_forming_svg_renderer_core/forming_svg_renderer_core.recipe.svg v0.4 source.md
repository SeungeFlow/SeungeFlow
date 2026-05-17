0. 인스턴스이름
instance_id = "ChatGPT.draw"

1. 대상
forming_svg_renderer_core.recipe.svg v0.4 source

2. 핵심
v0.4는 GitHub에 저장 가능한 첫 dynamic SVG state recipe다.

3. recipe.svg

```xml
<svg id="forming_svg_renderer_core"
     xmlns="http://www.w3.org/2000/svg"
     width="1200"
     height="520"
     viewBox="0 0 1200 520">

  <title>forming_svg_renderer_core.recipe.svg</title>

  <metadata id="recipe_metadata">
    schema_id: schema.043.forming_svg_renderer_core
    recipe_status: active
    renderer_type: dynamic_svg_state_renderer
    state_flow:
      field -> node -> forming_path -> candidate_path -> weight_state
      -> selected_path -> return_loop -> judgment_state
      -> weighted_visible -> history -> field
    layer_order:
      view_layer, field_layer, node_layer, forming_layer,
      candidate_layer, weight_layer, selected_layer, return_layer,
      judgment_layer, weighted_visible_layer, history_layer, relation_layer
    principle:
      formed X / forming O
      PNG X / SVG recipe O
  </metadata>

  <style>
    .bg { fill: white; }
    .field { fill: none; stroke: #dddddd; stroke-width: 1; }
    .node { fill: #111111; }
    .label { font-family: monospace; font-size: 18px; fill: #111111; }
    .small { font-family: monospace; font-size: 14px; fill: #555555; }
    .tiny { font-family: monospace; font-size: 12px; fill: #666666; }
    .forming { fill: none; stroke: #999999; stroke-width: 2; stroke-dasharray: 6 8; }
    .candidate { fill: none; stroke: #bbbbbb; stroke-width: 2; stroke-dasharray: 4 10; }
    .selected { fill: none; stroke: #111111; stroke-width: 3; }
    .return { fill: none; stroke: #666666; stroke-width: 2; stroke-dasharray: 8 6; }
    .state_box { fill: #ffffff; stroke: #111111; stroke-width: 1.6; }
    .soft_box { fill: #ffffff; stroke: #777777; stroke-width: 1.4; }
    .arrow { fill: none; stroke: #111111; stroke-width: 1.8; marker-end: url(#arrow); }
  </style>

  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10"
            refX="8" refY="5" orient="auto">
      <path d="M0,0 L10,5 L0,10 Z" fill="#111111"/>
    </marker>
  </defs>

  <g id="view_layer" data-state="view">
    <rect class="bg" x="0" y="0" width="1200" height="520"/>
  </g>

  <g id="field_layer" data-state="field">
    <rect class="field" x="80" y="135" width="1040" height="230" rx="18"/>
    <text class="small" x="90" y="125">field_layer = possibility field</text>
  </g>

  <g id="node_layer" data-state="node">
    <circle id="node_A" class="node" cx="180" cy="250" r="10"/>
    <circle id="node_B" class="node" cx="1020" cy="250" r="10"/>
    <text class="label" x="145" y="285">A</text>
    <text class="label" x="1008" y="285">B</text>
  </g>

  <g id="forming_layer" data-state="forming_path">
    <path id="forming_path"
          class="forming"
          d="M180 250 C360 170, 520 330, 700 250 S880 170, 1020 250"/>
    <text class="small" x="440" y="162">forming_path</text>
  </g>

  <g id="candidate_layer" data-state="candidate_path">
    <path id="candidate_path_1"
          class="candidate"
          d="M180 250 C360 100, 800 100, 1020 250"/>
    <path id="candidate_path_2"
          class="candidate"
          d="M180 250 C360 400, 800 400, 1020 250"/>
    <text class="small" x="455" y="398">candidate_paths</text>
  </g>

  <g id="weight_layer" data-state="weight_state">
    <rect id="weight_state" class="soft_box" x="500" y="185" width="200" height="50" rx="8"/>
    <text class="small" x="532" y="207">weight_state</text>
    <text class="tiny" x="525" y="225">candidate score / memory influence</text>
  </g>

  <g id="selected_layer" data-state="selected_path">
    <path id="selected_path"
          class="selected"
          d="M180 250 C420 220, 760 280, 1020 250"/>
    <text class="small" x="510" y="270">selected_path</text>
  </g>

  <g id="return_layer" data-state="return_loop">
    <path id="return_loop"
          class="return"
          d="M1020 250 C930 375, 270 375, 180 250"/>
    <text class="small" x="500" y="375">return_loop</text>
  </g>

  <g id="judgment_layer" data-state="judgment_state">
    <rect id="judgment_state" class="state_box" x="410" y="40" width="380" height="68" rx="8"/>
    <text class="small" x="438" y="64">judgment_state</text>
    <text class="tiny" x="438" y="86">return + preservation + closure</text>
  </g>

  <g id="weighted_visible_layer" data-state="weighted_visible">
    <rect id="weighted_visible" class="state_box" x="840" y="40" width="240" height="68" rx="8"/>
    <text class="small" x="868" y="64">weighted_visible</text>
    <text class="tiny" x="868" y="86">current view + history candidate</text>
  </g>

  <g id="history_layer" data-state="history_to_next_field">
    <path id="visible_to_history_to_field"
          class="arrow"
          d="M960 108 C960 20, 230 20, 120 135"/>
    <text class="small" x="250" y="30">weighted_visible → history → next field</text>
  </g>

  <g id="relation_layer" data-state="state_flow_relation">
    <text class="small" x="80" y="470">
      field → node → forming_path → candidate_path → weight_state → selected_path → return_loop → judgment_state → weighted_visible → history → field
    </text>
    <text class="tiny" x="80" y="495">
      candidate_path = possibility / selected_path = weight + judgment passed current path / weighted_visible = next history candidate
    </text>
  </g>

</svg>