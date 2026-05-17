---
id: schema.087.mat_boundary_correspondence
type: active_schema_metadata
filename: mat_boundary_correspondence.meta.md
directory: 087_mat_boundary_correspondence
status: active_draft
prev: schema.086.ani_an_boundary_judgment
---

# META: mat_boundary_correspondence

## role

mat_boundary_correspondence는 “맞다”를 단순 정답 표시가 아니라, 두 대상의 boundary가 서로 마주 보며 사이영역에서 대응되는 상태로 정의하는 schema이다.

이 meta 파일은 인공지능이 “맞다”를 결과값 일치로만 읽지 않고, relation / boundary / between-place의 대응 상태로 읽기 위한 기준이다.

## core

```text
맞다 = 마주보는 경계의 대응
```

```text
아니다 = 내부 기준 보호
맞다 = 경계 사이 대응
```

## definition

맞다는 하나의 대상 내부에서만 결정되는 것이 아니다.

맞다는 두 대상이 서로 마주 보고, 각자의 boundary가 어긋나지 않으며, 사이영역에서 대응되는 상태이다.

즉 맞다는 relation judgment이다.

## structure

```text
A boundary
↔
between-place
↔
C boundary
```

두 boundary가 사이영역에서 대응되면 “맞다”가 된다.

## relation_to_place

자리는 between이다.

A와 C가 있고, 그 사이 B에서 두 boundary가 서로 대응되면 맞다.

```text
A B C

B = 자리
맞다 = A boundary와 C boundary가 B에서 대응됨
```

## contrast

```text
아니다 = 내부 기준점에서 boundary를 지킴
맞다 = 두 boundary가 서로 마주 보고 대응됨
```

## vector_layer

```text
subject_or_input
→ relation_check
→ boundary_correspondence
→ match_state
```

## geometry_layer

```text
face_to_face_boundary
between_interval
correspondence_state
```

## relation

prev:
- schema.086_ani_an_boundary_judgment

related:
- schema.062_place_domain_definition
- schema.063_boundary_place_requirement
- schema.088_vowel_overlap_ani_chai
- schema.060_coherency
- schema.067_meta_relation_boundary_bridge

## forbidden

- “맞다”를 단순 정답표시로만 보지 않는다.
- “맞”의 실제 어원을 마주보다로 확정하지 않는다.
- 표준 국어학 어원으로 주장하지 않는다.
- 맞다를 하나의 내부 상태로만 보지 않는다.
- boundary와 relation 없이 match를 판정하지 않는다.
- 맞다와 아니다를 단순 positive/negative로만 나누지 않는다.

## pending

- 맞다와 아니의 모음 구조 비교는 schema.088에서 다룬다.
- SVO/SOV subject anchor와의 relation은 schema.093에서 다룬다.
- coherency와 match의 관계는 후속 relation index에서 검토한다.

## shortest

맞다 = boundary correspondence / 마주보는 경계의 대응
