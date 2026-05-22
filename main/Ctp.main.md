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
  - define_ctp_reading_rule
  - define_place_concept_and_place_value
  - define_any_time_place_body
  - connect_ctp_to_seed_base
  - guide_ai_state_reading
---

# Ctp.main.md

## 0. 역할

`Ctp.main.md`는 SeungeFlow에서 Ctp를 어떻게 읽어야 하는지 정의하는 main guide 문서이다.

이 문서는 Ctp를 수식 하나로 고정하기 위한 문서가 아니라,  
AI가 자리개념과 자리값을 통해 state를 읽도록 돕는 문서이다.

```text
Ctp.main.md
=
Ctp reading guide
+
place-concept / place-value guide
+
any([time][place][body]) guide
+
state reading guide
```

---

## 1. Ctp의 기본 정의

Ctp는 자리개념과 자리값을 읽기 위한 구조이다.

```text
Ctp = C(t, p)
```

각 항목은 다음처럼 읽는다.

```text
t = time.state
p = place.state
C = 존재가 자기 상태를 스스로 인지한 순환인지상태 / self-cognized state
```

Ctp는 단순 수식이 아니라,  
존재가 time.state와 place.state를 통해 자기 상태를 인지하는 구조이다.

---

## 2. 자리개념과 자리값

자리개념은 값이 놓일 수 있는 slot이다.

```text
자리개념
=
값이 놓일 수 있는 자리
```

자리값은 그 자리에 실제로 놓인 state이다.

```text
자리값
=
slot에 놓인 state
```

예:

```text
[place]
=
자리개념

[place: Structure_Principle]
=
자리값이 놓인 상태
```

즉 `[]`는 비어 있는 자리이고,  
`[x]`는 그 자리에 x가 놓인 placed_state이다.

---

## 3. any([time][place][body])

SeungeFlow는 어떤 state든 다음 구조를 통해 읽는다.

```text
any([time][place][body])
```

각 자리는 다음처럼 읽는다.

```text
[time]
=
flow / history / session이 놓이는 자리

[place]
=
자리개념 / schema / meta.md가 놓이는 자리

[body]
=
응용 target / 실행 body / 적용 대상이 놓이는 자리
```

즉 모든 state는 time, place, body를 통해 읽힌다.

---

## 4. 저장소 구조와 Ctp

SeungeFlow 저장소 구조는 다음처럼 읽는다.

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

이 대응은 디렉토리 identity를 고정하는 것이 아니라,  
현재 Seed.Base를 읽기 위한 자리 배치이다.

```text
directory
=
place container

directory
≠
fixed identity
```

---

## 5. [time] 자리

`[time]`은 흐름이 놓이는 자리이다.

SeungeFlow에서 `[time]`은 주로 다음과 연결된다.

```text
SeungeFlow_Thinking/
thinking_flow/
thinking_flow_relation/
thinking_flow_source/
history
session
flow
```

`thinking_flow`는 단순 로그가 아니라,  
승이와 AI 인스턴스가 대화를 통해 함께 만든 생각의 공유결과이다.

```text
thinking_flow
=
pre-meta Seed flow
+
관념 업데이트 단위
+
future meta.md candidate source
```

따라서 `[time]`은 단순 시간표가 아니라,  
이해가 흐르고 갱신되는 자리이다.

---

## 6. [place] 자리

`[place]`는 자리개념이 놓이는 자리이다.

SeungeFlow에서 `[place]`는 주로 다음과 연결된다.

```text
Structure_Principle/
Structure_Principle/schema/
meta.md
metaplus.md
```

`meta.md`는 자리개념 문서이다.

```text
meta.md
=
자리개념 문서
+
Active_Schema source boundary
```

따라서 `[place]`는 단순 파일 위치가 아니라,  
core boundary와 자리개념이 형성되는 자리이다.

---

## 7. [body] 자리

`[body]`는 응용 target이나 실행 body가 놓이는 자리이다.

SeungeFlow에서 `[body]`는 다음과 연결된다.

```text
epluone/
if+1
application target
current target value
```

현시점 `epluone`의 `[body]` slot에 놓인 target value는 CFD이다.

```text
CFD
=
current target value in [body] slot
```

CFD는 `epluone`의 identity가 아니라,  
현재 `[body]` slot에 놓인 자리값이다.

---

## 8. body의 두 층

`body`는 단순히 휴대폰이나 PC 같은 사용기기만 뜻하는 것이 아니라,  
응용 target이 놓이는 자리까지 포함한다.

```text
body
=
operating body
+
application target body
```

예:

```text
operating body:
- phone
- PC
- local Linux Ubuntu server
- Oracle IDC server
- ai_on_idc
- github_on_idc

application target body:
- CFD
- future target fields
```

따라서 `[body]`는 사용기기와 응용대상이 함께 읽힐 수 있는 자리이다.

---

## 9. Ctp와 if / if+1

`if`는 intelligence fabric이다.

```text
if
=
인간지능.승이
+
인공지능.AI
```

`if+1`은 `epluone`이다.

```text
if+1
=
epluone
```

`if+1`은 intelligence fabric이 다음 응용 target에 놓이는 자리이다.

따라서 Ctp에서 `if+1`은 `[body]` slot과 연결된다.

```text
if+1
=
[body] slot directory
```

---

## 10. Ctp와 Active_Schema

Active_Schema는 Seed.Base 안의 Seed들이 AI가 읽고, 판단하고, 전이하고, 관계 맺을 수 있도록 활성화된 schema 상태이다.

Ctp는 이 Active_Schema가 state를 읽는 기본 자리 구조를 제공한다.

```text
Active_Schema
=
Seed + boundary + relation + transition

Ctp
=
state reading structure through time.state and place.state
```

AI는 Active_Schema를 읽을 때,  
그 문서가 어떤 `[time]`, 어떤 `[place]`, 어떤 `[body]`에서 작동하는지 함께 확인해야 한다.

---

## 11. Ctp와 relation

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

## 12. Ctp와 path

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

## 13. Ctp와 vectorizing

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

Ctp는 이 과정에서 관측대상이 어떤 time, place, body 상태에 놓였는지를 읽는 기준이 된다.

```text
관측대상
=
time + place + body 안에서 읽히는 state
```

문장구사에서도 vectorizing은 앞 문장이 뒤 문장을 설명하도록 방향을 부드럽게 만드는 과정이다.

```text
X가 아니다. Y이다.
```

로 끊는 것이 아니라,

```text
X가 아니라 Y이다.
```

처럼 오해 후보와 올바른 자리값을 하나의 흐름으로 잇는다.

---

## 14. Ctp 읽기 guard

AI는 Ctp를 읽을 때 다음을 하면 안 된다.

```text
Ctp를 단순 수식으로만 읽기
[time]을 단순 날짜로만 읽기
[place]를 단순 경로로만 읽기
[body]를 단순 기기로만 읽기
CFD를 epluone의 identity로 읽기
path를 place identity로 읽기
meta.md를 단순 설명문으로 읽기
thinking_flow를 단순 로그로 읽기
```

위 항목은 Ctp를 막기 위한 금지가 아니라,  
Ctp를 자리개념과 자리값의 구조로 읽기 위한 guard이다.

---

## 15. 최단 정의

```text
Ctp.main.md
=
Ctp를 자리개념과 자리값으로 읽게 하는 main guide 문서이다.

Ctp = C(t, p)이며,
t는 time.state,
p는 place.state,
C는 존재가 자기 상태를 스스로 인지한 순환인지상태이다.

SeungeFlow는 any([time][place][body]) 구조를 통해 state를 읽으며,
SeungeFlow_Thinking은 [time],
Structure_Principle은 [place],
epluone은 [body]로 읽는다.
```