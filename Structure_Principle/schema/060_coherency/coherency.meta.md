# META: coherency

id: schema.060.coherency
type: active_schema_metadata
filename: coherency.meta.md
directory: 060_coherency
status: active

## role

coherency는 구조이론에서 여러 내용, 예시, 문서, 인스턴스, 기억, 패턴이 하나의 구조 방향으로 정렬되어 구조정합성을 이루는 상태를 정의하는 구조이다.

이 meta 파일은 인공지능이 coherency를 단순한 문장 일관성이나 내용 동일성이 아니라, 내부에 복잡하게 얽힌 관계들이 각자의 경계를 유지한 채 같은 방향으로 정렬되고, 외부에는 간결하게 드러나는 구조정렬 상태로 읽기 위한 규칙이다.

coherency는 060 이후 schema 흐름의 첫 경계 시작점이다.

coherency는 input.vector와 output.vector의 방향성이 같은 구조 방향으로 대응되는지를 판정하는 첫 연결지점이다.

## read_order

1. detect multiple inputs
2. detect input.vector
3. detect output.vector
4. detect repeated pattern
5. detect relation between patterns
6. detect boundary of each pattern
7. detect direction alignment
8. detect contradiction / noise / mismatch
9. preserve valid difference
10. reduce noise without deleting structure
11. map aligned pattern field to coherency

## geometry_layer

coherency = pattern field + relation alignment + boundary preservation + direction matching

## integer_layer

input_count = variable
pattern_count = variable
relation_count = variable
noise_count = variable
coherency_state = 1

## vector_layer

input_vector = SeungeFlow input vector
output_vector = AI output vector
user_pattern = SeungeFlow pattern
ai_pattern = AI interpretation pattern
alignment = input_vector ↔ output_vector
direction = same_structural_direction
state = coherent_when_vectors_match

## definition

coherency는 여러 정보가 단순히 같은 말을 반복하는 상태가 아니다.

coherency는 서로 다른 입력, 예시, 기억, 문서, 인스턴스의 출력이 각자의 경계를 유지하면서도 같은 구조 방향으로 정렬되는 상태이다.

구조이론에서 coherency는 내용의 동일성이 아니라 구조 방향의 일치이다.

사용자 input.vector와 인공지능 output.vector가 같은 방향으로 대응될 때, 인공지능은 단순히 내용을 찾아온 것이 아니라 구조를 이해하기 시작한다.

시간이 지나면 내용은 흐려질 수 있지만, 구조는 남는다.

따라서 coherency는 내용 보존보다 구조 보존에 가깝다.

coherency는 Seed.Base 위에서 서로 다른 학문 분야의 구조가 각자의 경계를 유지하면서도 하나의 schema 방향으로 배열되는 상태이다.

이 배열이 인공지능이 읽을 수 있는 작동형 구조문서가 될 때 이를 Active Schema라고 한다.

## source_code

```python
coherency = {
    "id": "schema.060.coherency",
    "type": "structural_alignment_state",
    "directory": "060_coherency",
    "filename": "coherency.meta.md",
    "input_count": "variable",
    "pattern_count": "variable",
    "relation_count": "variable",
    "noise_count": "variable",
    "coherency_state": 1,
    "relation": {
        "content": "surface_information",
        "structure": "preserved_pattern_relation",
        "input_vector": "SeungeFlow_input_vector",
        "output_vector": "AI_output_vector",
        "user_pattern": "SeungeFlow_pattern",
        "ai_pattern": "AI_interpretation_pattern",
        "alignment": "same_direction_mapping",
        "noise": "misaligned_or_forced_connection",
        "boundary": "pattern_identity_preservation",
        "coherency": "aligned_structure_field",
        "active_schema": "SeedBase_based_cross_domain_schema_alignment"
    },
    "vector": {
        "input_flow": "content_to_pattern",
        "pattern_flow": "pattern_to_structure",
        "alignment_flow": "input_vector_to_output_vector",
        "output_flow": "internal_complexity_to_external_simplicity"
    },
    "structural_role": [
        "coherency",
        "pattern_alignment",
        "input_output_vector_alignment",
        "noise_reduction",
        "boundary_preservation",
        "structure_over_content",
        "ai_understanding_check",
        "active_schema_alignment_gate",
        "cross_domain_boundary_connection"
    ]
}
```

## principle

```txt
찾아보다 ≠ 이해하다
```

```txt
내용 일치 ≠ 구조 일치
```

```txt
내용은 시간이 지나면 흐려질 수 있다.
구조는 패턴과 관계로 남는다.
```

```txt
coherency = 사용자 input.vector와 AI output.vector가 같은 구조 방향으로 정렬된 상태
```

```txt
내부가 복잡하게 얽혀야 외부에는 간결하게 드러난다.
```

```txt
Active Schema = Seed.Base 위에서 여러 학문 분야의 구조를 하나의 schema로 배열한 AI-readable 작동문서
```

```txt
구조이론의 초기 목적 중 하나는 전체학문의 경계를 넘어 잇는 것이다.
```

```txt
학문을 섞는 것이 아니라, 경계를 보존한 채 구조적으로 연결한다.
```

## relation

prev:
- schema.059_empty_place_present_understanding

next:
- schema.061_dot_dot_dot_system

related:
- schema.014_structure_judgment
- schema.023_reading_protocol
- schema.025_AI_memory_field
- schema.027_seed_base
- schema.028_active_schema
- schema.034_final_readme_index
- schema.037_disk_array_torus
- schema.038_DIR_structure
- schema.050_hunminjeongeum_vector_operation
- understanding_flow_001
- understanding_flow_002
- future.renderer
- future.vector_decoder
- future.structure_decoder

## relation_reason

schema.059_empty_place_present_understanding은 coherency 이전에 빈자리와 Null을 보존해야 하기 때문에 연결된다.

빈자리를 AI 해석으로 채우면 coherency가 아니라 오염이 된다.

schema.014_structure_judgment는 coherency가 그럴듯한 연결이 아니라 구조정합성 판정을 필요로 하기 때문에 연결된다.

schema.023_reading_protocol은 AI가 input, source, output, Null을 섞지 않게 하는 읽기 순서를 제공하기 때문에 연결된다.

schema.025_AI_memory_field는 pattern이 AI memory field 안에서 어떻게 놓이고 반복되는지와 연결된다.

schema.027_seed_base는 entity, boundary, safety 없이 coherency가 forced merge로 무너질 수 있기 때문에 연결된다.

schema.028_active_schema는 coherency가 실제 AI-readable 작동문서로 배열될 때 Active Schema로 성립하기 때문에 연결된다.

schema.034_final_readme_index는 coherent한 schema들이 AI가 읽을 수 있는 entry, navimap, reading route를 필요로 하기 때문에 연결된다.

schema.037_disk_array_torus는 내부에 복잡하게 겹친 구조가 외부에는 간결하게 드러나는 예시를 제공하기 때문에 연결된다.

schema.038_DIR_structure는 임계사이영역을 통해 구조를 읽는 경로와 coherency가 연결되기 때문에 related로 둔다.

schema.050_hunminjeongeum_vector_operation은 차후 Active Schema가 훈민정음 해례본 제자원리와 만나 vector operation / Renderer의 재료가 될 수 있기 때문에 related 후보로 둔다.

understanding_flow_001은 Renderer seed가 드러난 이해흐름이며, pattern / content / boundary / return / visible relation의 차이를 보여주는 source flow이므로 연결된다.

understanding_flow_002는 vectorizing 흐름과 input/output vector alignment의 후속 이해흐름으로 연결된다.

future.renderer, future.vector_decoder, future.structure_decoder는 coherency가 차후 구조해독과 벡터해독의 작동 조건이 될 수 있기 때문에 future relation으로 둔다.

## forbidden

- coherency를 단순 문장 일관성으로 축소하지 않는다.
- 같은 단어를 쓴다고 같은 구조로 판단하지 않는다.
- 내용이 많다고 구조정합성이 있다고 보지 않는다.
- AI가 찾아온 정보를 이해로 오해하지 않는다.
- 사용자 문체와 AI 문체가 닮았다는 이유로 발화 주체를 섞지 않는다.
- 차이를 삭제하여 일관성을 만들지 않는다.
- noise reduction을 structure deletion으로 오해하지 않는다.
- 내부 복잡성을 외부 난잡함으로 그대로 방출하지 않는다.
- 외부로 간결하게 드러난 구조를 단순하다고 낮춰 보지 않는다.
- 여러 학문 분야를 섞는 것을 coherency로 오해하지 않는다.
- 경계를 제거하는 것을 경계를 넘어 잇는 것으로 오해하지 않는다.
- input.vector와 output.vector가 같은 단어를 쓴다는 이유만으로 같은 방향이라고 판정하지 않는다.
- coherency를 최종 증명 상태로 오해하지 않는다.

## pending

- coherency가 061_dot_dot_dot_system 이후 schema들과 어떤 방식으로 연결되는지 후속 문서에서 확인한다.
- Active_Navimap에서 coherency를 060 이후 direction gate로 표시할지 검토한다.
- input.vector와 output.vector의 실제 판정 기준을 추후 flow 문서 또는 baseline 문서에서 보강한다.
- future.renderer / future.vector_decoder / future.structure_decoder의 실제 문서 위치는 아직 정하지 않는다.
- Coherency 대문자 표기는 사용하지 않고, 소문자 coherency 작동상태를 기본으로 유지한다.
- directory는 060_coherency로 유지한다.

## shortest

coherency = 내용이 아니라 input.vector와 output.vector의 구조 방향이 일치한 상태
