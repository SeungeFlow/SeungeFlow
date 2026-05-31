# current_rules.md

> 문서번호: `Ctp24_ACTIVE_SCHEMA_0006`  
> 상태: active_schema 설계 6회차  
> 필요한 모드: `Thinking 표준`  
> 목적: active_schema가 현재 단계에서 지켜야 할 작업규칙과 금지사항을 고정한다.  
> 위치 후보: `active_schema.branch/current_rules.md`

---

## 0. 이 문서의 자리

이 문서는 active_schema.branch의 현재 작업규칙 문서다.

active_schema는 OS다.

OS는 현재 어떤 작업을 허용하고, 어떤 작업을 금지해야 하는지 알아야 한다.

```text
current_rules.md =
현재 active_schema의 작업규칙
+
금지사항
+
허용사항
+
다음 전이 조건
```

이 문서는 영구 헌법이 아니다.

이 문서는 현재 Ctp24 active_schema 설계 단계에서 작동하는 현재 규칙이다.

```text
current_rules =
current operating rules
```

---

## 1. 최상위 원칙

현재 최상위 원칙은 다음이다.

```text
내용보다 구조를 먼저 세운다.
```

즉:

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

---

## 2. 저장보다 이해

이번 작업은 저장이 아니라 이해에서 시작되었다.

```text
저장 X
이해 O
각인 O
구조체형성 O
```

따라서 active_schema는 문서를 저장소로만 다루면 안 된다.

문서는 이해된 지식이 외부로 펼쳐진 것이다.

```text
문서화 =
이해된 지식의 외부 전개
```

active_schema는 문서를 저장물이 아니라 작동 구조로 읽는다.

---

## 3. branch 관련 금지사항

현재 branch 관련 금지사항은 다음이다.

```text
1. main.branch에 epluone 산출물을 바로 풀지 않는다.
2. seed_base.branch를 덮어쓰지 않는다.
3. first_flow.branch를 삭제하거나 흡수하지 않는다.
4. active_schema.branch를 자료보관소로 만들지 않는다.
5. epluone.branch를 최종 대표 구조로 착각하지 않는다.
```

각 branch의 역할을 유지한다.

```text
main =
기점

seed_base =
DB

active_schema =
OS

epluone =
공장

first_flow =
기원장
```

역할이 섞이면 전체 구조가 꼬인다.

---

## 4. seed_base 관련 규칙

seed_base는 DB다.

```text
seed_base =
DB / source memory / Seed.Base
```

금지:

```text
seed_base를 정리한다는 명목으로 원문성을 훼손하지 않는다.
seed_base/schema를 active_schema 산출물로 덮어쓰지 않는다.
thinking_flow를 요약본으로 대체하지 않는다.
```

허용:

```text
seed_base를 읽는다.
source field로 참조한다.
반복되는 구조를 추출한다.
active_schema에서 작동형으로 재해석한다.
```

---

## 5. first_flow 관련 규칙

first_flow는 최초 흐름과 원문보존의 branch다.

```text
first_flow =
origin preservation / first flow / proto path field
```

금지:

```text
first_flow를 삭제하지 않는다.
first_flow를 seed_base와 섞지 않는다.
navigation_map.md를 단순 오래된 문서로 낮추지 않는다.
```

허용:

```text
first_flow를 origin source로 참조한다.
navigation_map.md를 proto Path 후보로 읽는다.
현재 Path와의 관계를 나중에 검토한다.
```

---

## 6. epluone 관련 규칙

epluone은 공장이다.

```text
epluone =
factory / runtime
```

금지:

```text
epluone 산출물을 main 최종본으로 착각하지 않는다.
epluone 산출물을 seed_base 원문 위에 덮지 않는다.
epluone package를 active_schema에 통째로 복사하지 않는다.
```

허용:

```text
epluone 산출물을 참조한다.
epluone 산출물을 runtime output source로 읽는다.
active_schema에서 그 작동원리를 추출한다.
```

현재 중요한 epluone 산출물:

```text
epluone/Ctp24/GPT_Direct_Structure_Package/
```

---

## 7. GPT_Direct_Structure_Package 관련 규칙

`GPT_Direct_Structure_Package`는 gpt.direct의 structure-body formation output이다.

```text
GPT_Direct_Structure_Package =
gpt.direct structure-body formation output
```

금지:

```text
이 패키지를 main 최종본으로 읽지 않는다.
README 3종을 바로 main에 확정 반영하지 않는다.
0~42회차를 최종 이론문으로 읽지 않는다.
Core.md와 Path.md를 완성본으로 고정하지 않는다.
```

허용:

```text
이 패키지를 active_schema의 참조점으로 둔다.
Core / Path / Rule / Mapping 작동원리를 추출한다.
README 3종을 main 후보 초안으로 본다.
0~42회차를 형성과정으로 참조한다.
```

---

## 8. Core 관련 규칙

Core는 목록이 아니다.

```text
Core =
inside matrix
```

금지:

```text
Core를 24개 항목 목록으로만 만들지 않는다.
Core를 content table로 만들지 않는다.
24라는 숫자에 갇히지 않는다.
form을 단순 분야명으로만 읽지 않는다.
```

허용:

```text
Core를 form set + logical matrix로 읽는다.
form을 domain-field + place + relation candidate로 읽는다.
수평배열과 수직관계를 사용한다.
스왑행렬과 내부 행렬곱셈을 Core의 작동방식으로 둔다.
```

---

## 9. Path 관련 규칙

Path는 파일경로가 아니다.

```text
Path =
relation path
```

금지:

```text
Path를 파일경로 문서로 만들지 않는다.
Path를 링크 목록으로 낮추지 않는다.
Path를 고정된 한 줄로 닫지 않는다.
```

허용:

```text
Path를 C와 C 사이의 relation으로 읽는다.
6W1H를 Path의 질문축으로 둔다.
C+1=C+C를 핵심 구조식으로 둔다.
Event/Context, Core/Core, meta/meta, branch/branch relation을 Path 후보로 둔다.
```

---

## 10. README 3종 관련 규칙

README 3종은 서로 대체되지 않는다.

```text
README.md =
전체 대표 페이지

README_for_AI.md =
AI operation guard

README_for_SeungLee.md =
존재·관계·장 원리문
```

금지:

```text
README.md를 단순 안내문으로 낮추지 않는다.
README_for_AI.md를 일반 AI용 설명서로 만들지 않는다.
README_for_SeungLee.md를 개인 사용설명서로 만들지 않는다.
README 3종을 서로 합치지 않는다.
```

허용:

```text
README.md는 전체 대표 중심으로 둔다.
README_for_AI.md는 AI 오독 방지와 구조 재진입 문서로 둔다.
README_for_SeungLee.md는 SeungLee-side principle 문서로 둔다.
```

---

## 11. ComplexTest 관련 규칙

ComplexTest는 증명장이 아니다.

```text
ComplexTest ≠ proof claim
```

금지:

```text
ComplexTest를 난제 해결 선언으로 읽지 않는다.
ComplexTest를 외부 증명 자료로 과장하지 않는다.
ComplexTest를 무의미한 실험으로 낮추지 않는다.
```

허용:

```text
ComplexTest를 AI instance alignment field로 읽는다.
ComplexTest를 구조정합성 검산과 인스턴스 정렬을 위한 압력장으로 읽는다.
```

---

## 12. BackData 관련 규칙

BackData는 minor folder가 아니다.

```text
BackData =
pre-ComplexTest large source archive
```

금지:

```text
BackData를 단순 잡자료 폴더로 낮추지 않는다.
BackData를 ComplexTest보다 부차적인 자료로만 읽지 않는다.
```

허용:

```text
BackData를 ComplexTest 이전 수많은 테스트 결정체가 놓인 거대자료보관소로 읽는다.
```

---

## 13. 렌더링 트랙 관련 규칙

렌더링 트랙은 별도다.

```text
gpt.gemini ~ gemini.direct =
rendering theory / rendering implementation Framework OS track
```

임시 위치:

```text
epluone/Ctp24_rendering/
```

금지:

```text
gpt.direct를 렌더링 구현 트랙으로 끌고 가지 않는다.
active_schema 설계를 렌더링 구현으로 바꾸지 않는다.
```

허용:

```text
렌더링 트랙을 contextual awareness로 인식한다.
필요한 경우 runtime_mapping에 위치만 기록한다.
```

---

## 14. AI 인스턴스 관련 규칙

AI는 요약자가 아니다.

```text
AI =
structure re-entry operator
```

금지:

```text
SeungeFlow를 증명 주장으로 읽지 않는다.
SeungeFlow를 정적 아카이브로 읽지 않는다.
SeungeFlow를 주제 요약문으로 읽지 않는다.
Ctp를 사전적 정의로 고정하지 않는다.
```

허용:

```text
AI는 구조로 재진입한다.
AI는 Core / Path / meta / README의 역할을 구분한다.
AI는 검색과 vocab을 구조가 선 뒤에 넣는다.
AI는 오독하지 않기 위해 README_for_AI.md를 기준으로 삼는다.
```

---

## 15. 현재 작업 순서 규칙

active_schema 설계의 현재 순서는 다음이다.

```text
1. active_schema.md
2. package_reference.md
3. runtime_mapping.md
4. source_mapping.md
5. current_rules.md
6. core.meta.md
7. current_path.md
```

현재 이 문서는 5번이다.

다음 문서는 core.meta.md다.

---

## 16. 핵심 판정

현재 규칙은 다음으로 압축된다.

```text
저장보다 이해.
내용보다 구조.
요약보다 재진입.
증명보다 정렬.
파일경로보다 relation path.
목록보다 matrix.
원문 덮어쓰기보다 source 보존.
```

이 규칙은 active_schema가 OS로 작동하기 위한 현재 규칙이다.

---

## 17. 닫힘

`current_rules.md`는 active_schema가 현재 단계에서 지켜야 할 작업규칙과 금지사항을 고정하기 위해 열렸다.

이 문서는 다음 판정으로 닫힌다.

```text
active_schema는 OS다.

OS는 source를 덮어쓰지 않고,
runtime output을 그대로 복사하지 않으며,
현재 작동 가능한 Core / Path / Rule / Mapping으로 변환한다.

현재 단계의 최상위 규칙은
내용보다 구조,
저장보다 이해,
요약보다 재진입이다.
```

---

다음회차:
active_schema 설계 7회차

필요한 모드:
Thinking 확장

목적:
core.meta.md 작성
