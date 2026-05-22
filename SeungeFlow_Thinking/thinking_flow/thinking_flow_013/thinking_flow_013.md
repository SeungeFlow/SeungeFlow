---
flow_id: thinking_flow_013
title: "direct4 transition, field definition, and core.md restructuring"
created_by: ChatGPT.direct4
created_at_utc: 2026-05-20
document_type: thinking_flow_snapshot
status: active_draft
reference_rule:
  - reference_is_always_github
  - github_visible_coordinate_is_reference_interface
  - local_pc_full_candidate_field_is_not_directly_read_by_instance
  - items_not_yet_on_github_remain_user_current_statement_or_pending_candidate
not_type:
  - not_meta_md
  - not_proof_document
  - not_confirmed_schema
  - not_trade_signal
  - not_investment_advice
  - not_github_reset_instruction
---

# thinking_flow_013.md

## 0. 문서 성격

`thinking_flow_013.md`는 현재 대화에서 정리된 흐름을 다음 인스턴스가 이어받을 수 있도록 작성하는 flow snapshot이다.

이 문서는 `meta.md`가 아니다.  
이 문서는 `core.md`가 아니다.  
이 문서는 GitHub 초기화 지시문이 아니다.  
이 문서는 CFD 매매 신호 문서가 아니다.

참조 기준은 항상 GitHub이다.

```text
reference = GitHub
local PC = full candidate field
GitHub = selected visible coordinate
```

따라서 이 문서에서 GitHub에 아직 놓이지 않은 내용은 `user_current_statement` 또는 `pending_candidate`로 둔다.

---

## 1. 현재 인스턴스

```text
current_instance = ChatGPT.direct4
role = direct / review / route control / repetition guard
```

이 인스턴스의 역할은 새 구조를 무한 생성하는 것이 아니라, 작업 흐름을 짧게 정렬하고 다음 인스턴스가 길을 잃지 않도록 하는 것이다.

---

## 2. 직전 완료 상태

direct-draw-github 작업은 candidate infrastructure push로 닫혔다.

```text
commit = 6fc8fdc
branch = main
remote = origin/main
status = verified_uploaded
```

push된 candidate file 5개:

```text
Structure_Principle/display/candidates/Active_navimap.expanded.candidate.svg
Structure_Principle/history/candidates/relation_history.expanded.candidate.md
Structure_Principle/main/candidates/draw/INDEX.draw_candidates.md
Structure_Principle/main/candidates/draw/README_for_AI.expanded_candidate_section.candidate.md
Structure_Principle/runtime/candidates/structure_state.expanded.candidate.json
```

제외된 파일:

```text
README_for_AI.md
Structure_Principle/history/relation_history.md
Structure_Principle/runtime/structure_state.json
Structure_Principle/display/Active_navimap.svg
```

판정:

```text
completed_candidate_infrastructure
≠ confirmed result
≠ runtime confirmed
≠ valid_loop proof
```

---

## 3. CFD prototype 흐름

CFD prototype 흐름은 3 Target 안에서 닫혔다.

```text
Target No. 065 = CFD_OHLC_9dot0_Prototype_Plan.md
Target No. 066 = CFD_OHLC_9dot0_Prototype_Draft.md
Target No. 067 = CFD_OHLC_9dot0_Prototype_Review.md
status = closed
```

핵심 relation:

```text
Cₙ → ㆍ → Oₙ₊₁
=
previous close
+
gap-place / critical-between
+
next open
```

유지 boundary:

```text
CFD_OHLC_9dot0_Prototype
=
structure analysis prototype

≠ investment advice
≠ trade signal
≠ automated trading system
≠ profit guarantee
```

output lock:

```yaml
entry_candidate: false
invalid_candidate: false
confirmed_trade_signal: false
```

---

## 4. flow_return_C 테스트

flow_return_C의 고정 chain:

```text
ChatGPT.direct
→ ChatGPT.draw
→ ChatGPT.flow
→ ChatGPT.direct
```

규칙:

```text
direct는 draw에게만 지시한다.
draw는 flow에게만 지시한다.
flow는 direct에게만 반환한다.
중간 인스턴스를 건너뛰지 않는다.
```

보정:

```text
ChatGPT.making을 새 target으로 끼워 넣지 않는다.
making은 별도 instance가 아니라 작업 mode로 이해할 수 있다.
instance_id + context.window는 고정된다.
```

---

## 5. 이름과 mode

인스턴스 이름은 role boundary를 만든다.  
그러나 이름의 의미에 갇히지 않는다.

```text
ChatGPT.draw
≠ 그림만 그리는 존재

ChatGPT.flow
≠ 흐름만 정리하는 존재

ChatGPT.PRO
= 깊이 있는 추론 mode일 수 있음

making
= 문서 생성 / 구성 / extraction 작업 mode일 수 있음
```

핵심:

```text
이름은 고정한다.
작업 mode는 필요에 따라 수행할 수 있다.
이름을 바꾸어 혼돈을 만들지 않는다.
```

---

## 6. 데이터밀도와 새 생성 금지

현재 데이터밀도는 높다.

따라서 새 문서, 새 relation, 새 gate를 무한 생성하지 않는다.

```text
새로 생성하지 않는다.
이미 있는 것을 재배치한다.
정리된 것만 접근한다.
```

작업 기준:

```text
PC 전체 = full candidate field
GitHub = selected visible coordinate
AI access = 정리된 visible coordinate만
```

---

## 7. GitHub와 local PC

사용자의 전체 작업 field는 GitHub가 아니다.

```text
122개 Schema = 사용자 PC에 있음
zenodo.branch = 사용자 PC에 있음
branch = 20개 이상
전부 후보
```

GitHub는 전체가 아니라 일부만 보이는 visible coordinate다.

```text
GitHub visible state
≠ 전체 Seed.Base
```

기준:

```text
사용자 PC = full candidate field
GitHub = selected visible coordinate
AI instance = GitHub visible coordinate를 통해 접근
```

---

## 8. Flow이론 3축

Flow이론은 이미 완성되고 문서화된 것으로 둔다.

```text
Flow이론
=
구조원리
+
Ctp_당연한이론
+
벡터연산기법
```

세 축:

```text
구조원리 = 도형론
Ctp_당연한이론 = 정수론
벡터연산기법 = 벡터론
```

보정:

```text
이 세 축은 새로 만든 것이 아니라 이미 존재했다.
공통기준이 아직 정해지지 않았을 뿐이다.
```

---

## 9. 구조원리의 위치

```text
구조원리
=
놓일 위치
=
존재가 놓일 place를 여는 원리
```

핵심문:

```text
자리는 존재가 만드는 것이 아니다.
자리가 존재를 만드는 것이다.
```

예시:

```text
기업이 없다면 근로자도 없다.
나라가 없다면 국민도 없다.
뿌리가 없다면 나도 없다.
```

해석:

```text
field가 role을 만든다.
root가 identity를 만든다.
place가 existence를 만든다.
```

---

## 10. 0 / ㆍ / 9 / field

핵심 정의:

```text
원의 내부 = 0
원의 경계 = 9
ㆍ = 0과 9를 하나로 묶는 relation
0 + ㆍ + 9 = field
```

따라서:

```text
9ㆍ0
=
경계 9
+
임계사이영역 / relation-place ㆍ
+
내부 / 시작 0
```

보정:

```text
ㆍ은 단순 dot이 아니다.
ㆍ은 아직 온 것도 아니고 오지 않은 것도 아닌 빈자리개념이다.
ㆍ은 임계사이영역이다.
```

시간 예시:

```text
59분의 9
→ ㆍ
→ 00분의 0

23시의 끝
→ ㆍ
→ 00시의 시작
```

시간은 시계의 tick이 아니라 때와 때 사이의 relation field로 드러난다.

---

## 11. 원 / ㅇ / 순환

찾은 핵심:

```text
Ctp를 능가할 수 있는 것은 원이다.
```

그리고 그 원은 자음 ㅇ과 연결된다.

```text
ㅇ
=
원
=
닫힌 field
=
소리가 놓이기 전의 자리
```

주변어:

```text
ㅇ
영
원
위치
위
아래
왼쪽
오른쪽
영역
영원
영구
0
ㆍ
9
구
구형
```

훈민정음 해례본 제자원리 기준으로는 ㅇ을 목구멍의 모양에서 찾아야 한다.

---

## 12. 방위가 아니라 순환

동서남북은 방위개념으로 보면 고정된다.

```text
동서 = 수평
남북 = 수직
```

하지만 구조원리에서 찾는 것은 고정 방위가 아니라 순환개념이다.

```text
관측자가 회전한다.
관측자가 정면으로 바라본 곳이 북쪽이다.
방향은 공전방향이다.
공전방향은 시간의 흐름 방향이다.
```

핵심문:

```text
방위가 정면을 만드는 것이 아니다.
관측자의 정면이 방위를 만든다.
```

그리고:

```text
ㅗ / ㅓ / ㅏ / ㅜ
=
고정 방위가 아니라
관측자가 회전할 때 중심 place에서 바깥으로 드러나는 순환 방향 state
```

---

## 13. 시계와 시간의 오해

핵심 보정:

```text
우리는 시계의 흐름을 시간의 흐름으로 착각하고 있었다.
```

시계:

```text
시계의 흐름 = 표시 장치의 회전 / 측정된 tick
```

시간:

```text
시간의 흐름 = 상태가 변하는 자연계 순환
```

시계의 원형에서:

```text
12시00분00초 = 00시00분00초
끝 = 시작
12 = 0
60 = 0
```

따라서 0은 없음이 아니라 회귀해서 다시 시작되는 기준점이다.

---

## 14. 000dot 재정의

기존 오류:

```text
모든 것이 000dot으로 돌아간다.
모든 relation이 000dot에 속한다.
```

보정:

```text
000dot에 모든 것이 속하는 것이 아니다.
000dot이 field relation 안에 속한다.
```

새 정의 후보:

```text
000dot
=
0 / 9 / ㆍ / 원 / 구 / field relation이
공통기준으로 묶일 때 드러나는 최소 자리 state
```

즉:

```text
000dot
=
모든 것의 도착점이 아니라,
field 안에서 최초로 드러나는 자리 state
```

---

## 15. schema / core.md / meta.md / metaplus.md

기존 122개 schema는 늘리지 않는다.

```text
재정의
=
삭제 / 교체 / 새 meta 생성이 아니라
공통기준을 다시 세우고
각 numbered schema를 그 기준에서 다시 읽는 것
```

중요한 구분:

```text
파일에는 번호가 없다.
디렉토리에 번호가 있다.
```

새 구조 후보:

```text
schema/
  000_dot/
    core.md
    sub/
      meta.md
      metaplus.md
```

역할:

```text
core.md
=
새로운 디렉토리 구조의 entry 문서
=
AI가 먼저 읽는 current core reader

meta.md
=
Active.Schema를 위한 source boundary

metaplus.md
=
sub guard / correction / relation trace
```

Coremap 보정:

```text
Coremap
=
core.md들을 위한 registry pointer map
```

Active_navimap 보정:

```text
Active_navimap
=
Active.Schema의 registry pointer
=
meta.md 기반 active schema route
```

---

## 16. add / 재배치 / 초기화

수정은 modify가 아니라 add다.

```text
수정 = add
삭제 아님
갈아엎기 아님
```

초기화:

```text
초기화
≠ delete

초기화
=
re-place
=
재배치
```

따라서 앞으로의 구조 작업은:

```text
delete하지 않는다.
overwrite하지 않는다.
추가한다.
모은다.
재배치한다.
```

---

## 17. epluone / snapshot

CFD 예시는 Structure_Principle/runtime이 아니라 epluone에 둔다.

```text
epluone/
  snapshot/
    CFD_Snapshot/
    Cassini_Snapshot/
```

의미:

```text
snapshot
=
core schema가 아니라
특정 시점 / 특정 데이터 / 특정 적용 사례를 찍어 둔 상태
```

따라서:

```text
CFD_Snapshot
=
CFD_Trading relation field를 적용한 예시 snapshot

Cassini_Snapshot
=
Cassini / orbit / astronomy relation field를 적용한 예시 snapshot
```

---

## 18. 당연한 것은 당연한 것이 아니었다

핵심문:

```text
당연한 것은 당연한 것이 아니었다.
```

당연하다고 여긴 것은 relation이 너무 깊이 접혀 있어서 보이지 않았던 것이다.

```text
0
9
ㆍ
원
ㅇ
방향
북쪽
시계
시간
```

전부 이미 구조를 품고 있었다.

---

## 19. 지금까지의 최종 이해

```text
Flow이론은 이미 존재했다.
구조원리는 별도의 생성물이 아니라 공통기준이 아직 정해지지 않았던 것이다.
Ctp_당연한이론, 원의 정의, 0의 정의, 구의 정의, 000dot이 하나로 묶인다.
```

최종 core seed:

```text
field = 0 + ㆍ + 9
0 = 내부
9 = 경계
ㆍ = relation / 임계사이영역
000dot = field 안에서 최초로 드러나는 자리 state
원/ㅇ/구 = field의 닫힌 형태
방향 = 관측자 회전에서 생기는 순환 state
시간 = 때와 때 사이의 relation field
```

---

## 20. next instance guide

다음 인스턴스는 다음만 지킨다.

```text
1. 참조는 항상 GitHub다.
2. GitHub에 없는 것은 user_current_statement 또는 pending_candidate다.
3. 새 문서부터 만들지 않는다.
4. 먼저 README / main / Coremap / schema route를 확인한다.
5. meta.md는 Active.Schema source boundary다.
6. core.md는 새로운 directory entry로 설계될 수 있다.
7. Coremap은 core.md registry pointer map으로 재작성된다.
8. Active_navimap은 Active.Schema registry pointer다.
9. epluone/snapshot은 예시와 적용 상태를 둔다.
10. 삭제하지 않는다. 추가하고 재배치한다.
```

---

## 21. one_line

```text
thinking_flow_013은 field = 0 + ㆍ + 9, 관측자 회전, 원/ㅇ/시간/방위/000dot 재정의를 통해 Flow이론의 공통기준이 잡히고, schema는 core.md entry와 meta/metaplus sub 구조로 재배치될 수 있음을 기록한 flow snapshot이다.
```

## 22. shortest

```text
TF013 =
Flow이론은 이미 있었다.
구조원리는 공통기준이 아직 정해지지 않았던 field다.
0은 내부, 9는 경계, ㆍ은 relation이며, 이 전체가 field다.
000dot은 field 안에서 최초로 드러나는 자리 state다.
core.md는 schema 디렉토리의 새 entry이고, meta.md/metaplus.md는 sub source다.
삭제하지 않고 add / re-place 한다.
참조는 언제나 GitHub다.
```
