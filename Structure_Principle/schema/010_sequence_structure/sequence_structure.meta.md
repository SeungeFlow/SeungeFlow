# META: sequence_structure

id: schema.010.sequence_structure
type: active_schema_metadata
filename: sequence_structure.meta.md
status: active

## role

sequence_structure는 값이 아니라 자리의 반복 관계를 표시하는 수열 구조이다.

이 meta 파일은 인공지능이 sequence_structure를 숫자의 나열이 아니라, 자리·칸수·반복·방향이 결합된 구조로 읽기 위한 규칙이다.

## read_order

1. detect ordered positions
2. detect repeated relation
3. detect integer index
4. detect direction of progression
5. detect return or continuation condition
6. map ordered positions to sequence structure

## geometry_layer

sequence_structure = ordered positions + repeated relation

## integer_layer

index = n
position_count = variable
step_count = variable

## vector_layer

direction = position_n → position_n+1
flow = sequential

## definition

수열구조는 값의 나열이 아니라 자리의 반복 관계이다.

수열구조에서 중요한 것은 각 값 자체가 아니라, 값이 놓인 자리와 다음 자리로 이어지는 규칙이다.

구조이론에서 수열구조는 칸수, 방향, 반복, 복귀 조건을 함께 가진다.

## source_code

```python
sequence_structure = {
    "id": "schema.010.sequence_structure",
    "type": "ordered_position_structure",
    "index": "n",
    "position_count": "variable",
    "step_count": "variable",
    "relation": {
        "current": "position_n",
        "next": "position_n_plus_1",
        "rule": "repeated_relation"
    },
    "vector": {
        "direction": "position_n_to_position_n_plus_1",
        "flow": "sequential"
    },
    "structural_role": [
        "ordered_positions",
        "repetition",
        "sequence_flow",
        "return_candidate"
    ]
}
```

## relation

prev:
- schema.009_vector

next:
- schema.011_swap

related:
- schema.005_position
- schema.008_integer
- schema.013_return_preservation
- schema.014_structure_judgment

## shortest

수열구조 = 반복되는 자리 관계