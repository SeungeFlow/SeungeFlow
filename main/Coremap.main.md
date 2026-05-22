---
id: main.coremap
type: main_coremap_document
filename: Coremap.main.md
directory: /main/
status: active_draft
authority:
  - Human.Lee Seung
  - ChatGPT.direct
purpose:
  - define_coremap_reading_rule
  - map_core_relation_without_merge
  - preserve_core_boundary
  - distinguish_coremap_from_relation_guide
  - connect_schema_meta_to_relation_field
---

# Coremap.main.md

## 0. 역할

`Coremap.main.md`는 `Structure_Principle/schema/` 내부 core들이 서로 어떻게 연결될 수 있는지 안내하는 core relation map 문서이다.

이 문서는 단순 파일목록이 아니라,  
각 core boundary를 보존한 채 core 사이의 relation을 표시하기 위한 map 문서이다.

```text
Coremap.main.md
=
core relation map
+
boundary-preserving relation guide
+
schema connection map
+
relation state map
```

---

## 1. Coremap의 기본 정의

Coremap은 core들을 하나로 병합하는 map이 아니라,  
각 core의 boundary를 보존한 채 core와 core 사이의 relation을 표시하는 map이다.

```text
Coremap
=
boundary-preserving core relation map
```

Coremap은 다음을 보여준다.

```text
어떤 core가 있는가
어떤 core가 어떤 core와 relation을 가지는가
그 relation은 어떤 상태인가
그 relation은 merge가 아닌가
어떤 relation은 forbidden guard로 보존되어야 하는가
```

---

## 2. Coremap이 아닌 것

Coremap은 파일목록으로 읽는 것이 아니라,  
core boundary를 보존하는 relation map으로 읽는다.

```text
Coremap
≠
file list

Coremap
=
core relation map
```

Coremap은 개념사전으로 읽는 것이 아니라,  
각 core가 어떤 relation field 안에 놓이는지 보여주는 map으로 읽는다.

```text
Coremap
≠
concept dictionary

Coremap
=
relation field map
```

Coremap은 요약표로 읽는 것이 아니라,  
core 사이의 boundary-preserving relation을 보존하는 문서로 읽는다.

```text
Coremap
≠
summary table

Coremap
=
boundary-preserving relation map
```

Coremap은 merge map으로 읽는 것이 아니라,  
merge를 막고 relation을 보존하는 guard map으로 읽는다.

```text
Coremap
≠
merge map

Coremap
=
relation guard map
```

---

## 3. Coremap과 Core.main.md

`Core.main.md`는 각 core가 무엇을 설명하는지 안내하는 문서이다.

`Coremap.main.md`는 그 core들이 어떻게 연결될 수 있는지 안내하는 문서이다.

```text
Core.main.md
=
what each core explains

Coremap.main.md
=
how cores relate
```

즉 `Core.main.md`가 node guide라면,  
`Coremap.main.md`는 edge map이다.

```text
Core.main.md
=
node guide

Coremap.main.md
=
edge map
```

AI는 이 둘을 병합하는 것이 아니라,  
core 설명과 core relation을 구분해서 읽어야 한다.

---

## 4. Coremap과 Relation.main.md

`Relation.main.md`는 relation을 어떤 원칙으로 읽어야 하는지 설명하는 문서이다.

`Coremap.main.md`는 그 원칙을 바탕으로 core 사이의 relation을 표시하는 map 문서이다.

```text
Relation.main.md
=
relation reading rule

Coremap.main.md
=
core relation map
```

즉 Relation.main.md는 relation의 원리이고,  
Coremap.main.md는 core 사이 relation의 지도이다.

---

## 5. Coremap과 schema

Coremap은 `Structure_Principle/schema/` 내부의 `meta.md`들을 중심으로 읽는다.

```text
Structure_Principle/schema/
=
formed place-concept field

meta.md
=
Active_Schema source boundary
```

Coremap은 schema directory name을 identity로 삼는 것이 아니라,  
각 `meta.md`가 형성한 core boundary를 기준으로 relation을 표시한다.

```text
schema directory
=
path-coordinate container

meta.md
=
core boundary source
```

---

## 6. core node 읽기

Coremap에서 core node는 파일 경로 자체가 아니라,  
`meta.md`가 형성한 자리개념 boundary를 가리킨다.

core node는 다음 요소를 가질 수 있다.

```text
schema_id
order_hint
current_path
meta_path
status
boundary_summary
relation_state
```

각 항목은 다음처럼 읽는다.

```text
schema_id
=
작업상 core 이름

order_hint
=
탐색과 순서를 돕는 숫자

current_path
=
현재 path-coordinate

meta_path
=
core boundary가 놓인 meta.md 위치

status
=
active / candidate / reference_only / pending 등 상태

boundary_summary
=
해당 core가 보존해야 할 최소 boundary

relation_state
=
다른 core와의 relation 상태
```

---

## 7. order_hint 기준

Coremap에서 숫자는 identity가 아니라 order_hint이다.

```text
number
=
order_hint
```

예를 들어:

```text
000_dot
```

은 dot의 identity가 아니라,  
dot 자리개념이 현재 schema 안에서 놓인 order_hint와 local label이다.

```text
000_dot
=
order_hint + local_label + current_coordinate
```

AI는 숫자 순서를 존재 순서나 우열 순서로 읽는 것이 아니라,  
탐색을 돕는 order_hint로 읽어야 한다.

---

## 8. relation edge 읽기

Coremap에서 edge는 core와 core 사이의 relation을 표시한다.

edge는 다음 요소를 가질 수 있다.

```text
from
to
relation_type
relation_state
meaning
guard
source
```

각 항목은 다음처럼 읽는다.

```text
from
=
relation 출발 core

to
=
relation 도착 core

relation_type
=
transition / refinement / boundary_guard / correspondence 등

relation_state
=
candidate / confirmed / pending / forbidden 등

meaning
=
relation이 의미하는 구조

guard
=
merge나 오독을 막는 조건

source
=
relation 판단의 근거 문서
```

---

## 9. relation_state

Coremap의 relation은 상태를 가진다.

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

AI는 relation을 발견했다고 해서 바로 confirmed로 읽는 것이 아니라,  
relation_state를 보존한 채 읽어야 한다.

---

## 10. forbidden edge

Coremap에서 forbidden edge는 실패한 관계가 아니라,  
오독을 막기 위해 보존되는 guard relation이다.

```text
forbidden
=
guard
not failure
```

예를 들어 CoreDot이 dot을 대체한다는 읽기는 forbidden edge로 잠가야 한다.

```text
CoreDot
≠
dot의 본명
```

이 경우 forbidden은 relation이 없다는 뜻이 아니라,  
잘못된 방향의 relation을 막는 boundary guard이다.

---

## 11. dot preservation

`000_dot`은 dot의 최종 identity가 아니라,  
dot 자리개념 문서가 현재 놓인 origin coordinate이다.

`dot.meta.md`는 field 안에서 최초로 드러나는 최소 place-state를 설명한다.

```text
dot
=
field 안에서 최초로 드러나는 최소 place-state
```

Coremap은 dot을 후속 core와 연결할 수 있지만,  
후속 core가 dot을 대체하는 식으로 읽으면 안 된다.

```text
refinement
≠
replacement
```

---

## 12. CoreDot ambiguity boundary

`121_coredot_ambiguity_boundary`는 CoreDot이 dot을 대체하지 않도록 막는 boundary로 읽는다.

```text
121_coredot_ambiguity_boundary
=
CoreDot ambiguity guard
```

AI는 `CoreDot`을 dot의 본명으로 읽는 것이 아니라,  
dot과 CoreDot의 ambiguity를 보존하기 위한 boundary로 읽어야 한다.

```text
CoreDot
≠
dot identity
```

---

## 13. 100_empty_position

`100_empty_position`은 결손 번호가 아니라,  
formed-to-rebuilt 사이의 reserved gate로 읽는다.

```text
100_empty_position
=
reserved empty gate
```

AI는 100을 비어 있으므로 채워야 할 결손으로 읽는 것이 아니라,  
비어 있음이 보존된 자리로 읽어야 한다.

```text
empty position
=
preserved slot
```

---

## 14. thinking_flow와 Coremap

`thinking_flow_relation_*.md` 문서는 thinking_flow가 기존 schema, meta.md, Coremap, relation 후보와 어떻게 연결되는지 표시한다.

```text
thinking_flow_relation
=
candidate relation map
```

Coremap은 thinking_flow_relation을 확정 relation으로 바로 흡수하는 것이 아니라,  
candidate / pending / reference_only / confirmed 상태를 구분해서 반영해야 한다.

```text
relation found
≠
relation confirmed
```

---

## 15. Coremap과 meta.md 후보

thinking_flow에서 새로운 Seed 후보가 발견되면,  
먼저 기존 Coremap과 schema에 중복되는지 확인한다.

```text
thinking_flow Seed candidate
→
existing schema check
→
existing coremap relation check
→
duplicate or new boundary judgment
→
meta.md candidate decision
```

기존 schema와 Coremap 안에 이미 같은 자리개념이 있다면,  
새 meta.md를 만들기보다 relation을 연결한다.

```text
이미 schema에 있음
→
새 meta.md 생성보다 relation 연결 우선
```

---

## 16. Coremap과 CFD

CFD는 Coremap의 schema core identity가 아니라,  
현시점 `epluone`의 `[body]` slot에 놓인 target value이다.

```text
epluone
=
[body] slot directory

CFD
=
current target value in [body] slot
```

CFD와 Structure_Principle 사이에는 application relation이 있을 수 있지만,  
CFD를 schema core로 직접 병합하면 안 된다.

```text
CFD
≠
schema core identity

CFD
=
current application target value
```

---

## 17. Coremap과 path

Coremap은 path를 relation identity로 읽는 것이 아니라,  
현재 문서가 놓인 visible coordinate로 읽는다.

```text
path
=
visible coordinate

path
≠
relation identity
```

같은 디렉토리에 있다는 사실은 relation 후보가 될 수 있지만,  
그 자체로 confirmed relation은 아니다.

```text
same directory
≠
confirmed relation
```

---

## 18. Coremap 작성 시 금지되는 방식

AI는 Coremap을 작성하거나 읽을 때 다음을 하면 안 된다.

```text
Coremap을 file list로 만들기
Coremap을 concept dictionary로 만들기
Coremap을 summary table로 만들기
Coremap을 merge map으로 만들기
number를 identity로 사용하기
directory path를 relation identity로 사용하기
candidate relation을 confirmed로 승격하기
forbidden relation을 삭제하기
CoreDot을 dot의 본명으로 읽기
100_empty_position을 결손으로 채우기
CFD를 schema core로 병합하기
```

이 금지 목록은 Coremap을 막기 위한 것이 아니라,  
Coremap을 boundary-preserving relation map으로 유지하기 위한 guard이다.

---

## 19. Coremap entry 예시

예시:

```text
edge:
  from: dot
  to: coredot_ambiguity_boundary
  relation_type: boundary_guard
  relation_state: confirmed_link
  meaning: CoreDot이 dot을 대체하지 못하도록 ambiguity boundary를 보존한다.
  guard: CoreDot ≠ dot identity
```

이 edge는 dot과 CoreDot을 병합하는 relation이 아니라,  
dot의 boundary를 보존하기 위한 guard relation이다.

---

## 20. Coremap과 main guide

`Coremap.main.md`는 main guide layer에 놓인 문서이다.

따라서 Coremap.main.md는 primary source 자체가 아니라,  
primary source의 relation을 읽기 위한 guide map이다.

```text
primary source:
Structure_Principle/schema/
SeungeFlow_Thinking/thinking_flow/

guide map:
main/Coremap.main.md
```

AI는 Coremap.main.md를 schema보다 우선하는 identity로 읽는 것이 아니라,  
schema와 thinking_flow relation을 읽기 위한 guide map으로 읽어야 한다.

---

## 21. Reading Guard

AI는 Coremap을 읽을 때 다음을 지켜야 한다.

```text
Coremap은 file list가 아니라 boundary-preserving relation map이다.
Coremap은 concept dictionary가 아니라 core relation map이다.
Coremap은 summary table이 아니라 relation state map이다.
Coremap은 merge map이 아니라 relation guard map이다.
number는 identity가 아니라 order_hint이다.
path는 relation identity가 아니라 visible coordinate이다.
forbidden은 failure가 아니라 guard이다.
candidate는 confirmed가 아니다.
```

---

## 22. 최단 정의

```text
Coremap.main.md
=
Structure_Principle/schema/ 내부 core들의 relation을 boundary-preserving 방식으로 표시하는 main guide map이다.

Coremap은 file list, concept dictionary, summary table, merge map이 아니라,
각 core boundary를 보존한 채 relation state를 표시하는 core relation map이다.
```