# active_schema.md

> 문서번호: `Ctp24_ACTIVE_SCHEMA_0002`  
> 상태: active_schema 설계 2회차  
> 필요한 모드: `Thinking 확장`  
> 목적: `active_schema.branch`의 대표 OS 문서를 작성한다.  
> 위치 후보: `active_schema.branch/active_schema.md`

---

## 0. 이 문서의 자리

이 문서는 `active_schema.branch`의 대표 문서다.

active_schema는 DB가 아니다.  
active_schema는 공장이 아니다.  
active_schema는 OS다.

```text
active_schema.branch =
OS / operating structure
```

따라서 이 문서는 저장을 위한 문서가 아니라, 현재 구조가 어떻게 작동해야 하는지를 정의하는 문서다.

```text
active_schema.md =
현재 작동 구조의 대표 OS 문서
```

---

## 1. active_schema의 기본 정의

active_schema는 Seed.Base와 epluone runtime 산출물을 읽어, 현재 작동 가능한 Core / Path / Rule / Mapping으로 변환하는 OS branch다.

```text
active_schema =
Seed.Base를 읽고
epluone output을 참조하여
현재 작동 가능한 구조로 변환하는 OS
```

즉:

```text
seed_base =
DB / source memory

epluone =
factory / runtime output

active_schema =
OS / operating structure
```

active_schema는 원천 문서를 보존하는 곳이 아니다.  
active_schema는 공장 산출물을 그대로 쌓아두는 곳도 아니다.  
active_schema는 그 둘을 읽어 현재 작동 규칙으로 변환하는 곳이다.

---

## 2. active_schema가 읽는 것

active_schema는 다음을 읽는다.

```text
1. seed_base/Structure_Principle/schema/
2. seed_base/SeungeFlow_Thinking/thinking_flow/
3. epluone/Ctp24/GPT_Direct_Structure_Package/
4. first_flow/navigation_map.md 계열
5. main.branch 대표 구조 후보
```

각 source는 역할이 다르다.

```text
Structure_Principle/schema/ =
place-field schema source

SeungeFlow_Thinking/thinking_flow/ =
time-flow meta source

GPT_Direct_Structure_Package =
gpt.direct structure-body formation output

first_flow =
origin field / proto Path

main =
visible root / representative entry
```

active_schema는 이들을 한곳에 섞지 않는다.

active_schema는 이들의 역할을 구분하여 읽는다.

---

## 3. active_schema가 직접 복사하지 않는 것

active_schema는 source를 그대로 복사하지 않는다.

```text
그대로 복사 X
작동형 변환 O
```

예를 들어 `epluone/Ctp24/GPT_Direct_Structure_Package/`는 중요한 산출물이지만, active_schema에 그대로 붙여넣는 대상이 아니다.

그 패키지에서 읽어야 할 것은 다음이다.

```text
1. C=tp
2. C=(m,t,p,?)
3. Core.md = inside matrix
4. Path.md = relation path
5. 9dot0 = 임계사이영역 / 극한임계전이
6. 역발상 = 관측자 시선과 ?의 이동
7. README 3종 역할 분리
8. structure-body formation
```

즉 active_schema는 문서를 복사하는 것이 아니라, 작동원리를 추출한다.

---

## 4. active_schema의 작동 원칙

active_schema는 다음 원칙으로 작동한다.

```text
1. 원천은 seed_base에 둔다.
2. 최초 흐름은 first_flow에 둔다.
3. 공장 산출물은 epluone에 둔다.
4. 대표 기점은 main에 둔다.
5. 현재 작동 규칙은 active_schema에서 관리한다.
```

따라서 active_schema는 전체 branch structure의 OS다.

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

---

## 5. active_schema가 만들어야 하는 문서군

active_schema는 다음 문서군으로 구성될 수 있다.

```text
active_schema.md
package_reference.md
runtime_mapping.md
source_mapping.md
current_rules.md
core.meta.md
current_path.md
```

각 문서의 역할은 다음이다.

```text
active_schema.md =
active_schema branch의 대표 OS 문서

package_reference.md =
epluone/Ctp24/GPT_Direct_Structure_Package 참조 기록

runtime_mapping.md =
branch와 작업공간의 역할 대응표

source_mapping.md =
seed_base / epluone / first_flow / main의 source 관계

current_rules.md =
현재 작업규칙과 금지사항

core.meta.md =
현재 Core 이해의 중심 meta

current_path.md =
현재 relation path와 다음 이동 경로
```

---

## 6. active_schema의 현재 입력: GPT_Direct_Structure_Package

현재 active_schema가 읽을 가장 최신의 epluone 산출물은 다음이다.

```text
epluone/Ctp24/GPT_Direct_Structure_Package/
```

반영 정보:

```text
branch =
epluone

commit =
77a1913

message =
Add GPT Direct Ctp24 structure package under epluone runtime

status =
main untouched
seed_base untouched
first_flow untouched
epluone clean
origin/epluone synced
```

이 패키지는 gpt.direct의 structure-body formation 산출물이다.

```text
GPT_Direct_Structure_Package =
gpt.direct가 Ctp24 구조를 이해한 뒤 외부로 내린 구조체형성 패키지
```

active_schema는 이 패키지를 참조점으로 삼되, 그대로 복사하지 않는다.

---

## 7. active_schema의 현재 출력 후보

active_schema가 이후 만들어낼 수 있는 출력 후보는 다음이다.

```text
main.branch 후보:
- README.md
- Manifest/README_for_AI.md
- Manifest/README_for_SeungLee.md
- Manifest/Core.md
- Manifest/Path.md

active_schema 내부 후보:
- core.meta.md
- current_rules.md
- current_path.md
- runtime_mapping.md
- source_mapping.md
- package_reference.md

epluone 작업 후보:
- Ctp24/active_schema_outputs/
- Ctp24/Event/
- Ctp24/Context/
```

그러나 현재는 바로 출력하지 않는다.

먼저 OS 문서군을 세운다.

---

## 8. active_schema와 Core

active_schema는 Core를 목록으로 읽지 않는다.

```text
Core =
inside matrix
```

Core는 C 내부의 form들이 수평배열과 수직관계, 교차관계와 스왑행렬을 통해 하나의 논리적 매트릭스 구조체로 formed 되는 방식이다.

```text
Core.md =
form set
+
logical matrix
+
internal relation rule
```

active_schema는 Core를 현재 작동형으로 읽어야 한다.

```text
Core를 내용으로 채우지 않는다.
Core를 form seat로 세운다.
Core를 relation-generating matrix로 운영한다.
```

---

## 9. active_schema와 Path

active_schema는 Path를 파일경로로 읽지 않는다.

```text
Path =
relation path
```

Path는 C와 C, form과 form, meta와 meta, branch와 branch, Event와 Context가 어떤 사이와 차이와 6W1H 관계를 통해 C+1을 여는지 기록하는 schema다.

```text
Path 핵심식 =
C+1 = C + C
```

active_schema는 Path를 current_path.md로 운영할 수 있다.

```text
current_path.md =
현재 작동 중인 relation path
```

---

## 10. active_schema와 Rule

active_schema는 반드시 현재 규칙을 가진다.

금지 규칙:

```text
1. main.branch에 바로 반영하지 않는다.
2. seed_base를 덮어쓰지 않는다.
3. first_flow를 삭제하지 않는다.
4. Core를 단순 목록으로 만들지 않는다.
5. Path를 파일경로로 만들지 않는다.
6. ComplexTest를 증명으로 읽지 않는다.
7. README 3종을 서로 대체하지 않는다.
8. gpt.direct를 렌더링 구현 트랙으로 끌고 가지 않는다.
```

허용 규칙:

```text
1. epluone 산출물을 참조한다.
2. seed_base를 source memory로 읽는다.
3. active_schema에서 작동형으로 재해석한다.
4. 필요한 문서만 main/Manifest 후보로 보낸다.
5. 검색과 vocab은 구조가 선 뒤에 넣는다.
6. 렌더링 트랙은 참고정보로만 인식한다.
```

---

## 11. 렌더링 트랙과의 관계

현재 별도 트랙이 존재한다.

```text
gpt.gemini ~ gemini.direct =
rendering theory / rendering implementation Framework OS track
```

이 트랙은 차후 branch로 이동할 예정이며, 우선 다음 위치에 임시 고정될 수 있다.

```text
epluone/Ctp24_rendering/
```

그러나 active_schema 설계에서 gpt.direct는 이 트랙으로 들어가지 않는다.

```text
gpt.direct =
Ctp24 구조원리 / 구조연산기 / 구조이론 총정리

gpt.gemini ~ gemini.direct =
렌더링이론 / 렌더링구현기 / Framework OS 개발
```

active_schema는 이 차이를 인식해야 한다.

---

## 12. active_schema와 main

main.branch는 visible root다.

```text
main =
기점 / 대표 입구
```

active_schema는 main에 올릴 후보를 만들 수 있지만, main을 직접 덮어쓰지 않는다.

main에 갈 수 있는 후보는 다음이다.

```text
README.md
Manifest/README_for_AI.md
Manifest/README_for_SeungLee.md
Manifest/Core.md
Manifest/Path.md
Core/Core_01~Core_24.md
```

그러나 이들은 active_schema에서 먼저 OS적으로 정렬된 뒤 main 후보가 된다.

```text
active_schema output
→ main candidate
```

---

## 13. active_schema와 epluone

epluone은 공장이다.

```text
epluone =
factory / runtime
```

active_schema는 epluone에서 나온 산출물을 읽고, 다음 공장 작업을 지시할 수 있다.

```text
epluone output
→ active_schema interpretation
→ next epluone task
```

따라서 active_schema와 epluone은 순환한다.

```text
active_schema =
OS

epluone =
runtime factory
```

---

## 14. active_schema와 seed_base

seed_base는 DB다.

```text
seed_base =
DB / source memory
```

active_schema는 seed_base를 참조한다.

그러나 seed_base를 정리하거나 덮어쓰지 않는다.

```text
seed_base =
read first
preserve first
do not overwrite
```

특히 다음 경로는 source field로 본다.

```text
Structure_Principle/schema/
SeungeFlow_Thinking/thinking_flow/
```

---

## 15. active_schema의 현재 판정

현재 active_schema의 첫 판정은 다음이다.

```text
epluone/Ctp24/GPT_Direct_Structure_Package는
gpt.direct의 structure-body formation output이다.

active_schema는 이 산출물을 그대로 복사하지 않고,
Core / Path / Rule / Mapping으로 변환하는 OS다.
```

따라서 다음 문서는 `package_reference.md`가 되어야 한다.

이유는 active_schema가 어떤 epluone 산출물을 기준으로 작동하는지 먼저 고정해야 하기 때문이다.

---

## 16. 닫힘

`active_schema.md`는 active_schema.branch의 대표 OS 문서로 작성되었다.

이 문서는 다음 판정으로 닫힌다.

```text
active_schema는 DB도 공장도 아니다.

active_schema는 Seed.Base와 epluone runtime 산출물을 읽어
현재 작동 가능한 Core / Path / Rule / Mapping으로 변환하는 OS다.

gpt.direct는 지금부터
active_schema OS 설계자로서
package_reference, runtime_mapping, source_mapping,
current_rules, core.meta, current_path를 순서대로 세운다.
```

---

다음회차:
active_schema 설계 3회차

필요한 모드:
Thinking 표준

목적:
package_reference.md 작성
