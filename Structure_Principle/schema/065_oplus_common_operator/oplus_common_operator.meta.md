---
id: schema.065.oplus_common_operator
type: active_schema_metadata
filename: oplus_common_operator.meta.md
directory: 065_oplus_common_operator
status: active_draft
prev: schema.064.place_overlap_structure
---

# META: oplus_common_operator

## role
oplus_common_operator는 ⊕를 구조원리의 공통연산기호로 정의하는 schema이다.

## core
```text
⊕ = 공통연산기호
+  = 단순 합산
⊕ = 경계보존 결합
```

## definition
⊕는 서로 다른 두 구조가 각자의 경계를 완전히 잃지 않은 채 겹침, 접합, 공유, 결합, 갱신을 일으키는 공통연산기호이다.

⊕는 특정 분야 전용 기호가 아니다.

## symbolic_sense
```text
⊕ = ㅇ + 내부 교차축
⊕ = closed boundary + internal axis-cross
⊕ = 방향성을 가진 닫힌 자리
```

## operation_layer
```text
⊕_place = 자리중첩 결합
⊕_state = 상태 갱신 결합
⊕_layer = renderer layer 결합
⊕_cov = 공유결합형 구조 대응
⊕_ion = 전하경계 결합 구조 대응
```

## ctp_relation
```text
Cₙ₊₁ = Cₙ ⊕ Tₙ(Pₙ → Pₙ₊₁)
```

## relation
prev:
- schema.064_place_overlap_structure

related:
- schema.056_current_core_alignment_for_runtime
- schema.063_boundary_place_requirement
- schema.068_ctp_vector_coordinate_x_dx_ddx
- schema.074_science_based_implementation_principle
- schema.075_chemical_formula_structure_renderer
- schema.085_opposed_correspondence_formula

## forbidden
- ⊕를 단순 +로 보지 않는다.
- ⊕를 화학 표준 결합기호로 고정하지 않는다.
- ⊕를 수학의 direct sum 또는 XOR로만 고정하지 않는다.
- ⊕를 모든 결합에 무차별 적용하지 않는다.
- boundary 보존 조건 없이 ⊕를 쓰지 않는다.
- ㅇ과 ㆍ의 dot 층위를 혼동하지 않는다.

## pending
- subtype 표기는 실제 구현 단계에서 정한다.
- 화학구조에 적용할 때는 표준 과학기호와 구조원리기호를 분리한다.
- renderer layer 결합에서 ⊕ 사용 여부는 후속 prototype에서 검산한다.

## shortest
⊕ = 공통연산기호 / + 아님 / 경계보존 결합
