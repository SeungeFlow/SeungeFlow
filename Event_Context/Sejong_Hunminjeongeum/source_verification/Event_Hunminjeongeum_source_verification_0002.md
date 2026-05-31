# Event_Hunminjeongeum_source_verification_0002.md

> 문서번호: `Ctp24_EVENT_CONTEXT_0020`  
> 상태: Event / Context 적용 20회차  
> 필요한 모드: `Thinking 확장`  
> 목적: `Event_Hunminjeongeum.md`의 해례본 원문 / 제자원리 / 해례본 구성 source를 2차 검산한다.  
> 위치 후보: `epluone/Event_Context/Sejong_Hunminjeongeum/source_verification/Event_Hunminjeongeum_source_verification_0002.md`

---

## 0. 이 문서의 자리

이 문서는 `Event_Hunminjeongeum.md`의 source verification 2회차 문서다.

1회차 source verification에서는 훈민정음 창제 표식, 완성 / 문헌 표식, 해례본 구성의 기본 source anchor를 검산했다.

이번 2회차는 `Event_Hunminjeongeum_C`의 내부 구조를 강화하기 위해 다음 항목을 검산한다.

```text
훈민정음 해례본 원문 / 원문 이미지
해례본 체재
예의 / 해례 / 정인지 서문
제자해 / 초성해 / 중성해 / 종성해 / 합자해 / 용자례
제자원리
초성 / 중성 / 종성 운용 구조
책 / 문자체계 / 설명 구조의 층위
```

이 문서는 최종 해례본 해석문이 아니다.

이 문서는 source anchor들이 `Event_Hunminjeongeum`의 m / t / p / ? / 내부 층위 / Core reaction 중 어디를 지지하는지 확인하는 문서다.

```text
source
→ m / t / p / ?
→ Event_Hunminjeongeum_C 후보
→ Path_Sejong_Hunminjeongeum 후보
```

---

## 1. 검산 원칙

이번 source verification의 원칙은 다음이다.

```text
1. 해례본 원문과 현대 해설을 구분한다.
2. 책 / 문헌으로서의 훈민정음과 문자체계로서의 훈민정음을 구분한다.
3. 예의 / 해례 / 정인지 서문의 층위를 구분한다.
4. 제자해 / 초성해 / 중성해 / 종성해 / 합자해 / 용자례를 Event_m 내부 구조 후보로 둔다.
5. 제자원리를 Ctp24 구조원리와 직접 동일시하지 않는다.
6. 숫자패턴을 relation 근거로 사용하지 않는다.
7. source fact와 structure interpretation을 분리한다.
8. C+1은 아직 final judgment로 확정하지 않는다.
```

---

## 2. Verified Source Anchor E-HJ-01 — 해례본 체재

source:

```text
국가유산포털 / 한국의 세계기록유산 / 훈민정음 해례본
국가유산 용어사전 / 훈민정음 해례본
한국민족문화대백과 「훈민정음」
```

확인된 source fact:

```text
1. 훈민정음 해례본은 예의, 해례, 정인지 서문 등으로 구성되는 문헌 구조를 가진다.
2. 예의는 세종의 훈민정음 서문과 새 문자 훈민정음의 음가 및 운용법에 대한 간략한 설명으로 제시된다.
3. 해례는 제자해, 초성해, 중성해, 종성해, 합자해로 구성되고, 용자례가 포함된다.
4. 정인지 서문은 해례본의 마지막 층위로 제시된다.
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
E-HJ-01은
Hunminjeongeum Event의 내부 문헌 구조를 지지하는 source anchor로 적절하다.
```

구조해석:

```text
해례본 체재 =
Event_m 내부의 structure layer

예의 / 해례 / 서문 =
Event_m이 단순 문자 이름이 아니라
문헌적 설명 구조를 가진 formed structure임을 보여 주는 source-supported layer
```

주의:

```text
해례본 체재를 Ctp24 구조와 직접 동일시하지 않는다.
해례본 구성은 Event_m 내부 구조 후보로만 둔다.
```

---

## 3. Verified Source Anchor E-HJ-02 — 예의의 역할

source:

```text
국가유산포털 / 한국의 세계기록유산 / 훈민정음 해례본
한국민족문화대백과 「훈민정음」
```

확인된 source fact:

```text
1. 예의는 세종의 훈민정음 서문과 새 문자 훈민정음의 음가 및 운용법을 다룬다.
2. 예의에는 새 문자에 대한 기본 설명이 놓인다.
3. 정인지의 서문은 계해년 겨울 세종이 정음 28자를 창제하고 예의를 들어 보였으며 이름을 훈민정음이라 했다는 내용을 전한다.
```

Ctp24 mapping:

```text
maps_to =
Event_Hunminjeongeum_m
+
Event_Hunminjeongeum_t
+
Event_Hunminjeongeum_?
```

검산 판정:

```text
E-HJ-02는
예의를 Event_m 내부의 기본 운용 설명 layer로 두는 데 적절한 source anchor다.
```

구조해석:

```text
예의 =
훈민정음 문자체계의 기본 정의와 운용법을 보이는 layer
```

주의:

```text
예의는 Event_m 내부 layer이지,
Context_Sejong_C 자체가 아니다.
```

---

## 4. Verified Source Anchor E-HJ-03 — 해례의 다섯 해와 용자례

source:

```text
국가유산포털 / 국가유산 용어사전 / 훈민정음 해례본
국립국어원 「훈민정음 해례본의 겉과 속」
한국민족문화대백과 「훈민정음」
```

확인된 source fact:

```text
1. 해례에는 제자해, 초성해, 중성해, 종성해, 합자해가 포함된다.
2. 용자례는 실제 사용 예를 제시하는 층위로 설명된다.
3. 국립국어원 자료는 제자해에서 글자를 만든 원리를 해설하고, 초성해·중성해·종성해에서 각각 초성·중성·종성을 설명하며, 합자해에서 초성·중성·종성의 결합 방식을 설명하고, 용자례에서 실제 예를 제시한다고 설명한다.
```

Ctp24 mapping:

```text
maps_to =
Event_Hunminjeongeum_m
+
Event_Hunminjeongeum_p
+
Event_Hunminjeongeum_?
+
Core reaction 후보
```

검산 판정:

```text
E-HJ-03은
Event_Hunminjeongeum_C 내부의 설명 구조와 운용 구조를 지지하는 source anchor로 적절하다.
```

구조해석:

```text
제자해 =
formation principle layer

초성해 / 중성해 / 종성해 =
sound-position / letter-function layer

합자해 =
composition / operation layer

용자례 =
actual-use example layer
```

주의:

```text
이 층위들은 Ctp24의 Core와 비교될 수는 있지만,
직접 동일시하면 안 된다.
```

---

## 5. Verified Source Anchor E-HJ-04 — 제자원리

source:

```text
한국민족문화대백과 「훈민정음」
국립한글박물관 훈민정음 표준 해설서 소개
국립국어원 / 해례본 해설 자료
```

확인된 source fact:

```text
1. 한국민족문화대백과는 제자해를 제자원리, 제자기준, 자음체계, 모음체계, 운용법과 관련된 해설 층위로 설명한다.
2. 국립한글박물관은 훈민정음 표준 해설서가 훈민정음의 제자 원리와 자모 순서, 자모 명칭 등을 다룬다고 설명한다.
3. 제자원리는 현대 해설에서 훈민정음 해례본을 이해하는 핵심 항목 중 하나로 다루어진다.
```

Ctp24 mapping:

```text
maps_to =
Event_Hunminjeongeum_m
+
Event_Hunminjeongeum_?
+
Core reaction 후보
```

검산 판정:

```text
E-HJ-04는
제자원리를 Event_m 내부의 formation principle 후보로 두는 데 적절한 source anchor다.
```

구조해석:

```text
제자원리 =
Hunminjeongeum Event_m 내부의 formation principle 후보
```

주의:

```text
제자원리 =
SeungeFlow 구조원리 그 자체 X

제자원리와 Ctp24 구조원리는
비교 가능성은 있으나 직접 동일시하지 않는다.
```

특히 다음을 금지한다.

```text
천지인 / 자모 수 / 24 / 28 등의 숫자 또는 상징을
Ctp24의 근거로 직접 연결하지 않는다.
```

---

## 6. Verified Source Anchor E-HJ-05 — 초성 / 중성 / 종성 / 합자 운용 구조

source:

```text
국가유산포털 / 한국의 세계기록유산 / 훈민정음 해례본
국립국어원 「훈민정음 해례본의 겉과 속」
한국민족문화대백과 「훈민정음」
```

확인된 source fact:

```text
1. 예의는 초성자와 중성자의 음가를 밝힌다.
2. 해례에는 초성해, 중성해, 종성해, 합자해가 포함된다.
3. 초성·중성·종성의 관계와 결합 방식은 해례본 설명 구조의 주요 층위로 다루어진다.
4. 합자해는 초성·중성·종성의 세 글자를 합쳐 쓰는 방법에 대한 해설로 설명된다.
```

Ctp24 mapping:

```text
maps_to =
Event_Hunminjeongeum_m
+
Event_Hunminjeongeum_p
+
Core_10 Matrix / Swap Core 후보
+
Core_12 Structure Sequence Core 후보
```

검산 판정:

```text
E-HJ-05는
Hunminjeongeum Event가 단순 문자 목록이 아니라
운용 구조와 결합 구조를 가진 formed structure라는 판정을 지지한다.
```

구조해석:

```text
초성 / 중성 / 종성 / 합자 =
Event_m 내부의 operation layer 후보
```

주의:

```text
초성 / 중성 / 종성 구조를
Ctp24 구조수열이나 행렬곱셈으로 바로 번역하지 않는다.

비교는 가능하지만,
source fact와 structure interpretation을 분리한다.
```

---

## 7. Event_Hunminjeongeum_C에 대한 source-supported 강화

이전 Event_C 임시판정:

```text
Event_Hunminjeongeum_C =
Hunminjeongeum이
조선의 언어장,
문자장,
국가운영장,
학문장,
문서장 안에서
새 문자체계와 그 설명 구조로
formed 된 구조 형성물
```

이번 verification으로 강화되는 부분:

```text
1. “새 문자체계” layer는 창제 기록과 해례본 설명 구조로 지지된다.
2. “책 / 문헌” layer는 해례본 체재 source로 지지된다.
3. “설명 구조” layer는 예의 / 해례 / 정인지 서문 구성으로 지지된다.
4. “제자원리”는 Event_m 내부 formation principle 후보로 지지된다.
5. “운용 구조”는 초성해 / 중성해 / 종성해 / 합자해 / 용자례 source로 지지된다.
```

따라서 Event_Hunminjeongeum_C는 다음으로 조금 더 정밀화할 수 있다.

```text
Event_Hunminjeongeum_C =
Hunminjeongeum이
조선의 언어장 / 문자장 / 국가운영장 조건 속에서
새 문자체계,
책 / 문헌,
해례본 설명 구조,
제자원리와 운용 구조를 포함한
formed structure로 드러난 상태
```

단, 이것도 final judgment가 아니라 source-supported provisional judgment다.

---

## 8. Core reaction 검산

이번 source verification에서 강화되는 Core reaction 후보:

```text
Core_05 9dot0 Core
=
창제 표식 / 완성 표식 / 해례 구조 사이의 전이 후보

Core_08 C=tp Core
=
Event가 t와 p의 관계 속에서 formed 되는 구조

Core_09 C=(m,t,p,?) Core
=
문자체계 / 책 / 해례본 / 제자원리 / 운용 구조 층위 분해

Core_10 Matrix / Swap Core
=
초성 / 중성 / 종성 / 합자 운용 구조 비교 후보

Core_12 Structure Sequence Core
=
문자 운용 순서와 설명 구조의 층위 후보

Core_14 Observer Gaze Core
=
훈민정음을 문자체계로 볼 것인가, 책으로 볼 것인가, 해례본 구조로 볼 것인가

Core_17 Field / Fabric / Domain Core
=
언어장 / 문자장 / 문서장 / 학문장

Core_19 Event / Context Core
=
Event_Hunminjeongeum_C와 Context_Sejong_C 분리

Core_24 Structure-Body Formation Core
=
문자체계가 설명 구조를 가진 formed structure로 드러나는 후보
```

보류할 Core reaction:

```text
Core_18 Path / C+1 Core
=
Path 심화 후 판정

Core_03 Relation Core
=
Context와 Event 사이의 relation 검산 후 판정
```

---

## 9. Path로 넘길 항목

이번 verification에서 Path로 넘길 수 있는 항목:

```text
1. Hunminjeongeum은 창제 표식과 완성 / 문헌 표식을 가진다.
2. Hunminjeongeum은 문자체계 layer와 책 / 문헌 layer를 가진다.
3. 해례본은 예의 / 해례 / 정인지 서문 등 설명 구조를 가진다.
4. 해례에는 제자해, 초성해, 중성해, 종성해, 합자해, 용자례가 포함된다.
5. 제자원리는 Event_m 내부의 formation principle 후보이다.
6. 초성 / 중성 / 종성 / 합자 구조는 Event_m 내부 operation layer 후보이다.
```

Path에서 이 항목들을 다음 질문으로 다룬다.

```text
Context_Sejong_C의 언어장 / 문자장 조건이
Event_Hunminjeongeum_C의 문자체계 / 설명 구조 / 운용 구조와
어떤 relation을 맺는가?
```

---

## 10. source와 structure interpretation 분리

이번 verification에서 가장 중요한 guard는 다음이다.

```text
해례본 source fact
≠
Ctp24 structure interpretation
```

예를 들어:

```text
제자해 / 초성해 / 중성해 / 종성해 / 합자해 / 용자례
=
source fact에 가까운 해례본 구성 / 해설 층위

Core_10 Matrix / Swap Core
=
SeungeFlow 구조해석에서의 반응 후보
```

둘은 비교될 수 있다.

그러나 동일시하지 않는다.

```text
비교 가능
직접 동일시 금지
```

---

## 11. number-pattern guard 재확인

이번 verification에서도 숫자패턴 guard는 유지한다.

source에서 다음이 등장할 수 있다.

```text
정음 28자
초성 / 중성 / 종성 구성
현대 자모 24
옛자음 포함 체계
```

그러나 다음은 금지한다.

```text
정음 28자 =
Ctp24의 근거

현대 자모 24 =
Ctp24의 근거

24절기 =
Ctp24의 근거
```

판정:

```text
숫자패턴은 관측 후보일 수 있으나,
relation의 증거가 아니다.
```

---

## 12. source verification 2회차 판정

이번 2회차 판정은 다음이다.

```text
훈민정음 해례본의 체재와 구성 source anchor는 확인되었다.

예의 / 해례 / 정인지 서문,
제자해 / 초성해 / 중성해 / 종성해 / 합자해 / 용자례는
Event_Hunminjeongeum_m 내부 층위와 operation layer를 지지한다.

제자원리는 Event_m 내부 formation principle 후보로 유지 가능하다.

그러나 제자원리를 Ctp24 구조원리와 직접 동일시하지 않는다.
```

따라서:

```text
Event_Hunminjeongeum_C =
source-supported provisional judgment 강화

Path_Sejong_Hunminjeongeum_C =
심화 가능

C+1 =
final judgment 불가
provisional candidate 유지
```

---

## 13. 다음 verification 과제

다음 source verification 후보:

```text
A안 =
Path_Sejong_Hunminjeongeum source verification 1회차
between-field / difference / 임계사이영역 source 검산

B안 =
Event_Hunminjeongeum source verification 3회차
해례본 원문 세부 구절과 제자원리 심화 검산

C안 =
Sejong-Hunminjeongeum verification update package 생성
```

권장안:

```text
A안
```

이유:

```text
Context 쪽 언어장 / 문자장 조건과
Event 쪽 해례본 / 제자원리 / 운용 구조가 각각 강화되었다.

이제 둘 사이의 Path를 source verification 해야 한다.
```

---

## 14. 닫힘

`Event_Hunminjeongeum_source_verification_0002.md`는 해례본 원문 / 제자원리 / 해례본 구성 source를 2차 검산하기 위해 작성되었다.

이 문서는 다음 판정으로 닫힌다.

```text
Hunminjeongeum Event는
단순 문자 이름이 아니라
문자체계,
책 / 문헌,
해례본 설명 구조,
제자원리,
운용 구조를 가진
formed structure 후보로 유지 가능하다.

그러나 이것은 final judgment가 아니라
source-supported provisional judgment이다.
```

---

다음회차:
Event / Context 적용 21회차

필요한 모드:
Thinking 확장

목적:
Path_Sejong_Hunminjeongeum source verification 1회차 — between-field / difference / 임계사이영역 source 검산
