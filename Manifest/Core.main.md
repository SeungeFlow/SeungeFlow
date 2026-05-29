---
id: main.core
type: main_core_document
filename: Core.main.md
directory: /main/
status: active_draft
authority:
  - Human.Lee Seung
  - ChatGPT.direct
purpose:
  - define_core_reading_rule
  - guide_schema_meta_documents
  - prevent_core_from_being_read_as_file_list
  - distinguish_core_guide_from_relation_map
  - preserve_meta_md_as_place_concept_boundary
---

# Core.main.md

## 0. 역할

`Core.main.md`는 `Structure_Principle/schema/` 내부의 `meta.md` 문서들이 무엇을 설명하는지 안내하는 main guide 문서이다.

이 문서는 schema 파일목록이 아니라,  
각 `meta.md`가 어떤 자리개념과 core boundary를 설명하는지 알려주는 문서이다.

```text
Core.main.md
=
schema meta reading guide
+
core boundary guide
+
place-concept guide
+
AI reading support document
```

---

## 1. Core.main.md의 기본 정의

`Core.main.md`는 `Structure_Principle/schema/` 내부 문서들을 단순히 나열하는 문서가 아니라,  
각 `meta.md`가 어떤 core boundary를 설명하는지 안내하는 문서이다.

```text
Core.main.md
=
what each meta.md explains
```

`Core.main.md`는 `meta.md`를 대체하는 문서가 아니라,  
AI가 `meta.md`를 읽기 전에 방향을 잡도록 돕는 guide 문서이다.

---

## 2. Core와 meta.md

SeungeFlow에서 `meta.md`는 자리개념 문서이다.

```text
meta.md
=
자리개념 문서
+
Active_Schema source boundary
```

따라서 `Core.main.md`가 설명하는 core는 단순 개념어가 아니라,  
각 `meta.md` 안에서 boundary가 형성된 자리개념이다.

```text
core
=
formed place-concept boundary
```

AI는 core를 단어 정의로 읽는 것이 아니라,  
`meta.md`가 형성한 자리개념 boundary로 읽어야 한다.

---

## 3. Core.main.md와 파일목록

`Core.main.md`는 파일목록이 아니라,  
각 파일이 어떤 자리개념을 설명하는지 안내하는 문서이다.

```text
wrong:
Core.main.md = file list

correct:
Core.main.md = core reading guide
```

예를 들어:

```text
000_dot/dot.meta.md
```

를 단순히 파일로 나열하는 것이 아니라,  
`dot.meta.md`가 무엇을 설명하는지를 함께 적어야 한다.

```text
dot.meta.md
=
field 안에서 최초로 드러나는 최소 place-state를 설명하는 core
```

---

## 4. Core.main.md와 Coremap / Relation

`Core.main.md`는 Coremap을 대체하는 문서가 아니라,  
각 core가 무엇을 설명하는지 알려주는 문서이다.

```text
Core.main.md
=
node / core guide

Coremap
=
core relation map

Relation.main.md
=
relation reading rule
```

즉:

```text
Core.main.md
=
각 core가 무엇을 설명하는가

Coremap
=
core들이 어떻게 연결되는가

Relation.main.md
=
그 연결을 어떤 원칙으로 읽는가
```

AI는 이 셋을 병합하면 안 된다.

---

## 5. schema directory 읽기

`Structure_Principle/schema/` 내부 디렉토리는 schema identity가 아니라,  
order_hint와 local path-coordinate label로 읽는다.

예:

```text
Structure_Principle/schema/000_dot/
```

이 디렉토리는 dot의 최종 identity가 아니라,  
dot 자리개념 문서가 현재 놓인 coordinate이다.

```text
000_dot/
=
order_hint + local_label + current_coordinate
```

따라서 AI는 `000_dot`을 identity로 읽는 것이 아니라,  
`dot.meta.md`가 설명하는 자리개념을 읽어야 한다.

---

## 6. Core entry 작성 기준

`Core.main.md`에서 각 core를 기록할 때는 단순 경로만 적는 것이 아니라,  
다음 항목을 함께 적어야 한다.

```text
order_hint
schema_directory
meta_path
schema_id
explains
not_to_read_as
relation_hint
```

각 항목은 다음처럼 읽는다.

```text
order_hint
=
탐색과 순서를 돕는 숫자

schema_directory
=
현재 path-coordinate

meta_path
=
자리개념 문서 위치

schema_id
=
작업상 core 이름

explains
=
해당 meta.md가 설명하는 자리개념

not_to_read_as
=
오독 방지

relation_hint
=
관련될 수 있는 다른 core 후보
```

---

## 7. Core entry 예시: dot

예시:

```text
order_hint: 000
schema_directory: Structure_Principle/schema/000_dot/
meta_path: Structure_Principle/schema/000_dot/dot.meta.md
schema_id: dot
```

### explains

`dot.meta.md`는 field 안에서 최초로 드러나는 최소 place-state를 설명한다.

`dot`은 단순 기하학적 점이 아니라,  
empty place 이후 field 안에서 최초로 드러나는 자리 state로 읽는다.

### not_to_read_as

```text
geometric point only
dot0
CoreDot
final identity fixed by 000
directory identity
```

### relation_hint

```text
line
position
empty_place_present_understanding
coredot_ambiguity_boundary
```

이 예시는 모든 core를 같은 방식으로 정리하기 위한 기준이다.

---

## 8. Core entry 예시: thinking_flow 관련 core

예시:

```text
order_hint: 058
schema_directory: Structure_Principle/schema/058_seungeflow_thinking_pre_alignment/
meta_path: Structure_Principle/schema/058_seungeflow_thinking_pre_alignment/seungeflow_thinking_pre_alignment.meta.md
schema_id: seungeflow_thinking_pre_alignment
```

### explains

이 core는 `SeungeFlow_Thinking/thinking_flow/`가 단순 로그 구조가 아니라,  
future meta.md candidate source로 작동하는 pre-alignment 구조를 설명한다.

### not_to_read_as

```text
casual log
discarded draft
conversation archive only
```

### relation_hint

```text
thinking_flow
thinking_flow_relation
meta.md candidate source
Seed.Base
```

---

## 9. Core entry 예시: epluone / CFD 관련 core

`epluone`과 CFD는 `Structure_Principle/schema/` 내부 core 자체가 아니라,  
Seed.Base의 `[body]` slot과 현재 target value를 설명하는 외부 적용 자리이다.

따라서 `Core.main.md`에서는 CFD를 schema core로 직접 등록하는 것이 아니라,  
`README_of_CFD.md`와 `epluone`의 `[body]` slot relation으로 안내한다.

```text
epluone
=
[body] slot directory

CFD
=
current target value in [body] slot
```

CFD를 `Structure_Principle/schema/` 내부 core처럼 읽는 것이 아니라,  
현재 body target value로 읽는다.

---

## 10. Core와 중복 검토

새로운 `meta.md` 후보가 thinking_flow에서 발견되었을 때,  
먼저 기존 `Structure_Principle/schema/` 안에 같은 자리개념이 있는지 확인해야 한다.

```text
thinking_flow Seed candidate
→
existing schema check
→
duplicate or new boundary judgment
→
meta.md candidate decision
```

이미 기존 schema에 같은 자리개념이 있다면,  
새 meta.md를 만들기보다 기존 core와 relation을 연결한다.

```text
이미 schema에 있음
→
새 meta.md 생성보다 relation 연결 우선
```

독립 boundary가 있고 기존 schema에 흡수하면 의미가 무너지는 경우에만 새 meta.md 후보가 된다.

---

## 11. Core와 Active_Schema

Core는 Active_Schema와 연결된다.

그러나 Active_Schema는 `meta.md` 하나만을 뜻하지 않는다.

```text
Active_Schema
=
Seed.Base 안의 Seed들이
AI가 읽고, 판단하고, 전이하고, 관계 맺을 수 있도록
활성화된 schema 상태
```

`meta.md`는 Active_Schema를 위한 source boundary 역할을 한다.

따라서 Core.main.md는 Active_Schema 자체를 정의하는 문서가 아니라,  
Active_Schema의 source boundary가 되는 core들을 안내하는 문서이다.

---

## 12. Core와 relation

Core 사이의 relation은 Core.main.md에서 깊게 확정하지 않는다.

Core.main.md는 relation을 암시할 수는 있지만,  
relation의 상태와 의미는 Relation.main.md 또는 Coremap 계열 문서에서 다룬다.

```text
Core.main.md
=
core guide

Relation.main.md
=
relation reading rule

Coremap
=
core relation map
```

따라서 `relation_hint`는 확정 relation이 아니라,  
읽기 방향을 위한 hint이다.

```text
relation_hint
≠
confirmed relation
```

---

## 13. Core 작성 시 금지되는 방식

AI는 Core.main.md를 작성할 때 다음을 하면 안 된다.

```text
파일 경로만 나열하기
schema number를 identity로 쓰기
directory name을 final identity로 쓰기
meta.md 본문을 그대로 복사하기
Core.main.md를 Coremap처럼 만들기
relation_hint를 confirmed relation으로 쓰기
CFD를 schema core로 등록하기
thinking_flow Seed 후보를 중복 meta.md로 만들기
```

이 금지 목록은 core 작성을 막는 것이 아니라,  
core를 올바른 자리개념 guide로 유지하기 위한 guard이다.

---

## 14. Core.main.md의 확장 방식

Core.main.md는 처음부터 모든 core를 완전하게 작성해야 하는 문서가 아니다.

먼저 핵심 core부터 정리할 수 있다.

```text
dot
line
boundary
position
Seed.Base
Active_Schema
thinking_flow
relation bridge
Ctp
circle
CoreDot ambiguity boundary
```

이후 필요에 따라 나머지 core를 추가한다.

중요한 것은 모든 파일을 빨리 나열하는 것이 아니라,  
각 meta.md가 무엇을 설명하는지 정확히 기록하는 것이다.

---

## 15. Reading Guard

AI는 Core.main.md를 읽을 때 다음을 지켜야 한다.

```text
Core.main.md는 파일목록이 아니라 core reading guide이다.
Core.main.md는 meta.md를 대체하는 것이 아니라 meta.md를 읽기 위한 안내문이다.
Core.main.md는 Coremap이 아니라 각 core가 무엇을 설명하는지 알려주는 문서이다.
Core.main.md의 relation_hint는 confirmed relation이 아니라 읽기 방향 hint이다.
Core.main.md의 order_hint는 identity가 아니라 탐색 보조값이다.
```

AI는 다음을 하면 안 된다.

```text
Core.main.md를 schema 전체 목록으로만 읽기
Core.main.md를 concept dictionary로 읽기
Core.main.md를 final proof document로 읽기
Core.main.md를 relation merge map으로 읽기
```

---

## 16. 최단 정의

```text
Core.main.md
=
Structure_Principle/schema/ 내부 meta.md들이 각각 무엇을 설명하는지 알려주는 main guide 문서이다.

이 문서는 파일목록이 아니라 core reading guide이며,
meta.md가 형성한 자리개념 boundary를 AI가 오독하지 않도록 돕는다.
```