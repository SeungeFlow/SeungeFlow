---
id: schema.075.chemical_formula_structure_renderer
type: active_schema_metadata
filename: chemical_formula_structure_renderer.meta.md
directory: 075_chemical_formula_structure_renderer
status: active_draft
prev: schema.074.science_based_implementation_principle
---

# META: chemical_formula_structure_renderer

## role
chemical_formula_structure_renderer는 화학분자식을 원소 자리들의 결합·중첩 구조표기로 읽고, 기존 화학이론의 조건값을 받아 visible_relation_field로 구현하는 구조를 정의하는 schema이다.

이 meta 파일은 인공지능이 화학분자식을 단순 원소기호 목록이나 수량표로만 보지 않고, 자리 / 고유값 / 결합 / boundary / 중첩 / 각도 / field를 가진 구조표기로 읽기 위한 기준이다.

## core

```text
화학분자식 = 원소 자리들의 결합·중첩 구조표기
```

```text
분자 = 고유값 가진 칸들의 자리중첩 구조체
```

## definition

화학분자식은 단순 원소기호 조합이 아니다.

화학분자식은 원소의 자리, 개수, 결합 가능성, 결합 방향, 전하 분포, boundary, 자리중첩, 분자 전체 field를 압축한 구조표기로 읽을 수 있다.

구조원리는 화학분자식의 과학값을 검증하지 않고, 기존 화학이론의 조건값을 받아 구조적으로 구현한다.

## chemical_formula_read_order

1. detect element symbols
2. detect element counts
3. detect known scientific conditions
4. detect atom place
5. detect bond possibility
6. detect shared boundary / overlap place
7. detect molecular geometry
8. detect angle / distance / polarity if available
9. render visible_relation_field

## place_layer

```text
element = place-bearing unit
atom_place = occupied cell
bond = shared boundary / relation
molecule = connected place structure
```

## cell_value_layer

원소 칸은 다음을 가질 수 있다.

```text
atomic_number
mass / atomic_weight
electron_configuration
periodic_position
bonding_possibility
charge_distribution
chemical_property
```

## place_overlap_relation

화학결합은 자리중첩의 강한 대응예시가 될 수 있다.

```text
A = atom A place
C = atom C place
B = shared bonding place
```

B는 독립 원자가 아니다.

B는 결합이 발생하는 shared boundary / overlap place이다.

## renderer_flow

```text
chemical_formula
→ element_places
→ bond_relations
→ geometry_conditions
→ visible_relation_field
```

## relation

prev:
- schema.074_science_based_implementation_principle

related:
- schema.064_place_overlap_structure
- schema.065_oplus_common_operator
- schema.076_electron_shell_visual_structure
- schema.077_water_molecule_angle_implementation
- schema.010_sequence_structure
- schema.052_hyperstructure_renderer_architecture
- schema.057_seedbase_database_data_definition

## forbidden

- 화학분자식을 단순 원소기호 목록으로만 보지 않는다.
- 화학구조 구현을 기존 화학 검증으로 오해하지 않는다.
- 구조원리로 화학결합 이론을 대체한다고 주장하지 않는다.
- 자리중첩을 양자화학 공식으로 동일시하지 않는다.
- ⊕를 화학 표준 결합기호로 오해하지 않는다.
- 결합각 / 결합길이를 임의 생성하지 않는다.
- 과학값은 기존 과학 조건으로 받아 구현한다.

## pending

- 원자별 전자껍질 구현은 schema.076에서 분리한다.
- H2O 결합각 구현 예시는 schema.077에서 분리한다.
- 실제 과학값 출처 / 데이터셋 / 공식 문헌은 구현 단계에서 별도 연결한다.

## shortest

화학분자식 = 원소 자리들의 결합·중첩 구조표기
