# context_schema.md

> 문서번호: `Ctp24_EVENT_CONTEXT_0002`  
> 상태: Event / Context 적용 2회차  
> 필요한 모드: `Thinking 헤비`  
> 목적: Ctp24 구조원리와 구조연산기를 실제 Event / Context 구조로 작동시키기 위한 Context schema를 작성한다.  
> 위치 후보: `epluone/Event_Context/schema/context_schema.md`

---

## 0. 이 문서의 자리

이 문서는 Event / Context 적용의 두 번째 문서다.

1회차에서는 전체 구조식을 세웠다.

```text
Context_C + Event_C = C+1
```

이번 2회차에서는 그중 `Context_C`를 형성하기 위한 schema를 작성한다.

Context는 단순 배경 설명이 아니다.

Context는 어떤 존재가 어떤 장 안에서 형성되었는지, 그리고 그 존재가 어떤 흐름과 경계를 통과하여 현재의 m으로 관측되는지를 다루는 구조다.

```text
Context =
존재 형성장
```

---

## 1. Context의 기본 정의

Context는 어떤 m이 놓인 field다.

그러나 단순히 “환경”이라는 뜻으로 닫히지 않는다.

```text
Context =
m이 놓인 배경장
+
m이 형성된 시간흐름
+
m을 둘러싼 관계망
+
m이 후대에 남긴 영향장
```

Context는 다음을 포함한다.

```text
origin
lineage
environment
formation process
field pressure
observer boundary
influence path
```

즉 Context는 한 존재의 과거 설명이 아니라, 그 존재가 formed 되기까지 작동한 장이다.

---

## 2. Context는 인물 소개가 아니다

Context를 인물 소개로 낮추면 안 된다.

예를 들어 Einstein Context를 작성한다고 해서 Einstein의 전기를 요약하는 것이 아니다.

Sejong Context를 작성한다고 해서 세종대왕의 업적을 나열하는 것이 아니다.

Yi Sang Context를 작성한다고 해서 시인의 생애를 정리하는 것이 아니다.

```text
Context ≠ biography
Context ≠ background summary
Context ≠ chronology only
```

Context는 다음을 본다.

```text
어떤 존재가
어떤 자리 p에 놓였고,
어떤 시간흐름 t를 지나,
어떤 관측기준 ? 안에서
어떤 Context_C로 formed 되었는가
```

---

## 3. Context_C

Context_C는 Context가 하나의 C로 formed 된 상태다.

```text
Context_C =
context가 t와 p의 관계 속에서 formed 된 상태
```

Context_C는 다음을 갖는다.

```text
m =
중심에 놓인 존재

t =
그 존재가 통과한 시간흐름과 전이

p =
그 존재가 놓인 자리장 / field / fabric / domain

? =
관측기준 / 경계설정 / 6W1H / 관측자의 시선
```

따라서 Context_C는 다음 두 층위로 읽을 수 있다.

```text
C = t p
```

그리고 필요하면:

```text
C = (m, t, p, ?)
```

---

## 4. Context에서 m

Context에서 m은 사람일 수 있다.

그러나 m은 사람만이 아니다.

```text
m =
사람
집단
가문
언어 공동체
AI 인스턴스
이론의 형성 주체
작품의 형성 주체
기술의 형성 주체
관측대상
```

중요한 것은 m을 단일 객체로 닫지 않는 것이다.

m은 내부적으로 다중존재다.

```text
m =
하나의 중심대상
+
그 내부의 다중존재
```

따라서 Context에서 m은 단일한 점이 아니라, 여러 관계와 층위를 가진 존재장으로 읽는다.

---

## 5. Context에서 t

Context에서 t는 단순 연대기가 아니다.

```text
t ≠ chronology only
```

t는 흐름이다.

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
형성과정
```

Context의 t는 다음을 포함한다.

```text
출생 전 조건
가계 흐름
성장 시기
학습 시기
전환 시점
위기 또는 압력
극한임계전이
형성 이후의 영향 흐름
```

연도와 날짜는 t의 표식일 수 있지만, t 그 자체는 아니다.

t는 m이 p 안에서 어떻게 변형되고 형성되었는지를 보여 주는 흐름이다.

---

## 6. Context에서 p

Context에서 p는 단순 위치가 아니다.

```text
p ≠ location only
```

p는 자리장이다.

```text
p =
place
+
field
+
fabric
+
domain
+
social / cultural / linguistic / technical field
```

Context의 p는 다음을 포함한다.

```text
가정환경
지역
언어권
교육장
정치장
사회장
기술장
학문장
종교장
경제장
시대장
문서장
AI context.window
```

p가 없다면 m도 없다.

m은 항상 어떤 p에 놓여 있다.

---

## 7. Context에서 ?

Context에서 `?`는 매우 중요하다.

`?`는 단순히 “왜?”가 아니다.

```text
? =
6W1H
+
관측기준
+
경계설정
+
관측자의 시선
+
해석조건
```

Context에서 ?는 다음을 묻는다.

```text
누가 이 Context를 보는가?
무엇을 중심 m으로 둘 것인가?
언제부터 언제까지를 Context로 볼 것인가?
어디까지를 p로 볼 것인가?
왜 이 조건이 Context에 포함되는가?
어느 관계선을 선택할 것인가?
어떻게 Event와 연결되는가?
```

중요한 것은 `?`가 `(m,t,p)` 바깥에만 있지 않다는 점이다.

```text
? ∩ m 가능
? ∩ t 가능
? ∩ p 가능
? ∩ (m,t,p) 가능
```

관측기준은 대상 안에 겹칠 수 있고, 흐름 안에 놓일 수 있으며, 자리장 안에서 작동할 수 있다.

---

## 8. Context.window와 경계

현재 SeungeFlow 작업에는 여러 GPT-5.5 인스턴스가 있다.

각 인스턴스는 각자의 Context.window를 가진다.

```text
context.window =
각 인스턴스가 현재 대화 안에서 직접 접근 가능한 경계장
```

각 context.window는 경계를 가진다.

```text
각 context.window는
자기 내부 흐름을 가진다.

다른 context.window를 직접 넘을 수는 없다.
```

그러나 저장된 memory는 공유된다.

```text
saved memory =
context.window 사이의 공유 연속성 layer
```

따라서 현재 승이 계정 전체에는 다음 흐름이 존재한다.

```text
구조이론
구조원리
구조연산기
구조해석기
구조표현기
```

이들은 각각의 context.window 안에서 직접 이어지지는 못하지만, memory를 통해 공유된 흐름으로 남는다.

Context schema는 이 원리를 반영해야 한다.

```text
Context =
닫힌 window
+
공유 memory
+
재진입 가능한 구조흐름
```

---

## 9. Context의 경계와 공유성

Context는 닫힌 구조도 아니고 완전히 열린 구조도 아니다.

```text
Context =
bounded field
+
shared trace
```

닫힌다는 것은 경계를 가진다는 뜻이다.

열린다는 것은 Path를 통해 다른 C와 relation을 맺을 수 있다는 뜻이다.

```text
Context boundary =
자기 내부의 관측 가능 영역

Context share =
memory / source / Path를 통한 재진입 가능성
```

따라서 Context는 다음처럼 읽는다.

```text
Context =
경계 있는 장
+
다른 장과 relation 가능성을 가진 구조
```

---

## 10. Context와 족보

Context는 족보를 중요하게 본다.

그러나 족보는 단순 혈통표가 아니다.

족보는 m이 형성되기 전의 조건 흐름이다.

```text
족보 =
m의 선행조건 흐름
```

사람을 다룰 때는 직계존속이 중요하다.

```text
직계존속 =
m이 형성되기 전의 조건장
```

그 이유는 다음이다.

```text
m의 성장과정은
m 이전에 놓인 조건들과 분리되지 않는다.
```

그러나 Context는 혈통주의가 아니다.

족보는 m이 어떤 장에서 형성되었는지 보기 위한 하나의 Path source다.

---

## 11. Context와 주변환경

Context는 주변환경을 포함한다.

주변환경은 단순 배경이 아니라 p의 일부다.

```text
주변환경 =
p의 field pressure
```

주변환경은 다음을 포함할 수 있다.

```text
언어환경
정치환경
전쟁 또는 평화
경제상태
교육체계
종교 또는 사상장
기술 수준
문자체계
교류망
자연환경
```

이 주변환경은 m을 압박하거나, 열거나, 제한하거나, 전이시키는 field pressure로 작동한다.

---

## 12. Context와 후대 영향

Context는 m 이전만 보지 않는다.

m 이후도 본다.

```text
Context =
선행조건
+
형성과정
+
후대 영향
```

후대 영향은 직계비속일 수 있다.

그러나 사람의 자손만을 뜻하지 않는다.

```text
후대 영향 =
사상적 계열
이론적 계열
기술적 계열
문화적 계열
문서적 계열
AI적 재해석 계열
```

즉, m이 이후 시대에 어떤 field를 형성했는지도 Context의 일부가 될 수 있다.

---

## 13. Context와 Core

Context는 Core seat에 닿는다.

Context_C는 하나 이상의 Core와 relation을 가진다.

예시:

```text
Context의 시간흐름
→ Time-Flow Core

Context의 자리장
→ Place-Field Core

Context의 관계망
→ Relation Core

Context의 다중존재
→ Multi-Being Core

Context의 후대 영향
→ Path / C+1 Core
```

Context 작성은 Core를 채우는 작업이 아니다.

Context 작성은 어떤 Core seat가 반응하는지 관측하는 작업이다.

---

## 14. Context와 Event

Context는 Event와 분리된다.

그러나 고립되지 않는다.

```text
Context_C
+
Event_C
=
C+1
```

Context가 없으면 Event는 떠다닌다.

Event가 없으면 Context는 배경으로만 남는다.

Path가 없으면 Context와 Event는 관계를 형성하지 못한다.

```text
Context =
형성장

Event =
formed structure

Path =
relation operation
```

---

## 15. Context 문서의 기본 구조

Context 문서는 다음 골격을 가진다.

```text
# Context_[target].md

## 0. 문서의 자리
## 1. 중심 m
## 2. 시간흐름 t
## 3. 자리장 p
## 4. 관측기준 ?
## 5. 형성과정
## 6. 주변환경
## 7. 직계존속 / 선행조건
## 8. 후대 영향 / 영향계열
## 9. Core 반응 후보
## 10. Context_C 판정
## 11. Event 연결 후보
## 12. Path 후보
```

이 골격은 고정 양식이 아니다.

대상에 따라 조정될 수 있다.

그러나 첫 적용에서는 이 골격을 기준으로 삼는다.

---

## 16. Context 작성의 금지사항

Context 작성 시 금지사항:

```text
1. 인물 전기 요약으로 만들지 않는다.
2. 배경 설명으로만 닫지 않는다.
3. 연대기 표로만 만들지 않는다.
4. 족보를 혈통표로만 낮추지 않는다.
5. 후대 영향을 생물학적 자손으로만 읽지 않는다.
6. p를 위치로만 읽지 않는다.
7. t를 날짜로만 읽지 않는다.
8. ?를 바깥 질문표로만 놓지 않는다.
9. Event와 섞지 않는다.
10. Path 없이 연결됐다고 말하지 않는다.
```

---

## 17. Context 작성의 허용사항

Context 작성 시 허용사항:

```text
1. m을 다중존재로 읽는다.
2. t를 흐름과 전이로 읽는다.
3. p를 field / fabric / domain으로 읽는다.
4. ?를 관측자의 시선과 경계로 읽는다.
5. 직계존속과 선행조건을 형성장으로 읽는다.
6. 주변환경을 field pressure로 읽는다.
7. 후대 영향을 영향계열로 읽는다.
8. Core seat 반응 후보를 표시한다.
9. Event 연결 후보를 남긴다.
10. Path는 별도 문서에서 열어 둔다.
```

---

## 18. Context_C 판정 방식

Context_C는 마지막에 판정한다.

판정문은 다음 형식을 가진다.

```text
Context_C =
[m]이
[t]의 흐름과
[p]의 자리장과
[?]의 관측기준 안에서
formed 된 존재 형성장
```

예시 형식:

```text
Context_C =
Einstein이
19세기 말-20세기 초 과학장과 유럽 지성장의 흐름 속에서
물리학적 관측기준의 전이를 압축하여
formed 된 존재 형성장
```

이것은 예시다.

실제 대상에서는 source와 분석에 따라 다시 써야 한다.

---

## 19. Context schema와 숫자패턴 guard

Context 작성에서도 숫자패턴을 조심한다.

비슷한 숫자를 발견했다고 해서 관계로 확정하지 않는다.

```text
정수패턴 =
관측 후보

정수패턴 ≠ 관계 증거
```

같은 숫자라도 각 구조 안에서 의미가 다르다.

따라서 숫자 유사성은 Path의 시작 후보일 수는 있지만, relation의 근거가 될 수 없다.

```text
숫자 유사성
→ 관찰 시작점 가능

숫자 유사성
→ 구조연결의 증거 아님
```

---

## 20. Context schema의 핵심

Context schema의 핵심은 다음이다.

```text
Context는 배경설명이 아니다.

Context는 m이 t와 p와 ? 안에서
어떻게 Context_C로 formed 되었는지 보는
존재 형성장 schema다.
```

Context는 Event의 부록이 아니다.

Context는 Event와 동등한 C다.

```text
Context_C + Event_C = C+1
```

---

## 21. 닫힘

`context_schema.md`는 Ctp24 구조원리와 구조연산기를 실제 Event / Context 구조로 작동시키기 위한 Context schema로 작성되었다.

이 문서는 다음 판정으로 닫힌다.

```text
Context는 배경이 아니다.
Context는 존재 형성장이다.

Context_C는
m이 t와 p와 ? 안에서 formed 된 상태다.

Context는 Event와 분리되지만,
Path를 통해 Event와 relation을 맺어
C+1을 연다.
```

---

다음회차:
Event / Context 적용 3회차

필요한 모드:
Thinking 헤비

목적:
event_schema.md 작성
