# 0001 / 0002 Relation Map

## Run

rendering v0.4_prototype_run

## Turn

gpt.gemini 20회차 1차 마무리 — 13회차

## Instance

gpt.gemini

## Work

0001_overlap_volume과 0002_cut_plane의 관계 정리

## Purpose

이 문서는 `0001_overlap_volume`과 `0002_cut_plane`의 관계를 정리한다.

이 문서는 새 prototype을 생성하지 않는다.
이 문서는 두 prototype target의 의존 관계, 공통 구조, 차이, 경계, 다음 진입 조건을 보존하는 relation map이다.

---

## 1. Current Status

```text
0001_overlap_volume:
BROWSER_VALIDATION_READY / FIRST_CLOSURE_CANDIDATE

0002_cut_plane:
MINIMAL_PROTOTYPE_DRAFT / BROWSER_VALIDATION_CANDIDATE / LIMITATIONS_DEFINED
```

현재 `0001_overlap_volume`은 브라우저에서 내부 volume이 관측 가능한지 검산하는 첫 구조렌더링 prototype이다.

현재 `0002_cut_plane`은 `0001_overlap_volume` 위에 fixed z-axis slice index를 적용하여 cut layer, front/rear layer, CUT_SURFACE, VISIBLE_SECTION 후보를 표시하는 최소 prototype이다.

---

## 2. Structural Dependency

`0002_cut_plane`은 `0001_overlap_volume`을 대체하지 않는다.

```text
0001_overlap_volume
→ 0002_cut_plane
```

의존 관계는 다음과 같다.

```text
0001:
N × N × N CoordinateField
→ CellState
→ Z-axis SVG Film Layer
→ CSS 3D LayerStack
→ Browser observable volume

0002:
0001 structure
+ fixed z-axis slice index
+ rear / cut / front layer classification
+ CUT_SURFACE marker
+ VISIBLE_SECTION candidate
```

한국어 핵심문:

```text
0002_cut_plane은 0001_overlap_volume을 새로 대체하는 것이 아니다.
0002_cut_plane은 0001의 체적 구조 위에 관측 절단면을 얹는 다음 단계다.
```

---

## 3. Shared Structure

두 prototype은 다음 구조를 공유한다.

```text
CoordinateField
CellState
EMPTY_PRESENT
OCCUPIED_DOT
Z-axis SVG Film Layer
CSS 3D LayerStack
Info Panel
Observer Axis Display Aid
Vanilla HTML / CSS / SVG / JavaScript
```

공통 원칙:

```text
EMPTY_PRESENT는 삭제하지 않는다.
OCCUPIED_DOT은 밀도 표시로 렌더링된다.
Observer buttons는 stage view만 바꾼다.
외부 렌더링 엔진은 사용하지 않는다.
NASA 데이터와 실제 과학 수치는 사용하지 않는다.
```

---

## 4. Difference Between 0001 and 0002

| Axis | 0001_overlap_volume | 0002_cut_plane |
|---|---|---|
| Main question | 내부가 찬 volume을 볼 수 있는가? | 절단면을 통해 내부 단면을 볼 수 있는가? |
| Primary operation | Z-axis film layer stack | fixed z-axis cut-plane classification |
| Layer meaning | volume recomposition | rear / cut / front classification |
| Visible structure | occupied cells across stacked layers | cut layer and visible section candidate |
| CUT_SURFACE | not implemented | visual marker candidate |
| VISIBLE_SECTION | not implemented | candidate marker |
| Rejoin | not implemented | not implemented |
| Earth model | not implemented | not implemented |

압축식:

```text
0001 = volume observation
0002 = cut-plane observation
```

---

## 5. Ctp Reading

### 0001

```text
? = observer view aid
m = abstract filled solid candidate
P_place = N × N × N coordinate field
t = z-axis film extraction + layer stack overlap
C = browser observable volume
```

### 0002

```text
? = observer axis / fixed slice condition
m = same abstract solid candidate inherited from 0001
P_place = same N × N × N coordinate field
t = slice index classification + cut surface marking
C = browser observable cut-plane candidate
```

관계:

```text
0001 C
→ becomes source structure for
0002 m / P_place
```

즉 0001에서 형성된 volume은 0002에서 다시 관측 대상이 된다.

---

## 6. Observer Axis Boundary

`0001`과 `0002` 모두 observer view buttons를 가진다.

하지만 이 버튼의 의미는 제한된다.

```text
isometric / front / top / side
=
Observer Axis Display Aid
```

아직 아니다.

```text
full ObserverAxisModel runtime
interactive cut axis selector
dynamic slice control
full CutPlaneOperator
```

한국어 핵심문:

```text
Observer Axis Display Aid는 화면을 보는 방향을 바꾸는 표시 보조다.
Cut Plane Operation은 fixed slice index를 기준으로 layer를 분류하는 관측 절단 규칙이다.
둘을 혼동하지 않는다.
```

---

## 7. Cut Plane Boundary

`0002_cut_plane`에서 cut plane은 파괴면이 아니다.

```text
Cut Plane
=
internal relation-field가 관측 가능해지는 observation surface
```

현재 구현 수준:

```text
fixed z-axis center slice
rear / cut / front layer classification
CUT_SURFACE visual marker
VISIBLE_SECTION candidate marker
```

아직 아니다.

```text
full CutPlaneOperator
SeparatedPartModel
RejoinBoundaryModel
RelationFieldRecoveryRule
```

---

## 8. Not Yet Relation

`0001`과 `0002` 모두 다음을 구현하지 않는다.

```text
Rejoin
MoveRotateOperator
RenderingStateMachine full runtime
Earth Internal Structure
Solar System
Phenomenon Observation
Saturn Cassini
Blackhole Accretion Disk
NASA data
scientific numeric data
Three.js / WebGL / Blender
```

이 영역은 현재 target이 아니다.

---

## 9. Validation Relation

`0001` 검산이 없으면 `0002`로 들어갈 수 없다.

```text
0001 validation
→ 0002 entry condition
→ 0002 scope guard
→ 0002 file plan
→ 0002 README
→ 0002 minimal prototype
→ 0002 browser validation
→ 0002 naming stabilization
→ 0002 limitations
→ 0001 / 0002 relation map
```

현재 이 문서는 위 흐름의 relation map이다.

---

## 10. First Closure Relation

`0001`은 다음으로 닫힌다.

```text
0001_overlap_volume
=
first browser observable volume prototype
```

`0002`는 다음으로 닫힌다.

```text
0002_cut_plane
=
first browser observable cut-plane prototype candidate
```

둘의 관계:

```text
0001 forms volume.
0002 cuts observation surface into that volume.
```

한국어:

```text
0001은 체적을 형성한다.
0002는 그 체적 안에 관측면을 연다.
```

---

## 11. Current Judgment

```text
0001_0002_relation_map:
FORMED
```

판정:

```text
0001_overlap_volume과 0002_cut_plane의 관계는 정리되었다.
0002_cut_plane은 0001을 대체하지 않고 0001 위에 관측 절단면을 얹는 다음 prototype이다.
두 prototype은 모두 Earth model, Rejoin, MoveRotate, full State Machine, Solar System으로 확장되지 않는다.
```

---

## 12. Next Turn

다음 회차:

```text
gpt.gemini 20회차 1차 마무리
총 20회차 중 진행 14회차
작업: rendering path marker 갱신
출력: rendering/09_path_markers/active_target_guard.md
```

## Final Line

```text
0001_overlap_volume은 브라우저에서 내부 volume을 관측하는 첫 prototype이고,
0002_cut_plane은 그 volume 위에 fixed cut plane observation을 얹는 두 번째 prototype이다.
둘은 하나의 연속 구조지만, 0002는 0001을 대체하지 않는다.
```
