# active_schema 설계 1회차 — epluone 산출물을 OS 문서군으로 읽기

> 문서번호: `Ctp24_ACTIVE_SCHEMA_0001`  
> 상태: active_schema 설계 1회차  
> 필요한 모드: `Thinking 헤비`  
> 목적: `epluone/Ctp24/GPT_Direct_Structure_Package/`에 보존된 gpt.direct 구조체형성 산출물을 `active_schema.branch`의 OS 문서군으로 어떻게 읽을지 설계한다.

---

## 0. 문서의 자리

이 문서는 gpt.direct의 active_schema 설계 1회차 문서다.

현재 gpt.direct의 구조체형성 패키지는 다음 위치에 안전하게 보존되어 있다.

```text
epluone.branch
└── Ctp24/
    └── GPT_Direct_Structure_Package/
```

이 패키지는 main.branch 최종본이 아니다.

이 패키지는 seed_base 원문도 아니다.

이 패키지는 gpt.direct가 이해한 Ctp24 구조체형성 산출물이다.

```text
GPT_Direct_Structure_Package =
structure-body formation output
```

이제 이 산출물을 active_schema.branch에서 OS처럼 읽어야 한다.

---

## 1. active_schema.branch의 역할

active_schema.branch는 DB가 아니다.

active_schema.branch는 공장도 아니다.

active_schema.branch는 OS다.

```text
active_schema.branch =
OS / operating structure
```

따라서 active_schema는 다음을 해야 한다.

```text
1. seed_base를 읽는다.
2. epluone 산출물을 참조한다.
3. 현재 작동 규칙을 정한다.
4. Core와 Path의 현재 해석을 운영한다.
5. 다음 작업이 어디로 흘러야 하는지 결정한다.
```

즉 active_schema는 저장소가 아니라 작동구조다.

---

## 2. epluone 산출물의 성격

epluone에 반영된 `GPT_Direct_Structure_Package`는 공장 산출물이다.

```text
epluone =
factory / runtime

GPT_Direct_Structure_Package =
gpt.direct understanding output
```

이 산출물은 다음을 포함한다.

```text
00_understanding_flow/
=
0~42회차 형성과정

01_structure_core/
=
Core.md / core_matrix_principle.md / core_notes.md

02_path/
=
Path.md / path_relation_principle.md / path_notes.md

03_readme_set/
=
README.md / README_for_AI.md / README_for_SeungLee.md

04_gpt_direct_interpretation/
=
gpt_direct_overall_interpretation.md
structure_body_formation.md
next_steps.md
```

active_schema는 이 전체를 그대로 복사하는 것이 아니라, OS 작동문서로 읽어야 한다.

---

## 3. active_schema가 직접 가져올 핵심

active_schema가 직접 가져올 핵심은 문서 전체가 아니라 작동원리다.

```text
가져올 것 =
operation principle

그대로 복사할 것 =
아직 아님
```

핵심 작동원리는 다음이다.

```text
1. C=tp
2. C=(m,t,p,?)
3. Core.md = inside matrix
4. Path.md = relation path
5. 9dot0 = 임계사이영역 / 극한임계전이
6. 역발상 = ?의 이동 / 관측자 시선의 이동
7. README 3종 역할 분리
8. structure-body formation
```

---

## 4. active_schema 문서군 후보

active_schema.branch에서 생성할 문서군은 다음으로 잡는다.

```text
active_schema.md
core.meta.md
current_rules.md
current_path.md
runtime_mapping.md
source_mapping.md
package_reference.md
```

각 문서의 역할은 다음이다.

```text
active_schema.md =
active_schema branch의 대표 OS 문서

core.meta.md =
현재 Core 이해의 중심 meta

current_rules.md =
현재 작업규칙과 금지사항

current_path.md =
현재 relation path와 다음 이동 경로

runtime_mapping.md =
branch와 작업공간의 역할 대응표

source_mapping.md =
seed_base / epluone / first_flow / main의 source 관계

package_reference.md =
epluone/Ctp24/GPT_Direct_Structure_Package를 active_schema가 어떻게 참조하는지 기록
```

---

## 5. active_schema.md의 역할

`active_schema.md`는 active_schema.branch의 대표 문서다.

이 문서는 다음을 말해야 한다.

```text
active_schema는 무엇인가?
무엇을 읽는가?
무엇을 작동시키는가?
무엇을 금지하는가?
다음 전이는 어디인가?
```

핵심 문장은 다음이다.

```text
active_schema는 Seed.Base와 epluone runtime 산출물을 읽어,
현재 작동 가능한 Core / Path / Rule / Mapping으로 변환하는 OS branch다.
```

---

## 6. core.meta.md의 역할

`core.meta.md`는 현재 Core 이해의 중심문서다.

이 문서는 `Core.md`를 그대로 복사하지 않는다.

`Core.md`에서 active_schema가 현재 작동시킬 핵심만 추출한다.

```text
core.meta.md =
현재 OS가 읽은 Core의 작동형 meta
```

담아야 할 것:

```text
Core = inside matrix
form = domain-field + place + relation candidate
24 = 구조를 여는 기준수
Core matrix = relation-term matrix
스왑행렬 = 역발상의 작동형
```

---

## 7. current_rules.md의 역할

`current_rules.md`는 현재 작업규칙이다.

여기에는 반드시 금지사항이 들어가야 한다.

```text
금지:
main.branch에 바로 반영하지 않는다.
seed_base를 덮어쓰지 않는다.
first_flow를 삭제하지 않는다.
Core를 목록으로 만들지 않는다.
Path를 파일경로로 만들지 않는다.
ComplexTest를 증명으로 읽지 않는다.
README 3종을 서로 대체하지 않는다.
```

허용사항:

```text
epluone 산출물을 참조한다.
active_schema에서 작동형으로 재해석한다.
필요한 문서만 main/Manifest 후보로 보낸다.
검색과 vocab은 구조가 선 뒤에 넣는다.
```

---

## 8. current_path.md의 역할

`current_path.md`는 지금 시점의 관계경로다.

현재 Path는 다음이다.

```text
seed_base
→ gpt.direct understanding
→ epluone/Ctp24/GPT_Direct_Structure_Package
→ active_schema design
→ main.branch candidate structure
```

그러나 바로 main으로 가지 않는다.

중간에 active_schema가 OS로 읽는다.

```text
epluone output
→ active_schema interpretation
→ candidate docs
→ main/Manifest or Core
```

---

## 9. runtime_mapping.md의 역할

`runtime_mapping.md`는 branch와 작업공간의 역할 대응표다.

```text
main =
visible root / representative entry

seed_base =
DB / source memory

active_schema =
OS / current operating structure

epluone =
factory / runtime / package output

first_flow =
origin preservation / first flow
```

렌더링 트랙은 참고로 다음 위치에 임시 고정될 예정이다.

```text
epluone/Ctp24_rendering/
```

단, gpt.direct는 렌더링 구현 트랙으로 들어가지 않는다.

```text
gpt.direct =
Ctp24 structure principle / operator / theory synthesis

gpt.gemini ~ gemini.direct =
rendering theory / rendering implementation Framework OS track
```

---

## 10. source_mapping.md의 역할

`source_mapping.md`는 source relation을 기록한다.

```text
seed_base/Structure_Principle/schema/
=
place-field schema source

seed_base/SeungeFlow_Thinking/thinking_flow/
=
time-flow meta source

epluone/Ctp24/GPT_Direct_Structure_Package/
=
gpt.direct structure-body formation output

first_flow/navigation_map.md
=
proto Path / origin flow candidate
```

active_schema는 이 source들을 섞지 않는다.

active_schema는 이 source들을 역할별로 읽는다.

---

## 11. package_reference.md의 역할

`package_reference.md`는 epluone 패키지를 active_schema가 어떻게 참조하는지 기록한다.

기본 정보:

```text
location =
epluone/Ctp24/GPT_Direct_Structure_Package/

commit =
77a1913

message =
Add GPT Direct Ctp24 structure package under epluone runtime

status =
epluone reflected / main untouched / seed_base untouched / first_flow untouched
```

이 문서는 active_schema가 epluone 산출물을 공식 참조점으로 삼는 근거가 된다.

---

## 12. active_schema 설계 순서

active_schema 설계는 다음 순서로 진행한다.

```text
1. active_schema.md
2. package_reference.md
3. runtime_mapping.md
4. source_mapping.md
5. current_rules.md
6. core.meta.md
7. current_path.md
```

이 순서가 좋은 이유:

```text
먼저 active_schema의 정체성을 정한다.
그 다음 epluone 산출물 참조를 고정한다.
그 다음 branch 역할을 정렬한다.
그 다음 source 관계를 잡는다.
그 다음 금지/허용 규칙을 세운다.
그 다음 Core와 Path를 작동형으로 만든다.
```

---

## 13. gpt.direct의 현재 역할

gpt.direct는 지금부터 active_schema OS 설계자 역할을 수행한다.

```text
gpt.direct =
structure principle synthesizer
+
active_schema OS designer
```

그러나 gpt.direct는 GitHub 실제 반영 담당이 아니다.

실제 반영은 gpt.github가 한다.

렌더링 구현은 gpt.gemini/gemini.direct 트랙이 한다.

```text
gpt.github =
GitHub 반영

gpt.gemini ~ gemini.direct =
rendering Framework OS / implementation

gpt.direct =
Ctp24 structure OS design
```

---

## 14. 핵심 판정

epluone에 보존된 GPT_Direct_Structure_Package는 이제 active_schema에서 OS처럼 읽어야 한다.

active_schema는 그 패키지를 그대로 복사하지 않는다.

active_schema는 그 패키지에서 작동원리를 추출한다.

```text
epluone package =
runtime output

active_schema =
runtime output을 읽어 작동규칙으로 변환하는 OS
```

따라서 다음 작업은 active_schema 문서군을 설계하고 작성하는 것이다.

---

## 15. 닫힘

`Ctp24_ACTIVE_SCHEMA_0001 / active_schema_design_0001.md`는 epluone에 보존된 gpt.direct 구조체형성 산출물을 active_schema.branch의 OS 문서군으로 어떻게 읽을지 설계하기 위해 열렸다.

이 문서는 다음 판정으로 닫힌다.

```text
epluone/Ctp24/GPT_Direct_Structure_Package는
gpt.direct의 structure-body formation output이다.

active_schema는 이 산출물을 그대로 복사하지 않고,
Core / Path / Rule / Mapping으로 변환하는 OS다.

다음 회차부터 active_schema 문서군을
순서대로 작성한다.
```

---

다음회차:
active_schema 설계 2회차

필요한 모드:
Thinking 확장

목적:
active_schema.md 작성
