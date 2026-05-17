0. 인스턴스이름
instance_id = "ChatGPT.draw"

1. 대상
forming_svg_renderer_core.recipe.svg v0.2 source

2. 핵심
v0.2는 schema.043의 state_flow를 SVG layer 구조와 정확히 맞춘 최소 recipe다.

3. recipe.svg

```xml
<svg id="forming_svg_renderer_core"
     xmlns="http://www.w3.org/2000/svg"
     width="1200"
     height="460"
     viewBox="0 0 1200 460">

  <title>forming_svg_renderer_core.recipe.svg</title>

  <style>
    .bg { fill: white; }
    .field { fill: none; stroke: #dddddd; stroke-width: 1; }
    .node { fill: #111111; }
    .label { font-family: monospace; font-size: 18px; fill: #111111; }
    .small { font-family: monospace; font-size: 14px; fill: #555555; }
    .forming { fill: none; stroke: #999999; stroke-width: 2; stroke-dasharray: 6 8; }
    .candidate { fill: none; stroke: #bbbbbb; stroke-width: 2; stroke-dasharray: 4 10; }
    .weight { fill: #ffffff; stroke: #777777; stroke-width: 2; }
    .selected { fill: none; stroke: #111111; stroke-width: 3; }
    .return { fill: none; stroke: #666666; stroke-width: 2; stroke-dasharray: 8 6; }
    .judgment { fill: #ffffff; stroke: #111111; stroke-width: 2; }
    .visible { fill: #ffffff; stroke: #111111; stroke-width: 2; }
    .history { fill: none; stroke: #888888; stroke-width: 2; marker-end: url(#arrow); }
  </style>

  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10"
            refX="8" refY="5" orient="auto">
      <path d="M0,0 L10,5 L0,10 Z" fill="#111111"/>
    </marker>
  </defs>

  <g id="view_layer">
    <rect class="bg" x="0" y="0" width="1200" height="460"/>
  </g>

  <g id="field_layer">
    <rect class="field" x="80" y="110" width="1040" height="220" rx="18"/>
    <text class="small" x="90" y="100">field_layer = possibility field</text>
  </g>

  <g id="node_layer">
    <circle id="node_A" class="node" cx="180" cy="220" r="10"/>
    <circle id="node_B" class="node" cx="1020" cy="220" r="10"/>
    <text class="label" x="145" y="255">A</text>
    <text class="label" x="1008" y="255">B</text>
  </g>

  <g id="forming_layer">
    <path id="forming_path"
          class="forming"
          d="M180 220 C360 140, 520 300, 700 220 S880 140, 1020 220"/>
    <text class="small" x="445" y="132">forming_path</text>
  </g>

  <g id="candidate_layer">
    <path id="candidate_path_1"
          class="candidate"
          d="M180 220 C360 80, 800 80, 1020 220"/>
    <path id="candidate_path_2"
          class="candidate"
          d="M180 220 C360 360, 800 360, 1020 220"/>
    <text class="small" x="475" y="360">candidate_paths</text>
  </g>

  <g id="weight_layer">
    <rect id="weight_state" class="weight" x="520" y="155" width="160" height="38" rx="8"/>
    <text class="small" x="548" y="179">weight_state</text>
  </g>

  <g id="selected_layer">
    <path id="selected_path"
          class="selected"
          d="M180 220 C420 190, 760 250, 1020 220"/>
    <text class="small" x="510" y="240">selected_path</text>
  </g>

  <g id="return_layer">
    <path id="return_loop"
          class="return"
          d="M1020 220 C930 335, 270 335, 180 220"/>
    <text class="small" x="500" y="335">return_loop</text>
  </g>

  <g id="judgment_layer">
    <rect id="judgment_state" class="judgment" x="520" y="35" width="170" height="42" rx="8"/>
    <text class="small" x="548" y="62">judgment_state</text>
  </g>

  <g id="weighted_visible_layer">
    <rect id="weighted_visible" class="visible" x="790" y="35" width="210" height="42" rx="8"/>
    <text class="small" x="815" y="62">weighted_visible</text>
  </g>

  <g id="history_layer">
    <path id="visible_to_history"
          class="history"
          d="M895 77 C895 20, 230 20, 120 110"/>
    <text class="small" x="250" y="30">weighted_visible → history → field</text>
  </g>

  <g id="relation_layer">
    <text class="small" x="80" y="420">
      field → node → forming_path → candidate_path → weight_state → selected_path → return_loop → judgment_state → weighted_visible → history → field
    </text>
  </g>

</svg>