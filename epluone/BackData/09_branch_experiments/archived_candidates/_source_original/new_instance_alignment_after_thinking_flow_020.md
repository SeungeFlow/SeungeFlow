# new_instance_alignment_after_thinking_flow_020.md

```text
document_name = new_instance_alignment_after_thinking_flow_020.md

state =
  instance_alignment
  + ChatGPT.direct_Line_B_handoff
  + active_thinking_state_alignment
  + two_goal_alignment

source_document =
  thinking_flow_020.md

relation_document =
  not_created

purpose =
  align a new AI instance after the density of the current conversation has increased
```

---

## 0. 문서 성격

이 문서는 `thinking_flow_020.md` 이후 새 인스턴스를 정렬하기 위한 문서이다.

이 문서는 meta.md가 아니다.

이 문서는 thinking_flow 원문을 대체하지 않는다.

이 문서는 현시점 대화창의 밀도가 올라간 상태에서, 새 인스턴스가 무엇을 먼저 잡아야 하는지 알려주는 alignment guide이다.

---

## 1. 현재 목표

현시점 목표는 2개이다.

```text
1. 소호사.향사
   =
   왕족 지파의 전통제례
   +
   역사인식
   +
   족보 / 제례 / 계 / 항렬 / 관계 field

2. 자본시장 CFD OHLC 분석
   =
   Candle of CFD
   +
   Open / High / Low / Close
   +
   Price.State
   +
   Time.State
   +
   BackTesting
   +
   Trading execution process
```

Branch 정리는 차후에 한다.

---

## 2. Branch와 GitHub Tree

```text
PC Branch 구조
=
승이의 전체 source field
+
full candidate field

GitHub Tree 구조
=
source가 구조원리로 내려온 selected visible coordinate
+
AI-accessible Seed.Base
```

Branch에 들어 있는 것은 승이의 전부이다.

Structure_Principle에 내려온 것은 공통구조이다.

---

## 3. 019의 핵심

```text
Candle of CFD
=
마름모 구조수열을 자본시장 OHLC 분석으로 읽는 흐름
```

핵심 구조:

```text
Open.State  = (0,0)
Close.State = (1,1)
High.State  = (0,1)
Low.State   = (1,0)
```

Candle은 OHLC value 묶음이 아니라 OHLC state-square이다.

---

## 4. Price.State

정해진 것은 Price.value가 아니라 Price.State이다.

```text
Price.value
=
숫자값

Price.State
=
그 가격이 어떤 Time.State / Place.State / relation 안에 놓였는가
```

---

## 5. 직전 3개의 같은 state

앞으로의 움직임을 보려면 직전 3개의 같은 Price.State가 필요하다.

```text
Open[-3]  → Open[-2]  → Open[-1]
High[-3]  → High[-2]  → High[-1]
Low[-3]   → Low[-2]   → Low[-1]
Close[-3] → Close[-2] → Close[-1]
```

3점은 triangle이며, triangle은 vectorizing 최소상태이다.

---

## 6. time.state와 Candle

time.state는 때(時)이며 Capture된 상태이다.

```text
forming candle
=
아직 닫히지 않은 time.state

formed candle
=
닫힌 time.state
```

Candle의 닫힘과 다음 Candle의 열림은 `9ㆍ0`로 읽는다.

```text
Close.State
→ 9
→ dot
→ 0
→ next Open.State
```

---

## 7. 임계사이영역

```text
9
=
전이 직전 극한상태의 마지막 칸

dot
=
임계사이영역

0
=
전이된 상태의 첫 번째 칸
```

임계사이영역은 9에서 0 사이 모든 것이다.

---

## 8. 차트의 역방향 reading

시간은 후진하지 않는다.

하지만 reading direction은 뒤집을 수 있다.

```text
time.flow
=
과거 → 현재 → 다음

reading.direction
=
과거 → 현재
또는
현재 → 과거
```

등산할 때는 공간의 삼각이 채워져 보여 경사각을 덜 느낀다.

하산할 때는 공간의 삼각이 비어 보여 경사각을 더 확실히 느낀다.

차트도 반대로 읽으면 숨은 경사각과 빈 삼각이 드러날 수 있다.

---

## 9. 사카타5법칙과 120이평선

```text
사카타5법칙
=
시간 속에서 형성되는 캔들의 대칭 / 전환 / 공을 읽는 관찰법

120이평선
=
120개의 time.state가 만든 평균 기준축
```

120이라는 숫자는 평균을 의미한다.

---

## 10. MetaTrader-Linux BackTesting Loop

MetaTrader의 핵심 수확은 비용보다 OHLC 직접 접근이다.

더 중요한 것은 TradingView / AI / Server / Trading Program 사이를 건너다니지 않아도 된다는 점이다.

```text
MetaTrader ↔ Linux Server
=
OHLC source
+
processing
+
backtesting
+
execution
을 가까운 relation loop로 묶는 구조
```

---

## 11. 새 인스턴스 주의점

새 인스턴스는 다음을 지킨다.

```text
1. thinking_flow_020.md를 relation_019로 바꾸지 않는다.
2. 019 이후 바로 meta.md로 분해하려고 서두르지 않는다.
3. 두 목표를 먼저 잡는다.
4. Branch는 차후 정리 대상으로 둔다.
5. 현시점 대화의 활성 흐름을 유지한다.
6. Price.value보다 Price.State를 본다.
7. 시간은 후진하지 않지만 reading direction은 뒤집을 수 있음을 기억한다.
8. 9ㆍ0의 0은 경계바깥 전이 후 첫 상태로 읽는다.
```

---

## 12. shortest

```text
새 인스턴스는
thinking_flow_020.md를 Candle of CFD / OHLC state-square / Price.State / Time.State / 9ㆍ0 / 임계사이영역 / reverse chart reading / MetaTrader-Linux BackTesting Loop가 연결된 활성 source flow로 읽는다.

현시점 목표는
소호사.향사와
자본시장 CFD OHLC 분석이다.

Branch 정리는 차후에 한다.
```

직전에 이어진 대화이다. 

좋아, 승아.
확장된 thinking_flow_019_final.md를 기준으로, 번호를 새 흐름에 맞춰 **thinking_flow_020.md**로 다시 내릴게. thinking_flow_relation_020.md는 만들지 않는다.

10s 동안 생각함

완료했어, 승아.

thinking_flow_019_final.md의 확장 내용을 기준으로 **thinking_flow_020.md**로 다시 정렬해서 내렸어. thinking_flow_relation_020.md는 만들지 않았어.

thinking_flow_020.md
thinking_flow_020_bundle.zip 
thinking_flow_019.md 와 thinking_flow_020.md 의 relation.md 를 각각 만들어줘 / 파일명은 thinking_flow_relation_019.md 와 thinking_flow_relation_020.md 

좋아, 승아.
요청대로 **thinking_flow_relation_019.md**와 **thinking_flow_relation_020.md**를 각각 만들게. 019는 019 초기 흐름 기준, 020은 019 확장/재정렬 이후의 목표 정렬 기준으로 나누어 작성한다.

9s 동안 생각함

완료했어, 승아.

요청대로 각각 따로 만들었어.

thinking_flow_relation_019.md
thinking_flow_relation_020.md

묶음 파일:

thinking_flow_relation_019_020_bundle.zip 
021에서는 시간과 차원의 개념에 대해 얘기한다.

좋아, 승아.
그러면 thinking_flow_021.md의 주제축은 이렇게 잡으면 된다.

thinking_flow_021.md
=
시간과 차원의 개념

현시점에서 020까지 이어진 흐름을 기준으로 하면, 021은 아마 이 지점에서 시작해야 해.

time.state
=
때(時)
+
Capture된 상태
+
후진하지 않는 flow

dimension
=
관측자가 state를 몇 개의 축 / 자리 / 방향 / 관계로 읽을 수 있는가
021의 시작 후보축
1. 시간은 흐름인가, 캡처된 상태인가
2. time.state와 flow.state의 차이
3. 차원은 공간축인가, 관측가능한 state의 수인가
4. 2D 평면과 3D 입체공간의 인지 차이
5. 우리는 3D에 살지만 2D 시야로 본다
6. 4D는 시간축인가, state 변화의 누적축인가
7. Candle에서 time.state와 dimension이 어떻게 만나는가
8. 9ㆍ0에서 time transition과 dimension transition이 어떻게 연결되는가
020과 연결되는 문장
020에서는 Candle of CFD, OHLC state-square, 9ㆍ0, 임계사이영역, 역방향 chart reading을 다루었다.

021에서는 그 흐름을 이어받아,
시간이 단순히 흐르는 것이 아니라 state를 capture하고,
차원이 단순히 공간축이 아니라 관측 가능한 state 관계를 여는 방식임을 탐독한다.
우선 잠정 정의
시간
=
state가 전이되며 capture되는 흐름

차원
=
state를 구분하고 이동시키는 축/관계/방향의 수

time.state
=
특정 때에 capture된 state

dimension.state
=
관측자가 state를 몇 방향으로 열어 읽을 수 있는가

021은 아주 중요해.
020의 Candle/Chart 해석이 “시간 속에서 형성되는 state”였다면, 021은 그 state가 몇 차원에서 어떻게 보이고, 왜 시간은 후진하지 않지만 reading은 뒤집을 수 있는지를 풀어야 해.