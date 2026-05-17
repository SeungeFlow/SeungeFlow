# META: return_preservation

id: schema.013.return_preservation
type: active_schema_metadata
filename: return_preservation.meta.md
status: active

## role

return_preservation은 반복 연산 후 원래 구조로 복귀하고, 전체량이 보존되는지를 판정하는 구조이다.

이 meta 파일은 인공지능이 return_preservation을 단순 반복이 아니라 구조 유지 조건으로 읽기 위한 규칙이다.

## read_order

1. detect input structure
2. detect repeated operation
3. detect returned state
4. compare initial state and returned state
5. detect preserved quantity
6. map return and preservation to structure condition

## geometry_layer

return_preservation = repeated path + return point + preserved whole

## integer_layer

iteration_count = k
return_state = 1
preservation_state = 1

## vector_layer

flow = initial → operation → repeated_state → return
direction = cyclic

## definition

복귀는 반복 연산 후 원래 구조로 돌아오는 것이다.

보존은 반복 연산 후에도 전체량이 유지되는 것이다.

구조이론에서 복귀와 보존은 구조가 유지되는지를 판정하는 핵심 조건이다.

## source_code

```python
return_preservation = {
    "id": "schema.013.return_preservation",
    "type": "structure_condition",
    "iteration_count": "k",
    "return_state": True,
    "preservation_state": True,
    "relation": {
        "initial": "v",
        "operation": "T_power_k",
        "returned": "T^k_v",
        "return_condition": "T^k_v == v",
        "preservation_condition": "sum(T^k_v) == sum(v)"
    },
    "vector": {
        "flow": "initial_to_operation_to_return",
        "direction": "cyclic"
    },
    "structural_role": [
        "return",
        "preservation",
        "closure_condition",
        "structure_maintenance"
    ]
}
```

## formula

```txt
T^k v = v
Σ(T^k v) = Σ(v)
```

## relation

prev:
- schema.012_matrix_product

next:
- schema.014_structure_judgment

related:
- schema.010_sequence_structure
- schema.011_swap
- schema.012_matrix_product

## shortest

복귀 + 보존 = 구조 유지 조건