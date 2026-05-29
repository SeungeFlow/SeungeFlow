# thinking_flow_relation_020.md

> 기준 원본: `thinking_flow_020.md`  
> 생성일: 2026-05-29  
> 성격: `thinking_flow_020.md`의 Seed들이 `Structure_Principle/schema/` 흐름 중 어디에 연결되는지 표시하는 relation map

---

## 0. 문서 목적

이 문서는 `thinking_flow_020.md`를 대체하지 않는다.

`thinking_flow_020.md`는 `thinking_flow_019.md` 이후의 흐름을 확장하여, Candle of CFD, OHLC state-square, 차트의 역방향 reading, 사카타5법칙, 120이평선, MetaTrader-Linux BackTesting Loop, 그리고 두 목표 field를 함께 정렬한 pre-meta source flow이다.

이 relation 문서의 목적은 다음이다.

```text
thinking_flow_020.md
→ Seed 추출
→ Structure_Principle/schema/의 구조발생 흐름과 연결
→ 두 목표 field에 필요한 meta.md / guide 분리 전 relation 확인
```

---

## 1. 전체 relation 요약

```text
thinking_flow_020
=
thinking_flow_019 확장
+
OHLC state-square
+
same-state vectorizing
+
3D space / 2D sight
+
24 clock / 24 compass / 24 solar terms
+
critical_between_area_9_to_0
+
reverse chart reading
+
MetaTrader-Linux backtesting loop
+
dual-vector rhombus grid
+
pre_meta_source_flow
```

강한 schema 연결축은 다음이다.

```text
000_dot
001_line
002_surface
003_cell
004_boundary
005_position
006_entity
008_integer
009_vector
010_sequence_structure
011_swap
012_matrix_product
013_return_preservation
014_structure_judgment
050_hunminjeongeum_vector_operation
099_document_sorting_index
100_empty_position
101_three_dot_reading_mode_structure
```

---

## 2. Seed별 relation map

| thinking_flow_020 Seed | 연결 schema | relation 판정 |
|---|---|---|
| 목표 2개: 소호사.향사 / CFD OHLC | 099_document_sorting_index / 014_structure_judgment | source field를 목표별로 분리해야 함 |
| GitHub Tree와 PC Branch | 099_document_sorting_index / 005_position | GitHub는 selected visible coordinate, PC Branch는 full candidate field |
| 된장 항아리와 유기체 | 006_entity / 003_cell / 004_boundary | organism field / nested entity |
| 마름모 구조수열과 Candle of CFD | 002_surface / 010_sequence_structure / 101_three_dot_reading_mode_structure | chart는 마름모 구조의 1/4 단방향 절단면 |
| 산을 오르고 내리는 인지 | 002_surface / 004_boundary / 101_three_dot_reading_mode_structure | filled triangle / empty triangle perception |
| 3D 공간과 2D 시야 | 002_surface / 005_position / 101_three_dot_reading_mode_structure | 3D 움직임을 2D 평면으로 인식하는 투영 |
| 좌표 / 시계 / 방위 | 008_integer / 009_vector / 012_matrix_product | time/place/flow/vector의 분리 필요 |
| 24시계 / 24방위도 / 24절기 | 008_integer / 010_sequence_structure / 009_vector | 하나의 원 분할 방식이지만 대상이 다름 |
| 남향과 place.state | 005_position / 009_vector | place.state + sunlight vector.state + seasonal time.state |
| Open.Price.Place.State | 000_dot / 005_position / 001_line | Open.State=(0,0), 첫 시작점 |
| OHLC state-square | 003_cell / 005_position / 011_swap / 012_matrix_product | 2×2 state-square, 대각 relation |
| Price.State vs Price.value | 006_entity / 014_structure_judgment | value가 아니라 state를 먼저 판정 |
| 직전 3개의 같은 Price.State vectorizing | 009_vector / 010_sequence_structure | 같은 state끼리 3점 이상으로 vectorizing |
| time.state = 때(時) = Capture | 003_cell / 010_sequence_structure | formed/forming candle 구분 |
| 9ㆍ0와 Candle 생성 | 010_sequence_structure / 013_return_preservation | Close→dot→next Open |
| 9ㆍ0의 실체와 0의 위치 | 004_boundary / 005_position / 100_empty_position | 0은 경계바깥지점이자 다음 구조장 시작점 |
| 임계사이영역 | 004_boundary / 010_sequence_structure | 9에서 0 사이 모든 세분 구간 |
| 시간 흐름과 역방향 reading | 013_return_preservation / 101_three_dot_reading_mode_structure | time.flow는 후진하지 않지만 reading.direction은 뒤집을 수 있음 |
| 흐르는 시간 속의 대칭 | 010_sequence_structure / 011_swap / 013_return_preservation | 고점/저점은 9ㆍ0 전이 지점 |
| 사카타5법칙과 120이평선 | 008_integer / 014_structure_judgment | 평균장과 공(empty transition place) |
| MetaTrader-Linux BackTesting Loop | 012_matrix_product / 013_return_preservation / 014_structure_judgment | source-processing-backtesting-execution loop |
| dual-vector rhombus grid | 009_vector / 101_three_dot_reading_mode_structure | Candle이 생길 수 있는 자리와 관계를 펼친 장 |
| C=tp, F=ma, E=mc² 재확인 | 005_position / 014_structure_judgment | 변하지 않는 기준항과 전이항 구분 |
| 왼쪽 / 내부 / 포함장 | 004_boundary / 005_position / 006_entity | left as containing field 후보 |

---

## 3. OHLC state-square relation

`thinking_flow_020.md`에서 가장 중요한 추가 구조는 OHLC state-square이다.

```text
Open.State  = (0,0)
Close.State = (1,1)
High.State  = (0,1)
Low.State   = (1,0)
```

이를 사각 구조로 놓으면 다음이다.

```text
High(0,1)      Close(1,1)

Open(0,0)      Low(1,0)
```

relation 판정:

```text
Open → Close
=
주대각선

High ↔ Low
=
반대대각선

OHLC
≠
value bundle

OHLC
=
state-square
```

연결 schema:

```text
003_cell
005_position
011_swap
012_matrix_product
014_structure_judgment
```

---

## 4. same-state vectorizing relation

같은 state끼리 직전 3개를 모아야 vectorizing 가능성이 열린다.

```text
Open[-3]  → Open[-2]  → Open[-1]
High[-3]  → High[-2]  → High[-1]
Low[-3]   → Low[-2]   → Low[-1]
Close[-3] → Close[-2] → Close[-1]
```

중요한 guard:

```text
Open.State
≠
High.State
≠
Low.State
≠
Close.State
```

따라서 Open/High/Low/Close를 하나의 price.value 계열로 병합하면 안 된다.

연결 schema:

```text
009_vector
010_sequence_structure
014_structure_judgment
```

---

## 5. critical_between_area_9_to_0 relation

`thinking_flow_020.md`는 `9ㆍ0`를 Candle 생성 흐름으로 다시 정렬한다.

```text
9
=
이전 Candle의 닫힘 직전 / 극한상태

ㆍ
=
임계사이영역
=
닫힘과 다음 열림 사이

0
=
다음 Candle의 Open.State
```

즉:

```text
Close.State
→ 임계사이영역
→ next Open.State
```

연결 schema:

```text
004_boundary
010_sequence_structure
013_return_preservation
100_empty_position
```

---

## 6. reverse reading axis relation

time.flow는 후진하지 않는다.

```text
time.flow
=
과거 → 현재 → 다음
```

하지만 reading.direction은 뒤집을 수 있다.

```text
reading.direction
=
과거 → 현재
또는
현재 → 과거
```

이는 `101_three_dot_reading_mode_structure`와 강하게 연결된다.

```text
same object
+
different reading axis
=
different structural interpretation
```

연결 schema:

```text
101_three_dot_reading_mode_structure
013_return_preservation
014_structure_judgment
```

---

## 7. MetaTrader-Linux BackTesting Loop relation

`thinking_flow_020.md`는 TradingView를 경유하던 구조와 MetaTrader-Linux 구조를 비교한다.

```text
TradingView
→ 1차 가공
→ AI 확인
→ Local Linux Server 또는 Oracle Free Server
→ 2차 가공
→ Trading Program
→ 진입 / 청산
```

MetaTrader는 OHLC source에 더 직접 접근한다.

```text
MetaTrader
=
OHLC source 접근
+
BackTesting
+
전략 실행
+
진입 / 청산
```

relation 판정:

```text
MetaTrader ↔ Linux Server
=
processing loop
```

연결 schema:

```text
012_matrix_product
013_return_preservation
014_structure_judgment
```

이 흐름은 이후 L7OS / QnA OS / Linux log feedback 구조와도 연결 가능하다.

---

## 8. dual-vector rhombus grid relation

승이가 만든 차트는 단순 그림이 아니다.

```text
Candle이 움직이는 그림
```

이라기보다:

```text
Candle이 생길 수 있는 자리와 관계를 펼쳐 놓은 장
```

이다.

핵심 요소:

```text
점의 위치
대각선
사각 boundary
중앙 전이축
좌우 prime 대칭
상승 / 하강 vector relation
```

연결 schema:

```text
009_vector
010_sequence_structure
101_three_dot_reading_mode_structure
```

---

## 9. 두 목표 field relation

`thinking_flow_020.md`는 두 목표를 명시한다.

```text
Goal 1:
소호사.향사 / 왕족 지파의 전통제례와 역사인식

Goal 2:
자본시장 CFD OHLC 분석
```

relation 판정:

```text
Goal 1
=
족보 / 제례 / 계 / 항렬 / 관계 field

Goal 2
=
Candle / OHLC / Price.State / Time.State / BackTesting field
```

두 목표는 표면적으로 다르지만, 공통적으로 다음을 요구한다.

```text
place.state
+
time.state
+
relation
+
sequence
+
boundary
+
state judgment
```

연결 schema:

```text
005_position
010_sequence_structure
014_structure_judgment
099_document_sorting_index
```

---

## 10. meta.md 후보 Seed

`thinking_flow_020.md` 원본은 다음 meta.md 후보를 제시한다.

```text
candle_of_cfd.meta.md
open_price_place_state.meta.md
ohlc_state_square.meta.md
price_state_not_price_value.meta.md
chart_as_one_direction_slice_of_rhombus_structure.meta.md
filled_triangle_empty_triangle_perception.meta.md
reverse_reading_axis_for_chart.meta.md
time_flow_irreversible_but_reading_reversible.meta.md
flowing_time_symmetry_high_low.meta.md
sakata_empty_space_candle_gap.meta.md
moving_average_120_as_average_axis.meta.md
metatrader_linux_backtesting_loop.meta.md
direct_ohlc_access_trading_field.meta.md
critical_between_area_9_to_0.meta.md
nine_limit_before_zero_transition.meta.md
twenty_four_clock_time_state.meta.md
twenty_four_direction_place_vector_state.meta.md
seasonal_clock_24_solar_terms.meta.md
time_place_flow_vector_unified_clock.meta.md
jwahyang_place_vector_state.meta.md
time_state_inside_vector_state.meta.md
ctp_flow_vector_time_place_state.meta.md
dual_vector_rhombus_grid.meta.md
```

relation 판단상 우선순위는 다음이다.

```text
1순위:
ohlc_state_square.meta.md
open_price_place_state.meta.md
price_state_not_price_value.meta.md
critical_between_area_9_to_0.meta.md
time_flow_irreversible_but_reading_reversible.meta.md

2순위:
reverse_reading_axis_for_chart.meta.md
same_state_vectorizing.meta.md
metatrader_linux_backtesting_loop.meta.md
direct_ohlc_access_trading_field.meta.md
dual_vector_rhombus_grid.meta.md

3순위:
twenty_four_clock_time_state.meta.md
twenty_four_direction_place_vector_state.meta.md
seasonal_clock_24_solar_terms.meta.md
jwahyang_place_vector_state.meta.md
```

---

## 11. guard

```text
1. OHLC를 value bundle로 읽지 않는다. OHLC는 state-square이다.
2. Open/High/Low/Close를 같은 state로 병합하지 않는다.
3. Price.value보다 Price.State가 먼저다.
4. time.flow와 reading.direction을 혼동하지 않는다.
5. 9ㆍ0의 dot은 숫자항이 아니라 임계사이영역이다.
6. MetaTrader-Linux loop를 단순 trading implementation으로만 읽지 않는다.
7. 두 목표 field를 표면 주제 차이로 분리만 하지 말고, place/time/relation/sequence 공통구조를 본다.
8. 이 문서는 meta.md가 아니라 relation map이다.
```

---

## 12. shortest

```text
thinking_flow_relation_020.md는
thinking_flow_020.md의 OHLC state-square, Open.Price.Place.State, Price.State, 24시계, 24방위도, 24절기, 좌향, Time.State, Vector.State, 9ㆍ0 임계사이영역, 역방향 reading, 사카타5법칙, 120이평선, MetaTrader-Linux BackTesting Loop, dual-vector rhombus grid가 Structure_Principle/schema의 dot, line, surface, cell, boundary, position, entity, integer, vector, sequence, swap, matrix, return, judgment, three-dot reading mode와 어떻게 연결되는지 표시하는 relation map이다.
```

---

## Appendix. 원본 기준

이 relation 문서는 다음 원본 파일을 기준으로 작성되었다.

```text
thinking_flow_020.md
```
