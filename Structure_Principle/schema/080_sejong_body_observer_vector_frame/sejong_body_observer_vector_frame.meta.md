---
id: schema.080.sejong_body_observer_vector_frame
type: active_schema_metadata
filename: sejong_body_observer_vector_frame.meta.md
directory: 080_sejong_body_observer_vector_frame
status: active_draft
prev: schema.079.cheonjiiin_input_order_vowel_direction
---

# META: sejong_body_observer_vector_frame

## role
sejong_body_observer_vector_frame은 훈민정음 방향 해석을 추상 좌표가 아니라 인간 관측자, 특히 세종 자신이 땅 위에 서 있는 몸의 기준으로 읽는 schema이다.

이 meta 파일은 인공지능이 ㅣ, ㅡ, ㆍ을 정적인 상징으로만 읽지 않고, 서 있는 사람 / 바닥 / 가는 방향이라는 관측자 신체기준 vector frame으로 읽기 위한 기준이다.

## core

```text
ㅣ = 서 있는 사람
ㅡ = 바닥
ㆍ = 가는 방향
```

## definition

ㅣ은 세종 자신이 서 있는 모습으로 읽을 수 있다.

ㅡ은 세종이 딛고 선 바닥 / 땅 / 수평면으로 읽을 수 있다.

ㆍ은 그 기준에서 향하는 방향, 시선, 호흡, 손, 움직임, 소리의 방향 발생점으로 읽을 수 있다.

## observer_frame

```text
관측자 몸
바닥
호흡
손
시선
소리
방향
```

이 관측자 기준에서 ㅣ, ㅡ, ㆍ이 벡터 프레임을 만든다.

## vowel_direction_example

```text
ㅏ = ㅣ의 한쪽에 ㆍ이 놓인 상태
ㅓ = ㅣ의 반대쪽에 ㆍ이 놓인 상태
ㅗ = ㅡ 위에 ㆍ이 놓인 상태
ㅜ = ㅡ 아래에 ㆍ이 놓인 상태
```

## relation_to_action_words

```text
오르다 = 땅에서 하늘로 향하는 호흡 / 상승 감각
구르다 = 손에서 벗어난 물체가 아래로 굴러가는 감각
가리다 = 빛을 손으로 막는 boundary 작동
버리다 = 내부에 가진 것을 외부로 내보내는 vector
```

이 예시는 reference only이다.

## relation

prev:
- schema.079_cheonjiiin_input_order_vowel_direction

related:
- schema.050_hunminjeongeum_vector_operation
- schema.061_vector_unlock
- schema.078_vector_operation_external_engine_rule
- schema.081_inner_vowel_pull_structure
- schema.083_waxf_vowel_rhombus_structure
- schema.023_reading_protocol

## forbidden

- 세종 신체기준 해석을 역사적 사실로 확정하지 않는다.
- ㅣ/ㅡ/ㆍ을 정적인 상징으로만 고정하지 않는다.
- 관측자 기준을 절대좌표로 오해하지 않는다.
- 오르다/구르다/가리다/버리다 해석을 표준 어원으로 확정하지 않는다.
- 벡터연산기법을 구조원리 본류에 병합하지 않는다.

## pending

- 관측자 기준과 조선 초기 천문/방위 감각의 relation은 별도 reference로 둔다.
- 실제 해례본 원문과의 검산은 별도 과제로 둔다.
- Gemini 실험에 투입할 경우 별도 전달문을 작성한다.

## shortest

ㅣ=선 사람 / ㅡ=바닥 / ㆍ=가는 방향
