# Context_Sejong_source_verification_0003.md

> 문서번호: `Ctp24_EVENT_CONTEXT_0019`  
> 상태: Event / Context 적용 19회차  
> 필요한 모드: `Thinking 확장`  
> 목적: `Context_Sejong.md`의 언어장 / 문자장 / 백성 문자 접근성 source를 3차 검산한다.  
> 위치 후보: `epluone/Event_Context/Sejong_Hunminjeongeum/source_verification/Context_Sejong_source_verification_0003.md`

---

## 0. 이 문서의 자리

이 문서는 `Context_Sejong.md`의 source verification 3회차 문서다.

2회차에서는 세종의 기본 m, 왕위 형성 t, 조선 초기 국가운영장 p, 집현전 / 학문장 p를 검산했다.

이번 3회차에서는 `Context_Sejong.md`에서 가장 조심해야 할 축인 다음 항목을 검산한다.

```text
언어장
문자장
백성 문자 접근성
말과 글의 불일치
한자 / 한문 중심 문서장
훈민정음 Event로 향하는 조건장
```

이 문서는 최종 역사해석문이 아니다.

이 문서는 source anchor들이 `Context_Sejong`의 p / ? / Path 후보 중 어디를 지지하는지 확인하는 문서다.

```text
source
→ p / ?
→ Context_Sejong_C 후보
→ Path_Sejong_Hunminjeongeum 후보
```

---

## 1. 검산 원칙

이번 source verification의 원칙은 다음이다.

```text
1. 언어장 / 문자장을 Context의 p로 본다.
2. 백성 문자 접근성 문제를 Context와 Event 사이의 between-field 후보로 본다.
3. 훈민정음 어제서문의 문장을 구조해석으로 과잉 번역하지 않는다.
4. 원문 / 국역 / 해설을 구분한다.
5. 한자 / 한문 중심 문서장을 단순히 부정 대상으로 쓰지 않는다.
6. 훈민정음 Event 자체의 formed structure는 Event 문서에서 다룬다.
7. C+1은 아직 확정하지 않는다.
8. 숫자패턴은 relation 근거가 아니다.
```

---

## 2. Verified Source Anchor C-SJ-06 — 훈민정음 어제서문 / 말과 글의 불일치

source:

```text
우리역사넷 / 사료로 본 한국사
「한글의 글자 규칙」
```

확인된 source fact:

```text
1. 『훈민정음』 어제에는 “우리나라 말이 중국과 달라 한자와 서로 통하지 않는다”는 취지가 나타난다.
2. 말하고 싶은 것이 있어도 뜻을 잘 표현하지 못하는 백성이 많다는 취지가 나타난다.
3. 새로 28자를 만들었고, 사람들이 쉽게 익혀 날마다 쓰는 데 편하게 하려 했다는 취지가 나타난다.
```

Ctp24 mapping:

```text
maps_to =
Context_Sejong_p
+
Context_Sejong_?
+
Path_between 후보
```

검산 판정:

```text
C-SJ-06은
Context_Sejong의 언어장 / 문자장 / 백성 문자 접근성 문제를 지지하는 source anchor로 적절하다.
```

구조해석:

```text
말과 글의 불일치 =
Context_Sejong_p 안의 문자장 압력 후보

뜻을 표현하지 못하는 백성 =
Context_Sejong_? 안에서 관측되는 문자 접근성 조건

쉽게 익혀 쓰게 하려는 목적 =
Event_Hunminjeongeum으로 향하는 Path 후보
```

주의:

```text
이 source는 Event_Hunminjeongeum의 창제 목적과 연결될 수 있지만,
Context_Sejong.md 안에서는 조건장까지만 다룬다.
Event formed state는 Event_Hunminjeongeum.md에서 다룬다.
```

---

## 3. Verified Source Anchor C-SJ-07 — 일반 민중의 기록 / 전달 문제

source:

```text
한국민족문화대백과 「한글」 항목
```

확인된 source fact:

```text
1. 한글은 세종이 훈민정음이라는 이름으로 창제하여 1446년에 반포한 문자로 설명된다.
2. 어려운 한자를 빌려 문자로 사용할 경우 정확한 정보 기록과 소통이 불가능하다는 취지가 설명된다.
3. 일반 민중은 말 이외에 의사를 기록하고 전달할 방법이 없게 된다는 문제의식이 설명된다.
4. 이러한 문제의식에서 한글이 만들어지게 되었다고 설명된다.
```

Ctp24 mapping:

```text
maps_to =
Context_Sejong_p
+
Path_between 후보
+
Event_Hunminjeongeum_t 후보
```

검산 판정:

```text
C-SJ-07은
백성 문자 접근성 문제와 언어장 / 문자장 조건을 Context_Sejong_p로 설정하는 데 적절한 B급 source anchor다.
```

구조해석:

```text
일반 민중의 기록 / 전달 문제 =
Context_Sejong_p 안의 field pressure 후보

정확한 기록과 소통의 어려움 =
Event_Hunminjeongeum으로 향하는 조건장 후보
```

주의:

```text
이 source는 해설 source다.
원문 source를 대체하지 않는다.
```

---

## 4. Verified Source Anchor C-SJ-08 — 말과 글이 다른 문자생활

source:

```text
우리역사넷 「세종어제훈민정음」
```

확인된 source fact:

```text
1. 훈민정음 이전에는 말과 글이 다른 이중적인 언어생활이 있었다는 설명이 제시된다.
2. 이두, 구결, 향찰 같은 차용표기 체계가 있었지만, 말과 글이 다른 문자생활은 불완전하고 한계가 있었다고 설명된다.
3. 말과 글이 달라 겪는 불편함은 훈민정음 창제의 직접적인 원인이 되었다고 설명된다.
4. 어제서문은 말과 문자가 통하지 않아 뜻을 표현하지 못하는 백성이 많다는 내용을 제시한다.
```

Ctp24 mapping:

```text
maps_to =
Context_Sejong_p
+
Context_Sejong_t
+
Path_between 후보
```

검산 판정:

```text
C-SJ-08은
Context_Sejong의 언어장 / 문자장 조건을 단순 배경이 아니라
Event로 향하는 누적된 field pressure로 읽는 데 적절한 source anchor다.
```

구조해석:

```text
이중적 언어생활 =
Context_Sejong_p 내부의 문자장 구조

차용표기 체계의 한계 =
Path의 between-field 후보

말과 글의 불일치 =
Event_Hunminjeongeum으로 향하는 조건장 후보
```

주의:

```text
이 source는 Context와 Event 사이의 강한 Path 후보를 제공한다.
그러나 C+1은 아직 확정하지 않는다.
```

---

## 5. Verified Source Anchor C-SJ-09 — 반포와 동시에 문자생활 전체를 즉시 혁신하지는 못함

source:

```text
우리역사넷 「훈민정음과 우리 민족의 문자생활」
```

확인된 source fact:

```text
1. 훈민정음 창제로 국어의 전면적 표기가 가능해졌다고 설명된다.
2. 그러나 반포와 동시에 문자생활이 완전히 혁신된 것은 아니었다고 설명된다.
3. 한자 / 한문 사용이 상류층에 계속 존속했다는 설명이 있다.
4. 정음은 당초 한문의 결함을 보충하는 것으로 만들어졌다고 볼 수 있다는 해석이 제시된다.
5. 언문 보급은 점진적이었다는 설명이 있다.
```

Ctp24 mapping:

```text
maps_to =
Context_Sejong_p
+
Path_difference 후보
+
C+1 보류 근거
```

검산 판정:

```text
C-SJ-09는
Hunminjeongeum Event 이후의 C+1을 너무 빨리 확정하지 말아야 한다는 guard source로 적절하다.
```

구조해석:

```text
창제 / 반포 =
Event marker

문자생활 전체 혁신 =
즉시 확정 불가

후대 확산 =
별도 Path 필요
```

주의:

```text
C+1을 “한글이 즉시 문자생활 전체를 바꾸었다”로 단정하면 안 된다.
C+1은 provisional candidate로 유지한다.
```

---

## 6. Verified Source Anchor C-SJ-10 — 국립한글박물관의 문자생활 / 실용성 해설

source:

```text
국립한글박물관 상설전시 소개
「훈민정음, 천년의 문자 계획」
```

확인된 source fact:

```text
1. 훈민정음 이전 문자생활에서 우리말과 중국말이 다르고, 한자를 빌려 우리말을 적는 데 한계가 있었다고 설명한다.
2. 한자를 배우지 않고는 글을 쓰기 어려웠던 답답함을 전시 맥락에서 설명한다.
3. 세종이 글을 모르는 백성이 뜻을 제대로 전하지 못하는 것을 딱하게 여겨 쉽게 쓸 수 있는 문자를 만들고자 했다고 설명한다.
4. 이후 국가와 기관 주도의 한글 자료, 언해, 실용서 간행 등 지식과 정보 전파의 흐름을 소개한다.
```

Ctp24 mapping:

```text
maps_to =
Context_Sejong_p
+
Context_Sejong_?
+
Path_between 후보
+
후대 영향 후보
```

검산 판정:

```text
C-SJ-10은
언어장 / 문자장 / 백성 문자 접근성 문제를 Context_Sejong_p와 Path 후보로 읽는 보조 source anchor로 적절하다.
```

주의:

```text
전시 해설은 source anchor로 유용하지만,
원문 source를 대체하지 않는다.
후대 언해 / 실용서 흐름은 별도 Path에서 다시 검산한다.
```

---

## 7. verified / unverified 분리

현재 verified 상태:

```text
1. 훈민정음 어제서문은 말과 글의 불일치, 백성의 표현 곤란, 쉽게 익혀 쓰려는 목적을 source anchor로 제공한다.
2. 한글 관련 공신력 있는 해설 source는 일반 민중의 기록 / 전달 문제를 창제 배경으로 설명한다.
3. 우리역사넷 자료는 말과 글이 다른 이중적 언어생활과 차용표기 체계의 한계를 설명한다.
4. 우리역사넷 문자생활 자료는 훈민정음 반포가 문자생활 전체를 즉시 혁신하지는 않았다는 guard를 제공한다.
5. 국립한글박물관 해설은 한자 중심 문자생활과 백성 접근성 문제를 보조 source로 제공한다.
```

아직 additional verification 필요:

```text
1. 한자 / 한문 중심 문서장이 실제 행정 / 법제 / 국가운영과 어떻게 연결되었는지
2. 백성 문자 접근성 문제가 세종대 국가운영장 안에서 어떤 정책적 조건으로 작동했는지
3. 언어장 / 문자장 조건과 집현전 / 학문장 조건의 직접 relation
4. 후대 언해 / 실용서 간행이 Hunminjeongeum Event의 C+1인지, 별도 후대 Path인지
5. 한글 보급 범위와 시기별 확산에 대한 더 정밀한 source
```

---

## 8. Context_Sejong.md 검산 결과

`Context_Sejong.md`에서 다음 항목은 source-supported provisional 상태로 유지 가능하다.

```text
언어장 / 문자장 =
Context_Sejong_p의 핵심 후보

백성 문자 접근성 문제 =
Context_Sejong_p와 ?에 걸친 field pressure 후보

말과 글의 불일치 =
Event_Hunminjeongeum으로 향하는 between-field 후보
```

따라서 Context_Sejong_C의 기존 임시판정 중 다음 부분은 강화된다.

```text
Context_Sejong_C =
Sejong이
조선 초기 국가운영장,
학문장,
언어장 / 문자장,
왕권과 제도장의 흐름 속에서
특정 관측기준 ?에 의해
formed 된 존재 형성장
```

특히 이번 검산으로 다음이 강화된다.

```text
언어장 / 문자장 =
source-supported Context p 후보

백성 문자 접근성 =
source-supported Path between-field 후보
```

---

## 9. Path_Sejong_Hunminjeongeum.md에 넘길 항목

이번 source verification 3회차에서 Path로 넘길 수 있는 항목:

```text
1. 말과 글의 불일치
2. 한자 / 한문 중심 문자장과 한국어 표현의 차이
3. 백성의 뜻 표현 곤란
4. 쉽게 익혀 쓰게 하려는 목적
5. 차용표기 체계의 한계
6. 훈민정음 반포 이후 문자생활 전체 변화는 즉시 확정 불가
7. 후대 확산은 별도 Path 필요
```

Path에서 사용할 relation 후보:

```text
Context_Sejong_p 언어장 / 문자장
+
Event_Hunminjeongeum_C 새 문자체계 formed state
=
C+1 후보
```

그러나 C+1은 계속 보류한다.

---

## 10. Core reaction 검산

이번 source verification에서 지지되는 Core reaction 후보:

```text
Core_02 Place-Field Core
=
언어장 / 문자장 / 한자 중심 문서장

Core_03 Relation Core
=
말과 글, 백성 표현, 국가운영장과 문자체계 관계

Core_04 Difference / Between Core
=
한국어와 한자 / 한문, 말과 글의 차이

Core_08 C=tp Core
=
언어장 / 문자장 p와 문자 사용 흐름 t의 결합

Core_14 Observer Gaze Core
=
백성 문자 접근성을 어떤 기준으로 볼 것인가

Core_17 Field / Fabric / Domain Core
=
문자장, 문서장, 언어장

Core_18 Path / C+1 Core
=
Context와 Event의 relation 후보

Core_19 Event / Context Core
=
Context 조건과 Event formed structure의 분리
```

아직 보류할 Core reaction:

```text
Core_05 9dot0 Core
Core_24 Structure-Body Formation Core
```

이 Core들은 Path 심화와 C+1 검산 후 다시 판정한다.

---

## 11. C+1 보류 판정 강화

이번 verification은 C+1을 확정하지 않는 이유를 더 강화한다.

source들은 다음을 지지한다.

```text
훈민정음 창제와 반포는 문자체계 field 전이의 중요한 표식이다.
```

그러나 source들은 동시에 다음 guard도 제공한다.

```text
반포와 동시에 문자생활 전체가 완전히 혁신되지는 않았다.
```

따라서 현재 C+1은 다음 상태로 둔다.

```text
C+1 =
provisional candidate
final judgment 아님
```

현재 후보 문장:

```text
C+1 후보 =
조선의 국가운영장과 언어장 / 문자장이
Hunminjeongeum이라는 formed structure를 통해
새로운 문자체계 field로 전이될 수 있는 조건을 연 상태
```

`전이된 상태`보다 `전이될 수 있는 조건을 연 상태`가 더 안전하다.

---

## 12. number-pattern guard 재확인

이번 verification에서 숫자패턴 관련 guard는 계속 유지한다.

```text
세종실록의 언문 28자 표식 =
source fact

현대 자모 24 =
후대 체계

Ctp24 =
Ctp24 form seat 기준수

24절기 =
달력 / 계절 구분 체계
```

판정:

```text
숫자 유사성은 relation 증거가 아니다.
```

따라서 다음 연결은 금지한다.

```text
훈민정음 현대 자모 24
=
Ctp24의 근거

24절기
=
Ctp24의 근거

실록의 언문 28자
=
Ctp24의 근거
```

---

## 13. source verification 3회차 판정

이번 3회차 판정은 다음이다.

```text
Context_Sejong의 언어장 / 문자장 / 백성 문자 접근성 source anchor는 확인되었다.

말과 글의 불일치,
한자 / 한문 중심 문자생활의 한계,
백성의 뜻 표현 곤란,
쉽게 익혀 쓰게 하려는 목적은
Context_Sejong_p와 Path between-field 후보를 지지한다.

그러나 이것은 C+1 final judgment를 뜻하지 않는다.
```

따라서:

```text
Context_Sejong_C =
source-supported provisional judgment 유지

Path_Sejong_Hunminjeongeum_C =
강화 가능

C+1 =
final judgment 불가
provisional candidate 유지
```

---

## 14. 다음 verification 과제

다음 source verification 후보:

```text
A안 =
Event_Hunminjeongeum source verification 2회차
해례본 원문 / 제자원리 / 해례본 구성 source 검산

B안 =
Path_Sejong_Hunminjeongeum 심화 검산
between-field / difference / 임계사이영역 source 검산

C안 =
Sejong-Hunminjeongeum verification update package 생성
```

권장안:

```text
A안
```

이유:

```text
Context 쪽 언어장 / 문자장 조건은 1차 검산되었다.
이제 Event 쪽 해례본 원문 / 제자원리 / 해례본 구조를 더 검산해야
Path의 Event_C가 강화된다.
```

---

## 15. 닫힘

`Context_Sejong_source_verification_0003.md`는 언어장 / 문자장 / 백성 문자 접근성 source를 3차 검산하기 위해 작성되었다.

이 문서는 다음 판정으로 닫힌다.

```text
언어장 / 문자장 / 백성 문자 접근성은
Context_Sejong_p와 Path between-field 후보로 유지 가능하다.

훈민정음 창제와 반포는
새 문자체계 field 전이의 중요한 표식이다.

그러나 문자생활 전체의 즉시 혁신은 확정할 수 없으므로
C+1은 계속 provisional candidate로 둔다.
```

---

다음회차:
Event / Context 적용 20회차

필요한 모드:
Thinking 확장

목적:
Event_Hunminjeongeum source verification 2회차 — 해례본 원문 / 제자원리 / 해례본 구성 source 검산
