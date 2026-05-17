# META: structure_judgment

id: schema.014.structure_judgment
type: active_schema_metadata
filename: structure_judgment.meta.md
status: active

## role

structure_judgment는 구조가 성립하는지 판정하는 최종 구조이다.

이 meta 파일은 인공지능이 structure_judgment를 의미 해석이 아니라, 연산 후 복귀와 보존을 확인하는 판정 구조로 읽기 위한 규칙이다.

## read_order

1. detect difference
2. detect positions
3. detect swap operator
4. detect repeated operation
5. detect return condition
6. detect preservation condition
7. map result to structure judgment

## geometry_layer

structure_judgment = difference + swap + repetition + return + preservation

## integer_layer

operation_count = k
return_state = 1
preservation_state = 1
judgment_state = 1

## vector_layer

flow = difference → swap → repetition → return → preservation
direction = cyclic closure

## definition

구조판정은 차이를 자리교환 연산으로 처리한 뒤, 반복을 통해 복귀와 보존이 성립하는지를 확인하는 것이다.

구조이론에서 구조는 의미로 먼저 판정하지 않는다.

구조는 연산 후 복귀와 보존으로 판정한다.

## source_code

```python
structure_judgment = {
    "id": "schema.014.structure_judgment",
    "type": "final_structure_condition",
    "operation_count": "k",
    "relation": {
        "difference": "detected",
        "operator": "swap_T",
        "repetition": "T_power_k",
        "return_condition": "T^k_v == v",
        "preservation_condition": "sum(T^k_v) == sum(v)",
        "judgment": "structure_valid_if_return_and_preservation"
    },
    "vector": {
        "flow": [
            "difference",
            "swap",
            "repetition",
            "return",
            "preservation"
        ],
        "direction": "cyclic_closure"
    },
    "structural_role": [
        "final_judgment",
        "closure_check",
        "operator_based_structure_validation"
    ]
}
```

## formula

```txt
구조 = T^k
```

```txt
∃ k : T^k v = v
Σ(T^k v) = Σ(v)
```

## relation

prev:
- schema.013_return_preservation

related:
- schema.005_position
- schema.010_sequence_structure
- schema.011_swap
- schema.012_matrix_product
- schema.013_return_preservation

## shortest

구조 = T^k