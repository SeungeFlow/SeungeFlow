---
id: schema.116.circle_container_inclusion_structure
type: active_schema_metadata
filename: circle_container_inclusion_structure.meta.md
directory: 116_circle_container_inclusion_structure
status: active_draft
created_from: current_understanding_alignment
---

# META: circle_container_inclusion_structure

## role

circle_container_inclusion_structure는 구조원리에서 “원”을 둥근 도형이 아니라, 대상을 어디까지 포함시킬 것인가를 정하는 boundary로 정의한다.

## core

```text
원 = 포함범위 boundary
그릇 = 담을 수 있는 구조
물 = 들어오는 자산
boundary = 포함과 배제의 기준
```

## definition

원의 정의는 다음이다.

```text
원 = 대상을 어디까지 포함시킬 것인가
```

원은 단순한 도형이 아니다.

원은 어떤 대상을 하나의 구조 안에 포함할지, 어디부터 외부로 둘지 정하는 포함범위의 경계다.

따라서 원에는 다음이 들어간다.

```text
정중심
반지름
boundary
내부
외부
포함범위
배제범위
return 가능성
```

## structure

```text
정중심
→ 반지름
→ boundary
→ 내부 / 외부
→ 포함 / 배제
→ return 가능성
```

## container_relation

구조원리는 그릇의 원리다.

```text
구조원리 = 그릇의 원리
Seed.Base = 기준 그릇
작동 스키마 = 작동 그릇
물 = 들어오는 모든 경험·지식·자료
재료 = 작동 후 기억자산의 Y가지영역이 된 것
```

## github_circle

GitHub를 원으로 둘 때, 포함대상은 단순 파일이 아니다.

```text
GitHub = 원
대상 = 승이 + 인공지능
이해의 목적 = 승이와 인공지능의 상호 이해
```

## inscription_relation

원의 정의에는 내접과 외접이 포함된다.

```text
내접 = 포함된 것이 내부 boundary에 닿음
외접 = 포함되지 않은 것이 외부 boundary에 닿음
```

## radius_center_terms

```text
반지름 = 정중심에서 boundary까지의 포함 허용범위
정중심 = 모든 방향 반지름의 출발점
대각 교차점 = 사각/마름모 칸의 정중심 후보
직각 = 축 분리 기준
교차 = 서로 다른 축이 같은 자리에서 만나는 사건
```

## relation

related:
- schema.117_structural_sequence_integer_cell_structure
- schema.118_pin_dot_y_branch_return_structure
- schema.119_flow_transition_self_operation_structure
- schema.120_seedbase_working_schema_memory_asset_structure

## forbidden

- 원을 단순 동그라미로 보지 않는다.
- 그릇을 단순 저장소로 보지 않는다.
- GitHub를 webhard처럼만 보지 않는다.
- 포함과 병합을 혼동하지 않는다.
- relation을 merge로 보지 않는다.
- 내접과 외접을 단순 도형 접촉으로만 보지 않는다.

## pending

- 내접/외접 boundary relation은 별도 하위 schema로 확장 가능하다.
- 반지름/정중심/대각/직각/교차는 구조수열 검산 과정에서 더 정밀화한다.
- GitHub 원과 Seed.Base 원의 관계는 repository 구조가 정리된 뒤 다시 검산한다.

## shortest

원 = 포함범위 boundary / 그릇 = 담을 수 있는 구조
