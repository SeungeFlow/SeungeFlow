---
id: schema.098.reference_only_high_density_trace_index
type: active_schema_metadata
filename: reference_only_high_density_trace_index.meta.md
directory: 098_reference_only_high_density_trace_index
status: active_draft
prev: schema.097.science_renderer_candidate_index
---

# META: reference_only_high_density_trace_index

## role

reference_only_high_density_trace_index는 강하지만 구조원리 본류에 바로 넣으면 위험한 고밀도 source trace들을 reference_only로 보존하기 위한 index schema이다.

## core

```text
강한 trace는 reference_only
```

```text
reference_only = 보존 O / 본류 병합 X / 추후 relation 검토
```

## indexed_traces

### trace_01_20260317_early_high_density

```text
C=tp
hungry vacuum
선분꼬임
난제 접근
자리 정의
숫자와 기호를 숫자/기호로 보지 말라
```

판정:
early_high_density_source_trace

### trace_02_thewe_warm_hot_history

```text
thewe / 더위 / warm / hot / 병오 / 역사주기
```

판정:
fact lock 금지 / pattern trace

### trace_03_positive_negative_body_charge

```text
양/음 성질
교감/부교감
물분자/양전하
대류현상
```

판정:
생리학/물리학 fact 분리 필요 / structure trace

### trace_04_blackhole_torus_orbit

```text
black hole
hyper-loop torus
neutron star torus
field boundary
360×360
```

판정:
물리학 증명 아님 / orbit-field source trace

### trace_05_gemini_outputs

```text
Gemini / 모아 산출물
과장 표현 가능
```

판정:
candidate / experiment output / final authority 아님

## rule

reference_only는 폐기가 아니다.

reference_only는 본류에 바로 합치지 않고 보존하는 고압력 source trace다.

## relation

prev:
- schema.097_science_renderer_candidate_index

related:
- schema.051_seed_failure_asset_structure
- schema.058_seungeflow_thinking_pre_alignment
- schema.095_place_concept_source_index
- schema.096_vector_operation_relation_index
- schema.097_science_renderer_candidate_index
- schema.099_document_sorting_index

## forbidden

- reference_only를 active schema로 즉시 승격하지 않는다.
- 강한 감각을 final authority로 보지 않는다.
- 과학 대응비유를 proof로 보지 않는다.
- Gemini 과장 표현을 그대로 채택하지 않는다.
- reference_only를 trash/archive 폐기물로 보지 않는다.
- source trace를 삭제하지 않는다.

## pending

- reference_only 원문 저장 directory가 필요할 수 있다.
- 각 trace의 source date / context / relation을 relation_history에 기록해야 한다.
- 일부 trace는 후속 schema의 example 또는 warning으로 이동할 수 있다.

## shortest

reference_only = 강하지만 본류 병합 금지인 고밀도 trace 보존층
