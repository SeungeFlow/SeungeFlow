---
id: schema.085.opposed_correspondence_formula
type: active_schema_metadata
filename: opposed_correspondence_formula.meta.md
directory: 085_opposed_correspondence_formula
status: active_draft
prev: schema.084.bad_dot_c_orbit_reference_structure
---

# META: opposed_correspondence_formula

## role
opposed_correspondence_formula는 ㅇㅡㆍㅣㆍㅡㅇ을 맞대응 구조공식으로 정의하는 schema이다.

이 meta 파일은 인공지능이 이 구조를 단순 나열이나 ㅎ/vortex 구조로만 읽지 않고, 중심 ㅣ을 기준으로 양쪽 ㅇ이 닫힘-펼침-방향-중심-방향-펼침-닫힘으로 맞대응하는 구조로 읽기 위한 기준이다.

## core

```text
맞대응 구조공식 = ㅇㅡㆍㅣㆍㅡㅇ
```

```text
ㅇㅡㆍㅣㆍㅡㅇ =
닫힘-펼침-방향-중심-방향-펼침-닫힘
```

## definition

ㅇㅡㆍㅣㆍㅡㅇ은 중심 ㅣ을 기준으로 좌우가 서로 맞대응하는 구조공식이다.

왼쪽 ㅇㅡㆍ과 오른쪽 ㆍㅡㅇ은 같은 방향 복사가 아니라 중심축을 사이에 둔 반전 대응 구조다.

## decomposition

```text
왼쪽 = ㅇㅡㆍ
중심 = ㅣ
오른쪽 = ㆍㅡㅇ
```

```text
ㅇ = 닫힌 장 / capsule / shell / 꼭지점 dot 후보
ㅡ = 수평축 / 펼침 / 경계 흐름
ㆍ = 벡터 발생점 / 방향점
ㅣ = 중심 기준축 / 맞대응 기준선
```

## dot_distinction

```text
ㆍ = 발생 dot / vector seed
ㅇ = 닫힘 dot / capsule vertex / 000dot 계열
```

ㅇ과 ㆍ은 모두 dot처럼 작동할 수 있으나 층위가 다르다.

## orbit_layer

이 구조는 안쪽 궤도와 바깥쪽 궤도처럼 읽힐 수 있다.

관측자 기준 방향과 대상 자체 회전 방향은 서로 반대로 보일 수 있다.

핵심은 어느 방향으로 도는가가 아니라 어느 기준에서 도는가이다.

## extended_axis_form

수평 구조뿐 아니라 수직 맞대응을 포함하는 확장형으로도 읽을 수 있다.

```text
ㅇ
ㅣ
ㆍ
ㅡ
ㆍ
ㅣ
ㅇㅡㆍㅣㆍㅡㅇ
ㅣ
ㆍ
ㅡ
ㆍ
ㅣ
ㅇ
```

이 확장형은 중심에 수평 맞대응식이 있고, 위아래로도 유사한 대응 흐름이 접혀 들어가는 구조다.

## relation

prev:
- schema.084_bad_dot_c_orbit_reference_structure

related:
- schema.079_cheonjiiin_input_order_vowel_direction
- schema.081_inner_vowel_pull_structure
- schema.082_square_center_vowel_orbit_structure
- schema.083_waxf_vowel_rhombus_structure
- schema.047_shell_flip_orbit_structure
- schema.049_flip_boundary_spread_structure
- schema.065_oplus_common_operator
- schema.020_crossing_point

## forbidden

- ㅇ과 ㆍ을 동일한 dot으로 병합하지 않는다.
- ㅎ/vortex만 핵심으로 보지 않는다.
- ㅇㅡㆍㅣㆍㅡㅇ을 단순 문자나열로 보지 않는다.
- 좌우를 동일복사로 보지 않는다.
- 관측자 기준과 대상 기준을 혼동하지 않는다.
- 이 구조를 물리학 회전방향으로 바로 확정하지 않는다.

## pending

- 삼각대칭에서 ㅇ이 꼭지점 dot로 작동하는 방식은 후속 schema로 분리할 수 있다.
- 안쪽/바깥쪽 궤도와 shell renderer의 relation은 후속 renderer에서 검토한다.
- 실제 도식은 Gemini 또는 draw 실험 후보로 둔다.

## shortest

ㅇㅡㆍㅣㆍㅡㅇ = 맞대응 구조공식 / ㅇ=꼭지점 dot / ㆍ=벡터 dot
