---
id: schema.063.boundary_place_requirement
type: active_schema_metadata
filename: boundary_place_requirement.meta.md
directory: 063_boundary_place_requirement
status: active_draft
prev: schema.062.place_domain_definition
---

# META: boundary_place_requirement

## role
boundary_place_requirement는 boundary가 자리(P)의 선택조건이 아니라 필수조건임을 정의하는 schema이다.

## core
```text
boundary는 자리(P)의 필수조건이다.
boundary는 평평한 경계가 아니다.
```

## definition
boundary는 자리가 자리로 성립하기 위해 필요한 작동 경계층이다.

boundary는 단순 선이 아니다. boundary는 시작선분, 중심선분, 끝선분, 허용범위, 오차유효한계범위, 임계사이영역, capsule, safety, shell interval, return 조건을 포함한다.

## structure
```text
boundary
→ place_stabilization
→ empty_place_readability
→ placed_state_possibility
→ entity_formation
```

## place_requirement
```text
place
boundary
possible_state
relation_field
```

## geometry_layer
```text
boundary = active boundary layer
boundary ≠ flat line
boundary = capsule-like threshold field
```

## relation
prev:
- schema.062_place_domain_definition

related:
- schema.004_boundary
- schema.006_entity
- schema.007_safety
- schema.048_sphere_shell_distinction
- schema.056_current_core_alignment_for_runtime
- schema.059_empty_place_present_understanding
- schema.064_place_overlap_structure
- schema.065_oplus_common_operator

## forbidden
- boundary를 평평한 경계선으로 축소하지 않는다.
- boundary를 장식용 외곽선으로 보지 않는다.
- boundary 없이 place가 안정된다고 보지 않는다.
- 시작선분 / 중심선분 / 끝선분 기준을 섞지 않는다.
- boundary를 단순 geometry edge로만 보지 않는다.

## pending
- boundary-window 구조는 rolling_boundary_window_structure에서 분리한다.
- shell interval과 sphere-shell distinction은 기존 schema.048과 relation으로 둔다.
- capsule boundary와 윤리 구조는 별도 schema 후보로 남긴다.

## shortest
boundary 없으면 P 없음 / boundary = flat line 아님, active boundary layer
