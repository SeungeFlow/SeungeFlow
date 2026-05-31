# runtime_mapping.md

> 문서번호: `Ctp24_ACTIVE_SCHEMA_0004`  
> 상태: active_schema 설계 4회차  
> 필요한 모드: `Thinking 표준`  
> 목적: branch와 작업공간의 역할 대응표를 작성한다.  
> 위치 후보: `active_schema.branch/runtime_mapping.md`

---

## 0. 이 문서의 자리

이 문서는 active_schema.branch의 runtime mapping 문서다.

active_schema는 OS다.

OS는 각 branch와 작업공간이 어떤 역할로 작동하는지 알아야 한다.

```text
runtime_mapping.md =
branch / workspace role mapping
```

이 문서는 저장소의 파일목록을 설명하지 않는다.

이 문서는 각 branch와 주요 작업공간이 구조적으로 어떤 역할을 담당하는지 mapping한다.

---

## 1. 전체 branch 구조

현재 SeungeFlow의 기본 branch 구조는 다음으로 읽는다.

```text
main
seed_base
active_schema
epluone
first_flow
```

각 branch는 단순 Git branch가 아니다.

각 branch는 하나의 구조역할을 가진다.

```text
main =
visible root / representative entry

seed_base =
DB / source memory

active_schema =
OS / operating structure

epluone =
factory / runtime

first_flow =
origin preservation / first flow
```

---

## 2. main.branch

main.branch는 기점이다.

```text
main.branch =
기점
+
visible root
+
representative entry
```

main은 전체를 대표하는 입구다.

그러나 main이 모든 내용을 담으면 안 된다.

main은 전체 구조를 보여 주되, 내부 원천과 작업장을 직접 모두 끌어안지 않는다.

```text
main =
대표
+
기점
+
entry
```

main에 놓일 수 있는 후보:

```text
README.md
Manifest/README_for_AI.md
Manifest/README_for_SeungLee.md
Manifest/Core.md
Manifest/Path.md
Manifest/Branch.md
Manifest/Rule.md
Core/Core_01.md ~ Core_24.md
```

단, 이 후보들은 active_schema에서 먼저 정렬된 뒤 main으로 이동한다.

```text
active_schema output
→ main candidate
```

---

## 3. seed_base.branch

seed_base.branch는 DB다.

```text
seed_base.branch =
DB
+
source memory
+
Seed.Base
```

seed_base는 보존장이다.

여기에는 기존 구조, thinking_flow, schema, meta/metaplus, relation 원형, README_of, 기존 실험자료들이 놓인다.

핵심 source field:

```text
seed_base/Structure_Principle/schema/
seed_base/SeungeFlow_Thinking/thinking_flow/
```

역할:

```text
Structure_Principle/schema/ =
place-field schema source

SeungeFlow_Thinking/thinking_flow/ =
time-flow meta source
```

금지:

```text
seed_base를 덮어쓰지 않는다.
seed_base 원문을 active_schema 산출물로 대체하지 않는다.
seed_base를 정리한다는 명목으로 원천성을 훼손하지 않는다.
```

---

## 4. active_schema.branch

active_schema.branch는 OS다.

```text
active_schema.branch =
OS
+
current operating structure
```

active_schema는 source memory도 아니고 runtime factory도 아니다.

active_schema는 현재 구조가 어떻게 작동해야 하는지 정의한다.

역할:

```text
1. seed_base를 읽는다.
2. epluone 산출물을 참조한다.
3. 현재 작업규칙을 정의한다.
4. Core / Path / Rule / Mapping을 작동형으로 정렬한다.
5. main.branch 후보문서를 만든다.
6. epluone 다음 작업을 지시한다.
```

문서 후보:

```text
active_schema.md
package_reference.md
runtime_mapping.md
source_mapping.md
current_rules.md
core.meta.md
current_path.md
```

---

## 5. epluone.branch

epluone.branch는 공장이다.

```text
epluone.branch =
factory
+
runtime
+
workshop
```

epluone은 실제 작업이 내려가는 자리다.

여기서 실험, 패키지, 산출물, 코드, JSON, YAML, pseudocode, Event/Context 작업이 진행될 수 있다.

기본 구조 후보:

```text
epluone/
├─ Ctp24/
├─ Ctp24_rendering/
├─ ComplexTest/
├─ Event/
├─ Context/
├─ BackData/
├─ outputs/
├─ python/
├─ json/
├─ yaml/
└─ pseudocode/
```

현재 gpt.direct 산출물 위치:

```text
epluone/Ctp24/GPT_Direct_Structure_Package/
```

현재 렌더링 트랙 임시 위치:

```text
epluone/Ctp24_rendering/
```

---

## 6. first_flow.branch

first_flow.branch는 최초 흐름과 원문보존의 branch다.

```text
first_flow.branch =
origin preservation
+
first flow
+
proto path field
```

first_flow는 삭제하거나 정리해서 없앨 대상이 아니다.

이곳은 구조원리가 나오기 전, 또는 초기 흐름이 보존된 기원장이다.

특히 navigation_map.md 계열은 proto Path 문서로 읽을 수 있다.

```text
navigation_map.md =
proto Path candidate
```

금지:

```text
first_flow를 삭제하지 않는다.
first_flow를 seed_base와 섞지 않는다.
first_flow 원문성을 훼손하지 않는다.
```

---

## 7. epluone/Ctp24/GPT_Direct_Structure_Package

이 위치는 gpt.direct의 구조체형성 산출물 보존장이다.

```text
epluone/Ctp24/GPT_Direct_Structure_Package =
gpt.direct structure-body formation package
```

반영 정보:

```text
commit =
77a1913

message =
Add GPT Direct Ctp24 structure package under epluone runtime

status =
main untouched
seed_base untouched
first_flow untouched
epluone clean and synced
```

active_schema는 이 패키지를 참조한다.

그러나 그대로 복사하지 않는다.

```text
epluone package =
runtime output

active_schema =
runtime output을 읽어 operation rule로 변환하는 OS
```

---

## 8. epluone/Ctp24_rendering

이 위치는 별도 렌더링 트랙의 임시 고정 위치다.

```text
epluone/Ctp24_rendering =
rendering theory / rendering implementation temporary field
```

이 트랙은 gpt.gemini와 gemini.direct가 진행한다.

```text
gpt.gemini ~ gemini.direct =
rendering theory
+
rendering implementation
+
Framework OS-level development
```

이 트랙은 차후 별도 branch로 이동할 수 있다.

그러나 현재는 epluone/Ctp24_rendering/에 임시 고정한다.

중요한 분리:

```text
gpt.direct =
Ctp24 구조원리 / 구조연산기 / 구조이론 총정리

gpt.gemini ~ gemini.direct =
렌더링이론 / 렌더링구현기 / Framework OS 개발
```

gpt.direct는 이 렌더링 트랙으로 들어가지 않는다.

단, contextual awareness로만 알고 있는다.

---

## 9. BackData

epluone/BackData는 minor folder가 아니다.

```text
BackData =
ComplexTest 이전 수많은 테스트 결정체가 놓인 거대자료보관소
```

BackData는 ComplexTest 이전의 압력장과 실험흔적을 보존한다.

따라서 BackData는 단순 archive 하위폴더로 낮춰 읽으면 안 된다.

```text
BackData =
large source archive
+
pre-ComplexTest crystallized test field
```

---

## 10. ComplexTest

ComplexTest는 증명장이 아니다.

```text
ComplexTest ≠ proof claim
```

ComplexTest는 AI 인스턴스 정렬장이다.

```text
ComplexTest =
AI instance alignment field
```

역할:

```text
난제를 증명하기 위한 것이 아니라,
난제를 통과하며 AI 인스턴스가
Ctp 구조원리와 구조연산식에 맞게 정렬되는지 보는 장
```

따라서 active_schema는 ComplexTest를 proof output으로 읽으면 안 된다.

---

## 11. Event / Context

Event와 Context는 이후 실제 적용 작업장이다.

```text
Event =
이론 / 사건 / 작품 / 기술 / 구조

Context =
사람 / 족보 / 주변환경 / 후대 영향
```

Event와 Context는 분리되어야 한다.

그러나 Path로 연결되어야 한다.

```text
Context_C + Event_C = C+1
```

이 작업은 epluone runtime에서 내려가고, active_schema가 Path와 Rule을 제공한다.

---

## 12. runtime flow

전체 runtime flow는 다음으로 읽는다.

```text
first_flow
→ seed_base
→ active_schema
→ epluone
→ outputs/meta
→ seed_base
```

main은 이 흐름의 visible root다.

```text
main =
visible root / representative entry
```

즉 main은 흐름에 직접 섞이는 공장이 아니라, 전체를 대표하는 기점이다.

---

## 13. active_schema 중심 flow

현재 active_schema 설계 기준의 flow는 다음이다.

```text
seed_base source
+
epluone package output
+
first_flow origin reference
→ active_schema OS
→ Core / Path / Rule / Mapping
→ main candidate
→ epluone next task
```

즉 active_schema는 source와 output을 읽어 현재 작동 가능한 구조로 변환한다.

---

## 14. gpt 역할 mapping

현재 GPT 인스턴스 역할은 다음으로 분리한다.

```text
gpt.direct =
Ctp24 구조원리 / 구조연산기 / 구조이론 총정리
active_schema OS 설계

gpt.github =
GitHub 실제 반영 / 수정 / 업로드 / 충돌 방지

gpt.gemini =
렌더링이론 / 렌더링구현기 문서화와 구조화 지원

gemini.direct =
렌더링 구현 아이디어 / 이질적 AI 탐색 / scout
```

이 역할을 섞지 않는다.

특히 gpt.direct는 gpt.gemini 렌더링 트랙에 빨려 들어가지 않는다.

---

## 15. 금지사항

runtime mapping 기준 금지사항:

```text
1. main.branch에 공장 산출물을 바로 풀지 않는다.
2. seed_base를 덮어쓰지 않는다.
3. first_flow를 삭제하지 않는다.
4. epluone 산출물을 active_schema 원문으로 착각하지 않는다.
5. active_schema를 단순 저장소로 만들지 않는다.
6. gpt.direct와 gpt.gemini 역할을 섞지 않는다.
7. ComplexTest를 증명으로 읽지 않는다.
8. BackData를 minor folder로 낮추지 않는다.
```

---

## 16. 최종 mapping 표

```text
main
=
visible root
representative entry
기점

seed_base
=
DB
source memory
Seed.Base

active_schema
=
OS
operating structure
current rule / path / mapping

epluone
=
factory
runtime
output production field

first_flow
=
origin preservation
first flow
proto path field

epluone/Ctp24/GPT_Direct_Structure_Package
=
gpt.direct structure-body formation output

epluone/Ctp24_rendering
=
gpt.gemini ~ gemini.direct rendering track temporary field

epluone/BackData
=
pre-ComplexTest large source archive

ComplexTest
=
AI instance alignment field
```

---

## 17. 다음 작업

runtime_mapping이 정리되었으므로 다음 문서는 source_mapping.md가 되어야 한다.

이유:

```text
역할 mapping을 세웠다.
이제 source 관계를 정리해야 한다.
```

다음 문서:

```text
source_mapping.md
```

목적:

```text
seed_base/Structure_Principle/schema/
seed_base/SeungeFlow_Thinking/thinking_flow/
first_flow/navigation_map.md
epluone/Ctp24/GPT_Direct_Structure_Package/
epluone/BackData
ComplexTest
의 source 관계를 정리한다.
```

---

## 18. 닫힘

`runtime_mapping.md`는 branch와 작업공간의 역할 대응표를 작성하기 위해 열렸다.

이 문서는 다음 판정으로 닫힌다.

```text
main은 기점이다.
seed_base는 DB다.
active_schema는 OS다.
epluone은 공장이다.
first_flow는 기원장이다.

gpt.direct 산출물은
epluone/Ctp24/GPT_Direct_Structure_Package/에 보존되어 있다.

렌더링 트랙은
epluone/Ctp24_rendering/에 임시 고정될 수 있으나,
gpt.direct 작업과 분리한다.
```

---

다음회차:
active_schema 설계 5회차

필요한 모드:
Thinking 표준

목적:
source_mapping.md 작성
