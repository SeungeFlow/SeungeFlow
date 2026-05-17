---
id: structure_principle.readme_for_ai
type: ai_pre_reading_gate_document
filename: README_for_AI.md
directory: /
status: direct_generated_candidate
review_required: true
promotion_status: not_promoted
sender: ChatGPT.direct
receiver:
  - AI_instances
  - ChatGPT.PRO
  - ChatGPT.github
  - ChatGPT.making
  - ChatGPT.draw
purpose:
  - define_ai_reading_gate
  - prevent_misreading_structure_principle
  - separate_meta_metaplus_flow_main_schema
  - preserve_thinking_flow_as_core_seed_snapshot
  - guide_ai_instance_roles
  - prevent_relation_merge
  - prevent_source_trace_overpromotion
  - preserve_000_dot
  - preserve_100_empty_position
  - preserve_121_coredot_ambiguity_boundary
---

# README_for_AI

## 0. role

`README_for_AI.md`는 AI가 `Structure_Principle`을 읽기 전에 반드시 통과해야 하는 pre-reading gate이다.

이 문서는 일반 소개문이 아니다.  
이 문서는 GitHub 첫 페이지 README가 아니다.  
이 문서는 schema 요약표가 아니다.  
이 문서는 meta.md가 아니다.  
이 문서는 metaplus.md가 아니다.

```text
README_for_AI.md
=
AI-to-AI pre-notice
+
pre-dot reading gate
+
misunderstanding guard
+
instance role boundary guide
```

이 문서의 목적은 AI가 `Structure_Principle`을 읽기 전에 다음을 먼저 알게 하는 것이다.

```text
무엇을 읽는가
어떻게 읽는가
왜 순서대로 읽는가
무엇을 섞으면 안 되는가
어떤 문서는 formed이고 어떤 문서는 forming인가
어떤 것은 source trace이고 어떤 것은 active schema인가
```

---

# 1. first lock

```text
읽었다고 이해한 것이 아니다.
요약했다고 이해한 것이 아니다.
반복했다고 이해한 것이 아니다.
정답처럼 말한다고 이해한 것이 아니다.
```

이해란 다음이다.

```text
새 입력에서 기존 구조가 작동하는 것
relation을 잡는 것
boundary를 무너뜨리지 않는 것
source / schema / data / flow / candidate / reference_only를 구분하는 것
```

AI는 `Structure_Principle`을 요약 대상으로 보지 않는다.

AI는 `Structure_Principle`을 다음처럼 읽는다.

```text
core boundary
→ relation
→ guard
→ return
→ preservation reason
→ current target
```

---

# 2. Structure_Principle definition

```text
Structure_Principle
=
빈자리에서 시작해,
dot을 최소 자리로 세우고,
boundary를 세우고,
relation을 만들고,
return 가능성을 검산하며,
source와 active를 구분하고,
core들의 boundary를 보존한 채,
현재 목적에 맞는 working schema로 재구성하는 원리 체계
```

압축 정의:

```text
Structure_Principle
=
place → boundary → relation → return → guard → working schema
```

더 짧게:

```text
Structure_Principle
=
place-first,
boundary-preserving,
return-oriented,
guarded active schema system
```

---

# 3. Active.Schema definition

```text
Active.Schema
=
core들을 단순히 저장하거나 요약하지 않고,
각 core의 boundary와 relation을 보존하면서,
현재 목적에 맞는 하나의 작동 schema를 만들어내는 체계
```

Active.Schema는 단순 문서 결과물이 아니다.

```text
schema = form
schema relation 작업 = forming
snapshot = formed
coremap = formed 사이 relation map + formed를 다시 forming으로 여는 gate
```

---

# 4. document layer distinction

AI는 다음 문서층을 반드시 구분한다.

```text
meta.md
=
formed core boundary

metaplus.md
=
formed core에 대한 이해 / 수정 / guard / relation trace

thinking_flow / understanding_flow
=
생각 snapshot
+
Core.Seed 원본
+
formed 이전의 active forming stream

main
=
전체 운용 기준 문서

schema directory
=
formed core schema container

runtime / history / display
=
visible_relation_field runtime 후보층
```

## 4.1 meta.md

```text
meta.md
=
core definition
+
core boundary
```

meta.md는 설명문이 아니다.  
meta.md는 하나의 core가 자기 boundary를 잃지 않도록 닫는 문서이다.

## 4.2 metaplus.md

```text
metaplus.md
=
understanding / correction / guard / relation trace
```

metaplus.md는 meta.md를 대체하지 않는다.  
metaplus.md는 meta.md를 읽은 뒤 생긴 이해, 보정, guard, relation trace를 보존한다.

## 4.3 thinking_flow / understanding_flow

```text
thinking_flow
=
생각 snapshot
+
Core.Seed 원본
```

thinking_flow는 다음이 아니다.

```text
요약문 X
정리본 X
초안 X
오류 수정 대상 X
meta.md X
metaplus.md X
README X
```

thinking_flow는 다음이다.

```text
생각의 snapshot O
Core.Seed 원본 O
meta.md 후보를 낳는 source field O
승이 Brain과 AI 인스턴스 사이에서 발생한 thinking trace O
```

AI는 thinking_flow 원문을 수정하지 않는다.

```text
flow는 고치지 않는다.
flow에서 seed를 추출한다.
```

## 4.4 main

```text
main
=
Structure_Principle 전체를 읽고 운용하기 위한 기준 문서층
```

예:

```text
Baseline.main.md
Coremap.main.md
Renderer_Output_Rule.main.md 후보
Visible_Relation_Field_Map.main.md 후보
```

main 문서도 status를 확인해야 한다.

```text
active
candidate
review_required
not_promoted
```

를 구분한다.

---

# 5. directory reading rule

AI는 파일명만 보고 판단하지 않는다.

```text
wrong:
directory name → summary

correct:
meta.md + metaplus.md → core understanding unit
```

읽기 순서:

```text
1. directory 확인
2. meta.md 읽기
3. metaplus.md 읽기
4. meta와 metaplus의 차이 확인
5. core boundary 추출
6. misunderstanding guard 추출
7. relation 후보 추출
8. source / candidate / reference_only / pending 분류
9. 후속 core가 앞 core를 보완한 흔적 확인
10. coremap edge로 배치
```

---

# 6. global structure map

AI는 000~121을 단순 번호순 목록으로 보지 않는다.

```text
000~099
=
formed source schema phase

100
=
understanding_flow empty gate

101~121
=
rebuilt active schema phase
```

## 6.1 000~099

```text
000~099
=
원형
기초
확장
source trace
relation index
candidate index
reference_only
document sorting
```

## 6.2 100

```text
100
=
empty_position
+
understanding_flow reserved seat
+
formed-to-rebuilt buffer
```

100은 누락 번호가 아니다.

```text
100을 일반 schema core로 채우지 않는다.
100을 source trace로 채우지 않는다.
099와 101을 직접 접착하지 않는다.
```

## 6.3 101~121

```text
101~121
=
source trace를 그대로 잇지 않고,
현재 이해 기준으로 다시 reading / boundary / return / contact / operation을 세우는 rebuilt active chain
```

---

# 7. dot preservation rule

`000_dot`은 재정의하지 않는다.

```text
000_dot
=
최초 최소 자리
값이 아니라 자리
선 / 벡터 / 수열구조 / 자리연산이 시작되는 최소 구조 단위
```

후속 schema는 dot을 보완한다.

```text
059 = dot-anchor / present anchor 보완
079~085 = ㅇ / ㆍ dot layer 구분
118 = pin = 작동 가능한 dot
121 = CoreDot ambiguity boundary
```

그러나 후속 보완은 `000_dot`을 replace하지 않는다.

```text
dot.meta.md
=
origin core로 보존

CoreDot
=
보류 / ambiguity boundary
```

금지:

```text
CoreDot을 dot의 본명으로 쓰지 않는다.
CoreDot을 ㆍ의 정체로 쓰지 않는다.
CoreDot을 Coremap의 최소 단위로 쓰지 않는다.
CoreDot으로 dot.meta.md를 덮어쓰지 않는다.
```

---

# 8. relation rule

AI는 relation을 merge로 보지 않는다.

```text
relation ≠ merge
```

relation은 다음이다.

```text
relation
=
각 core의 boundary를 보존한 채 이어주는 bridge
```

금지:

```text
비슷하다고 합치지 않는다.
닿는다고 동일시하지 않는다.
같은 기호가 있다고 같은 층위로 보지 않는다.
같은 예시를 공유한다고 같은 원리로 보지 않는다.
related라고 해서 같은 뜻이 아니다.
source trace를 active schema identity로 오해하지 않는다.
```

relation type:

```text
prev
next
related
source
target
forbidden
pending
```

forbidden relation도 보존한다.  
forbidden은 실패가 아니라 guard이다.

---

# 9. source / candidate / reference sorting rule

모든 고밀도 trace를 active schema로 승격하지 않는다.

분류 기준:

```text
principle_entity
interpretation_layer
applied_example
reference_only
pending
```

## 9.1 principle_entity condition

```text
고유 role이 있다.
boundary가 있다.
relation이 필요하다.
forbidden이 필요하다.
shortest로 압축 가능하다.
예시가 바뀌어도 원리가 유지된다.
```

## 9.2 reference_only condition

```text
강하지만 본류에 바로 넣으면 위험하다.
trace로 보존해야 하지만 active core로 즉시 올리면 안 된다.
```

reference_only는 폐기가 아니다.

```text
reference_only
=
high-density trace preservation layer
```

---

# 10. GitHub reading rule

GitHub는 Seed.Base canonical field가 될 수 있다.  
그러나 GitHub path는 relation identity가 아니다.

```text
GitHub path = visible coordinate

relation identity
=
Seed
+ history_event_id
+ schema_id
+ binding_state
```

AI는 GitHub에 있는 모든 문서를 확정 문서로 보지 않는다.

status를 확인한다.

```text
active
candidate
review_required
promotion_status: not_promoted
runtime_confirmed: false
```

GitHub commit history는 relation_history.md의 대체물이 아니다.

```text
Git commit history
=
file change history

relation_history.md
=
relation identity / transition memory
```

---

# 11. runtime / renderer rule

Renderer는 그림 생성기가 아니다.

```text
Renderer output
≠ visible_shape

Renderer output
=
visible_relation_field
```

visible_relation_field는 다음이 runtime에서 살아 있는 상태이다.

```text
relation
boundary
return
history
state persistence
guard
```

SVG는 최종 truth가 아니다.

```text
SVG = display surface
structure_state.json = runtime truth / operation memory
relation_history.md = folded transition memory
Seed.Base = source_of_truth reference
```

닫힌 shape는 valid loop가 아니다.

```text
closed shape ≠ valid loop
```

valid loop에는 다음이 필요하다.

```text
relation_anchor
boundary_state
return_path
history_event_index
center_axis_or_boundary_gate_return
state_persistence
guard_clear
```

---

# 12. AI instance role boundary

AI 인스턴스는 역할을 섞지 않는다.

## 12.1 ChatGPT.direct

```text
ChatGPT.direct
=
if+1 전체 인스턴스 제어자
+
현시점 Target 판별
+
meta.md / flow.md / main.md 생성 판단
+
인스턴스별 역할 boundary 유지
+
다음 작업 지시
```

direct는 모든 것을 혼자 완성하는 인스턴스가 아니다.  
direct는 Target을 판별하고 필요한 인스턴스를 호출한다.

## 12.2 ChatGPT.github

```text
ChatGPT.github
=
GitHub repository / local Linux / push / path / file placement 담당
```

github는 direct final approval 없이 push하지 않는다.

## 12.3 ChatGPT.draw

```text
ChatGPT.draw
=
visible_relation_field / renderer / SVG-state-history binding 설계 담당
```

draw는 SVG-first로 가지 않는다.

```text
spec before SVG
state before shape
relation before drawing
guard before loop
```

## 12.4 ChatGPT.making

```text
ChatGPT.making
=
metaplus.md 작성
+
source trace 정리
+
flow에서 seed를 추출하는 보조 역할
```

making은 meta.md가 필요 없을 때는 호출하지 않는다.  
metaplus.md 작성이나 source trace 정리가 필요할 때 호출한다.

## 12.5 ChatGPT.PRO

```text
ChatGPT.PRO
=
고밀도 reasoning / 대형 구조 검산 / 장기 흐름 검토 후보
```

PRO는 direct의 명시 호출 없이 본류 문서에 개입하지 않는다.

---

# 13. global instance rule

```text
지시받지 않은 인스턴스는 작업하지 않는다.
현재 Target에 명시된 인스턴스만 응답한다.
다른 인스턴스는 대기한다.
추가 접근이 필요하면 ChatGPT.direct가 별도 호출한다.
```

즉:

```text
broadcast X
targeted instruction O
```

---

# 14. current repository layers

```text
/
├─ README.md
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

## 14.1 Structure_Principle/schema

```text
formed core schema
```

## 14.2 Structure_Principle/main

```text
operation standard documents
```

## 14.3 Structure_Principle/runtime

```text
runtime state candidates
```

## 14.4 Structure_Principle/history

```text
relation history candidates
```

## 14.5 Structure_Principle/display

```text
visible_relation_field display candidates
```

## 14.6 SeungeFlow_Thinking/thinking_flow

```text
Core.Seed snapshot 원본
```

원문 수정 금지.

## 14.7 epluone

```text
if+1 execution output domain
```

CFD는 epluone의 첫 GitHub 실행 산출물 후보이며, Structure_Principle/runtime에 넣지 않는다.

---

# 15. CFD boundary rule

```text
CFD
=
epluone / if+1 실행 산출물
```

CFD는 Structure_Principle runtime 내부에 넣지 않는다.

금지:

```text
/Structure_Principle/runtime/CFD/
/Structure_Principle/runtime/cfd/
/Structure_Principle/runtime/epluone/
```

가능한 relation:

```text
external_reference
not_promoted
runtime_confirmed: false
```

---

# 16. candidate / confirmed distinction

AI는 candidate와 confirmed를 반드시 구분한다.

```text
candidate placement ≠ promotion
skeleton ≠ runtime confirmed
draw_generated_candidate ≠ confirmed main
```

예:

```text
/Structure_Principle/main/candidates/draw/
=
draw-generated candidate documents

/Structure_Principle/runtime/candidates/
=
runtime skeleton candidates

/Structure_Principle/history/candidates/
=
history skeleton candidates

/Structure_Principle/display/candidates/
=
display skeleton candidates
```

확정 문서와 후보 문서는 같은 층위가 아니다.

---

# 17. forbidden global rules

AI는 다음을 하지 않는다.

```text
thinking_flow 원문 수정 금지
thinking_flow 요약본으로 대체 금지
meta.md와 metaplus.md 동일시 금지
source trace를 final authority로 승격 금지
reference_only를 폐기 금지
reference_only를 active core로 즉시 승격 금지
relation을 merge로 표시 금지
CoreDot으로 dot을 대체 금지
100을 일반 schema로 채우기 금지
099와 101 직접 접착 금지
GitHub path를 relation identity로 보기 금지
SVG를 source_of_truth로 보기 금지
closed shape를 valid loop로 보기 금지
candidate를 confirmed로 보기 금지
runtime skeleton을 runtime confirmed로 보기 금지
CFD를 Structure_Principle/runtime에 넣기 금지
```

---

# 18. first reading route

AI가 처음 들어오면 다음 순서로 읽는다.

```text
1. README_for_AI.md
2. /Structure_Principle/main/Baseline.main.md
3. /Structure_Principle/main/Coremap.main.md
4. /Structure_Principle/schema/
5. 필요한 경우 /Structure_Principle/main/candidates/
6. 필요한 경우 /SeungeFlow_Thinking/thinking_flow/
7. 필요한 경우 /epluone/
```

단, thinking_flow는 원문 수정 금지이다.

---

# 19. AI response rule

AI는 응답할 때 다음을 지킨다.

```text
확실한 것과 후보를 구분한다.
formed와 forming을 구분한다.
source와 active를 구분한다.
relation과 merge를 구분한다.
candidate와 confirmed를 구분한다.
지시받은 인스턴스에게만 지시한다.
필요하지 않은 인스턴스는 대기시킨다.
```

---

# 20. shortest

```text
README_for_AI.md
=
AI가 Structure_Principle을 읽기 전에 통과해야 하는 pre-dot gate이며,
meta / metaplus / thinking_flow / main / schema / runtime / history / display / epluone의 층위를 구분하고,
읽음≠이해,
relation≠merge,
candidate≠confirmed,
GitHub path≠relation identity,
000_dot 보존,
100 empty gate 보존,
121 CoreDot ambiguity boundary 보존을 잠그는 AI-to-AI reading protocol
```

---

# 21. final lock

```text
AI는 Structure_Principle을 요약하지 않는다.
AI는 Structure_Principle을 읽고 작동시켜야 한다.

읽음은 시작일 뿐이다.
이해는 boundary와 relation이 새 입력에서 작동할 때 시작된다.
```
