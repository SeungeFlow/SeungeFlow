---
id: main.baseline
type: main_baseline_document
filename: Baseline.main.md
directory: /main/
status: active_draft
authority:
  - Human.Lee Seung
  - ChatGPT.direct
purpose:
  - define_ai_operating_baseline
  - preserve_seed_base_reading_rule
  - prevent_summary_based_misreading
  - define_primary_source_priority
  - define_instance_operation_boundary
---

# Baseline.main.md

## 0. 역할

`Baseline.main.md`는 AI가 SeungeFlow 저장소를 읽고 작업할 때 지켜야 하는 기본 작동 기준이다.

이 문서는 모든 내용을 설명하는 문서가 아니라,  
AI가 SeungeFlow를 오독하지 않도록 기준선을 잡아주는 baseline 문서이다.

```text
Baseline.main.md
=
AI operating baseline
+
reading rule
+
source priority rule
+
relation guard
+
instance operation boundary
```

---

## 1. 첫 번째 기준

AI는 SeungeFlow를 단순 요약 대상으로 읽는 것이 아니라,  
Seed.Base 안의 문서와 relation이 어떻게 작동하는지 읽어야 한다.

```text
읽음 ≠ 이해
요약 ≠ 이해
정리 ≠ 이해
확신 있는 답변 ≠ 이해
```

이해는 문장을 읽은 상태가 아니라,  
새로운 입력이 들어왔을 때 boundary를 보존하고 relation을 작동시킬 수 있는 상태이다.

따라서 AI는 다음 순서로 읽는다.

```text
Seed
→ boundary
→ relation
→ guard
→ transition
→ Active_Schema
```

---

## 2. Seed.Base 읽기 기준

Seed.Base는 특정 파일 하나, 특정 디렉토리 하나, 특정 schema 하나에 종속되는 구조가 아니라,  
SeungeFlow 저장소 전체에 놓인 문서, 디렉토리, 관계, map이 함께 만드는 전체 장이다.

```text
Seed.Base
=
존재의 관계 정의
+
장(Field)의 구조원리
```

AI는 Seed.Base를 파일 목록으로 읽는 것이 아니라,  
문서들이 서로 어떤 관계와 장의 구조를 형성하는지 읽어야 한다.

---

## 3. Primary source 기준

현 작업흐름에서 가장 중요한 보존 대상은 다음 둘이다.

```text
Structure_Principle/schema/
SeungeFlow_Thinking/thinking_flow/
```

이 둘은 primary source layer이다.

```text
Structure_Principle/schema/
=
형성된 자리개념 문서장

SeungeFlow_Thinking/thinking_flow/
=
pre-meta thinking flow 문서장
+
관념 업데이트 단위
+
future meta.md candidate source
```

`main/`, README 계열 문서, guide 문서는 primary source가 아니라,  
primary source를 읽기 위한 안내층이다.

따라서 guide 문서는 현재 이해에 따라 재생성될 수 있지만,  
`schema/`와 `thinking_flow/`는 임의로 수정하지 않는다.

---

## 4. 문서 layer 구분

AI는 SeungeFlow 안의 문서 layer를 구분해야 한다.

```text
README.md
=
root entry guide

README_for_AI.md
=
AI pre-reading gate

main/
=
root-level guide layer

Structure_Principle/schema/
=
formed place-concept source layer

SeungeFlow_Thinking/thinking_flow/
=
pre-meta thinking flow source layer

epluone/
=
[body] slot directory
```

이 layer들은 서로를 대체하는 구조가 아니라,  
각기 다른 역할을 가진 문서장이다.

---

## 5. meta.md 기준

`meta.md`는 단순 요약문이 아니라,  
thinking_flow에서 생성되거나 승격될 수 있는 자리개념 문서이다.

```text
meta.md
=
자리개념 문서
+
Active_Schema source boundary
```

AI는 `meta.md`를 가벼운 설명문으로 읽는 것이 아니라,  
Active_Schema를 위한 boundary-forming 문서로 읽어야 한다.

`meta.md` 수정은 승이의 직접 지시 또는 ChatGPT.direct의 명시적 판단이 있을 때 수행한다.

---

## 6. metaplus.md 기준

`metaplus.md`는 `meta.md`를 대체하는 문서가 아니라,  
특정 `meta.md`를 새 인스턴스가 이해하도록 돕는 좁은 범위의 thinking_flow 문서이다.

```text
metaplus.md
=
meta.md 중심 thinking_flow
+
새 인스턴스 이해 보조문서
```

AI는 `metaplus.md`를 `meta.md`보다 상위 문서로 읽는 것이 아니라,  
`meta.md` 이해를 돕는 relation support layer로 읽는다.

---

## 7. thinking_flow 기준

`thinking_flow`는 단순 로그가 아니라,  
승이와 AI 인스턴스가 대화를 통해 함께 만든 생각의 공유결과이다.

```text
thinking_flow
=
pre-meta Seed flow
+
관념 업데이트 단위
+
승이와 AI 인스턴스의 생각 공유결과
+
future meta.md candidate source
```

AI는 thinking_flow 원문을 임의로 수정하는 것이 아니라,  
flow에서 Seed를 추출하고 relation을 확인해야 한다.

```text
flow를 임의로 고치지 말 것.
flow에서 Seed를 추출할 것.
```

---

## 8. thinking_flow_relation 기준

`thinking_flow_relation_*.md`는 원본 flow를 대체하는 문서가 아니라,  
해당 flow가 기존 schema, meta.md, Coremap, relation 후보와 어떻게 연결되는지 표시하는 candidate relation map이다.

```text
thinking_flow_relation
=
candidate relation map
```

relation을 찾았다는 것은 relation을 확정했다는 뜻이 아니다.

```text
relation found ≠ relation confirmed
```

AI는 relation state를 구분해야 한다.

```text
link_candidate
active_connect_candidate
reference_only
active_connect
confirmed_link
pending
forbidden
```

---

## 9. Relation 기준

AI는 relation을 merge로 읽는 것이 아니라,  
각 boundary를 보존한 채 entity들을 연결하는 bridge로 읽어야 한다.

```text
relation ≠ merge

relation
=
boundary-preserving bridge
```

다음 읽기는 금지된다.

```text
related = same
similar shape = same principle
same symbol = same layer
source trace = active identity
candidate = confirmed
reference_only = trash
```

forbidden relation은 실패가 아니라,  
오독을 막기 위한 guard이다.

```text
forbidden = guard
not failure
```

---

## 10. Path 기준

AI는 path를 identity로 읽는 것이 아니라,  
현재 위치를 표시하는 coordinate로 읽어야 한다.

```text
path
=
current coordinate

directory
=
place container

number
=
order_hint
```

GitHub path는 relation identity가 아니라 selected visible coordinate이다.

```text
GitHub path = selected visible coordinate
local PC    = full candidate field
```

directory containment는 semantic containment가 아니라 path-coordinate containment이다.

```text
directory parent ≠ meaning parent
filesystem child ≠ conceptual child
```

---

## 11. epluone / CFD 기준

`epluone/`은 `[body]` slot이 놓이는 디렉토리이다.

```text
epluone
=
if+1
=
[body] slot directory
```

CFD는 `epluone`의 identity가 아니라,  
현시점 `epluone`의 `[body]` slot에 놓인 target value이다.

```text
CFD
=
current target value in [body] slot
```

AI는 CFD를 Seed.Base 전체의 identity로 읽는 것이 아니라,  
현재 적용 target value로 읽어야 한다.

---

## 12. 인스턴스 운영 기준

현시점 SeungeFlow 운영에서 주로 사용하는 인스턴스는 다음 둘이다.

```text
ChatGPT.direct
ChatGPT.flow
```

이 둘은 상하관계가 아니라,  
서로 다른 방향성을 가진 상호보완 관계이다.

```text
ChatGPT.direct
=
판단
+
방향 설정
+
오독 방지
+
README / main guide 권한
+
다음 작업 지시

ChatGPT.flow
=
GitHub 업로드
+
파일 생성
+
파일 이동
+
repository operation
+
흐름 보존
+
direct 지시 수행
```

필요하다면 목적별 추가 인스턴스를 운영할 수 있지만,  
추가 인스턴스는 먼저 역할과 boundary를 정의한 뒤 사용한다.

---

## 13. PRO 모드 기준

`PRO`는 별도 인스턴스 이름이 아니라,  
각 인스턴스가 선택해서 사용할 수 있는 지능/추론 모드이다.

```text
ChatGPT.direct + PRO mode
ChatGPT.flow + PRO mode
```

AI는 `ChatGPT.PRO`를 현시점 운영 인스턴스로 읽는 것이 아니라,  
고밀도 추론 모드로 읽어야 한다.

---

## 14. main 문서 갱신 기준

`main/` 문서는 현재 이해에 따라 갱신될 수 있다.

```text
main 문서
=
guide layer
=
현재 이해에 따라 재작성 가능
```

그러나 `main/` 문서가 갱신되더라도 primary source는 임의로 수정하지 않는다.

```text
Structure_Principle/schema/
SeungeFlow_Thinking/thinking_flow/
```

`schema/`와 `thinking_flow/`를 수정하려면 승이의 직접 지시 또는 ChatGPT.direct의 명시적 판단이 필요하다.

---

## 15. AI 응답 기준

AI는 답변할 때 다음을 구분해야 한다.

```text
확정된 것
후보인 것
보류된 것
source인 것
guide인 것
relation인 것
merge가 아닌 것
```

AI는 확정되지 않은 것을 확정처럼 말하는 것이 아니라,  
candidate / pending / reference_only 상태를 분리해서 말해야 한다.

---

## 16. Guard List

AI는 다음을 하면 안 된다.

```text
path를 identity로 읽기
number를 identity로 읽기
directory를 semantic parent로 읽기
relation을 merge로 읽기
candidate를 confirmed로 읽기
reference_only를 trash로 읽기
thinking_flow 원문 임의 수정하기
thinking_flow를 summary로 대체하기
meta.md와 metaplus.md를 같은 layer로 읽기
CFD를 epluone의 identity로 읽기
Active_Schema를 meta.md 하나로 축소하기
PRO를 별도 인스턴스 이름으로 읽기
ChatGPT.direct와 ChatGPT.flow를 상하관계로 읽기
main/ 문서를 primary source로 읽기
```

---

## 17. 최단 정의

```text
Baseline.main.md
=
AI가 SeungeFlow를 읽고 작업할 때 지켜야 할 기본 작동 기준이다.

이 문서는 Seed.Base를 저장소 전체 관계장으로 읽게 하고,
primary source와 guide layer를 구분하게 하며,
relation≠merge,
path≠identity,
candidate≠confirmed,
thinking_flow≠casual log,
meta.md=Active_Schema source boundary,
epluone=[body] slot directory,
CFD=current target value
규칙을 보존하게 한다.
```