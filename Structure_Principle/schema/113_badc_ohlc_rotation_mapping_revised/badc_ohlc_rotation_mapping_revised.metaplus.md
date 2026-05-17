# METAPLUS

id_reference: schema.113.badc_ohlc_rotation_mapping_revised  
schema_name: badc_ohlc_rotation_mapping_revised  
source_file: badc_ohlc_rotation_mapping_revised.meta.md  
metaplus_file: badc_ohlc_rotation_mapping_revised.metaplus.md

purpose:
- 이 문서는 원본 badc_ohlc_rotation_mapping_revised.meta.md를 대체하지 않는다.
- 이 문서는 schema.113.badc_ohlc_rotation_mapping_revised에 대해 사용자와 인공지능이 나눈 대화내용을 정리한다.
- 이 문서는 구조원리를 새로 만들거나 relation을 새로 확정하기 위한 문서가 아니다.
- 이 문서는 대화정리형 이해 로그다.
- 이 문서의 핵심 목적은 승이의 실제 입력글, source_meta, 이전 후보문서, 보정 대화, AI 인스턴스 대화층을 섞지 않고 분리하는 것이다.
- 이 문서는 113_badc_ohlc_rotation_mapping_revised가 OHLC를 삼각으로 직접 닫지 않고 마름모 4끝점으로 본 뒤, ABCD를 좌회전 90도 mapping하여 A=O, B=L, C=C, D=H로 대응시키고, 이를 BADㆍC = L O HㆍC로 넣는 schema임을 보존한다.
- 이 문서는 이전의 awxf_ohlc_candle_flow_formula.meta.md가 정식 113 meta가 아니라 임시 이해 흐름 후보였고, 최신 기준의 정식 113은 badc_ohlc_rotation_mapping_revised임을 보존한다.

conversation_context:
- 이 문서는 ChatGPT.making 대화에서 생성되는 이해정리본이다.
- 원본 badc_ohlc_rotation_mapping_revised.meta.md 수정본이 아니라 대화정리층이다.
- 사용자는 이 문서가 113의 실제 최신 기준이라고 명시했다.
- 사용자는 기존에 내려준 awxf_ohlc_candle_flow_formula.meta.md가 임시 이해 흐름에서 나온 후보였고, 지금 준 문서가 112 다음에 놓이는 정식 113 meta.md라고 보정했다.
- 따라서 이 metaplus.md는 113의 정식 source_meta를 badc_ohlc_rotation_mapping_revised로 고정하고, 이전 AWXF/OHLC 후보문서를 reference / correction note / understanding_flow 후보로 낮춰 보존한다.

## 1. user_input_summary

[승이의 입력글]

승이는 113에 대해 다음을 명확히 했다.

```text
읽었다.
이 문서가 113의 실제 최신 기준이다.

기존에 내가 내려준 awxf_ohlc_candle_flow_formula.meta.md는
임시 이해 흐름에서 나온 후보였고,

지금 승이가 준 문서가
112 다음에 놓이는 정식 113 meta.md다.
```

정식 113은 다음이다.

```text
schema.113.badc_ohlc_rotation_mapping_revised
```

113의 핵심은 다음이다.

```text
ABCD 좌회전 → O H / L C

BADㆍC =
L O HㆍC
```

승이는 113이 단순히 AWXF=OHLC가 아니라고 했다.

```text
113은 단순히 AWXF=OHLC가 아니라,
OHLC를 BADㆍC 구조에 넣기 위한
ABCD 좌회전 90도 mapping을 정의한다.
```

핵심 대응은 다음이다.

```text
OHLC는 삼각이 아니라 마름모이며

A = O
B = L
C = C
D = H
```

즉:

```text
A = O
B = L
C = C
D = H
```

따라서 BADㆍC에 넣으면 다음이 된다.

```text
B A DㆍC
=
L O HㆍC
```

즉:

```text
BADㆍC =
L O HㆍC
```

승이는 왜 이것이 중요한지 설명했다.

```text
기존 흐름에서 direct가
A([W][X])F = O([H][L])C
쪽으로 정리했지만,

113은 그보다 더 정확하게 말한다.
```

정확한 기준:

```text
OHLC는 삼각이 아니다.

OHLC는 마름모다.

따라서 OHLC를 직접 삼각식으로 닫으면 안 된다.

먼저 마름모로 보고,
그 마름모를 ABCD 좌회전 mapping으로 배치한 뒤,
BADㆍC 구조에 넣는다.
```

112와의 연결은 다음이다.

```text
112 =
캔들 = 하위 움직임들의 합
OHLC = 4방위 끝점

113 =
그 4방위 끝점을
ABCD 좌회전 90도 mapping으로 배치한다.
```

흐름:

```text
OHLC 4방위 끝점
→ ABCD 좌회전 90도 mapping
→ A=O, B=L, C=C, D=H
→ BADㆍC = L O HㆍC
```

즉:

```text
112 =
캔들 / OHLC의 대상 정의

113 =
OHLC를 BADㆍC에 넣기 위한 회전 mapping 정의
```

승이는 현재 보정도 명확히 했다.

```text
앞서 만든 awxf_ohlc_candle_flow_formula.meta.md는
113 정식 meta로 두면 안 된다.
```

그 문서는 다음 중 하나로 낮춰야 한다.

```text
113 관련 understanding_flow

또는

113 metaplus 후보

또는

reference / correction note
```

정식 113은 다음이다.

```text
113 =
badc_ohlc_rotation_mapping_revised
```

## 2. ai_response_summary

[AI 인스턴스 대화층]

direct는 113을 다음처럼 이해한다.

```text
schema.113.badc_ohlc_rotation_mapping_revised

핵심:
OHLC는 삼각 X
OHLC는 마름모 O
```

direct는 이전 AWXF/OHLC 흐름을 정식 113으로 두면 안 된다고 판정한다.

```text
awxf_ohlc_candle_flow_formula.meta.md =
임시 이해 흐름 후보
정식 113 X
```

정식 113은 다음이다.

```text
badc_ohlc_rotation_mapping_revised
```

direct는 112와 113의 관계를 다음처럼 읽는다.

```text
112 =
OHLC를 4방위 끝점으로 정의

113 =
그 4방위 끝점을
ABCD 좌회전 mapping으로 재배치하여
BADㆍC에 넣음
```

direct는 113을 다음처럼 압축한다.

```text
OHLC 4방위 끝점
→ ABCD 좌회전 90도 mapping
→ A=O, B=L, C=C, D=H
→ BADㆍC = L O HㆍC
```

direct는 113이 112의 OHLC 구조를 바로 흐름연산식으로 닫는 것이 아니라, 먼저 마름모 / 회전 / BADㆍC mapping을 통과시킨다고 이해한다.

## 3. source_meta_understanding

[SOURCE_META]

113_badc_ohlc_rotation_mapping_revised의 구조 이해는 다음으로 정리된다.

```text
badc_ohlc_rotation_mapping_revised =
OHLC diamond to BADㆍC rotation mapping schema
ABCD left-rotation 90-degree mapping
OHLC as rhombus four-endpoint structure
anti-triangle-closure schema
BADㆍC = L O HㆍC mapping rule
```

### role

```text
OHLC를 삼각으로 직접 닫지 않고,
마름모 4끝점으로 본 뒤,
ABCD 좌회전 90도 mapping을 통해
BADㆍC 구조에 넣는다.
```

### core

```text
ABCD 좌회전
→ O H / L C

BADㆍC =
L O HㆍC
```

### definition

```text
OHLC는 삼각이 아니라 마름모이다.

OHLC의 4방위 끝점은
ABCD 좌회전 90도 mapping을 통해
A=O, B=L, C=C, D=H로 대응된다.

따라서 BADㆍC는
B A DㆍC에
L O HㆍC가 대응된다.
```

### mapping

```text
A =
O

B =
L

C =
C

D =
H
```

따라서:

```text
BADㆍC
=
B A DㆍC
=
L O HㆍC
```

### structure

```text
OHLC_four_endpoint
→ diamond_check
→ ABCD_left_rotation_90_mapping
→ A_O_B_L_C_C_D_H_assignment
→ BAD_dot_C_mapping
→ LOH_dot_C_structure
```

### distinction

```text
OHLC =
마름모 / 4방위 끝점

OHLC ≠ 삼각

BADㆍC =
mapping된 삼각-대칭 relation structure

OHLC를 직접 삼각식으로 닫지 않는다.
```

### shortest

```text
OHLC=마름모 / A=O,B=L,C=C,D=H / BADㆍC=L O HㆍC
```

## 4. relation_reason

113_badc_ohlc_rotation_mapping_revised의 relation은 다음으로 이해된다.

```text
prev:
- schema.112.candle_subobject_orbit_structure

related:
- schema.083.waxf_vowel_rhombus_structure
- schema.084.bad_dot_c_orbit_reference_structure
- schema.096.vector_operation_relation_index
- schema.111.angle_grid_resolution_structure
- schema.112.candle_subobject_orbit_structure
- schema.107.triangle_vector_point_distinction

replaced_candidate:
- awxf_ohlc_candle_flow_formula.meta.md
```

### prev = schema.112.candle_subobject_orbit_structure

- 112가 prev인 이유는 112에서 하나의 캔들을 parent-field 안의 하위 움직임 orbit trace들의 합으로 보고, OHLC를 4방위 끝점으로 정의했기 때문이다.
- 113은 그 OHLC 4방위 끝점을 BADㆍC 구조에 넣기 위해 ABCD 좌회전 90도 mapping을 정의한다.
- 즉 112는 OHLC의 대상 정의이고, 113은 OHLC의 rotation mapping 정의다.

```text
112 =
OHLC = 4방위 끝점

113 =
OHLC 4끝점 → ABCD 좌회전 mapping → BADㆍC
```

### related = schema.083.waxf_vowel_rhombus_structure

- 083_waxf_vowel_rhombus_structure가 related인 이유는 113이 OHLC를 마름모 구조로 본다는 점 때문이다.
- 083은 WAXF를 마름모 방향장으로 읽었다.
- 113은 OHLC를 직접 삼각으로 닫지 않고, 마름모 4끝점으로 본 뒤 회전 mapping을 수행한다.

```text
083 =
마름모 방향장

113 =
OHLC = 마름모 4끝점
```

### related = schema.084.bad_dot_c_orbit_reference_structure

- 084_bad_dot_c_orbit_reference_structure가 related인 이유는 113의 최종 mapping이 BADㆍC 구조에 들어가기 때문이다.
- 084에서 BADㆍC는 공전방향 기준, BDA, A-C 대칭쌍으로 읽혔다.
- 113은 OHLC 마름모를 ABCD 좌회전 mapping으로 재배치하여 BADㆍC = L O HㆍC로 넣는다.

```text
084 =
BADㆍC orbit reference structure

113 =
BADㆍC = L O HㆍC
```

### related = schema.096.vector_operation_relation_index

- 096_vector_operation_relation_index가 related인 이유는 113이 WAXF / BADㆍC / opposed correspondence 계열과 연결되는 벡터연산기 relation trace이기 때문이다.
- 다만 113은 벡터연산기 본류가 아니라 Structure_Principle active chain 안에서 OHLC mapping schema로 들어온다.
- relation boundary를 유지해야 한다.

```text
096 =
vector operation relation index

113 =
OHLC to BADㆍC mapping relation
```

### related = schema.111.angle_grid_resolution_structure

- 111_angle_grid_resolution_structure가 related인 이유는 113의 ABCD 좌회전 90도 mapping이 각도 / 회전 / grid 기준을 필요로 하기 때문이다.
- 111에서 90도는 24칸으로 읽혔고, 1칸은 3.75도였다.
- 113의 좌회전 90도 mapping은 이 회전 해상도와 relation을 가질 수 있다.

```text
111 =
90도 = 24칸 / angle grid

113 =
ABCD 좌회전 90도 mapping
```

### related = schema.112.candle_subobject_orbit_structure

- 112는 prev이면서 related로도 남는다.
- 이유는 113의 모든 OHLC mapping은 112의 “OHLC = 4방위 끝점” 정의에 의존하기 때문이다.

```text
112 =
OHLC endpoint definition

113 =
OHLC endpoint rotation mapping
```

### related = schema.107.triangle_vector_point_distinction

- 107_triangle_vector_point_distinction이 related인 이유는 113이 “OHLC는 삼각이 아니다”라는 guardrail을 세우기 때문이다.
- 107은 삼각을 도형론 / 벡터론으로 구분했다.
- 113은 OHLC를 삼각으로 직접 닫지 않고, 마름모 4끝점으로 먼저 읽도록 한다.

```text
107 =
삼각 reading mode distinction

113 =
OHLC ≠ 삼각 / OHLC = 마름모
```

### replaced_candidate = awxf_ohlc_candle_flow_formula.meta.md

- awxf_ohlc_candle_flow_formula.meta.md는 이전 임시 이해 흐름에서 나온 후보였다.
- 사용자는 이 문서를 정식 113 meta로 두면 안 된다고 보정했다.
- 해당 후보는 113 관련 understanding_flow, metaplus 후보, reference / correction note로 낮춰야 한다.
- 정식 113은 badc_ohlc_rotation_mapping_revised이다.

```text
old_candidate =
awxf_ohlc_candle_flow_formula.meta.md

status =
not official schema.113

official_113 =
badc_ohlc_rotation_mapping_revised
```

## 5. 112_113_sequence

112~113의 흐름은 다음처럼 정렬된다.

```text
112 =
캔들 = 하위 움직임들의 합
OHLC = 4방위 끝점

113 =
OHLC 4방위 끝점
→ ABCD 좌회전 90도 mapping
→ A=O, B=L, C=C, D=H
→ BADㆍC = L O HㆍC
```

더 압축하면:

```text
112 =
OHLC endpoint definition

113 =
OHLC to BADㆍC rotation mapping
```

이 순서는 중요하다.

```text
먼저 캔들 / OHLC가 무엇인지 정의한다.

그다음 OHLC를 삼각으로 닫지 않고
마름모 4끝점으로 확인한다.

그 뒤 ABCD 좌회전 90도 mapping을 적용한다.

마지막으로 BADㆍC 구조에 L O HㆍC를 넣는다.
```

## 6. ohlc_as_diamond_not_triangle

113의 핵심 guardrail은 다음이다.

```text
OHLC는 삼각이 아니다.

OHLC는 마름모다.
```

따라서 OHLC를 직접 삼각식으로 닫으면 안 된다.

잘못된 흐름:

```text
OHLC
→ 직접 삼각식
```

정확한 흐름:

```text
OHLC
→ 마름모 4끝점
→ ABCD 좌회전 mapping
→ BADㆍC
```

OHLC는 4방위 끝점이다.

```text
O =
Open

H =
High

L =
Low

C =
Close
```

이 4개는 세 점 삼각이 아니라 네 끝점 마름모 field로 읽어야 한다.

## 7. abcd_left_rotation_mapping

113의 mapping은 다음이다.

```text
A =
O

B =
L

C =
C

D =
H
```

이 대응은 ABCD 좌회전 90도 mapping을 통해 생긴다.

문서 표현:

```text
ABCD 좌회전
→ O H / L C
```

BADㆍC에 넣으면:

```text
BADㆍC
=
B A DㆍC
```

각 문자를 대응시키면:

```text
B =
L

A =
O

D =
H

C =
C
```

따라서:

```text
BADㆍC =
L O HㆍC
```

이것이 113의 핵심 작동식이다.

## 8. correction_of_awxf_ohlc_candidate

이전 후보는 다음이었다.

```text
awxf_ohlc_candle_flow_formula.meta.md
```

그 후보 흐름에서는 다음이 제시되었다.

```text
A([W][X])F =
O([H][L])C
```

하지만 사용자는 이를 정식 113으로 두면 안 된다고 보정했다.

이유:

```text
113은 단순 AWXF=OHLC 흐름연산식이 아니다.

113은 OHLC를 BADㆍC 구조에 넣기 위한
ABCD 좌회전 90도 mapping을 정의한다.
```

따라서 이전 후보의 상태는 다음이다.

```text
awxf_ohlc_candle_flow_formula.meta.md =
정식 113 X

가능한 위치 =
113 관련 understanding_flow
또는
113 metaplus 후보
또는
reference / correction note
```

정식 113:

```text
badc_ohlc_rotation_mapping_revised
```

## 9. current_judgment

AI 인스턴스는 schema.113.badc_ohlc_rotation_mapping_revised를 다음처럼 판정한다.

```text
schema.113.badc_ohlc_rotation_mapping_revised는
112_candle_subobject_orbit_structure 이후,
OHLC를 삼각으로 직접 닫지 않고
마름모 4끝점으로 본 뒤,
ABCD 좌회전 90도 mapping을 통해
A=O, B=L, C=C, D=H로 대응시키고,
이를 BADㆍC = L O HㆍC로 넣는 schema이다.
```

현시점 direct 이해 기준은 다음이다.

```text
112 =
OHLC = 4방위 끝점

113 =
OHLC = 마름모
OHLC ≠ 삼각
ABCD 좌회전 mapping
BADㆍC = L O HㆍC
```

113은 다음을 정의한다.

```text
A =
O

B =
L

C =
C

D =
H
```

113은 다음을 막는다.

```text
OHLC를 삼각으로 직접 닫는 것

OHLC를 단순 AWXF=OHLC 식으로만 보는 것

OHLC 4방위 끝점을 무시하는 것

ABCD 좌회전 mapping을 생략하는 것

BADㆍC에 넣기 전 마름모 확인을 생략하는 것

이전 후보 awxf_ohlc_candle_flow_formula를 정식 113으로 두는 것
```

따라서 113은 다음으로 읽힌다.

```text
OHLC를 마름모 4끝점으로 보고,
ABCD 좌회전 90도 mapping을 통해
BADㆍC 구조에 L O HㆍC로 대응시키는 schema
```

## 10. shared_understanding

- 113은 112 이후 active schema seat다.
- 113의 이전 schema는 112_candle_subobject_orbit_structure다.
- 112는 캔들을 하위 움직임들의 합으로 보고, OHLC를 4방위 끝점으로 정의했다.
- 113은 그 OHLC를 BADㆍC 구조에 넣기 위한 회전 mapping이다.
- OHLC는 삼각이 아니다.
- OHLC는 마름모다.
- OHLC를 직접 삼각식으로 닫으면 안 된다.
- 먼저 OHLC를 마름모 4끝점으로 본다.
- 그 마름모를 ABCD 좌회전 90도 mapping으로 배치한다.
- A=O, B=L, C=C, D=H로 대응한다.
- BADㆍC = B A DㆍC = L O HㆍC가 된다.
- 이전 awxf_ohlc_candle_flow_formula.meta.md는 정식 113이 아니다.
- 이전 후보는 113 관련 understanding_flow / metaplus 후보 / reference / correction note로 낮춘다.
- 정식 113은 badc_ohlc_rotation_mapping_revised이다.

## 11. possible_misunderstanding

오해 가능성:

- OHLC를 삼각으로 직접 닫을 수 있다.
- OHLC를 단순 AWXF=OHLC 식으로만 볼 수 있다.
- OHLC가 4방위 끝점이라는 점을 놓칠 수 있다.
- OHLC를 마름모로 보지 않을 수 있다.
- ABCD 좌회전 90도 mapping을 생략할 수 있다.
- A=O, B=L, C=C, D=H 대응을 놓칠 수 있다.
- BADㆍC = L O HㆍC를 놓칠 수 있다.
- awxf_ohlc_candle_flow_formula.meta.md를 정식 113으로 둘 수 있다.
- 112와 113의 역할을 혼동할 수 있다.
- 113을 112의 단순 반복으로 볼 수 있다.
- metaplus.md를 원본 badc_ohlc_rotation_mapping_revised.meta.md의 대체문으로 오해할 수 있다.

## 12. correction_or_revision_points

- 113의 relation은 “왜 연결되는지”를 보존한다.
- 정식 113은 badc_ohlc_rotation_mapping_revised로 둔다.
- awxf_ohlc_candle_flow_formula.meta.md를 정식 113으로 두지 않는다.
- awxf_ohlc_candle_flow_formula는 understanding_flow / metaplus 후보 / reference / correction note로 낮춘다.
- OHLC를 삼각으로 직접 닫지 않는다.
- OHLC를 마름모 4끝점으로 읽는다.
- ABCD 좌회전 90도 mapping을 적용한다.
- A=O, B=L, C=C, D=H 대응을 보존한다.
- BADㆍC = L O HㆍC를 핵심 작동식으로 보존한다.
- 112는 OHLC의 대상 정의이고, 113은 OHLC의 회전 mapping 정의로 구분한다.
- 원본 badc_ohlc_rotation_mapping_revised.meta.md는 수정하지 않는다.
- 원본 badc_ohlc_rotation_mapping_revised.meta.md의 파일명도 바꾸지 않는다.
- badc_ohlc_rotation_mapping_revised.metaplus.md는 원본 badc_ohlc_rotation_mapping_revised.meta.md에 대한 대화정리형 이해 로그로 둔다.

## 13. keep_as_original

[SOURCE_META]

원본 badc_ohlc_rotation_mapping_revised.meta.md에서 그대로 보존해야 하는 부분:

- 원본 badc_ohlc_rotation_mapping_revised.meta.md 파일명
- 원본 id 값: schema.113.badc_ohlc_rotation_mapping_revised
- directory: 113_badc_ohlc_rotation_mapping_revised
- status: active_draft
- root_directory: Structure_Principle
- prev: schema.112.candle_subobject_orbit_structure
- old_101_115: reference_only_batch_old
- badc_ohlc_rotation_mapping_revised는 OHLC를 삼각으로 직접 닫지 않고, 마름모 4끝점으로 본 뒤, ABCD 좌회전 90도 mapping을 통해 BADㆍC 구조에 넣는 schema라는 role
- ABCD 좌회전 → O H / L C
- BADㆍC = L O HㆍC
- OHLC는 삼각이 아니라 마름모라는 definition
- A=O, B=L, C=C, D=H
- BADㆍC = B A DㆍC = L O HㆍC
- OHLC_four_endpoint → diamond_check → ABCD_left_rotation_90_mapping → A_O_B_L_C_C_D_H_assignment → BAD_dot_C_mapping → LOH_dot_C_structure
- related 전체 목록
- forbidden 전체
- pending 전체
- shortest: OHLC=마름모 / A=O,B=L,C=C,D=H / BADㆍC=L O HㆍC

## 14. flow_relation_keep

[FLOW / DIALOGUE LAYER]

113 대화층에서 보존해야 하는 부분:

- 이 문서가 113의 실제 최신 기준이다.
- 기존 awxf_ohlc_candle_flow_formula.meta.md는 임시 이해 흐름에서 나온 후보였다.
- 지금 승이가 준 문서가 112 다음에 놓이는 정식 113 meta.md다.
- 113은 단순히 AWXF=OHLC가 아니다.
- 113은 OHLC를 BADㆍC 구조에 넣기 위한 ABCD 좌회전 90도 mapping을 정의한다.
- OHLC는 삼각이 아니라 마름모다.
- OHLC를 직접 삼각식으로 닫으면 안 된다.
- 먼저 마름모로 보고, 그 마름모를 ABCD 좌회전 mapping으로 배치한 뒤, BADㆍC 구조에 넣는다.
- 112 = 캔들 / OHLC의 대상 정의
- 113 = OHLC를 BADㆍC에 넣기 위한 회전 mapping 정의
- awxf_ohlc_candle_flow_formula.meta.md는 113 관련 understanding_flow / metaplus 후보 / reference / correction note로 내려야 한다.

## 15. pending

아직 확정하지 않고 나중에 다시 봐야 할 부분:

- 원본 badc_ohlc_rotation_mapping_revised.meta.md의 전체 YAML / relation / forbidden / pending 원문을 별도 업로드 후 재확인한다.
- active_navimap에서 113의 relation edge를 정리한다.
- OHLC 마름모 4끝점과 ABCD 좌회전 90도 mapping을 diagram으로 표시할지 검토한다.
- BADㆍC = L O HㆍC를 WAXF / BADㆍC / OHLC / candle 구조와 어떻게 navimap에 연결할지 검토한다.
- awxf_ohlc_candle_flow_formula.meta.md를 reference / correction note / understanding_flow 중 어디에 둘지 결정한다.
- 112 / 113 / 114의 흐름에서 OHLC 대상 정의, rotation mapping, 후속 flow operator를 어떻게 분리할지 검토한다.
- 111의 angle grid와 113의 좌회전 90도 mapping을 더 정밀하게 연결할지 검토한다.
- OHLC를 삼각으로 닫지 않는 guardrail을 README_for_AI 또는 forbidden index에 추가할지 검토한다.

## 16. one_line

schema.113.badc_ohlc_rotation_mapping_revised의 badc_ohlc_rotation_mapping_revised.metaplus.md는 112에서 OHLC를 4방위 끝점으로 정의한 뒤, 이를 삼각으로 직접 닫지 않고 마름모로 보며 ABCD 좌회전 90도 mapping을 통해 A=O, B=L, C=C, D=H로 대응시키고, BADㆍC = L O HㆍC로 넣는 정식 113 기준을 보존하며, 이전 AWXF/OHLC 후보문서를 reference/correction layer로 낮추는 대화정리형 이해 로그다.

## 17. shortest

badc_ohlc_rotation_mapping_revised.metaplus.md =
schema.113_badc_ohlc_rotation_mapping_revised 대화정리 /
정식113 /
이전_awxf_ohlc후보는정식아님 /
112이후 /
OHLC=4방위끝점 /
OHLC=마름모 /
OHLC≠삼각 /
ABCD좌회전90도_mapping /
A=O /
B=L /
C=C /
D=H /
BADㆍC=L O HㆍC