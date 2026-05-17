---
id: schema.082.square_center_vowel_orbit_structure
type: active_schema_metadata
filename: square_center_vowel_orbit_structure.meta.md
directory: 082_square_center_vowel_orbit_structure
status: active_draft
prev: schema.081.inner_vowel_pull_structure
---

# META: square_center_vowel_orbit_structure

## role
square_center_vowel_orbit_structure는 ㅇ을 중심칸으로 두고, 사각의 네 변에 놓인 ㆍ이 공전방향으로 회전하며 오·어·우·아의 네 방향 상태를 만드는 구조를 정의하는 schema이다.

이 meta 파일은 인공지능이 ㅇ을 단순 원형 자모로 보지 않고, 000dot / 중심칸 / closed center field로 읽으며, ㆍ을 네 변 위를 도는 공전 방향점으로 읽기 위한 기준이다.

## core

```text
ㅇ = 중심칸 / 000dot
ㆍ = 공전 방향점
네 변 = ㅡ / ㅣ 선분
오·어·우·아 = ㆍ의 위치상태
```

## definition

사각 구조에서 ㅇ은 중심칸이다.

네 변의 ㅡ/ㅣ 선분 위에 놓이는 ㆍ은 공전방향으로 회전하는 방향점이다.

ㆍ의 위치와 입력순서에 따라 오, 어, 우, 아의 네 방향 상태가 생긴다.

## square_structure

```text
ㆍ
ㆍㅁㆍ
ㆍ
```

또는 중심 ㅇ을 기준으로:

```text
center = ㅇ
edge_points = ㆍ
edge_segments = ㅡ / ㅣ
```

## vowel_generation

```text
ㅇㆍㅡ = 오
ㅇㆍㅣ = 어
ㅇㅡㆍ = 우
ㅇㅣㆍ = 아
```

## orbit_principle

ㅇ이 중심칸이 된 상태에서 네 변을 선분이 감싸고 있을 때, ㆍ은 공전방향으로 회전하는 현상 또는 상황을 표시하는 원리다.

오·어·우·아는 중심 ㅇ을 기준으로 ㆍ이 ㅡ/ㅣ 선분과 만나는 위치상태이다.

## relation

prev:
- schema.081_inner_vowel_pull_structure

related:
- schema.079_cheonjiiin_input_order_vowel_direction
- schema.080_sejong_body_observer_vector_frame
- schema.083_waxf_vowel_rhombus_structure
- schema.084_bad_dot_c_orbit_reference_structure
- schema.085_opposed_correspondence_formula
- schema.019_center_point
- schema.036_orbit_structure

## forbidden

- ㅇ을 단순 자모 원형으로 보지 않는다.
- ㆍ을 고정점으로만 보지 않는다.
- 오·어·우·아를 의미 먼저로 읽지 않는다.
- 공전방향을 절대 천문학 방향으로 고정하지 않는다.
- 중심 ㅇ과 방향점 ㆍ의 dot 층위를 혼동하지 않는다.

## pending

- 사각 구조와 마름모 구조의 전환은 schema.083에서 다룬다.
- 공전방향의 정확한 기준은 BADㆍC schema와 relation으로 둔다.
- 실제 렌더링은 future vector operation experiment에서 검토한다.

## shortest

ㅇ=중심칸 / ㆍ=공전 방향점 / 네 변=ㅡ·ㅣ / 오어우아=ㆍ의 위치상태
