# META: scale_change

id: schema.022.scale_change
type: active_schema_metadata
filename: scale_change.meta.md
status: active

## role

scale_change는 같은 구조를 다른 칸수 기준으로 다시 읽는 운용 구조이다.

이 meta 파일은 인공지능이 scale_change를 단순 확대·축소가 아니라, 같은 영역 안에서 칸수와 값의 대응이 바뀌는 구조로 읽기 위한 규칙이다.

## read_order

1. detect fixed area
2. detect current cell division
3. detect changed cell division
4. compare cell count and value mapping
5. detect preserved structure
6. map scale change to cell-value reinterpretation

## geometry_layer

scale_change = fixed area + changed cell division

## integer_layer

area_count = 1
cell_count = variable
value_mapping = variable

## vector_layer

scale_in = coarse → fine
scale_out = fine → coarse
state = reinterpretation

## definition

스케일 변화는 같은 구조를 다른 칸수 기준으로 다시 읽는 것이다.

같은 영역 안에서 칸수를 더 잘게 나누면 값의 배치가 달라진다.

칸수를 고정하면 숫자값이 변하고, 숫자값을 고정하면 칸수값이 변한다.

구조이론에서 스케일 변화는 구조 자체의 변화가 아니라 칸수와 값의 대응 변화이다.

## source_code

```python
scale_change = {
    "id": "schema.022.scale_change",
    "type": "cell_value_reinterpretation",
    "area_count": 1,
    "cell_count": "variable",
    "value_mapping": "variable",
    "relation": {
        "fixed_area": True,
        "cell_count_fixed": "value_changes",
        "value_fixed": "cell_count_changes",
        "structure": "preserved",
        "mapping": "reinterpreted"
    },
    "vector": {
        "scale_in": "coarse_to_fine",
        "scale_out": "fine_to_coarse",
        "state": "reinterpretation"
    },
    "structural_role": [
        "scale",
        "cell_division",
        "value_mapping",
        "reinterpretation",
        "structure_preservation"
    ]
}
```

## relation

prev:
- schema.021_fold_unfold

next:
- schema.023_reading_protocol

related:
- schema.003_cell
- schema.005_position
- schema.008_integer
- schema.010_sequence_structure
- schema.012_matrix_product

## shortest

스케일 변화 = 칸수와 값의 대응 변화