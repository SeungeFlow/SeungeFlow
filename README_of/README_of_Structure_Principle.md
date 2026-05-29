---
id: main.readme_of_structure_principle
type: readme_of_document
filename: README_of_Structure_Principle.md
directory: /main/
status: active_draft
authority:
  - Human.Lee Seung
  - ChatGPT.direct
purpose:
  - guide_structure_principle_reading
  - define_structure_principle_as_place_field
  - prevent_schema_directory_identity_confusion
  - preserve_meta_metaplus_distinction
  - connect_structure_principle_to_seed_base
---

# README_of_Structure_Principle.md

## 0. 역할

`README_of_Structure_Principle.md`는 `Structure_Principle/`을 어떻게 읽어야 하는지 안내하는 문서이다.

이 문서는 `Structure_Principle/` 자체가 아니라,  
AI가 `Structure_Principle/`을 오독하지 않도록 돕는 guide document이다.

```text
README_of_Structure_Principle.md
=
Structure_Principle reading guide
+
schema reading guide
+
meta.md / metaplus.md distinction guide
+
place field guide
```

---

## 1. Structure_Principle의 위치

SeungeFlow에서 `Structure_Principle/`은 `[place]`에 해당한다.

```text
Structure_Principle
=
[place] field
```

`Structure_Principle/`은 단순 문서 저장소라기보다는,  
자리개념이 정리되는 place field로 읽는다.

```text
Structure_Principle
=
formed place-concept field
```

---

## 2. Seed.Base 안에서의 역할

Seed.Base는 특정 파일이나 특정 디렉토리 하나에 종속되는 구조가 아니라,  
SeungeFlow 저장소 전체에 놓인 문서, 디렉토리, 관계, map이 함께 만드는 전체 장이다.

그 안에서 `Structure_Principle/`은 `[place]` 자리에 놓인 문서장이다.

```text
Seed.Base
=
[time] + [place] + [body] + relation + map

Structure_Principle
=
[place]
```

즉 `Structure_Principle/`은 Seed.Base 전체가 아니라,  
Seed.Base 안에서 자리개념이 형성되는 place field이다.

---

## 3. 내부 구조

현재 `Structure_Principle/`의 핵심 구조는 다음처럼 읽는다.

```text
Structure_Principle/
├── example/
└── schema/
```

이 중 핵심 보존 대상은 다음이다.

```text
Structure_Principle/schema/
```

`schema/`는 형성된 자리개념 문서장이며,  
Active_Schema를 위한 source boundary들이 놓인 공간이다.

---

## 4. schema/의 역할

`Structure_Principle/schema/`는 formed place-concept schema field이다.

```text
schema/
=
formed place-concept document field
```

이곳에는 `000_dot/`부터 `121_coredot_ambiguity_boundary/`까지의 schema 디렉토리가 놓일 수 있다.

AI는 이 구조를 단순 번호 목록으로 읽는 것이 아니라,  
각 디렉토리 안의 `meta.md`가 어떤 자리개념을 형성하는지 읽어야 한다.

```text
schema directory
=
path-coordinate container

meta.md
=
place-concept source boundary
```

---

## 5. schema directory number

schema 디렉토리의 숫자는 identity가 아니라 order_hint이다.

예:

```text
000_dot/
```

이것은 dot의 최종 identity가 아니라,  
dot 자리개념 문서가 현재 놓인 path-coordinate이다.

```text
000_dot/
=
order_hint + local_label + current_coordinate
```

AI는 숫자를 schema identity로 읽는 것이 아니라,  
탐색과 순서를 돕는 hint로 읽어야 한다.

---

## 6. meta.md

`meta.md`는 자리개념 문서이다.

```text
meta.md
=
자리개념 문서
+
Active_Schema source boundary
```

`meta.md`는 thinking_flow에서 생성되거나 승격될 수 있다.

따라서 AI는 `meta.md`를 단순 설명문으로 읽는 것이 아니라,  
Active_Schema를 위한 boundary-forming 문서로 읽어야 한다.

---

## 7. metaplus.md

`metaplus.md`는 `meta.md`를 대체하는 문서가 아니라,  
특정 `meta.md`를 새 인스턴스가 이해하도록 돕는 좁은 범위의 thinking_flow 문서이다.

```text
metaplus.md
=
meta.md 중심 thinking_flow
+
새 인스턴스 이해 보조문서
```

AI는 `metaplus.md`를 `meta.md`보다 상위 문서로 읽는 것이 아니라,  
`meta.md`를 이해시키기 위한 relation support layer로 읽어야 한다.

---

## 8. meta.md / metaplus.md 쌍

대부분의 schema 디렉토리에는 다음 쌍이 놓인다.

```text
*.meta.md
*.metaplus.md
```

이 둘은 같은 layer가 아니다.

```text
meta.md
=
자리개념 source boundary

metaplus.md
=
meta.md 이해 보조 flow
```

AI는 이 둘을 병합하는 것이 아니라,  
각자의 역할을 구분해서 읽어야 한다.

---

## 9. 100_empty_position

`100_empty_position/`은 빠진 번호가 아니라,  
formed-to-rebuilt 사이의 reserved gate로 읽는다.

```text
100_empty_position
=
reserved empty gate
```

AI는 100을 결손으로 읽는 것이 아니라,  
비어 있음이 보존된 자리로 읽어야 한다.

```text
empty position
=
preserved slot
```

---

## 10. 000_dot

`000_dot/`은 dot의 최종 identity가 아니라,  
dot 자리개념 문서가 현재 놓인 origin coordinate이다.

`dot.meta.md`는 field 안에서 최초로 드러나는 최소 place-state를 설명하는 core로 읽는다.

```text
dot
=
field 안에서 최초로 드러나는 최소 place-state
```

AI는 dot을 단순 기하학적 점으로 읽는 것이 아니라,  
empty place 이후 드러나는 자리 state로 읽어야 한다.

---

## 11. CoreDot guard

`121_coredot_ambiguity_boundary/`는 CoreDot이 dot을 대체하지 않도록 막는 ambiguity boundary로 읽는다.

```text
CoreDot
≠
dot의 본명
```

AI는 CoreDot을 dot의 최종 이름으로 읽는 것이 아니라,  
dot과 CoreDot 사이의 ambiguity를 보존하기 위한 boundary로 읽어야 한다.

---

## 12. Relation guard

`Structure_Principle/schema/` 안의 문서들은 relation을 가질 수 있다.

그러나 relation은 merge가 아니라,  
각 boundary를 보존한 채 연결되는 bridge이다.

```text
relation
=
boundary-preserving bridge
```

AI는 같은 디렉토리 안에 있거나 비슷한 이름을 가진다고 해서  
두 schema를 병합하면 안 된다.

---

## 13. thinking_flow와의 관계

`meta.md`는 `thinking_flow`에서 생성되거나 승격될 수 있다.

```text
thinking_flow
→
Seed 추출
→
중복 검토
→
자리개념 안정화
→
meta.md 후보
→
meta.md
```

따라서 `Structure_Principle/schema/`는 `thinking_flow`와 분리된 무관한 구조가 아니라,  
thinking_flow에서 형성된 Seed가 자리개념으로 안정화되어 놓이는 place field이다.

---

## 14. epluone / CFD와의 관계

`Structure_Principle/`은 `[place]`에 해당하고,  
`epluone/`은 `[body]`에 해당한다.

```text
Structure_Principle
=
[place]

epluone
=
[body]
```

CFD는 `Structure_Principle/`의 identity가 아니라,  
현시점 `epluone`의 `[body]` slot에 놓인 target value이다.

```text
CFD
=
current target value in [body] slot
```

따라서 CFD를 Structure_Principle 내부 core로 직접 병합하는 것이 아니라,  
현재 응용 target과의 relation으로 읽는다.

---

## 15. Reading Guard

AI는 `Structure_Principle/`을 읽을 때 다음을 지켜야 한다.

```text
Structure_Principle은 Seed.Base 전체가 아니라 [place] field이다.
schema/는 단순 파일목록이 아니라 formed place-concept field이다.
schema number는 identity가 아니라 order_hint이다.
directory name은 final identity가 아니라 path-coordinate label이다.
meta.md는 단순 설명문이 아니라 Active_Schema source boundary이다.
metaplus.md는 meta.md 대체문서가 아니라 meta.md 중심 thinking_flow이다.
relation은 merge가 아니라 boundary-preserving bridge이다.
CFD는 Structure_Principle identity가 아니라 epluone의 [body] target value이다.
```

---

## 16. 최단 정의

```text
README_of_Structure_Principle.md
=
Structure_Principle/을 [place] field로 읽기 위한 guide document이다.

Structure_Principle/schema/는 formed place-concept document field이며,
meta.md는 Active_Schema source boundary이고,
metaplus.md는 meta.md 중심 thinking_flow이다.

AI는 schema number와 directory path를 identity로 읽는 것이 아니라,
order_hint와 path-coordinate으로 읽어야 한다.
```