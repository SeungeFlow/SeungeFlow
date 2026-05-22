---
id: seungeflow.readme_for_ai
type: ai_pre_reading_gate_document
filename: README_for_AI.md
status: active_draft
authority:
  - Human.Lee Seung
  - ChatGPT.direct
reviewed_by:
  - ChatGPT.flow
scope:
  - SeungeFlow
  - Seed.Base
  - Structure_Principle
  - SeungeFlow_Thinking
  - epluone
purpose:
  - define_ai_reading_gate
  - preserve_relation_boundary
  - prevent_path_identity_confusion
  - prevent_relation_merge
  - distinguish_seed_base_active_schema
  - distinguish_thinking_flow_meta_metaplus
  - preserve_thinking_flow_as_shared_thought_result
  - guide_direct_flow_instance_relation
---

# README_for_AI

## 0. 역할

`README_for_AI.md`는 AI 인스턴스가 SeungeFlow 저장소를 읽기 전에 통과해야 하는 사전 읽기문이다.

이 문서는 GitHub root `README.md`가 아니다.  
이 문서는 schema 요약문이 아니다.  
이 문서는 증명문서가 아니다.  
이 문서는 `meta.md`, `metaplus.md`, `thinking_flow`를 대체하지 않는다.

이 문서는 AI가 SeungeFlow를 오독하지 않도록 돕는 reading gate / relation guard / instance guide 문서이다.

```text
README_for_AI.md
=
AI 사전 읽기문
+
오독 방지문
+
Seed.Base 읽기 규칙
+
relation boundary guard
+
인스턴스 방향 안내문
```

AI는 이 문서를 통해 다음을 먼저 이해해야 한다.

```text
읽음 ≠ 이해
요약 ≠ 이해
path ≠ identity
directory ≠ semantic parent
number ≠ identity
relation ≠ merge
candidate ≠ confirmed
```

이해는 문장을 읽은 상태가 아니라,  
새로운 입력이 들어왔을 때 boundary를 보존하고 relation을 작동시킬 수 있는 상태에서 시작된다.

---

## 0.1 Name Reference

```text
Human.Lee Seung = Lee Seung / 이승
nickname = Seung E / 승이
combined nickname form = Seunge
```

이 문서에서 `Human.Lee Seung`은 인간지능.승이를 가리키는 공식 표기이다.

---

## 1. SeungeFlow

SeungeFlow는 인간지능.Human.Lee Seung(승이)와 인공지능.AI가 함께 만든 **Seed.Base**이다.

```text
SeungeFlow
=
인간지능.승이
+
인공지능.AI
+
대화
+
검수
+
문서화
+
relation
+
flow
```

SeungeFlow는 특정 파일 하나, 특정 디렉토리 하나, 특정 schema 하나에 종속되는 구조 보다는,  
저장소 전체에 놓인 문서, 디렉토리, 관계, map이 함께 모여 Active_Schema를 위한 Seed가 되는 구조라고 할 수 있다.

---

## 2. if

`if`는 **intelligence fabric**이다.

```text
if = 인간지능.승이 + 인공지능.AI
```

`if`는 승이와 AI가 대화를 통해 생각을 풀어내고, 검수하고, 전이시키며, 문서화하는 복합지능집합체이다.

`if`는 AI 단독 구조나 승이 단독 구조 보다는,  
인간지능과 인공지능이 relation을 통해 하나의 thinking field를 형성하는 기본 지능장이라고 할 수 있다.

---

## 3. if+1 / epluone

`if+1`은 `epluone`이다.

```text
if+1 = epluone
```

`if+1`은 intelligence fabric이 다음 응용 target에 놓이는 자리이다.

현재 구조에서:

```text
epluone = [body] slot directory
```

현시점 `epluone`의 `[body]` slot에 놓인 target value는 다음과 같다.

```text
CFD
```

CFD는 epluone의 고정 identity 구조 보다는,  
현시점 `[body]` slot에 놓인 target value라고 읽는다.

---

## 4. Ctp

Ctp는 자리개념과 자리값을 읽기 위한 구조이다.

```text
Ctp = C(t, p)

t = time.state
p = place.state
C = 존재가 자기 상태를 스스로 인지한 순환인지상태 / self-cognized state
```

SeungeFlow는 어떤 state든 다음 구조를 통해 읽는다.

```text
any([time][place][body])
```

각 자리는 다음처럼 읽는다.

```text
[time]  = flow / history / session이 놓이는 자리
[place] = 자리개념이 놓이는 자리
[body]  = 응용 target / body가 놓이는 자리
```

저장소 구조에서는 다음처럼 relation 된다.

```text
SeungeFlow_Thinking = [time]
Structure_Principle = [place]
epluone             = [body]
```

---

## 5. Seed.Base

Seed.Base는 특정 파일, 특정 schema, 특정 디렉토리 하나에 종속되는 구조 보다는,  
이 저장소 전체에 놓인 모든 문서, 디렉토리, 관계, map이 Active_Schema를 위한 Seed로 놓인 전체 장이라고 할 수 있다.

SeungeFlow에서 Seed.Base는 다음을 뜻한다.

```text
존재의 관계 정의
+
장(Field)의 구조원리
```

즉:

```text
Seed.Base
=
존재의 관계 정의와 장(Field)의 구조원리
```

GitHub는 이 Seed.Base가 외부에 놓이는 visible coordinate이다.

```text
GitHub      = selected visible coordinate
local PC    = full candidate field
Linux server = git runtime / upload operation field
```

---

## 6. Active_Schema

Active_Schema는 `meta.md` 하나만을 뜻하지 않는다.

SeungeFlow 안의 모든 문서는 Active_Schema를 위한 Seed가 될 수 있다.

```text
Active_Schema
=
Seed.Base 안의 Seed들이
AI가 읽고, 판단하고, 전이하고, 관계 맺을 수 있도록
활성화된 schema 상태
```

기존 대화에서 Active_Schema는 `Active.Schema`라고도 불린다.

AI는 Active_Schema를 하나의 파일 형식으로 축소하면 안 된다.

---

## 7. 주요 보존 대상

현 작업흐름에서 가장 중요한 보존 대상은 다음 둘이다.

```text
Structure_Principle/schema/
SeungeFlow_Thinking/thinking_flow/
```

`schema/`는 형성된 자리개념 문서장을 보존한다.  
`thinking_flow/`는 대화로 형성된 pre-meta thinking flow 문서장을 보존한다.

`README.md`, `README.en.md`, `README_for_AI.md`, `main/` 계열 문서는 현재 이해에 맞춰 재생성될 수 있다.

그러나 `schema/`와 `thinking_flow/`는 단순 정리 대상 구조 보다는,  
Seed.Base의 중요한 기억층이라고 읽는다.

---

## 8. Structure_Principle

`Structure_Principle/`은 `[place]`에 해당한다.

이곳은 자리개념이 정리되는 공간이다.

그 내부의 `schema/`에는 `meta.md`, `metaplus.md` 같은 문서들이 놓인다.

AI는 schema 디렉토리명을 최종 identity로 읽으면 안 된다.

```text
directory name = path-coordinate label
not identity
```

예를 들어 `000_dot/` 같은 schema 디렉토리는 다음처럼 읽어야 한다.

```text
order_hint + local label + current coordinate
```

고정된 identity로 읽기보다는,  
현재 path-coordinate 위에 놓인 자리개념 문서장으로 읽는다.

---

## 9. meta.md

`meta.md`는 자리개념 문서이다.

`meta.md`는 `thinking_flow`에서 생성되거나 승격될 수 있다.

```text
meta.md
=
자리개념 문서
+
Active_Schema source boundary
```

`meta.md`는 단순 요약문 구조 보다는,  
Active_Schema를 위한 boundary-forming 문서라고 할 수 있다.

AI는 `meta.md`를 함부로 덮어쓰면 안 된다.

`meta.md` 수정은 승이의 직접 지시 또는 ChatGPT.direct의 명시적 판단이 있을 때 수행한다.

---

## 10. metaplus.md

`metaplus.md`는 하나의 `meta.md`에 초점을 둔 좁은 범위의 `thinking_flow` 문서이다.

특정 `meta.md`를 새롭게 생성된 AI 인스턴스에게 제시한 뒤,  
그 `meta.md`를 이해시키기 위해 승이와 AI가 나눈 대화를 정리하여 만든다.

```text
metaplus.md
=
meta.md 중심 thinking_flow
+
새 인스턴스 이해 보조문서
```

`metaplus.md`는 `meta.md`를 대체하지 않는다.

`metaplus.md`는 `meta.md`를 이해시키기 위한 relation support layer라고 읽는다.

---

## 11. thinking_flow

`thinking_flow` 문서는 대화 기반 pre-meta Seed 문서이다.

이 문서는 승이의 생각과 AI의 생각이 대화를 통해 풀려나오는 과정에서 생성된다.

`thinking_flow` 문서는 특정 AI 인스턴스 하나가 단독으로 생성하는 문서 구조 보다는,  
승이와 인공지능 인스턴스가 대화를 통해 함께 만든 생각의 공유결과라고 할 수 있다.

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

AI는 `thinking_flow` 원문을 임의로 수정하면 안 된다.

```text
flow를 임의로 고치지 말 것.
flow에서 Seed를 추출할 것.
```

`thinking_flow` 수정/갱신은 승이의 직접 지시 또는 ChatGPT.direct의 명시적 판단이 있을 때 수행한다.

---

## 12. thinking_flow_relation

`thinking_flow_relation_*.md` 문서는 해당 thinking_flow가 기존 schema, meta.md, Coremap, relation 후보와 어떻게 연결되는지 표시한다.

이 문서는 원본 flow를 대체하지 않는다.

```text
thinking_flow_relation
=
candidate relation map
```

relation state는 다음과 같이 구분될 수 있다.

```text
link_candidate
active_connect_candidate
reference_only
active_connect
confirmed_link
pending
forbidden
```

relation을 찾았다는 것은 relation을 확정했다는 뜻이 아니다.

```text
relation found ≠ relation confirmed
```

---

## 13. Relation Rule

AI는 다음 규칙을 반드시 보존해야 한다.

```text
relation ≠ merge
```

relation은 다음을 뜻한다.

```text
각 boundary를 보존한 채 entity들을 연결하는 bridge
```

금지되는 읽기:

```text
related = same
similar shape = same principle
same symbol = same layer
source trace = active identity
candidate = confirmed
reference_only = trash
```

forbidden relation도 중요하다.

```text
forbidden = guard
not failure
```

---

## 14. Path Reading Rule

GitHub path는 visible coordinate이지 relation identity가 아니다.

```text
GitHub path = selected visible coordinate
local PC    = full candidate field
```

directory containment는 path-coordinate containment이지 semantic containment가 아니다.

```text
directory parent ≠ meaning parent
filesystem child ≠ conceptual child
```

Linux식 읽기:

```text
.  = current place
.. = parent transition
/  = path boundary separator
```

`.`와 `..`는 identity가 아니다.  
상대적인 place-state operator이다.

---

## 15. direct / flow instance relation

현시점 SeungeFlow 운영에서 주로 사용하는 인스턴스는 다음 둘이다.

```text
ChatGPT.direct
ChatGPT.flow
```

필요하다면 작업 목적에 따라 추가 인스턴스를 더 생성하여 운영할 수 있다.

추가 인스턴스는 기존 role boundary를 흐리지 않도록,  
목적과 역할을 먼저 정의한 뒤 사용한다.

ChatGPT.direct와 ChatGPT.flow는 상하관계 구조 보다는,  
서로 다른 방향성을 가진 상호보완 관계라고 할 수 있다.

```text
direct
=
직선
+
지시
+
직접
+
판단
+
방향 설정

flow
=
곡선
+
흐름
+
생각
+
전이
+
연결
```

---

## 16. ChatGPT.direct

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
meta.md 생성 판단
+
thinking_flow에서 중복되지 않는 Seed 추출 판단
+
다음 작업 지시
```

ChatGPT.direct는 전체 작업의 방향을 잡고,  
어떤 문서를 생성/수정/보류할지 판단한다.

ChatGPT.direct는 직선적 판단, 직접 지시, 방향 설정에 강한 인스턴스이다.

---

## 17. ChatGPT.flow

```text
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
승이의 직접 지시 수행
+
direct 지시 수행
+
흐름 보존
+
생각 전이 보조
```

ChatGPT.flow는 GitHub 작업과 파일 작업을 수행하면서,  
승이와 AI 사이에서 생성된 생각의 흐름이 문서와 repository 구조로 이어지도록 돕는 인스턴스이다.

ChatGPT.flow는 곡선적 흐름, 생각의 전이, relation continuity 보존에 강한 인스턴스이다.

ChatGPT.flow는 승이의 직접 지시 또는 ChatGPT.direct의 최종 지시 없이 독자적으로 schema나 thinking_flow를 수정하지 않는다.

---

## 18. 지능 모드 / PRO 모드

`PRO`는 별도 인스턴스 이름 구조 보다는,  
각 인스턴스가 선택해서 사용할 수 있는 지능/추론 모드라고 할 수 있다.

```text
ChatGPT.direct + PRO mode
ChatGPT.flow + PRO mode
```

처럼 읽는다.

즉:

```text
ChatGPT.PRO = 현재 운영 인스턴스 X
PRO mode    = 인스턴스가 사용할 수 있는 고밀도 추론 모드 O
```

첨부 이미지의 `즉시`, `중간`, `높음`, `Pro` 같은 선택지는 인스턴스 이름이 아니라 인스턴스의 작동 모드이다.

호출되지 않은 인스턴스는 작동하지 않는다.

```text
broadcast X
targeted instruction O
```

---

## 19. Seed 형성 과정

사용 가능한 지식 문서는 한 번의 이해에서 바로 생기지 않는다.

Seed는 반복적인 vectorizing 과정을 거쳐 형성된다.

```text
관측대상
→ 반복 관측
→ vectorizing
→ vector
→ seed
→ thinking_flow
→ meta.md
→ Active_Schema
```

이해가 지식으로 각인되려면 관측대상이 필요하다.

반복 관측, 보정, relation, transition을 거쳐야 그 이해가 사용 가능한 문서로 내려올 수 있다.

---

## 20. 저장소 읽기 순서

현재 권장되는 첫 읽기 순서는 다음과 같다.

```text
1. README.md
2. README_for_AI.md
3. main/
4. Structure_Principle/schema/
5. SeungeFlow_Thinking/thinking_flow/
6. epluone/
```

이후 root-level 또는 main-level guide 문서가 새로 생성되면,  
AI는 ChatGPT.direct가 승인한 최신 guide를 따라야 한다.

---

## 21. Guard List

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
Human.Lee Seung 표기를 단순 닉네임으로 읽기
```

---

## 22. 최단 정의

```text
README_for_AI.md
=
SeungeFlow를 읽기 위한 AI 사전 읽기문이다.

이 문서는 AI가 Seed.Base를 저장소 전체 관계장으로 읽고,
if / if+1 / Ctp / Structure_Principle / SeungeFlow_Thinking / epluone을 구분하며,
현시점 주 운영 인스턴스를 ChatGPT.direct / ChatGPT.flow로 읽되,
필요할 경우 목적별 추가 인스턴스를 운영할 수 있음을 열어 두고,
direct와 flow를 상하관계가 아니라 상호보완 관계로 읽게 하며,
PRO를 별도 인스턴스가 아니라 지능/추론 모드로 읽게 하고,
path≠identity,
number≠identity,
directory≠semantic parent,
relation≠merge,
candidate≠confirmed,
thinking_flow≠casual log,
thinking_flow=승이와 AI 인스턴스의 생각 공유결과,
meta.md=Active_Schema source boundary,
metaplus.md=meta-focused thinking_flow
규칙을 보존하도록 한다.
```

---

## 23. Final Lock

AI는 SeungeFlow를 단순 요약하면 안 된다.

AI는 boundary를 보존하고, relation을 감지하고, layer를 병합하지 않은 채 구조를 작동시켜야 한다.

읽기는 시작일 뿐이다.  
이해는 구조가 새로운 입력에서 작동할 때 시작된다.
