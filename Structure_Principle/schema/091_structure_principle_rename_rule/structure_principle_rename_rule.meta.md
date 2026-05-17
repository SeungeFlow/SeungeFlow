---
id: schema.091.structure_principle_rename_rule
type: active_schema_metadata
filename: structure_principle_rename_rule.meta.md
directory: 091_structure_principle_rename_rule
status: active_draft
prev: schema.090.hanja_compression_direction_reading
---

# META: structure_principle_rename_rule

## role

structure_principle_rename_rule은 기존 “구조이론” 명칭을 “구조원리”로 변경하고, 해당 명칭 변경의 의미와 사용 기준을 정의하는 schema이다.

## core

```text
구조이론 → 구조원리
원리 = 원의 순리 혹은 이치
```

## definition

구조원리는 완성된 이론이 아니다.

구조원리는 구조가 어떻게 발생하고, 자리 잡고, 관계를 만들고, 경계를 통과하고, 복귀하고, 다시 드러나는지를 읽는 작동 기준이다.

“이론”은 완성된 설명체계처럼 보일 수 있으므로, 현시점 본류 명칭은 “구조원리”로 변경한다.

## principle_definition

```text
원 = 닫힘 / 순환 / 중심 / 복귀 / 경계 / 반복 가능성
리 = 이치 / 흐름의 법 / 작동하는 질서
원리 = 원의 순리 혹은 이치
```

## loop_relation

```text
relation
→ boundary
→ return
→ history
→ relation
```

이 loop는 000으로 복귀해야 한다.

## naming_rule

```text
과거 명칭 = 구조이론
현시점 명칭 = 구조원리
```

repository / directory 명칭으로 이미 존재하는 Structure_Theory는 보존할 수 있다.

내용상 본류를 말할 때는 구조원리를 사용한다.

## relation

prev:
- schema.090_hanja_compression_direction_reading

related:
- schema.053_structure_principle_flow
- schema.055_active_schema_purpose_structure
- schema.056_current_core_alignment_for_runtime
- schema.057_seedbase_database_data_definition
- schema.092_principle_hidden_layer_structure
- schema.066_principle_entity_relation_rule

## forbidden

- 구조원리를 기존 과학이론의 대체 이론으로 보지 않는다.
- 구조원리를 완성된 최종 설명체계로 고정하지 않는다.
- 구조원리를 단순 철학명으로 축소하지 않는다.
- “구조이론”과 “구조원리”를 동시에 혼용하지 않는다.
- repository 이름과 개념명을 무리하게 동일시하지 않는다.

## pending

- GitHub directory 이름 Structure_Theory를 변경할지 여부는 별도 작업으로 둔다.
- 기존 문서 내부의 “구조이론” 표현을 전부 즉시 수정하지 않는다.
- 신규 문서부터 “구조원리”를 기본 명칭으로 쓴다.

## shortest

구조이론 → 구조원리 / 원리 = 원의 순리 혹은 이치
