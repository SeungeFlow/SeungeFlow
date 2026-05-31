# Ctp24 Active Schema Design Package

> 목적: `active_schema.branch`에 반영할 OS 문서군 후보를 패키지화한다.  
> 상태: gpt.direct active_schema 설계 산출물  
> 성격: 최종 GitHub 반영본이 아니라 gpt.github가 검토할 handoff package

---

## 0. 이 패키지의 자리

이 패키지는 `epluone/Ctp24/GPT_Direct_Structure_Package/`를 active_schema에서 OS처럼 읽기 위해 만든 문서군이다.

```text
epluone package =
gpt.direct structure-body formation runtime output

active_schema =
runtime output을 읽어 Core / Path / Rule / Mapping으로 변환하는 OS
```

---

## 1. 포함 문서

```text
00_design_notes/
└─ active_schema_design_0001.md

01_active_schema/
├─ active_schema.md
├─ package_reference.md
├─ runtime_mapping.md
├─ source_mapping.md
├─ current_rules.md
├─ core.meta.md
└─ current_path.md
```

---

## 2. 각 문서 역할

```text
active_schema_design_0001.md =
active_schema 설계 전체 계획

active_schema.md =
active_schema.branch 대표 OS 문서

package_reference.md =
epluone/Ctp24/GPT_Direct_Structure_Package 참조 고정

runtime_mapping.md =
branch와 작업공간 역할 대응표

source_mapping.md =
seed_base / first_flow / epluone / BackData / ComplexTest source 관계표

current_rules.md =
현재 작업규칙과 금지사항

core.meta.md =
현재 Core 이해의 작동형 meta

current_path.md =
현재 active_schema가 따라갈 relation path
```

---

## 3. 반영 원칙

```text
1. main.branch에 바로 반영하지 않는다.
2. seed_base를 덮어쓰지 않는다.
3. first_flow를 건드리지 않는다.
4. epluone package를 active_schema에 통째로 복사하지 않는다.
5. 이 문서군은 active_schema.branch 후보로 검토한다.
6. gpt.github가 실제 repo 상태를 보고 반영한다.
```

---

## 4. 추천 반영 위치

```text
active_schema branch root
├─ active_schema.md
├─ package_reference.md
├─ runtime_mapping.md
├─ source_mapping.md
├─ current_rules.md
├─ core.meta.md
└─ current_path.md
```

설계 노트는 다음 중 하나로 둘 수 있다.

```text
active_schema branch root:
active_schema_design_0001.md

또는:
docs/active_schema_design_0001.md
```

---

## 5. 닫힘

이 패키지는 active_schema 문서군을 GitHub에 반영하기 전, gpt.github가 검토할 handoff package다.
