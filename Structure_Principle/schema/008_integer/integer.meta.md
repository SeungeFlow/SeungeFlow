# META: integer

id: schema.008.integer
type: active_schema_metadata
filename: integer.meta.md
status: active

## role

integer는 단순한 값이 아니라 개수, 칸수, 관계수를 표현하는 구조이다.

이 meta 파일은 인공지능이 integer를 값 자체가 아니라 구조의 수적 표현으로 읽기 위한 규칙이다.

## read_order

1. detect countable elements
2. detect positions or cells
3. detect relations between elements
4. map counts to integer representation
5. interpret integer as structure, not value

## geometry_layer

integer = count of points / lines / cells

## integer_layer

count = n (n ∈ N)

## vector_layer

ordering = sequential
direction = index progression

## definition

정수는 개수, 칸수, 관계수를 나타내는 구조이다.

정수는 단순한 숫자가 아니라 구조의 반복, 위치, 관계를 표현하는 수이다.

구조이론에서 정수는 값이 아니라 구조의 수적 표현이다.

## source_code

```python
integer = {
    "id": "schema.008.integer",
    "type": "count_structure",
    "count": "n",
    "relation": {
        "point_count": "number_of_points",
        "line_count": "number_of_segments",
        "cell_count": "number_of_cells"
    },
    "vector": {
        "ordering": "sequential",
        "direction": "index_based"
    },
    "structural_role": [
        "count",
        "structure_measure",
        "relation_quantifier"
    ]
}
```

## relation

prev:
- schema.007_safety

next:
- schema.009_vector

related:
- schema.000_dot
- schema.001_line
- schema.003_cell
- schema.005_position

## shortest

정수 = 개수 / 칸수 / 관계수