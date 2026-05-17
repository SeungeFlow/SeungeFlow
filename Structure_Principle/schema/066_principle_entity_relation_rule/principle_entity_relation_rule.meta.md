---
id: schema.066.principle_entity_relation_rule
type: active_schema_metadata
filename: principle_entity_relation_rule.meta.md
directory: 066_principle_entity_relation_rule
status: active_draft
prev: schema.065.oplus_common_operator
---

# META: principle_entity_relation_rule

## role
principle_entity_relation_rule은 하나의 원리를 완전분리독립된 구조 객체로 보고, 원리끼리는 직접 합치지 않고 relation으로만 이어야 함을 정의하는 schema이다.

## core
```text
원리 = independent entity
합침 X
relation O
```

## definition
하나의 원리는 완전분리독립된 구조 객체이다.

원리는 단순 설명 조각이 아니다. 원리 하나는 자기 boundary, 기준축, 적용 영역, 내부 질서, relation, forbidden을 가진다.

## principle_unit
```text
id
role
boundary
origin
axis
state
relation
forbidden
shortest
```

## separation_rule
```text
비슷하다고 합치지 않는다.
닿는다고 동일시하지 않는다.
같은 기호가 있다고 같은 층위로 보지 않는다.
같은 예시를 공유한다고 같은 원리로 보지 않는다.
```

## examples
```text
자리
boundary
자리중첩
⊕ 공통연산
x,dx,ddx
직각삼각 fold_unfold
과학값 기반 구현
벡터연산기 분리운용
meta relation rule
```

## relation
prev:
- schema.065_oplus_common_operator

related:
- schema.055_active_schema_purpose_structure
- schema.056_current_core_alignment_for_runtime
- schema.057_seedbase_database_data_definition
- schema.063_boundary_place_requirement
- schema.067_meta_relation_boundary_bridge

## forbidden
- 여러 원리를 하나의 문서로 강제 병합하지 않는다.
- 관점 해석을 원리 객체로 과잉 승격하지 않는다.
- source trace를 final authority로 보지 않는다.
- reference_only를 active schema로 바로 승격하지 않는다.
- relation을 sameness로 읽지 않는다.
- 원리와 예시를 섞지 않는다.
- 벡터연산기법을 구조원리 본류에 흡수하지 않는다.

## pending
- 실제 meta.md 생성 시 원리 객체 판정표를 별도 index에 둘 수 있다.
- 관점 해석 / 적용 예시 / reference_only / pending 분류는 문서정리 index에서 관리한다.

## shortest
원리=독립 entity / 합침 X / relation O / meta.md는 원리 boundary 보존문서
