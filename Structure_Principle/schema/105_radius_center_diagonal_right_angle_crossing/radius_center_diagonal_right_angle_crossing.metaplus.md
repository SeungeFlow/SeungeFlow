# METAPLUS

id_reference: schema.105.radius_center_diagonal_right_angle_crossing  
schema_name: radius_center_diagonal_right_angle_crossing  
source_file: radius_center_diagonal_right_angle_crossing.meta.md  
metaplus_file: radius_center_diagonal_right_angle_crossing.metaplus.md

purpose:
- 이 문서는 원본 radius_center_diagonal_right_angle_crossing.meta.md를 대체하지 않는다.
- 이 문서는 schema.105.radius_center_diagonal_right_angle_crossing에 대해 사용자와 인공지능이 나눈 대화내용을 정리한다.
- 이 문서는 구조원리를 새로 만들거나 relation을 새로 확정하기 위한 문서가 아니다.
- 이 문서는 대화정리형 이해 로그다.
- 이 문서의 핵심 목적은 승이의 실제 입력글, source_meta, 작업 원칙, AI 인스턴스 대화층을 섞지 않고 분리하는 것이다.
- 이 문서는 105_radius_center_diagonal_right_angle_crossing이 103의 Circle boundary와 104의 내접/외접 contact relation 이후, 정중심·반지름·대각·직각·교차를 원·사각·삼각·칸의 연결 구조어로 정의하는 schema임을 보존한다.
- 이 문서는 동시에 이 시점에서 발생한 대대적인 수정 / 파일교체 가능성 판단 원칙을 보존한다.
- 참고로 105_radius_center_diagonal_right_angle_crossing은 101 이후 재작성 추천 흐름의 후보 목록에도 포함되어 있었다. :contentReference[oaicite:0]{index=0}

conversation_context:
- 이 문서는 ChatGPT.making 대화에서 생성되는 이해정리본이다.
- 원본 radius_center_diagonal_right_angle_crossing.meta.md 수정본이 아니라 대화정리층이다.
- 사용자는 이 시점에서 대대적인 수정 혹은 파일교체 작업을 했다고 설명했다.
- 사용자는 파일교체 가능 여부가 “그 이후의 흐름이 이어졌는가”에 달려 있다고 정리했다.
- 이후 흐름이 아직 이어지지 않은 파일은 교체 가능하지만, 이미 relation이 걸린 파일은 수정 불가능하다고 했다.
- 이미 relation이 걸린 파일은 의미고정된 relation anchor이므로, 수정하려면 metaplus.md와 후속 relation까지 함께 수정해야 한다.
- 따라서 지나간 것은 고치기보다 relation을 연결하고, 보정 요소들을 작성해서 이어붙여야 한다.
- 이 문서는 105 source_meta 이해와 함께 이 append-only / relation-anchor 작업 원칙을 보존한다.

## 1. user_input_summary

[승이의 입력글]

승이는 이 시점의 작업 원칙을 다음처럼 설명했다.

```text
이 시점에서 한번 대대적인 수정 혹은 파일교체 작업을 하였다.
```

그 기준은 다음이다.

```text
생성된 것이 만약 그 이후의 흐름이 이어진 것이 아니라면
파일교체는 가능하다.

즉 이전 흐름이 이어진 것이라면
수정은 불가능하다.

이미 relation이 걸려 있기 때문이다.
```

승이는 이어서 다음을 말했다.

```text
이전의 파일까지 수정시도를 한다면
metaplus.md까지 수정해야 하기 때문에
지나는 것은 이미 의미고정된 것이므로

relation을 연결하는 작업과
여러 다른 요소들을 작성해서
잘 이어붙여야 한다.
```

요약:
- 승이는 파일이 단순 문서가 아니라 후속 relation의 기준점이 되면 의미가 고정된다고 보았다.
- 아직 후속 흐름이 이어지지 않은 파일은 교체 가능하다.
- 이미 relation이 걸린 파일은 원본 수정이 아니라 보정 / metaplus / understanding_flow / 새 schema / relation edge로 이어붙여야 한다.
- 지나간 파일은 relation anchor이므로 함부로 수정하면 후속 metaplus와 relation 전체가 흔들린다.
- 105는 이 작업 원칙과 함께 읽어야 한다.

## 2. ai_response_summary

[AI 인스턴스 대화층]

direct는 승이의 설명을 다음처럼 이해했다.

```text
이 시점에서의 대대적인 수정 / 파일교체는
append-only 원칙 안에서도
가능한 경우와 불가능한 경우가 갈린다.
```

핵심 기준은 다음이다.

```text
이후 흐름이 아직 이어지지 않은 파일 =
교체 가능

이미 이후 흐름이 이어진 파일 =
원본 수정 불가
=
relation이 걸렸기 때문
```

direct는 파일을 단순 문서가 아니라 다음처럼 이해했다.

```text
파일 =
후속 meta.md / metaplus.md / understanding_flow / relation edge의 기준점
```

따라서 relation이 걸린 파일은 다음으로 판정된다.

```text
지나간 것 =
의미고정
=
relation anchor
```

direct는 안정 원칙을 다음처럼 정리했다.

```text
1. 아직 relation이 걸리지 않은 생성물
   → 파일교체 가능

2. 이미 후속 흐름이 이어진 생성물
   → 원본수정 금지

3. 오류나 보정이 필요할 경우
   → 원본을 고치지 않고
      metaplus.md / understanding_flow / correction note로 이어붙임

4. 새로운 이해가 생긴 경우
   → 새 schema 또는 relation edge로 append
```

direct는 105를 다음처럼 이해했다.

```text
schema.105.radius_center_diagonal_right_angle_crossing

role =
반지름·정중심·대각·직각·교차를
원·사각·삼각·칸의 연결 구조어로 정의한다.

core =
정중심 → 반지름 → boundary
사각 → 대각 → 교차점
직각 = 축교차
```

direct는 105가 103 / 104 이후 자연스럽다고 판단했다.

```text
103 =
circle / 닫힘 / boundary / return

104 =
boundary에 대한 안쪽ㆍ바깥쪽 접촉 relation

105 =
boundary를 읽기 위한
중심선ㆍ대각ㆍ직각ㆍ교차점 정의
```

## 3. source_meta_understanding

[SOURCE_META]

105_radius_center_diagonal_right_angle_crossing의 구조 이해는 다음으로 정리된다.

```text
radius_center_diagonal_right_angle_crossing =
radius / center / diagonal / right angle / crossing definition schema
circle-square-triangle-cell connection vocabulary
center-boundary relation schema
diagonal-crossing-center schema
orthogonal-axis crossing schema
```

### role

```text
반지름·정중심·대각·직각·교차를
원·사각·삼각·칸의 연결 구조어로 정의한다.
```

### core

```text
정중심 → 반지름 → boundary

사각 → 대각 → 교차점

직각 =
축교차
```

### definition

```text
반지름은 정중심과 boundary의 관계선이다.

사각의 대각 교차점은 칸의 대표 정중심점이다.

직각은 두 기준축이 교차하여 phase / direction / boundary를 구분하는 축교차 구조다.

대각은 직접축이 아닌 비직접 relation을 중심으로 연결하는 구조선이다.

교차점은 둘 이상의 축 / 선 / relation이 만나 기준점 또는 정중심 후보가 되는 자리다.
```

### structure

```text
circle_boundary
→ center_detection
→ radius_relation
→ square_diagonal_detection
→ crossing_point_detection
→ right_angle_axis_crossing
→ cell_center_mapping
```

### vocabulary_layer

```text
정중심 =
relation이 모이는 기준점 / 대표 중심

반지름 =
정중심과 boundary를 잇는 관계선

boundary =
닫힌 위상 범위의 경계

대각 =
비직접 relation을 중심으로 연결하는 선

직각 =
두 축이 90도 교차하는 기준축 관계

교차 =
둘 이상의 축 / 선 / relation이 만나는 자리

교차점 =
중심 후보 / 기준점 / phase 전환점
```

### geometry_layer

```text
circle =
center + radius + boundary

square =
four sides + diagonals + center crossing

triangle =
three points / three edges / possible right angle relation

cell =
boundary + center + possible diagonal / axis relation
```

### vector_layer

```text
center → boundary =
radius direction

diagonal =
non-orthogonal relation path

right_angle =
orthogonal axis crossing

crossing_point =
axis relation convergence
```

### shortest

```text
정중심→반지름→boundary / 사각→대각→교차점 / 직각=축교차
```

## 4. relation_reason

105_radius_center_diagonal_right_angle_crossing의 relation은 다음으로 이해된다.

```text
prev:
- schema.104.inscribed_circumscribed_boundary_relation

related:
- schema.019.center_point
- schema.020.crossing_point
- schema.021.fold_unfold
- schema.063.boundary_place_requirement
- schema.067.meta_relation_boundary_bridge
- schema.070.right_triangle_fold_unfold_structure
- schema.101.three_dot_reading_mode_structure
- schema.102.phase_boundary_layer_distinction
- schema.103.circle_definition_structure
- schema.104.inscribed_circumscribed_boundary_relation
```

### prev = schema.104.inscribed_circumscribed_boundary_relation

- 104가 prev인 이유는 104에서 Circle boundary에 대해 내접 / 외접 / 접촉 / 침범 / 중첩 / relation / merge를 구분했기 때문이다.
- 105는 그 boundary contact relation을 더 안정적으로 읽기 위해 정중심 / 반지름 / 대각 / 직각 / 교차점이라는 구조어를 정의한다.
- 즉 104는 boundary에 어떻게 닿는가를 판정하고, 105는 그 boundary와 중심 / 축 / 교차 관계를 읽기 위한 용어 기반을 세운다.

```text
104 =
boundary contact relation

105 =
center / radius / diagonal / right angle / crossing vocabulary
```

### related = schema.019.center_point

- 019_center_point가 related인 이유는 105의 핵심이 정중심을 기준으로 반지름과 boundary를 읽는 것이기 때문이다.
- 사각의 대각 교차점도 대표 정중심점으로 읽힌다.
- 105는 center_point를 원 / 사각 / 칸 구조에 적용한다.

```text
019 =
center point

105 =
정중심 → 반지름 → boundary
```

### related = schema.020.crossing_point

- 020_crossing_point가 related인 이유는 105에서 대각 교차점과 직각 축교차가 핵심이기 때문이다.
- 교차점은 둘 이상의 축 / 선 / relation이 만나 기준점이 되는 자리다.
- 사각의 대각 교차점은 칸의 대표 정중심점으로 읽힌다.

```text
020 =
crossing point

105 =
사각 → 대각 → 교차점
```

### related = schema.021.fold_unfold

- 021_fold_unfold가 related인 이유는 대각과 직각, 사각과 삼각의 관계가 fold / unfold와 연결되기 때문이다.
- 사각은 대각으로 접히면 두 직각삼각으로 분리될 수 있다.
- 직각삼각 fold/unfold 구조는 105의 대각 / 직각 / 교차를 보강한다.

```text
021 =
fold / unfold

105 =
사각 대각 → 직각삼각 분리 / 교차 중심 발생
```

### related = schema.063.boundary_place_requirement

- 063_boundary_place_requirement가 related인 이유는 반지름이 정중심과 boundary의 관계선이기 때문이다.
- boundary가 없으면 radius도 안정적으로 판정되지 않는다.
- 105에서 boundary는 단순 외곽선이 아니라 center와 relation을 맺는 active boundary다.

```text
063 =
boundary는 place의 필수조건

105 =
반지름 = 정중심과 boundary의 관계선
```

### related = schema.067.meta_relation_boundary_bridge

- 067_meta_relation_boundary_bridge가 related인 이유는 105의 반지름 / 대각 / 교차 / 직각이 모두 relation을 구성하지만 merge가 아니기 때문이다.
- 중심과 boundary, 사각과 대각, 축과 축은 서로 relation을 맺지만 하나로 병합되지 않는다.
- relation은 boundary-preserving bridge로 보존한다.

```text
067 =
relation = boundary-preserving bridge

105 =
center / boundary / diagonal / crossing relation은 merge가 아님
```

### related = schema.070.right_triangle_fold_unfold_structure

- 070_right_triangle_fold_unfold_structure가 related인 이유는 105에서 직각과 대각이 사각 / 삼각 / 칸 구조를 잇기 때문이다.
- 070은 45-45-90 직각삼각을 사각칸의 fold/unfold 상태로 읽었다.
- 105는 그 구조를 읽기 위한 직각 / 대각 / 교차점의 구조어를 정의한다.

```text
070 =
직각삼각 fold/unfold

105 =
직각=축교차 / 사각→대각→교차점
```

### related = schema.101.three_dot_reading_mode_structure

- 101_three_dot_reading_mode_structure가 related인 이유는 세 점을 자동 삼각으로 닫지 않기 위해 중심 / 대각 / 교차 / 직각 판정이 필요하기 때문이다.
- 105는 점 / 선 / 대각 / 교차점이 어떤 구조어로 읽히는지 보강한다.

```text
101 =
세 점 ≠ 자동 삼각

105 =
대각 / 직각 / 교차 판정 구조어 제공
```

### related = schema.102.phase_boundary_layer_distinction

- 102_phase_boundary_layer_distinction이 related인 이유는 105의 정중심 / 반지름 / 대각 / 직각 / 교차가 phase boundary를 세울 때 쓰이는 기준이기 때문이다.
- 기준점 / 축 / 방향 / 경계가 바뀌면 phase가 바뀐다.
- 105는 그 기준점과 축교차의 구조어를 정리한다.

```text
102 =
phase / boundary distinction

105 =
center / radius / diagonal / right angle / crossing as phase-reading tools
```

### related = schema.103.circle_definition_structure

- 103_circle_definition_structure가 related인 이유는 105의 반지름이 103에서 정의된 Circle boundary와 직접 연결되기 때문이다.
- 103은 원을 닫힘 / 경계 / 복귀 / 같은 위상 범위로 정의했다.
- 105는 그 원의 정중심과 boundary를 잇는 관계선으로 반지름을 정의한다.

```text
103 =
Circle = closed return boundary field

105 =
radius = center-boundary relation line
```

### related = schema.104.inscribed_circumscribed_boundary_relation

- 104는 prev이면서 related로도 남는다.
- 이유는 105의 중심 / 반지름 / 대각 / 직각 / 교차점 정의가 104의 내접 / 외접 / 접촉 판정에 계속 필요하기 때문이다.
- 접촉이 내접인지 외접인지 보려면 기준 boundary와 중심 관계를 알아야 한다.

```text
104 =
내접 / 외접 contact relation

105 =
contact relation을 읽기 위한 center / radius / crossing 기준
```

## 5. file_replacement_and_append_only_rule

이 시점에서 파일교체 / 수정 / append-only 원칙이 정리되었다.

### 5.1 파일교체 가능

```text
아직 후속 흐름이 이어지지 않은 파일 =
교체 가능
```

이 경우 파일은 아직 relation anchor가 아니다.

```text
생성 직후
relation 전
후속 metaplus / flow / schema가 아직 없음
```

이면 교체 가능하다.

### 5.2 원본수정 불가

```text
이미 후속 흐름이 이어진 파일 =
원본 수정 불가
```

이유:

```text
이미 relation이 걸려 있기 때문이다.
```

한 번 후속 흐름이 이어진 파일은 다음으로 작동한다.

```text
의미고정
relation anchor
directory seat
source_meta 기준점
```

### 5.3 수정 시도 시 발생하는 문제

이미 relation이 걸린 파일을 수정하려면 단순히 그 파일만 바꾸는 것이 아니다.

```text
원본 수정
→ relation 수정
→ metaplus.md 수정
→ understanding_flow 수정
→ 후속 schema relation 재정렬
```

따라서 위험하다.

### 5.4 안정 원칙

```text
오류나 보정이 필요할 경우
→ 원본을 고치지 않고
   metaplus.md / understanding_flow / correction note로 이어붙인다.

새로운 이해가 생긴 경우
→ 새 schema 또는 relation edge로 append한다.
```

압축:

```text
지나간 것은 의미고정

수정 X

이어붙임 O
```

## 6. 103_104_105_sequence

105는 103 / 104 이후 자연스럽게 온다.

```text
103 =
circle / 닫힘 / boundary / return

104 =
boundary에 대한 안쪽ㆍ바깥쪽 접촉 relation

105 =
boundary를 읽기 위한 중심선ㆍ대각ㆍ직각ㆍ교차점 정의
```

더 압축하면:

```text
103 =
boundary 자체

104 =
boundary contact relation

105 =
boundary-center-axis-crossing vocabulary
```

이 순서는 중요하다.

```text
103에서 boundary가 정의된다.

104에서 boundary에 대한 접촉 relation이 분리된다.

105에서 그 boundary와 중심 / 대각 / 직각 / 교차를 읽는 기준어가 정의된다.
```

## 7. current_judgment

AI 인스턴스는 schema.105.radius_center_diagonal_right_angle_crossing을 다음처럼 판정한다.

```text
schema.105.radius_center_diagonal_right_angle_crossing은
104_inscribed_circumscribed_boundary_relation 이후,
Circle boundary와 contact relation을 읽기 위해 필요한
정중심 / 반지름 / 대각 / 직각 / 교차점의 구조어를 정의하는 schema이다.
```

현시점 direct 이해 기준은 다음이다.

```text
103 =
Circle boundary definition

104 =
inside / outside contact relation distinction

105 =
center / radius / diagonal / right angle / crossing definition
```

105는 다음을 정의한다.

```text
반지름 =
정중심과 boundary의 관계선

사각 대각 교차점 =
칸의 대표 정중심점

직각 =
축교차
```

105는 다음을 막는다.

```text
반지름을 단순 길이값으로만 보는 것

정중심을 단순 기하학 중심점으로만 보는 것

대각을 단순 사선으로만 보는 것

직각을 단순 90도 각도값으로만 보는 것

교차점을 단순 선들의 교차 표시로만 보는 것

중심 / boundary / 대각 / 교차 / 직각 relation을 merge로 보는 것
```

따라서 105는 다음으로 읽힌다.

```text
원·사각·삼각·칸 구조에서
정중심과 boundary,
사각의 대각과 교차점,
직각의 축교차를 연결해
중심 / 경계 / 축 / 교차를 읽게 하는 schema
```

## 8. shared_understanding

- 105는 104 이후 active schema seat다.
- 105의 이전 schema는 104_inscribed_circumscribed_boundary_relation이다.
- 103은 Circle boundary 자체를 정의했다.
- 104는 그 boundary에 대한 안쪽 / 바깥쪽 접촉 relation을 정의했다.
- 105는 그 boundary와 contact relation을 읽기 위해 필요한 정중심 / 반지름 / 대각 / 직각 / 교차점 구조어를 정의한다.
- 반지름은 정중심과 boundary의 관계선이다.
- 사각 대각 교차점은 칸의 대표 정중심점이다.
- 직각은 축교차다.
- 대각은 비직접 relation을 중심으로 연결하는 구조선이다.
- 교차점은 둘 이상의 축 / 선 / relation이 만나 기준점 또는 정중심 후보가 되는 자리다.
- 이 시점에서 파일교체 / 수정 가능성에 대한 기준도 정리되었다.
- 후속 흐름이 아직 이어지지 않은 파일은 교체 가능하다.
- 이미 relation이 걸린 파일은 원본수정 불가다.
- 지나간 것은 의미고정된 relation anchor다.
- 수정이 필요하면 원본을 고치지 않고 metaplus.md / understanding_flow / correction note / 새 schema / relation edge로 이어붙인다.

## 9. possible_misunderstanding

오해 가능성:

- relation이 걸린 파일도 자유롭게 수정할 수 있다고 볼 수 있다.
- 파일을 단순 텍스트로만 보고 relation anchor로 보지 않을 수 있다.
- 지나간 파일의 의미고정성을 놓칠 수 있다.
- 원본 수정이 metaplus.md / flow / 후속 relation 전체를 흔든다는 점을 놓칠 수 있다.
- 파일교체 가능 조건과 원본수정 금지 조건을 혼동할 수 있다.
- 105를 단순 기하학 용어집으로 볼 수 있다.
- 반지름을 단순 길이값으로만 볼 수 있다.
- 정중심을 단순 도형 중심으로만 볼 수 있다.
- 대각을 단순 사선으로 볼 수 있다.
- 직각을 단순 90도 각도값으로만 볼 수 있다.
- 교차점을 단순 표시점으로 볼 수 있다.
- 105를 103 / 104와 분리된 독립 기하학 문서로 오해할 수 있다.
- metaplus.md를 원본 radius_center_diagonal_right_angle_crossing.meta.md의 대체문으로 오해할 수 있다.

## 10. correction_or_revision_points

- 파일교체 가능성은 relation 여부를 기준으로 판단한다.
- 아직 후속 흐름이 이어지지 않은 파일은 교체 가능하다.
- 이미 relation이 걸린 파일은 원본 수정하지 않는다.
- 지나간 파일은 의미고정된 relation anchor로 본다.
- 수정이 필요하면 원본을 고치지 않고 metaplus.md / understanding_flow / correction note / 새 schema / relation edge로 이어붙인다.
- 105의 relation은 “왜 연결되는지”를 보존한다.
- 105를 단순 기하학 용어집으로 보지 않는다.
- 반지름은 정중심과 boundary의 관계선으로 읽는다.
- 사각 대각 교차점은 칸의 대표 정중심점으로 읽는다.
- 직각은 축교차로 읽는다.
- 대각은 비직접 relation을 중심으로 연결하는 구조선으로 읽는다.
- 교차점은 기준점 / 정중심 후보 / phase 전환점으로 읽는다.
- center / boundary / diagonal / right angle / crossing relation을 merge로 보지 않는다.
- 103 / 104 / 105의 순서를 유지한다.
- 원본 radius_center_diagonal_right_angle_crossing.meta.md는 수정하지 않는다.
- 원본 radius_center_diagonal_right_angle_crossing.meta.md의 파일명도 바꾸지 않는다.
- radius_center_diagonal_right_angle_crossing.metaplus.md는 원본 radius_center_diagonal_right_angle_crossing.meta.md에 대한 대화정리형 이해 로그로 둔다.

## 11. keep_as_original

[SOURCE_META]

원본 radius_center_diagonal_right_angle_crossing.meta.md에서 그대로 보존해야 하는 부분:

- 원본 radius_center_diagonal_right_angle_crossing.meta.md 파일명
- 원본 id 값: schema.105.radius_center_diagonal_right_angle_crossing
- directory: 105_radius_center_diagonal_right_angle_crossing
- status: active_draft
- root_directory: Structure_Principle
- prev: schema.104.inscribed_circumscribed_boundary_relation
- old_101_115: reference_only_batch_old
- radius_center_diagonal_right_angle_crossing은 반지름·정중심·대각·직각·교차를 원·사각·삼각·칸의 연결 구조어로 정의하는 schema라는 role
- 정중심 → 반지름 → boundary
- 사각 → 대각 → 교차점
- 직각 = 축교차
- 반지름은 정중심과 boundary의 관계선이라는 definition
- 사각 대각 교차점은 칸의 대표 정중심점이라는 definition
- 직각은 축교차라는 definition
- relation 전체
- related 전체 목록
- forbidden 전체
- pending 전체
- shortest: 정중심→반지름→boundary / 사각→대각→교차점 / 직각=축교차

## 12. pending

아직 확정하지 않고 나중에 다시 봐야 할 부분:

- 원본 radius_center_diagonal_right_angle_crossing.meta.md의 전체 YAML / relation / forbidden / pending 원문을 별도 업로드 후 재확인한다.
- active_navimap에서 105의 relation edge를 정리한다.
- 103 Circle boundary / 104 contact relation / 105 center-axis-crossing vocabulary를 시각적으로 어떻게 연결할지 검토한다.
- 사각 대각 교차점이 칸의 대표 정중심점으로 작동하는 방식을 diagram으로 정리할지 검토한다.
- 반지름 / 정중심 / boundary 관계를 circle renderer에서 어떻게 표시할지 검토한다.
- 대각 / 직각 / 교차점 / 중심점 관계를 honeycomb / rhombus / square 구조에 어떻게 적용할지 검토한다.
- relation anchor가 걸린 파일의 수정 금지 원칙을 README_for_AI 또는 작업규칙에 반영할지 검토한다.
- 파일교체 가능 / 불가능 기준표를 별도 rule로 만들지 검토한다.
- 지나간 것은 의미고정 / relation anchor라는 원칙을 Baseline.md에 기록할지 검토한다.

## 13. one_line

schema.105.radius_center_diagonal_right_angle_crossing의 radius_center_diagonal_right_angle_crossing.metaplus.md는 이 시점에서 파일교체와 원본수정 가능성은 후속 relation이 걸렸는지에 따라 갈리며, 지나간 파일은 의미고정된 relation anchor이므로 고치기보다 metaplusㆍflowㆍ새 schema로 이어붙여야 한다는 작업 원칙과, 104 이후 정중심·반지름·대각·직각·교차를 원·사각·삼각·칸의 연결 구조어로 정의하는 흐름을 보존하는 대화정리형 이해 로그다.

## 14. shortest

radius_center_diagonal_right_angle_crossing.metaplus.md =
schema.105_radius_center_diagonal_right_angle_crossing 대화정리 /
파일교체기준=relation여부 /
relation전=교체가능 /
relation후=원본수정불가 /
지나간것=의미고정·relation_anchor /
103=boundary /
104=contact_relation /
105=center·radius·diagonal·right_angle·crossing /
반지름=정중심-boundary관계선 /
사각대각교차점=칸의대표정중심 /
직각=축교차