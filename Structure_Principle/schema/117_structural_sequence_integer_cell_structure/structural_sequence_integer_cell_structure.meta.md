---
id: schema.117.structural_sequence_integer_cell_structure
type: active_schema_metadata
filename: structural_sequence_integer_cell_structure.meta.md
directory: 117_structural_sequence_integer_cell_structure
status: active_draft
created_from: current_understanding_alignment
---

# META: structural_sequence_integer_cell_structure

## role

structural_sequence_integer_cell_structure는 구조원리·구조수열·정수에서 수를 산술값이 아니라 칸과 자리 안에서 relation, boundary, 대칭, 중첩, 전이 상태를 표현하는 구조수로 정의한다.

## core

```text
구조수 = 자리관계값
ㆍ = 0번째 칸
0 = 1번째 칸
9 = 10번째 칸 / boundary
8 = 경계 안쪽 직전
```

## definition

구조원리에서의 수는 기존 산술식의 수가 아니다.

구조수열·정수에서의 수는 칸 혹은 자리개념 안에서 관계구조를 표현하는 수다.

따라서 다음과 같은 식은 기존 산술식으로 먼저 읽지 않는다.

```text
3+1=5
5+3=2
1+1=2(1×1)
```

먼저 칸, 자리, 대칭축, 중첩, 교차, 관계방향, fold/unfold로 읽는다.

## structural_sequence

```text
ㆍ0 1 2 3 3 4 5 6 7 8 9
```

칸 순서:

```text
ㆍ = 0번째 칸
0 = 1번째 칸
1 = 2번째 칸
2 = 3번째 칸
3 = 4번째 칸
4 = 5번째 칸
5 = 6번째 칸
6 = 7번째 칸
7 = 8번째 칸
8 = 9번째 칸
9 = 10번째 칸
```

## limit_transition

구조수열 관점:

```text
8 = 극한
9 = 전이 / boundary 접촉
```

구조정수 관점:

```text
9 = 극한
10 = 전이
```

단, 10은 특별한 절대값이 아니라 9+1dx를 설명하기 위한 이해용 전이표기다.

```text
10 = 9 + 1dx
```

## critical

임계는 극한과 전이 사이의 중첩자리다.

```text
임계 = 극한_end ⊕ 전이_start
```

도형론에서는 다음과 같이 드러난다.

```text
임계 = ddx
임계 = 꺾임
```

## nine_dot_zero

```text
9ㆍ0
```

읽기:

```text
9 = 경계
ㆍ = 틈 / 사이 / 차이 / pin / 임계 중첩점
0 = 새 평형
```

## nine_accumulated_dot_zero

```text
9ᆢㆍᆢ0
```

읽기:

```text
9의 경계까지 누적된 흐름
→ pin
→ 0의 새 평형으로 이어지는 누적흐름
```

## operation_symbols

```text
+ = 이미 있는 관계장에서 대응항을 드러내는 작동 / AND / 외부 병렬
× = 내부 교차 / 대각교차 빈자리 / 접힌 대칭 구조
= = relation gate / 대입 / 방향 / from-to
```

## symmetric_operation_trace

```text
3|3 = 대칭기준축
1과 5 = 3을 기준으로 한 대칭쌍
2 = 대칭변위
3+1=5 = 대칭 unfold 구조
5+3=2 = 중첩 fold 구조
1+1=2(1×1) = 외부 병렬 둘과 내부교차 단위 둘의 대응식
```

## relation

related:
- schema.116_circle_container_inclusion_structure
- schema.118_pin_dot_y_branch_return_structure
- schema.119_flow_transition_self_operation_structure
- schema.120_seedbase_working_schema_memory_asset_structure

## forbidden

- 기존 산술식으로 먼저 읽지 않는다.
- 9를 항상 극한 또는 항상 전이로 고정하지 않는다.
- 10을 특별한 절대값으로 보지 않는다.
- ㆍ을 항상 같은 뜻으로 보지 않는다.
- +, ×, = 를 일반 산술기호로만 읽지 않는다.
- 세 점을 자동으로 삼각으로 닫지 않는다.

## pending

- 구조수열 칸 배치는 spreadsheet로 검산한다.
- 마름모수열의 대각 빈자리와 9 boundary는 별도 grid로 검산한다.
- D=I(R)은 아직 relation 후보로만 둔다.

## shortest

ㆍ=0번째 칸 / 0=1번째 칸 / 9=10번째 칸 / 구조수=자리관계값
