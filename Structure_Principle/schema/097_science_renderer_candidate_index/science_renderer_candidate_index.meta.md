---
id: schema.097.science_renderer_candidate_index
type: active_schema_metadata
filename: science_renderer_candidate_index.meta.md
directory: 097_science_renderer_candidate_index
status: active_draft
prev: schema.096.vector_operation_relation_index
---

# META: science_renderer_candidate_index

## role

science_renderer_candidate_index는 기존 과학값을 조건으로 받아 visible_relation_field로 구현할 수 있는 과학 구현 후보들을 모으는 index schema이다.

## core

```text
과학문서
→ 조건추출
→ 구조구현
→ visible_relation_field
→ 이해
```

## candidate_domains

### candidate_01_chemical_formula_structure

```text
화학분자식 = 원소 자리들의 결합·중첩 구조표기
분자 = 고유값 가진 칸들의 자리중첩 구조체
```

related:
- schema.075_chemical_formula_structure_renderer

### candidate_02_electron_shell_visual_structure

```text
전자껍질 = 원소 자리의 visible shell
전자껍질은 결합 가능성을 보이게 하는 layer
```

related:
- schema.076_electron_shell_visual_structure

### candidate_03_water_molecule_angle

```text
H2O = 104.5도 조건 구현
104.5도 검증 X
```

related:
- schema.077_water_molecule_angle_implementation

### candidate_04_periodic_table_cell_value

```text
원소주기율표 칸 = 고유값 가진 자리
```

related:
- schema.010_molecular_particle_periodic_cell_value

### candidate_05_slice_window_renderer

```text
TradingView / MRI / Disk_Array slice
= 평면창 기반 구조단면 구현 후보
```

related:
- slice_plane_window_structure
- rolling_boundary_window_structure

## principle

구조원리는 과학을 대체하지 않는다.

구조원리는 과학값을 조건으로 받아 구현한다.

## relation

prev:
- schema.096_vector_operation_relation_index

related:
- schema.074_science_based_implementation_principle
- schema.075_chemical_formula_structure_renderer
- schema.076_electron_shell_visual_structure
- schema.077_water_molecule_angle_implementation
- schema.052_hyperstructure_renderer_architecture
- schema.057_seedbase_database_data_definition
- schema.098_reference_only_high_density_trace_index

## forbidden

- 과학 구현 후보를 과학 검증 결과로 보지 않는다.
- 과학값을 구조원리가 임의 생성한다고 보지 않는다.
- 화학구조를 벡터연산기법과 병합하지 않는다.
- 전자껍질을 단순 이미지로 보지 않는다.
- renderer를 picture generator로 보지 않는다.
- 과학 대응비유를 scientific proof로 승격하지 않는다.

## pending

- 공식 과학값 source 연결이 필요하다.
- 실제 구현 prototype directory는 epluone 후보로 둘 수 있다.
- 화학구조가 첫 구현 후보로 가장 안정적이다.

## shortest

과학구현 후보 index / 과학값 기반 visible_relation_field 구현
