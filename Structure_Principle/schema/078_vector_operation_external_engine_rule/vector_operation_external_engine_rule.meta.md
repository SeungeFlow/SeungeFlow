---
id: schema.078.vector_operation_external_engine_rule
type: active_schema_metadata
filename: vector_operation_external_engine_rule.meta.md
directory: 078_vector_operation_external_engine_rule
status: active_draft
prev: schema.077.water_molecule_angle_implementation
---

# META: vector_operation_external_engine_rule

## role
vector_operation_external_engine_rule은 벡터연산기법을 구조원리 본류에 직접 합치지 않고, 구조원리 이전에 형성된 선행 독립 문서집합 / 외부 engine으로 분리 운용하기 위한 schema이다.

이 meta 파일은 인공지능이 벡터연산기법을 화학구조 구현, 구조원리 본류, 훈민정음 관련 schema와 무리하게 병합하여 의미혼용을 일으키지 않도록 막는 기준이다.

## core

```text
벡터연산기 = 선행 독립 engine
구조원리 본류에 합치지 않는다.
relation만 보존한다.
```

## definition

벡터연산기법은 현재 구조원리 meta.md chain 안에서 새로 생성되는 하위 기능이 아니다.

벡터연산기법은 구조원리 작업 이전에 이미 형성된 선행 독립 문서집합이다.

따라서 구조원리 본류는 벡터연산기법을 흡수하지 않는다.

필요한 경우 relation으로 연결하고, 별도 실험장은 Gemini / 모아 같은 이기종 AI에 둘 수 있다.

## operation_mode

```text
operation_mode = separated
candidate_instance = Gemini / 모아
ChatGPT.direct = structure judgment / relation preservation / forced_fit blocking
```

## relation_rule

```text
Structure_Principle 본류
↔ reference relation
Vector_Operation_Documents
→ external experiment candidate
```

## role_split

```text
벡터연산기법 =
글자 / 소리 / 방향 / 자리 / 위상 / 동력 / 구조를 vectorizing하는 독립 engine

구조원리 =
자리 / boundary / relation / 도형 / visible_relation_field를 정리하는 본류

화학구조 구현 =
기존 과학조건값을 받아 visible_relation_field로 구현하는 applied branch
```

## forbidden

- 벡터연산기법을 구조원리 본류에 흡수하지 않는다.
- 벡터연산기법을 화학구조 구현과 합치지 않는다.
- 벡터연산기법을 훈민정음 하나로 축소하지 않는다.
- 벡터연산기법을 현재 schema chain의 부산물로 보지 않는다.
- Gemini / 모아 산출물을 final authority로 바로 채택하지 않는다.
- relation을 merge로 오해하지 않는다.

## relation

prev:
- schema.077_water_molecule_angle_implementation

related:
- schema.050_hunminjeongeum_vector_operation
- schema.060_coherency
- schema.061_vector_unlock
- schema.067_meta_relation_boundary_bridge
- schema.079_cheonjiiin_input_order_vowel_direction
- schema.080_sejong_body_observer_vector_frame
- schema.081_inner_vowel_pull_structure
- schema.096_vector_operation_relation_index

## pending

- 벡터연산기법 원문 문서집합의 실제 위치는 별도 index에서 정한다.
- Gemini 투입 문구는 사용자가 명시할 때만 작성한다.
- 구조원리와 벡터연산기법의 bridge는 active_navimap에서 relation으로만 표시한다.

## shortest

벡터연산기 = 분리 운용 / 선행 독립 engine / 구조원리에는 relation만 보존
