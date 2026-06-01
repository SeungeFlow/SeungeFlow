# 0002 Cut Plane Entry Condition

## Instance

```text
gpt.gemini
```

## Run

```text
rendering v0.4_prototype_run
```

## Turn

```text
gpt.gemini 20회차 1차 마무리
총 20회차 중 진행 5회차
```

## Work

```text
0002_cut_plane 진입 조건 정리
```

## Purpose

This document defines the conditions required before entering `0002_cut_plane`.

This document does not implement `0002_cut_plane`.

이 문서는 `0002_cut_plane` 구현 문서가 아니다.  
이 문서는 `0001_overlap_volume` 이후 `0002_cut_plane`으로 들어가기 위한 진입 조건을 정리하는 문서이다.

---

## Current Previous Target

```text
0001_overlap_volume
```

Current status:

```text
FIRST_CLOSURE_CANDIDATE
```

Meaning:

```text
0001_overlap_volume is a browser-observable prototype candidate.
It is not the final rendering engine.
It is not Earth model.
It is not Cut Plane implementation.
It is not Rejoin implementation.
It is not MoveRotateOperator implementation.
It is not RenderingStateMachine implementation.
```

Korean statement:

```text
0001_overlap_volume은 브라우저에서 내부 volume이 관측 가능한지 검산하는 첫 구조렌더링 prototype이다.
0001_overlap_volume은 최종 렌더링 엔진이 아니다.
0001_overlap_volume은 Earth model이 아니다.
0001_overlap_volume은 Cut Plane 구현이 아니다.
```

---

## 0002 Cut Plane Definition

```text
0002_cut_plane
=
0001_overlap_volume 위에 observer axis와 slice index를 적용하여
특정 layer를 cut layer로 판정하고,
front / cut / rear layer classification과 visible section 후보를 표시하는 최소 prototype
```

A cut plane is not a destruction surface.

```text
Cut Plane
=
내부 relation-field가 관측 가능해지는 관측면
```

Korean core statement:

```text
절단면은 파괴면이 아니다.
절단면은 내부 relation-field가 관측 가능해지는 관측면이다.
```

---

## Entry Status

```text
0002_cut_plane entry status:
CONDITIONAL_READY
```

Reason:

```text
0001_overlap_volume structure is formed enough to define 0002 entry conditions.
However, final browser validation still requires confirming:
- no console error
- no external network request
```

If these two checks pass, 0002 can move from `CONDITIONAL_READY` to `READY`.

---

## Required Conditions Before 0002

### 1. 0001 File Presence

The following files must exist:

```text
rendering/06_examples/0001_overlap_volume/README.md
rendering/06_examples/0001_overlap_volume/index.html
rendering/06_examples/0001_overlap_volume/style.css
rendering/06_examples/0001_overlap_volume/main.js
```

Status:

```text
PASS
```

---

### 2. 0001 Browser Validation

Required checks:

```text
index.html opens in browser
Info Panel appears
SVG Film Layer stack appears
Observer buttons appear
Observer buttons change display view only
Cut Plane remains not implemented
External engine remains none
NASA data remains none
```

Status:

```text
PASS CANDIDATE
```

Additional checks still required:

```text
Console error: none
Network external request: none
```

---

### 3. 0001 Scope Freeze

Before entering 0002, `0001_overlap_volume` must be frozen as a baseline.

Freeze meaning:

```text
0001 no longer receives new structural features.
0001 remains overlap volume prototype.
0001 remains SVG Film Layer + CSS 3D LayerStack.
0001 does not absorb cut plane, rejoin, move, Earth, solar system, or phenomenon features.
```

Korean statement:

```text
0001은 겹침 볼륨으로 닫는다.
0001 안에 0002_cut_plane 기능을 섞지 않는다.
```

---

### 4. 0002 Allowed Scope

`0002_cut_plane` may include only:

```text
ObserverAxis display / cut axis declaration
fixed slice index
cut layer classification
front layer classification
rear layer classification
CUT_SURFACE marking
VISIBLE_SECTION candidate marking
Info Panel update for cut status
README scope and limitation documentation
```

---

### 5. 0002 Out-of-Scope

The following remain outside 0002:

```text
Rejoin
MoveRotateOperator
full RenderingStateMachine implementation
Earth Internal Structure implementation
NASA data
scientific numeric data
solar_system directory
phenomena directory
Saturn Cassini
Blackhole Accretion Disk
Three.js
WebGL
Blender
external rendering engine
```

---

## 0002 Target Folder

When 0002 starts, its target folder is:

```text
rendering/06_examples/0002_cut_plane/
```

Candidate files:

```text
rendering/06_examples/0002_cut_plane/README.md
rendering/06_examples/0002_cut_plane/index.html
rendering/06_examples/0002_cut_plane/style.css
rendering/06_examples/0002_cut_plane/main.js
```

This document does not create those files.

---

## 0002 Minimal Prototype Rule

The first 0002 prototype should begin from 0001 structure.

Flow:

```text
0001_overlap_volume baseline
→ add fixed observer axis
→ add fixed slice index
→ classify layers as rear / cut / front
→ mark cut layer
→ show visible section candidate
```

Do not add:

```text
interactive physics
Earth data
rejoin logic
move / rotate operator
state machine engine
solar system structure
```

---

## 0002 Info Panel Requirements

The 0002 Info Panel should display:

```text
Run: rendering v0.4_prototype_run
Target: 0002_cut_plane
Base: 0001_overlap_volume
Grid: N × N × N
Layer count
Slice axis
Slice index
Rear layer count
Cut layer index
Front layer count
Cut Plane: implemented as observation surface
Rejoin: not implemented
Move / Rotate Operator: not implemented
Rendering State Machine: not implemented
Earth model: not implemented
External engine: none
NASA data: none
```

---

## Go / No-Go Rule

### READY

0002 may start if:

```text
0001 files exist
0001 browser visible structure works
Info Panel appears
Observer buttons work as display aid
Console error is none
Network external request is none
0001 scope is frozen
```

### HOLD

0002 should not start if:

```text
0001 has unresolved browser error
external request appears
cut plane is confused with observer display aid
0001 baseline is still unstable
new feature pressure pushes toward Earth / solar system / phenomenon observation
```

---

## Current Judgment

```text
0002_cut_plane:
ENTRY_CONDITION_DEFINED

Entry status:
CONDITIONAL_READY
```

Korean judgment:

```text
0002_cut_plane은 아직 구현하지 않는다.
0002_cut_plane으로 들어가기 위한 조건은 정의되었다.
0001_overlap_volume의 Console / Network 검산이 확인되면 READY로 전환할 수 있다.
```

---

## Boundary

```text
gpt.gemini는 rendering 작업만 한다.
gpt.direct 작업을 하지 않는다.
gpt.music 작업을 하지 않는다.
gpt.github 작업을 하지 않는다.
gemini.direct 결과는 rendering prototype hint로만 사용한다.
```

---

## Next Turn

```text
gpt.gemini 20회차 1차 마무리
총 20회차 중 진행 5회차 완료
다음: 6회차 — 0002_cut_plane 범위 고정
필요 모드: Pro-확장
```
