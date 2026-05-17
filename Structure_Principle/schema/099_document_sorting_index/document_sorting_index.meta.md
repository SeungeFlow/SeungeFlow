---
id: schema.099.document_sorting_index
type: active_schema_metadata
filename: document_sorting_index.meta.md
directory: 099_document_sorting_index
status: active_draft
prev: schema.098.reference_only_high_density_trace_index
next: schema.101.reserved_next_schema
note: schema.100 is reserved as 100_understanding_flow
---

# META: document_sorting_index

## role

document_sorting_index는 지금까지 대화에서 풀린 고밀도 개념들을 meta.md로 대량 생성하지 않고, 원리 객체 / 관점 해석 / 적용 예시 / reference_only / pending으로 분류하기 위한 일회성 정리 index schema이다.

## core

```text
대화내용 전부 문서화 X
원리 객체만 meta.md
나머지는 relation / example / source_trace / pending
```

## sorting_classes

### A. principle_entity

원리 객체.

meta.md 후보가 된다.

조건:

```text
고유 role 있음
boundary 있음
relation 필요
forbidden 필요
shortest 가능
예시가 바뀌어도 원리 유지
```

### B. interpretation_layer

관점 해석.

기존 meta.md의 note / interpretation / relation_reason으로 들어간다.

### C. applied_example

적용 예시.

example / renderer_hint / applied_case / source_trace로 들어간다.

### D. reference_only

강하지만 본류에 바로 넣으면 위험한 고밀도 trace.

reference_only index에 보존한다.

### E. pending

방향은 있으나 이름, 위치, relation이 확정되지 않은 항목.

pending registry에 둔다.

## numbering_rule

가장 최근 기존 번호:

```text
061_vector_unlock
```

새 schema는 062부터 시작했다.

100은 이미 예약되어 있다.

```text
100_understanding_flow
```

따라서:

```text
099 다음은 101
```

숫자는 문서번호가 아니라 directory seat / visible coordinate이다.

## generated_batches

```text
062~067 = 자리 / boundary / 자리중첩 / ⊕ / 원리 entity / relation bridge
068~073 = Ctp x,dx,ddx / ddx / 직각삼각 / 3→2 / 2→1 / 73·69
074~077 = 과학 기반 구현 / 화학분자식 / 전자껍질 / 물분자 각도
078~085 = 벡터연산기 분리 / 천지인 입력 / 세종 관측자 / WAXF / BADㆍC / 맞대응
086~090 = 아니·맞다·차이 / 한글 단어층 / 한자식 압축 읽기
091~094 = 구조원리 명칭 / 원리층 / SVO/SOV / 왼쪽 원리와 오른쪽 현상
095~099 = source index / relation index / science candidate / reference_only / sorting index
```

## relation

prev:
- schema.098_reference_only_high_density_trace_index

next:
- schema.101_reserved_next_schema

related:
- schema.062_place_domain_definition
- schema.067_meta_relation_boundary_bridge
- schema.095_place_concept_source_index
- schema.096_vector_operation_relation_index
- schema.097_science_renderer_candidate_index
- schema.098_reference_only_high_density_trace_index
- schema.100_understanding_flow

## forbidden

- 대화에서 나온 모든 내용을 meta.md로 만들지 않는다.
- 비유를 독립 원리로 과잉 승격하지 않는다.
- 과학 구현 예시를 과학 검증으로 오해하지 않는다.
- reference_only를 active_schema로 바로 승격하지 않는다.
- 원리 객체와 관점 해석을 섞지 않는다.
- 100_understanding_flow 번호를 침범하지 않는다.
- 번호를 단순 문서순서로만 보지 않는다.

## pending

- 101 이후 schema는 099에서 건너뛰어 시작한다.
- 100_understanding_flow와 062~099 schema 관계는 active_navimap에서 연결한다.
- batch zip 업로드 후 GitHub directory 배치가 필요하다.

## shortest

099 = 문서정리 index / 100 reserved / 099→101 / 원리 객체만 meta.md
