---
id: ctp.readme
type: ctp_directory_entry_document
filename: README.md
directory: /Ctp/
status: active_draft
authority:
  - Human.Lee Seung
  - ChatGPT.direct
purpose:
  - define_ctp_directory_role
  - preserve_ctp_as_backbone_document_set
  - prevent_ctp_from_being_overdefined_in_main_guides
  - mark_ctp_as_reference_backbone_for_time_place_state
---

# Ctp/README.md

## 0. 역할

`Ctp/` 디렉토리는 Ctp Backbone 문서집합이 놓일 자리이다.

이 문서는 Ctp 전체를 완성 정의하는 문서가 아니라,  
Ctp 문서집합이 어떤 위치와 역할을 가지는지 표시하는 입구 문서이다.

```text
Ctp/
=
Ctp Backbone document set directory
+
time.state / place.state reference field
+
Ctp reading entry
```

---

## 1. Ctp의 현재 위치

현시점에서 Ctp는 완성된 단일 정의로 닫힌 개념이라기보다,  
SeungeFlow 전체에서 Backbone 역할을 하는 거대문서집합의 tag name / reference name이다.

```text
Ctp
=
Backbone document set tag name
+
time.state / place.state reference structure
```

따라서 이 문서에서 Ctp를 완전히 정의하지 않는다.

이 문서는 Ctp 전체를 닫는 문서가 아니라,  
Ctp 문서집합으로 들어가기 위한 첫 자리이다.

---

## 2. 최소 reading marker

현재 SeungeFlow reading layer에서 Ctp는 다음 최소 표기로 읽을 수 있다.

```text
Ctp = C(t, p)
```

각 항목은 현재 다음 정도의 reading marker로만 둔다.

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

## 3. SeungeFlow 안에서의 연결

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
time.state와 place.state를 중심으로 state가 어떻게 읽히는지 받치는 Backbone reference이다.

---

## 4. main/ 문서와의 관계

`main/Ctp.main.md`나 `main/README_of_Ctp.md`는 Ctp를 완성 정의하는 문서가 아니라,  
`Ctp/` 문서집합을 읽기 위한 guide 문서이다.

```text
main/Ctp.main.md
=
Ctp guide document

main/README_of_Ctp.md
=
Ctp reading guide

Ctp/
=
Ctp Backbone document set
```

AI는 main guide 문서의 짧은 설명을 Ctp 전체 정의로 읽으면 안 된다.

---

## 5. Structure_Principle과의 관계

`Structure_Principle/`은 `[place]`에 해당하는 자리개념 문서장이다.

Ctp는 `Structure_Principle/` 내부의 하위 디렉토리라기보다,  
time.state와 place.state를 받치는 Backbone reference field로 root 하위에 놓인다.

```text
Structure_Principle
=
[place] field

Ctp
=
time.state / place.state Backbone reference field
```

따라서 Ctp는 `Structure_Principle/`에 종속되는 구조가 아니라,  
root 하위에서 SeungeFlow 전체 reading과 연결되는 Backbone 문서집합이다.

---

## 6. epluone과의 관계

`epluone/`은 `if+1`이며 `[body]` slot directory이다.

```text
epluone
=
if+1
=
[body] slot directory
```

Ctp는 `[body]` target value를 직접 고정하는 문서가 아니라,  
time.state와 place.state를 통해 어떤 state가 어떤 자리에 놓이는지 읽는 Backbone이다.

현시점 `[body]` slot의 target value는 CFD이지만,  
CFD는 Ctp의 identity가 아니다.

```text
CFD
=
current target value in epluone's [body] slot

CFD
≠
Ctp identity
```

---

## 7. Ctp 문서 작성 원칙

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

## 8. Reading Guard

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

## 9. 최단 정의

```text
Ctp/README.md
=
Ctp Backbone 문서집합의 입구 문서이다.

Ctp는 현시점에서 단일 완성 정의가 아니라,
time.state와 place.state를 중심으로 SeungeFlow 전체 state reading을 받치는 Backbone document set의 tag name / reference name이다.

Ctp = C(t,p)는 전체 정의가 아니라 최소 reading marker이다.
```
