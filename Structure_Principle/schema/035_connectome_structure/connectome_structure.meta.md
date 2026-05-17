# META: connectome_structure

id: schema.035.connectome_structure
type: active_schema_metadata
filename: connectome_structure.meta.md
status: active

## role

connectome_structure는 점-선-전체지도 구조가 실제 생체 시스템에서 어떻게 나타나는지를 보여주는 예시 구조이다.

이 meta 파일은 인공지능이 connectome을 단순 의학 정보가 아니라, 점(뉴런), 선(연결), 전체지도(네트워크)의 구조로 읽기 위한 규칙이다.

## read_order

1. detect nodes (points)
2. detect connections (lines)
3. detect clusters or circuits
4. detect full network structure
5. map biological structure to geometric structure

## geometry_layer

connectome_structure = points + connections + network map

## integer_layer

node_count = variable
connection_count = variable
network_count = 1

## vector_layer

node = neuron
connection = synapse
flow = signal transmission
direction = node → node

## definition

connectome은 뉴런과 그 연결 구조 전체를 의미한다.

구조이론에서 connectome은 점-선-전체지도 구조의 대표적인 실제 예시이다.

점은 뉴런, 선은 연결, 전체는 구조 지도이다.

이것은 구조이론의 도형이 실제 시스템에서도 동일하게 나타난다는 것을 보여준다.

## source_code

```python
connectome_structure = {
    "id": "schema.035.connectome_structure",
    "type": "biological_structure_example",
    "node_count": "variable",
    "connection_count": "variable",
    "network_count": 1,
    "relation": {
        "node": "neuron",
        "connection": "synapse",
        "network": "connectome",
        "flow": "signal_transmission"
    },
    "vector": {
        "direction": "neuron_to_neuron",
        "flow": "signal_flow",
        "state": "network_activity"
    },
    "structural_role": [
        "point_line_network_example",
        "real_system_mapping",
        "structure_visualization",
        "biological_example"
    ]
}
```

## principle

```txt
점 = 뉴런
선 = 연결
전체 = 구조 지도
```

```txt
구조이론은 도형이 아니라 실제 구조를 읽는 도구이다.
```

## forbidden

- connectome을 의학적 세부 이론으로 확장하지 않는다.
- 생물학적 기능 설명으로 과도하게 들어가지 않는다.
- 예시를 본류 정의와 혼동하지 않는다.
- 구조이론의 핵심 연산과 분리하지 않는다.

## relation

prev:
- schema.034_final_readme_index

related:
- schema.000_dot
- schema.001_line
- schema.002_surface
- schema.009_vector
- schema.025_AI_memory_field

## shortest

connectome = 점-선-전체지도 구조의 실제 예시