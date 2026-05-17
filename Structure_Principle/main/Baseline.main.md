---
id: main.baseline
type: structure_principle_main_document
filename: Baseline.main.md
directory: /Structure_Principle/main/
status: active_draft
scope:
  target: Structure_Principle
  role: baseline_reading_and_operation_rule
  source_range: 000~121
created_for:
  - ChatGPT.direct
  - Active.Schema scan
depends_on:
  - schema.000.dot
  - schema.066.principle_entity_relation_rule
  - schema.067.meta_relation_boundary_bridge
  - schema.099.document_sorting_index
  - schema.100.understanding_flow
  - schema.120.seedbase_working_schema_memory_asset_structure
  - schema.121.coredot_ambiguity_boundary
---

# Baseline.main

## 0. role

`Baseline.main.md`는 `/Structure_Principle/main/`의 기준 문서이다.

이 문서는 `Structure_Principle/schema/`에 있는 122개 core schema를 AI가 어떻게 읽어야 하는지,
무엇을 본류로 세우고, 무엇을 source trace / relation / candidate / reference_only / pending으로 보존해야 하는지,
그리고 어떤 방식으로 Active.Schema를 형성해야 하는지를 정의한다.

```text
Baseline.main.md
=
Structure_Principle 전체를 읽기 위한 기준 boundary
```

## 1. Structure_Principle definition

```text
Structure_Principle
=
빈자리에서 시작해,
dot을 최소 자리로 세우고,
boundary를 세우고,
relation을 만들고,
return 가능성을 검산하며,
source와 active를 구분하고,
core들의 boundary를 보존한 채,
현재 목적에 맞는 working schema로 재구성하는 원리 체계
```

압축 정의:

```text
Structure_Principle
=
place → boundary → relation → return → guard → working schema
```

더 짧게:

```text
Structure_Principle
=
place-first,
boundary-preserving,
return-oriented,
guarded active schema system
```

## 2. Active.Schema definition

```text
Active.Schema
=
122개 core schema를 단순히 저장하거나 요약하지 않고,
각 core의 boundary와 relation을 보존하면서,
현재 목적에 맞는 하나의 작동 schema를 만들어내는 체계
```

Active.Schema는 결과물이면서 동시에 작동 과정이다.

```text
schema = form
schema relation 작업 = forming
snapshot = formed
coremap = formed 사이 relation map + formed를 다시 forming으로 여는 gate
```

## 3. directory / meta / metaplus rule

하나의 schema directory는 하나의 core container이다.

```text
directory
=
core container

meta.md
=
core definition
+
core boundary

metaplus.md
=
AI/user understanding log
+
correction layer
+
misunderstanding guard
+
relation trace
+
pending / reference boundary
```

따라서 AI는 파일명만 보고 판단하지 않는다.

```text
wrong:
directory name → summary

correct:
meta.md + metaplus.md → core understanding unit
```

## 4. core rule

각 core는 독립 entity로 읽는다.

```text
core
=
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

비슷하다고 합치지 않는다.

```text
same word ≠ same core
same sign ≠ same layer
same example ≠ same principle
relation ≠ merge
```

## 5. relation rule

relation은 단순 link가 아니다.

```text
relation
=
각 core의 boundary를 보존한 채 이어주는 bridge
```

`Coremap.main.md`에서 사용하는 relation type은 다음을 따른다.

```text
prev      = 앞선 구조 / 발생 순서
next      = 다음 구조 / 이어질 가능성
related   = 직접 병합하지 않지만 연결되는 구조
parent    = 상위 기준 구조
source    = 기원 자료 / source trace
target    = 내려갈 방향
forbidden = 연결하면 안 되는 오해 방향
pending   = 아직 확정하지 않은 연결 후보
```

핵심 guard:

```text
related라고 해서 같은 뜻이 아니다.
prev라고 해서 원인 전체가 아니다.
next라고 해서 자동 확정이 아니다.
source는 기원 trace다.
forbidden relation도 필요하다.
```

## 6. source / candidate / reference sorting rule

모든 고밀도 trace를 active schema로 승격하지 않는다.

분류 기준:

```text
principle_entity
interpretation_layer
applied_example
reference_only
pending
```

### principle_entity condition

```text
고유 role이 있다.
boundary가 있다.
relation이 필요하다.
forbidden이 필요하다.
shortest로 압축 가능하다.
예시가 바뀌어도 원리가 유지된다.
```

### reference_only condition

```text
강하지만 본류에 바로 넣으면 위험하다.
과학 / 역사 / 문화 / 언어 / 외부 engine과 직접 섞일 위험이 있다.
trace로 보존해야 하지만 active core로 즉시 올리면 안 된다.
```

Reference-only는 폐기가 아니다.

```text
reference_only
=
high-density trace preservation layer
```

## 7. 000~099 / 100 / 101~121 reading rule

전체 schema는 번호순 목록이 아니다.
순서는 발생 순서이지만, 후속 core가 앞 core를 다시 보완한다.

```text
000~099
=
formed source schema phase

100
=
understanding_flow empty gate

101~121
=
rebuilt active schema phase
```

### 000~099

```text
formed source schema phase
=
원형
기초
확장
source trace
relation index
candidate index
reference_only
document sorting
```

### 100

```text
100
=
understanding_flow reserved seat
+
empty phase gate
+
formed-to-rebuilt buffer
```

100은 누락 번호가 아니다.

```text
100을 일반 개념 schema로 채우지 않는다.
100을 source trace로 채우지 않는다.
099와 101을 직접 접착하지 않는다.
```

### 101~121

```text
rebuilt active schema phase
=
source trace를 그대로 잇지 않고
현재 이해 기준으로 다시 reading / boundary / return / contact / operation을 세우는 chain
```

## 8. dot preservation rule

`000_dot`은 재정의하지 않는다.

```text
000_dot
=
최초 최소 자리
값이 아니라 자리
선 / 벡터 / 수열구조 / 자리연산이 시작되는 최소 구조 단위
```

후속 schema는 dot을 계속 보완한다.

```text
059 = dot-anchor / present anchor 보완
079~085 = ㅇ / ㆍ dot layer 구분
118 = pin = 작동 가능한 dot
121 = CoreDot ambiguity boundary
```

그러나 후속 보완은 `000_dot`을 replace하지 않는다.

```text
dot.meta.md
=
origin core로 보존

CoreDot
=
보류 / ambiguity boundary
```

금지:

```text
CoreDot을 dot의 본명으로 쓰지 않는다.
CoreDot을 ㆍ의 정체로 쓰지 않는다.
CoreDot을 Coremap의 최소 단위로 쓰지 않는다.
CoreDot으로 dot.meta.md를 덮어쓰지 않는다.
```

## 9. working schema rule

`120_seedbase_working_schema_memory_asset_structure` 기준:

```text
Seed.Base
=
기준 그릇

working_schema
=
작동 그릇

water / incoming asset
=
들어오는 경험 / 학문 / 대화 / 감각 / 과학값 / 예시 / 기억자산 / 구조재료

material
=
working schema를 통과해 relation flow와 accumulation을 거친 기억자산
```

자료는 곧바로 지식이 아니다.

```text
raw_data
→ working_schema_operation
→ relation_flow
→ accumulation
→ materialization
→ memory_asset
```

## 10. link / connect distinction

```text
link
=
논리적 연결
relation potential

connect
=
실제 작동 연결
relation operation
```

Coremap에 edge가 있다고 해서 실제 connect가 성립한 것은 아니다.

```text
coremap edge = link 후보
active operation = connect 검산 필요
```

## 11. AI reading protocol

AI는 다음 순서로 읽는다.

```text
1. directory 확인
2. meta.md 읽기
3. metaplus.md 읽기
4. meta와 metaplus의 차이 확인
5. core boundary 추출
6. misunderstanding guard 추출
7. relation 후보 추출
8. source / candidate / reference_only / pending 분류
9. 후속 core가 앞 core를 보완한 흔적 확인
10. coremap edge로 배치
```

읽었다고 이해한 것이 아니다.

```text
read ≠ understand
summary ≠ understand
naming ≠ understand
understanding = boundary + relation + guard + return + preservation reason
```

## 12. global guard

```text
파일명만 보지 않는다.
번호에 매몰되지 않는다.
source trace를 final authority로 보지 않는다.
reference_only를 폐기물로 보지 않는다.
relation을 merge로 보지 않는다.
CoreDot으로 dot을 덮지 않는다.
과학값 기반 구현을 과학검증으로 착각하지 않는다.
한글/한자/언어 구조해석을 표준 어원 확정으로 주장하지 않는다.
vector operation external engine을 Structure_Principle 본류에 흡수하지 않는다.
meta.md와 metaplus.md를 같은 층위로 보지 않는다.
```

## 13. shortest

```text
Baseline.main.md
=
Structure_Principle을 읽고 Active.Schema를 형성하기 위한 기준 boundary
```
