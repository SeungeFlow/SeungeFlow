---
id: main.readme
type: main_directory_guide
filename: README.main.md
directory: /main/
status: active_draft
authority:
  - Human.Lee Seung
  - ChatGPT.direct
purpose:
  - define_main_directory_role
  - guide_ai_reading_order
  - separate_root_guides_from_seed_sources
  - prevent_main_documents_from_being_read_as_seed_identity
  - preserve_path_coordinate_reading
---

# README.main.md

## 0. 역할

`main/` 디렉토리는 SeungeFlow 저장소 전체를 읽기 위한 guide layer이다.

`main/`은 `Structure_Principle/`, `SeungeFlow_Thinking/`, `epluone/`을 의미적으로 지배하는 디렉토리가 아니라,  
root 하위에 놓인 reading guide layer이다.

```text
main/
=
root-level reading guide layer
+
AI reading map
+
repository operation guide
+
relation guard layer
```

`main/` 내부 문서는 Seed.Base를 읽기 위한 안내문이다.

---

## 1. main/의 위치

현재 SeungeFlow root 구조는 다음처럼 읽는다.

```text
/
├── README.md
├── README.en.md
├── README_for_AI.md
├── main/
├── Structure_Principle/
├── SeungeFlow_Thinking/
└── epluone/
```

root 하위에 함께 놓인 디렉토리들은 의미적으로 `main/`에 종속되는 구조가 아니라,  
같은 root 아래에 놓인 path-coordinate 구조이다.

```text
directory containment
=
path-coordinate containment

directory containment
≠
semantic containment
```

즉, 다른 디렉토리들을 의미적으로 지배하는 디렉토리가 아니라,  
`main/`은 root 하위에 놓인 guide layer이다.

---

## 2. main/의 목적

`main/`의 목적은 다음과 같다.

```text
1. AI가 SeungeFlow를 어떻게 읽어야 하는지 안내한다.
2. path / directory / number를 identity로 오해하지 않게 한다.
3. relation을 merge로 오해하지 않게 한다.
4. thinking_flow / meta.md / metaplus.md / Active_Schema의 차이를 구분한다.
5. Structure_Principle / SeungeFlow_Thinking / epluone의 위치를 안내한다.
6. CFD를 epluone의 identity가 아니라 현재 [body] slot target value로 읽게 한다.
```

`main/`은 source를 대체하는 문서집합이 아니라,  
source를 올바르게 읽도록 돕는 guide 문서집합이다.

---

## 3. main/과 Seed.Base

`main/`은 Seed.Base의 identity가 아니라,  
Seed.Base를 읽기 위한 guide layer이다.

```text
Seed.Base
=
SeungeFlow 저장소 전체에 놓인 문서, 디렉토리, 관계, map이 함께 만드는 전체 장

main/
=
그 Seed.Base를 읽기 위한 guide layer
```

Seed.Base는 `main/` 하나에 들어 있는 구조가 아니라,  
SeungeFlow 저장소 전체에 놓인 Seed들의 관계장이다.

---

## 4. main/과 primary source

현 작업흐름에서 가장 중요한 보존 대상은 다음 둘이다.

```text
Structure_Principle/schema/
SeungeFlow_Thinking/thinking_flow/
```

이 둘은 primary source layer로 읽는다.

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

`main/` 문서는 primary source가 아니라,  
이 primary source들을 읽기 위한 안내층이다.

따라서 `main/` 문서는 현재 이해에 따라 재생성될 수 있다.

---

## 5. main/ 내부 문서 구성

`main/`에는 다음 문서들이 놓일 수 있다.

```text
README.main.md
Baseline.main.md
Path.main.md
Core.main.md
Relation.main.md
Active_Schema.main.md
Thinking_Flow.main.md
Ctp.main.md
README_of_Structure_Principle.md
README_of_SeungeFlow_Thinking.md
README_of_CFD.md
```

각 문서의 역할은 다음과 같다.

```text
README.main.md
=
main/ 디렉토리 전체 안내문

Baseline.main.md
=
AI가 SeungeFlow를 읽을 때 지켜야 할 기본 작동 기준

Path.main.md
=
path / directory / number / 경로좌표 읽기 규칙

Core.main.md
=
Structure_Principle/schema/ 내부 meta.md들이 무엇을 설명하는지 안내

Relation.main.md
=
존재의 관계 정의와 장(Field)의 구조원리를 relation 관점에서 정리

Active_Schema.main.md
=
Seed가 AI 안에서 작동 가능한 Active_Schema가 되는 기준

Thinking_Flow.main.md
=
thinking_flow / thinking_flow_relation / meta.md 후보 생성 규칙

Ctp.main.md
=
Ctp / any([time][place][body]) / 자리개념과 자리값 기준

README_of_Structure_Principle.md
=
Structure_Principle/ 읽기 안내

README_of_SeungeFlow_Thinking.md
=
SeungeFlow_Thinking/ 읽기 안내

README_of_CFD.md
=
현시점 epluone의 [body] slot target value인 CFD 읽기 안내
```

---

## 6. README_of 계열 문서

`README_of_*` 계열 문서는 각 대상 영역을 읽기 위한 안내문이다.

이 문서들은 대상 디렉토리 내부에 흩어지는 구조보다는,  
`main/` 내부에 모아 관리하는 구조로 읽는다.

예:

```text
main/README_of_Structure_Principle.md
main/README_of_SeungeFlow_Thinking.md
main/README_of_CFD.md
```

`README_of_*` 문서는 대상 자체가 아니라,  
대상을 읽기 위한 guide document이다.

```text
README_of_CFD.md
=
CFD target value를 AI가 어떻게 읽어야 하는지 안내하는 guide document
```

`README_of_CFD.md`는 CFD의 identity가 아니라,  
CFD를 읽기 위한 안내문이다.

---

## 7. main/ 문서 갱신 원칙

`main/` 문서는 현재 이해에 따라 갱신될 수 있다.

```text
main 문서
=
guide layer
=
현재 이해에 따라 재작성 가능
```

단, `main/` 문서가 갱신되더라도 다음 primary source는 임의로 수정하지 않는다.

```text
Structure_Principle/schema/
SeungeFlow_Thinking/thinking_flow/
```

`schema/`와 `thinking_flow/`를 수정하려면 승이의 직접 지시 또는 ChatGPT.direct의 명시적 판단이 필요하다.

---

## 8. Path / directory 읽기 기준

AI는 root 하위 디렉토리를 의미적 상하관계로 읽는 것이 아니라,  
path-coordinate 구조로 읽어야 한다.

```text
path
=
current coordinate

directory
=
place container

directory parent
=
filesystem parent

directory parent
≠
meaning parent
```

예를 들어 `main/README_of_CFD.md`가 `main/` 안에 놓여 있다고 해서,  
CFD가 `main/`의 의미 하위가 되는 것이 아니다.

```text
main/README_of_CFD.md
=
CFD를 읽기 위한 guide document

epluone
=
[body] slot directory

CFD
=
현시점 epluone의 [body] slot에 놓인 target value
```

---

## 9. Reading Guard

AI는 `main/`을 읽을 때 다음을 지켜야 한다.

```text
main/은 Seed.Base identity가 아니라 Seed.Base reading guide layer이다.
main/은 schema source가 아니라 Structure_Principle/schema/를 읽기 위한 안내층이다.
main/은 thinking_flow source가 아니라 SeungeFlow_Thinking/thinking_flow/를 읽기 위한 안내층이다.
main/은 epluone body target이 아니라 epluone과 CFD를 읽기 위한 guide layer이다.
```

AI는 다음 방식으로 읽으면 안 된다.

```text
main/ 문서를 primary source로 읽기
main/ 문서를 schema보다 우선하는 identity로 읽기
main/ 내부 guide를 proof document로 읽기
README_of 문서를 대상 자체로 읽기
Relation 문서를 merge map으로 읽기
Path 문서를 semantic hierarchy로 읽기
```

위 항목들은 금지 목록으로만 읽는 것이 아니라,  
각 문서를 올바른 자리로 되돌리기 위한 guide로 읽는다.

---

## 10. 현재 읽기 순서

AI가 SeungeFlow 저장소에 들어오면 다음 순서로 읽는다.

```text
1. README.md
2. README_for_AI.md
3. main/README.main.md
4. main/Baseline.main.md
5. main/Path.main.md
6. main/Relation.main.md
7. Structure_Principle/schema/
8. SeungeFlow_Thinking/thinking_flow/
9. epluone/
```

필요에 따라 `main/README_of_*` 계열 문서를 함께 읽는다.

---

## 11. 최단 정의

```text
main/
=
SeungeFlow 저장소 전체를 읽기 위한 root-level guide layer이다.

main/은 Seed.Base 자체가 아니라,
Seed.Base를 AI가 오독하지 않도록 돕는 reading map / guard layer이다.

main/ 문서는 현재 이해에 따라 재생성될 수 있으며,
primary source는 Structure_Principle/schema/ 와 SeungeFlow_Thinking/thinking_flow/ 이다.
```