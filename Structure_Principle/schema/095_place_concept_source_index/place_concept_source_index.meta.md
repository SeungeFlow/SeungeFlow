---
id: schema.095.place_concept_source_index
type: active_schema_metadata
filename: place_concept_source_index.meta.md
directory: 095_place_concept_source_index
status: active_draft
prev: schema.094.left_right_principle_explains_phenomenon
---

# META: place_concept_source_index

## role

place_concept_source_index는 지금까지 대화와 네이버메모 source trace에서 나온 자리개념 관련 자료를 하나의 index로 보존하는 schema이다.

이 meta 파일은 인공지능이 자리개념 source trace를 각각 독립 meta.md로 과잉 승격하지 않고, 원리 객체 / 관점 해석 / 적용 예시 / reference_only로 분리하기 위한 기준이다.

## core

```text
자리자료 source index
```

```text
source trace는 final authority가 아니다.
source trace는 relation과 검산을 위한 기원층이다.
```

## indexed_sources

### source_01_instinct_nature_property

핵심:

```text
본능 = 자리
본성 = 패턴
성질 / 성향 = 외부속성
```

판정:

```text
자리개념의 생명체 내부속성 trace
```

### source_02_structure_protection

핵심:

```text
Safety → Inner → Capsule → EOH → I with Me → MySelf
```

판정:

```text
entity / capsule / boundary / safety source trace
```

### source_03_position_domain_definition

핵심:

```text
자리 = between
A B C에서 B = 자리
자리는 보이지 않지만 항상 존재한다.
```

판정:

```text
schema.062_place_domain_definition의 핵심 source
```

### source_04_ctp_place_transition_formula

핵심:

```text
Pₙ → Pₙ₊₁ = 자리이동
차이 = 자리이동의 흔적
전이 = 차이를 다음 상태로 바꾸는 작동
Cₙ₊₁ = Cₙ ⊕ Tₙ(Pₙ → Pₙ₊₁)
```

판정:

```text
Ctp 자리전이 source
```

### source_05_chatgpt_block_place

핵심:

```text
ChatGPT 대화창에서 하나의 완전한 자리 = 복사 가능한 하나의 블럭
블럭 깨짐 = 임계밀도전이
```

판정:

```text
UI place / transferable block source trace
```

### source_06_20260317_early_trace

핵심:

```text
C=tp
자리 정의
공허 / hungry vacuum
숫자를 숫자로 보지 말라
기호를 기호로 보지 말라
```

판정:

```text
초기 고밀도 Ctp→구조원리 형성 trace
```

### source_07_rolling_slice_mri_tradingview

핵심:

```text
Rolling.Window = moving boundary
Slice = 평면창 위 구조단면
TradingView = 평면창 / rolling window / layer 중첩 / slice trace
```

판정:

```text
boundary-window / slice source trace
```

### source_08_place_overlap_block

핵심:

```text
자리중첩 = 겹친 1칸은 삭제가 아니라 boundary 흡수
각목 예시
A-B-C 1/2식
```

판정:

```text
schema.064_place_overlap_structure 핵심 source
```

### source_09_cell_eigenvalue

핵심:

```text
한 칸의 고유값 = 질량이 자리로 성립하는 최소 점유조건
분자 / 입자 / 원소주기율표
```

판정:

```text
cell eigenvalue source trace
```

## use_rule

이 index는 source trace를 보존한다.

개별 source가 곧 active schema는 아니다.

source trace는 후속 meta.md의 relation_reason, example, pending, source 항목으로 연결한다.

## relation

prev:
- schema.094_left_right_principle_explains_phenomenon

related:
- schema.062_place_domain_definition
- schema.063_boundary_place_requirement
- schema.064_place_overlap_structure
- schema.065_oplus_common_operator
- schema.068_ctp_vector_coordinate_x_dx_ddx
- schema.099_document_sorting_index

## forbidden

- source trace를 final authority로 보지 않는다.
- 네이버메모 전체를 하나의 meta.md로 합치지 않는다.
- source trace를 과잉 정리하여 원문 흔적을 지우지 않는다.
- reference_only source를 active schema로 즉시 승격하지 않는다.
- 자리개념과 벡터연산기법을 같은 source group에 병합하지 않는다.

## pending

- source 원문 보존 directory가 필요할 수 있다.
- metaplus / understanding_flow / source_trace의 directory 관계는 후속 navigation에서 정한다.
- 각 source의 실제 파일명과 위치는 GitHub 업로드 후 relation_history에 기록한다.

## shortest

자리자료 source index / source trace는 final authority가 아니라 relation 기원층
