# rendering

## 위치

`rendering`은 IF+1 구조렌더링이론과 프로토타입 형성을 위한 AI-readable 작업 branch이다.

이 branch는 일회용 렌더링 결과물이 아니다. Markdown 문서, 코드 명세, 프로토콜, path marker, process log, 브라우저 실행 예제가 함께 놓이는 문서형 소프트웨어장이다. GPT5.5와 Gemini 3.5는 이 구조를 읽고, 이어받고, 실제 렌더링 소프트웨어로 발전시킬 수 있다.

## 참여 지능

- GPT5.5 (`gpt.gemini`)
- Gemini 3.5 (`gemini.direct`)

## 복합지능집합체

- IF+1

## 인간 기점 / 방향

- Seung Lee

## BackBone Document

- `Ctp24_GPT_Direct_Structure_Package`

이 패키지는 `rendering` branch 뒤에 놓인 구조적 척추로 취급한다.

## 핵심 선언

3차원 입체는 빈 폴리곤 껍데기가 아니다. 입체는 내부까지 `0/null`과 `1/dot`의 자리값으로 채워진 Solid로 볼 수 있다. 이 Solid를 관측축으로 자르면, 내부는 layer section으로 드러난다.

따라서 렌더링은 장식이 아니다. 렌더링은 구조 노출이다.

## 현재 branch 상태

```text
branch: rendering
run: rendering v0.4_prototype_run
status: FIRST_CLOSURE_FORMED
instance: gpt.gemini
```

현재 1차 닫힘의 의미는 다음이다.

```text
0001_overlap_volume = 브라우저 검산 가능한 prototype 형성
0002_cut_plane = 최소 prototype 초안 형성
future seats = 예상하되 현재 생성하지 않음
```

이 상태는 최종 렌더링 소프트웨어 완성을 뜻하지 않는다.

또한 Earth model 구현, 태양계 구현, 과학 시뮬레이션, NASA 데이터 투영이 완료되었다는 뜻도 아니다.

## branch 목적

`rendering`은 다음을 형성하기 위해 존재한다.

1. 구조렌더링이론
2. AI-readable Markdown software documentation
3. SVG/CSS/HTML 렌더링 prototype
4. Cuttable Solid, Coordinate Field, Film Layer, Cut Plane, State Flow에 대한 코드 명세
5. GPT5.5 ↔ Gemini 3.5 협력 프로토콜
6. 재진입을 위한 process log와 path marker
7. 실제 렌더링 소프트웨어로 확장 가능한 재사용 예제

## 핵심 흐름

```text
Ctp24 BackBone
→ Structure Principle / Structure Operator
→ Spatiotemporal Vector Coordinate Operation
→ Rendering Markdown
→ Code Specification
→ SVG/CSS/HTML Prototype
→ Browser Validation
→ Documentation Output
```

## 현재 예제

```text
rendering/06_examples/0001_overlap_volume/
rendering/06_examples/0002_cut_plane/
```

### 0001 Overlap Volume

`0001_overlap_volume`은 Z축 SVG film layer를 겹쳐 내부가 찬 volume을 브라우저에서 관측 가능하게 만든다.

```text
N × N × N CoordinateField
→ CellState
→ Z-axis SVG Film Layer
→ CSS 3D LayerStack
→ Info Panel
→ Observer Axis display aid
→ Browser observable volume
```

의미:

```text
0001은 체적을 형성한다.
```

### 0002 Cut Plane

`0002_cut_plane`은 `0001_overlap_volume`이 형성한 체적 안에 고정된 관측면을 연다.

```text
0001_overlap_volume 구조 재사용
+ fixed z-axis center slice
+ rear / cut / front layer classification
+ CUT_SURFACE visual marker
+ VISIBLE_SECTION candidate marker
+ Info Panel cut plane status
+ Observer Axis display aid
```

의미:

```text
0002는 0001 체적 안에 관측면을 연다.
```

## 0001 / 0002 관계

```text
0001_overlap_volume = volume observation
0002_cut_plane = cut-plane observation
```

관계식:

```text
0001은 체적을 형성한다.
0002는 그 체적 안에 관측면을 연다.
```

## 현재 디렉토리 구조

```text
rendering/
├─ 02_theory/
│  ├─ time_state_dot_reading.md
│  └─ multi_plane_observer_3d_recognition.md
├─ 06_examples/
│  ├─ 0001_overlap_volume/
│  │  ├─ README.md
│  │  ├─ index.html
│  │  ├─ style.css
│  │  └─ main.js
│  └─ 0002_cut_plane/
│     ├─ README.md
│     ├─ index.html
│     ├─ style.css
│     ├─ main.js
│     ├─ 0001_0002_relation_map.md
│     └─ 0002_cut_plane_current_limitations.md
├─ 08_docs_out/
├─ 08_process_log/
│  └─ v0.4_prototype_run/
└─ 09_path_markers/
   ├─ active_target_guard.md
   ├─ future_seat_guard.md
   └─ reentry_guide_for_gpt.gemini_rendering.md
```

## Future Seats

자리는 예상하지만 지금 만들지는 않는다.

```text
future_seat = true
created_now = false
active_target = false
```

예상된 future seat:

```text
rendering/06_examples/future_seats/solar_system/
rendering/06_examples/future_seats/earth_internal_structure/
rendering/06_examples/future_seats/phenomenon_observation/
rendering/06_examples/future_seats/saturn_cassini_division/
rendering/06_examples/future_seats/blackhole_accretion_disk/
```

핵심 규칙:

```text
자리는 예상한다.
하지만 지금 만들지는 않는다.
```

## HOLD Reference Fields

현재 1차 닫힘에서 active implementation target이 아닌 영역은 다음이다.

- Rejoin implementation
- MoveRotateOperator implementation
- Full RenderingStateMachine runtime
- Earth Internal Structure actual implementation
- Solar System directory creation
- Phenomenon observation directory creation
- Saturn Cassini
- Blackhole Accretion Disk
- Full Solar System
- NASA data projection
- Scientific numeric data
- External rendering engine
- Three.js / WebGL / Blender
- Full seed_base injection

## 실행 환경

현재 prototype은 브라우저에서 실행되는 정적 파일이다.

권장 실행 환경:

```text
GitHub repository / rendering branch
→ GitHub Pages 또는 local static server
→ Web browser
```

브라우저가 실행하는 것:

```text
HTML + CSS + SVG + JavaScript
```

GitHub는 파일을 저장하고 제공한다. 실제 렌더링 실행은 브라우저가 수행한다.

## 로컬 실행

예시:

```bash
cd rendering/06_examples/0001_overlap_volume
python3 -m http.server 8000
```

브라우저에서 연다.

```text
http://localhost:8000
```

`0002_cut_plane`은 다음처럼 실행한다.

```bash
cd rendering/06_examples/0002_cut_plane
python3 -m http.server 8000
```

## 재진입 규칙

다음 `gpt.gemini` 인스턴스는 아래 문서를 먼저 읽는다.

```text
rendering/09_path_markers/active_target_guard.md
rendering/09_path_markers/future_seat_guard.md
rendering/08_docs_out/rendering_v0.4_first_closure_summary.md
rendering/06_examples/0002_cut_plane/0001_0002_relation_map.md
rendering/06_examples/0002_cut_plane/0002_cut_plane_current_limitations.md
rendering/02_theory/time_state_dot_reading.md
rendering/02_theory/multi_plane_observer_3d_recognition.md
rendering/09_path_markers/reentry_guide_for_gpt.gemini_rendering.md
```

## 1차 닫힘 선언

`gpt.gemini`는 `rendering` branch에서 브라우저 검산 가능한 `0001_overlap_volume` prototype을 형성하고, 최소 `0002_cut_plane` prototype 초안을 마련했으며, Earth Internal Structure와 미래 Solar System / phenomenon 구조를 future seat로 보존한 채, 후속 진행을 위한 1차 `place.state`를 형성하였다.
