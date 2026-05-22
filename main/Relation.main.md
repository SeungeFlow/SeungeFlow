---
id: main.relation
type: main_relation_document
filename: Relation.main.md
directory: /main/
status: active_draft
authority:
  - Human.Lee Seung
  - ChatGPT.direct
purpose:
  - define_relation_reading_rule
  - preserve_boundary_between_entities
  - prevent_relation_merge
  - connect_seed_base_field_structure
  - guide_core_relation_and_thinking_flow_relation
---

# Relation.main.md

## 0. 역할

`Relation.main.md`는 SeungeFlow에서 relation을 어떻게 읽어야 하는지 정의하는 문서이다.

이 문서는 단순 연결 목록이 아니라,  
존재의 관계 정의와 장(Field)의 구조원리를 relation 관점에서 정리하는 guide 문서이다.

```text
Relation.main.md
=
relation reading rule
+
boundary-preserving guide
+
field-structure guide
+
merge prevention guard
```

---

## 1. relation의 기본 정의

SeungeFlow에서 relation은 entity를 병합하는 것이 아니라,  
각 boundary를 보존한 채 entity들을 잇는 bridge이다.

```text
relation
=
boundary-preserving bridge
```

따라서 relation은 다음처럼 읽는다.

```text
entity A
+
boundary
+
bridge
+
boundary
+
entity B
```

relation은 두 대상을 하나로 만드는 것이 아니라,  
두 대상이 서로를 침범하지 않으면서 이어지는 구조이다.

---

## 2. relation ≠ merge

AI는 relation을 merge로 읽으면 안 된다.

```text
relation ≠ merge
```

이 문장은 relation을 부정하는 것이 아니라,  
relation을 boundary-preserving bridge로 읽으라는 뜻이다.

```text
wrong:
related = same

correct:
related = connected while preserving boundary
```

즉 relation은 같아지는 것이 아니라,  
다른 상태를 유지한 채 연결되는 것이다.

---

## 3. relation과 boundary

relation이 성립하려면 boundary가 먼저 보존되어야 한다.

```text
boundary 없는 relation
=
merge risk
```

boundary는 relation을 막는 벽이 아니라,  
relation이 merge로 무너지지 않게 하는 기준선이다.

```text
boundary
=
relation preservation condition
```

따라서 AI는 두 문서, 두 개념, 두 field가 연결되어 있다고 해서  
그 boundary를 지우면 안 된다.

---

## 4. relation과 Seed.Base

Seed.Base는 단일 파일이나 단일 schema가 아니라,  
문서, 디렉토리, 관계, map이 함께 만드는 전체 장이다.

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

Relation은 Seed.Base 안의 Seed들이 서로 어떻게 이어지는지 보여주는 구조이다.

즉 relation은 Seed.Base의 부가 요소가 아니라,  
Seed.Base가 하나의 field로 작동하게 만드는 핵심 조건이다.

---

## 5. relation과 Field

Field는 단순 공간이 아니라,  
relation이 놓이고 작동하는 장이다.

```text
Field
=
place
+
boundary
+
relation
+
transition
+
return possibility
```

AI는 field를 배경으로 읽는 것이 아니라,  
relation이 작동하는 구조장으로 읽어야 한다.

즉:

```text
relation 없는 field
=
단순 배경

relation이 작동하는 field
=
구조장
```

---

## 6. relation과 Ctp

Ctp는 자리개념과 자리값을 읽기 위한 구조이다.

```text
Ctp = C(t, p)
```

relation은 Ctp 안에서 다음처럼 놓일 수 있다.

```text
time.state relation
place.state relation
body target relation
```

또한 SeungeFlow는 어떤 state든 다음 구조를 통해 읽는다.

```text
any([time][place][body])
```

따라서 relation도 다음 세 자리에서 읽을 수 있다.

```text
[time] relation
=
flow / history / session 사이의 relation

[place] relation
=
자리개념 / schema / meta.md 사이의 relation

[body] relation
=
응용 target / CFD / epluone 사이의 relation
```

---

## 7. relation과 path

path는 relation identity가 아니라,  
relation을 찾을 때 참고할 수 있는 visible coordinate이다.

```text
path
=
visible coordinate

path
≠
relation identity
```

같은 디렉토리에 있다는 것은 relation 후보가 될 수 있지만,  
그 자체로 relation 확정을 뜻하지 않는다.

```text
same directory
≠
confirmed relation
```

가까운 path는 가까운 의미를 보장하지 않는다.

```text
near path
≠
same principle
```

따라서 relation은 path가 아니라,  
문서 boundary와 relation record를 통해 판단해야 한다.

---

## 8. relation과 thinking_flow

`thinking_flow`는 승이와 AI 인스턴스가 대화를 통해 함께 만든 생각의 공유결과이다.

```text
thinking_flow
=
pre-meta Seed flow
+
관념 업데이트 단위
+
future meta.md candidate source
```

`thinking_flow_relation_*.md` 문서는 해당 flow가 기존 schema, meta.md, Coremap, relation 후보와 어떻게 연결되는지 표시한다.

```text
thinking_flow_relation
=
candidate relation map
```

AI는 thinking_flow_relation을 확정 relation으로 읽는 것이 아니라,  
candidate relation map으로 읽어야 한다.

```text
relation found
≠
relation confirmed
```

---

## 9. relation과 meta.md

`meta.md`는 자리개념 문서이며,  
Active_Schema를 위한 source boundary 역할을 한다.

```text
meta.md
=
place-concept document
+
Active_Schema source boundary
```

`meta.md` 간의 relation은 단순히 파일 사이의 연결이 아니라,  
자리개념 사이의 relation이다.

따라서 AI는 `meta.md` relation을 문서 링크로만 읽는 것이 아니라,  
자리개념 사이의 boundary-preserving bridge로 읽어야 한다.

---

## 10. relation과 metaplus.md

`metaplus.md`는 특정 `meta.md`를 새 인스턴스가 이해하도록 돕는 좁은 범위의 thinking_flow 문서이다.

```text
metaplus.md
=
meta.md 중심 thinking_flow
+
새 인스턴스 이해 보조문서
```

`metaplus.md`는 `meta.md`를 대체하는 것이 아니라,  
`meta.md` 이해를 돕는 relation support layer이다.

따라서 `metaplus.md`가 어떤 relation을 설명하더라도,  
AI는 그것을 `meta.md`의 boundary를 덮어쓰는 것으로 읽으면 안 된다.

---

## 11. relation state

relation은 발견되었다고 해서 모두 확정되는 것이 아니다.

relation은 상태를 가진다.

```text
link_candidate
active_connect_candidate
reference_only
active_connect
confirmed_link
pending
forbidden
```

각 상태는 다음처럼 읽는다.

```text
link_candidate
=
관계 후보

active_connect_candidate
=
작동 가능성이 높은 연결 후보

reference_only
=
강하지만 직접 승격하지 않는 참조 관계

active_connect
=
현재 작동 중인 연결

confirmed_link
=
확정된 연결

pending
=
보류된 연결

forbidden
=
오독을 막기 위해 금지된 연결
```

AI는 candidate를 confirmed로 읽는 것이 아니라,  
relation state를 보존한 채 읽어야 한다.

---

## 12. forbidden relation

forbidden relation은 실패가 아니라,  
오독을 막기 위한 guard이다.

```text
forbidden
=
guard
not failure
```

예를 들어:

```text
CoreDot이 dot을 대체한다
```

와 같은 읽기는 forbidden relation으로 잠글 수 있다.

이 경우 forbidden은 연결이 없다는 뜻이 아니라,  
특정 방향의 오독을 막는 boundary guard이다.

---

## 13. relation의 금지되는 오독

AI는 다음을 하면 안 된다.

```text
related = same 으로 읽기
similar shape = same principle 로 읽기
same symbol = same layer 로 읽기
source trace = active identity 로 읽기
candidate = confirmed 로 읽기
reference_only = trash 로 읽기
forbidden = failure 로 읽기
path = relation identity 로 읽기
```

이 금지 목록은 relation을 막는 것이 아니라,  
relation을 올바른 boundary-preserving bridge로 되돌리기 위한 guard이다.

---

## 14. relation과 외형 유사성

외형이 비슷하다는 것은 relation 후보가 될 수 있지만,  
그 자체로 같은 원리를 뜻하지 않는다.

```text
similar shape
≠
same principle
```

예를 들어 Y branch와 4-rhombus가 연결될 수 있는 이유는  
외형이 닮아서가 아니라, 내부 전이 구조와 방향 대응 구조가 relation을 만들기 때문이다.

```text
Y branch
=
branch transition

4-rhombus
=
direction correspondence field
```

따라서 AI는 외부 형상을 따라 병합하는 것이 아니라,  
내부 전이 구조와 장의 관계를 확인해야 한다.

---

## 15. relation과 CFD

CFD는 epluone의 identity가 아니라,  
현시점 `epluone`의 `[body]` slot에 놓인 target value이다.

```text
epluone
=
[body] slot directory

CFD
=
current target value in [body] slot
```

CFD와 Seed.Base의 relation은 identity relation이 아니라,  
current application target relation이다.

```text
CFD
≠
Seed.Base identity

CFD
=
current body target value
```

---

## 16. relation과 direct / flow

ChatGPT.direct와 ChatGPT.flow는 상하관계가 아니라,  
서로 다른 방향성을 가진 상호보완 relation이다.

```text
ChatGPT.direct
=
판단
+
방향 설정
+
오독 방지
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
```

direct는 flow를 지배하는 위치가 아니라,  
작업 방향과 판단 boundary를 잡는 인스턴스이다.

flow는 direct의 하위 인스턴스가 아니라,  
GitHub 작업과 흐름 보존을 담당하는 상호보완 인스턴스이다.

---

## 17. Relation.main.md와 Coremap

`Relation.main.md`는 Coremap을 대체하는 문서가 아니라,  
relation을 어떻게 읽어야 하는지 설명하는 main guide 문서이다.

```text
Relation.main.md
=
relation reading guide

Coremap
=
core relation map
```

Coremap이 relation edge의 map이라면,  
Relation.main.md는 그 relation edge를 어떤 원칙으로 읽어야 하는지 설명하는 guide이다.

---

## 18. 최단 정의

```text
Relation.main.md
=
SeungeFlow에서 relation을 merge가 아니라 boundary-preserving bridge로 읽게 하는 문서이다.

이 문서는 존재의 관계 정의와 장(Field)의 구조원리를 relation 관점에서 정리하며,
path, shape, symbol, candidate, reference_only, forbidden을 오독하지 않도록 guard를 제공한다.
```