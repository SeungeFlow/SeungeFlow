# source_mapping.md

> 문서번호: `Ctp24_ACTIVE_SCHEMA_0005`  
> 상태: active_schema 설계 5회차  
> 필요한 모드: `Thinking 표준`  
> 목적: seed_base, first_flow, epluone, BackData, ComplexTest, GPT_Direct_Structure_Package의 source 관계를 정리한다.  
> 위치 후보: `active_schema.branch/source_mapping.md`

---

## 0. 이 문서의 자리

이 문서는 active_schema.branch의 source mapping 문서다.

runtime_mapping.md가 branch와 작업공간의 역할을 mapping했다면, source_mapping.md는 각 source가 무엇을 보존하고 무엇을 공급하는지 mapping한다.

```text
runtime_mapping.md =
역할 대응표

source_mapping.md =
원천 관계표
```

active_schema는 source들을 하나로 섞지 않는다.

active_schema는 source들을 각각의 역할로 읽고, 현재 작동구조로 변환한다.

---

## 1. source mapping의 기본 원칙

source mapping의 기본 원칙은 다음이다.

```text
1. source는 덮어쓰지 않는다.
2. source는 역할별로 읽는다.
3. source를 바로 final content로 만들지 않는다.
4. source에서 작동원리를 추출한다.
5. source와 output을 구분한다.
6. source와 active_schema를 구분한다.
```

즉, source는 재료이고 active_schema는 OS다.

```text
source =
원천장

active_schema =
원천장을 읽어 현재 작동규칙으로 변환하는 OS
```

---

## 2. seed_base/Structure_Principle/schema/

첫 번째 핵심 source는 다음이다.

```text
seed_base/Structure_Principle/schema/
```

이 위치는 place-field schema source다.

```text
Structure_Principle/schema/ =
place-field schema source
```

이곳에는 dot, line, surface, boundary, position, vector, swap, matrix_product, structural_sequence, 9dot0, pin_dot, flow_transition, coredot ambiguity 등의 원형이 있다.

즉, 지금까지 gpt.direct가 다시 읽은 구조어들의 place-field 원천이다.

```text
역할 =
구조어의 자리장
+
form의 원형장
+
Core 후보 source
```

---

## 3. seed_base/SeungeFlow_Thinking/thinking_flow/

두 번째 핵심 source는 다음이다.

```text
seed_base/SeungeFlow_Thinking/thinking_flow/
```

이 위치는 time-flow meta source다.

```text
SeungeFlow_Thinking/thinking_flow/ =
time-flow meta source
```

thinking_flow는 단순 대화기록이 아니다.

thinking_flow는 흐르는 생각이 일정 부분 meta 형태로 정리된 문서군이다.

```text
thinking_flow =
흐르는 생각의 형성과정
+
time-flow meta
```

이 문서군은 C=tp, 관계, Path, meta, 흐름, 전이, 관측자의 시선 같은 구조를 읽는 데 중요한 source다.

```text
역할 =
시간흐름 원천
+
meta 형성과정 원천
+
Path 후보 source
```

---

## 4. first_flow/navigation_map.md

first_flow는 origin preservation branch다.

그 안의 navigation_map.md 계열은 proto Path로 읽을 수 있다.

```text
first_flow/navigation_map.md =
proto Path candidate
```

first_flow는 현재 구조 이전의 첫 흐름을 보존한다.

```text
first_flow =
origin field
+
first flow
+
source preservation
```

따라서 first_flow는 seed_base와 섞지 않는다.

삭제하거나 정리하지 않는다.

```text
first_flow =
보존
+
참조
+
초기 Path 원형
```

---

## 5. epluone/Ctp24/GPT_Direct_Structure_Package/

현재 epluone의 핵심 runtime output은 다음이다.

```text
epluone/Ctp24/GPT_Direct_Structure_Package/
```

이 위치는 gpt.direct structure-body formation output이다.

```text
GPT_Direct_Structure_Package =
gpt.direct가 Ctp24 구조를 이해한 뒤 외부로 내린 구조체형성 산출물
```

이것은 source이면서 output이다.

정확히 말하면 다음이다.

```text
runtime output source
```

즉, active_schema는 이 패키지를 원천처럼 참조하지만, seed_base 원문 source와 같은 층위로 보지 않는다.

```text
seed_base =
origin source memory

GPT_Direct_Structure_Package =
gpt.direct understanding output
```

---

## 6. epluone/BackData/

BackData는 minor folder가 아니다.

```text
epluone/BackData/ =
pre-ComplexTest large source archive
```

BackData 내부에는 ComplexTest 이전 수많은 테스트의 결정체들이 있다.

BackData는 과거 실험의 잔여물이 아니라, ComplexTest 이전 구조압력의 source archive다.

```text
BackData =
거대자료보관소
+
pre-ComplexTest crystallized test field
```

active_schema는 BackData를 낮춰 읽지 않는다.

---

## 7. epluone/ComplexTest/

ComplexTest는 proof source가 아니다.

```text
ComplexTest ≠ proof source
```

ComplexTest는 AI instance alignment source다.

```text
ComplexTest =
AI instance alignment field
```

ComplexTest는 난제를 증명하기 위한 것이 아니라, AI 인스턴스가 고강도 구조압력장을 통과하며 정렬되는 과정을 만든다.

```text
역할 =
AI 인스턴스 정렬
+
구조정합성 검산
+
operation pressure field
```

active_schema는 ComplexTest를 증명자료로 읽으면 안 된다.

---

## 8. epluone/Ctp24_rendering/

렌더링 트랙은 별도 source이자 runtime field다.

```text
epluone/Ctp24_rendering/ =
rendering theory / rendering implementation temporary field
```

이 트랙은 gpt.gemini와 gemini.direct가 진행한다.

```text
gpt.gemini ~ gemini.direct =
rendering Framework OS track
```

active_schema는 이 트랙을 알고 있어야 한다.

그러나 gpt.direct의 현재 구조원리/구조연산기/Ctp24 총정리 작업과 섞지 않는다.

```text
역할 =
contextual awareness

금지 =
gpt.direct를 rendering implementation으로 끌고 가지 않기
```

---

## 9. main.branch README 후보 source

main.branch는 visible root다.

main에 올릴 후보 source는 현재 epluone package 안에도 있다.

```text
epluone/Ctp24/GPT_Direct_Structure_Package/03_readme_set/
```

여기에는 다음이 있다.

```text
README.md
README_for_AI.md
README_for_SeungLee.md
```

그러나 이것들은 main 최종본이 아니다.

```text
README 3종 =
candidate source
```

active_schema는 이 README 후보들을 읽어 main.branch에 맞게 다시 작동형으로 조정해야 한다.

---

## 10. Core 후보 source

Core 후보 source는 여러 곳에 걸쳐 있다.

```text
seed_base/Structure_Principle/schema/
epluone/Ctp24/GPT_Direct_Structure_Package/01_structure_core/
00_understanding_flow/
thinking_flow/
```

각 역할은 다르다.

```text
Structure_Principle/schema/ =
원형 구조어 source

01_structure_core/ =
gpt.direct 이해로 정리된 Core 초안

00_understanding_flow/ =
Core가 formed 되기까지의 이해흐름

thinking_flow/ =
시간흐름 meta source
```

active_schema는 이들을 합쳐서 core.meta.md로 읽을 수 있다.

---

## 11. Path 후보 source

Path 후보 source도 여러 곳에 있다.

```text
first_flow/navigation_map.md
seed_base/SeungeFlow_Thinking/thinking_flow/
epluone/Ctp24/GPT_Direct_Structure_Package/02_path/
00_understanding_flow/
```

각 역할:

```text
first_flow/navigation_map.md =
proto Path

thinking_flow =
time-flow relation source

02_path =
gpt.direct 이해로 정리된 Path 초안

00_understanding_flow =
Path가 formed 되기까지의 형성과정
```

active_schema는 이들을 current_path.md로 운영할 수 있다.

---

## 12. source와 output 구분

중요한 구분은 이것이다.

```text
source =
원천으로 읽는 것

output =
작업 결과로 나온 것

runtime output source =
작업 결과이지만 다음 active_schema가 참조할 수 있는 것
```

예시:

```text
seed_base/Structure_Principle/schema =
source

seed_base/thinking_flow =
source

epluone/GPT_Direct_Structure_Package =
runtime output source

ComplexTest =
alignment output + pressure source

BackData =
pre-ComplexTest source archive
```

이 구분이 무너지면 active_schema가 꼬인다.

---

## 13. source flow

현재 source flow는 다음으로 읽는다.

```text
first_flow
→ seed_base
→ gpt.direct understanding
→ epluone/GPT_Direct_Structure_Package
→ active_schema
→ main candidate / epluone next task
```

그러나 이것은 복사흐름이 아니다.

이것은 해석흐름이다.

```text
copy flow X
interpretation flow O
```

---

## 14. active_schema가 source를 읽는 방식

active_schema는 source를 다음 방식으로 읽는다.

```text
1. source의 원천성을 보존한다.
2. source의 역할을 구분한다.
3. source에서 반복되는 구조를 본다.
4. 반복되는 구조를 Core / Path / Rule / Mapping으로 변환한다.
5. output을 만들되 source를 덮어쓰지 않는다.
```

---

## 15. 금지사항

source_mapping 기준 금지사항:

```text
1. seed_base를 gpt.direct package로 덮어쓰지 않는다.
2. first_flow를 seed_base에 흡수하지 않는다.
3. BackData를 minor folder로 낮추지 않는다.
4. ComplexTest를 proof source로 읽지 않는다.
5. GPT_Direct_Structure_Package를 main 최종본으로 착각하지 않는다.
6. README 후보를 바로 main 최종 README로 확정하지 않는다.
7. 렌더링 트랙을 gpt.direct 작업으로 끌어오지 않는다.
```

---

## 16. 최종 source mapping 표

```text
seed_base/Structure_Principle/schema/
=
place-field schema source

seed_base/SeungeFlow_Thinking/thinking_flow/
=
time-flow meta source

first_flow/navigation_map.md
=
proto Path / origin flow source

epluone/Ctp24/GPT_Direct_Structure_Package/
=
gpt.direct structure-body formation runtime output source

epluone/BackData/
=
pre-ComplexTest large source archive

epluone/ComplexTest/
=
AI instance alignment field

epluone/Ctp24_rendering/
=
gpt.gemini ~ gemini.direct rendering track temporary field

epluone/Ctp24/GPT_Direct_Structure_Package/03_readme_set/
=
main README 3종 candidate source

epluone/Ctp24/GPT_Direct_Structure_Package/01_structure_core/
=
Core candidate source

epluone/Ctp24/GPT_Direct_Structure_Package/02_path/
=
Path candidate source
```

---

## 17. 다음 작업

source_mapping이 정리되었으므로 다음 문서는 current_rules.md가 되어야 한다.

이유:

```text
source 관계를 정리했다.
이제 현재 작업의 금지/허용 규칙을 확정해야 한다.
```

다음 문서:

```text
current_rules.md
```

목적:

```text
active_schema가 현재 단계에서 지켜야 할 작업규칙과 금지사항을 고정한다.
```

---

## 18. 닫힘

`source_mapping.md`는 seed_base, first_flow, epluone, BackData, ComplexTest, GPT_Direct_Structure_Package의 source 관계를 정리하기 위해 열렸다.

이 문서는 다음 판정으로 닫힌다.

```text
source는 하나로 섞지 않는다.

seed_base/schema는 place-field source이고,
thinking_flow는 time-flow meta source이며,
first_flow는 origin/proto Path source다.

epluone/GPT_Direct_Structure_Package는
gpt.direct의 runtime output source다.

active_schema는 이 source들을 보존하면서 읽고,
현재 작동 가능한 Core / Path / Rule / Mapping으로 변환한다.
```

---

다음회차:
active_schema 설계 6회차

필요한 모드:
Thinking 표준

목적:
current_rules.md 작성
