---
id: schema.067.meta_relation_boundary_bridge
type: active_schema_metadata
filename: meta_relation_boundary_bridge.meta.md
directory: 067_meta_relation_boundary_bridge
status: active_draft
prev: schema.066.principle_entity_relation_rule
---

# META: meta_relation_boundary_bridge

## role
meta_relation_boundary_bridge는 meta.md의 relation이 단순 링크 목록이 아니라, 개념과 원리를 직접 합치지 않고 각자의 boundary를 보존한 채 이어 주는 구조 경로임을 정의하는 schema이다.

## core
```text
relation = boundary-preserving bridge
relation = 합침 아님 / 끊김 아님 / boundary 보존 연결
```

## definition
relation은 개념을 직접 합치지 않는다.

relation은 각 개념의 boundary를 유지한다.

relation은 origin, role, layer, direction, forbidden을 보존하면서 필요한 연결만 표시한다.

## relation_types
```text
prev = 앞선 구조 / 발생 순서
next = 다음 구조 / 이어질 가능성
related = 직접 병합하지 않지만 연결되는 구조
parent = 상위 기준 구조
source = 기원 자료
target = 내려갈 방향
forbidden = 연결하면 안 되는 오해 방향
pending = 아직 확정하지 않은 연결 후보
```

## rule
```text
related라고 해서 같은 뜻이 아니다.
prev라고 해서 원인 전체가 아니다.
next라고 해서 자동 확정이 아니다.
source는 기원 trace다.
parent는 상위 구조다.
target은 내려갈 방향이다.
forbidden relation도 필요하다.
```

## why_needed
훈민정음 벡터연산기법, Ctp_당연한이론, 구조원리, 화학구조 구현, Renderer, Seed.Base, 자리개념, BADㆍC, WAXF, 마름모 수열, 전자껍질 구현은 서로 연결될 수 있지만 같은 것이 아니다.

이들을 한 문서에 섞으면 붕괴한다.

그러나 끊으면 다시 이어지지 않는다.

따라서 relation이 필요하다.

## relation
prev:
- schema.066_principle_entity_relation_rule

related:
- schema.057_seedbase_database_data_definition
- schema.058_seungeflow_thinking_pre_alignment
- schema.060_coherency
- schema.062_place_domain_definition
- schema.063_boundary_place_requirement
- schema.096_vector_operation_relation_index

## forbidden
- relation을 단순 링크로 보지 않는다.
- relation을 동일시로 보지 않는다.
- relation이 있다고 merge하지 않는다.
- related를 parent로 오해하지 않는다.
- source trace를 active schema identity로 오해하지 않는다.
- path를 relation identity로 보지 않는다.
- relation_reason 없이 relation만 나열하지 않는다.
- forbidden relation을 생략하지 않는다.

## pending
- relation_history.md와 relation field를 어떻게 동기화할지 후속 runtime schema에서 다룬다.
- active_navimap에서 relation type을 시각적으로 구분할 필요가 있다.
- relation identity는 path가 아니라 Seed / relation_history / schema_identity / navigation_layer로 보존한다.

## shortest
relation = 합침 아님 / 끊김 아님 / boundary 보존 연결
