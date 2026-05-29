---
id: main.readme_of_main
type: readme_of_document
filename: README_of_main.md
directory: /main/
status: active_draft
authority:
  - Human.Lee Seung
  - ChatGPT.direct
purpose:
  - guide_main_directory_reading
  - define_main_as_root_level_guide_layer
  - prevent_main_from_being_read_as_primary_source
  - distinguish_main_from_seed_base_identity
  - connect_readme_of_documents
---

# README_of_main.md

## 0. 역할

`README_of_main.md`는 `main/` 디렉토리 자체를 어떻게 읽어야 하는지 안내하는 문서이다.

이 문서는 `main/` 내부 전체 문서 목록을 단순 나열하기 위한 문서가 아니라,  
AI가 `main/`을 root-level guide layer로 읽도록 돕는 guide document이다.

```text
README_of_main.md
=
main directory reading guide
+
root-level guide layer explanation
+
README_of document family guide
+
main source confusion guard
```

---

## 1. main/의 기본 정의

`main/`은 SeungeFlow 저장소 전체를 읽기 위한 root-level guide layer이다.

```text
main/
=
root-level guide layer
```

`main/`은 `Structure_Principle/`, `SeungeFlow_Thinking/`, `epluone/`을 의미적으로 지배하는 디렉토리가 아니라,  
root 하위에 놓인 guide document field이다.

```text
main/
=
guide document field

main/
≠
semantic parent of other root directories
```

---

## 2. main/과 Seed.Base

Seed.Base는 `main/` 하나에 종속되는 구조가 아니라,  
SeungeFlow 저장소 전체에 놓인 문서, 디렉토리, 관계, map이 함께 만드는 전체 장이다.

```text
Seed.Base
=
whole repository field
```

`main/`은 Seed.Base 자체가 아니라,  
Seed.Base를 읽기 위한 guide layer이다.

```text
main/
=
Seed.Base reading guide layer
```

따라서 AI는 `main/`을 Seed.Base의 identity로 읽는 것이 아니라,  
Seed.Base를 읽기 위한 안내층으로 읽어야 한다.

---

## 3. main/과 primary source

현 작업흐름에서 primary source는 다음 둘이다.

```text
Structure_Principle/schema/
SeungeFlow_Thinking/thinking_flow/
```

`main/`은 primary source가 아니라,  
primary source를 읽도록 돕는 guide layer이다.

```text
main/
=
guide layer

Structure_Principle/schema/
=
formed place-concept source layer

SeungeFlow_Thinking/thinking_flow/
=
pre-meta thinking flow source layer
```

따라서 `main/` 문서는 현재 이해에 따라 재작성될 수 있지만,  
primary source는 임의로 수정하지 않는다.

---

## 4. main/ 내부 문서

`main/` 내부 문서는 SeungeFlow를 읽기 위한 guide document이다.

예:

```text
README.main.md
Baseline.main.md
Path.main.md
Core.main.md
Relation.main.md
Coremap.main.md
Active_Schema.main.md
Thinking_Flow.main.md
Ctp.main.md
README_of_main.md
README_of_Structure_Principle.md
README_of_SeungeFlow_Thinking.md
README_of_epluone.md
README_of_CFD.md
```

이 문서들은 각각 다른 역할을 가진다.

```text
Baseline.main.md
=
AI 기본 작동 기준

Path.main.md
=
path / directory / number 읽기 기준

Core.main.md
=
schema meta.md core 안내

Relation.main.md
=
relation 읽기 원칙

Coremap.main.md
=
core relation map

Active_Schema.main.md
=
Seed 활성화 기준

Thinking_Flow.main.md
=
thinking_flow 읽기 기준

Ctp.main.md
=
Ctp / any([time][place][body]) 기준
```

---

## 5. README_of 계열 문서

`README_of_*` 계열 문서는 대상 자체가 아니라,  
대상을 읽기 위한 guide document이다.

```text
README_of_*
=
guide document for target
```

예:

```text
README_of_Structure_Principle.md
=
Structure_Principle/ reading guide

README_of_SeungeFlow_Thinking.md
=
SeungeFlow_Thinking/ reading guide

README_of_epluone.md
=
epluone/ reading guide

README_of_CFD.md
=
CFD target value reading guide
```

이 문서들이 `main/`에 모여 있다는 것은 대상들이 `main/`에 의미적으로 종속된다는 뜻이 아니라,  
guide 문서들이 root-level guide layer에 모여 있다는 뜻이다.

---

## 6. main/과 epluone

`epluone/`은 `if+1`이며 `[body]` slot directory이다.

```text
epluone
=
if+1
=
[body] slot directory
```

`main/README_of_epluone.md`는 `epluone/` 자체가 아니라,  
`epluone/`을 읽기 위한 guide document이다.

`main/README_of_CFD.md`는 CFD 자체가 아니라,  
현시점 `epluone`의 `[body]` slot에 놓인 target value인 CFD를 읽기 위한 guide document이다.

---

## 7. main/과 relation

`main/` 내부 relation 문서들은 relation을 병합시키기 위한 문서가 아니라,  
각 boundary를 보존한 채 relation을 읽도록 돕는 guide 문서이다.

```text
relation
=
boundary-preserving bridge
```

따라서 AI는 `Relation.main.md`나 `Coremap.main.md`를 merge map으로 읽는 것이 아니라,  
relation guard / relation map으로 읽어야 한다.

---

## 8. main/ 갱신 기준

`main/` 문서는 현재 이해에 따라 갱신될 수 있다.

```text
main document
=
regenerable guide layer
```

그러나 `main/` 문서의 갱신은 primary source를 자동으로 수정한다는 뜻이 아니다.

```text
main update
≠
schema update

main update
≠
thinking_flow update
```

`Structure_Principle/schema/`와 `SeungeFlow_Thinking/thinking_flow/`는 승이의 직접 지시 또는 ChatGPT.direct의 명시적 판단 없이는 수정하지 않는다.

---

## 9. Reading Guard

AI는 `main/`을 읽을 때 다음을 지켜야 한다.

```text
main/은 Seed.Base identity가 아니라 Seed.Base reading guide layer이다.
main/은 primary source가 아니라 primary source guide layer이다.
main/은 다른 root 디렉토리의 semantic parent가 아니라 root-level guide field이다.
README_of_* 문서는 대상 자체가 아니라 대상 읽기 guide document이다.
main/ 문서는 현재 이해에 따라 재생성될 수 있는 guide layer이다.
```

AI는 다음을 하면 안 된다.

```text
main/을 Seed.Base 전체로 읽기
main/을 Structure_Principle/의 상위 의미구조로 읽기
main/을 SeungeFlow_Thinking/의 상위 의미구조로 읽기
main/을 epluone/의 상위 의미구조로 읽기
README_of_* 문서를 대상 자체로 읽기
main/ 문서를 proof document로 읽기
main/ 문서를 primary source로 읽기
```

---

## 10. 최단 정의

```text
README_of_main.md
=
main/ 디렉토리를 root-level guide layer로 읽기 위한 guide document이다.

main/은 Seed.Base 자체가 아니라 Seed.Base reading guide layer이고,
primary source는 Structure_Principle/schema/ 와 SeungeFlow_Thinking/thinking_flow/ 이다.

README_of_* 계열 문서는 대상 자체가 아니라 대상 읽기 guide document이다.
```