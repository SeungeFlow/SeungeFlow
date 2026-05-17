---
id: schema.071.three_to_two_place_overlap_principle
type: active_schema_metadata
filename: three_to_two_place_overlap_principle.meta.md
directory: 071_three_to_two_place_overlap_principle
status: active_draft
prev: schema.070.right_triangle_fold_unfold_structure
---

# META: three_to_two_place_overlap_principle

## role
three_to_two_place_overlap_principle은 3칸처럼 보이는 구조가 자리중첩을 통해 유효 2칸으로 읽히는 원리를 정의하는 schema이다.

이 meta 파일은 인공지능이 A-B-C 구조에서 B를 독립된 세 번째 칸으로만 세지 않고, A와 C의 shared boundary cell로 읽을 수 있게 하는 기준이다.

## core

```text
3칸처럼 보이나 유효 2칸
```

```text
A + B + C = 3
A ⊕ C = 2
```

## definition

3칸ㆍ2칸 원리는 A-B-C처럼 세 칸이 보이는 구조에서, 가운데 B가 독립칸이 아니라 A의 끝자리와 C의 시작자리가 겹친 자리중첩 영역일 때, 전체 유효칸수가 2가 되는 원리이다.

B는 삭제되지 않는다.

B는 A와 C의 공유 boundary로 흡수된다.

## abc_structure

```text
A = 하나의 완전한 칸
C = 하나의 완전한 칸
B = A_end(1/2) + C_start(1/2)
```

```text
A[1/2]
+
B(A[1/2] ⊕ C[1/2])
+
C[1/2]
=
2
```

## place_overlap_rule

B를 독립 entity로 보면 전체는 3이다.

B를 shared boundary cell로 보면 전체는 2이다.

따라서 B의 정체를 먼저 판정해야 한다.

## geometry_layer

```text
visible: A B C
effective: A ⊕ C
B = overlap boundary
```

## integer_layer

```text
visible_count = 3
effective_count = 2
overlap_count = 1
```

## vector_layer

```text
A_end → B ← C_start
B = transition overlap
```

## relation

prev:
- schema.070_right_triangle_fold_unfold_structure

related:
- schema.064_place_overlap_structure
- schema.065_oplus_common_operator
- schema.069_ddx_right_triangle_transition
- schema.072_two_to_one_triangle_overlap_principle
- schema.046_flip_cycle_transition_structure

## forbidden

- 3칸을 무조건 3개의 독립 entity로 보지 않는다.
- B를 독립칸으로 두 번 세지 않는다.
- 2칸을 단순 감소로 보지 않는다.
- 겹친 칸의 흡수를 삭제로 보지 않는다.
- 양자중첩으로 동일시하지 않는다.

## pending

- 9와 0의 중첩은 related note로 보존하되 독립 schema 여부는 보류한다.
- 직각삼각대칭에서 3칸ㆍ2칸이 어떻게 렌더링되는지는 후속 renderer에서 검토한다.

## shortest

3처럼 보이나 B가 공유 boundary면 유효 2 / A⊕C
