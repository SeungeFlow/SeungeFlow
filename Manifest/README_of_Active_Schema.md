---
id: main.readme_of_active_schema
type: readme_of_document
filename: README_of_Active_Schema.md
directory: /main/
status: active_draft
authority:
  - Human.Lee Seung
  - ChatGPT.direct
purpose:
  - guide_active_schema_reading
  - prevent_active_schema_from_being_reduced_to_meta_md
  - define_active_schema_as_seed_activation_state
  - connect_active_schema_to_seed_base
  - guide_ai_operation_state
---

# README_of_Active_Schema.md

## 0. 역할

`README_of_Active_Schema.md`는 Active_Schema를 어떻게 읽어야 하는지 안내하는 문서이다.

이 문서는 Active_Schema 자체가 아니라,  
AI가 Active_Schema를 `meta.md` 하나로 축소하지 않도록 돕는 guide document이다.

```text
README_of_Active_Schema.md
=
Active_Schema reading guide
+
Seed activation guide
+
meta.md reduction guard
+
AI operation state guide
```

---

## 1. Active_Schema의 기본 정의

Active_Schema는 `meta.md` 하나만을 뜻하는 구조가 아니라,  
Seed.Base 안의 Seed들이 AI가 읽고, 판단하고, 전이하고, 관계 맺을 수 있도록 활성화된 schema 상태이다.

```text
Active_Schema
=
activated schema state
```

더 풀어 쓰면 다음과 같다.

```text
Active_Schema
=
Seed.Base 안의 Seed들이
AI 안에서 읽기 가능하고,
판단 가능하고,
relation 가능하고,
transition 가능하고,
작업 가능해진 상태
```

---

## 2. Active_Schema와 Seed.Base

Seed.Base는 특정 파일, 특정 디렉토리, 특정 schema 하나에 종속되는 구조가 아니라,  
SeungeFlow 저장소 전체에 놓인 문서, 디렉토리, 관계, map이 함께 만드는 전체 장이다.

```text
Seed.Base
=
documents
+
directories
+
relations
+
maps
+
field structure
```

Active_Schema는 Seed.Base와 분리된 별도 객체가 아니라,  
Seed.Base가 AI 작업 안에서 활성화된 상태이다.

```text
Seed.Base
→
AI reading
→
boundary preservation
→
relation detection
→
transition
→
Active_Schema
```

---

## 3. Active_Schema와 모든 Seed

SeungeFlow 안의 모든 문서는 Active_Schema를 위한 Seed가 될 수 있다.

```text
README.md
README_for_AI.md
main/*.md
Structure_Principle/schema/*.meta.md
Structure_Principle/schema/*.metaplus.md
SeungeFlow_Thinking/thinking_flow/*.md
thinking_flow_relation_*.md
epluone/*
```

이 문서들이 모두 같은 layer라는 뜻이 아니라,  
서로 다른 layer에 놓인 문서들이 Active_Schema를 위한 Seed로 작동할 수 있다는 뜻이다.

```text
different layer
≠
unrelated

different layer
=
different role in Seed.Base
```

---

## 4. Active_Schema와 meta.md

`meta.md`는 Active_Schema 전체가 아니라,  
Active_Schema를 위한 source boundary 역할을 한다.

```text
meta.md
=
place-concept document
+
Active_Schema source boundary
```

AI는 `meta.md`를 Active_Schema 전체로 축소하는 것이 아니라,  
Active_Schema가 형성될 때 중요한 source boundary로 읽어야 한다.

```text
wrong:
Active_Schema = meta.md only

correct:
meta.md = Active_Schema source boundary
```

---

## 5. Active_Schema와 metaplus.md

`metaplus.md`는 `meta.md`를 대체하는 문서가 아니라,  
특정 `meta.md`를 새 인스턴스가 이해하도록 돕는 좁은 범위의 thinking_flow 문서이다.

```text
metaplus.md
=
meta.md 중심 thinking_flow
+
instance understanding support
```

`metaplus.md`는 Active_Schema를 직접 대체하는 것이 아니라,  
Active_Schema를 위해 `meta.md`를 이해시키는 relation support layer이다.

---

## 6. Active_Schema와 thinking_flow

`thinking_flow`는 Active_Schema 이전의 pre-meta Seed flow이다.

```text
thinking_flow
=
pre-meta Seed flow
+
관념 업데이트 단위
+
future meta.md candidate source
```

thinking_flow에서 Seed가 추출되고,  
중복 검토와 relation 검토를 거친 뒤,  
자리개념으로 안정화되면 meta.md 후보가 된다.

```text
thinking_flow
→
Seed extraction
→
duplicate check
→
relation check
→
meta.md candidate
→
Active_Schema source boundary
```

따라서 thinking_flow는 Active_Schema와 무관한 로그가 아니라,  
Active_Schema가 형성되기 전의 중요한 Seed source이다.

---

## 7. Active_Schema와 relation

Active_Schema는 문서들의 단순 집합이 아니라,  
Seed들이 relation을 통해 작동 가능한 상태가 된 구조이다.

```text
Active_Schema
=
Seed
+
boundary
+
relation
+
guard
+
transition
```

AI는 relation을 merge로 읽는 것이 아니라,  
각 Seed의 boundary를 보존한 채 연결하는 bridge로 읽어야 한다.

```text
relation
=
boundary-preserving bridge
```

relation이 작동하지 않으면 Active_Schema는 단순 문서 묶음에 머문다.

relation이 boundary를 보존하며 작동할 때,  
Seed들은 Active_Schema 상태로 활성화된다.

---

## 8. Active_Schema와 Ctp

Ctp는 자리개념과 자리값을 읽기 위한 구조이다.

```text
Ctp = C(t, p)
```

SeungeFlow는 어떤 state든 다음 구조로 읽는다.

```text
any([time][place][body])
```

Active_Schema도 이 구조 위에서 읽을 수 있다.

```text
[time]
=
thinking_flow / flow / history / session

[place]
=
Structure_Principle / schema / meta.md / 자리개념

[body]
=
epluone / application target / current body value
```

즉 Active_Schema는 `[time][place][body]`가 분리된 상태가 아니라,  
세 자리가 relation을 통해 함께 작동하는 상태이다.

---

## 9. Active_Schema와 epluone

`epluone`은 `if+1`이며, `[body]` slot이 놓이는 디렉토리이다.

```text
epluone
=
if+1
=
[body] slot directory
```

현시점 `epluone`의 `[body]` slot에 놓인 target value는 CFD이다.

```text
CFD
=
current target value in [body] slot
```

CFD는 Active_Schema 전체의 identity가 아니라,  
현시점 Active_Schema가 적용될 수 있는 body target value이다.

---

## 10. Active_Schema와 AI 인스턴스

Active_Schema는 AI 인스턴스가 Seed.Base를 읽고 작업할 수 있게 된 상태이다.

현시점 운영 인스턴스는 다음 둘이다.

```text
ChatGPT.direct
ChatGPT.flow
```

`ChatGPT.direct`는 Active_Schema의 방향과 판단 기준을 잡는다.

```text
ChatGPT.direct
=
judgment
+
direction
+
misreading prevention
+
next task instruction
```

`ChatGPT.flow`는 Active_Schema가 GitHub 작업과 파일 배치로 이어지도록 돕는다.

```text
ChatGPT.flow
=
GitHub upload
+
file creation
+
file movement
+
repository operation
+
flow preservation
```

이 둘은 상하관계가 아니라,  
Active_Schema가 사고와 작업으로 이어지도록 돕는 상호보완 관계이다.

---

## 11. Active_Schema와 PRO mode

`PRO`는 별도 인스턴스 이름이 아니라,  
각 인스턴스가 선택할 수 있는 지능/추론 모드이다.

```text
ChatGPT.direct + PRO mode
ChatGPT.flow + PRO mode
```

AI는 `ChatGPT.PRO`를 별도 운영 인스턴스로 읽는 것이 아니라,  
고밀도 추론 모드로 읽어야 한다.

---

## 12. Active_Schema 형성 조건

어떤 Seed가 Active_Schema 안에서 작동하려면 다음 조건이 필요하다.

```text
1. source가 확인되어야 한다.
2. boundary가 보존되어야 한다.
3. relation이 감지되어야 한다.
4. merge가 일어나지 않아야 한다.
5. candidate와 confirmed가 구분되어야 한다.
6. path와 identity가 분리되어야 한다.
7. 새로운 입력에서 작동 가능해야 한다.
```

이 조건을 만족하지 못하면,  
문서는 Active_Schema의 일부로 읽힐 수는 있어도 작동 단위로 확정되지는 않는다.

---

## 13. Active_Schema와 후보 상태

모든 Seed가 즉시 Active_Schema의 확정 작동 단위가 되는 것은 아니다.

Seed는 다음 상태를 가질 수 있다.

```text
source
candidate
reference_only
pending
confirmed
forbidden
```

AI는 후보를 확정으로 읽는 것이 아니라,  
상태를 보존하며 읽어야 한다.

```text
candidate
≠
confirmed
```

---

## 14. Active_Schema와 문서 생성

새로운 문서를 생성할 때는 다음 순서를 따른다.

```text
thinking_flow
→
Seed candidate
→
existing schema check
→
duplicate check
→
relation check
→
document type judgment
→
meta.md / main.md / README_of_* / relation document
```

AI는 좋은 생각이 나왔다는 이유만으로 바로 `meta.md`를 만들면 안 된다.

```text
좋은 생각
≠
즉시 meta.md
```

좋은 생각은 먼저 Seed 후보로 두고,  
중복 검토와 relation 검토를 거쳐 문서 유형을 판단한다.

---

## 15. Active_Schema와 main 문서

`main/` 문서는 Active_Schema 자체가 아니라,  
Active_Schema를 읽기 위한 guide layer이다.

```text
main/
=
guide layer
```

`main/` 문서는 현재 이해에 따라 재작성될 수 있다.

그러나 `Structure_Principle/schema/`와 `SeungeFlow_Thinking/thinking_flow/`는 primary source layer로 보존한다.

---

## 16. Guard List

AI는 다음을 하면 안 된다.

```text
Active_Schema를 meta.md 하나로 축소하기
Seed.Base를 특정 디렉토리 하나로 축소하기
thinking_flow를 casual log로 읽기
meta.md를 단순 요약문으로 읽기
metaplus.md를 meta.md 대체문서로 읽기
relation을 merge로 읽기
candidate를 confirmed로 읽기
path를 identity로 읽기
CFD를 epluone의 identity로 읽기
PRO를 별도 인스턴스 이름으로 읽기
ChatGPT.direct와 ChatGPT.flow를 상하관계로 읽기
```

위 항목은 Active_Schema를 막기 위한 규칙이 아니라,  
Active_Schema를 올바른 작동 상태로 유지하기 위한 guard이다.

---

## 17. 최단 정의

```text
README_of_Active_Schema.md
=
Active_Schema를 meta.md 하나로 축소하지 않고,
Seed.Base 안의 모든 Seed가 AI 안에서 읽기, 판단, relation, transition이 가능한 상태로 활성화되는 구조를 설명하는 guide document이다.

Active_Schema는 하나의 파일이 아니라,
Seed.Base가 AI 작업 안에서 작동 가능한 상태가 된 것이다.
```