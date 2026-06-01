# 0002 Cut Plane File Plan

## 0. 문서 정보

```text
인스턴스 id:
gpt.gemini

작업:
rendering branch
0002_cut_plane 최소 파일 구조 준비

회차:
gpt.gemini 20회차 중 7회차

출력:
0002_cut_plane_file_plan.md
```

---

## 1. 목적

이 문서는 `0002_cut_plane` 최소 프로토타입을 만들기 전에 필요한 파일 구조를 준비하기 위한 계획 문서다.

이번 회차는 실행 파일을 생성하지 않는다.  
이번 회차는 `0002_cut_plane`에 필요한 파일 후보와 각 파일의 책임만 정리한다.

```text
이번 회차의 목표:
0002_cut_plane에 필요한 파일 구조를 정한다.

이번 회차에서 하지 않는 것:
index.html / style.css / main.js 실제 생성
cut plane prototype 구현
visible section 구현
rejoin 구현
move / rotate 구현
Earth model 구현
```

---

## 2. 현재 기준 상태

이전 회차에서 `0002_cut_plane`의 범위는 다음으로 고정되었다.

```text
0002_cut_plane:
SCOPE_GUARD_DEFINED
```

허용 범위:

```text
0001_overlap_volume 구조 재사용
fixed slice index
Observer Axis 기준 표시
cut layer 표시
front / cut / rear layer 분류
CUT_SURFACE 표시
VISIBLE_SECTION 후보 표시
Info Panel에 cut plane status 표시
Vanilla HTML / CSS / SVG / JavaScript 유지
```

현재 범위 밖:

```text
Rejoin 구현
MoveRotateOperator 구현
RenderingStateMachine 전체 구현
Earth Internal Structure 구현
solar_system 디렉토리 생성
phenomenon_observation 디렉토리 생성
Saturn Cassini
Blackhole Accretion Disk
NASA 데이터
실제 과학 수치
Three.js / WebGL / Blender
```

---

## 3. 목표 파일 구조

`0002_cut_plane`의 목표 파일 구조는 다음이다.

```text
rendering/
└─ 06_examples/
   └─ 0002_cut_plane/
      ├─ README.md
      ├─ index.html
      ├─ style.css
      └─ main.js
```

주의:

```text
이번 7회차에서는 위 파일을 실제 생성하지 않는다.
이번 7회차에서는 파일 후보와 책임만 정리한다.
```

---

## 4. 파일별 책임

### 4.1 README.md

역할:

```text
0002_cut_plane의 목적과 범위 설명
0001_overlap_volume과의 차이 설명
Cut Plane이 파괴면이 아니라 관측면임을 명시
현재 미구현 범위 명시
브라우저 검산 기준 명시
```

필수 포함 항목:

```text
Purpose
Scope
Relation to 0001_overlap_volume
Cut Plane Definition
Not Implemented
Browser Validation Checklist
Korean Core Statement
```

---

### 4.2 index.html

역할:

```text
브라우저 실행 진입점
Info Panel
Viewport
Stage
Cut Plane Controls
Observer View Controls
```

예상 DOM 구조:

```html
<div id="app">
  <aside id="info-panel">
    <h2>Info Panel</h2>
    <div id="stats-content">Loading...</div>
  </aside>

  <main id="viewport">
    <div id="stage" data-view="isometric"></div>
  </main>

  <nav id="observer-controls">
    <button data-view="isometric">isometric</button>
    <button data-view="front">front</button>
    <button data-view="top">top</button>
    <button data-view="side">side</button>
  </nav>

  <section id="cut-controls">
    <label for="slice-index">slice index</label>
    <input id="slice-index" type="range" min="0" max="6" value="3">
  </section>
</div>
```

주의:

```text
slice control은 0002에서 허용되는 후보지만,
이번 7회차에서는 구현하지 않는다.
```

---

### 4.3 style.css

역할:

```text
기본 레이아웃
Info Panel
Viewport perspective
Stage preserve-3d
Z-axis SVG film layer style
front / cut / rear layer 표시 규칙
CUT_SURFACE highlight 후보
VISIBLE_SECTION 후보 표시
control UI 표시
```

예상 클래스:

```text
.film-layer
.film-svg
.occupied-dot
.empty-present
.layer-front
.layer-cut
.layer-rear
.cut-surface
.visible-section
```

주의:

```text
이번 7회차에서는 CSS 파일을 실제 생성하지 않는다.
표시 규칙 후보만 정리한다.
```

---

### 4.4 main.js

역할:

```text
0001_overlap_volume의 coordinate field / cell state / SVG film layer 생성 흐름 재사용
fixed slice index 기준으로 layer를 front / cut / rear로 분류
cut layer에 CUT_SURFACE 표시 후보 부여
Info Panel에 cut plane status 표시
Observer view display aid 유지
```

예상 함수:

```text
createCoordinateField(config)
assignCellStates(field, config)
createZAxisFilmLayers(cellStates, config)
classifyLayersByCut(layers, sliceIndex)
createCutPlaneState(sliceIndex, layers)
createSvgFilmLayer(layer, cutPlaneState, config)
renderLayerStack(layers, cutPlaneState, stage, config)
updateInfoPanel(stats, cutPlaneState, config, currentView)
bindObserverControls(stats, config)
bindCutControls(layers, config)
initPrototype()
```

주의:

```text
이번 7회차에서는 main.js를 실제 생성하지 않는다.
함수 후보만 정리한다.
```

---

## 5. 0001과 0002의 차이

| 항목 | 0001_overlap_volume | 0002_cut_plane |
|---|---|---|
| 핵심 목표 | 내부가 찬 volume 관측 | 절단면과 내부 단면 관측 |
| layer stack | 있음 | 있음 |
| SVG film layer | 있음 | 있음 |
| observer view button | display aid | display aid |
| cut plane | 없음 | 있음 |
| slice index | 없음 | fixed 또는 range 후보 |
| front / cut / rear | 없음 | 있음 |
| visible section | 없음 | 후보 있음 |
| rejoin | 없음 | 없음 |
| Earth model | 없음 | 없음 |

---

## 6. 0002에서 허용되는 최소 구조

```text
CoordinateField
CellState
ZAxisFilmLayer
LayerStack
ObserverAxis display aid
SliceIndexRule
CutPlaneModel 후보
front / cut / rear classification
CUT_SURFACE overlay role
VISIBLE_SECTION 후보
Info Panel status
```

---

## 7. 0002에서 아직 하지 않는 것

```text
Rejoin
MoveRotateOperator
RenderingStateMachine 전체 구현
Earth Internal Structure
solar_system
phenomenon_observation
Saturn Cassini
Blackhole Accretion Disk
NASA 데이터
실제 과학 수치
external rendering engine
Three.js
WebGL
Blender
```

---

## 8. 브라우저 검산 후보

0002가 실제 생성된 뒤 검산할 항목은 다음이다.

```text
1. index.html이 브라우저에서 열린다.
2. Info Panel이 표시된다.
3. SVG film layer stack이 표시된다.
4. slice index 또는 fixed cut index가 표시된다.
5. cut layer가 front / rear와 구분된다.
6. CUT_SURFACE가 기존 cell을 삭제하지 않는다.
7. visible section 후보가 표시된다.
8. Observer view buttons는 view만 바꾼다.
9. Console error가 없다.
10. Network 외부 요청이 없다.
11. NASA data가 없다.
12. external engine이 없다.
```

---

## 9. 8회차로 넘길 준비

다음 회차인 8회차에서는 `0002_cut_plane`의 README 초안을 작성한다.

8회차 입력 기준:

```text
이 문서의 파일 구조
0002_cut_plane_scope_guard.md
0002_cut_plane_entry_condition.md
0001_overlap_volume current files
```

8회차 출력 후보:

```text
rendering/06_examples/0002_cut_plane/README.md
```

단, 8회차에서도 아직 전체 prototype 구현은 하지 않는다.

---

## 10. 현재 판정

```text
0002_cut_plane:
FILE_PLAN_DEFINED
```

의미:

```text
0002_cut_plane에 필요한 파일 구조와 파일별 책임을 정리했다.
아직 0002 디렉토리나 실행 파일은 생성하지 않았다.
아직 cut plane prototype은 구현하지 않았다.
```

---

## 11. 한 줄 요약

```text
0002_cut_plane은 0001_overlap_volume의 Z-axis SVG film layer와 LayerStack을 재사용하여, fixed slice index 기준으로 cut layer와 front/rear layer를 구분하는 최소 절단면 prototype으로 준비하되, 이번 회차에서는 파일 구조와 책임만 정의하고 실행 파일은 생성하지 않는다.
```
