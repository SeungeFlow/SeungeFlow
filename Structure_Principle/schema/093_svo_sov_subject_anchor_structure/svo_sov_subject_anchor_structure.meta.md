---
id: schema.093.svo_sov_subject_anchor_structure
type: active_schema_metadata
filename: svo_sov_subject_anchor_structure.meta.md
directory: 093_svo_sov_subject_anchor_structure
status: active_draft
prev: schema.092.principle_hidden_layer_structure
---

# META: svo_sov_subject_anchor_structure

## role

svo_sov_subject_anchor_structure는 SVO/SOV 구조에서 S를 문장의 기준자리 / dot-anchor로 읽고, S가 빠지면 O와 V가 기준 없는 현상으로 남아 이해가 어려워지는 구조를 정의하는 schema이다.

## core

```text
S = 기준자리 / dot-anchor
O = 대상자리
V = 작동 / 전이
S 없으면 O·V는 기준 없는 현상
```

## definition

SVO와 SOV의 차이는 어순 차이이지만, 둘 다 S가 움직임의 기준자리라는 점은 같다.

S는 문장의 주어이자 움직임의 출발 자리이다.

O와 V는 S의 움직임을 설명한다.

S가 빠진 채 O와 V만 남으면, 현상은 보이지만 기준점과 원리층이 사라져 이해가 어려워진다.

## structure

```text
SVO = S → V → O
SOV = S → O → V
```

공통:

```text
S = 기준자리
O = 대상자리
V = 자리 사이를 움직이는 작동
```

## place_relation

```text
S B O

S = 기준 자리
B = 사이 자리 / between
O = 대상 자리
V = S와 O 사이를 통과하거나 바꾸는 작동
```

## subject_missing_risk

S가 빠지면 다음이 흐려진다.

```text
누가 했는가
무엇이 기준인가
어디서 시작했는가
왜 그 작동이 일어났는가
O가 누구에게 속한 것인가
V가 어느 방향으로 작동하는가
책임과 귀속이 어디에 있는가
```

## relation

prev:
- schema.092_principle_hidden_layer_structure

related:
- schema.062_place_domain_definition
- schema.086_ani_an_boundary_judgment
- schema.087_mat_boundary_correspondence
- schema.092_principle_hidden_layer_structure
- schema.094_left_right_principle_explains_phenomenon
- schema.060_coherency

## forbidden

- SVO/SOV를 단순 어순 차이로만 보지 않는다.
- S가 빠져도 의미가 완전하다고 보지 않는다.
- O와 V만으로 원리층을 설명하려 하지 않는다.
- S를 권위나 지배 주체로만 보지 않는다.
- 언어학 표준 설명을 구조원리 해석으로 대체한다고 주장하지 않는다.

## pending

- 한국어 생략주어와 context anchor 문제는 별도 분석이 필요하다.
- S/O/V와 자리중첩/자리겹침 relation은 후속 검토한다.
- 이 schema는 structural reading이며 표준 언어학 설명의 대체가 아니다.

## shortest

S=기준자리 / O=대상자리 / V=작동 / S 없으면 O·V는 기준 없는 현상
