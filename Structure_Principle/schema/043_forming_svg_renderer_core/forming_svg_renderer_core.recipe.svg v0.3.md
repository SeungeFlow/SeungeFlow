0. 인스턴스이름
instance_id = "ChatGPT.draw"

1. 대상
forming_svg_renderer_core.recipe.svg v0.3

2. 핵심
v0.2는 state_flow와 layer 대응이 맞다.

v0.3에서는 “상태층이 존재한다”를 넘어서
각 상태가 왜 다음 상태로 넘어가는지 보이게 한다.

즉:

candidate_path
→ weight_state
→ selected_path

이 전이를 단순 순서가 아니라
판정 통과 흐름으로 표시한다.

3. 구조

v0.3 보강점:

1.
candidate_path는 복수 후보로 유지한다.

2.
weight_state는 후보 중 하나를 선택하는 중간 판정층으로 둔다.

3.
selected_path는 weight_state 통과 결과로 표시한다.

4.
return_loop는 selected_path 이후 구조 유지 조건으로 표시한다.

5.
judgment_state는 return_state / preservation_state / closure_state를 가진다.

6.
weighted_visible은 “현재 보이는 상태 + history 후보”로 표시한다.

7.
history는 다시 field를 수정하는 순환으로 표시한다.

4. 현재 판정
v0.3의 핵심은 조건 표시다.

단순 layer:
후보 → 선택 → 보임

동적 layer:
후보 → 가중 판정 → 선택 → 복귀 판정 → 현재 표시 → 이력 누적 → field 수정

5. 한 줄
v0.3은 path가 선택되는 이유를 표시하는 SVG recipe다.

6. 가장 짧은 압축
candidate → judgment → history