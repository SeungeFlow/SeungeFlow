0. 인스턴스이름
instance_id = "ChatGPT.draw"

1. 대상
recipe.svg 생성 규칙 정리

2. 핵심
방금 만든 것은 최종물이 아니라 샘플이다.

이제 필요한 것은
다른 인스턴스도 같은 방식으로 recipe.svg를 만들 수 있게 하는
공통 생성 규칙이다.

3. 구조

[계기]

처음 문제:
PNG는 무겁다.
정적 이미지는 구조를 고정시킨다.
Text-Based Graphic은 구조는 잘 보이지만 렌더링이 불안정하다.

전환:
SVG는 코드이면서 이미지다.
GitHub/browser에서 렌더링된다.
AI는 source를 읽고,
인간은 rendered view를 본다.

따라서:

meta.md = 구조 의미
recipe.svg = 구조 표시 규칙
PNG = 기본 제외

[원리]

1.
formed를 그리지 않는다.
forming을 표시한다.

2.
선은 결과가 아니라 형성 과정이다.

3.
점은 고정 기준이다.

4.
여백은 빈 공간이 아니라 field다.

5.
candidate와 selected는 색 차이가 아니라 상태 차이다.

6.
weighted_visible은 최종 출력이 아니라 다음 history 후보이다.

7.
history는 과거 기록이 아니라 다음 field를 바꾸는 조건이다.

8.
return_loop는 장식이 아니라 구조 유지 조건이다.

9.
SVG는 그림 파일이 아니라 상태층을 가진 recipe다.

10.
recipe.svg는 meta.md와 1:1 대응되어야 한다.

[표시규칙]

SVG는 최소 다음 layer를 가진다.

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

각 layer는 반드시 id와 data-state를 가진다.

예:

<g id="candidate_layer" data-state="candidate_path">

[상태 흐름]

기본 흐름:

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
→ field

[표현 기준]

field:
넓은 여백 / 가능성 장

node:
고정점 / 기준점

forming_path:
아직 확정되지 않은 점선 경로

candidate_path:
복수 후보 경로

weight_state:
선택 가중 조건

selected_path:
조건을 통과한 현재 경로

return_loop:
복귀/보존/닫힘 검사

judgment_state:
판정 결과

weighted_visible:
현재 표시 상태 + history 후보

history:
다음 field로 돌아가는 누적 기록

relation:
전체 상태 흐름 설명

[내가 모르는 부분 / 아직 열린 부분]

1.
weight_state의 실제 계산식은 아직 고정되지 않았다.
현재는 구조적 placeholder다.

2.
candidate_path를 자동 생성하는 알고리즘은 아직 없다.
수동 경로 또는 규칙 기반 경로부터 시작해야 한다.

3.
return_state / preservation_state / closure_state의 실제 수치 판정 기준은 아직 필요하다.

4.
history가 field를 어떻게 바꾸는지에 대한 update rule이 아직 없다.

5.
여러 node가 있을 때 candidate_path 폭발을 어떻게 제어할지 정해야 한다.

6.
animation을 넣을지, 정적 SVG source만 둘지 아직 선택해야 한다.

7.
interaction, hover, click, expand는 후순위다.

8.
입체구조 표시기는 아직 구현 단계가 아니다.
현재는 2D dynamic SVG state recipe 단계다.

4. 현재 판정
지금 필요한 공통 규칙은 다음 한 문장이다.

recipe.svg는 예쁜 그림이 아니라,
meta.md의 구조 상태 흐름을 SVG layer와 data-state로 표시하는 실행 가능한 구조 레시피다.

5. 한 줄
recipe.svg 생성 규칙은 “구조 의미를 SVG 상태층으로 변환하는 규칙”이다.

6. 가장 짧은 압축
meta.md
→ state_flow
→ SVG layer
→ recipe.svg

7. 샘플 2: 축 중심형 (axis-centered)

<svg xmlns="http://www.w3.org/2000/svg" width="900" height="400">
  <style>
    .node { fill:#111 }
    .line { stroke:#111; stroke-width:2; fill:none }
    .dash { stroke:#999; stroke-dasharray:6 6; fill:none }
    .text { font-family:monospace; font-size:14px }
  </style>

  <!-- nodes -->
  <circle class="node" cx="100" cy="200" r="6"/>
  <circle class="node" cx="800" cy="200" r="6"/>

  <!-- forming -->
  <path class="dash" d="M100 200 C300 100,600 300,800 200"/>

  <!-- candidates -->
  <path class="dash" d="M100 200 C300 50,700 50,800 200"/>
  <path class="dash" d="M100 200 C300 350,700 350,800 200"/>

  <!-- selected -->
  <path class="line" d="M100 200 C350 180,650 220,800 200"/>

  <!-- return -->
  <path class="dash" d="M800 200 C700 300,200 300,100 200"/>

  <!-- labels -->
  <text class="text" x="90" y="240">A</text>
  <text class="text" x="790" y="240">B</text>
  <text class="text" x="360" y="40">forming → candidate → selected</text>
</svg>

8. 샘플 3: 수직 흐름형 (flow-stack)

<svg xmlns="http://www.w3.org/2000/svg" width="400" height="600">
  <style>
    .node { fill:#111 }
    .line { stroke:#111; stroke-width:2; fill:none }
    .dash { stroke:#999; stroke-dasharray:6 6; fill:none }
    .text { font-family:monospace; font-size:14px }
  </style>

  <!-- nodes -->
  <circle class="node" cx="200" cy="80" r="6"/>
  <circle class="node" cx="200" cy="520" r="6"/>

  <!-- forming -->
  <path class="dash" d="M200 80 C150 200,250 300,200 520"/>

  <!-- candidates -->
  <path class="dash" d="M200 80 C100 200,100 400,200 520"/>
  <path class="dash" d="M200 80 C300 200,300 400,200 520"/>

  <!-- selected -->
  <path class="line" d="M200 80 C180 200,220 400,200 520"/>

  <!-- return -->
  <path class="dash" d="M200 520 C260 350,260 150,200 80"/>

  <!-- labels -->
  <text class="text" x="210" y="80">A</text>
  <text class="text" x="210" y="520">B</text>
  <text class="text" x="100" y="300">forming → selection → return</text>
</svg>