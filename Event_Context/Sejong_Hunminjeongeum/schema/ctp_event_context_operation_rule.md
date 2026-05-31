# ctp_event_context_operation_rule.md

> 문서번호: `Ctp24_EVENT_CONTEXT_0005`  
> 상태: Event / Context 적용 5회차  
> 필요한 모드: `Thinking 헤비`  
> 목적: Ctp24 구조원리와 구조연산기를 실제 Event / Context 구조에서 작동시키기 위한 operation rule을 작성한다.  
> 위치 후보: `epluone/Event_Context/schema/ctp_event_context_operation_rule.md`

---

## 0. 이 문서의 자리

이 문서는 Event / Context 적용의 다섯 번째 문서다.

이전 문서들은 각각 다음을 정의했다.

```text
event_context_schema_overview.md
=
Event / Context 적용 전체 개요

context_schema.md
=
Context_C 형성 schema

event_schema.md
=
Event_C 형성 schema

event_context_path_schema.md
=
Context_C + Event_C = C+1 relation path schema
```

이번 문서는 그 위에서 실제 작동 규칙을 고정한다.

즉, 이 문서는 다음을 정한다.

```text
C=tp를 언제 쓰는가?
C=(m,t,p,?)를 언제 쓰는가?
Context_C와 Event_C를 어떻게 판정하는가?
Path에서 C+1을 어떻게 판정하는가?
Core_01~Core_24는 어떻게 반응하는가?
```

---

## 1. operation rule의 기본 목적

이 문서는 설명문이 아니라 작동규칙이다.

```text
operation rule =
실제 적용 때 따라야 하는 구조연산 규칙
```

Event / Context 적용에서 가장 위험한 것은 설명으로 흘러가는 것이다.

```text
위험:
Context를 배경 설명으로 만들기
Event를 사건 요약으로 만들기
Path를 연결 설명으로 만들기
Core를 내용표로 채우기
```

operation rule은 이 오독을 막는다.

---

## 2. 최상위 operation formula

Event / Context 적용의 최상위 공식은 다음이다.

```text
Context_C + Event_C = C+1
```

여기서 `+`는 단순 덧셈이 아니다.

```text
+ =
relation
```

즉:

```text
Context_C
+
Event_C
=
Context와 Event가 relation을 맺어
새로운 formed state인 C+1을 여는 구조연산
```

이 공식은 모든 Event / Context 적용의 중심이다.

---

## 3. C=tp의 역할

`C=tp`는 전체 흐름식이다.

```text
C = t p
```

여기서 `t`는 시간만이 아니다.

```text
t =
시간
+
흐름
+
전이
+
차이
+
사이
+
수평배열
```

여기서 `p`는 위치만이 아니다.

```text
p =
자리
+
field
+
fabric
+
domain
+
수직배열
```

따라서 C=tp는 다음을 뜻한다.

```text
C =
t의 흐름과 p의 자리장이 relation을 맺어
하나의 formed state가 된 것
```

Event / Context 적용에서 C=tp는 다음 경우에 사용한다.

```text
1. 전체 흐름을 볼 때
2. Context가 어떤 장 안에서 formed 되었는지 볼 때
3. Event가 어떤 조건장 안에서 formed 되었는지 볼 때
4. 세부 요소보다 흐름과 자리의 결합이 더 중요할 때
```

---

## 4. C=(m,t,p,?)의 역할

`C=(m,t,p,?)`는 C=tp를 폐기한 식이 아니다.

이 식은 C=tp를 분해하는 작동식이다.

```text
C=tp =
전체 흐름식

C=(m,t,p,?) =
분해·분석·검증·확인·의심의 순환식
```

Event / Context 적용에서 C=(m,t,p,?)는 다음 경우에 사용한다.

```text
1. 중심 m을 분리해야 할 때
2. t의 흐름을 세부적으로 검산해야 할 때
3. p의 자리장을 구체적으로 설정해야 할 때
4. ?의 관측기준과 경계를 명시해야 할 때
5. Context_C 또는 Event_C 판정이 모호할 때
6. Path에서 relation의 근거를 확인해야 할 때
```

즉, C=tp는 전체를 잡고, C=(m,t,p,?)는 검산한다.

```text
C=tp =
전체 파악

C=(m,t,p,?) =
구조 검산
```

---

## 5. Context_C 형성 rule

Context_C는 다음 조건을 만족해야 한다.

```text
Context_C =
m이 t와 p와 ? 안에서 formed 된 존재 형성장
```

Context_C 판정 전에는 다음을 확인한다.

```text
m =
중심 존재가 무엇인가?

t =
그 존재가 어떤 시간흐름과 전이를 통과했는가?

p =
그 존재가 어떤 자리장 / field / fabric / domain에 놓였는가?

? =
어떤 관측기준과 경계로 이 Context를 보는가?
```

Context_C는 다음으로 만들면 안 된다.

```text
인물 요약
배경 설명
연대기
환경 목록
족보표
```

Context_C는 존재 형성장이어야 한다.

---

## 6. Event_C 형성 rule

Event_C는 다음 조건을 만족해야 한다.

```text
Event_C =
m이 t와 p와 ? 안에서 formed 된 구조 형성물
```

Event_C 판정 전에는 다음을 확인한다.

```text
m =
Event의 중심 formed structure는 무엇인가?

t =
그 Event가 어떤 흐름과 전이를 지나 formed 되었는가?

p =
그 Event가 어떤 field / domain / condition 안에 놓였는가?

? =
어떤 관측기준과 경계로 이 Event를 보는가?
```

Event_C는 다음으로 만들면 안 된다.

```text
사건 요약
결과물 설명
발표일 기록
중요 사건 목록
단순 이론 설명
```

Event_C는 formed structure여야 한다.

---

## 7. Path_C 형성 rule

Path는 Context_C와 Event_C 사이에서 작동한다.

```text
Path =
Context_C와 Event_C 사이의 relation operation
```

Path_C라는 표현을 사용한다면, 그것은 Path 자체가 하나의 C로 formed 된 상태를 말한다.

```text
Path_C =
Context_C와 Event_C의 relation이
사이와 차이와 ? 안에서 formed 된 상태
```

Path에서 반드시 확인해야 할 항목은 다음이다.

```text
1. Context_C는 무엇인가?
2. Event_C는 무엇인가?
3. 둘 사이의 사이는 무엇인가?
4. 둘 사이의 차이는 무엇인가?
5. ?는 어디에 놓이는가?
6. 전제조건은 무엇인가?
7. 임계사이영역은 어디인가?
8. 극한임계전이는 무엇인가?
9. 어떤 Core seat가 반응하는가?
10. C+1은 무엇인가?
```

---

## 8. C+1 판정 rule

C+1은 Context와 Event의 단순 합이 아니다.

```text
C+1 ≠ Context 요약 + Event 요약
```

C+1은 relation을 통해 새로 열린 formed state다.

```text
C+1 =
Context_C와 Event_C 사이의 relation이
임계사이영역과 극한임계전이를 지나
새로 opened 된 formed state
```

C+1 판정 전에는 다음 질문에 답해야 한다.

```text
1. 이 relation이 새로 연 것은 무엇인가?
2. 이전 C와 달라진 점은 무엇인가?
3. 어떤 Core seat가 반응했는가?
4. 어떤 다음 Path 후보가 열렸는가?
5. 이 C+1은 단순 해석인가, 구조전이인가?
```

C+1을 너무 빨리 선언하면 안 된다.

```text
C+1 declaration =
마지막 판정
```

---

## 9. 9dot0 operation rule

Event / Context 적용에서 9dot0는 전이 구조다.

```text
9 dot 0
```

Path에서는 다음처럼 읽는다.

```text
9 =
이전 구조의 끝점

dot =
Context_C와 Event_C 사이의 임계사이영역

0 =
C+1의 시작점
```

9dot0 판정 전에는 다음을 확인한다.

```text
1. 무엇이 이전 구조의 끝점인가?
2. 어떤 사이영역이 dot으로 작동하는가?
3. 무엇이 다음 시작점인가?
4. 끝점은 어떤 전제조건이 되는가?
5. dot은 어떤 잠재가능성을 품는가?
```

dot은 단순 중간지점이 아니다.

```text
dot =
무한한 잠재가능성
+
임계사이영역
+
전이 압력장
```

---

## 10. ? operation rule

`?`는 모든 단계에서 필요하다.

```text
? =
6W1H
+
관측자의 시선
+
경계설정
+
해석조건
```

Event / Context 적용에서는 `?`의 위치를 반드시 기록해야 한다.

```text
? ∩ Context_C 가능
? ∩ Event_C 가능
? ∩ Path 가능
? ∩ C+1 가능
```

`?`를 생략하면 구조는 설명으로 흘러간다.

`?`를 기록하면 구조연산이 가능해진다.

---

## 11. Core reaction rule

Core_01~Core_24는 내용을 채우기 위한 칸이 아니다.

```text
Core_01~Core_24 =
content slots X
form seats O
```

Event / Context 적용에서 Core는 다음처럼 작동한다.

```text
Context_C가 닿는 Core seat
Event_C가 닿는 Core seat
Path가 열어 주는 Core ↔ Core relation
C+1에서 새로 반응하는 Core seat
```

Core reaction은 다음 방식으로 표시한다.

```text
Core reaction candidate:
- Core_01 Time-Flow Core
- Core_03 Relation Core
- Core_05 9dot0 Core
```

그러나 Core를 확정적으로 채우지 않는다.

```text
Core reaction =
관측 후보

Core content completion =
아직 아님
```

---

## 12. source rule

Event / Context 적용은 source를 필요로 한다.

그러나 source를 덮어쓰지 않는다.

```text
source =
읽을 것

output =
작성할 것
```

주요 source:

```text
seed_base/Structure_Principle/schema/
seed_base/SeungeFlow_Thinking/thinking_flow/
first_flow/navigation_map.md
epluone/BackData/
epluone/ComplexTest/
active_schema/current_rules.md
active_schema/core.meta.md
active_schema/current_path.md
```

source를 그대로 복사하지 않는다.

source에서 작동원리를 읽는다.

---

## 13. 숫자패턴 guard

정수패턴은 relation의 증거가 아니다.

```text
정수패턴 =
관측 후보

정수패턴 ≠ relation 증거
```

예를 들어 24라는 숫자가 여러 구조에서 보인다고 해서 곧바로 연결하면 안 된다.

```text
Ctp24의 24
=
Ctp24 구조 안에서 의미

24절기의 24
=
시간 / 계절 / 달력 체계 안에서 의미

훈민정음 현대 자모 24
=
현대 자모 체계 안에서 의미
```

숫자 유사성은 관찰 시작점일 수 있다.

그러나 Path는 숫자 유사성이 아니라 구조적 사이와 차이와 전이로 열어야 한다.

---

## 14. three-document operation set

Event / Context 적용은 세 문서가 하나의 operation set으로 작동한다.

```text
Context_[target].md
Event_[target].md
Path_[Context]_[Event].md
```

각 문서 역할:

```text
Context_[target].md =
Context_C 형성

Event_[target].md =
Event_C 형성

Path_[Context]_[Event].md =
Context_C + Event_C = C+1 판정
```

세 문서는 분리되어야 한다.

그러나 고립되면 안 된다.

Path가 둘을 relation으로 연결한다.

---

## 15. operation sequence

실제 적용 순서는 다음이다.

```text
1. target 후보를 정한다.
2. Context 대상과 Event 대상을 분리한다.
3. Context_C를 작성한다.
4. Event_C를 작성한다.
5. Path를 작성한다.
6. Core reaction 후보를 표시한다.
7. C+1을 판정한다.
8. 다음 Path 후보를 남긴다.
```

주의:

```text
target 선택 전에 schema를 먼저 세운다.
Context와 Event를 먼저 섞지 않는다.
Path 없이 C+1을 선언하지 않는다.
```

---

## 16. output rule

Event / Context 적용의 산출물은 다음으로 나눌 수 있다.

```text
schema output =
context_schema.md
event_schema.md
event_context_path_schema.md
ctp_event_context_operation_rule.md

application output =
Context_[target].md
Event_[target].md
Path_[Context]_[Event].md

meta output =
operation_log.md
core_reaction_log.md
next_path_candidates.md
```

처음에는 schema output을 완성한다.

그 다음 application output으로 간다.

---

## 17. 금지사항

Event / Context operation에서 금지되는 것:

```text
1. Context를 배경 요약으로 만들기
2. Event를 사건 요약으로 만들기
3. Path를 파일경로로 만들기
4. C+1을 너무 빨리 선언하기
5. Core_01~Core_24를 content table로 채우기
6. 숫자패턴으로 relation 만들기
7. source를 output으로 덮어쓰기
8. Context와 Event를 섞기
9. ?의 위치를 생략하기
10. 발표일과 극한임계전이를 혼동하기
```

---

## 18. 허용사항

Event / Context operation에서 허용되는 것:

```text
1. Context를 존재 형성장으로 작성한다.
2. Event를 formed structure로 작성한다.
3. Path를 relation operation으로 작성한다.
4. C=tp로 전체 흐름을 읽는다.
5. C=(m,t,p,?)로 세부 검산한다.
6. 9dot0로 전이구조를 읽는다.
7. Core reaction 후보를 표시한다.
8. source를 보존하며 참조한다.
9. C+1을 마지막에 판정한다.
10. 다음 Path 후보를 남긴다.
```

---

## 19. operation rule의 핵심

이 문서의 핵심은 다음이다.

```text
C=tp =
전체 흐름식

C=(m,t,p,?) =
세부 검산식

Context_C =
존재 형성장

Event_C =
구조 형성물

Path =
Context_C와 Event_C가 relation을 맺어 C+1을 여는 경로

C+1 =
relation으로 열린 다음 formed state
```

---

## 20. 닫힘

`ctp_event_context_operation_rule.md`는 Ctp24 구조원리와 구조연산기를 실제 Event / Context 구조에서 작동시키기 위한 operation rule로 작성되었다.

이 문서는 다음 판정으로 닫힌다.

```text
Event / Context 적용은 설명이 아니다.
Event / Context 적용은 구조연산이다.

C=tp는 전체 흐름을 잡고,
C=(m,t,p,?)는 구조를 검산한다.

Context_C와 Event_C는 Path를 통해 relation을 맺고,
그 relation은 C+1을 연다.
```

---

다음회차:
Event / Context 적용 6회차

필요한 모드:
Thinking 확장

목적:
first_application_candidate.md 작성
