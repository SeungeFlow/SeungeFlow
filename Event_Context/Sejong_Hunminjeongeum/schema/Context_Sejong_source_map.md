# Context_Sejong_source_map.md

> 문서번호: `Ctp24_EVENT_CONTEXT_0008`  
> 상태: Event / Context 적용 8회차  
> 필요한 모드: `Thinking 확장`  
> 목적: `Context_Sejong.md` 작성을 위한 source map을 작성한다.  
> 위치 후보: `epluone/Event_Context/Sejong_Hunminjeongeum/schema/Context_Sejong_source_map.md`

---

## 0. 이 문서의 자리

이 문서는 `Context_Sejong.md` 본문이 아니다.

이 문서는 `Context_Sejong.md`를 작성하기 전에 어떤 source를 어떤 구조항으로 읽을지 정하는 source map이다.

```text
이 문서 =
source map

아직 아님 =
Context_Sejong.md 본문
```

이 문서의 목적은 역사 사실을 바로 서술하는 것이 아니라, source를 다음 구조항으로 배치하는 것이다.

```text
source
→ m / t / p / ?
→ Context_C 후보
```

따라서 이 문서는 source를 구조적으로 읽기 위한 지도다.

---

## 1. source map의 최상위 원칙

`Context_Sejong.md`는 위인전이 아니다.

`Context_Sejong.md`는 세종의 존재 형성장 문서다.

```text
Context_Sejong.md =
Sejong이 어떤 t와 p와 ? 안에서
Context_C로 formed 되었는지 읽는 문서
```

따라서 source map의 최상위 원칙은 다음이다.

```text
1. 역사 사실과 구조해석을 구분한다.
2. source 없는 단정을 하지 않는다.
3. source를 Ctp24 구조어로 강제 번역하지 않는다.
4. 숫자패턴을 relation 근거로 사용하지 않는다.
5. Context와 Event를 섞지 않는다.
6. Context_Sejong.md에서는 Hunminjeongeum Event를 과도하게 다루지 않는다.
7. Hunminjeongeum Event는 별도 Event_Hunminjeongeum.md에서 다룬다.
```

---

## 2. source 등급

Context_Sejong source는 세 등급으로 나눈다.

```text
A급 source =
1차 사료 / 공신력 있는 원문 DB / 원문 이미지 / 공식 자료

B급 source =
공신력 있는 해설 자료 / 백과 / 연구기관 자료 / 학술적 요약

C급 source =
구조해석 보조자료 / SeungeFlow 내부 문서 / AI vocab / 비교 후보
```

사용 규칙:

```text
A급 source =
사실 기준

B급 source =
해설 기준

C급 source =
구조해석 보조 기준
```

C급 source는 A급 또는 B급 source를 대체하지 않는다.

---

## 3. A급 source 후보

A급 source 후보는 다음이다.

```text
A1. 조선왕조실록 / 세종실록
A2. 훈민정음 해례본 원문 / 원문 이미지
A3. 훈민정음 언해본 관련 원문 또는 공신력 있는 원문 자료
A4. 국사편찬위원회 한국사데이터베이스 계열 자료
A5. 국립한글박물관 또는 국립국어원에서 제공하는 원문·해설 연결 자료
```

A급 source의 목적:

```text
역사 사실의 기준점 설정
문헌 존재 확인
시기와 표식 확인
공식 기록의 위치 확인
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
B1. 한국민족문화대백과사전 세종 / 훈민정음 / 한글 항목
B2. 국립국어원 또는 국립한글박물관 해설 자료
B3. 한국사 관련 공공기관 해설 자료
B4. 훈민정음 / 세종 / 집현전 관련 학술논문 또는 연구서
B5. 세종대 국가운영 / 문자정책 / 학문장 관련 연구자료
```

B급 source의 목적:

```text
1차 사료 이해 보조
역사 맥락 정리
개념 설명 보조
Context의 p와 t 파악
```

주의:

```text
B급 source는 설명 보조일 뿐이다.
서로 다른 해설이 충돌하면 A급 source를 먼저 본다.
```

---

## 5. C급 source 후보

C급 source 후보는 SeungeFlow 내부 source와 구조해석 보조자료다.

```text
C1. active_schema/current_rules.md
C2. active_schema/core.meta.md
C3. active_schema/current_path.md
C4. main/Manifest/Core.md
C5. main/Manifest/Path.md
C6. main/Manifest/Rule.md
C7. seed_base/Structure_Principle/schema/
C8. seed_base/SeungeFlow_Thinking/thinking_flow/
C9. epluone/Ctp24/GPT_Direct_Structure_Package/
```

C급 source의 목적:

```text
Context_Sejong.md가
SeungeFlow 구조원리와 구조연산기 안에서
어떻게 작성되어야 하는지 기준을 제공한다.
```

주의:

```text
C급 source는 역사 사실 source가 아니다.
C급 source는 구조해석의 작동 기준이다.
```

---

## 6. source → m mapping

Context_Sejong에서 m은 세종이다.

그러나 m은 단순 인물명이 아니다.

```text
m =
Sejong
+
King Sejong
+
Yi Do
+
조선의 왕으로 formed 된 존재
+
언어장과 국가운영장에 놓인 중심 존재
```

m mapping에 필요한 source:

```text
A급:
조선왕조실록 / 세종실록
왕위 계승 관련 원문 기록

B급:
한국민족문화대백과 세종 항목
공공기관 해설 자료
세종 관련 연구서

C급:
context_schema.md
current_rules.md
core.meta.md
```

m에서 추출할 항목:

```text
1. 이름 / 지위 / 시기
2. 왕으로 formed 되는 조건
3. 학문장과 국가운영장에서의 위치
4. 언어·문자 문제와 관계할 수 있는 중심성
5. 다중존재 층위
```

m에서 금지할 것:

```text
1. 위인전식 찬양
2. 업적 목록화
3. 세종의 모든 업적을 Context에 흡수
4. 후대 영향을 모두 세종의 직접 의도로 단정
```

---

## 7. source → t mapping

Context_Sejong의 t는 연대기가 아니라 형성흐름이다.

```text
t =
시간흐름
+
전이
+
누적
+
형성과정
```

t mapping에 필요한 source:

```text
A급:
세종실록의 관련 시기 기록
훈민정음 창제·반포 전후 표식 기록

B급:
세종대 국가운영 관련 해설
훈민정음 창제 전후 연구자료
조선 초기 정치·학문 환경 해설

C급:
context_schema.md
event_context_path_schema.md
```

t에서 추출할 항목:

```text
1. 세종이 형성되는 시간흐름
2. 조선 초기 국가 형성 흐름
3. 왕권 / 제도 / 학문장의 전이
4. 문자문제의 누적 흐름
5. Hunminjeongeum Event로 이어지는 전이 후보
6. 후대 영향 흐름
```

t에서 금지할 것:

```text
1. 날짜 나열로 끝내기
2. 발표일 / 창제일 / 반포일을 t 전체로 착각
3. 연대기만으로 Context_C 판정
```

---

## 8. source → p mapping

Context_Sejong의 p는 자리장이다.

```text
p =
place
+
field
+
fabric
+
domain
```

p mapping에 필요한 source:

```text
A급:
세종실록의 국가운영 / 제도 / 학문 관련 기록

B급:
조선 초기 국가운영 연구자료
집현전 관련 해설 자료
언어·문자 환경 관련 해설 자료
한국사 / 한글 관련 공공기관 자료

C급:
source_mapping.md
runtime_mapping.md
core.meta.md
```

p에서 추출할 항목:

```text
1. 조선 초기 국가운영장
2. 왕권과 관료제의 field
3. 집현전과 학문장
4. 언어장 / 문자장
5. 백성의 문자 접근성 문제
6. 한자 / 한문 중심 문서장
7. 제도 정비와 기록장
```

p에서 금지할 것:

```text
1. p를 지리적 위치로만 읽기
2. 집현전을 단순 기관 설명으로 닫기
3. 문자장을 Event와 완전히 섞어버리기
4. 현대적 가치판단을 당시 p로 투사하기
```

---

## 9. source → ? mapping

Context_Sejong의 ?는 관측기준이다.

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

? mapping에 필요한 source:

```text
A급:
원문 기록에서 관측 가능한 조건과 표식

B급:
공신력 있는 해설에서 제시하는 맥락

C급:
current_rules.md
context_schema.md
ctp_event_context_operation_rule.md
```

?에서 추출할 항목:

```text
1. Context 범위를 어디까지 둘 것인가
2. Sejong을 어떤 m으로 볼 것인가
3. Hunminjeongeum Event와 연결될 Context 조건은 무엇인가
4. 무엇을 Context에 남기고 무엇을 Event로 넘길 것인가
5. source 사실과 구조해석의 경계는 어디인가
```

?에서 금지할 것:

```text
1. 관측기준을 생략
2. 구조해석을 역사 사실로 둔갑
3. 훈민정음 Event를 Context 안에서 완성
4. 숫자 24를 relation 근거로 사용
```

---

## 10. Context_Sejong source table

초기 source table은 다음과 같다.

```text
source_category | source_type | maps_to | use
--------------- | ----------- | ------- | ---
세종실록 | A급 원문 DB | m/t/p | 사실 표식, 시기, 왕권·국가운영 조건
훈민정음 관련 원문 | A급 원문 / 원문 이미지 | t/p/? | Event로 향하는 조건 확인
국립국어원 / 국립한글박물관 자료 | A/B급 공식 해설 | p/? | 원문·해설 연결, 문자장 이해
한국민족문화대백과 | B급 해설 | m/t/p | 역사 맥락 보조
학술논문 / 연구서 | B급 연구자료 | t/p/? | 국가운영장, 학문장, 문자정책 분석 보조
SeungeFlow active_schema | C급 구조 source | ?/Core/Path | 작성 규칙과 구조연산 기준
SeungeFlow seed_base | C급 구조 source | Core/Path | 구조원리 source
```

이 table은 확정 source list가 아니다.

실제 작성 단계에서 source를 구체화한다.

---

## 11. Context와 Event 경계

Context_Sejong source map에서 가장 중요한 경계는 Context와 Event의 분리다.

```text
Context_Sejong.md =
Sejong이 어떤 존재 형성장으로 formed 되었는가

Event_Hunminjeongeum.md =
Hunminjeongeum이 어떤 formed structure로 드러났는가
```

Context에서 다룰 수 있는 것:

```text
세종의 형성과정
조선 초기 국가운영장
학문장
언어장 / 문자장 조건
문자 문제의 누적
Hunminjeongeum Event로 향하는 전제조건
```

Event로 넘길 것:

```text
훈민정음의 제자원리
훈민정음의 문헌 구조
창제 / 반포의 formed state
문자체계의 구조적 특이점
훈민정음 자체의 Event_C 판정
```

---

## 12. source map과 Path 후보

Context_Sejong source map은 Path 후보를 남긴다.

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
1. 세종 Context와 훈민정음 Event 사이의 사이는 무엇인가?
2. 둘 사이의 차이는 무엇인가?
3. 어떤 전제조건이 있었는가?
4. 어디가 임계사이영역인가?
5. 어떤 극한임계전이가 있었는가?
6. 어떤 Core seat가 반응하는가?
7. C+1은 무엇인가?
```

이 질문들은 `Path_Sejong_Hunminjeongeum.md`에서 다룬다.

---

## 13. Core reaction 후보

Context_Sejong source map 기준 Core reaction 후보:

```text
Core_01 Time-Flow Core
Core_02 Place-Field Core
Core_03 Relation Core
Core_04 Difference / Between Core
Core_08 C=tp Core
Core_09 C=(m,t,p,?) Core
Core_14 Observer Gaze Core
Core_15 Existence Core
Core_16 Multi-Being Core
Core_17 Field / Fabric / Domain Core
Core_19 Event / Context Core
Core_20 Branch Structure Core
Core_21 Seed.Base / Active.Schema Core
Core_24 Structure-Body Formation Core
```

이것은 확정이 아니다.

```text
Core reaction =
관측 후보
```

실제 Context_Sejong.md 작성 후 조정한다.

---

## 14. source map 작성 후 다음 작업

이 source map 이후 다음 작업은 두 가지 중 하나다.

```text
A안:
source 확인을 먼저 수행한다.

B안:
source map을 기준으로 Context_Sejong.md 구조 초안을 작성한다.
```

현재 권장안은 A안과 B안을 결합하는 방식이다.

```text
1. source map 기준으로 Context_Sejong.md 골격 작성
2. 역사 사실 부분은 source 확인 필요 표시
3. 구조해석 부분은 해석으로 표시
4. source 확인 후 본문 확정
```

즉, 다음 문서는 본문 초안이되, source requirement 표시를 유지한다.

---

## 15. Context_Sejong.md 초안 작성 방식

다음 회차에서 Context_Sejong.md를 작성한다면 다음 방식으로 쓴다.

```text
1. 역사 사실 단정 최소화
2. source 필요 지점 표시
3. Context_C 판정은 임시판정으로 표시
4. Event 내용은 과도하게 넣지 않음
5. Path 후보만 남김
6. 숫자패턴 guard 유지
```

표시 방식:

```text
[Source Required]
[Structure Interpretation]
[Provisional Judgment]
[Do Not Merge with Event]
```

이 표식을 사용하면 source 없는 단정과 구조해석 과잉을 줄일 수 있다.

---

## 16. 닫힘

`Context_Sejong_source_map.md`는 `Context_Sejong.md`를 작성하기 위한 source map으로 작성되었다.

이 문서는 다음 판정으로 닫힌다.

```text
Context_Sejong.md는
세종대왕 위인전이 아니다.

Context_Sejong.md는
Sejong이 어떤 m, t, p, ? 안에서
Context_C로 formed 되었는지 보는
존재 형성장 문서다.

이를 위해 source는
m / t / p / ? / Core reaction / Path 후보로
분리해서 mapping해야 한다.
```

---

다음회차:
Event / Context 적용 9회차

필요한 모드:
Thinking 헤비

목적:
Context_Sejong.md 초안 작성
