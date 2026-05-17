# META: swap

id: schema.011.swap
type: active_schema_metadata
filename: swap.meta.md
status: active

## role

swap은 두 자리의 값을 서로 교환하는 최소 연산 구조이다.

이 meta 파일은 인공지능이 swap을 값의 변화가 아니라 자리 간 교환으로 읽기 위한 규칙이다.

## read_order

1. detect two positions
2. detect values assigned to positions
3. detect exchange operation
4. verify position swap
5. map exchange to swap operation

## geometry_layer

swap = position A ↔ position B

## integer_layer

position_count = 2
swap_count = 1

## vector_layer

direction = A → B and B → A
flow = bidirectional exchange

## definition

swap은 두 자리의 값을 서로 교환하는 연산이다.

swap은 값 자체를 변경하지 않고, 값이 놓인 자리를 바꾼다.

구조이론에서 swap은 모든 구조 변환의 최소 연산 단위이다.

## source_code

```python
swap = {
    "id": "schema.011.swap",
    "type": "position_exchange",
    "position_count": 2,
    "swap_count": 1,
    "relation": {
        "before": ["A", "B"],
        "after": ["B", "A"]
    },
    "vector": {
        "direction": ["A_to_B", "B_to_A"],
        "flow": "bidirectional"
    },
    "matrix": [
        [0, 1],
        [1, 0]
    ],
    "structural_role": [
        "position_exchange",
        "minimal_operation",
        "structure_transition"
    ]
}
```

## relation

prev:
- schema.010_sequence_structure

next:
- schema.012_matrix_product

related:
- schema.005_position
- schema.009_vector
- schema.014_structure_judgment

## shortest

swap = 자리교환