# Sejong_Hunminjeongeum_source_verification_0001.md

> 문서번호: `Ctp24_EVENT_CONTEXT_0017`  
> 상태: Event / Context 적용 17회차  
> 필요한 모드: `Thinking 확장`  
> 목적: Sejong-Hunminjeongeum Event / Context 첫 적용 세트의 source verification 1회차를 수행한다.  
> 위치 후보: `epluone/Event_Context/Sejong_Hunminjeongeum/source_verification/Sejong_Hunminjeongeum_source_verification_0001.md`

---

## 0. 이 문서의 자리

이 문서는 최종 역사해석문이 아니다.

이 문서는 `Context_Sejong.md`, `Event_Hunminjeongeum.md`, `Path_Sejong_Hunminjeongeum.md`에서 사용한 source anchor들이 어떤 사실 표식과 어떤 구조항을 지지하는지 1차로 검산하는 문서다.

```text
이 문서 =
source verification 1회차

아직 아님 =
최종 역사 판정
최종 C+1 판정
최종 Path 판정
```

검산 대상:

```text
Context_Sejong.md
Event_Hunminjeongeum.md
Path_Sejong_Hunminjeongeum.md
```

검산 중심:

```text
source
→ m / t / p / ?
→ Context_C / Event_C / Path 후보
```

---

## 1. 검산 원칙

source verification의 원칙은 다음이다.

```text
1. source가 말하는 사실과 Ctp24 구조해석을 분리한다.
2. 원문 기록과 현대 해설을 구분한다.
3. 날짜 표식과 구조 전이를 구분한다.
4. 문자체계 / 책 / 해례본 / 후대 한글을 구분한다.
5. 숫자패턴을 relation 근거로 사용하지 않는다.
6. source anchor가 지지하지 않는 문장은 확정하지 않는다.
7. C+1은 아직 final judgment가 아니다.
```

---

## 2. source 등급 재확인

현재 source는 다음 등급으로 둔다.

```text
A급 source =
조선왕조실록 / 원문 기록 / 원문 이미지 / 원문 DB

B급 source =
공신력 있는 기관 해설 / 백과 / 현대어 풀이 / 해제 자료

C급 source =
SeungeFlow 내부 schema / active_schema / Core / Path / AI vocab
```

이 문서에서 검산하는 source는 대부분 A급과 B급이다.

C급 source는 구조해석 기준이지 역사 사실 source가 아니다.

---

## 3. Verified Source Anchor A1 — 세종 25년 12월 30일 기록

source:

```text
조선왕조실록 / 세종실록 102권
세종 25년 12월 30일 경술 2/2 기사
제목: 훈민정음을 창제하다
```

확인된 source fact:

```text
1. 세종 25년 12월 30일 기록이다.
2. 기사 제목은 “훈민정음을 창제하다”이다.
3. 국역 본문에는 임금이 친히 언문 28자를 지었다는 내용이 있다.
4. 초성·중성·종성으로 나누어 합한 뒤 글자를 이룬다는 내용이 있다.
5. 이것을 훈민정음이라고 불렀다는 내용이 있다.
```

Ctp24 mapping:

```text
maps_to =
Event_Hunminjeongeum_t
+
Event_Hunminjeongeum_m
+
Event_Hunminjeongeum_?
```

검산 판정:

```text
A1은
Hunminjeongeum Event의 “창제 표식” source anchor로 적절하다.
```

주의:

```text
A1은 창제 표식이다.
A1 하나만으로 Event_C 전체를 확정하지 않는다.
A1의 “28자”를 Ctp24의 24와 연결하지 않는다.
```

---

## 4. Verified Source Anchor A2 — 세종 28년 9월 29일 기록

source:

```text
조선왕조실록 / 세종실록 113권
세종 28년 9월 29일 갑오 1번째 기사
```

확인된 source fact:

```text
1. 세종 28년 9월 29일 기사이다.
2. 기사 목록에 “《훈민정음》이 이루어지다. 어제와 예조 판서 정인지의 서문”이 있다.
3. 이 source는 창제 표식과 별도의 완성 / 문헌 표식 후보로 쓸 수 있다.
```

Ctp24 mapping:

```text
maps_to =
Event_Hunminjeongeum_t
+
Event_Hunminjeongeum_m
+
Event_Hunminjeongeum_?
```

검산 판정:

```text
A2는
Hunminjeongeum Event의 “완성 / 문헌 표식” source anchor로 적절하다.
```

주의:

```text
A1과 A2를 혼동하지 않는다.

A1 =
창제 표식

A2 =
완성 / 문헌 / 서문 표식 후보
```

또한 A2의 날짜를 곧바로 극한임계전이로 확정하지 않는다.

```text
date =
marker

transition =
structural change
```

---

## 5. Verified Source Anchor B1 — 한국민족문화대백과 「훈민정음」

source:

```text
한국민족문화대백과 「훈민정음」 항목
```

확인된 source fact:

```text
1. 해례본은 전권 33장 1책의 목판본으로 설명된다.
2. 1446년 9월 상한에 완성되었다고 설명된다.
3. 해례본의 구성은 본문(예의), 해례, 정인지서문으로 나누어진다.
4. 예의에는 어제서문과 새 글자의 음가·운용법 설명이 포함된다.
5. 해례에는 제자해, 초성해, 중성해, 종성해, 합자해, 용자례가 포함된다.
6. 정인지서문은 창제이유, 창제자, 우수성, 편찬자, 편찬연월일 등을 밝힌 것으로 설명된다.
```

Ctp24 mapping:

```text
maps_to =
Event_Hunminjeongeum_m
+
Event_Hunminjeongeum_p
+
Event_Hunminjeongeum_?
```

검산 판정:

```text
B1은
Hunminjeongeum Event의 내부 층위,
특히 책 / 문헌 / 해례본 설명 구조를 mapping하는 source anchor로 적절하다.
```

주의:

```text
B1은 공신력 있는 해설 source다.
원문 source를 대체하지 않는다.
해례본 구성은 Event_m 내부 구조 후보로 읽는다.
```

---

## 6. Verified Source Anchor B2 — 국립국어원 「알기 쉽게 풀어 쓴 훈민정음」

source:

```text
국립국어원 자료
알기 쉽게 풀어 쓴 훈민정음
```

확인된 source fact:

```text
1. 훈민정음 해례본의 한문 원문을 쉬운 현대 한국어로 번역한 내용이 포함된다.
2. 영어 번역도 함께 제시된다.
3. 훈민정음이라는 문자의 언어학적 가치와 책의 서지적 특징을 해설한 논문도 포함된다.
4. 훈민정음 해례본과 언해본의 원문 이미지 연계 링크를 제공한다.
5. 해례본 원문 이미지와 언해본 원문 이미지 접근 경로가 제시된다.
```

Ctp24 mapping:

```text
maps_to =
Event_Hunminjeongeum_?
+
Event_Hunminjeongeum_m
+
Event_Hunminjeongeum_p
```

검산 판정:

```text
B2는
원문 이해 보조,
현대어 풀이,
원문 이미지 접근 경로,
해례본 / 언해본 층위 구분을 위한 source anchor로 적절하다.
```

주의:

```text
현대어 풀이는 원문 이해 보조다.
현대어 풀이를 원문 사실과 동일시하지 않는다.
```

---

## 7. Verified Source Anchor B3 — 한국민족문화대백과 「한글」

source:

```text
한국민족문화대백과 「한글」 항목
```

확인된 source fact:

```text
1. 한글은 조선 제4대 임금 세종대왕이 훈민정음이라는 이름으로 창제하여 1446년에 반포한 우리나라 고유 문자로 설명된다.
2. 한글 항목은 일반 민중의 문자 사용과 기록·소통 문제를 창제 배경으로 설명한다.
3. 해당 항목은 훈민정음의 본문과 해례 구성, 그리고 1443년 기록과 1446년 기록의 구분을 설명한다.
```

Ctp24 mapping:

```text
maps_to =
Context_Sejong_p
+
Event_Hunminjeongeum_t
+
Event_Hunminjeongeum_?
+
Path_between 후보
```

검산 판정:

```text
B3은
언어장 / 문자장 조건,
후대 한글 설명,
창제 표식과 반포 / 책 형성 표식 구분을 보조하는 source anchor로 적절하다.
```

주의:

```text
B3은 한글 일반 설명을 포함한다.
Event_Hunminjeongeum을 현대 한글 전체로 확장할 때는 별도 Path가 필요하다.
```

---

## 8. verified / unverified 분리

현재 verified 상태:

```text
A1 =
세종 25년 12월 30일 훈민정음 창제 기록 확인

A2 =
세종 28년 9월 29일 《훈민정음》 완성 / 서문 관련 기사 확인

B1 =
훈민정음 해례본 구성과 서지 관련 백과 해설 확인

B2 =
국립국어원 현대어 풀이 / 원문 이미지 연계 자료 확인

B3 =
한글 일반 개념과 1446 반포 설명, 창제 배경 해설 확인
```

아직 unverified 또는 additional verification 필요:

```text
1. 세종의 생애 / 왕위 계승 / 교육 관련 세부 source
2. 조선 초기 국가운영장 source
3. 집현전과 훈민정음 창제의 직접 관계 source
4. 해례본 원문 세부 구절별 분석
5. 언해본과 해례본의 세부 층위 검산
6. 후대 한글 확산과 현대 자모 체계 source
```

---

## 9. Context_Sejong.md에 대한 source verification

`Context_Sejong.md`에서 source 검산이 된 부분:

```text
1. 세종과 훈민정음의 관계를 볼 수 있는 source anchor가 존재한다.
2. 언어장 / 문자장 조건을 보조하는 B3 source가 있다.
3. 집현전 관련 source는 아직 추가 확인이 필요하다.
```

현재 Context_Sejong_C 판정은 유지하되 provisional 상태로 둔다.

```text
Context_Sejong_C =
provisional
```

이유:

```text
Sejong의 생애, 왕위 형성, 국가운영장, 집현전의 역할은
추가 source verification이 필요하다.
```

---

## 10. Event_Hunminjeongeum.md에 대한 source verification

`Event_Hunminjeongeum.md`에서 source 검산이 된 부분:

```text
1. 창제 표식 source anchor 확인
2. 완성 / 문헌 표식 source anchor 확인
3. 해례본 구성 source anchor 확인
4. 현대어 풀이와 원문 이미지 접근 source anchor 확인
```

따라서 Event_Hunminjeongeum_C의 기본 방향은 유지 가능하다.

```text
Event_Hunminjeongeum_C =
source-supported provisional judgment
```

단, Event_C 최종 판정은 아직 하지 않는다.

```text
Event_C =
provisional
```

이유:

```text
해례본 원문 구조와 제자원리 세부 분석은
추가 source verification이 필요하다.
```

---

## 11. Path_Sejong_Hunminjeongeum.md에 대한 source verification

`Path_Sejong_Hunminjeongeum.md`에서 source anchor가 지지하는 부분:

```text
1. Context와 Event 사이에 언어장 / 문자장 조건이 놓일 수 있다.
2. 창제 표식과 완성 / 문헌 표식은 구분 가능하다.
3. Event_m 내부에 문자체계 / 책 / 해례본 설명 구조 층위가 존재한다.
```

아직 source anchor가 부족한 부분:

```text
1. 정확한 임계사이영역 판정
2. 극한임계전이 판정
3. C+1 판정
4. 집현전과 훈민정음 Event의 직접 relation
5. 조선 국가운영장과 문자체계 field의 구체 relation
```

따라서 Path_C는 유지하되, C+1은 계속 보류한다.

```text
C+1 =
provisional candidate
final judgment 아님
```

---

## 12. number-pattern guard 검산

현재 source verification으로 확인된 숫자 관련 표식은 다음이다.

```text
세종실록 25년 12월 30일 기록 =
언문 28자 표식

현대 한글 / 자모 24 =
별도 현대 체계 설명에서 나타나는 숫자일 수 있음

Ctp24 =
Ctp24 구조 안의 form seat 기준수

24절기 =
달력 / 계절 구분 체계
```

검산 판정:

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

세종실록 28자
=
Ctp24의 근거
```

숫자는 각 source context 안에서만 우선 의미를 가진다.

---

## 13. source verification 결과 표

```text
source | grade | verified fact | maps_to | status
------ | ----- | ------------- | ------- | ------
세종실록 25년 12월 30일 | A | 창제 표식, 언문 28자, 훈민정음 명칭 | Event_t / Event_m / ? | verified
세종실록 28년 9월 29일 | A | 《훈민정음》 완성 / 서문 관련 기사 | Event_t / Event_m / ? | verified
한국민족문화대백과 「훈민정음」 | B | 해례본 서지와 구성 | Event_m / Event_p / ? | verified as B-source
국립국어원 자료 | B | 현대어 풀이, 영어 번역, 원문 이미지 링크 | Event_? / source access | verified as B-source
한국민족문화대백과 「한글」 | B | 한글 개념, 창제·반포 설명, 창제 배경 해설 | Context_p / Event_t / Path 후보 | verified as B-source
```

---

## 14. source verification 1회차 판정

이번 source verification 1회차의 판정은 다음이다.

```text
A1 / A2 =
Event_Hunminjeongeum의 시간 표식 source anchor로 적절

B1 / B2 =
Event_Hunminjeongeum의 내부 층위와 원문 접근 보조 source anchor로 적절

B3 =
Context와 Event 사이의 언어장 / 문자장 조건을 보조하는 source anchor로 적절
```

그러나 아직 다음은 최종 판정하지 않는다.

```text
Context_Sejong_C final judgment
Event_Hunminjeongeum_C final judgment
Path_Sejong_Hunminjeongeum_C final judgment
C+1 final judgment
```

---

## 15. 다음 verification 과제

다음 source verification에서 확인할 과제:

```text
1. 세종 생애 / 왕위 / 교육 / 국가운영장 source
2. 집현전 source
3. 세종과 집현전 / 문자정책 relation source
4. 훈민정음 해례본 원문 세부 구조 source
5. 제자원리 세부 source
6. 후대 한글 확산 source
```

특히 다음이 중요하다.

```text
집현전은 Context_Sejong_p 후보이나,
Hunminjeongeum Event와의 직접 relation은
source 검산 전에는 확정하지 않는다.
```

---

## 16. 닫힘

`Sejong_Hunminjeongeum_source_verification_0001.md`는 Sejong-Hunminjeongeum Event / Context 첫 적용 세트의 source verification 1회차로 작성되었다.

이 문서는 다음 판정으로 닫힌다.

```text
Event_Hunminjeongeum의 기본 source anchor는 확인되었다.

그러나 Context_Sejong과 Path_Sejong_Hunminjeongeum의
세부 relation 판정에는 추가 source verification이 필요하다.

C+1은 계속 provisional candidate로 둔다.
```

---

다음회차:
Event / Context 적용 18회차

필요한 모드:
Thinking 확장

목적:
Context_Sejong source verification 2회차 — 세종 생애 / 국가운영장 / 집현전 source 검산
