---
id: schema.000.dot
type: active_schema_metadata
filename: dot.meta.md
directory: 000_dot
status: active_draft
root_directory: Structure_Principle
role_mode: origin_pointer_schema
---

# META: dot

## role

dot을 최초 최소 자리로 보존한다.

동시에 `dot.meta.md`는 dot의 의미를 000 안에서 완전히 닫는 문서가 아니다.

`dot.meta.md`는 001~121 active schema 안에서 dot과 유사하게 작동하는 자리, 중심, 교차, pin, 임계, 구심, 문맥별 작동점을 가리키는 origin pointer schema이다.

즉 이 문서는 dot의 최종 의미고정 문서가 아니라, dot이 이후 schema들 안에서 어떤 모습으로 다시 나타나는지 추적하기 위한 root reference 문서이다.

## core

```text
dot =
최초 최소 자리

dot.meta.md =
dot 의미고정문서 X
dot-related schema를 가리키는 origin pointer O
```

## definition

dot은 값이 아니라 자리이다.

dot은 구조 안에서 최초로 드러나는 최소 place-state이며, 선, 벡터, 수열, 자리연산, relation이 시작될 수 있는 최소 anchor이다.

그러나 dot의 모든 작동을 `000_dot` 안에서 완전히 닫지 않는다.

001~121 active schema 안에서 dot과 유사하게 작동하는 구조들이 나타날 수 있다.

`dot.meta.md`는 그 구조들을 하나로 병합하지 않고, 각자의 문맥과 boundary를 보존한 채 relation으로 가리킨다.

따라서 dot은 다음처럼 읽는다.

```text
dot =
최초 최소 자리
값이 아니라 place-state
구조가 시작될 수 있는 최소 anchor
```

그리고 `dot.meta.md`는 다음처럼 읽는다.

```text
dot.meta.md =
000 안에서 dot을 완전히 닫는 문서 X
001~121 안의 dot-like function을 가리키는 origin pointer O
```

## structure

```text
dot
→ pointer_to_dot_related_schema
→ context_check
→ dot_like_function_extract
→ relation_preservation
→ no_merge
```

## dot_related_pointer

### 001_line

```text
related:
- schema.001.line
```

dot과 닿는 부분:

```text
line =
dot과 dot 사이에 차이 / 방향 / relation이 생길 때 드러나는 선분 구조 후보
```

주의:

```text
line ≠ dot
line은 dot 사이의 relation이 드러난 구조이다.
```

### 002_surface

```text
related:
- schema.002.surface
```

dot과 닿는 부분:

```text
surface =
여러 dot / line / boundary relation이 펼쳐져 드러나는 면 구조 후보
```

주의:

```text
surface ≠ dot
surface는 dot이 확장되어 드러난 결과층이지 dot 자체가 아니다.
```

### 003_cell

```text
related:
- schema.003.cell
```

dot과 닿는 부분:

```text
cell =
state가 놓일 수 있는 최소 칸 / place unit 후보
```

주의:

```text
cell ≠ dot
cell은 dot이 놓이거나 relation이 배치될 수 있는 칸 구조이다.
```

### 019_center_point

```text
related:
- schema.019.center_point
```

dot과 닿는 부분:

```text
center_point =
중심점 / 기준점 / 정중심 후보
```

주의:

```text
center_point ≠ dot
center_point는 dot-like center function을 가질 수 있으나 dot 자체는 아니다.
```

### 020_crossing_point

```text
related:
- schema.020.crossing_point
```

dot과 닿는 부분:

```text
crossing_point =
둘 이상의 line / axis / relation이 만나는 자리
```

주의:

```text
crossing_point ≠ 000dot
crossing_point는 교차 이후 생기는 자리이다.
```

### 026_dot_dot_system

```text
related:
- schema.026.dot_dot_system
```

dot과 닿는 부분:

```text
dot =
상태 / 자리

dot_dot =
두 dot 사이의 차이 / 선분 / relation
```

주의:

```text
dot_dot은 dot의 단순 반복이 아니라
두 자리 사이에서 차이가 드러난 relation 구조이다.
```

### 059_empty_place_present_understanding

```text
related:
- schema.059.empty_place_present_understanding
```

dot과 닿는 부분:

```text
empty_place =
아직 state가 놓이지 않은 자리

000dot =
field 안에서 최초로 드러나는 place-state
```

주의:

```text
empty_place ≠ 000dot
empty_place는 아직 state가 놓이지 않은 자리이고,
000dot은 최초로 드러난 place-state이다.
```

### 062_place_domain_definition

```text
related:
- schema.062.place_domain_definition
```

dot과 닿는 부분:

```text
place =
A와 C 사이의 B
relation이 발생할 수 있는 between-domain
```

주의:

```text
dot은 place의 최소 anchor로 작동할 수 있으나
place 전체와 동일하지 않다.
```

### 068_ctp_vector_coordinate_x_dx_ddx

```text
related:
- schema.068.ctp_vector_coordinate_x_dx_ddx
```

dot과 닿는 부분:

```text
x =
기준축 / 기준 자리

dx =
자리전이 / 첫 변위

ddx =
꺾임 / 경사 / 변위의 변화
```

주의:

```text
dot은 x / dx / ddx의 기준 anchor와 relation을 가질 수 있으나
x / dx / ddx 자체로 병합하지 않는다.
```

### 079_cheonjiiin_input_order_vowel_direction

```text
related:
- schema.079.cheonjiiin_input_order_vowel_direction
```

dot과 닿는 부분:

```text
ㆍ =
방향 발생 dot / vector dot 후보

ㅇ =
000dot / 닫힌 원형 dot / 정중심 후보
```

주의:

```text
ㆍ ≠ ㅇ
ㆍ ≠ 000dot
ㅇ도 문맥에 따라 000dot 계열로 읽을 수 있으나,
항상 schema.000.dot과 동일시하지 않는다.
```

### 081_inner_vowel_pull_structure

```text
related:
- schema.081.inner_vowel_pull_structure
```

dot과 닿는 부분:

```text
ㆍ =
끌림점 / 방향점
```

주의:

```text
ㆍ은 축에 붙는 수동 점이 아니라,
문맥에 따라 ㅡ / ㅣ을 끌어당기는 작동점으로 읽힐 수 있다.
하지만 이 ㆍ을 000dot으로 고정하지 않는다.
```

### 082_square_center_vowel_orbit_structure

```text
related:
- schema.082.square_center_vowel_orbit_structure
```

dot과 닿는 부분:

```text
ㅇ =
중심칸 / 000dot 후보

ㆍ =
공전 방향점
```

주의:

```text
ㅇ과 ㆍ은 둘 다 dot-like function을 가질 수 있으나 층위가 다르다.
ㅇ은 중심칸 후보이고, ㆍ은 공전 방향점 후보이다.
```

### 085_opposed_correspondence_formula

```text
related:
- schema.085.opposed_correspondence_formula
```

dot과 닿는 부분:

```text
ㅇ =
닫힌 장 / capsule / shell / 꼭지점 dot 후보

ㆍ =
vector seed / 방향 발생 dot
```

주의:

```text
ㅇ과 ㆍ을 동일한 dot으로 병합하지 않는다.
```

### 101_three_dot_reading_mode_structure

```text
related:
- schema.101.three_dot_reading_mode_structure
```

dot과 닿는 부분:

```text
세 점 ≠ 자동 삼각

도형론 =
삼각

벡터론 =
Y / 방향변화

flow론 =
흐름 / 회전
```

주의:

```text
dot_dot_dot은 dot의 단순 반복이 아니라
reading mode에 따라 다른 구조를 여는 raw structure이다.
```

### 110_nine_zero_overlap_transition

```text
related:
- schema.110.nine_zero_overlap_transition
```

dot과 닿는 부분:

```text
9_end ㆍ 0_start

ㆍ =
끝과 시작의 방향중첩점
```

주의:

```text
여기서 ㆍ은 000dot이 아니라
끝과 시작이 겹치는 transition pin으로 읽는다.
```

### 117_structural_sequence_integer_cell_structure

```text
related:
- schema.117.structural_sequence_integer_cell_structure
```

dot과 닿는 부분:

```text
ㆍ =
0번째 칸

0 =
1번째 칸

9 =
10번째 칸 / boundary
```

주의:

```text
ㆍ = 0번째 칸은 구조수열 문맥의 reading이다.
000dot 정의 자체로 병합하지 않는다.
```

### 118_pin_dot_y_branch_return_structure

```text
related:
- schema.118.pin_dot_y_branch_return_structure
```

dot과 닿는 부분:

```text
pin =
작동 가능한 dot

dot =
최소자리
```

주의:

```text
pin ≠ dot
pin은 dot이 작동 가능 상태로 들어간 문맥별 기능이다.
```

### 119_flow_transition_self_operation_structure

```text
related:
- schema.119.flow_transition_self_operation_structure
```

dot과 닿는 부분:

```text
무수한 ㆍ
→ ㅡ

임계ㆍ
→ ㅣ

전이
→ ㅎ
```

주의:

```text
여기서 ㆍ은 흐름이 꺾이고 임계에 도달하는 작동점이다.
000dot으로 고정하지 않는다.
```

### 121_coredot_ambiguity_boundary

```text
related:
- schema.121.coredot_ambiguity_boundary
```

dot과 닿는 부분:

```text
Core =
사용 가능 후보

Coremap =
사용 가능 후보

CoreDot =
보류

dot =
000에서 보존

ㆍ =
문맥별 작동점
```

주의:

```text
CoreDot은 dot의 본명도 아니고,
ㆍ의 정체도 아니고,
Coremap의 최소 단위도 아니다.
```

## relation

prev:
- none

next:
- schema.001.line

related:
- schema.001.line
- schema.002.surface
- schema.003.cell
- schema.019.center_point
- schema.020.crossing_point
- schema.026.dot_dot_system
- schema.059.empty_place_present_understanding
- schema.062.place_domain_definition
- schema.068.ctp_vector_coordinate_x_dx_ddx
- schema.079.cheonjiiin_input_order_vowel_direction
- schema.081.inner_vowel_pull_structure
- schema.082.square_center_vowel_orbit_structure
- schema.085.opposed_correspondence_formula
- schema.101.three_dot_reading_mode_structure
- schema.110.nine_zero_overlap_transition
- schema.117.structural_sequence_integer_cell_structure
- schema.118.pin_dot_y_branch_return_structure
- schema.119.flow_transition_self_operation_structure
- schema.121.coredot_ambiguity_boundary

relation_reason:

```text
000dot은 최초 최소 자리로 보존한다.
그러나 001~121 active schema 안에는 dot처럼 보이거나 dot처럼 작동하는 구조들이 여러 문맥에서 나타난다.
이 문서는 그 구조들을 dot에 병합하지 않고, 각 schema의 문맥 안에서 dot-like function으로 가리킨다.
```

## forbidden

```text
dot을 단순 수학적 점으로 보지 않는다.
dot을 값으로 보지 않는다.
dot.meta.md를 dot 의미고정 종착문서로 보지 않는다.
dot을 모든 ㆍ과 동일시하지 않는다.
dot을 dot0과 혼동하지 않는다.
dot을 CoreDot으로 바꾸지 않는다.
dot을 Core 또는 Coremap의 최소 단위로 고정하지 않는다.
dot을 empty_place와 동일시하지 않는다.
dot을 pin과 병합하지 않는다.
dot을 center_point나 crossing_point와 병합하지 않는다.
dot-related schema를 dot의 확장으로 강제 병합하지 않는다.
```

## pending

```text
001~121 전체 active schema에서 dot-like function을 더 세밀하게 추출할 수 있다.
dot_related_pointer는 고정 목록이 아니라 갱신 가능한 relation map으로 둔다.
CoreDot 용어는 schema.121에서 계속 보류한다.
dot0와 000dot의 차이는 별도 relation note로 더 정리할 수 있다.
ㆍ의 문맥별 작동점 목록은 별도 index로 둘 수 있다.
```

## shortest

```text
dot =
최초 최소 자리

dot.meta.md =
의미고정문서 X
001~121 dot-like function을 가리키는 origin pointer O

핵심 guard =
dot ≠ ㆍ 전체
dot ≠ pin
dot ≠ dot0
dot ≠ CoreDot
dot ≠ empty_place
```
