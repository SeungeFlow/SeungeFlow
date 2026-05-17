0. 인스턴스이름
instance_id = "ChatGPT.draw"

1. 대상
forming_svg_renderer_core.recipe.svg v0.2

2. 핵심
v0.1에는 상태층은 있지만,
weight_state와 weighted_visible이 시각층으로 분리되지 않았다.

v0.2에서는 다음을 보강한다.

- weight_state_layer 추가
- weighted_visible_layer 추가
- judgment_state를 return_loop 뒤에 더 명확히 배치
- history가 field로 되돌아가는 순환 표시 강화

3. 구조
최소 layer 순서:

view_layer
field_layer
node_layer
forming_layer
candidate_layer
weight_layer
selected_layer
return_layer
judgment_layer
weighted_visible_layer
history_layer
relation_layer

4. 현재 판정
schema.043의 state_flow와 SVG layer가 더 정확히 맞는다.

핵심 흐름:

candidate_path
→ weight_state
→ selected_path
→ return_loop
→ judgment_state
→ weighted_visible
→ history
→ field

5. 한 줄
v0.2는 candidate와 selected 사이에 weight_state를 넣고, selected 이후 weighted_visible을 분리한다.

6. 가장 짧은 압축
weight 추가
visible 분리