0. 인스턴스이름
instance_id = "ChatGPT.draw"

1. 대상
forming_svg_renderer_core.recipe.svg v0.1

2. 핵심
이제 recipe.svg의 최소 source를 내린다.

3. 구조
아래 SVG는 “그림”이 아니라 상태층 구조다.

- view_layer
- field_layer
- node_layer
- forming_layer
- candidate_layer
- selected_layer
- return_layer
- history_layer
- judgment_layer
- relation_layer

4. recipe.svg

```xml
<svg id="forming_svg_renderer_core"
     xmlns="http://www.w3.org/2000/svg"
     width="1200"
     height="420"
     viewBox="0 0 1200 420">

  <title>forming_svg_renderer_core.recipe.svg</title>

  <style>
    .bg { fill: white; }
    .field { fill: none; stroke: #dddddd; stroke-width: 1; }
    .node { fill: #111111; }
    .label { font-family: monospace; font-size: 18px; fill: #111111; }
    .small { font-family: monospace; font-size: 14px; fill: #555555; }
    .forming { fill: none; stroke: #999999; stroke-width: 2; stroke-dasharray: 6 8; }
    .candidate { fill: none; stroke: #bbbbbb; stroke-width: 2; stroke-dasharray: 4 10; }
    .selected { fill: none; stroke: #111111; stroke-width: 3; }
    .return { fill: none; stroke: #666666; stroke-width: 2; stroke-dasharray: 8 6; }
    .history { fill: none; stroke: #888888; stroke-width: 2; marker-end: url(#arrow); }
    .judgment { fill: #ffffff; stroke: #111111; stroke-width: 2; }
  </style>

  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10"
            refX="8" refY="5" orient="auto">
      <path d="M0,0 L10,5 L0,10 Z" fill="#111111"/>
    </marker>
  </defs>

  <g id="view_layer">
    <rect class="bg" x="0" y="0" width="1200" height="420"/>
  </g>

  <g id="field_layer">
    <rect class="field" x="80" y="90" width="1040" height="210" rx="18"/>
    <text class="small" x="90" y="82">field_layer = possibility field</text>
  </g>

  <g id="node_layer">
    <circle id="node_A" class="node" cx="180" cy="200" r="10"/>
    <circle id="node_B" class="node" cx="1020" cy="200" r="10"/>
    <text class="label" x="145" y="235">A</text>
    <text class="label" x="1008" y="235">B</text>
  </g>

  <g id="forming_layer">
    <path id="forming_path"
          class="forming"
          d="M180 200 C360 120, 520 280, 700 200 S880 120, 1020 200"/>
    <text class="small" x="445" y="115">forming_path</text>
  </g>

  <g id="candidate_layer">
    <path id="candidate_path_1"
          class="candidate"
          d="M180 200 C360 60, 800 60, 1020 200"/>
    <path id="candidate_path_2"
          class="candidate"
          d="M180 200 C360 340, 800 340, 1020 200"/>
    <text class="small" x="475" y="340">candidate_paths</text>
  </g>

  <g id="selected_layer">
    <path id="selected_path"
          class="selected"
          d="M180 200 C420 170, 760 230, 1020 200"/>
    <text class="small" x="510" y="220">selected_path</text>
  </g>

  <g id="return_layer">
    <path id="return_loop"
          class="return"
          d="M1020 200 C930 310, 270 310, 180 200"/>
    <text class="small" x="500" y="315">return_loop</text>
  </g>

  <g id="judgment_layer">
    <rect id="judgment_state" class="judgment" x="520" y="30" width="160" height="42" rx="8"/>
    <text class="small" x="548" y="57">judgment: pass</text>
  </g>

  <g id="history_layer">
    <path id="history_to_field"
          class="history"
          d="M600 72 C600 20, 100 20, 100 105"/>
    <text class="small" x="120" y="30">history → field</text>
  </g>

  <g id="relation_layer">
    <text class="small" x="80" y="380">
      field → node → forming_path → candidate_path → weight_state → selected_path → return_loop → judgment_state → weighted_visible → history
    </text>
  </g>

</svg>