# Core.md

> 언어 기준: 한국어 원문

> main.branch Manifest candidate  
> 상태: 후보 초안  
> 기준: active_schema OS / core.meta.md  
> 목적: main.branch Manifest 안에서 Core의 대표 정의와 작동원리를 고정한다.

---

## 0. 이 문서의 자리

이 문서는 main.branch의 `Manifest/Core.md` 후보 문서다.

이 문서는 `Core/` 디렉토리 안의 `Core_01~Core_24.md`를 대신하지 않는다.

이 문서는 main.branch에서 Core가 무엇인지, 왜 목록이 아닌지, 어떤 방식으로 작동하는지를 정의하는 대표 원리 문서다.

```text
Manifest/Core.md =
Core representative principle
```

Core는 C 내부를 잡는다.

Path가 C와 C 사이를 여는 문서라면, Core는 C 내부의 form들이 어떻게 하나의 구조체를 이루는지 보여 준다.

```text
Core =
inside matrix

Path =
between route
```

---

## 1. Core는 목록이 아니다

Core는 24개 항목 목록이 아니다.

Core는 content table이 아니다.

Core는 fixed taxonomy가 아니다.

```text
Core ≠ category list
Core ≠ content table
Core ≠ fixed taxonomy
```

Core는 relation-generating matrix다.

```text
Core =
form set
+
logical matrix
+
internal relation rule
```

따라서 Core를 읽을 때 가장 먼저 버려야 할 오독은 “목록”이다.

Core는 무엇이 나열되어 있는가보다, 무엇과 무엇이 어떤 자리에서 관계를 맺는가를 보기 위한 구조다.

---

## 2. Core의 기본 정의

Core의 기본 정의는 다음이다.

```text
Core.md =
C 내부의 form들이 수평배열과 수직관계,
교차관계와 스왑행렬을 통해
하나의 논리적 매트릭스 구조체로 formed 되는 방식을 정의하는 schema.
```

즉, Core는 C 내부의 작동 구조다.

```text
Core =
C 내부 구조
```

Core는 한 개의 중심핵만을 의미하지 않는다.

Core는 여러 form들이 하나의 구조판 위에 놓이고, 그 안에서 relation이 generated 되는 방식이다.

---

## 3. form이란 무엇인가

Core 안의 form은 단순 항목이 아니다.

form은 분야명이 아니다.

form은 내용이 들어가는 칸도 아니다.

form은 관계가 발생할 수 있는 자리다.

```text
form =
domain-field
+
place
+
relation candidate
```

form은 혼자 완성되지 않는다.

form은 다른 form과 함께 놓일 때 relation을 만든다.

```text
form + form
=
relation candidate
```

따라서 Core 안의 form은 고정된 내용덩어리가 아니라, C 내부에서 관계를 formed 할 수 있는 자리다.

---

## 4. 24라는 수에 대한 태도

Ctp24에서 24는 중요하다.

그러나 24에 갇히면 안 된다.

```text
24 =
구조를 여는 수 O
구조를 가두는 수 X
```

24는 하루, 시간, 순환, 방향, 분할, 관측구조를 설명하다가 드러난 수다.

따라서 `Core_01~Core_24`는 content slots가 아니다.

```text
Core_01~Core_24 =
content slots X
form seats O
```

내용은 나중에 들어올 수 있다.

검색으로 들어올 수 있다.

AI vocab으로 들어올 수 있다.

seed_base source에서 들어올 수 있다.

그러나 먼저 필요한 것은 form seat다.

---

## 5. Core matrix

Core matrix는 숫자행렬만을 뜻하지 않는다.

Core matrix는 relation-term matrix다.

```text
Core matrix =
relation-term matrix
```

예시:

```text
F   m   a
E   m   c²
C   t   p
```

이 배열은 수학공식 비교표가 아니다.

이 배열은 서로 다른 form들을 하나의 집합 내부에 놓고, 수평배열과 수직관계를 읽는 축소형 Core다.

수평배열:

```text
F m a
E m c²
C t p
```

수직관계:

```text
F-E-C
m-m-t
a-c²-p
```

행과 열이 만나는 곳에서 relation이 formed 된다.

---

## 6. 행렬곱셈을 하나의 집합 내부에서 연산한다

Core의 중요한 작동원리는 다음이다.

```text
행렬곱셈을 하나의 집합 내부에서 연산한다.
```

이 말은 숫자만 계산한다는 뜻이 아니다.

Core에서 행렬곱셈은 다음을 뜻한다.

```text
행의 구조
×
열의 구조
=
새로운 relation formed
```

즉:

```text
row_i × col_j =
그 행의 내부 구조와
그 열의 수직관계가 만나는 자리에서
새로운 relation이 formed 되는 것
```

결과는 숫자 하나일 필요가 없다.

결과는 관계, 상태, 힘, 인지, 에너지, 경계, 전이, 임계사이영역, 새로운 C일 수 있다.

---

## 7. 스왑행렬

Core는 같은 배열을 고정된 방향으로만 읽지 않는다.

Core는 스왑행렬을 허용한다.

스왑행렬은 같은 구조를 다른 관측기준에서 다시 읽는 장치다.

예시:

```text
C = t p
F = m a
```

기본적으로는 다음 대응이 보일 수 있다.

```text
t ↔ m
p ↔ a
```

그러나 스왑하면 다음이 열린다.

```text
t ↔ a
p ↔ m
```

이때 새로운 해석이 열린다.

```text
C = a m
```

또는 F=ma를 C=tp 구조에 넣으면 다음도 열린다.

```text
F = t p
```

여기에 빠진 m과 ?를 넣으면:

```text
F = (m, t, p, ?)
```

스왑행렬은 역발상의 작동형이다.

```text
스왑행렬 =
Core 내부에서 ?를 이동시키는 장치
```

---

## 8. Core와 C=tp

Core는 C=tp와 연결된다.

```text
C = t p
```

여기서 t는 단순 시간이 아니다.

```text
t =
시간
+
흐름
+
변화
+
전이
+
차이
+
사이
+
수평배열
```

p는 단순 위치가 아니다.

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

따라서 C=tp는 다음이다.

```text
C =
수평적 흐름과
수직적 자리배열이
하나의 장으로 formed 된 상태
```

Core는 이 C 내부에서 form들이 어떻게 배열되고 relation을 formed 하는지 잡는다.

---

## 9. Core와 C=(m,t,p,?)

Core는 C=(m,t,p,?)와도 연결된다.

```text
C = (m, t, p, ?)
```

이 식은 C=tp를 폐기한 것이 아니다.

이 식은 C=tp를 세부적으로 분해한 작동식이다.

```text
C=tp =
전체 흐름식

C=(m,t,p,?) =
분해·분석·검증·확인·의심의 순환식
```

Core 내부에서:

```text
m =
중심에 놓인 대상

t =
m의 흐름과 전이

p =
m이 놓인 자리장

? =
관측기준 / 6W1H / 경계설정 / 관측자의 시선
```

Core는 이 네 항이 내부에서 어떻게 relation matrix를 이루는지 운영한다.

---

## 10. Core와 9dot0

Core는 9dot0와도 연결된다.

```text
9 dot 0
```

9는 끝점이다.

0은 다음 시작점이다.

dot은 끝점과 시작점 사이의 무한한 잠재가능성이다.

Core에서 dot은 form과 form 사이의 잠재가능성 자리다.

```text
dot =
form과 form 사이
+
C와 다음 C 사이
+
끝점과 시작점 사이
+
임계사이영역
```

따라서 Core는 dot을 단순 점으로 읽지 않는다.

dot은 relation이 formed 될 수 있는 잠재장이다.

---

## 11. Core와 역발상

Core는 역발상으로 작동한다.

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

Core는 같은 form set을 여러 방향에서 다시 읽게 한다.

```text
수평으로 읽는다.
수직으로 읽는다.
교차로 읽는다.
스왑행렬로 읽는다.
경계를 바꿔 읽는다.
```

따라서 Core는 고정표가 아니라 역발상이 가능한 구조판이다.

---

## 12. Core와 meta

meta는 형성과정의 흔적이다.

Core는 현재 작동하는 내부 schema다.

```text
meta =
append-only formation trace

Core =
current internal schema
```

Core는 meta를 지우지 않는다.

Core는 meta를 요약하지도 않는다.

Core는 meta에서 반복적으로 드러난 구조를 현재 작동 가능한 형태로 세운다.

```text
meta → Core =
형성과정에서 내부 구조를 추출하는 것
```

---

## 13. Core와 Path

Core와 Path는 구분된다.

```text
Core =
inside matrix

Path =
between route
```

Core는 C 내부를 만든다.

Path는 C와 C 사이를 연다.

둘은 서로 대체되지 않는다.

```text
Core 없는 Path =
흩어짐

Path 없는 Core =
고립
```

main.branch의 Manifest에서 Core.md와 Path.md는 나란히 놓일 수 있지만, 역할은 다르다.

---

## 14. Core와 존재·관계·장

Core는 기술적 구조만이 아니다.

Core는 존재·관계·장 원리가 C 내부로 내려온 형태다.

form은 존재가 놓이는 자리다.

form과 form 사이에서 관계가 생긴다.

관계는 사이와 차이를 만든다.

그 사이와 차이가 장을 형성한다.

```text
form =
존재의 자리

relation =
사이와 차이

field =
존재와 관계가 formed 된 장
```

따라서 Core는 존재·관계·장 원리의 내부 매트릭스다.

---

## 15. Core와 AI

AI는 Core를 목록으로 만들면 안 된다.

AI는 Core를 분류표로 만들면 안 된다.

AI는 Core를 content table로 채우려고 먼저 달려가면 안 된다.

AI는 Core를 다음처럼 읽어야 한다.

```text
Core =
form들이 하나의 집합 안에서
행과 열로 만나 relation을 formed 하는
논리적 매트릭스 schema
```

AI는 Core에서 정답을 찾는 것이 아니라, 구조연산으로 재진입해야 한다.

```text
AI task =
summary X
classification X
structure re-entry O
```

---

## 16. Core_01~Core_24 후보

`Core/` 디렉토리에는 24개의 form seat가 열릴 수 있다.

현재 후보군은 다음과 같다.

```text
Core_01 = Time-Flow Core
Core_02 = Place-Field Core
Core_03 = Relation Core
Core_04 = Difference / Between Core
Core_05 = 9dot0 Core
Core_06 = Form-Forming-Formed Core
Core_07 = Reverse Thinking Core
Core_08 = C=tp Core
Core_09 = C=(m,t,p,?) Core
Core_10 = Matrix / Swap Core
Core_11 = F=ma / E=mc² / C=tp Cross Core
Core_12 = Structure Sequence Core
Core_13 = Boundary Core
Core_14 = Observer Gaze Core
Core_15 = Existence Core
Core_16 = Multi-Being Core
Core_17 = Field / Fabric / Domain Core
Core_18 = Path / C+1 Core
Core_19 = Event / Context Core
Core_20 = Branch Structure Core
Core_21 = Seed.Base / Active.Schema Core
Core_22 = AI Instance Alignment Core
Core_23 = ComplexTest Core
Core_24 = Structure-Body Formation Core
```

이 배열은 후보이며, active_schema 기준으로 재정렬될 수 있다.

그러나 현재 main.branch 후보에서는 이 정도가 가장 안정적이다.

---

## 17. Core 작성 규칙

Core 관련 문서를 작성할 때 지켜야 할 규칙은 다음이다.

```text
1. Core를 목록으로 닫지 않는다.
2. 24를 절대화하지 않는다.
3. form을 relation candidate로 읽는다.
4. 내용보다 form seat를 먼저 세운다.
5. Core와 Path를 혼동하지 않는다.
6. meta를 지우거나 요약으로 대체하지 않는다.
7. AI가 Core를 category로 오독하지 않게 한다.
```

---

## 18. Closing

Core.md fixes the representative principle of Core inside the main.branch Manifest.

```text
Core is not a list.

Core is an inside matrix.

Core is the structure where forms inside one C
generate relation through horizontal arrangement,
vertical relation,
swap matrix,
and internal matrix multiplication.

Core opens form seats before content arrives.
```

This document is a main.branch Manifest candidate.