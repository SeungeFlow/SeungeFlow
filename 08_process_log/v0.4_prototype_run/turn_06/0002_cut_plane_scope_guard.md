# 0002 Cut Plane Scope Guard

## 0. 문서 성격

이 문서는 `gpt.gemini`가 하던 `rendering` 작업의 20회차 중 6회차 산출물이다.

이 문서는 `0002_cut_plane`을 구현하는 문서가 아니다.  
이 문서는 `0002_cut_plane`에서 허용할 범위와 이번 1차 마무리 안에서 제외할 범위를 고정하는 경계 문서다.

```text
인스턴스 id:
gpt.gemini

작업:
rendering branch

현재 run:
rendering v0.4_prototype_run

현재 회차:
총 20회차 중 진행 6회차

작업명:
0002_cut_plane 범위 고정
```

---

## 1. 이전 회차 상태

5회차에서 `0002_cut_plane` 진입 조건은 다음 상태로 정의되었다.

```text
0002_cut_plane:
ENTRY_CONDITION_DEFINED

Entry status:
CONDITIONAL_READY
```

의미:

```text
0002_cut_plane은 아직 구현하지 않는다.
0002_cut_plane으로 들어가기 위한 조건만 정의했다.
0001_overlap_volume의 Console / Network 검산이 확인되면 READY로 전환할 수 있다.
```

따라서 6회차에서는 구현으로 들어가지 않고, 먼저 범위를 고정한다.

---

## 2. 0002_cut_plane의 목적

`0002_cut_plane`의 목적은 다음이다.

```text
0001_overlap_volume 위에
Observer Axis와 Slice Index를 적용하여
Cut Plane,
Visible Section,
front / cut / rear layer classification을
최소 prototype 수준에서 관측 가능하게 하는 것
```

한국어 핵심문:

```text
0002_cut_plane은 입체를 부수는 구현이 아니다.
0002_cut_plane은 내부 relation-field가 보이도록 관측면을 여는 최소 구조렌더링 prototype이다.
```

---

## 3. 0002에서 허용되는 것

이번 1차 마무리 안에서 `0002_cut_plane`에 허용되는 범위는 다음이다.

```text
1. 0001_overlap_volume 구조 재사용
2. fixed slice index 사용
3. Observer Axis 기준 표시
4. cut layer 표시
5. front layer / cut layer / rear layer 분류
6. CUT_SURFACE 표시
7. VISIBLE_SECTION 후보 표시
8. Info Panel에 cut plane status 표시
9. Cut Plane이 display aid와 다르다는 설명
10. Vanilla HTML / CSS / SVG / JavaScript 유지
```

---

## 4. 0002에서 아직 하지 않는 것

이번 1차 마무리 안에서 `0002_cut_plane`은 다음을 하지 않는다.

```text
1. Rejoin 구현
2. MoveRotateOperator 구현
3. RenderingStateMachine 전체 구현
4. Earth Internal Structure 구현
5. Earth layer cut 구현
6. NASA 데이터 투입
7. 실제 과학 수치 입력
8. solar_system 디렉토리 생성
9. phenomenon_observation 디렉토리 생성
10. Saturn Cassini 구현
11. Blackhole Accretion Disk 구현
12. Three.js / WebGL / Blender 사용
13. 외부 렌더링 엔진 사용
```

---

## 5. Observer Axis Display Aid와 Cut Plane Operation 구분

`0001_overlap_volume`의 observer buttons는 표시 보조다.

```text
Observer Axis Display Aid
=
현재 volume을 여러 방향에서 보기 위한 view transform
```

`0002_cut_plane`의 Cut Plane은 다르다.

```text
Cut Plane Operation
=
layer와 cell에 CUT_SURFACE / VISIBLE_SECTION 역할을 부여하는 관측면 설정
```

구분:

| 항목 | 의미 | 0001 | 0002 |
|---|---|---:|---:|
| Observer View Button | 화면 시점 변경 | 사용 | 사용 가능 |
| Slice Index | 절단 위치 선택 | 없음 | fixed로 허용 |
| Cut Layer | 절단 layer 표시 | 없음 | 허용 |
| Visible Section | 내부 단면 후보 표시 | 없음 | 허용 |
| front / cut / rear | layer classification | 없음 | 허용 |

한국어 핵심문:

```text
시점을 바꾸는 것과 절단면을 여는 것은 다르다.
0001은 시점 보조이고, 0002는 관측면 설정이다.
```

---

## 6. 0002 최소 상태 모델

`0002_cut_plane`의 최소 상태는 다음만 가진다.

```text
CutPlaneState {
  enabled
  axis
  sliceIndex
  frontLayerCount
  cutLayerIndex
  rearLayerCount
  cutSurfaceCellCount
  visibleSectionCellCount
}
```

기본값 후보:

```text
enabled = true
axis = "z"
sliceIndex = center_index
```

주의:

```text
이 상태 모델은 최소 prototype 상태다.
전체 RenderingStateMachine 구현이 아니다.
```

---

## 7. 0002 최소 표시 규칙

`0002_cut_plane`에서는 layer를 다음처럼 분류한다.

```text
z < sliceIndex  → rear layer
z == sliceIndex → cut layer
z > sliceIndex  → front layer
```

표시 후보:

```text
rear layer  → 낮은 opacity
cut layer   → 강조 표시
front layer → 낮은 opacity 또는 선택적 표시
```

주의:

```text
opacity는 표시 보조다.
물리적 투명도나 실제 물질 속성을 의미하지 않는다.
```

---

## 8. 0002 파일 범위

`0002_cut_plane`에서 생성 가능한 파일 후보는 다음이다.

```text
rendering/06_examples/0002_cut_plane/
├─ README.md
├─ index.html
├─ style.css
└─ main.js
```

그러나 6회차에서는 이 파일들을 생성하지 않는다.

6회차는 범위 고정 문서만 생성한다.

---

## 9. 0002 진입 전 조건

`0002_cut_plane` 구현에 들어가기 전 확인할 조건은 다음이다.

```text
1. 0001_overlap_volume 파일 4개가 존재한다.
2. 0001_overlap_volume이 브라우저에서 열린다.
3. Info Panel이 표시된다.
4. SVG film layers가 보인다.
5. Observer buttons는 view만 바꾼다.
6. Console error가 없다.
7. Network 외부 요청이 없다.
8. 0001의 scope가 freeze되었다.
```

---

## 10. 0002 완료 후보 조건

`0002_cut_plane`이 1차 prototype으로 닫히려면 다음이 필요하다.

```text
1. cut layer가 화면에서 구분된다.
2. front / rear layer가 cut layer와 구분된다.
3. cut plane은 파괴면이 아니라 관측면으로 문서화된다.
4. visible section 후보가 표시된다.
5. EMPTY_PRESENT는 데이터 모델에서 삭제되지 않는다.
6. OCCUPIED_DOT은 전체 실체로 오독되지 않는다.
7. Rejoin / Move / Earth model은 구현되지 않는다.
8. 외부 엔진과 외부 데이터가 사용되지 않는다.
```

---

## 11. 현재 HOLD

다음은 현재 HOLD 상태를 유지한다.

```text
Earth Internal Structure actual implementation
Sun-Earth-Moon system
Full Solar System
Saturn Cassini
Blackhole Accretion Disk
NASA data projection
scientific numeric data
external rendering engine
```

---

## 12. 6회차 판정

```text
C_06
=
0002_cut_plane scope guard formed
```

현재 상태:

```text
0002_cut_plane:
SCOPE_GUARD_DEFINED
```

의미:

```text
0002_cut_plane의 허용 범위와 제외 범위를 고정했다.
아직 0002 파일을 생성하지 않았다.
아직 cut plane prototype을 구현하지 않았다.
```

---

## 13. 다음 회차

다음 회차는 다음이다.

```text
gpt.gemini 20회차 중 7회차

작업:
0002 최소 파일 구조 준비

출력:
0002_cut_plane_file_plan.md
```

필요 모드:

```text
Pro-확장
```

---

## 최종 한 줄

`0002_cut_plane`은 `0001_overlap_volume` 위에 관측면을 여는 최소 prototype으로만 제한하며, 이번 6회차에서는 구현하지 않고 cut plane / visible section / front-cut-rear classification의 허용 범위와 rejoin / move / Earth / solar / phenomenon 제외 범위를 고정했다.
