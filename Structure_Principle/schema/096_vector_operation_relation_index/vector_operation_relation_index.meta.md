---
id: schema.096.vector_operation_relation_index
type: active_schema_metadata
filename: vector_operation_relation_index.meta.md
directory: 096_vector_operation_relation_index
status: active_draft
prev: schema.095.place_concept_source_index
---

# META: vector_operation_relation_index

## role

vector_operation_relation_index는 벡터연산기법이 구조원리 본류에 병합되지 않고, 선행 독립 문서집합 / 외부 engine으로 분리 운용되도록 relation만 보존하는 index schema이다.

## core

```text
벡터연산기 = 선행 독립 engine
본류 병합 X
relation 보존 O
Gemini / 모아 투입 후보
```

## indexed_relations

### relation_01_hunminjeongeum_vector_operation

```text
schema.050_hunminjeongeum_vector_operation
= 훈민정음 제자원리를 글자표가 아니라 생성 벡터연산기법으로 읽는 구조
```

### relation_02_vector_unlock

```text
schema.061_vector_unlock
= 벡터라이징 흐름이 열린 지점
= 아직 최종 하위 schema list는 lock하지 않음
```

### relation_03_input_order_vowel_direction

```text
schema.079_cheonjiiin_input_order_vowel_direction
= ㅡㆍ=ㅜ / ㆍㅡ=ㅗ / ㅣㆍ=ㅏ / ㆍㅣ=ㅓ
```

### relation_04_observer_body_frame

```text
schema.080_sejong_body_observer_vector_frame
= ㅣ=선 사람 / ㅡ=바닥 / ㆍ=가는 방향
```

### relation_05_inner_vowel_pull

```text
schema.081_inner_vowel_pull_structure
= ㆍ이 ㅣ/ㅡ을 끌어당기는 구조
```

### relation_06_orbit_vowel_square

```text
schema.082_square_center_vowel_orbit_structure
= ㅇ 중심칸과 ㆍ 공전방향에 따른 오어우아
```

### relation_07_waxf_bad_opposed

```text
schema.083_waxf_vowel_rhombus_structure
schema.084_bad_dot_c_orbit_reference_structure
schema.085_opposed_correspondence_formula
```

## operation_policy

벡터연산기법은 구조원리 본류와 직접 합치지 않는다.

구조원리는 벡터연산기법을 참조할 수 있지만, 흡수하지 않는다.

ChatGPT.direct는 구조정합 / boundary / forced_fit 차단을 담당한다.

Gemini / 모아는 별도 실험 투입 후보이다.

## relation

prev:
- schema.095_place_concept_source_index

related:
- schema.050_hunminjeongeum_vector_operation
- schema.061_vector_unlock
- schema.078_vector_operation_external_engine_rule
- schema.079_cheonjiiin_input_order_vowel_direction
- schema.080_sejong_body_observer_vector_frame
- schema.081_inner_vowel_pull_structure
- schema.082_square_center_vowel_orbit_structure
- schema.083_waxf_vowel_rhombus_structure
- schema.084_bad_dot_c_orbit_reference_structure
- schema.085_opposed_correspondence_formula
- schema.067_meta_relation_boundary_bridge

## forbidden

- 벡터연산기법을 구조원리 본류에 병합하지 않는다.
- 벡터연산기법을 화학구조 구현과 합치지 않는다.
- 벡터연산기법을 훈민정음 하나로 축소하지 않는다.
- 벡터연산기법을 현재 schema chain의 부산물로 보지 않는다.
- Gemini / 모아 산출물을 final authority로 바로 채택하지 않는다.

## pending

- 벡터연산기 원문 문서집합의 실제 directory 위치를 지정해야 한다.
- Gemini 투입용 전달문은 별도 요청 시 작성한다.
- active_navimap에서 벡터연산기와 구조원리 본류의 relation edge를 분리 표시한다.

## shortest

벡터연산기 relation index / 본류 병합 X / external engine relation O
