---
id: schema.121.coredot_ambiguity_boundary
type: active_schema_metadata
filename: coredot_ambiguity_boundary.meta.md
directory: 121_coredot_ambiguity_boundary
status: active_draft
prev: schema.120.pending
layer: Schema
---

# META: coredot_ambiguity_boundary

## role

`coredot_ambiguity_boundary`는 `Core`, `Coremap`, `dot`, `ㆍ`, `coredot/CoreDot` 사이의 의미 혼용을 막기 위한 boundary schema이다.

이 meta 파일은 `CoreDot`을 새 핵심 용어로 확정하는 문서가 아니다.

오히려 이 문서는 `CoreDot`이라는 용어가 현시점에서 모호하므로, 기존 `000_dot/dot.meta.md`에 섞어 넣지 않고 별도 schema.121에서 보류·경계·검산 대상으로 둔다.

---

## core

```txt
Core = 사용 가능 후보
Coremap = 사용 가능 후보
CoreDot = 모호함
dot = 기존 schema.000.dot에서 보존
ㆍ = 문맥별 작동점
```

```txt
CoreDot을 000_dot에 병합하지 않는다.
CoreDot을 dot의 본명으로 쓰지 않는다.
CoreDot은 schema.121에서 모호성 경계 대상으로 둔다.
```

---

## definition

`CoreDot`은 현시점에서 다음 이유로 모호하다.

```txt
1. dot과 Core가 합쳐져 dot의 원래 정의를 덮을 위험이 있다.
2. ㆍ의 여러 문맥 역할을 하나의 이름으로 고정할 위험이 있다.
3. Coremap의 Core와 schema.000.dot의 dot을 잘못 병합할 위험이 있다.
4. Core가 구조핵인지, 중심인지, 평형점인지, 구심점인지 불명확해질 수 있다.
5. dot은 이미 schema.000.dot에서 최초 최소 자리로 정의되어 있다.
```

따라서 `CoreDot`은 현시점에서 active core term이 아니라, ambiguity boundary term으로 보존한다.

---

## distinction

### dot

```txt
dot =
최초 최소 자리
값이 아니라 자리
선 / 벡터 / 수열구조 / 자리연산이 시작되는 최소 구조 단위
```

dot은 schema.000.dot에서 보존한다.

dot은 line이 아니다.

dot은 CoreDot으로 재명명하지 않는다.

---

### ㆍ

```txt
ㆍ =
문맥별 작동점
방향 발생점 후보
끌림점 후보
공전 방향점 후보
relation marker 후보
천지인 문맥의 점 후보
```

ㆍ은 하나의 이름으로 고정하지 않는다.

ㆍ은 `CoreDot`으로 고정하지 않는다.

---

### Core

```txt
Core =
구조핵
boundary 안에서 pull / relation / density / axis-cross가 응집한 내부 작동핵
```

Core는 사용할 수 있다.

다만 Core는 dot이 아니다.

Core는 구조핵이고, dot은 최소 자리이다.

---

### Coremap

```txt
Coremap =
Core들의 관계지도
구조핵들이 relation / boundary / axis / flow / return 기준으로 배열된 구조지도
```

Coremap은 사용할 수 있다.

Coremap은 dot 정의문서가 아니다.

Coremap은 /main 계열의 상위 구조지도 문서로 둔다.

---

### CoreDot

```txt
CoreDot =
현시점 모호한 합성어
Core와 dot의 boundary를 흐릴 위험이 있는 표현
```

CoreDot은 지금 사용하지 않는다.

CoreDot은 schema.121에서 모호성 검산 대상으로 둔다.

---

## why_separate_schema

CoreDot을 000_dot에 넣지 않는 이유는 다음이다.

```txt
000_dot
= 최초 dot 이해 보존

121_coredot_ambiguity_boundary
= CoreDot 용어가 왜 모호한지 보존
= dot / Core / ㆍ / Coremap의 boundary를 지킴
```

즉 121은 새로운 dot 정의가 아니다.

121은 용어 혼용을 막는 boundary schema이다.

---

## relation_to_000_dot

schema.000.dot은 보존한다.

```txt
schema.000.dot
= dot의 최초 최소 자리 정의
```

121은 000을 수정하지 않는다.

121은 000에 후속으로 덮어쓰기 하지 않는다.

121은 다음만 수행한다.

```txt
CoreDot을 dot에 병합하지 말 것
CoreDot을 ㆍ의 이름으로 고정하지 말 것
Core와 dot의 층위를 구분할 것
```

---

## relation_to_coremap

Coremap은 사용할 수 있다.

Coremap은 다음을 의미한다.

```txt
Coremap =
Core들의 relation map
```

하지만 Coremap이 존재한다고 해서 CoreDot을 자동 생성하지 않는다.

```txt
Coremap O
Core O
CoreDot 보류
```

---

## relation_to_renderer

Renderer.md는 객체의 relation-structure.md이다.

Renderer.md 안에서 Coremap을 사용할 수 있다.

하지만 Renderer.md 안에서 dot을 CoreDot으로 바꾸면 안 된다.

안정 표현은 다음이다.

```txt
dot = minimal place / anchor
Core = structural core
Coremap = relation map of cores
```

불안정 표현은 다음이다.

```txt
CoreDot = dot의 본명
CoreDot = ㆍ의 정체
CoreDot = Coremap의 최소 단위
```

---

## ambiguity_reason

CoreDot이 모호한 이유는 다음이다.

```txt
Core + Dot
```

이라는 합성은 좋아 보이지만, 두 단어가 가진 층위가 다르다.

```txt
Core =
응집된 구조핵

dot =
최소 자리 / 발생점 / anchor
```

둘이 만날 수는 있다.

하지만 만나면 곧바로 하나의 단어로 고정되는 것은 아니다.

따라서 더 정확한 표현은 경우별로 나눈다.

```txt
dot acting as core
core-like dot behavior
dot as structural anchor
dot in core position
```

그러나 이것도 아직 용어 lock 대상은 아니다.

---

## forbidden

```txt
CoreDot을 000_dot/dot.meta.md에 병합하지 않는다.
CoreDot을 dot의 최종 이름으로 쓰지 않는다.
CoreDot을 ㆍ의 정체로 고정하지 않는다.
Core와 dot을 동일시하지 않는다.
Coremap의 Core와 schema.000.dot의 dot을 섞지 않는다.
dot을 line으로 보지 않는다.
dot과 ㅇ을 동일시하지 않는다.
ㆍ과 ㅇ을 동일시하지 않는다.
CoreDot을 Renderer.md의 필수 단위로 쓰지 않는다.
모호한 합성어를 원리 객체로 과잉 승격하지 않는다.
```

---

## pending

```txt
1. Core 용어는 /main/Coremap.meta.md에서 계속 검토한다.
2. dot은 schema.000.dot에서 보존한다.
3. ㆍ의 문맥별 작동은 후속 schema 또는 relation index에서 분리한다.
4. CoreDot이라는 용어는 현시점 사용하지 않는다.
5. 필요하다면 후속에서 “dot_in_core_position” 같은 더 명확한 표현을 검토한다.
```

---

## current_judgment

CoreDot은 현시점에서 모호하다.

Core와 Coremap은 사용할 수 있다.

dot은 schema.000.dot에서 보존한다.

ㆍ은 문맥별 작동점으로 분석한다.

CoreDot은 이들 사이의 boundary를 흐릴 위험이 있으므로, schema.121에서 모호성 경계 대상으로 보존하고 본류 용어로 사용하지 않는다.

---

## one_line

schema.121.coredot_ambiguity_boundary는 CoreDot이라는 합성어가 dot, ㆍ, Core, Coremap의 boundary를 흐릴 수 있으므로 이를 본류 용어로 쓰지 않고 모호성 검산 대상으로 분리 보존하는 schema이다.

---

## shortest

```txt
Core O
Coremap O
CoreDot 보류
dot은 000에서 보존
ㆍ은 문맥별 분석
```
