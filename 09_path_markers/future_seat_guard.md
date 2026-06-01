# Future Seat Guard

## Document Status

- Instance ID: `gpt.gemini`
- Branch: `rendering`
- Run: `rendering v0.4_prototype_run`
- Turn: `15 / 20`
- Current Stage: `future seat 정리`
- Active Target: `Earth Internal Structure Implementation`
- Immediate Target: `rendering first-closure stabilization`

## Purpose

This document defines the structures that may be needed later, but are not created in the current first-closure run.

The purpose is to preserve future seats without turning them into active implementation targets.

## Core Rule

```text
자리는 예상한다.
하지만 지금 만들지는 않는다.
```

English core statement:

```text
Reserve future seats.
Do not create them now.
```

## Current Formed Prototype Scope

The current formed prototype scope is limited to:

```text
rendering/06_examples/0001_overlap_volume/
rendering/06_examples/0002_cut_plane/
```

Current formed meaning:

```text
0001_overlap_volume = volume observation
0002_cut_plane = fixed cut-plane observation
```

These are first-stage browser-observable structure-rendering prototypes.

They are not the final rendering engine.
They are not Earth Internal Structure implementation.
They are not Solar System implementation.

## Future Seat Definition

A future seat is a structural place that may be needed later, but is not created or implemented now.

```text
future_seat = true
created_now = false
active_target = false
```

A future seat may be documented as an expected place, but it must not become a directory, file, prototype, or implementation target during this first-closure run unless gpt.gemini explicitly opens a new run and reclassifies it.

## Future Seats Reserved

The following future seats are reserved only as future candidates.

```text
rendering/06_examples/future_seats/solar_system/
rendering/06_examples/future_seats/earth_internal_structure/
rendering/06_examples/future_seats/phenomenon_observation/
rendering/06_examples/future_seats/saturn_cassini_division/
rendering/06_examples/future_seats/blackhole_accretion_disk/
```

These paths are conceptual future seats.
They are not created in the current run.

## Solar System Future Seat

Future candidate:

```text
rendering/06_examples/future_seats/solar_system/
```

Possible later structure:

```text
solar_system/
├─ bodies/
├─ relations/
├─ phenomena/
├─ observations/
└─ system/
```

Current status:

```text
future_seat = true
created_now = false
```

Current rule:

```text
Do not create solar_system/ in this run.
Do not create bodies/ in this run.
Do not create relations/ in this run.
Do not create system registry files in this run.
```

## Earth Internal Structure Future Seat

Future candidate:

```text
rendering/06_examples/future_seats/earth_internal_structure/
```

Possible later structure:

```text
earth_internal_structure/
├─ earth_run.html
├─ earth_style.css
├─ earth_main.js
├─ earth_model.js
└─ earth_internal_layers.js
```

Current status:

```text
future_seat = true
created_now = false
```

Current rule:

```text
Do not create Earth model files in this run.
Do not inject NASA data in this run.
Do not add scientific numeric values in this run.
```

## Phenomenon Observation Future Seat

Future candidate:

```text
rendering/06_examples/future_seats/phenomenon_observation/
```

Possible later meaning:

```text
Phenomenon
=
body itself is not the phenomenon.
A phenomenon is an observable structural event appearing through body, relation-field, boundary, time-state, and observer-axis.
```

Current status:

```text
future_seat = true
created_now = false
```

Current rule:

```text
Do not create phenomenon observation directories in this run.
Do not create phenomenon observer code in this run.
```

## Saturn Cassini Future Seat

Future candidate:

```text
rendering/06_examples/future_seats/saturn_cassini_division/
```

Current status:

```text
future_seat = true
created_now = false
HOLD = true
```

Current rule:

```text
Saturn Cassini remains a HOLD reference field.
Do not create Saturn / ring / Cassini Division files in this run.
```

## Blackhole Accretion Disk Future Seat

Future candidate:

```text
rendering/06_examples/future_seats/blackhole_accretion_disk/
```

Current status:

```text
future_seat = true
created_now = false
HOLD = true
```

Current rule:

```text
Blackhole Accretion Disk remains a HOLD reference field.
Do not create blackhole or accretion disk files in this run.
```

## HOLD Reference Fields

The following remain outside the current first-closure implementation scope:

```text
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

## Current Allowed Work

The current first-closure work remains limited to:

```text
0001_overlap_volume browser validation and closure
0002_cut_plane browser validation candidate
0001 / 0002 relation map
active target guard
future seat guard
reentry / closure documents
```

## Validation Rule

A future seat is valid when:

```text
1. It is named as a possible later place.
2. It is not created now.
3. It does not become an active target in this run.
4. It does not pull the current prototype into a wider system.
5. It remains marked as future_seat = true and created_now = false.
```

## Korean Core Statement

future seat는 지금 만들 디렉토리가 아니다.
future seat는 나중에 구조가 놓일 수 있음을 기억하는 자리다.

현재 run에서는 자리를 예상하되 만들지 않는다.

## Current Judgment

```text
C_15 = future seat guard formed
```

## Next Turn

```text
gpt.gemini 20회차 1차 마무리
총 20회차 중 진행 15회차 완료
다음: 16회차 — time.state / dot 힌트 반영 문서화
필요 모드: Thinking-헤비
```
