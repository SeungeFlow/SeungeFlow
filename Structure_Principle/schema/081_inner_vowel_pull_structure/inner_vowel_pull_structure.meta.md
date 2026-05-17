---
id: schema.081.inner_vowel_pull_structure
type: active_schema_metadata
filename: inner_vowel_pull_structure.meta.md
directory: 081_inner_vowel_pull_structure
status: active_draft
prev: schema.080.sejong_body_observer_vector_frame
---

# META: inner_vowel_pull_structure

## role
inner_vowel_pull_structure는 ㆍ이 ㅣ 또는 ㅡ에 단순히 붙는 것이 아니라, ㅣ 또는 ㅡ을 끌어당기는 방향점으로 작동한다는 구조를 정의하는 schema이다.

이 meta 파일은 인공지능이 ㅗ와 ㅓ를 외부 부착 모음으로만 보지 않고, ㆍ이 먼저 놓여 ㅡ/ㅣ을 끌어당기는 안쪽 기준 구조로 읽기 위한 기준이다.

## core

```text
ㆍ = 끌림점 / 방향점
ㅗ = ㆍㅡ
ㅓ = ㆍㅣ
안쪽 기준 = ㅗ와 ㅓ
```

## definition

ㆍ은 ㅣ 또는 ㅡ에 붙는 수동 점이 아니다.

ㆍ은 ㅣ 또는 ㅡ을 끌어당기는 방향점으로 읽을 수 있다.

ㆍ이 먼저 놓이고 그 뒤에 ㅡ 또는 ㅣ이 오면, ㅗ와 ㅓ가 형성된다.

## pull_structure

```text
ㆍㅡ = ㅗ
ㆍㅣ = ㅓ
```

이 구조에서 ㆍ이 먼저 놓이고 축이 뒤따라온다.

따라서 ㅗ와 ㅓ는 안쪽 기준으로 읽을 수 있다.

## relation_to_o_eo

ㅇ이 붙으면 다음이 된다.

```text
ㅇㆍㅡ = 오
ㅇㆍㅣ = 어
```

ㅇ은 000dot이다.

따라서 오와 어는 000dot 안에서 ㆍ이 먼저 놓이고, 그 ㆍ이 ㅡ 또는 ㅣ을 끌어당겨 생긴 방향음으로 읽을 수 있다.

## action_trace

```text
오르다 = ㆍㅡㅡ
어리다 = ㆍㅣㅣ
```

축은 먼저 단방향 순방향, 축변환 없는 형태를 기준으로 읽는다.

## relation

prev:
- schema.080_sejong_body_observer_vector_frame

related:
- schema.079_cheonjiiin_input_order_vowel_direction
- schema.082_square_center_vowel_orbit_structure
- schema.083_waxf_vowel_rhombus_structure
- schema.085_opposed_correspondence_formula
- schema.086_ani_an_boundary_judgment

## forbidden

- ㆍ을 단순 부착점으로만 보지 않는다.
- ㅗ와 ㅓ를 외부 방향으로만 고정하지 않는다.
- 안쪽 기준을 절대 방향으로 고정하지 않는다.
- 오르다/어리다를 표준 어원으로 확정하지 않는다.
- 이 schema를 구조원리 본류와 병합하지 않는다.

## pending

- ㆍ의 pull 구조와 공전방향의 relation은 schema.082에서 보강한다.
- ㅗ/ㅓ의 안쪽 기준이 WAXF에서 어떤 자리에 놓이는지는 schema.083에서 분리한다.

## shortest

ㆍ=끌림점 / ㅗ=ㆍㅡ / ㅓ=ㆍㅣ / 안쪽 기준=ㅗ·ㅓ
