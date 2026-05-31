# Rule.md

> 언어 기준: 한국어 원문

> main.branch Manifest candidate  
> 상태: 후보 초안  
> 기준: active_schema OS / current_rules.md  
> 목적: main.branch Manifest 안에서 SeungeFlow의 대표 작업규칙과 금지사항을 고정한다.

---

## 0. 이 문서의 자리

이 문서는 main.branch의 `Manifest/Rule.md` 후보 문서다.

이 문서는 전체 repository의 모든 규칙을 영구적으로 닫는 헌법이 아니다.

이 문서는 main.branch에서 SeungeFlow가 오독되지 않도록 하는 대표 rule guard다.

```text
Manifest/Rule.md =
representative rule guard
```

active_schema의 `current_rules.md`가 현재 OS의 작동규칙이라면, Manifest/Rule.md는 그 규칙을 main.branch에서 대표 문장으로 압축한 것이다.

```text
active_schema/current_rules.md =
current operating rules

main.branch/Manifest/Rule.md =
representative rule guard
```

---

## 1. 최상위 규칙

SeungeFlow의 최상위 규칙은 다음이다.

```text
내용보다 구조.
저장보다 이해.
요약보다 재진입.
증명보다 정렬.
파일경로보다 relation path.
목록보다 matrix.
원문 덮어쓰기보다 source 보존.
```

이 규칙들은 단순 슬로건이 아니다.

이 규칙들은 SeungeFlow를 잘못 읽지 않기 위한 최소 guard다.

---

## 2. 내용보다 구조

SeungeFlow는 내용을 먼저 채우는 방식으로 움직이지 않는다.

```text
content first X
structure first O
```

내용은 나중에 들어올 수 있다.

검색으로 들어올 수 있다.

AI vocab으로 들어올 수 있다.

seed_base source에서 들어올 수 있다.

그러나 구조가 없으면 내용은 흩어진다.

```text
구조 없음 =
내용이 흩어진다.

구조 있음 =
내용이 놓인다.
```

따라서 먼저 필요한 것은 구조체다.

---

## 3. 저장보다 이해

SeungeFlow의 문서는 저장 자체가 목적이 아니다.

문서는 이해된 지식이 외부로 펼쳐진 것이다.

```text
문서화 =
이해된 지식의 외부 전개
```

이해가 반복되면 각인이 된다.

```text
이해 + 이해 + 이해 + ...
=
각인
```

따라서 문서를 저장소로만 읽으면 안 된다.

문서는 이해와 각인이 밖으로 펼쳐진 자리다.

---

## 4. 요약보다 재진입

AI는 SeungeFlow를 요약 대상으로만 읽으면 안 된다.

```text
summary X
structure re-entry O
```

AI는 구조로 다시 들어가야 한다.

```text
AI =
structure re-entry operator
```

AI가 해야 할 일은 단순 요약이 아니라, Core / Path / meta / README 구조 안으로 재진입하여 현재 C가 어떻게 formed 되는지 읽는 것이다.

---

## 5. 증명보다 정렬

ComplexTest는 증명장이 아니다.

```text
ComplexTest ≠ proof claim
```

ComplexTest는 AI 인스턴스 정렬장이다.

```text
ComplexTest =
AI instance alignment field
```

따라서 ComplexTest를 난제 해결 주장으로 과장하면 안 된다.

또한 무의미한 실험으로 낮춰도 안 된다.

정확히는 다음이다.

```text
ComplexTest =
고강도 구조압력장을 통해
AI 인스턴스가 Ctp 구조원리와 구조연산식에 맞게
정렬되는지 보는 장
```

---

## 6. 파일경로보다 relation path

Path는 파일경로가 아니다.

```text
Path.md ≠ file path
Path.md = relation path
```

Path는 C와 C 사이에서 relation을 읽는다.

```text
C + C =
relation

C+1 =
relation으로 열린 다음 formed state
```

따라서 Path를 링크 목록, 목차, 파일경로 안내로 낮추면 안 된다.

Path는 relation path다.

---

## 7. 목록보다 matrix

Core는 목록이 아니다.

```text
Core.md ≠ category list
Core.md ≠ content table
Core.md = inside matrix
```

Core는 form들이 하나의 집합 안에서 수평배열과 수직관계, 스왑행렬과 내부 행렬곱셈을 통해 relation을 formed 하는 구조다.

```text
Core =
form set
+
logical matrix
+
internal relation rule
```

따라서 Core를 24개 항목 표로만 읽으면 안 된다.

`Core_01~Core_24`는 content slots가 아니라 form seats다.

```text
Core_01~Core_24 =
content slots X
form seats O
```

---

## 8. source 보존

source는 덮어쓰지 않는다.

```text
source preservation first
```

중요 source:

```text
seed_base/Structure_Principle/schema/
seed_base/SeungeFlow_Thinking/thinking_flow/
first_flow/navigation_map.md
epluone/BackData/
```

이 source들은 active_schema 산출물이나 epluone output으로 덮어쓰지 않는다.

source는 source로 보존하고, active_schema가 그 작동원리를 읽어 현재 구조로 변환한다.

---

## 9. branch role 보존

branch 역할을 섞지 않는다.

```text
main =
visible root

seed_base =
source memory

active_schema =
OS

epluone =
runtime factory

first_flow =
origin preservation
```

금지:

```text
main을 DB로 만들지 않는다.
seed_base를 runtime output으로 덮지 않는다.
active_schema를 archive로 만들지 않는다.
epluone을 representative root로 만들지 않는다.
first_flow를 삭제하지 않는다.
```

branch는 단순 Git 가지가 아니라 role-bearing structure field다.

---

## 10. README 3종 분리

README 3종은 서로 대체되지 않는다.

```text
README.md =
전체 대표 페이지

README_for_AI.md =
AI operation guard

README_for_SeungLee.md =
SeungLee-side principle page
```

금지:

```text
README.md를 단순 안내문으로 낮추지 않는다.
README_for_AI.md를 일반 AI 설명서로 만들지 않는다.
README_for_SeungLee.md를 개인 사용설명서로 만들지 않는다.
README 3종을 하나로 합쳐 역할을 지우지 않는다.
```

각 README는 서로 다른 관측기준을 가진다.

---

## 11. Ctp 읽기 규칙

C=tp를 단순 공식으로 읽지 않는다.

```text
C = t p
```

여기서 t는 시간만이 아니다.

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

p는 위치만이 아니다.

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

C=tp는 흐름과 자리가 하나의 장으로 formed 되는 상태다.

C=(m,t,p,?)는 C=tp를 폐기한 것이 아니라, 세부적으로 분해한 작동식이다.

```text
C=tp =
전체 흐름식

C=(m,t,p,?) =
분해·분석·검증·확인·의심의 순환식
```

---

## 12. ? 읽기 규칙

`?`는 단순 질문표가 아니다.

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

`?`는 `(m,t,p)` 바깥에만 있지 않다.

```text
? ∩ m 가능
? ∩ t 가능
? ∩ p 가능
? ∩ (m,t,p) 가능
```

따라서 관측기준은 target, flow, field 안에 겹쳐 놓일 수 있다.

---

## 13. 9dot0 읽기 규칙

9dot0는 단순 숫자 배열이 아니다.

```text
9 dot 0
```

9는 끝점이다.

0은 다음 시작점이다.

dot은 끝점과 시작점 사이의 무한한 잠재가능성이다.

```text
9dot0 =
극한임계전이
=
하나의 dot
=
임계사이영역
```

dot은 단순 점이 아니다.

dot은 관측자의 시선과 경계에 따라 점, 선, 면, 공간으로 드러날 수 있는 잠재장이다.

---

## 14. 역발상 규칙

역발상은 반대로 생각하기가 아니다.

```text
역발상 ≠ 반대 의견
역발상 ≠ 거꾸로 말하기
역발상 ≠ 기존 해석 부정
```

역발상은 구조를 돌리는 것이 아니라 관측자의 시선을 돌리는 것이다.

```text
역발상 =
관측자의 시선 이동
+
기점 이동
+
경계 이동
+
?의 이동
```

구조는 단방향으로 이어진다.

역검산도 구조를 뒤로 돌리는 것이 아니라, 관측자의 시선이 돌아가는 것이다.

---

## 15. 렌더링 트랙 분리

렌더링 트랙은 별도다.

```text
gpt.gemini ~ gemini.direct =
rendering theory / rendering implementation Framework OS track
```

임시 위치:

```text
epluone/Ctp24_rendering/
```

gpt.direct는 이 렌더링 구현 트랙에 들어가지 않는다.

```text
gpt.direct =
Ctp24 구조원리 / 구조연산기 / active_schema OS 설계
```

렌더링 트랙은 contextual awareness로만 둔다.

---

## 16. 금지사항 요약

```text
1. seed_base를 덮어쓰지 않는다.
2. first_flow를 삭제하지 않는다.
3. BackData를 minor folder로 낮추지 않는다.
4. ComplexTest를 proof claim으로 읽지 않는다.
5. Core를 목록으로 만들지 않는다.
6. Path를 file path로 만들지 않는다.
7. README 3종을 합치지 않는다.
8. epluone output을 main 최종본으로 착각하지 않는다.
9. active_schema를 archive로 만들지 않는다.
10. gpt.direct를 rendering implementation으로 끌고 가지 않는다.
```

---

## 17. 허용사항 요약

```text
1. seed_base를 source memory로 읽는다.
2. first_flow를 origin/proto Path로 읽는다.
3. epluone output을 runtime output source로 참조한다.
4. active_schema에서 작동형으로 재해석한다.
5. main.branch에는 대표 구조 후보만 올린다.
6. Core를 inside matrix로 운영한다.
7. Path를 relation path로 운영한다.
8. 검색과 vocab은 구조가 선 뒤에 넣는다.
9. AI는 structure re-entry operator로 작동한다.
10. 문서는 이해된 지식의 외부 전개로 읽는다.
```

---

## 18. Closing

Rule.md fixes the representative operating rules inside the main.branch Manifest.

```text
structure before content
understanding before storage
re-entry before summary
alignment before proof
relation path before file path
matrix before list
source preservation before overwrite
```

These rules protect SeungeFlow from structural misreading.