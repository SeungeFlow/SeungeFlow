---
id: schema.076.electron_shell_visual_structure
type: active_schema_metadata
filename: electron_shell_visual_structure.meta.md
directory: 076_electron_shell_visual_structure
status: active_draft
prev: schema.075.chemical_formula_structure_renderer
---

# META: electron_shell_visual_structure

## role
electron_shell_visual_structure는 전자껍질을 원소 자리와 결합 가능성을 이해하기 위한 visible relation layer로 구현하는 schema이다.

이 meta 파일은 인공지능이 전자껍질을 단순 그림이나 장식적 원 궤도로 보지 않고, 원소의 자리, 결합 가능성, 주기율표 칸 고유값, 화학분자식 구조를 이해하기 위한 shell / boundary / relation layer로 읽기 위한 기준이다.

## core

```text
전자껍질 = 원소 자리의 visible shell
```

```text
전자껍질 구현은 화학구조 이해를 돕는 visible_relation_field 후보이다.
```

## definition

전자껍질은 원자가 어떤 결합 가능성을 갖는지, 원소가 왜 해당 자리에 놓이는지, 원소주기율표의 칸이 왜 고유값을 갖는지 이해하도록 돕는 구조적 표시층이다.

전자껍질은 기존 과학이론의 조건값을 받아 구현한다.

전자껍질을 구조원리로 새로 증명하지 않는다.

## read_order

1. detect element
2. detect atomic number
3. detect electron shell data from science source
4. detect shell layers
5. detect valence layer
6. detect bonding possibility
7. detect relation field
8. render visible shell structure

## shell_layer

```text
nucleus = center place
electron_shell = surrounding layer
valence_shell = outer relation layer
bonding_possibility = shell boundary interaction
```

## relation_to_cell_value

원소 칸의 고유값은 전자껍질과 연결된다.

```text
element_cell_value
= atomic_number
+ mass_condition
+ electron_configuration
+ periodic_position
+ bonding_possibility
```

## renderer_role

전자껍질 구현은 원소의 결합 가능성을 눈으로 보이게 하는 것이 목적이다.

목표는 아름다운 원자 그림이 아니다.

목표는 원소 자리의 relation / boundary / shell / valence layer가 보이게 하는 것이다.

## geometry_layer

```text
center
→ shell
→ outer boundary
→ bonding relation
```

## vector_layer

```text
nucleus_center
→ shell_expansion
→ valence_boundary
→ bond_direction_candidate
```

## relation

prev:
- schema.075_chemical_formula_structure_renderer

related:
- schema.048_sphere_shell_distinction
- schema.049_flip_boundary_spread_structure
- schema.057_seedbase_database_data_definition
- schema.074_science_based_implementation_principle
- schema.077_water_molecule_angle_implementation
- schema.010_sequence_structure
- schema.065_oplus_common_operator

## forbidden

- 전자껍질을 단순 이미지로 보지 않는다.
- 전자껍질을 과학적으로 임의 생성하지 않는다.
- 전자껍질 구현을 양자역학 증명으로 보지 않는다.
- 전자껍질을 행성궤도식 모형으로만 고정하지 않는다.
- valence layer와 전체 shell을 혼동하지 않는다.
- shell을 장식용 외곽선으로 보지 않는다.
- 과학값 출처 없이 세부값을 확정하지 않는다.

## pending

- 실제 shell 데이터는 구현 단계에서 공식 과학 자료를 참조한다.
- 단순 Bohr-style rendering과 orbital rendering은 구분해야 한다.
- 전자구름 / 오비탈 / 확률분포 구현은 후속 단계로 보류한다.

## shortest

전자껍질 = 원소 자리의 visible shell / 결합 가능성을 보이게 하는 layer
