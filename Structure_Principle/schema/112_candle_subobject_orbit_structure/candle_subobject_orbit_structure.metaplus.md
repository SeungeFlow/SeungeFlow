# METAPLUS

id_reference: schema.112.candle_subobject_orbit_structure  
schema_name: candle_subobject_orbit_structure  
source_file: candle_subobject_orbit_structure.meta.md  
metaplus_file: candle_subobject_orbit_structure.metaplus.md

purpose:
- 이 문서는 원본 candle_subobject_orbit_structure.meta.md를 대체하지 않는다.
- 이 문서는 schema.112.candle_subobject_orbit_structure에 대해 사용자와 인공지능이 나눈 대화내용을 정리한다.
- 이 문서는 구조원리를 새로 만들거나 relation을 새로 확정하기 위한 문서가 아니다.
- 이 문서는 대화정리형 이해 로그다.
- 이 문서의 핵심 목적은 승이의 실제 입력글, source_meta, 후속 flow, AI 인스턴스 대화층을 섞지 않고 분리하는 것이다.
- 이 문서는 112_candle_subobject_orbit_structure가 하나의 캔들을 단일 막대가 아니라 parent-field 안의 하위 움직임 orbit trace들의 합으로 보고, 그 결과로 드러난 OpenㆍHighㆍLowㆍClose를 4방위 끝점으로 정의하는 schema임을 보존한다.
- 이 문서는 111_angle_grid_resolution_structure와 113_AWXF/OHLC 흐름연산식 사이에서, 112가 “캔들 자체의 구조적 대상 정의” 역할을 한다는 점을 보존한다.

conversation_context:
- 이 문서는 ChatGPT.making 대화에서 생성되는 이해정리본이다.
- 원본 candle_subobject_orbit_structure.meta.md 수정본이 아니라 대화정리층이다.
- 사용자는 schema.112.candle_subobject_orbit_structure를 읽고, 112가 아직 AWXF=OHLC 흐름연산식으로 들어가기 전 단계라고 설명했다.
- 사용자는 112가 캔들 자체가 무엇인지를 정의하는 문서라고 했다.
- 사용자는 111의 각도/칸수 해상도 격자와 113의 흐름연산식 사이에서 112가 parent-field / subobject orbit trace / OHLC 4방위 끝점 구조를 세운다고 설명했다.
- 이 문서는 사용자의 직접 입력과 AI 인스턴스 대화층을 분리해 보존한다.

## 1. user_input_summary

[승이의 입력글]

승이는 112를 다음처럼 읽었다.

```text
schema.112.candle_subobject_orbit_structure
```

핵심은 다음이다.

```text
캔들 =
하위 움직임들의 합

OHLC =
4방위 끝점
```

승이는 112가 아직 AWXF=OHLC 흐름연산식으로 들어가기 전 단계라고 했다.

```text
112는 캔들 자체가 무엇인가를 정의한다.
```

112의 역할은 다음이다.

```text
하나의 캔들을
상위 장 안의 하위 움직임들의 궤도합으로 읽는다.
```

여기서:

```text
큰 캔들 =
parent-field

내부 하위 움직임 =
orbit trace

OHLC =
그 orbit trace가 외부에 드러낸 4방위 끝점
```

예시:

```text
1시간봉 =
parent-field

60개 1분봉 =
하위 움직임 / orbit trace

1시간봉 OHLC =
하위 움직임들의 압축 끝점
```

승이는 111과 112의 연결을 다음처럼 설명했다.

111은 각도 / 칸수 해상도였다.

```text
45도 =
12칸

90도 =
24칸

한 칸 =
3.75도
```

이후 피타고라스 보정에서 다음이 열렸다.

```text
대각1ㆍ수직2개ㆍ대각1
=
14 + 10 + 10 + 14
=
48
```

그리고 60분 대응:

```text
60 ÷ 48 =
1.25

14:20:14
→ 17.5:25:17.5

정수고정
→ 3:4:3
=
18:24:18
```

즉:

```text
111 =
해상도 격자

112 =
그 격자 안에서 캔들 하나를
하위 움직임의 궤도합으로 읽는 방식
```

승이는 113과의 관계도 다음처럼 잡았다.

```text
112 =
캔들 = 하위 움직임들의 합
OHLC = 4방위 끝점

113 =
A([W][X])F = O([H][L])C
AI용 일반식 = O([A][B])C
```

따라서:

```text
112 =
캔들의 구조적 대상 정의

113 =
캔들의 흐름연산식 정의
```

한 줄 정리:

```text
112는 하나의 캔들을 단일 막대가 아니라
parent-field 안의 하위 움직임 orbit trace들의 합으로 보고,
그 결과로 드러난 OpenㆍHighㆍLowㆍClose를
4방위 끝점으로 정의하는 meta 문서다.
```

## 2. ai_response_summary

[AI 인스턴스 대화층]

direct는 112를 다음처럼 이해한다.

```text
schema.112.candle_subobject_orbit_structure

핵심:
캔들 = 하위 움직임들의 합
OHLC = 4방위 끝점
```

direct는 112를 111 이후, 113 이전의 중간 정의 schema로 읽는다.

```text
111 =
각도 / 칸수 해상도 격자

112 =
캔들 자체의 parent-field / subobject orbit trace 정의

113 =
OHLC를 AWXF 흐름연산식으로 압축
```

direct는 112가 캔들을 단일 막대나 단일 값으로 보지 않는다고 판정한다.

```text
캔들 =
상위 시간장 / 가격장 안에 들어 있는
하위 움직임들의 궤도합
```

direct는 OHLC를 단순 네 가격값이 아니라, 하위 움직임들이 외부에 드러낸 4방위 끝점으로 본다.

```text
O =
시작 끝점 / open endpoint

H =
상방 극점 / high endpoint

L =
하방 극점 / low endpoint

C =
닫힘 끝점 / close endpoint
```

direct는 112를 다음처럼 압축한다.

```text
112 =
candle as parent-field containing subobject orbit traces
```

## 3. source_meta_understanding

[SOURCE_META]

112_candle_subobject_orbit_structure의 구조 이해는 다음으로 정리된다.

```text
candle_subobject_orbit_structure =
candle as parent-field schema
subobject orbit trace aggregation
OHLC as four-direction endpoint structure
higher timeframe candle from lower timeframe motions
pre-AWXF/OHLC operation schema
```

### role

```text
하나의 캔들을
상위 장 안의 하위 움직임들의 궤도합으로 읽고,
OHLC를 그 궤도합이 외부에 드러낸 4방위 끝점으로 정의한다.
```

### core

```text
캔들 =
하위 움직임들의 합

OHLC =
4방위 끝점
```

### definition

```text
하나의 캔들은 단일 막대가 아니라,
상위 시간장 / 가격장 안에서 발생한 하위 움직임들의 orbit trace가 압축된 구조체이다.

OpenㆍHighㆍLowㆍClose는 단순 가격 네 개가 아니라,
하위 움직임들의 궤도합이 외부에 드러낸
4방위 끝점이다.
```

### structure

```text
parent_field
→ subobject_motions
→ orbit_trace_aggregation
→ endpoint_extraction
→ OHLC_four_direction_endpoints
```

### candle_layer

```text
candle =
parent-field

large candle =
상위 시간장 / 상위 가격장

lower candles =
하위 움직임 / subobject orbit traces

single candle =
subobject orbit trace들의 압축 결과
```

### OHLC_layer

```text
O =
open / 시작 끝점

H =
high / 상방 극점

L =
low / 하방 극점

C =
close / 닫힘 끝점
```

### four_direction_endpoint

```text
OHLC =
하위 움직임이 외부에 드러낸
4방위 끝점 구조
```

### shortest

```text
캔들=하위움직임들의합 / OHLC=4방위끝점
```

## 4. relation_reason

112_candle_subobject_orbit_structure의 relation은 다음으로 이해된다.

```text
prev:
- schema.111.angle_grid_resolution_structure

next_candidate:
- schema.113.AWXF_OHLC_flow_operator_structure

related:
- schema.052.hyperstructure_renderer_architecture
- schema.057.seedbase_database_data_definition
- schema.083.waxf_vowel_rhombus_structure
- schema.097.science_renderer_candidate_index
- schema.111.angle_grid_resolution_structure
- schema.113.AWXF_OHLC_flow_operator_structure
```

### prev = schema.111.angle_grid_resolution_structure

- 111이 prev인 이유는 111에서 방향전이를 각도 / 칸수 해상도 격자로 읽는 기준이 세워졌기 때문이다.
- 112는 그 해상도 격자 위에서 캔들 하나를 parent-field로 보고, 그 내부 하위 움직임들의 orbit trace를 읽는다.
- 즉 111이 방향의 resolution 기준을 세운다면, 112는 그 resolution 안에서 시간장 / 가격장 / 하위 움직임의 압축 결과를 캔들로 읽는다.

```text
111 =
각도 해상도 격자

112 =
그 격자 안의 parent-field candle / subobject orbit trace
```

### next_candidate = schema.113.AWXF_OHLC_flow_operator_structure

- 113이 다음 후보로 연결되는 이유는 112가 캔들 자체의 구조적 대상 정의이고, 113은 그 OHLC 끝점을 AWXF / O([H][L])C 흐름연산식으로 압축하기 때문이다.
- 112가 “캔들이 무엇인가”를 정의한다면, 113은 “그 캔들의 OHLC 흐름을 어떻게 식으로 읽을 것인가”를 정의한다.

```text
112 =
캔들의 구조적 대상 정의

113 =
캔들의 흐름연산식 정의
```

### related = schema.052.hyperstructure_renderer_architecture

- 052_hyperstructure_renderer_architecture가 related인 이유는 캔들 구조가 visible_relation_field / renderer 후보가 될 수 있기 때문이다.
- 캔들 하나를 단순 막대가 아니라 하위 움직임들의 orbit trace와 OHLC endpoint로 렌더링하면, relation structure를 시각화할 수 있다.

```text
052 =
HyperRendererCore / visible_relation_field

112 =
candle as orbit trace aggregation renderer candidate
```

### related = schema.057.seedbase_database_data_definition

- 057_seedbase_database_data_definition이 related인 이유는 캔들 안의 subobject motions / OHLC / timeframe / endpoint / trace가 모두 data로 보존될 수 있기 때문이다.
- 112는 가격 데이터 자체를 다루는 것이 아니라, 데이터가 구조적으로 어떻게 압축되는지 읽는다.

```text
057 =
wide data definition

112 =
OHLC / lower timeframe motions / orbit trace as structured data
```

### related = schema.083.waxf_vowel_rhombus_structure

- 083_waxf_vowel_rhombus_structure가 related인 이유는 112의 OHLC 4방위 끝점이 WAXF / 마름모 방향장과 연결될 수 있기 때문이다.
- 112는 아직 AWXF=OHLC 식으로 들어가지 않지만, OHLC를 4방위 끝점으로 정의한다.
- 이 4방위 구조는 WAXF / AWXF / OHLC 흐름으로 이어질 수 있다.

```text
083 =
WAXF 마름모 방향장

112 =
OHLC = 4방위 끝점
```

### related = schema.097.science_renderer_candidate_index

- 097_science_renderer_candidate_index가 related인 이유는 캔들 구조가 과학 renderer라기보다 데이터 구조 / visible_relation_field 구현 후보로 연결될 수 있기 때문이다.
- 단, 금융 차트 해석을 과학적 증명으로 보지 않는다.
- 112는 trading / chart data를 구조원리식 relation-field로 읽는 applied renderer candidate에 가깝다.

```text
097 =
renderer candidate index

112 =
candle orbit trace visible relation candidate
```

### related = schema.111.angle_grid_resolution_structure

- 111은 prev이면서 related로도 남는다.
- 이유는 112의 캔들 내부 orbit trace를 각도 / 칸수 / resolution 기준으로 읽으려면 111의 grid가 계속 필요하기 때문이다.

```text
111 =
angle grid

112 =
candle trace read within grid
```

### related = schema.113.AWXF_OHLC_flow_operator_structure

- 113은 next_candidate이면서 related로도 남는다.
- 112의 OHLC 4방위 끝점이 113에서 AWXF / O([H][L])C 흐름연산식으로 압축되기 때문이다.

```text
112 =
OHLC endpoint structure

113 =
OHLC flow operator structure
```

## 5. 111_112_113_sequence

111~113 흐름은 다음처럼 정렬된다.

```text
111 =
각도 / 칸수 해상도 격자

112 =
그 격자 안에서 캔들 하나를
하위 움직임의 궤도합으로 읽는 방식

113 =
그 캔들의 OHLC 끝점을
AWXF / O([H][L])C 흐름연산식으로 압축
```

더 압축하면:

```text
111 =
resolution grid

112 =
candle as orbit aggregation

113 =
OHLC flow operator
```

이 순서는 중요하다.

```text
각도 해상도 기준이 있어야 방향과 기울기를 읽을 수 있다.

그 기준 위에서 캔들 내부 하위 움직임들의 궤도를 읽을 수 있다.

그 궤도의 외부 끝점 OHLC를 다음 schema에서 흐름연산식으로 압축할 수 있다.
```

## 6. candle_as_parent_field

112는 캔들을 단일 막대로 보지 않는다.

```text
캔들 =
parent-field
```

예를 들어 1시간봉 하나는 다음처럼 읽힌다.

```text
1시간봉 =
parent-field
```

그 안에는 하위 움직임이 있다.

```text
60개 1분봉 =
subobject motions
=
orbit traces
```

1시간봉의 OHLC는 그 하위 움직임들의 압축 끝점이다.

```text
1시간봉 OHLC =
하위 움직임들의 압축 끝점
```

따라서:

```text
candle =
하위 움직임들이 지나간 궤도 흔적의 압축 구조
```

## 7. ohlc_as_four_direction_endpoints

OHLC는 단순 가격 네 개가 아니다.

```text
OHLC =
4방위 끝점
```

각각은 다음처럼 읽힌다.

```text
O =
Open =
시작 끝점

H =
High =
상방 극점

L =
Low =
하방 극점

C =
Close =
닫힘 끝점
```

OHLC는 하위 orbit trace가 외부에 남긴 압축 좌표다.

```text
하위 움직임
→ orbit trace
→ endpoint extraction
→ O/H/L/C
```

즉:

```text
OHLC =
하위 움직임들의 궤도합이 외부에 드러낸
4방위 endpoint structure
```

## 8. resolution_ratio_flow

사용자는 111 이후 피타고라스 보정 흐름을 112와 연결했다.

```text
대각1ㆍ수직2개ㆍ대각1
=
14 + 10 + 10 + 14
=
48
```

그리고 60분 대응:

```text
60 ÷ 48 =
1.25
```

따라서:

```text
14:20:14
→ 17.5:25:17.5
```

정수고정:

```text
3:4:3
=
18:24:18
```

이 flow는 다음처럼 이해된다.

```text
111 =
angle grid resolution

112 =
time/candle parent-field 안의 orbit trace를
grid / ratio / endpoint로 읽는 방식
```

아직 이 비율은 112 source_meta 안의 최종 공식으로 확정하지 않는다.

다만 112의 flow layer에서, 캔들 내부 하위 움직임을 해상도 / 시간 / 칸수 / ratio로 읽기 위한 연결 후보로 보존한다.

## 9. current_judgment

AI 인스턴스는 schema.112.candle_subobject_orbit_structure를 다음처럼 판정한다.

```text
schema.112.candle_subobject_orbit_structure는
111_angle_grid_resolution_structure 이후,
하나의 캔들을 단일 막대가 아니라
parent-field 안의 하위 움직임 orbit trace들의 합으로 보고,
그 결과로 드러난 OpenㆍHighㆍLowㆍClose를
4방위 끝점으로 정의하는 schema이다.
```

현시점 direct 이해 기준은 다음이다.

```text
111 =
angle resolution grid

112 =
candle as parent-field / subobject orbit aggregation

113 =
OHLC flow operator candidate
```

112는 다음을 정의한다.

```text
캔들 =
하위 움직임들의 합

OHLC =
4방위 끝점
```

112는 다음을 막는다.

```text
캔들을 단일 막대로만 보는 것

OHLC를 단순 가격 네 개로만 보는 것

상위 캔들 내부 하위 움직임을 삭제하는 것

orbit trace를 보지 않고 endpoint만 보는 것

112를 113의 흐름연산식과 혼동하는 것
```

따라서 112는 다음으로 읽힌다.

```text
하나의 캔들을
상위 장 안의 하위 움직임들의 궤도합으로 보고,
OHLC를 그 궤도합이 외부에 드러낸
4방위 끝점으로 정의하는 schema
```

## 10. shared_understanding

- 112는 111 이후 active schema seat다.
- 112의 이전 schema는 111_angle_grid_resolution_structure다.
- 111은 각도 / 칸수 해상도 격자다.
- 112는 그 격자 안에서 캔들 하나를 하위 움직임의 궤도합으로 읽는다.
- 캔들은 단일 막대가 아니다.
- 캔들은 parent-field이다.
- 캔들 내부에는 하위 움직임들이 있다.
- 하위 움직임들은 orbit trace로 읽힌다.
- OHLC는 하위 움직임들의 압축 끝점이다.
- OHLC는 4방위 끝점이다.
- 1시간봉은 parent-field이고, 60개 1분봉은 하위 움직임 / orbit trace다.
- 1시간봉 OHLC는 하위 움직임들의 압축 endpoint다.
- 112는 캔들의 구조적 대상 정의다.
- 113은 캔들의 흐름연산식 정의로 이어질 수 있다.

## 11. possible_misunderstanding

오해 가능성:

- 캔들을 단일 막대로만 볼 수 있다.
- OHLC를 단순 가격 네 개로만 볼 수 있다.
- 하위 timeframe 움직임을 삭제할 수 있다.
- parent-field와 subobject orbit trace의 관계를 놓칠 수 있다.
- OHLC를 4방위 끝점으로 보지 않을 수 있다.
- 112를 곧바로 AWXF=OHLC 흐름연산식으로 오해할 수 있다.
- 112와 113의 역할을 혼동할 수 있다.
- 111의 angle grid와 112의 candle orbit trace 관계를 놓칠 수 있다.
- 금융 차트 예시를 과학적 증명으로 오해할 수 있다.
- metaplus.md를 원본 candle_subobject_orbit_structure.meta.md의 대체문으로 오해할 수 있다.

## 12. correction_or_revision_points

- 112의 relation은 “왜 연결되는지”를 보존한다.
- 캔들을 단일 막대로만 보지 않는다.
- 캔들을 parent-field로 읽는다.
- 하위 움직임을 subobject orbit trace로 읽는다.
- OHLC를 단순 가격 네 개로 보지 않는다.
- OHLC를 하위 움직임들이 외부에 드러낸 4방위 끝점으로 읽는다.
- 112는 캔들의 구조적 대상 정의로 둔다.
- 113은 캔들의 흐름연산식 정의로 분리한다.
- 111의 angle grid와 112의 candle orbit aggregation을 연결하되 동일시하지 않는다.
- 60분 / 48칸 / 3:4:3 보정 흐름은 flow layer에 보존하고, source_meta 정의로 과잉 확정하지 않는다.
- 원본 candle_subobject_orbit_structure.meta.md는 수정하지 않는다.
- 원본 candle_subobject_orbit_structure.meta.md의 파일명도 바꾸지 않는다.
- candle_subobject_orbit_structure.metaplus.md는 원본 candle_subobject_orbit_structure.meta.md에 대한 대화정리형 이해 로그로 둔다.

## 13. keep_as_original

[SOURCE_META]

원본 candle_subobject_orbit_structure.meta.md에서 그대로 보존해야 하는 부분:

- 원본 candle_subobject_orbit_structure.meta.md 파일명
- 원본 id 값: schema.112.candle_subobject_orbit_structure
- directory: 112_candle_subobject_orbit_structure
- status: active_draft
- root_directory: Structure_Principle
- prev: schema.111.angle_grid_resolution_structure
- old_101_115: reference_only_batch_old
- candle_subobject_orbit_structure는 하나의 캔들을 상위 장 안의 하위 움직임들의 궤도합으로 읽고, OHLC를 그 궤도합이 외부에 드러낸 4방위 끝점으로 정의하는 schema라는 role
- 캔들 = 하위 움직임들의 합
- OHLC = 4방위 끝점
- parent_field → subobject_motions → orbit_trace_aggregation → endpoint_extraction → OHLC_four_direction_endpoints
- related 전체 목록
- forbidden 전체
- pending 전체
- shortest: 캔들=하위움직임들의합 / OHLC=4방위끝점

## 14. flow_relation_keep

[FLOW / DIALOGUE LAYER]

112 대화층에서 보존해야 하는 부분:

- 112는 아직 AWXF=OHLC 흐름연산식으로 들어가기 전 단계다.
- 112는 캔들 자체가 무엇인가를 정의한다.
- 1시간봉 = parent-field
- 60개 1분봉 = 하위 움직임 / orbit trace
- 1시간봉 OHLC = 하위 움직임들의 압축 끝점
- 111은 각도 / 칸수 해상도 격자다.
- 피타고라스 보정 흐름: 대각1ㆍ수직2개ㆍ대각1 = 14 + 10 + 10 + 14 = 48
- 60 ÷ 48 = 1.25
- 14:20:14 → 17.5:25:17.5
- 정수고정 → 3:4:3 = 18:24:18
- 112는 그 격자 안에서 캔들 하나를 하위 움직임의 궤도합으로 읽는 방식이다.
- 113은 A([W][X])F = O([H][L])C / AI용 일반식 = O([A][B])C로 이어진다.
- 112 = 캔들의 구조적 대상 정의
- 113 = 캔들의 흐름연산식 정의

## 15. pending

아직 확정하지 않고 나중에 다시 봐야 할 부분:

- 원본 candle_subobject_orbit_structure.meta.md의 전체 YAML / relation / forbidden / pending 원문을 별도 업로드 후 재확인한다.
- active_navimap에서 112의 relation edge를 정리한다.
- parent-field / subobject orbit trace / OHLC endpoint를 시각화할지 검토한다.
- 1시간봉 / 60개 1분봉 예시를 renderer prototype으로 만들지 검토한다.
- 14:20:14 → 17.5:25:17.5 → 18:24:18 보정 흐름을 별도 flow 또는 schema 후보로 둘지 검토한다.
- OHLC 4방위 끝점과 WAXF / AWXF / 113 흐름연산식을 어떻게 분리 연결할지 검토한다.
- 캔들 orbit trace를 금융 차트 분석으로 오해하지 않도록 boundary note를 둘지 검토한다.
- candle structure를 Structure_Principle의 renderer candidate 또는 data-structure case로 둘지 검토한다.

## 16. one_line

schema.112.candle_subobject_orbit_structure의 candle_subobject_orbit_structure.metaplus.md는 하나의 캔들을 단일 막대가 아니라 parent-field 안의 하위 움직임 orbit trace들의 합으로 보고, 그 결과로 드러난 OpenㆍHighㆍLowㆍClose를 4방위 끝점으로 정의하며, 111의 각도 해상도 격자와 113의 OHLC 흐름연산식 사이에서 캔들의 구조적 대상 정의를 담당하는 흐름을 보존하는 대화정리형 이해 로그다.

## 17. shortest

candle_subobject_orbit_structure.metaplus.md =
schema.112_candle_subobject_orbit_structure 대화정리 /
111이후 /
캔들=하위움직임들의합 /
캔들=parent_field /
하위움직임=orbit_trace /
OHLC=4방위끝점 /
1시간봉=parent_field /
60개1분봉=subobject_motions /
112=캔들구조적대상정의 /
113=캔들흐름연산식정의