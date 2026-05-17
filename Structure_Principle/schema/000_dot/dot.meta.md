# META: dot

id: schema.000.dot
type: active_schema_metadata
filename: dot.meta.md
status: active

## role

dot.png는 점의 구조를 표시하는 Active Schema image이다.

이 meta 파일은 인공지능이 dot.png를 구조적으로 읽기 위한 메타데이터이다.

## read_order

1. image first
2. detect central dot
3. detect integer count
4. detect vector origin
5. detect examples
6. map examples to structural function

## geometry_layer

dot = point

## integer_layer

point_count = 1

## vector_layer

origin = dot
direction = potential

## examples

- 마침표
- 소수점
- dot
- vector origin
- 훈민정음 천지인의 점

## structural_equivalence

위 예시들은 역사적 기원이 같다는 뜻이 아니다.

구조이론 안에서 모두 경계, 자리, 시작점으로 작동한다는 점에서 같은 구조기호로 읽는다.

## definition

점은 값이 아니라 자리이다.

점은 선, 벡터, 수열구조, 자리연산이 시작되는 최소 구조 단위이다.

## source_code

```python
dot = {
    "id": "schema.000.dot",
    "geometry": "point",
    "integer_count": 1,
    "vector_role": "origin",
    "direction": "potential",
    "structural_role": [
        "position",
        "boundary",
        "start"
    ],
    "examples": [
        "period_dot",
        "decimal_point",
        "dot",
        "vector_origin_dot",
        "hunminjeongeum_heaven_dot"
    ]
}
```

## relation

next:
- schema.001.line

related:
- schema.005.position
- schema.008_integer
- schema.009_vector

## shortest

점 = 최소 자리
