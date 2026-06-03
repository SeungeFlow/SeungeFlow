# Y_Branch tree

## 0. Role of this file

`tree.md`는 `Y_Branch`의 place-state map이다.

이 문서는 파일 목록만 나열하지 않는다. 각 문서가 왜 그 자리에 놓이는지, 어떤 문서가 어떤 역할을 갖는지, 어떤 문서가 아직 pending seat인지 기록한다.

---

## 1. Root documents

```text
Y_Branch/
├─ README.md
├─ tree.md
└─ Path.md
```

- `README.md`: first gateway
- `tree.md`: place-state map
- `Path.md`: path rule

---

## 2. source_index/

```text
source_index/
├─ README.md
├─ raw_source_index_11th_brake_test.md
├─ music_language_sources.md        [pending seat]
├─ event_context_sources.md         [pending seat]
└─ y_branch_source_status.md
```

`source_index/`는 원자료의 의미를 해석하지 않는다. source identity만 기록한다.

---

## 3. schema/

```text
schema/
├─ 000_dot/
│  ├─ meta.md
│  └─ metaplus.md                 [pending seat]
├─ 001_diff/
│  └─ diff.meta.md
├─ 002_orbit/
│  └─ orbit.meta.md               [pending seat]
├─ 003_cog_9dot0/
│  └─ cog_9dot0.meta.md           [pending seat]
├─ 004_ctp/
│  └─ ctp.meta.md
├─ 005_dimension/
│  └─ dimension.meta.md
├─ 006_ctp24/
│  └─ ctp24.meta.md
├─ 007_source_identity/
│  └─ source_identity.meta.md
├─ 008_matrix_swap/
│  └─ matrix_swap.meta.md         [pending seat]
├─ 009_number_pattern/
│  └─ number_pattern.meta.md      [pending seat]
├─ 010_y_structure/
│  └─ y_structure.meta.md         [pending seat]
└─ 011_structure_interpretation/
   └─ structure_interpretation.meta.md [pending seat]
```

---

## 4. operation/

```text
operation/
├─ S1_minimal_sequence.md          [pending seat]
├─ S2_dimension_structure.md
├─ S3_orbit_operation.md           [pending seat]
├─ S4_cog_9dot0_nested_orbit.md    [pending seat]
├─ R07_boundary_preserving_matrix_swap.md
├─ R12_field_question_validation.md
├─ dot_observer_criterion_operation.md       [pending seat]
├─ vertical_matrix_swap_operation.md         [pending seat]
├─ place_value_carry_transition.md           [pending seat]
├─ spatial_partition_conservation.md         [pending seat]
└─ structure_interpretation_operation.md     [pending seat]
```

---

## 5. engine/

```text
engine/
├─ README.md
├─ state_machine.md                [pending seat]
├─ validator_loop.md
├─ instruction_set.md              [pending seat]
├─ mtp_object_model.md             [pending seat]
├─ confidence_sensitivity_guard.md [pending seat]
├─ ctp24_filter.md
├─ source_identity_filter.md
├─ brake_test_protocol.md
├─ cross_matrix_engine.md          [pending seat]
├─ noise_substance_classifier.md
└─ output_diagnosis_format.md      [pending seat]
```

---

## 6. field/

```text
field/
├─ README.md
├─ capital_market/                 [pending seat]
├─ cosmic_field/                   [pending seat]
├─ root_lineage/                   [pending seat]
├─ narrative_structure/            [pending seat]
├─ music_language/
│  └─ README.md
└─ event_context/
   └─ README.md
```

---

## 7. relation/

```text
relation/
├─ README.md
├─ relation_music_language_to_event_context.md
├─ relation_brake_test_result.md
├─ relation_y_branch_to_tokamak_like_confinement.md [pending seat]
└─ relation_y_structure_root_lineage.md             [pending seat]
```

---

## 8. guard/

```text
guard/
├─ README.md
├─ source_identity_guard.md
├─ original_vs_derived_guard.md
├─ no_source_merge_guard.md
├─ no_overinterpretation_guard.md
├─ no_final_judgment_guard.md
└─ y_branch_source_status_guard.md
```

---

## 9. handoff/

```text
handoff/
├─ README.md
├─ gpt_github_instruction.md
└─ new_instance_alignment.md
```

---

## 10. Reading order

```text
1. README.md
2. tree.md
3. Path.md
4. source_index/
5. schema/007_source_identity/
6. schema/004_ctp/
7. schema/006_ctp24/
8. operation/S2, R07, R12
9. engine/
10. guard/
11. field/
12. relation/
13. handoff/
```

---

## 11. Pending seats

Pending seat는 실패가 아니다. Pending seat는 아직 source / meta / operation이 완전히 닫히지 않은 자리다.

대표 pending:

```text
schema/002_orbit/
schema/003_cog_9dot0/
operation/S4_cog_9dot0_nested_orbit.md
relation/relation_y_branch_to_tokamak_like_confinement.md
field/capital_market/
field/cosmic_field/
field/root_lineage/
```

---

## 12. Shortest

```text
tree.md = place-state map
README.md = first gateway
Path.md = path rule
source_index/ = source fact
guard/ = source interpretation risk control
```
