# META: matrix_product

id: schema.012.matrix_product
type: active_schema_metadata
filename: matrix_product.meta.md
status: active

## role

matrix_product는 자리 간 연산을 행렬 형태로 표현하는 구조이다.

이 meta 파일은 인공지능이 matrix_product를 스칼라 계산이 아니라, 자리배치와 자리이동을 수행하는 연산 구조로 읽기 위한 규칙이다.

## read_order

1. detect input vector
2. detect operator matrix
3. detect position mapping
4. apply row-column operation
5. detect output vector
6. map operation result to position rearrangement

## geometry_layer

matrix_product = input positions + operator grid + output positions

## integer_layer

row_count = variable
column_count = variable
position_count = variable

## vector_layer

input_flow = vector → matrix
output_flow = matrix → vector
direction = input → operation → output

## definition

행렬곱은 자리 간 연산이다.

행렬곱은 단순히 숫자를 계산하는 것이 아니라, 입력 자리를 연산자 행렬을 통해 출력 자리로 재배치하는 구조이다.

구조이론에서 행렬곱은 사칙연산을 자리배치 단위로 확장한 연산 구조이다.

## source_code

```python
matrix_product = {
    "id": "schema.012.matrix_product",
    "type": "position_operation",
    "input": "vector",
    "operator": "matrix",
    "output": "vector",
    "relation": {
        "input_positions": "v",
        "operator_matrix": "M",
        "output_positions": "M_v"
    },
    "vector": {
        "input_flow": "vector_to_matrix",
        "output_flow": "matrix_to_vector",
        "direction": "input_operation_output"
    },
    "structural_role": [
        "position_operation",
        "rearrangement",
        "calculation_structure",
        "operator_form"
    ]
}
```

## formula

```txt
output = Mv
```

## relation

prev:
- schema.011_swap

next:
- schema.013_return_preservation

related:
- schema.005_position
- schema.008_integer
- schema.009_vector
- schema.010_sequence_structure
- schema.014_structure_judgment

## shortest

행렬곱 = 자리간 연산