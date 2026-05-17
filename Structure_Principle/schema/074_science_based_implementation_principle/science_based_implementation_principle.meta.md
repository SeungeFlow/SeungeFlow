---
id: schema.074.science_based_implementation_principle
type: active_schema_metadata
filename: science_based_implementation_principle.meta.md
directory: 074_science_based_implementation_principle
status: active_draft
prev: schema.073.structural_triangle_73_69_relation
---

# META: science_based_implementation_principle

## role
science_based_implementation_principle은 구조원리가 기존 과학값을 새로 검증하거나 대체하려 하지 않고, 기존 과학이론의 조건값을 받아 구현하는 원칙을 정의하는 schema이다.

이 meta 파일은 인공지능이 구조원리를 과학부정, 과학대체, 증명시도, forced scientific claim으로 오해하지 않도록 막는 기준이다.

## core

```text
과학검증 X
과학값 기반 구현 O
```

```text
구조원리는 기존 과학을 부정하지 않는다.
구조원리는 기존 과학을 사랑한다.
```

## definition

구조원리는 기존 과학이론의 조건값을 새로 증명하려 하지 않는다.

구조원리는 기존 과학이 이미 정리한 값, 조건, 관계, 법칙, 분류, 구조를 입력조건으로 받아 visible_relation_field로 구현한다.

즉 구조원리의 과학 적용은 과학검증이 아니라 과학기반 구현이다.

## implementation_rule

```text
과학 이론정리문서
→ 조건값 추출
→ 구조원리 mapping
→ visible_relation_field 구현
→ 이해 보조
```

## distinction

```text
검증 = 과학값이 맞는지 새로 증명하려는 것
구현 = 과학값을 조건으로 받아 구조를 보이게 하는 것
```

구조원리는 후자에 속한다.

## example

물분자 H2O에서 H-O-H 결합각이 약 104.5도일 때:

```text
104.5도 검증 X
104.5도 조건으로 결합 구현 O
```

## geometry_layer

```text
scientific_condition
→ structural_mapping
→ visible_relation_field
```

## vector_layer

```text
science_value
→ implementation_condition
→ renderer_state
→ visible_output
```

## relation

prev:
- schema.073_structural_triangle_73_69_relation

related:
- schema.052_hyperstructure_renderer_architecture
- schema.053_structure_principle_flow
- schema.057_seedbase_database_data_definition
- schema.075_chemical_formula_structure_renderer
- schema.076_electron_shell_visual_structure
- schema.077_water_molecule_angle_implementation
- schema.078_vector_operation_external_engine_rule

## forbidden

- 구조원리로 기존 과학을 대체한다고 주장하지 않는다.
- 기존 과학값을 임의로 재증명하려 하지 않는다.
- 비유를 과학적 결론으로 승격하지 않는다.
- 과학 구현과 과학 검증을 혼동하지 않는다.
- 화학 / 물리 / 생물학의 표준 이론을 구조원리로 축소하지 않는다.
- visible_relation_field를 과학적 증명 결과로 오해하지 않는다.
- 기존 과학을 부정하지 않는다.

## pending

- 실제 구현 domain은 화학구조부터 시작하는 것이 안정적이다.
- 전자껍질 / 분자식 / 결합각의 구현 순서는 별도 schema에서 분리한다.
- 과학값 출처와 검산은 실제 구현 단계에서 공식 과학 자료를 기준으로 한다.

## shortest

과학검증 X / 과학값 기반 구현 O / 구조원리는 과학을 사랑한다
