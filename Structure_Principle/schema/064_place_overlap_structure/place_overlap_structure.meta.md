---
id: schema.064.place_overlap_structure
type: active_schema_metadata
filename: place_overlap_structure.meta.md
directory: 064_place_overlap_structure
status: active_draft
prev: schema.063.boundary_place_requirement
---

# META: place_overlap_structure

## role
place_overlap_structure는 두 구조체가 이어질 때 겹친 자리를 독립 칸으로 두 번 세지 않고, 그 겹친 자리를 새 구조의 내부 boundary로 흡수하는 자리중첩 원리를 정의하는 schema이다.

## core
```text
자리중첩 = 겹친 자리를 두 번 세지 않는 연결 조건
겹친 1칸은 삭제가 아니라 공유 boundary로 흡수된다.
```

## definition
자리중첩이란 두 구조체가 이어질 때, 서로의 끝자리와 시작자리가 같은 자리영역을 공유하여 그 겹친 자리가 독립 칸으로 남지 않고 새 구조의 boundary 안으로 흡수되는 상태이다.

자리중첩은 물리학의 양자중첩과 동일하지 않다.

## example_core
```text
ㅁㆍㅁ
→ 외부 add / 내부 cut
→ ㆍ 흡수
→ ㄴ형 구조체
```

## abc_half_structure
```text
A = 하나의 완전한 칸
C = 하나의 완전한 칸
B = A의 끝 1/2과 C의 시작 1/2이 겹친 자리중첩 영역
B = A_end(1/2) + C_start(1/2)
```

B는 독립 entity가 아니다. B는 shared boundary cell이다.

## integer_layer
```text
visible_cell_count = 3 possible
effective_cell_count = 2
overlap_cell_count = 1
```

## relation
prev:
- schema.063_boundary_place_requirement

related:
- schema.062_place_domain_definition
- schema.065_oplus_common_operator
- schema.071_three_to_two_place_overlap_principle
- schema.072_two_to_one_triangle_overlap_principle
- schema.013_return_preservation
- schema.046_flip_cycle_transition_structure

## forbidden
- 자리중첩을 양자역학의 양자중첩으로 동일시하지 않는다.
- 겹친 칸을 독립 entity로 두 번 세지 않는다.
- 1칸 소실을 단순 삭제로 보지 않는다.
- 접합을 단순 add로만 보지 않는다.
- 자리중첩과 자리겹침을 혼동하지 않는다.

## pending
- 자리겹침과의 구분은 별도 schema에서 다룬다.
- 3칸→2칸 원리는 후속 schema에서 분리한다.
- 직각삼각 fold_unfold와의 관계는 후속 schema에서 보강한다.

## shortest
자리중첩 = 겹친 칸의 boundary 흡수 / 삭제 X, 구조 흡수 O
