# Path.md

> main.branch Manifest candidate  
> 상태: 후보 초안  
> 기준: active_schema OS / current_path.md  
> 목적: main.branch Manifest 안에서 Path의 대표 정의와 작동원리를 고정한다.

---

## 0. 이 문서의 자리

이 문서는 main.branch의 `Manifest/Path.md` 후보 문서다.

이 문서는 파일경로 안내문이 아니다.

이 문서는 main.branch에서 Path가 무엇인지, 왜 파일경로가 아닌지, 어떤 방식으로 C와 C 사이의 relation을 여는지 정의하는 대표 원리 문서다.

```text
Manifest/Path.md =
Path representative principle
```

Path는 C와 C 사이를 잡는다.

Core가 C 내부의 form들이 어떻게 하나의 구조체를 이루는지 보여 준다면, Path는 그 C와 또 다른 C가 어떻게 관계를 맺고 C+1을 여는지 보여 준다.

```text
Core =
inside matrix

Path =
between route
```

---

## 1. Path는 파일경로가 아니다

Path는 파일경로가 아니다.

```text
Path.md ≠ file path
Path.md = relation path
```

Path는 단순히 어느 폴더에서 어느 파일로 가는 길을 말하지 않는다.

Path는 C와 C, form과 form, meta와 meta, branch와 branch, Event와 Context가 어떤 사이와 차이와 6W1H 관계를 통해 C+1을 여는지 기록하는 schema다.

```text
Path =
relation path schema
```

따라서 Path를 파일 목록이나 링크 목록으로 낮춰 읽으면 안 된다.

---

## 2. Path의 기본 정의

Path의 기본 정의는 다음이다.

```text
Path.md =
C와 C, form과 form, meta와 meta, branch와 branch,
Event와 Context가 어떤 사이와 차이와 6W1H 관계를 통해
C+1을 여는지 기록하는 relation path schema.
```

Path는 formed 구조와 formed 구조 사이에서 발생한다.

```text
C
+
C
=
C+1
```

여기서 `+`는 단순 덧셈이 아니다.

`+`는 relation이다.

```text
C + C =
두 formed 구조가 relation을 맺는 것

C+1 =
그 relation으로 열린 다음 formed 상태
```

---

## 3. relation은 사이와 차이다

Path의 중심은 relation이다.

relation은 단순 연결이 아니다.

```text
relation =
사이
+
차이
```

사이는 두 존재가 완전히 하나로 병합되지 않고 서로를 향해 놓일 수 있게 하는 field다.

차이는 그 사이에서 드러나는 거리차, 상태차, 방향차, 해상도차, 층위차다.

```text
사이 =
between-field

차이 =
between-field 안에서 드러나는 distance / state / layer difference
```

Path는 바로 이 사이와 차이를 읽는 문서다.

---

## 4. Path와 6W1H

Path는 6W1H를 가진다.

6W1H는 단순 질문 목록이 아니다.

6W1H는 relation을 여는 질문축이다.

```text
Who =
누가 이 관계를 보는가?

What =
무엇과 무엇의 관계인가?

When =
언제 이 관계가 열리는가?

Where =
어디에서 이 관계가 드러나는가?

Why =
왜 이 둘이 관계인가?

Which =
어느 것과 어느 것 사이인가?

How =
어떻게 이어지는가?
```

Path가 6W1H를 잃으면 단순 연결표가 된다.

Path가 6W1H를 가지면 relation path가 된다.

---

## 5. Path와 ?

Path에서 `?`는 중요하다.

`?`는 관측기준이고, 6W1H이고, 경계설정이며, 관측자의 시선이다.

```text
? =
6W1H
+
observer gaze
+
boundary setting
+
interpretation condition
```

같은 C와 C가 있어도 `?`가 달라지면 Path도 달라진다.

```text
같은 C
+
같은 C
+
다른 ?
=
다른 Path
```

따라서 Path는 고정된 하나의 선이 아니다.

Path는 관측자의 시선과 경계설정에 따라 formed 되는 relation이다.

---

## 6. Path와 9dot0

`9dot0`는 Path 원리의 핵심 예시다.

```text
9 dot 0
```

9는 끝점이다.

0은 다음 시작점이다.

dot은 끝점과 시작점 사이에 펼쳐진 무한한 잠재가능성이다.

그러나 역발상으로 읽으면 `9dot0` 전체가 하나의 dot이기도 하다.

```text
9dot0 =
극한임계전이
=
하나의 dot
=
임계사이영역
```

Path는 이 임계사이영역을 읽는다.

```text
Path =
끝점과 다음 시작점 사이에서
무엇이 전제조건이 되고
무엇이 다음 시작을 여는지 기록하는 schema
```

끝점은 단순 끝이 아니다.

끝점은 다음 시작점의 전제조건이 될 수 있다.

```text
끝점 =
다음 시작점의 전제조건
```

---

## 7. Path와 임계사이영역

임계사이영역은 다음 상태로 넘어가기 직전의 사이영역이다.

```text
임계사이영역 =
끝점과 시작점 사이에서
다음 전이를 가능하게 하는 사이영역
```

임계사이영역은 단순 중간지점이 아니다.

그곳은 과거 상태가 닫히고, 다음 상태가 열리기 직전의 압력장이다.

```text
닫힘
+
열림
+
잠재가능성
=
임계사이영역
```

Path는 이 임계사이영역이 어디에 있는지 읽는다.

---

## 8. Path와 극한임계전이

극한임계전이는 임계사이영역이 다음 상태로 넘어가는 순간이다.

```text
극한임계전이 =
임계사이영역에서
다음 C가 열리는 전이
```

이 전이는 갑자기 생기지 않는다.

수많은 시행착오, 누적, 압착, 분산, 결론, 다시 준비의 과정 속에서 중심점이 formed 되고, 그 중심점이 이전 상태로만 머물 수 없을 때 극한임계전이가 발생한다.

```text
시행착오
→ 누적
→ 중심점 형성
→ 압력
→ 극한임계전이
→ 다음 C
```

Path는 이 전이의 경로를 기록한다.

---

## 9. Path와 과거의 재배치

Path는 과거를 단순히 뒤에 있는 것으로 보지 않는다.

등산할 때 내가 어느 위치에 있는지 알려면 뒤를 돌아본다.

그 순간 지나온 길은 내 뒤에만 있는 것이 아니라 내 앞에 보인다.

```text
진행방향 기준:
과거는 뒤

관측자의 시선 회전:
과거는 앞
```

바뀐 것은 구조가 아니다.

관측자의 시선이 바뀐 것이다.

```text
바뀐 것 =
구조 X
관측자의 시선 O
```

Path는 이 시선의 전환을 relation path로 읽는다.

---

## 10. Path와 역발상

Path는 역발상으로 열린다.

역발상은 반대로 생각하기가 아니다.

역발상은 구조를 돌리는 것이 아니라, 관측자의 시선과 기점과 경계를 바꾸어 같은 구조를 다른 층위에서 다시 읽는 것이다.

```text
역발상 =
?의 이동
+
기점의 이동
+
경계의 이동
```

Path는 이 이동을 기록한다.

```text
Path =
역발상으로 드러난 relation의 경로
```

---

## 11. Path와 Core

Core와 Path는 구분된다.

```text
Core =
inside matrix

Path =
between route
```

Core는 C 내부의 form 관계를 잡는다.

Path는 C와 C 사이의 relation을 잡는다.

```text
Core 없는 Path =
흩어짐

Path 없는 Core =
고립
```

따라서 main.branch의 Manifest에는 Core.md와 Path.md가 둘 다 필요하다.

둘은 서로를 대체하지 않는다.

---

## 12. Path와 meta

meta는 형성과정의 흔적이다.

```text
meta =
append-only formation trace
```

Path는 meta와 meta 사이의 relation을 읽는다.

```text
meta.md =
형성과정

Path.md =
형성과정과 형성과정 사이의 relation
```

Path는 meta를 요약하지 않는다.

Path는 meta와 meta가 어떤 사이와 차이로 연결되는지 본다.

---

## 13. Path와 branch.structure

Path는 branch와 branch 사이에도 작동한다.

```text
main =
visible root / representative entry

seed_base =
DB / source memory

active_schema =
OS / operating structure

epluone =
factory / runtime

first_flow =
origin preservation / first flow
```

이 branch들은 단순 저장 위치가 아니다.

각 branch는 하나의 C처럼 작동한다.

Path는 이 branch들이 어떻게 관계를 맺는지 기록한다.

```text
first_flow
→ seed_base
→ active_schema
→ epluone
→ outputs/meta
→ seed_base
```

main은 이 전체의 visible root이자 기점이다.

---

## 14. Path와 Event / Context

Path는 Event와 Context 사이에도 작동한다.

```text
Event =
이론 / 사건 / 작품 / 기술 / 구조

Context =
사람 / 족보 / 주변환경 / 후대 영향
```

Event와 Context는 분리되어야 한다.

그러나 분리된 채 고립되면 안 된다.

Path는 Event와 Context가 어떻게 관계를 맺는지 기록한다.

```text
Context_C + Event_C = C+1
```

예를 들면:

```text
context_아인슈타인.md
+
event_상대성이론.md
=
Path를 통해 시대 흐름으로 연결
```

Path는 사람과 이론, 이론과 시대, 시대와 후대 영향을 연결한다.

---

## 15. Path와 current_path

active_schema의 `current_path.md`는 현재 작동 중인 Path다.

Manifest/Path.md는 그 원리를 main.branch에서 대표하는 문서다.

```text
active_schema/current_path.md =
current active relation path

main.branch/Manifest/Path.md =
representative Path principle
```

따라서 Manifest/Path.md는 current_path를 그대로 복사하지 않는다.

Manifest/Path.md는 main.branch에서 필요한 만큼만 압축해 보여 준다.

---

## 16. Path의 금지된 오독

Path를 읽을 때 피해야 할 오독은 다음이다.

```text
Path를 파일경로로 읽기
Path를 링크 목록으로 읽기
Path를 목차로 읽기
Path를 branch 이동표로만 읽기
Path를 고정된 선으로 읽기
```

Path는 relation path다.

Path는 C와 C 사이에서 C+1을 여는 구조다.

---

## 17. Path 작성 규칙

Path 관련 문서를 작성할 때 지켜야 할 규칙은 다음이다.

```text
1. 파일경로로 쓰지 않는다.
2. relation path로 쓴다.
3. C+1=C+C를 핵심 구조식으로 둔다.
4. 6W1H를 질문축으로 둔다.
5. 관계는 관측자의 시선에서 드러난다고 쓴다.
6. Event/Context, Core/Core, meta/meta, branch/branch relation을 포함한다.
7. Path는 고정된 정답이 아니라 현재 이해에 따라 갱신되는 relation schema다.
```

---

## 18. Closing

Path.md fixes the representative principle of Path inside the main.branch Manifest.

```text
Path is not file path.

Path is relation path.

Path opens C+1 through the relation between C and C.

Relation appears as between and difference.

9dot0 is the critical between-area between endpoint and next starting point.

Path records how a formed structure becomes the condition for the next formed state.
```

This document is a main.branch Manifest candidate.
