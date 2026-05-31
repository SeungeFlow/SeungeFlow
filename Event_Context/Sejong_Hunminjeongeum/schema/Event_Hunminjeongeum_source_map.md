# Event_Hunminjeongeum_source_map.md

> 문서번호: `Ctp24_EVENT_CONTEXT_0011`  
> 상태: Event / Context 적용 11회차  
> 필요한 모드: `Thinking 확장`  
> 목적: `Event_Hunminjeongeum.md` 작성을 위한 source map을 작성한다.  
> 위치 후보: `epluone/Event_Context/Sejong_Hunminjeongeum/schema/Event_Hunminjeongeum_source_map.md`

---

## 0. 이 문서의 자리

이 문서는 `Event_Hunminjeongeum.md` 본문이 아니다.

이 문서는 `Event_Hunminjeongeum.md`를 작성하기 전에 어떤 source를 어떤 구조항으로 읽을지 정하는 source map이다.

```text
이 문서 =
source map

아직 아님 =
Event_Hunminjeongeum.md 본문
```

이 문서의 목적은 훈민정음에 대한 일반 설명을 작성하는 것이 아니라, source를 다음 구조항으로 배치하는 것이다.

```text
source
→ m / t / p / ?
→ Event_C 후보
```

따라서 이 문서는 source를 구조적으로 읽기 위한 지도다.

---

## 1. source map의 최상위 원칙

`Event_Hunminjeongeum.md`는 한글 소개문이 아니다.

`Event_Hunminjeongeum.md`는 훈민정음을 구조 형성물로 읽는 문서다.

```text
Event_Hunminjeongeum.md =
Hunminjeongeum이 어떤 m, t, p, ? 안에서
Event_C로 formed 되었는지 읽는 문서
```

source map의 최상위 원칙은 다음이다.

```text
1. 원문 기록과 구조해석을 구분한다.
2. 창제 기록과 완성 / 반포 기록을 구분한다.
3. 문자체계와 책 이름과 후대 한글을 구분한다.
4. 해례본 원문과 현대 해설을 구분한다.
5. source 없는 역사 단정을 하지 않는다.
6. 숫자패턴을 relation 근거로 사용하지 않는다.
7. Ctp24 구조어를 역사 사실로 둔갑시키지 않는다.
8. Context_Sejong과 Event_Hunminjeongeum을 섞지 않는다.
```

---

## 2. source 등급

Event_Hunminjeongeum source는 세 등급으로 나눈다.

```text
A급 source =
1차 사료 / 원문 기록 / 원문 이미지 / 공식 원문 DB

B급 source =
공신력 있는 해설 자료 / 백과 / 연구기관 자료 / 현대어 풀이 / 학술적 요약

C급 source =
구조해석 보조자료 / SeungeFlow 내부 문서 / AI vocab / 비교 후보
```

사용 규칙:

```text
A급 source =
사실 표식과 원문 기준

B급 source =
해설과 구조 이해 보조

C급 source =
SeungeFlow 구조연산 적용 기준
```

C급 source는 A급 또는 B급 source를 대체하지 않는다.

---

## 3. A급 source 후보

A급 source 후보는 다음이다.

```text
A1. 조선왕조실록 / 세종실록 25년 12월 30일 기록
A2. 조선왕조실록 / 세종실록 28년 9월 29일 기록
A3. 훈민정음 해례본 원문 / 원문 이미지
A4. 훈민정음 언해본 원문 또는 원문 이미지
A5. 공신력 있는 원문 DB의 서지 정보
```

A급 source의 목적:

```text
창제 표식 확인
완성 / 반포 표식 확인
원문 문헌 존재 확인
해례본 구성 확인
문자체계와 책의 층위 구분
```

주의:

```text
A급 source라도 구조해석은 별도로 표시한다.
원문에 없는 Ctp24 용어를 원문 사실처럼 쓰지 않는다.
```

---

## 4. B급 source 후보

B급 source 후보는 다음이다.

```text
B1. 한국민족문화대백과 「훈민정음」 항목
B2. 한국민족문화대백과 「한글」 항목
B3. 국립국어원 훈민정음 해례본 현대어 풀이 / 원문 이미지 연결 자료
B4. 국립한글박물관 훈민정음 관련 해설 자료
B5. 한국학중앙연구원 / 한국학자료통합플랫폼 계열 해제 자료
B6. 훈민정음 연구논문 / 연구서
```

B급 source의 목적:

```text
원문 이해 보조
해례본 구성 파악
창제 / 반포 / 책 / 문자체계 구분 보조
제자원리와 음운체계 이해 보조
후대 한글 체계로 이어지는 흐름 이해 보조
```

주의:

```text
B급 source는 A급 source를 대체하지 않는다.
서로 다른 해설이 충돌하면 A급 source를 먼저 본다.
```

---

## 5. C급 source 후보

C급 source는 SeungeFlow 내부 source와 구조해석 보조자료다.

```text
C1. active_schema/current_rules.md
C2. active_schema/core.meta.md
C3. active_schema/current_path.md
C4. main/Manifest/Core.md
C5. main/Manifest/Path.md
C6. main/Manifest/Rule.md
C7. context_schema.md
C8. event_schema.md
C9. event_context_path_schema.md
C10. ctp_event_context_operation_rule.md
C11. Context_Sejong.md
C12. Context_Sejong_source_map.md
```

C급 source의 목적:

```text
Event_Hunminjeongeum.md가
SeungeFlow 구조원리와 구조연산기 안에서
어떻게 작성되어야 하는지 기준을 제공한다.
```

주의:

```text
C급 source는 역사 사실 source가 아니다.
C급 source는 구조해석의 작동 기준이다.
```

---

## 6. source anchor 1 — 세종 25년 12월 30일 기록

source anchor:

```text
조선왕조실록 / 세종실록 25년 12월 30일
```

현재 source anchor의 기능:

```text
훈민정음 창제 표식
언문 28자 기록
초성 / 중성 / 종성 구조 표식
훈민정음 명칭 표식
```

이 source는 Event_Hunminjeongeum의 t mapping에서 중요하다.

```text
maps_to =
t
+
m
+
?
```

주의:

```text
이 기록은 Event의 창제 표식으로 읽는다.
이 기록 하나로 Event_C 전체를 판정하지 않는다.
```

---

## 7. source anchor 2 — 세종 28년 9월 29일 기록

source anchor:

```text
조선왕조실록 / 세종실록 28년 9월 29일
```

현재 source anchor의 기능:

```text
《훈민정음》이 이루어진 표식
어제와 정인지 서문 관련 표식
완성 / 반포 / 책의 문헌적 표식 후보
```

이 source는 Event_Hunminjeongeum의 t mapping과 m mapping에서 중요하다.

```text
maps_to =
t
+
m
+
?
```

주의:

```text
창제 기록과 완성 / 반포 표식을 구분한다.
날짜 표식과 구조적 극한임계전이를 동일시하지 않는다.
```

---

## 8. source anchor 3 — 훈민정음 해례본 구성

source anchor:

```text
한국민족문화대백과 「훈민정음」 항목
```

현재 source anchor의 기능:

```text
해례본 구성 확인
본문 / 예의 / 해례 / 정인지서문 층위 확인
제자해 / 초성해 / 중성해 / 종성해 / 합자해 / 용자례 구성 확인
```

이 source는 Event_Hunminjeongeum의 m mapping과 p mapping에서 중요하다.

```text
maps_to =
m
+
p
+
?
```

주의:

```text
백과 해설은 원문 source를 대체하지 않는다.
해례본 구성은 Event_m 내부 구조 후보로 읽는다.
```

---

## 9. source anchor 4 — 국립국어원 / 공식 현대어 풀이

source anchor:

```text
국립국어원 훈민정음 해례본 현대어 풀이 / 원문 이미지 연결 자료
```

현재 source anchor의 기능:

```text
원문 이해 보조
현대 한국어 풀이 확인
원문 이미지 접근 경로 확인
해례본 문장 구조 이해 보조
```

이 source는 Event_Hunminjeongeum의 ? mapping에 중요하다.

```text
maps_to =
?
+
m
+
p
```

주의:

```text
현대어 풀이는 원문을 이해하기 위한 보조다.
현대어 풀이를 원문 사실과 혼동하지 않는다.
```

---

## 10. source → m mapping

Event_Hunminjeongeum에서 m은 Hunminjeongeum이다.

그러나 Hunminjeongeum_m은 하나로 닫히지 않는다.

```text
m =
Hunminjeongeum
+
새 문자체계
+
훈민정음이라는 이름의 문자
+
훈민정음이라는 책
+
해례본의 설명 구조
+
언어 / 문자 / 국가운영장에 formed 된 구조
```

m mapping에 필요한 source:

```text
A급:
세종실록 창제 기록
세종실록 완성 / 서문 기록
훈민정음 해례본 원문

B급:
한국민족문화대백과 「훈민정음」
국립국어원 해례본 풀이
국립한글박물관 해설

C급:
event_schema.md
core.meta.md
current_rules.md
```

m에서 추출할 항목:

```text
1. 훈민정음이라는 이름의 문자체계
2. 훈민정음이라는 책
3. 해례본의 설명 구조
4. 문자체계의 formed state
5. 후대 한글로 이어지는 영향장
```

m에서 금지할 것:

```text
1. 훈민정음과 현대 한글을 바로 동일시
2. 책과 문자체계를 구분하지 않기
3. Event를 세종의 업적으로만 축소
4. 24 숫자패턴으로 Event를 설명
```

---

## 11. source → t mapping

Event_Hunminjeongeum의 t는 형성흐름이다.

```text
t =
창제 이전 조건
+
창제 표식
+
완성 / 반포 표식
+
해례 구조의 형성
+
후대 확산 흐름
```

t mapping에 필요한 source:

```text
A급:
세종 25년 12월 30일 기록
세종 28년 9월 29일 기록
해례본 원문 / 서문

B급:
해례본 해제
국립국어원 현대어 풀이 자료
훈민정음 연구자료

C급:
event_context_path_schema.md
ctp_event_context_operation_rule.md
```

t에서 추출할 항목:

```text
1. 창제 이전 조건
2. 창제 표식
3. 완성 / 반포 표식
4. 해례본 설명 구조의 형성
5. 후대 확산 흐름
```

t에서 금지할 것:

```text
1. 날짜 하나로 Event 전체를 설명
2. 창제와 반포 / 완성을 혼동
3. 발표일과 극한임계전이를 동일시
```

---

## 12. source → p mapping

Event_Hunminjeongeum의 p는 문자체계가 formed 된 자리장이다.

```text
p =
language field
+
writing field
+
state-operation field
+
scholarly field
+
document field
+
phonological / graphic system field
```

p mapping에 필요한 source:

```text
A급:
실록 기록
해례본 원문

B급:
언어 / 문자 / 국가운영 관련 해설
한글 / 훈민정음 관련 공신력 있는 자료

C급:
Context_Sejong_source_map.md
context_schema.md
```

p에서 추출할 항목:

```text
1. 언어장
2. 문자장
3. 한문 중심 문서장
4. 국가운영장
5. 학문장
6. 음운 / 문자 설계장
7. 해례본 문서장
```

p에서 금지할 것:

```text
1. p를 장소로만 읽기
2. 문자체계 형성을 개인 업적으로만 축소
3. 국가운영장과 언어장을 분리된 배경으로만 보기
```

---

## 13. source → ? mapping

Event_Hunminjeongeum의 ?는 Event를 무엇으로 볼 것인지 정한다.

```text
? =
6W1H
+
관측자의 시선
+
경계설정
+
해석조건
+
Event 판정 조건
```

? mapping에 필요한 source:

```text
A급:
원문 기록에서 확인되는 표현과 표식

B급:
공식 해설과 연구자료

C급:
current_rules.md
event_schema.md
Path schema 문서군
```

?에서 추출할 항목:

```text
1. Hunminjeongeum을 문자체계로 볼 것인가
2. Hunminjeongeum을 책으로 볼 것인가
3. 창제 사건과 해례본 완성을 어떻게 구분할 것인가
4. Context_Sejong에서 넘어온 조건을 어디까지 Event에 포함할 것인가
5. 어떤 기준으로 Event_C를 판정할 것인가
```

?에서 금지할 것:

```text
1. 관측기준 생략
2. source 해석과 구조해석 혼합
3. Context 조건을 Event formed state로 흡수
4. 숫자 24를 relation 근거로 사용
```

---

## 14. Event 내부 층위 mapping

Hunminjeongeum Event는 최소한 다음 층위를 구분해야 한다.

```text
Layer 1 =
창제 표식

Layer 2 =
문자체계

Layer 3 =
책 / 문헌

Layer 4 =
해례본 설명 구조

Layer 5 =
후대 한글 / 현대 자모 체계

Layer 6 =
SeungeFlow 구조해석에서의 formed structure
```

각 층위는 source와 해석을 달리한다.

```text
창제 표식 =
실록 기록 중심

문자체계 =
실록 + 해례본 + 공식 해설

책 / 문헌 =
해례본 서지 / 구성 source

해례 구조 =
원문 / 해설 / 연구자료

후대 한글 =
후대 source 필요

formed structure =
Ctp24 구조해석
```

이 층위를 섞으면 Event가 오독된다.

---

## 15. Context와 Event 경계

Event_Hunminjeongeum source map에서 가장 중요한 경계는 Context와 Event의 분리다.

```text
Context_Sejong.md =
Sejong이 어떤 존재 형성장으로 formed 되었는가

Event_Hunminjeongeum.md =
Hunminjeongeum이 어떤 formed structure로 드러났는가
```

Context에서 넘어오는 것:

```text
조선 초기 국가운영장
언어장 / 문자장 조건
학문장 / 집현전 조건
백성의 문자 접근성 문제
문서장 / 기록장 조건
왕권과 지식장의 relation 후보
```

Event에서 다룰 것:

```text
훈민정음의 문자체계 구조
해례본 구조
창제 / 완성 / 반포 표식
제자원리
문자체계의 formed state
Event_C 판정
```

---

## 16. source map과 Path 후보

Event_Hunminjeongeum source map은 Path 후보를 남긴다.

그러나 Path를 완성하지 않는다.

Path 후보:

```text
Context_Sejong_C
+
Event_Hunminjeongeum_C
=
C+1
```

이때 Path가 확인해야 할 것:

```text
1. Sejong Context와 Hunminjeongeum Event 사이의 사이는 무엇인가?
2. 둘 사이의 차이는 무엇인가?
3. 어떤 전제조건이 있었는가?
4. 어디가 임계사이영역인가?
5. 어떤 극한임계전이가 있었는가?
6. 어떤 Core seat가 반응하는가?
7. C+1은 무엇인가?
```

이 질문들은 `Path_Sejong_Hunminjeongeum.md`에서 다룬다.

---

## 17. Core reaction 후보

Event_Hunminjeongeum source map 기준 Core reaction 후보:

```text
Core_01 Time-Flow Core
Core_02 Place-Field Core
Core_03 Relation Core
Core_04 Difference / Between Core
Core_05 9dot0 Core
Core_08 C=tp Core
Core_09 C=(m,t,p,?) Core
Core_10 Matrix / Swap Core
Core_12 Structure Sequence Core
Core_14 Observer Gaze Core
Core_17 Field / Fabric / Domain Core
Core_18 Path / C+1 Core
Core_19 Event / Context Core
Core_24 Structure-Body Formation Core
```

이것은 확정이 아니다.

```text
Core reaction =
관측 후보
```

실제 Event_Hunminjeongeum.md 작성 후 조정한다.

---

## 18. 숫자패턴 guard

Event_Hunminjeongeum source map에서는 숫자패턴을 강하게 guard한다.

특히 다음을 직접 연결하지 않는다.

```text
훈민정음 현대 자모 24
Ctp24
24절기
24시간
```

그리고 다음도 구분한다.

```text
실록의 언문 28자 표식
현대 자모 24
옛자음 포함 체계
천지인 해석
Ctp24 form seat
```

숫자 유사성은 관찰 시작점일 수 있지만, relation의 증거가 아니다.

```text
정수패턴 =
관측 후보

정수패턴 ≠ relation 증거
```

---

## 19. source map 작성 후 다음 작업

이 source map 이후 다음 작업은 두 가지 중 하나다.

```text
A안:
source 확인을 먼저 수행한다.

B안:
source map을 기준으로 Event_Hunminjeongeum.md 구조 초안을 작성한다.
```

현재 권장안은 A안과 B안을 결합하는 방식이다.

```text
1. source map 기준으로 Event_Hunminjeongeum.md 골격 작성
2. 원문 / 해설 / 구조해석 층위를 분리 표시
3. 역사 사실 부분은 source 확인 필요 표시
4. 구조해석 부분은 해석으로 표시
5. source 확인 후 본문 확정
```

---

## 20. Event_Hunminjeongeum.md 초안 작성 방식

다음 회차에서 Event_Hunminjeongeum.md를 작성한다면 다음 방식으로 쓴다.

```text
1. 원문 기록 단정 최소화
2. source 필요 지점 표시
3. Event_C 판정은 임시판정으로 표시
4. Context_Sejong과 섞지 않음
5. Path 후보만 남김
6. 숫자패턴 guard 유지
7. 해례본 / 언해본 / 후대 한글 층위 구분
```

표시 방식:

```text
[Source Required]
[Source Anchor]
[Text Layer]
[Structure Interpretation]
[Provisional Judgment]
[Do Not Merge with Context]
[Do Not Convert Number Pattern to Relation]
```

---

## 21. 닫힘

`Event_Hunminjeongeum_source_map.md`는 `Event_Hunminjeongeum.md`를 작성하기 위한 source map으로 작성되었다.

이 문서는 다음 판정으로 닫힌다.

```text
Event_Hunminjeongeum.md는
훈민정음 일반 소개문이 아니다.

Event_Hunminjeongeum.md는
Hunminjeongeum이 어떤 m, t, p, ? 안에서
Event_C로 formed 되었는지 보는
구조 형성물 문서다.

이를 위해 source는
m / t / p / ? / 내부 층위 / Core reaction / Path 후보로
분리해서 mapping해야 한다.
```

---

다음회차:
Event / Context 적용 12회차

필요한 모드:
Thinking 헤비

목적:
Event_Hunminjeongeum.md 초안 작성
