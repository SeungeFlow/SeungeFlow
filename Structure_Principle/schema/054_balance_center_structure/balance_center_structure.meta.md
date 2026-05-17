id: schema.054.balance_center_structure
type: active_schema_metadata
filename: balance_center_structure.meta.md
status: active

# META: balance_center_structure

## role

balance_center_structure는 중심을 단순 평균값이나 기하학적 가운데가 아니라, 여러 목적칸 사이에서 역할·무게·방향·조건을 조정하며 이동 가능한 균형 중심으로 읽는 구조이다.

이 meta 파일은 인공지능이 중심을 average로 고정하지 않고, balance로 판정하기 위한 규칙이다.

## read_order

1. detect goal center
2. detect purpose cells
3. detect dual-purpose tension
4. distinguish average from balance
5. detect role weight
6. detect movable center
7. map balance center to structural goal

## geometry_layer

balance_center_structure = purpose cell + movable goal center + purpose cell

## integer_layer

purpose_count = 2
goal_center_count = 1
movement_step = 1
balance_state_count = variable

## vector_layer

purpose_A → goal_center
purpose_B → goal_center
goal_center → purpose_A
goal_center → purpose_B

## definition

목표는 하나이고 목적은 여러 방향을 가진다.

두 개의 목적이 있을 때 구조는 다음처럼 놓인다.

```txt
목적칸 A
→ 목표칸
← 목적칸 B
```

목적칸은 다른 목적칸으로 직접 이동하지 않는다.

목적칸은 반드시 목표칸을 통과해야 다른 목적칸과 연결된다.

따라서 목표칸은 단순 가운데가 아니라, 두 목적을 이어주는 통과 중심칸이다.

이 중심은 average가 아니라 balance이다.

## average_balance_distinction

```txt
average = 같은 비율로 나눈 중심값
balance = 역할·무게·방향·조건을 고려한 균형 중심값
```

```txt
average = 공평에 가까움
balance = 형평에 가까움
```

average는 수치상 가운데값이다.

balance는 구조가 유지되도록 중심을 조정하는 값이다.

따라서 balance center는 고정된 중앙값이 아니라, 조건에 따라 한 칸씩 이동 가능한 중심칸이다.

## instrument_analogy

드럼과 피아노는 무조건 앉아서 연주해야 하는 대표적 악기이다.

이유는 손뿐 아니라 발도 사용하기 때문이다.

```txt
손 = 표면 작동
발 = 하부 지지 / 리듬 / 페달 / 중심 조절
```

드럼은 손으로 타격하고 발로 킥과 하이햇을 조절한다.

피아노는 손으로 선율과 화성을 만들고 발로 페달과 울림을 조절한다.

두 악기의 목표는 하나이다.

```txt
다른 악기들과 평형을 맞추는 것
```

즉 balance는 각 악기의 역할, 소리의 밀도, 리듬의 위치, 진입 타이밍, 지속 시간에 따라 이동하는 중심이다.

## source_code

```python
balance_center_structure = {
    "id": "schema.054.balance_center_structure",
    "type": "movable_balance_center_structure",
    "relation": {
        "goal": "movable_balance_center",
        "purpose_A": "one_directional_purpose_cell",
        "purpose_B": "another_directional_purpose_cell",
        "average": "equal_ratio_center",
        "balance": "role_weight_condition_adjusted_center"
    },
    "flow": [
        "purpose_A",
        "goal_center",
        "purpose_B"
    ],
    "movement_rule": {
        "purpose_to_purpose": "must_pass_through_goal",
        "goal_to_purpose": "movable_to_either_side",
        "center_step": "one_cell_at_a_time"
    },
    "distinction": {
        "average": "same_ratio_fairness",
        "balance": "conditional_equity"
    },
    "structural_role": [
        "goal_center",
        "purpose_relation",
        "balance_judgment",
        "movable_center",
        "anti_average_reduction"
    ]
}
```

## principle

```txt
목표는 하나
목적은 여러 방향
```

```txt
목적 A → 목표 ← 목적 B
```

```txt
목적은 서로 직접 만나지 않는다.
목표에서 만난다.
```

```txt
목표 = 통과 중심칸
목적 = 방향 끝점
```

```txt
average는 가운데값이고,
balance는 역할을 살리는 중심값이다.
```

## renderer_hint

balance_center_structure는 SVG에서 단순 중앙점으로 표시하지 않는다.

목표칸은 두 목적 사이에서 고정된 정중앙이 아니라, 조건에 따라 이동 가능한 balance center로 표시해야 한다.

```txt
purpose_A
→ movable_goal_center
← purpose_B
```

## forbidden

- 중심을 항상 수학적 평균으로 고정하지 않는다.
- average와 balance를 같은 것으로 보지 않는다.
- 공평과 형평을 혼동하지 않는다.
- 목적칸끼리 직접 연결하지 않는다.
- 목표칸을 단순 가운데 칸으로 축소하지 않는다.
- balance center의 이동 가능성을 제거하지 않는다.
- 드럼/피아노 비유를 감상적 설명으로만 처리하지 않는다.

## relation

prev:
- schema.053_structure_principle_flow

related:
- schema.000_dot
- schema.005_position
- schema.009_vector
- schema.013_return_preservation
- schema.019_center_point
- schema.025_AI_memory_field
- schema.053_structure_principle_flow

## renderer_hint_short

movable goal center between two purpose cells

## shortest

average = 가운데값 / balance = 역할을 살리는 중심값