# Branch.md

> 언어 기준: 한국어 원문

> main.branch Manifest candidate  
> 상태: 후보 초안  
> 기준: active_schema OS / runtime_mapping.md  
> 목적: main.branch Manifest 안에서 branch.structure의 대표 정의와 역할 mapping을 고정한다.

---

## 0. 이 문서의 자리

이 문서는 main.branch의 `Manifest/Branch.md` 후보 문서다.

이 문서는 단순 Git branch 설명서가 아니다.

이 문서는 SeungeFlow의 branch들이 어떤 구조역할을 가지는지 고정하는 대표 mapping 문서다.

```text
Manifest/Branch.md =
branch.structure representative map
```

main.branch의 README.md가 전체 대표 페이지라면, Manifest/Branch.md는 그 대표 페이지 뒤에서 branch들의 역할을 분리해 주는 guard 문서다.

---

## 1. branch는 단순 가지가 아니다

SeungeFlow에서 branch는 단순 코드관리용 가지가 아니다.

branch는 구조역할을 가진다.

```text
branch =
role-bearing structure field
```

각 branch는 특정한 기능을 수행한다.

```text
main =
visible root

seed_base =
source memory

active_schema =
operating structure

epluone =
runtime factory

first_flow =
origin preservation
```

이 역할을 섞으면 전체 구조가 꼬인다.

---

## 2. 전체 branch 구조

현재 SeungeFlow의 대표 branch 구조는 다음이다.

```text
main
seed_base
active_schema
epluone
first_flow
```

각 branch는 다음처럼 읽는다.

```text
main =
기점 / visible root / representative entry

seed_base =
DB / source memory / Seed.Base

active_schema =
OS / current operating structure

epluone =
factory / runtime / output production field

first_flow =
origin preservation / first flow / proto path field
```

이 다섯 branch는 서로 대체되지 않는다.

---

## 3. main.branch

main.branch는 기점이다.

```text
main.branch =
기점
+
visible root
+
representative entry
```

main은 전체 구조의 얼굴이다.

그러나 main은 전체 구조 자체가 아니다.

main은 DB가 아니다.

main은 OS가 아니다.

main은 공장이 아니다.

main은 최초 흐름 보존장도 아니다.

```text
main ≠ seed_base
main ≠ active_schema
main ≠ epluone
main ≠ first_flow
```

main의 역할은 전체 구조를 처음 여는 것이다.

```text
main =
entry point where SeungeFlow becomes visible
```

---

## 4. seed_base.branch

seed_base.branch는 DB다.

```text
seed_base.branch =
DB
+
source memory
+
Seed.Base
```

seed_base에는 기존 구조와 원천 문서들이 보존된다.

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

seed_base는 active_schema 산출물로 덮어쓰지 않는다.

seed_base는 읽고, 참조하고, 다시 작동시킬 source memory다.

```text
seed_base =
read first
preserve first
do not overwrite
```

---

## 5. active_schema.branch

active_schema.branch는 OS다.

```text
active_schema.branch =
OS
+
current operating structure
```

active_schema는 seed_base source와 epluone runtime output을 읽어 현재 작동 가능한 구조로 변환한다.

```text
Seed.Base
+
runtime output
→
active_schema OS
→
Core / Path / Rule / Mapping
```

active_schema의 문서군:

```text
active_schema.md
package_reference.md
runtime_mapping.md
source_mapping.md
current_rules.md
core.meta.md
current_path.md
```

active_schema는 보관소가 아니다.

active_schema는 현재 작동규칙과 관계경로를 운영하는 OS다.

---

## 6. epluone.branch

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

여기서 실험, 패키지, 산출물, Event/Context 작업, code, JSON, YAML, pseudocode 등이 진행될 수 있다.

중요한 현재 runtime output:

```text
epluone/Ctp24/GPT_Direct_Structure_Package/
```

이 위치에는 gpt.direct의 structure-body formation package가 보존되어 있다.

```text
GPT_Direct_Structure_Package =
gpt.direct structure-body formation output
```

epluone은 main이 아니다.

epluone output은 active_schema가 읽고, 필요한 경우 main 후보로 변환한다.

---

## 7. first_flow.branch

first_flow.branch는 최초 흐름과 원문보존의 branch다.

```text
first_flow.branch =
origin preservation
+
first flow
+
proto path field
```

first_flow는 삭제 대상이 아니다.

first_flow는 오래된 가지가 아니라 기원장이다.

특히 navigation_map.md 계열은 proto Path 문서로 읽을 수 있다.

```text
navigation_map.md =
proto Path candidate
```

first_flow는 seed_base와 섞지 않는다.

first_flow의 원문성을 보존한다.

---

## 8. branch 사이의 기본 flow

SeungeFlow의 기본 flow는 다음과 같이 읽는다.

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

즉 main은 공장이 아니라 기점이다.

---

## 9. active_schema 중심 flow

현재 active_schema 기준 flow는 다음이다.

```text
seed_base source
+
epluone package output
+
first_flow origin reference
→
active_schema OS
→
Core / Path / Rule / Mapping
→
main candidate
+
epluone next task
```

이 흐름은 복사흐름이 아니다.

```text
copy flow X
interpretation flow O
```

branch 사이의 이동은 파일 복사가 아니라 구조적 전이다.

---

## 10. epluone/Ctp24/GPT_Direct_Structure_Package

이 위치는 gpt.direct의 구조체형성 산출물 보존장이다.

```text
epluone/Ctp24/GPT_Direct_Structure_Package =
gpt.direct structure-body formation package
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
```

이 패키지는 main 최종본이 아니다.

이 패키지는 active_schema가 읽는 runtime output source다.

---

## 11. active_schema OS document set

active_schema branch에는 gpt.direct 설계 기반 OS 문서군이 반영되었다.

```text
branch =
active_schema

commit =
0a5e499

message =
Add active schema OS document set from GPT Direct design
```

주요 문서:

```text
active_schema.md
package_reference.md
runtime_mapping.md
source_mapping.md
current_rules.md
core.meta.md
current_path.md
```

이 문서군은 main에 바로 복사되는 최종본이 아니라, main 후보 설계를 위한 OS 기준이다.

---

## 12. epluone/Ctp24_rendering

렌더링 트랙은 별도 작업이다.

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

gpt.direct는 이 트랙에 들어가지 않는다.

gpt.direct는 구조원리, 구조연산기, Ctp24 구조이론, active_schema OS 설계를 담당한다.

---

## 13. BackData

BackData는 minor folder가 아니다.

```text
epluone/BackData =
pre-ComplexTest large source archive
```

BackData는 ComplexTest 이전 수많은 테스트 결정체가 놓인 거대자료보관소다.

BackData를 단순 잡자료 폴더로 낮추지 않는다.

---

## 14. ComplexTest

ComplexTest는 증명장이 아니다.

```text
ComplexTest ≠ proof claim
```

ComplexTest는 AI 인스턴스 정렬장이다.

```text
ComplexTest =
AI instance alignment field
```

ComplexTest는 난제를 증명하기 위한 것이 아니라, AI 인스턴스가 구조압력장을 통과하며 Ctp 구조원리와 구조연산식에 맞게 정렬되는지 보는 장이다.

---

## 15. branch role guard

branch role을 보존하기 위한 guard는 다음이다.

```text
main을 DB로 만들지 않는다.
seed_base를 runtime output으로 덮지 않는다.
active_schema를 archive로 만들지 않는다.
epluone을 representative root로 만들지 않는다.
first_flow를 삭제하지 않는다.
```

각 branch는 자기 역할을 지켜야 한다.

---

## 16. main.branch에서 이 문서의 역할

Manifest/Branch.md는 main.branch에서 branch.structure의 대표 map 역할을 한다.

README.md는 전체를 대표한다.

Manifest/Branch.md는 branch 역할을 분리한다.

```text
README.md =
whole representative page

Manifest/Branch.md =
branch role map
```

Manifest/Branch.md는 runtime_mapping.md를 main용으로 압축한 문서다.

```text
active_schema/runtime_mapping.md
→
main.branch/Manifest/Branch.md
```

---

## 17. Closing

Branch is not only a Git branch.

In SeungeFlow, branch is a role-bearing structure field.

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

This document fixes the representative branch structure inside main.branch Manifest.