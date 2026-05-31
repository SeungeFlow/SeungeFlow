# event_context_path_schema.md

> 문서번호: `Ctp24_EVENT_CONTEXT_0004`  
> 상태: Event / Context 적용 4회차  
> 필요한 모드: `Thinking 헤비`  
> 목적: Ctp24 구조원리와 구조연산기를 실제 Event / Context 구조로 작동시키기 위한 Path schema를 작성한다.  
> 위치 후보: `epluone/Event_Context/schema/event_context_path_schema.md`

---

## 0. 이 문서의 자리

이 문서는 Event / Context 적용의 네 번째 문서다.

1회차에서는 전체 구조식을 세웠다.

```text
Context_C + Event_C = C+1
```

2회차에서는 Context를 존재 형성장으로 정의했다.

```text
Context =
존재 형성장
```

3회차에서는 Event를 formed structure로 정의했다.

```text
Event =
formed structure
```

이번 4회차에서는 Context_C와 Event_C 사이에서 실제 구조연산이 일어나는 Path를 정의한다.

Path는 파일경로가 아니다.

```text
Path ≠ file path
Path = relation path
```

이 문서의 핵심은 다음이다.

```text
Path =
Context_C와 Event_C가 relation을 맺어
C+1을 여는 구조연산 경로
```

---

## 1. Path의 기본 정의

Path는 Context와 Event를 단순 연결하지 않는다.

Path는 두 C 사이에서 사이와 차이를 읽고, 그 사이와 차이가 어떤 다음 C+1을 여는지 기록한다.

```text
Path =
C와 C 사이의 relation operation
```

Event / Context 적용에서 Path는 다음이다.

```text
Path =
Context_C와 Event_C 사이의 relation path
```

중심식:

```text
Context_C + Event_C = C+1
```

여기서 `+`는 단순 덧셈이 아니다.

```text
+ =
relation
```

따라서 이 식은 다음을 뜻한다.

```text
Context_C
+
Event_C
=
Context와 Event가 relation을 맺어
다음 formed state인 C+1을 여는 것
```

---

## 2. Path는 요약이 아니다

Path는 Context.md와 Event.md를 요약하는 문서가 아니다.

```text
Path ≠ Context 요약 + Event 요약
```

Path는 둘 사이에서 발생하는 구조연산을 기록하는 문서다.

Context_C가 있어도 Event_C와 relation을 맺지 않으면 C+1은 열리지 않는다.

Event_C가 있어도 Context_C와 relation을 맺지 않으면 C+1은 열리지 않는다.

```text
Context_C alone ≠ C+1
Event_C alone ≠ C+1
Context_C + Event_C through relation = C+1
```

따라서 Path는 가장 중요한 작동 문서다.

---

## 3. Context_C

Path는 먼저 Context_C를 확인한다.

Context_C는 배경 설명이 아니다.

```text
Context_C =
m이 t와 p와 ? 안에서 formed 된 존재 형성장
```

Path에서 Context_C는 다음 질문으로 압축된다.

```text
이 존재는 어떤 장에서 형성되었는가?
이 존재는 어떤 시간흐름과 압력을 통과했는가?
이 존재의 선행조건은 무엇인가?
이 존재가 후대에 형성한 영향장은 무엇인가?
이 Context는 어떤 Core seat에 닿는가?
```

Path는 Context_C를 다시 쓰지 않는다.

Path는 Context_C가 Event_C와 relation을 맺는 지점을 찾는다.

---

## 4. Event_C

Path는 다음으로 Event_C를 확인한다.

Event_C는 사건 설명이 아니다.

```text
Event_C =
m이 t와 p와 ? 안에서 formed 된 구조 형성물
```

Path에서 Event_C는 다음 질문으로 압축된다.

```text
이 Event는 어떤 조건에서 formed 되었는가?
이 Event는 어떤 임계사이영역을 통과했는가?
이 Event의 구조적 특이점은 무엇인가?
이 Event가 열어 놓은 후대 영향은 무엇인가?
이 Event는 어떤 Core seat에 닿는가?
```

Path는 Event_C를 다시 쓰지 않는다.

Path는 Event_C가 Context_C와 relation을 맺는 지점을 찾는다.

---

## 5. relation은 무엇인가

Path에서 relation은 단순 연결이 아니다.

```text
relation ≠ connection only
```

relation은 사이와 차이다.

```text
relation =
사이
+
차이
```

사이는 Context_C와 Event_C가 완전히 하나로 병합되지 않고 서로를 향해 놓일 수 있게 하는 field다.

차이는 그 사이에서 드러나는 거리차, 상태차, 방향차, 해상도차, 층위차다.

```text
사이 =
between-field

차이 =
between-field 안에서 드러나는 difference
```

Path는 이 사이와 차이를 읽는다.

---

## 6. Path의 6W1H

Path는 6W1H를 가진다.

이 질문들은 단순 체크리스트가 아니다.

이 질문들은 relation을 여는 질문축이다.

```text
Who =
누가 이 relation을 보는가?

What =
무엇과 무엇의 relation인가?

When =
언제 이 relation이 열리는가?

Where =
어디에서 이 relation이 드러나는가?

Why =
왜 이 Context와 Event가 relation을 맺는가?

Which =
어느 조건과 어느 형성물 사이인가?

How =
어떻게 C+1이 열리는가?
```

Path가 6W1H를 잃으면 단순 연결표가 된다.

Path가 6W1H를 가지면 구조연산 경로가 된다.

---

## 7. ?의 위치

Path에서 `?`는 중요하다.

`?`는 관측기준이고, 경계설정이고, 관측자의 시선이다.

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

Path에서 `?`는 Context 쪽에 놓일 수도 있다.

Event 쪽에 놓일 수도 있다.

둘 사이의 사이에 놓일 수도 있다.

둘 전체를 감싸는 field에 놓일 수도 있다.

```text
? ∩ Context_C 가능
? ∩ Event_C 가능
? ∩ between 가능
? ∩ (Context_C + Event_C) 가능
```

따라서 Path는 `?`가 어디에 놓였는지 기록해야 한다.

---

## 8. 사이

Path에서 사이는 핵심이다.

Context_C와 Event_C 사이에는 반드시 between-field가 있다.

```text
Context_C
｜
between-field
｜
Event_C
```

이 사이가 없으면 Context와 Event는 서로 병합되거나, 반대로 무관한 두 덩어리로 떨어진다.

Path는 둘을 병합하지 않는다.

Path는 둘을 무관하게 두지도 않는다.

Path는 사이를 읽는다.

```text
Path =
between-field를 읽는 문서
```

---

## 9. 차이

사이에서 차이가 드러난다.

차이는 단순 다름이 아니다.

```text
차이 =
사이영역과 사이영역 사이의 거리차
```

Context_C와 Event_C 사이의 차이는 다음이 될 수 있다.

```text
시대 차이
관측기준 차이
형성조건 차이
문제의식 차이
표현방식 차이
기술조건 차이
사회장 차이
언어장 차이
후대 영향 차이
```

Path는 이 차이가 어떤 relation을 여는지 기록한다.

---

## 10. 전제조건

Path에서 전제조건은 중요하다.

전제조건은 배경이 아니다.

전제조건은 다음 Event가 formed 되기 위한 조건일 수 있다.

```text
전제조건 =
다음 formed state가 열리기 위해 먼저 놓인 조건
```

9dot0로 읽으면 다음과 같다.

```text
9 =
이전 구조의 끝점

dot =
임계사이영역

0 =
다음 시작점
```

여기서 9는 단순 끝점이 아니다.

9는 0이 시작점이 되기 위한 전제조건이다.

```text
끝점 =
다음 시작점의 전제조건
```

Path는 이 전제조건을 기록한다.

---

## 11. 임계사이영역

Path는 임계사이영역을 찾아야 한다.

임계사이영역은 Context_C와 Event_C 사이에서 다음 C+1이 열리기 직전의 압력장이다.

```text
임계사이영역 =
Context_C와 Event_C 사이에서
다음 전이가 가능해지는 between-field
```

임계사이영역은 단순 중간이 아니다.

```text
임계사이영역 =
닫힘
+
열림
+
압력
+
잠재가능성
```

Path는 이 임계사이영역이 어디서 발생하는지 묻는다.

---

## 12. 극한임계전이

극한임계전이는 임계사이영역이 다음 C+1을 여는 순간이다.

```text
극한임계전이 =
임계사이영역을 지나
C+1이 열리는 전이
```

Event / Context Path에서는 다음처럼 읽는다.

```text
Context_C
+
Event_C
→
임계사이영역
→
극한임계전이
→
C+1
```

극한임계전이는 단순 발표일, 사건일, 발생일과 같지 않을 수 있다.

날짜는 표식이다.

전이는 구조가 바뀌는 순간이다.

```text
date =
marker

transition =
structural change
```

---

## 13. 9dot0와 Path

Path는 9dot0 구조를 가진다.

```text
9 dot 0
```

Context_C와 Event_C가 만나는 사이에서 이전 구조의 끝점, 임계사이영역, 다음 시작점이 나타난다.

```text
9 =
이전 Context 또는 Event 구조의 끝점

dot =
Context와 Event 사이의 임계사이영역

0 =
C+1의 시작점
```

따라서 Path는 다음을 기록한다.

```text
어디가 9인가?
어디가 dot인가?
어디가 0인가?
```

이 판정 없이 C+1을 말하면 안 된다.

---

## 14. C+1

C+1은 Context와 Event를 합친 결과물이 아니다.

C+1은 relation으로 열린 다음 formed state다.

```text
C+1 ≠ Context 요약 + Event 요약
```

C+1은 다음이다.

```text
C+1 =
Context_C와 Event_C 사이의 relation이
임계사이영역과 극한임계전이를 지나
새로 열린 formed state
```

C+1은 다음 질문으로 판정한다.

```text
이 relation은 무엇을 새로 열었는가?
이전 C와 다른 점은 무엇인가?
어떤 Core seat가 반응했는가?
어떤 다음 Path가 열리는가?
```

---

## 15. Core 반응

Path는 Core 반응을 본다.

Context_C와 Event_C가 relation을 맺으면 특정 Core seat들이 반응할 수 있다.

예시:

```text
Context의 시간흐름
+
Event의 형성시간
→ Time-Flow Core

Context의 자리장
+
Event의 형성자리
→ Place-Field Core

Context의 다중존재
+
Event의 formed structure
→ Multi-Being Core

Context와 Event의 전이
→ 9dot0 Core

C+1 판정
→ Path / C+1 Core
```

Core 반응은 내용을 채우는 것이 아니다.

Core seat가 어떤 relation에 반응하는지 관측하는 것이다.

---

## 16. Path 문서의 기본 구조

Path 문서는 다음 골격을 가진다.

```text
# Path_[Context]_[Event].md

## 0. 문서의 자리
## 1. Context_C 확인
## 2. Event_C 확인
## 3. relation 질문
## 4. ?
## 5. 사이
## 6. 차이
## 7. 전제조건
## 8. 임계사이영역
## 9. 극한임계전이
## 10. 9dot0 판정
## 11. Core 반응
## 12. C+1 판정
## 13. 다음 Path 후보
```

이 골격은 고정 양식이 아니다.

그러나 첫 적용에서는 이 골격을 기준으로 삼는다.

---

## 17. Path 작성의 금지사항

Path 작성 시 금지사항:

```text
1. 파일경로로 쓰지 않는다.
2. Context 요약 + Event 요약으로 만들지 않는다.
3. 단순 연결표로 만들지 않는다.
4. C+1을 너무 빨리 선언하지 않는다.
5. 숫자패턴만으로 relation을 만들지 않는다.
6. Context와 Event를 병합하지 않는다.
7. Context와 Event를 무관하게 두지 않는다.
8. Core를 content table처럼 채우지 않는다.
9. 발표일과 극한임계전이를 혼동하지 않는다.
10. ?의 위치를 생략하지 않는다.
```

---

## 18. Path 작성의 허용사항

Path 작성 시 허용사항:

```text
1. Context_C와 Event_C를 각각 하나의 C로 본다.
2. 사이와 차이를 분리해 읽는다.
3. 6W1H로 relation을 연다.
4. ?의 위치를 기록한다.
5. 전제조건을 찾는다.
6. 임계사이영역을 찾는다.
7. 극한임계전이를 판정한다.
8. 9dot0 구조를 표시한다.
9. Core 반응 후보를 남긴다.
10. C+1을 formed state로 판정한다.
```

---

## 19. Path와 숫자패턴 guard

Path 작성에서도 숫자패턴을 조심한다.

비슷한 숫자를 발견했다고 해서 relation으로 확정하지 않는다.

```text
정수패턴 =
관측 후보

정수패턴 ≠ relation 증거
```

숫자 유사성은 관찰 시작점일 수는 있지만, 구조연결의 근거가 될 수 없다.

Path는 숫자 유사성이 아니라 구조적 사이와 차이와 전이로 열린다.

---

## 20. Path schema의 핵심

Path schema의 핵심은 다음이다.

```text
Path는 파일경로가 아니다.

Path는 Context_C와 Event_C가 relation을 맺어
C+1을 여는 구조연산 경로다.
```

Context는 배경이 아니다.

Event는 사건이 아니다.

Path는 연결이 아니다.

```text
Context =
존재 형성장

Event =
formed structure

Path =
relation operation
```

---

## 21. 닫힘

`event_context_path_schema.md`는 Ctp24 구조원리와 구조연산기를 실제 Event / Context 구조로 작동시키기 위한 Path schema로 작성되었다.

이 문서는 다음 판정으로 닫힌다.

```text
Path는 파일경로가 아니다.
Path는 relation path다.

Path는 Context_C와 Event_C 사이에서
사이와 차이와 ?를 읽고,
임계사이영역과 극한임계전이를 지나
C+1을 여는 구조연산 경로다.
```

---

다음회차:
Event / Context 적용 5회차

필요한 모드:
Thinking 헤비

목적:
ctp_event_context_operation_rule.md 작성
