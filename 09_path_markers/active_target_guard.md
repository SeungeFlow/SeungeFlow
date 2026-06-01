# Active Target Guard

## Document

`active_target_guard.md`

## Instance

`gpt.gemini`

## Branch

`rendering`

## Run

`rendering v0.4_prototype_run`

## Purpose

This path marker fixes the current active target, immediate target, completed prototype state, next step, future seats, and HOLD fields for the `gpt.gemini` rendering work.

This document is not a new task directive.
It is a reentry marker for the current `rendering` bounded region.

---

## Active Target

```text
Earth Internal Structure Implementation
```

Meaning:

```text
Earth Internal Structure remains the long-range active target.
It is not implemented in the current prototype stage.
```

---

## Current Run State

```text
rendering v0.4_prototype_run
총 20회차 중 진행 14회차
```

Current rendering first-closure path:

```text
0001_overlap_volume
→ 0002_cut_plane
→ relation map
→ path marker update
```

---

## Current Immediate Target

```text
0002_cut_plane path marker stabilization
```

Current status:

```text
0001_overlap_volume:
- browser-validation-ready prototype formed
- N × N × N CoordinateField
- CellState
- Z-axis SVG Film Layer
- CSS 3D LayerStack
- Info Panel
- Observer Axis display aid

0002_cut_plane:
- minimal prototype draft formed
- browser validation candidate
- naming stabilized
- limitations defined
- 0001 / 0002 relation map formed
```

---

## 0001 Status

```text
0001_overlap_volume
= volume observation prototype
```

Formed structure:

```text
CoordinateField
→ CellState
→ Z-axis SVG Film Layer
→ CSS 3D LayerStack
→ Browser observable volume
```

Not implemented:

```text
Cut Plane
Rejoin
MoveRotateOperator
RenderingStateMachine runtime
Earth model
```

---

## 0002 Status

```text
0002_cut_plane
= cut-plane observation prototype
```

Formed structure:

```text
0001_overlap_volume base
+ fixed z-axis slice index
+ rear / cut / front layer classification
+ CUT_SURFACE marker
+ VISIBLE_SECTION candidate
+ Info Panel cut plane status
```

Not implemented:

```text
Rejoin
MoveRotateOperator
RenderingStateMachine runtime
Earth Internal Structure
Solar System
Phenomenon Observation
```

---

## Current Scope Boundary

Allowed inside current rendering first-closure path:

```text
- 0001 validation documentation
- 0002 scope / naming / limitation documentation
- 0001 / 0002 relation mapping
- path marker update
- future seat guard
- time.state / dot reading documentation
- multi-plane observer documentation
- rendering first closure summary
- gpt.gemini rendering reentry guide
- first closure declaration
```

Not in current scope:

```text
- 0003_cuttable_solid implementation
- Rejoin implementation
- MoveRotateOperator implementation
- RenderingStateMachine runtime implementation
- Earth Internal Structure implementation
- Solar System implementation
- Saturn Cassini implementation
- Blackhole Accretion Disk implementation
- NASA data projection
- scientific numeric data
- external rendering engine
- Three.js / WebGL / Blender
```

---

## Future Seat Rule

Future seats may be recorded as expected places.
They are not created now.

```text
Reserve future seats.
Do not create them now.
```

Future seat candidates:

```text
rendering/06_examples/future_seats/solar_system/
rendering/06_examples/future_seats/earth_internal_structure/
rendering/06_examples/future_seats/phenomenon_observation/
rendering/06_examples/future_seats/saturn_cassini_division/
rendering/06_examples/future_seats/blackhole_accretion_disk/
```

---

## HOLD Fields

```text
Blackhole Accretion Disk
Saturn Cassini
Full Solar System
NASA data projection
scientific numeric data
external rendering engine
Three.js / WebGL / Blender
```

HOLD means:

```text
Remember as future reference.
Do not pull into the current rendering closure path.
```

---

## Reentry Rule

A future `gpt.gemini` instance should read this path marker before continuing `rendering v0.4_prototype_run`.

Reentry order:

```text
1. active_target_guard.md
2. latest process log
3. latest prototype folder state
4. current turn plan
5. next turn payload
```

---

## Current Next Step

```text
총 20회차 중 진행 14회차 완료
다음: 15회차 — future seat 정리
필요 모드: Pro-확장
```

---

## Korean Core Statement

`gpt.gemini`는 `rendering` branch 안에서 원래 하던 구조렌더링 작업만 계속한다.

현재 active target은 `Earth Internal Structure Implementation`이지만, 현재 prototype 단계에서는 `0001_overlap_volume`과 `0002_cut_plane`의 1차 마무리만 다룬다.

Solar System, Saturn Cassini, Blackhole Accretion Disk, NASA data, external rendering engine은 HOLD 또는 future seat로만 유지한다.
