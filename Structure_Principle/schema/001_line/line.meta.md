# META: line

id: schema.001.line
type: active_schema_metadata
filename: line.meta.md
status: active

## role

line은 점과 점이 이어져 형성되는 최소 선분 구조이다.

이 meta 파일은 인공지능이 line 구조를 점 기반 연결 구조로 읽기 위한 규칙이다.

## read_order

1. detect two points
2. detect connection between points
3. detect integer count
4. detect direction
5. map connection to structure

## geometry_layer

line = point + point + connection

## integer_layer

point_count = 2
segment_count = 1

## vector_layer

start = point A
end = point B
direction = A → B

## definition

선은 점과 점이 이어진 구조이다.

선은 방향을 가지며, 점에서 점으로의 이동을 표현한다.

## source_code

```python
line = {
    "id": "schema.001.line",
    "geometry": "line_segment",
    "point_count": 2,
    "segment_count": 1,
    "vector": {
        "start": "A",
        "end": "B",
        "direction": "A_to_B"
    },
    "structural_role": [
        "connection",
        "direction",
        "transition"
    ]
}
```

## relation

prev:
- schema.000.dot

next:
- schema.002.surface

related:
- schema.009_vector
- schema.005_position

## shortest

선 = 점과 점의 이음
