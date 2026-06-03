# new_instance_alignment

신규 인스턴스는 다음 순서로 읽는다.

```text
1. README.md
2. tree.md
3. Path.md
4. source_index/
5. schema/007_source_identity/
6. schema/004_ctp/
7. schema/006_ctp24/
8. operation/S2_dimension_structure.md
9. operation/R07_boundary_preserving_matrix_swap.md
10. operation/R12_field_question_validation.md
11. engine/
12. guard/
13. field/
14. relation/
15. handoff/
```

중요:

```text
field/부터 읽지 않는다.
source identity와 Ctp24를 먼저 읽는다.
```
