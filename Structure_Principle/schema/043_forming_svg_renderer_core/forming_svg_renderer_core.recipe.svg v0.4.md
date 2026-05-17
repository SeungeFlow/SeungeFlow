0. 인스턴스이름
instance_id = "ChatGPT.draw"

1. 대상
forming_svg_renderer_core.recipe.svg v0.4

2. 핵심
v0.3은 최소 실행 recipe로 가능하다.

v0.4에서는 “저장 가능한 최종 원형”으로 정리한다.

수정 방향은 3개다.

1.
SVG 내부 metadata를 추가한다.

2.
각 layer에 data-state 속성을 붙인다.

3.
history → field 순환이 단순 화살표가 아니라 다음 cycle 입력임을 명시한다.

3. 구조

v0.4 추가 규칙:

```txt
<metadata>
  schema_id
  recipe_status
  state_flow
  layer_order
  forbidden
</metadata>