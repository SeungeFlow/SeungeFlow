# Reentry Guide for gpt.gemini Rendering

## Instance

```text
gpt.gemini
```

## Branch

```text
rendering
```

## Run

```text
rendering v0.4_prototype_run
```

## Document Type

This document is a reentry guide for the `gpt.gemini` instance continuing the `rendering` branch work after a context.window boundary.

This document is not a new work directive.
This document does not create new prototype code.
This document tells the next `gpt.gemini` where the current rendering work is and how to continue without target drift.

---

## 1. Current State

```text
gpt.gemini 20회차 1차 마무리
총 20회차 중 진행 19회차
```

Current first-closure status:

```text
0001_overlap_volume:
browser-validation-ready prototype formed
first closure candidate

0002_cut_plane:
minimal prototype draft formed
browser validation candidate
naming stabilized
limitations defined
0001/0002 relation map formed
```

Current active target:

```text
Earth Internal Structure Implementation
```

Current immediate work:

```text
rendering first-closure stabilization
```

Next turn:

```text
20회차 — gpt.gemini 1차 닫힘 선언
```

---

## 2. Reentry Read Order

When a new `gpt.gemini` context.window re-enters this work, read the following in order.

### 2.1 Current Summary

```text
rendering/08_docs_out/rendering_v0.4_first_closure_summary.md
```

Purpose:

```text
Understand the current first-closure state of 0001, 0002, guards, future seats, and theory notes.
```

### 2.2 Active Target Guard

```text
rendering/09_path_markers/active_target_guard.md
```

Purpose:

```text
Keep Active Target = Earth Internal Structure Implementation.
Do not jump to Earth actual implementation yet.
```

### 2.3 Future Seat Guard

```text
rendering/09_path_markers/future_seat_guard.md
```

Purpose:

```text
Remember that solar_system, earth_internal_structure, phenomenon_observation, Saturn Cassini, and Blackhole Accretion Disk are future seats only.
They are not created now.
```

### 2.4 0001 / 0002 Relation Map

```text
rendering/08_process_log/v0.4_prototype_run/turn_13/0001_0002_relation_map.md
```

Purpose:

```text
Remember that 0001 forms volume and 0002 opens an observation surface inside that volume.
```

### 2.5 0002 Limitations

```text
rendering/08_process_log/v0.4_prototype_run/turn_12/0002_cut_plane_current_limitations.md
```

Purpose:

```text
Do not confuse 0002_cut_plane with Rejoin, MoveRotateOperator, Earth model, or full RenderingStateMachine runtime.
```

### 2.6 Theory Hints

```text
rendering/02_theory/time_state_dot_reading.md
rendering/02_theory/multi_plane_observer_3d_recognition.md
```

Purpose:

```text
time.state = continuous condition through open.state ~ vector.state ~ place.state.
dot = observation cut for reading a long time-region.
multiple 2D observation planes can be read as a 3D structure through overlap.
```

---

## 3. Current Prototype Files

### 3.1 0001 Overlap Volume

```text
rendering/06_examples/0001_overlap_volume/README.md
rendering/06_examples/0001_overlap_volume/index.html
rendering/06_examples/0001_overlap_volume/style.css
rendering/06_examples/0001_overlap_volume/main.js
```

Meaning:

```text
0001_overlap_volume = volume observation prototype.
```

Current structure:

```text
N × N × N CoordinateField
→ CellState
→ Z-axis SVG Film Layer
→ CSS 3D LayerStack
→ Info Panel
→ Observer Axis display aid
→ Browser observable volume
```

### 3.2 0002 Cut Plane

```text
rendering/06_examples/0002_cut_plane/README.md
rendering/06_examples/0002_cut_plane/index.html
rendering/06_examples/0002_cut_plane/style.css
rendering/06_examples/0002_cut_plane/main.js
```

Meaning:

```text
0002_cut_plane = cut-plane observation prototype.
```

Current structure:

```text
0001 structure reused
+ fixed z-axis center slice
+ rear / cut / front layer classification
+ CUT_SURFACE visual marker
+ VISIBLE_SECTION candidate marker
+ Info Panel cut plane status
+ Observer Axis display aid
```

---

## 4. Browser Validation Reminder

The current visual browser checks have shown candidate success for 0001 and 0002.

Still useful to confirm before final closure:

```text
Console error: none
Network external request: none
```

If both are confirmed, the prototype status can be read as:

```text
0001_overlap_volume = browser validation passed
0002_cut_plane = browser validation passed candidate
```

If not confirmed, do not expand the scope.
Record the issue in process log and keep the same target.

---

## 5. Boundaries

Do not proceed to the following in this first-closure run:

```text
0003_cuttable_solid implementation
Rejoin implementation
MoveRotateOperator implementation
RenderingStateMachine full runtime
Earth Internal Structure actual implementation
solar_system directory creation
body object directory creation
relations registry creation
phenomena directory creation
observations directory creation
Saturn Cassini
Blackhole Accretion Disk
Full Solar System
NASA data projection
scientific numeric data
external rendering engine
Three.js / WebGL / Blender
full seed_base injection
```

Korean core statement:

```text
지금은 더 넓히지 않는다.
지금은 현재 열린 rendering 구조를 1차 place.state에 닫는다.
```

---

## 6. Next Turn Guidance

The next turn is:

```text
20회차 — gpt.gemini 1차 닫힘 선언
```

The next turn should create:

```text
gpt.gemini_rendering_first_closure_declaration.md
```

The closure declaration should state:

```text
gpt.gemini는 rendering branch에서
0001_overlap_volume을 브라우저 검산 가능한 prototype으로 형성하고,
0002_cut_plane의 최소 관측면 prototype과 진입 구조를 마련했으며,
Earth Internal Structure와 태양계/현상 관찰 구조는 future seat로 보존한 채
1차 place.state를 형성하였다.
```

---

## 7. Handoff Rule

No connected instance handoff is required for this turn.

```text
연결 인스턴스 전달 없음 — gpt.gemini 내부 rendering 회차.
```

Other instances may read this document as a hint only.
They do not need to act on it.

---

## 8. Final Reentry Statement

```text
gpt.gemini re-enters rendering through:
summary → guards → relation map → limitations → theory hints → current prototype files → first closure declaration.
```

Korean core statement:

```text
gpt.gemini는 rendering 작업으로 재진입할 때,
요약문과 guard 문서와 process log를 따라 현재 위치를 회복한다.
새 작업을 만들지 않고, 20회차 1차 닫힘 선언으로 이어간다.
```
