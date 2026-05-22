---
id: main.path
type: main_path_reading_rule
filename: Path.main.md
directory: /main/
status: active_draft
authority:
  - Human.Lee Seung
  - ChatGPT.direct
purpose:
  - define_path_coordinate_reading
  - prevent_path_identity_confusion
  - prevent_directory_semantic_hierarchy_confusion
  - define_linux_based_path_transition
  - guide_repository_place_reading
---

# Path.main.md

## 0. 역할

`Path.main.md`는 SeungeFlow 저장소 안의 path, directory, number를 어떻게 읽어야 하는지 정의하는 문서이다.

이 문서는 파일 위치를 의미 identity로 고정하기 위한 문서가 아니라,  
AI가 path를 현재 좌표와 전이 구조로 읽도록 돕는 guide 문서이다.

```text
Path.main.md
=
path-coordinate reading rule
+
directory containment guard
+
number identity guard
+
Linux-based transition guide
```

---

## 1. 기본 규칙

AI는 path를 identity로 읽는 것이 아니라,  
현재 위치를 표시하는 coordinate로 읽어야 한다.

```text
path
=
current coordinate
```

AI는 directory를 의미상 부모로 읽는 것이 아니라,  
filesystem 위의 place container로 읽어야 한다.

```text
directory
=
place container
```

AI는 number를 identity로 읽는 것이 아니라,  
order_hint로 읽어야 한다.

```text
number
=
order_hint
```

---

## 2. path와 identity

GitHub path는 relation identity가 아니라,  
selected visible coordinate이다.

```text
GitHub path
=
selected visible coordinate
```

local PC는 GitHub에 선택되어 보이는 좌표가 아니라,  
더 넓은 candidate field로 읽는다.

```text
local PC
=
full candidate field
```

따라서 AI는 GitHub에 보이는 path만으로 relation identity를 확정하면 안 된다.

```text
GitHub path
≠
relation identity
```

이 문장은 path를 무시하라는 뜻이 아니라,  
path를 identity가 아닌 visible coordinate로 읽으라는 뜻이다.

---

## 3. directory containment

directory containment는 semantic containment가 아니라,  
path-coordinate containment이다.

```text
directory containment
=
path-coordinate containment
```

따라서 directory parent는 meaning parent가 아니라,  
filesystem parent이다.

```text
directory parent
=
filesystem parent

directory parent
≠
meaning parent
```

예를 들어 `main/README_of_CFD.md`가 `main/` 아래에 있다고 해서,  
CFD가 `main/`의 의미 하위가 되는 것은 아니다.

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

## 4. root 하위 디렉토리 읽기

SeungeFlow root 하위 구조는 다음처럼 읽는다.

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

이 구조는 semantic hierarchy로 읽는 것이 아니라,  
root 아래에 함께 놓인 path-coordinate field로 읽는다.

```text
root children
=
same-root path-coordinate entries
```

각 디렉토리의 역할은 다음처럼 읽는다.

```text
main/
=
root-level guide layer

Structure_Principle/
=
[place] field
+
formed place-concept schema field

SeungeFlow_Thinking/
=
[time] field
+
pre-meta thinking flow field

epluone/
=
[body] slot directory
+
current application target place
```

---

## 5. Linux식 path 전이

승이의 컴퓨팅 개념은 Linux 기반이므로,  
SeungeFlow의 path도 Linux식 place-state transition으로 읽는다.

```text
.  = current place
.. = parent transition
/  = path boundary separator
```

`.`는 현재 위치 자체를 고정 identity로 만드는 것이 아니라,  
현재 place-state를 가리킨다.

```text
.
=
current place-state
```

`..`는 특정 디렉토리 이름이 아니라,  
현재 위치에서 parent place로 전이하는 operator이다.

```text
..
=
parent transition
```

`/`는 단순 문자 구분자가 아니라,  
path boundary separator로 읽는다.

```text
/
=
path boundary separator
```

---

## 6. `..`와 전이

`..`는 identity가 아니라,  
현재 위치에 따라 달라지는 relative transition이다.

예를 들어:

```text
Structure_Principle/schema/000_dot/..
=
Structure_Principle/schema/
```

그리고:

```text
SeungeFlow_Thinking/thinking_flow/thinking_flow_014/..
=
SeungeFlow_Thinking/thinking_flow/
```

두 경우 모두 `..`는 같은 identity를 가리키는 것이 아니라,  
각 현재 위치에서 parent place로 전이하는 operator이다.

```text
.. 
=
current place → parent place
```

---

## 7. schema directory number

`Structure_Principle/schema/` 내부의 숫자 디렉토리는 schema identity가 아니라,  
order_hint와 local path-coordinate label로 읽는다.

예:

```text
Structure_Principle/schema/000_dot/
```

이 path는 다음처럼 읽는다.

```text
order_hint: 000
local_label: dot
current_coordinate: Structure_Principle/schema/000_dot/
schema_id_hint: dot
```

이 path는 dot의 최종 identity가 아니라,  
dot 자리개념 문서가 현재 놓인 coordinate이다.

따라서:

```text
000_dot/
=
order_hint + local_label + current_coordinate
```

로 읽는다.

---

## 8. meta.md와 path

`meta.md`는 path 자체가 아니라,  
해당 자리개념의 source boundary 역할을 한다.

```text
meta.md
=
place-concept document
+
Active_Schema source boundary
```

그러나 `meta.md`가 놓인 directory는 그 meta의 identity가 아니라,  
현재 저장소 안에서 그 문서가 놓인 coordinate이다.

```text
meta.md identity
≠
directory path identity
```

더 정확히는:

```text
directory path
=
where the document is currently placed

meta.md
=
what place-concept boundary is being formed
```

---

## 9. README_of 문서와 path

`README_of_*` 문서는 대상 자체가 아니라,  
대상을 읽기 위한 guide document이다.

예:

```text
main/README_of_Structure_Principle.md
=
Structure_Principle/을 읽기 위한 guide document

main/README_of_SeungeFlow_Thinking.md
=
SeungeFlow_Thinking/을 읽기 위한 guide document

main/README_of_CFD.md
=
CFD target value를 읽기 위한 guide document
```

이 문서들이 `main/` 아래에 놓여 있다는 것은,  
그 대상들이 `main/`에 의미적으로 종속된다는 뜻이 아니라,  
guide 문서들이 root-level guide layer에 모여 있다는 뜻이다.

---

## 10. relation과 path

relation은 path에서 자동으로 생기는 것이 아니라,  
문서의 boundary와 의미, 그리고 relation record를 통해 생긴다.

```text
same path group
≠
same relation

near path
≠
strong relation

same directory
≠
same meaning
```

relation은 다음처럼 읽는다.

```text
relation
=
boundary-preserving bridge
```

따라서 AI는 같은 directory 안에 있다는 이유만으로 두 문서를 merge하면 안 된다.

---

## 11. GitHub와 local PC

GitHub는 selected visible coordinate이다.

```text
GitHub
=
selected visible coordinate
```

local PC는 full candidate field이다.

```text
local PC
=
full candidate field
```

이 뜻은 GitHub가 중요하지 않다는 뜻이 아니라,  
GitHub가 현재 선택되어 외부에 드러난 coordinate라는 뜻이다.

local PC는 더 많은 후보 파일, 실험 파일, 미정리 자료가 존재할 수 있는 candidate field이다.

따라서 AI는 GitHub에 없다는 이유로 존재하지 않는다고 단정하면 안 된다.

---

## 12. Linux server와 path operation

local Linux Ubuntu server는 Oracle IDC server로 가기 전의 staging/test layer이다.

```text
local_linux_ubuntu_server
=
staging / test / git operation field
```

Oracle IDC server는 장시간 계산과 CFD 백테스팅을 위한 experiment execution layer이다.

```text
oracle_idc_server
=
long-running experiment / CFD backtesting field
```

GitHub upload 작업에서는 local Linux server가 repository operation body로 작동할 수 있다.

```text
local_linux_server
=
git runtime / upload operation body
```

---

## 13. Path Guard

AI는 다음을 하면 안 된다.

```text
path를 identity로 읽기
directory를 semantic parent로 읽기
number를 schema identity로 읽기
same directory를 same meaning으로 읽기
README_of 문서를 대상 자체로 읽기
GitHub path를 relation identity로 확정하기
local PC에 있는 candidate field를 무시하기
..를 특정 identity로 읽기
```

위 항목은 단순 금지 목록이 아니라,  
path를 올바른 자리로 되돌리기 위한 guard이다.

---

## 14. 최단 정의

```text
Path.main.md
=
SeungeFlow 저장소의 path, directory, number를
identity가 아니라 current coordinate / place container / order_hint로 읽게 하는 문서이다.

AI는 path를 의미 identity로 고정하는 것이 아니라,
현재 놓인 자리와 전이 구조로 읽어야 한다.
```