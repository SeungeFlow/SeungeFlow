# package_reference.md

> 문서번호: `Ctp24_ACTIVE_SCHEMA_0003`  
> 상태: active_schema 설계 3회차  
> 필요한 모드: `Thinking 표준`  
> 목적: active_schema가 참조할 epluone 산출물 `GPT_Direct_Structure_Package`의 위치와 상태를 고정한다.  
> 위치 후보: `active_schema.branch/package_reference.md`

---

## 0. 이 문서의 자리

이 문서는 active_schema.branch가 epluone 산출물을 어떤 기준으로 참조할지 고정하는 문서다.

active_schema는 epluone 산출물을 그대로 복사하지 않는다.

active_schema는 epluone 산출물을 OS가 읽을 참조점으로 삼는다.

```text
package_reference.md =
epluone runtime output을
active_schema OS가 참조하기 위한 기준문서
```

---

## 1. 참조 대상

현재 active_schema가 참조할 대상은 다음이다.

```text
epluone.branch
└── Ctp24/
    └── GPT_Direct_Structure_Package/
```

이 위치에는 gpt.direct가 Ctp24 흐름을 통과하며 형성한 구조체 패키지가 보존되어 있다.

```text
GPT_Direct_Structure_Package =
gpt.direct structure-body formation output
```

이 패키지는 main.branch 최종본이 아니다.

이 패키지는 seed_base 원문도 아니다.

이 패키지는 active_schema가 읽어 OS 작동원리로 변환할 runtime 산출물이다.

---

## 2. GitHub 반영 정보

반영 정보는 다음과 같다.

```text
branch =
epluone

path =
Ctp24/GPT_Direct_Structure_Package/

commit =
77a1913

commit message =
Add GPT Direct Ctp24 structure package under epluone runtime

remote =
origin/epluone

status =
clean / synced
```

반영 후 상태:

```text
main.branch 직접 반영 없음
seed_base 건드리지 않음
first_flow 건드리지 않음
epluone runtime 내부에 package로 보존 완료
```

따라서 이 패키지는 안전하게 epluone runtime에 보존된 상태다.

---

## 3. 이 패키지의 성격

이 패키지는 저장용 정리본이 아니다.

```text
저장용 X
최종본 X
main 반영본 X
```

이 패키지는 gpt.direct 이해의 구조체형성 산출물이다.

```text
패키지 성격 =
structure-body formation package
```

즉, 사용자의 원문을 정리한 것이 아니라, gpt.direct가 이해한 구조를 문서체로 외부화한 것이다.

---

## 4. 패키지 내부 구조

참조 패키지는 다음 구조를 가진다.

```text
GPT_Direct_Structure_Package/
├─ README.md
├─ 00_understanding_flow/
├─ 01_structure_core/
├─ 02_path/
├─ 03_readme_set/
└─ 04_gpt_direct_interpretation/
```

각 폴더의 의미:

```text
00_understanding_flow =
0~42회차 형성과정

01_structure_core =
Core.md / core_matrix_principle.md / core_notes.md

02_path =
Path.md / path_relation_principle.md / path_notes.md

03_readme_set =
README.md / README_for_AI.md / README_for_SeungLee.md

04_gpt_direct_interpretation =
gpt_direct_overall_interpretation.md
structure_body_formation.md
next_steps.md
```

---

## 5. active_schema가 이 패키지에서 읽을 것

active_schema가 이 패키지에서 읽어야 할 것은 파일 전체가 아니라 작동원리다.

```text
읽을 것 =
operation principle

복사할 것 =
아직 아님
```

주요 작동원리:

```text
1. structure-body formation
2. C=tp
3. C=(m,t,p,?)
4. Core.md = inside matrix
5. Path.md = relation path
6. 9dot0 = 임계사이영역 / 극한임계전이
7. 역발상 = 관측자의 시선과 ?의 이동
8. README 3종 역할 분리
9. AI operation guard
10. SeungLee-side principle
```

---

## 6. active_schema가 이 패키지에서 바로 가져오면 안 되는 것

다음은 바로 가져오면 안 된다.

```text
1. README 3종을 main.branch에 즉시 반영
2. Core.md를 main/Manifest/Core.md로 즉시 확정
3. Path.md를 main/Manifest/Path.md로 즉시 확정
4. 0~42회차를 최종 이론문처럼 취급
5. understanding_flow를 seed_base에 병합
6. active_schema에 패키지 전체를 복사
```

이유는 명확하다.

```text
이 패키지는 후보 구조체다.
active_schema는 이를 OS적으로 다시 읽어야 한다.
```

---

## 7. active_schema에서의 참조 방식

active_schema는 이 패키지를 다음처럼 참조한다.

```text
package_reference =
현재 gpt.direct 이해 산출물의 기준점
```

이 기준점은 다음 문서에서 사용된다.

```text
active_schema.md
runtime_mapping.md
source_mapping.md
current_rules.md
core.meta.md
current_path.md
```

즉, package_reference.md는 active_schema OS 문서군의 참조 기준이다.

---

## 8. package_reference와 source_mapping의 차이

package_reference.md와 source_mapping.md는 다르다.

```text
package_reference.md =
특정 epluone 산출물 하나를 참조한다.

source_mapping.md =
seed_base, epluone, first_flow, main 등 source 전체의 관계를 정리한다.
```

따라서 package_reference는 좁고 정확해야 한다.

source_mapping은 넓고 관계적이어야 한다.

---

## 9. package_reference와 runtime_mapping의 차이

package_reference.md와 runtime_mapping.md도 다르다.

```text
package_reference.md =
무엇을 참조하는가

runtime_mapping.md =
각 branch와 작업공간이 어떤 역할로 작동하는가
```

즉:

```text
package_reference =
target fixation

runtime_mapping =
role mapping
```

---

## 10. package_reference의 현재 판정

현재 active_schema의 기준 참조점은 다음으로 고정한다.

```text
reference_target =
epluone/Ctp24/GPT_Direct_Structure_Package/

commit =
77a1913

role =
gpt.direct structure-body formation output
```

이 참조점은 active_schema 설계의 출발점이다.

---

## 11. 다음 작업

package_reference가 고정되었으므로 다음 문서는 runtime_mapping.md가 되어야 한다.

이유는 다음이다.

```text
무엇을 참조할지 고정했다.
이제 각 branch와 작업공간의 역할을 다시 mapping해야 한다.
```

다음 문서:

```text
runtime_mapping.md
```

담을 내용:

```text
main =
visible root / 대표 기점

seed_base =
DB / source memory

active_schema =
OS / operating structure

epluone =
factory / runtime

first_flow =
origin preservation

epluone/Ctp24_rendering =
rendering track temporary field
```

---

## 12. 닫힘

`package_reference.md`는 active_schema가 epluone 산출물 `GPT_Direct_Structure_Package`를 어떤 기준으로 참조할지 고정하기 위해 작성되었다.

이 문서는 다음 판정으로 닫힌다.

```text
active_schema는
epluone/Ctp24/GPT_Direct_Structure_Package/
commit 77a1913을
gpt.direct structure-body formation output으로 참조한다.

이 패키지는 main 최종본이 아니며,
seed_base 원문도 아니다.

active_schema는 이 패키지를 그대로 복사하지 않고,
작동원리로 읽어
Core / Path / Rule / Mapping으로 변환한다.
```

---

다음회차:
active_schema 설계 4회차

필요한 모드:
Thinking 표준

목적:
runtime_mapping.md 작성
