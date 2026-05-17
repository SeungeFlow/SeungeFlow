---
id: schema.084.bad_dot_c_orbit_reference_structure
type: active_schema_metadata
filename: bad_dot_c_orbit_reference_structure.meta.md
directory: 084_bad_dot_c_orbit_reference_structure
status: active_draft
prev: schema.083.waxf_vowel_rhombus_structure
---

# META: bad_dot_c_orbit_reference_structure

## role
bad_dot_c_orbit_reference_structure는 “어” 위치를 기준으로 공전방향을 잡았을 때, ([x][dx][ddx])가 BDA로 읽히고 A의 대칭점 C가 ㆍ 기준으로 대응되는 구조식 BADㆍC를 정의하는 schema이다.

이 meta 파일은 인공지능이 ABCD, BADC, BAD, BADㆍC를 혼동하지 않도록 분리하는 기준이다.

## core

```text
기준 = 어 위치
방향 = 공전방향
[x dx ddx] = B D A
C = A의 대칭점
표기 = BADㆍC
```

## definition

BADㆍC는 알파벳 순서가 아니다.

BADㆍC는 “어” 위치를 기준으로 공전방향을 잡았을 때, x, dx, ddx가 BDA로 외부화되고, A의 대칭점인 C가 ㆍ을 기준으로 대응되는 구조식이다.

## distinction

```text
ABCD = 네 자리 전체 배치 / 마름모 꼭지점 / 사각 네 변 / 순서 표시
BADC = 공전방향 / 자리 재배치 / 마름모 회전 배치
BAD = A를 꼭지점으로 하는 꺾인 선분
C = A의 대칭점
BADㆍC = 꺾인 선분과 대칭점의 관계식
```

## x_dx_ddx_mapping

```text
([x][dx][ddx])
→ B D A
```

이는 수학기호 대응이 아니라, 자리전이 좌표를 공전방향에 따라 방위 배치로 바꾼 것이다.

## symmetry_rule

A와 C는 하나의 대칭쌍이다.

C는 BAD 구조 안에 직접 들어온 세 번째 흐름이 아니라 A와 맞대응하는 반대 자리다.

## orbit_reference

방향기준은 공전방향이다.

이 구조는 화면상의 좌우, 알파벳 순서, 글자 입력순서가 아니라 공전방향에 따른 자리배치로 읽는다.

## relation

prev:
- schema.083_waxf_vowel_rhombus_structure

related:
- schema.068_ctp_vector_coordinate_x_dx_ddx
- schema.070_right_triangle_fold_unfold_structure
- schema.079_cheonjiiin_input_order_vowel_direction
- schema.081_inner_vowel_pull_structure
- schema.082_square_center_vowel_orbit_structure
- schema.085_opposed_correspondence_formula
- schema.020_crossing_point
- schema.021_fold_unfold

## forbidden

- ABCD, BADC, BAD, BADㆍC를 같은 구조로 병합하지 않는다.
- BAD를 알파벳 순서로 읽지 않는다.
- BADㆍC를 최종 물리방향으로 확정하지 않는다.
- A와 C의 대칭관계를 생략하지 않는다.
- ㆍ을 단순 구분점으로만 보지 않는다.
- 이 구조를 구조원리 본류에 병합하지 않는다.

## pending

- 어 위치 기준의 정확한 렌더링은 후속 실험으로 둔다.
- BADㆍC와 WAXF의 relation은 active_navimap에서 분리 표시한다.
- 이 schema는 벡터연산기법 relation으로 보존한다.

## shortest

BADㆍC = 어 기준 / 공전방향 / [x dx ddx]=BDA / C=A의 대칭점
