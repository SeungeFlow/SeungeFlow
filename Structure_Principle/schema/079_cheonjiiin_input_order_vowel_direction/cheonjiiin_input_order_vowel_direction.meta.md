---
id: schema.079.cheonjiiin_input_order_vowel_direction
type: active_schema_metadata
filename: cheonjiiin_input_order_vowel_direction.meta.md
directory: 079_cheonjiiin_input_order_vowel_direction
status: active_draft
prev: schema.078.vector_operation_external_engine_rule
---

# META: cheonjiiin_input_order_vowel_direction

## role
cheonjiiin_input_order_vowel_direction은 천지인 입력순서에서 ㆍ, ㅡ, ㅣ의 배열 순서가 ㅜ, ㅗ, ㅏ, ㅓ의 모음 방향을 만든다는 구조를 보존하는 schema이다.

이 meta 파일은 인공지능이 모음 방향을 의미해석이나 자모목록으로만 읽지 않고, 입력순서 기반 vector direction으로 읽기 위한 기준이다.

## core

```text
ㅡㆍ = ㅜ
ㆍㅡ = ㅗ
ㅣㆍ = ㅏ
ㆍㅣ = ㅓ
```

```text
ㅇ = 000dot
ㆍ = 방향 발생 dot / vector dot
```

## definition

천지인 입력순서에서 같은 ㆍ, ㅡ, ㅣ이라도 입력순서가 바뀌면 방향이 달라진다.

모음 방향은 ㆍ, ㅡ, ㅣ의 입력순서에서 발생한다.

ㅇ은 이 구조에서 000dot으로 읽는다.

## input_order_table

```text
ㅡㆍ = ㅜ
ㆍㅡ = ㅗ
ㅣㆍ = ㅏ
ㆍㅣ = ㅓ
```

## dot_distinction

```text
ㆍ = 방향 발생 dot / vector dot
ㅇ = 000dot / 닫힌 원형 dot / 정중심 후보
```

둘 다 dot 계열이지만 층위가 다르다.

## read_order

1. detect ㆍ / ㅡ / ㅣ
2. detect input order
3. map input order to vowel direction
4. preserve ㅇ as 000dot
5. prevent semantic-first reading
6. map to vector operation relation only

## vector_layer

```text
input_order
→ direction
→ vowel
→ possible meaning later
```

## relation

prev:
- schema.078_vector_operation_external_engine_rule

related:
- schema.050_hunminjeongeum_vector_operation
- schema.059_empty_place_present_understanding
- schema.061_vector_unlock
- schema.080_sejong_body_observer_vector_frame
- schema.081_inner_vowel_pull_structure
- schema.082_square_center_vowel_orbit_structure
- schema.083_waxf_vowel_rhombus_structure
- schema.085_opposed_correspondence_formula

## forbidden

- ㆍ와 ㅇ의 dot 층위를 혼동하지 않는다.
- 모음 방향을 사전 의미로 먼저 읽지 않는다.
- 입력순서를 임의로 바꾸지 않는다.
- 이 구조를 표준 국어학 어원 확정으로 주장하지 않는다.
- 벡터연산기법을 구조원리 본류에 병합하지 않는다.

## pending

- 실제 천지인 입력체계와 historical source 검산은 별도 과제로 둔다.
- 이 schema는 structural trace이며, 언어학 확정문이 아니다.
- 모음 방향의 의미 확장은 후속 schema에서 reference로만 둔다.

## shortest

ㅡㆍ=ㅜ / ㆍㅡ=ㅗ / ㅣㆍ=ㅏ / ㆍㅣ=ㅓ / ㅇ=000dot
