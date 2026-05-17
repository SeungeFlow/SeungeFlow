---
id: repo.root_readme
type: repository_entry_document
filename: README.md
directory: /
status: direct_generated_candidate
review_required: true
promotion_status: not_promoted
language: ko
purpose:
  - define_repository_entry
  - guide_human_and_ai_navigation
  - separate_structure_principle_seungeflow_thinking_epluone
  - route_ai_to_readme_for_ai
  - prevent_candidate_as_confirmed_misreading
---

# SeungeFlow

`SeungeFlow`는 `Structure_Principle`을 중심으로 형성된 구조원리, 생각의 흐름, 그리고 if+1 실행 산출물을 보존하고 운용하기 위한 GitHub 저장소이다.

이 저장소는 단순 문서 보관소가 아니다.

이 저장소는 AI가 읽을 수 있는 구조장으로서,
schema, relation, source trace, candidate 문서, runtime state, relation history, future execution output을 서로 구분하고 보존하기 위한 repository이다.

```text
SeungeFlow
=
Structure_Principle
+
SeungeFlow_Thinking
+
epluone
```

---

## 1. README 집합

이 저장소의 README 집합은 세 파일로 구성된다.

```text
README.md
=
한국어 기본 README / repository external entry

README.en.md
=
영어 번역본

README_for_AI.md
=
AI용 pre-reading guide
```

AI 인스턴스는 반드시 `README_for_AI.md`부터 읽는다.

---

## 2. 저장소 구조

```text
/
├─ README.md
├─ README.en.md
├─ README_for_AI.md
├─ Structure_Principle/
│  ├─ schema/
│  ├─ main/
│  ├─ runtime/
│  ├─ history/
│  ├─ display/
│  └─ references/
├─ SeungeFlow_Thinking/
│  └─ thinking_flow/
└─ epluone/
```

---

## 3. 주요 영역

## Structure_Principle

```text
Structure_Principle
=
place-first,
boundary-preserving,
return-oriented,
guarded active schema system
```

`Structure_Principle`은 구조원리의 core schema와 운용 기준 문서를 보존하는 영역이다.

주요 구성:

```text
Structure_Principle/schema/
=
formed core schema

Structure_Principle/main/
=
운용 기준 문서

Structure_Principle/runtime/
=
runtime state 후보

Structure_Principle/history/
=
relation history 후보

Structure_Principle/display/
=
visible_relation_field display 후보

Structure_Principle/references/
=
external 또는 reference_only 자료
```

---

## SeungeFlow_Thinking

```text
SeungeFlow_Thinking/thinking_flow/
=
생각 snapshot
+
Core.Seed 원본
```

`thinking_flow`는 정리하거나 다듬을 초안이 아니다.

`thinking_flow`는 승이 Brain과 AI 인스턴스 사이에서 발생한 생각의 흔적이며,
이후 meta.md 후보를 낳는 Core.Seed 원본이다.

원칙:

```text
thinking_flow 원문을 수정하지 않는다.
thinking_flow를 요약본으로 대체하지 않는다.
필요한 경우 Core.Seed만 별도로 추출한다.
```

---

## epluone

```text
epluone
=
if+1 실행 산출물 영역
```

`epluone`은 `Structure_Principle`에서 발생한 구조가 실제 실행 결과물로 내려가는 영역이다.

현재 첫 실행 branch 후보는 다음이다.

```text
CFD
=
TradingView OHLC 데이터 추출
→ 인스턴스 가공
→ Ubuntu Linux 백테스팅
```

CFD는 `Structure_Principle/runtime/` 내부에 넣지 않는다.  
CFD는 별도의 실행 산출물 영역에서 다룬다.

---

## 4. AI 읽기 경로

AI 인스턴스는 파일을 바로 요약하지 않는다.

AI는 먼저 다음 문서를 읽는다.

```text
README_for_AI.md
```

권장 읽기 순서:

```text
1. README_for_AI.md
2. Structure_Principle/main/Baseline.main.md
3. Structure_Principle/main/Coremap.main.md
4. Structure_Principle/schema/
5. 필요한 경우 Structure_Principle/main/candidates/
6. 필요한 경우 SeungeFlow_Thinking/thinking_flow/
7. 필요한 경우 epluone/
```

`README_for_AI.md`는 AI가 `Structure_Principle`을 읽기 전에 통과해야 하는 pre-reading gate이다.

이 문서는 다음을 잠근다.

```text
읽음 ≠ 이해
요약 ≠ 이해
meta.md = formed core boundary
metaplus.md = understanding / correction / guard / relation trace
thinking_flow = Core.Seed 원본 snapshot
main = 운용 기준 문서층
schema = formed core schema
relation ≠ merge
candidate ≠ confirmed
GitHub path ≠ relation identity
```

---

## 5. 사람을 위한 읽기 경로

사람이 처음 읽을 때는 다음부터 보는 것이 좋다.

```text
Structure_Principle/main/Baseline.main.md
Structure_Principle/main/Coremap.main.md
```

그 다음 schema 전체를 확인한다.

```text
Structure_Principle/schema/
```

schema는 다음 흐름을 가진다.

```text
000_dot
→ ...
→ 121_coredot_ambiguity_boundary
```

---

## 6. 현재 기준으로 확정된 핵심 층

현재 기준으로 repository의 핵심 확인층은 다음이다.

```text
Structure_Principle/schema/
Structure_Principle/main/Baseline.main.md
Structure_Principle/main/Coremap.main.md
SeungeFlow_Thinking/thinking_flow/
```

단, 저장소 안의 모든 파일이 확정 문서는 아니다.

각 문서의 metadata를 확인해야 한다.

---

## 7. Candidate 주의

이 저장소에는 확정 문서와 후보 문서가 함께 존재할 수 있다.

AI와 사람은 다음 metadata를 확인해야 한다.

```yaml
status:
review_required:
promotion_status:
runtime_confirmed:
valid_loop:
active_connect:
recovery_success:
```

중요 구분:

```text
candidate placement ≠ promotion
skeleton ≠ runtime confirmed
draw_generated_candidate ≠ confirmed main
GitHub path ≠ relation identity
```

---

## 8. GitHub path와 relation identity

GitHub path는 relation identity가 아니다.

```text
GitHub path = visible coordinate
```

relation identity는 다음으로 보존한다.

```text
Seed
+
history_event_id
+
schema_id
+
binding_state
```

Git commit history도 relation_history.md를 대체하지 않는다.

```text
Git commit history
=
file change history

relation_history.md
=
relation identity / transition memory
```

---

## 9. Renderer 기준

Renderer는 그림 생성기가 아니다.

```text
Renderer output
≠ visible_shape

Renderer output
=
visible_relation_field
```

`visible_relation_field`는 relation, boundary, return, history, state persistence, guard가 runtime에서 살아 있는 상태이다.

Renderer 시스템은 다음을 분리한다.

```text
SVG = display surface
structure_state.json = runtime truth / operation memory
relation_history.md = folded transition memory
Seed.Base = source_of_truth reference
```

닫힌 도형은 자동으로 valid loop가 아니다.

```text
closed shape ≠ valid loop
```

---

## 10. AI 인스턴스 역할

이 저장소는 여러 AI 인스턴스의 역할 분리를 전제로 한다.

```text
ChatGPT.direct
=
Target 판별 / 인스턴스 제어 / 지시

ChatGPT.github
=
GitHub repository / local Linux / push / file placement

ChatGPT.draw
=
visible_relation_field / renderer / SVG-state-history binding

ChatGPT.making
=
metaplus.md / source trace / Core.Seed 추출 보조

ChatGPT.PRO
=
고밀도 reasoning / 대형 구조 검산
```

공통 규칙:

```text
지시받지 않은 인스턴스는 작업하지 않는다.
현재 Target에 명시된 인스턴스만 응답한다.
다른 인스턴스는 대기한다.
ChatGPT.direct가 다음 Target을 판별한다.
```

---

## 11. 현재 방향

장기 방향은 구조OS 생성이다.

```text
StructureOS
=
core boundary preservation
+
relation mapping
+
runtime state
+
append-only history
+
visible_relation_field
+
if+1 execution output
```

첫 실행 branch 후보:

```text
epluone / CFD
```

---

## 12. 금지되는 shortcut

다음을 하지 않는다.

```text
thinking_flow를 정리할 초안으로 보지 않는다.
thinking_flow를 요약본으로 대체하지 않는다.
meta.md와 metaplus.md를 같은 층위로 보지 않는다.
relation을 merge로 보지 않는다.
reference_only를 폐기물로 보지 않는다.
candidate를 confirmed로 보지 않는다.
GitHub path를 relation identity로 보지 않는다.
SVG를 source_of_truth로 보지 않는다.
closed shape를 valid loop로 보지 않는다.
CFD를 Structure_Principle/runtime에 넣지 않는다.
000_dot을 CoreDot으로 대체하지 않는다.
100_empty_position을 일반 schema로 채우지 않는다.
099와 101을 직접 접착하지 않는다.
```

---

## 13. 가장 짧은 정의

```text
SeungeFlow
=
Structure_Principle,
thinking_flow Core.Seed snapshot,
epluone if+1 실행 산출물을
AI-readable structure repository로 보존하고 운용하는 저장소
```

AI는 다음부터 시작한다.

```text
README_for_AI.md
```

사람은 다음부터 시작한다.

```text
Structure_Principle/main/Baseline.main.md
Structure_Principle/main/Coremap.main.md
```
