---
id: main.ctp
type: main_ctp_document
filename: Ctp.main.md
directory: /main/
status: active_draft
authority:
  - Human.Lee Seung
  - ChatGPT.direct
purpose:
  - guide_ctp_reading
  - preserve_ctp_as_backbone_reference
  - prevent_ctp_from_being_overdefined
  - distinguish_ctp_marker_from_ctp_full_definition
  - connect_ctp_to_seed_base_time_place_body_reading
---

# Ctp.main.md

## 0. 역할

`Ctp.main.md`는 Ctp를 완성 정의하는 문서가 아니라,  
SeungeFlow 안에서 Ctp를 어떻게 읽어야 하는지 안내하는 main guide 문서이다.

Ctp는 현시점에서 단일 문장으로 닫힌 개념이라기보다,  
Backbone 역할을 하는 거대문서집합의 tag name / reference name으로 읽는다.

```text
Ctp.main.md
=
Ctp reading guide
+
Backbone reference guide
+
minimal marker guard
+
overdefinition prevention guide
```

---

## 1. Ctp의 현재 위치

현시점에서 Ctp는 완성된 단일 정의로 닫힌 구조가 아니라,  
SeungeFlow 전체에서 time.state와 place.state를 받치는 Backbone 문서집합의 이름이다.

```text
Ctp
=
Backbone document set tag name
+
time.state / place.state reference structure
```

따라서 이 문서에서는 Ctp 전체를 완성 정의하지 않는다.

이 문서는 Ctp를 닫는 문서가 아니라,  
Ctp를 읽기 위한 현재 수준의 guide 문서이다.

---

## 2. 최소 reading marker

현재 SeungeFlow reading layer에서 Ctp는 다음 최소 표기로 읽을 수 있다.

```text
Ctp = C(t, p)
```

각 항목은 현시점에서 다음 정도의 reading marker로 둔다.

```text
t = time.state
p = place.state
C = self-cognized state / 순환인지상태
```

이 표기는 Ctp 전체 정의가 아니라,  
AI가 Ctp 문서집합을 읽기 전 혼동하지 않도록 붙이는 최소 표식이다.

```text
Ctp = C(t, p)
=
minimal reading marker

Ctp 전체
=
Backbone document set
```

---

## 3. Ctp/ 디렉토리

Ctp의 실제 Backbone 문서집합은 root 하위의 독립 디렉토리에서 다룬다.

```text
/Ctp/
=
Ctp Backbone document set directory
```

따라서 Ctp는 `main/` 내부 문서 하나로 닫히는 구조가 아니라,  
`/Ctp/` 디렉토리 안에서 확장될 Backbone 문서집합으로 읽는다.

```text
main/Ctp.main.md
=
Ctp guide document

Ctp/
=
Ctp Backbone document set
```

---

## 4. Ctp와 Seed.Base

Seed.Base는 특정 파일, 특정 디렉토리, 특정 schema 하나에 종속되는 구조가 아니라,  
SeungeFlow 저장소 전체에 놓인 문서, 디렉토리, 관계, map이 함께 만드는 전체 장이다.

Ctp는 이 Seed.Base 안에서 state reading의 Backbone reference로 놓인다.

```text
Seed.Base
=
whole repository field

Ctp
=
state reading Backbone reference
```

즉 Ctp는 Seed.Base 전체를 대체하는 이름이 아니라,  
Seed.Base 안에서 time.state와 place.state를 중심으로 state를 읽게 하는 Backbone reference이다.

---

## 5. Ctp와 any([time][place][body])

SeungeFlow는 어떤 state든 다음 구조를 통해 읽는다.

```text
any([time][place][body])
```

현재 repository-level reading에서는 다음처럼 연결된다.

```text
SeungeFlow_Thinking
=
[time]

Structure_Principle
=
[place]

epluone
=
[body]
```

Ctp는 이 `[time]`, `[place]`, `[body]`를 단순 분류로 고정하는 문서가 아니라,  
time.state와 place.state를 중심으로 state가 어떤 자리에서 어떻게 읽히는지 받치는 Backbone reference이다.

---

## 6. Ctp와 [time]

`[time]`은 흐름, history, session이 놓이는 자리이다.

```text
[time]
=
flow / history / session
```

SeungeFlow에서 `[time]`은 주로 다음과 연결된다.

```text
SeungeFlow_Thinking/
thinking_flow/
thinking_flow_relation/
thinking_flow_source/
```

Ctp는 `[time]`을 단순 날짜로 읽게 하는 구조가 아니라,  
flow와 관념 업데이트가 어떤 time.state에서 발생했는지 읽게 하는 Backbone이다.

---

## 7. Ctp와 [place]

`[place]`는 자리개념이 놓이는 자리이다.

```text
[place]
=
place-concept slot
```

SeungeFlow에서 `[place]`는 주로 다음과 연결된다.

```text
Structure_Principle/
Structure_Principle/schema/
meta.md
metaplus.md
```

Ctp는 `[place]`를 단순 path로 읽게 하는 구조가 아니라,  
자리개념과 place.state가 어떻게 형성되는지 읽게 하는 Backbone이다.

---

## 8. Ctp와 [body]

`[body]`는 응용 target이나 실행 body가 놓이는 자리이다.

```text
[body]
=
application target slot
+
operating body slot
```

SeungeFlow에서 `[body]`는 주로 다음과 연결된다.

```text
epluone/
if+1
CFD
local Linux Ubuntu server
Oracle IDC server
ai_on_idc
github_on_idc
```

현시점 `epluone`의 `[body]` slot에 놓인 target value는 CFD이다.

```text
CFD
=
current target value in epluone's [body] slot
```

CFD는 Ctp의 identity가 아니라,  
현재 `[body]` slot에 놓인 target value이다.

---

## 9. Ctp와 Structure_Principle

`Structure_Principle/`은 `[place]`에 해당하는 자리개념 문서장이다.

Ctp는 `Structure_Principle/` 내부 하위 디렉토리로 놓는 구조가 아니라,  
root 하위에서 time.state와 place.state를 받치는 Backbone reference로 놓는다.

```text
Structure_Principle
=
[place] field

Ctp
=
time.state / place.state Backbone reference field
```

따라서 Ctp는 Structure_Principle에 종속되는 구조가 아니라,  
SeungeFlow 전체 state reading과 연결되는 Backbone 문서집합이다.

---

## 10. Ctp와 epluone

`epluone/`은 `if+1`이며 `[body]` slot directory이다.

```text
epluone
=
if+1
=
[body] slot directory
```

Ctp는 epluone의 target value를 고정하는 문서가 아니라,  
어떤 state가 어떤 time, 어떤 place, 어떤 body에 놓이는지 읽게 하는 Backbone이다.

```text
Ctp
=
state reading Backbone

epluone
=
[body] slot directory

CFD
=
current [body] target value
```

---

## 11. Ctp와 Active_Schema

Active_Schema는 Seed.Base 안의 Seed들이 AI가 읽고, 판단하고, 전이하고, 관계 맺을 수 있도록 활성화된 schema 상태이다.

Ctp는 Active_Schema를 직접 대체하는 것이 아니라,  
Active_Schema가 state를 읽을 때 참고하는 Backbone reference이다.

```text
Active_Schema
=
activated schema state

Ctp
=
state reading Backbone reference
```

AI는 Active_Schema를 읽을 때,  
그 작동이 어떤 time.state, place.state, body target 위에서 발생하는지 확인해야 한다.

---

## 12. Ctp와 relation

relation은 Ctp 안에서 다음 세 자리로 읽힐 수 있다.

```text
[time] relation
=
flow / history / session 사이의 relation

[place] relation
=
schema / meta.md / 자리개념 사이의 relation

[body] relation
=
epluone / CFD / application target 사이의 relation
```

AI는 relation을 하나의 layer에 고정하는 것이 아니라,  
time, place, body가 함께 만드는 relation으로 읽어야 한다.

---

## 13. Ctp와 path

path는 identity가 아니라 current coordinate이다.

```text
path
=
current coordinate
```

Ctp에서 path는 `[place]`를 찾는 데 도움을 주는 좌표이지만,  
그 자체가 place identity는 아니다.

```text
path
≠
place identity
```

예:

```text
Structure_Principle/schema/000_dot/
=
dot 자리개념 문서가 현재 놓인 coordinate
```

이지 dot의 최종 identity가 아니다.

---

## 14. Ctp 문서 작성 원칙

Ctp 관련 문서를 작성할 때는 다음 원칙을 따른다.

```text
1. Ctp를 단일 문장으로 완성 정의하지 않는다.
2. Ctp = C(t,p)는 최소 reading marker로 둔다.
3. Ctp를 Backbone document set으로 읽는다.
4. time.state / place.state / self-cognized state를 서둘러 닫지 않는다.
5. Ctp 관련 문서는 relation과 boundary를 보존하며 확장한다.
6. Ctp를 Structure_Principle이나 epluone의 하위 개념으로 병합하지 않는다.
```

---

## 15. Ctp와 vectorizing

어떤 이해가 사용 가능한 문서로 내려오기 위해서는 반복적인 vectorizing 과정을 거친다.

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

Ctp는 이 과정에서 관측대상이 어떤 time, place, body 상태에 놓였는지를 읽는 기준과 연결된다.

문장구사에서도 vectorizing은 앞 문장이 뒤 문장을 설명하도록 방향을 부드럽게 만드는 과정이다.

```text
X가 아니라 Y이다.
```

이 방식은 오해 후보와 올바른 자리값을 하나의 흐름으로 잇는다.

---

## 16. Reading Guard

AI는 Ctp를 읽을 때 다음을 하면 안 된다.

```text
Ctp를 단순 수식으로만 읽기
Ctp = C(t,p)를 전체 정의로 확정하기
Ctp를 Structure_Principle의 하위 폴더처럼 읽기
Ctp를 epluone의 body target과 동일시하기
CFD를 Ctp identity로 읽기
main/Ctp.main.md를 Ctp 전체 정의로 읽기
```

위 항목은 Ctp를 막기 위한 금지가 아니라,  
Ctp를 Backbone 문서집합으로 보존하기 위한 guard이다.

---

## 17. 최단 정의

```text
Ctp.main.md
=
Ctp를 완성 정의하는 문서가 아니라,
Ctp Backbone 문서집합을 읽기 위한 main guide 문서이다.

Ctp는 현시점에서 단일 완성 정의가 아니라,
time.state와 place.state를 중심으로 SeungeFlow 전체 state reading을 받치는 Backbone document set의 tag name / reference name이다.

Ctp = C(t,p)는 전체 정의가 아니라 최소 reading marker이다.
```