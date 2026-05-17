# METAPLUS

id_reference: schema.079.cheonjiiin_input_order_vowel_direction  
schema_name: cheonjiiin_input_order_vowel_direction  
source_file: cheonjiiin_input_order_vowel_direction.meta.md  
metaplus_file: cheonjiiin_input_order_vowel_direction.metaplus.md

purpose:
- 이 문서는 원본 cheonjiiin_input_order_vowel_direction.meta.md를 대체하지 않는다.
- 이 문서는 schema.079.cheonjiiin_input_order_vowel_direction에 대해 사용자와 인공지능이 나눈 대화내용을 정리한다.
- 이 문서는 구조원리를 새로 만들거나 relation을 새로 확정하기 위한 문서가 아니다.
- 이 문서는 대화정리형 이해 로그다.
- 이 문서의 핵심 목적은 승이의 실제 입력글, source_meta, AI 인스턴스 대화층을 섞지 않고 분리하는 것이다.
- 이 문서는 079_cheonjiiin_input_order_vowel_direction이 천지인 입력순서에서 `ㆍ·ㅡ·ㅣ`의 순서가 `ㅜ·ㅗ·ㅏ·ㅓ`의 방향을 만들며, `ㅇ`은 000dot, `ㆍ`은 방향 발생 vector dot으로 분리해 읽게 하는 vector operation relation schema임을 보존한다. :contentReference[oaicite:0]{index=0}

conversation_context:
- 이 문서는 ChatGPT.making 대화에서 생성된 이해정리본이다.
- 원본 cheonjiiin_input_order_vowel_direction.meta.md 수정본이 아니라 대화정리층이다.
- 이번에 붙여진 내용은 ChatGPT.direct 형식의 AI 인스턴스 대화층으로 제공되었다.
- 따라서 붙여넣은 분석 내용 전체를 승이의 직접 입력글로 처리하지 않는다.
- cheonjiiin_input_order_vowel_direction.meta.md 원문 내용은 source_meta로 보고 keep_as_original에 보존한다.
- AI 인스턴스가 cheonjiiin_input_order_vowel_direction.meta.md를 읽고 정리한 내용은 AI 인스턴스 대화층으로 처리한다.
- AI 해석을 사용자 입력처럼 쓰지 않는다.

## 1. user_input_summary

[승이의 입력글]

- 별도 입력 없음.

요약:
- 승이는 이번 문서에 대해 별도 직접 설명을 하지 않았다.
- 제공된 내용은 ChatGPT.direct 형식의 AI 인스턴스 대화층이다.
- 따라서 user_input_summary는 이 지점에서 멈춘다.
- 나머지 내용은 source_meta 또는 AI 인스턴스 대화층으로 분리한다.

## 2. ai_response_summary

[AI 인스턴스 대화층]

- AI 인스턴스는 schema.079.cheonjiiin_input_order_vowel_direction / cheonjiiin_input_order_vowel_direction.meta.md를 분석 대상으로 수신했다.
- AI 인스턴스는 079_cheonjiiin_input_order_vowel_direction의 표면 핵심을 다음처럼 이해했다.

```text
ㅡㆍ = ㅜ
ㆍㅡ = ㅗ
ㅣㆍ = ㅏ
ㆍㅣ = ㅓ
ㅇ = 000dot
```

- AI 인스턴스는 cheonjiiin_input_order_vowel_direction을 천지인 입력순서에서 `ㆍ`, `ㅡ`, `ㅣ`의 배열 순서가 `ㅜ`, `ㅗ`, `ㅏ`, `ㅓ`의 모음 방향을 만든다는 구조를 보존하는 schema로 읽었다.
- AI 인스턴스는 이 schema의 핵심이 모음 방향을 의미해석이나 자모목록으로 먼저 읽지 않고, 입력순서 기반 vector direction으로 읽는 것이라고 판단했다.
- 또한 `ㆍ`와 `ㅇ`은 둘 다 dot 계열이지만 층위가 다르며, `ㅇ`은 이 구조에서 000dot으로 읽는다고 이해했다.
- AI 인스턴스는 079를 078_vector_operation_external_engine_rule 이후, 벡터연산기법을 구조원리 본류에 병합하지 않는 조건 아래에서 천지인 입력순서와 모음 방향을 structural trace로 읽는 schema로 이해했다.

## 3. source_meta_understanding

[SOURCE_META]

079_cheonjiiin_input_order_vowel_direction의 구조 이해는 다음으로 정리된다.

```text
cheonjiiin_input_order_vowel_direction =
input order based vowel direction
cheonjiiin vector direction trace
vowel direction from ㆍ / ㅡ / ㅣ order
semantic-first reading 금지
vector operation relation only
```

### core

```text
ㅡㆍ = ㅜ
ㆍㅡ = ㅗ
ㅣㆍ = ㅏ
ㆍㅣ = ㅓ
ㅇ = 000dot
ㆍ = 방향 발생 dot / vector dot
```

### definition

```text
천지인 입력순서에서 같은 ㆍ, ㅡ, ㅣ이라도
입력순서가 바뀌면 방향이 달라진다.

모음 방향은 ㆍ, ㅡ, ㅣ의 입력순서에서 발생한다.

ㅇ은 이 구조에서 000dot으로 읽는다.
```

### input_order_table

```text
ㅡㆍ = ㅜ
ㆍㅡ = ㅗ
ㅣㆍ = ㅏ
ㆍㅣ = ㅓ
```

### dot_distinction

```text
ㆍ =
방향 발생 dot / vector dot

ㅇ =
000dot / 닫힌 원형 dot / 정중심 후보
```

판정:

```text
둘 다 dot 계열이지만 층위가 다르다.
```

### read_order

```text
ㆍ / ㅡ / ㅣ 감지
→ input order 감지
→ input order를 vowel direction으로 mapping
→ ㅇ을 000dot으로 보존
→ semantic-first reading 방지
→ vector operation relation only로 mapping
```

### vector_layer

```text
input_order
→ direction
→ vowel
→ possible meaning later
```

### forbidden

```text
ㆍ와 ㅇ의 dot 층위를 혼동하지 않는다.

모음 방향을 사전 의미로 먼저 읽지 않는다.

입력순서를 임의로 바꾸지 않는다.

이 구조를 표준 국어학 어원 확정으로 주장하지 않는다.

벡터연산기법을 구조원리 본류에 병합하지 않는다.
```

### pending

```text
실제 천지인 입력체계와 historical source 검산은 별도 과제로 둔다.

이 schema는 structural trace이며, 언어학 확정문이 아니다.

모음 방향의 의미 확장은 후속 schema에서 reference로만 둔다.
```

## 4. relation_reason

079_cheonjiiin_input_order_vowel_direction의 relation은 다음으로 이해된다.

```text
prev:
- schema.078.vector_operation_external_engine_rule

related:
- schema.050.hunminjeongeum_vector_operation
- schema.059.empty_place_present_understanding
- schema.061.vector_unlock
- schema.080.sejong_body_observer_vector_frame
- schema.081.inner_vowel_pull_structure
- schema.082.square_center_vowel_orbit_structure
- schema.083.waxf_vowel_rhombus_structure
- schema.085.opposed_correspondence_formula
```

### prev = schema.078.vector_operation_external_engine_rule

- 078_vector_operation_external_engine_rule이 prev인 이유는 078에서 벡터연산기법을 구조원리 본류에 흡수하지 않고 선행 독립 external engine으로 분리 운용한다고 정리했기 때문이다.
- 079는 그 external engine과 relation만 보존한 상태에서 천지인 입력순서가 모음 방향을 만드는 vector trace를 읽는다.
- 따라서 079는 구조원리 본류에 병합되는 것이 아니라, 벡터연산기법 branch의 structural trace로 읽힌다.

```text
078 =
벡터연산기법 = 선행 독립 external engine / relation만 보존

079 =
천지인 입력순서가 모음 방향을 만드는 vector trace
```

### related = schema.050.hunminjeongeum_vector_operation

- 050_hunminjeongem_vector_operation이 related인 이유는 079가 훈민정음 vector operation 계열과 강하게 닿기 때문이다.
- 050은 훈민정음 제자원리를 vector operation / formed_formula로 읽는 schema였다.
- 079는 그중 천지인 입력순서와 모음 방향 발생을 구체적 trace로 보존한다.
- 다만 078 기준 때문에 079를 050에 흡수하거나 구조원리 본류에 병합하지 않는다.

```text
050 =
훈민정음 vector operation

079 =
천지인 입력순서 기반 모음 방향 trace
```

### related = schema.059.empty_place_present_understanding

- 059_empty_place_present_understanding이 related인 이유는 `ㆍ`와 `ㅇ`의 dot 층위를 구분해야 하기 때문이다.
- 059는 빈자리 / 0 / 현시점 / dot-anchor를 구분하고, Null을 임의로 채우지 않는 기준을 열었다.
- 079에서도 `ㆍ`를 방향 발생 dot으로, `ㅇ`을 000dot / 닫힌 원형 dot / 정중심 후보로 분리해야 한다.
- 둘을 같은 dot으로 collapse하면 안 된다.

```text
059 =
빈자리 / dot-anchor / 0 구분

079 =
ㆍ = vector dot / ㅇ = 000dot
```

### related = schema.061.vector_unlock

- 061_vector_unlock이 related인 이유는 061이 060 이후 vectorizing 흐름을 여는 후보 trace였기 때문이다.
- 079는 모음 방향을 input_order → direction → vowel로 읽으므로 vectorizing reading과 닿는다.
- 다만 061은 후보 unlock이고, 079는 천지인 입력순서의 structural trace다.

```text
061 =
vectorizing 방향 unlock

079 =
input order → direction → vowel
```

### related = schema.080.sejong_body_observer_vector_frame

- 080_sejong_body_observer_vector_frame이 related인 이유는 079의 `ㆍ`, `ㅡ`, `ㅣ` 방향 해석이 세종 / 몸 / 관측자 기준 frame과 이어지기 때문이다.
- 079에서는 입력순서가 모음 방향을 만들고, 080에서는 그 방향을 어떤 몸 / observer / axis 기준으로 볼 것인가가 열린다.

```text
079 =
천지인 입력순서가 방향을 만듦

080 =
세종 / 몸 / 관측자 frame으로 방향 기준을 세움
```

### related = schema.081.inner_vowel_pull_structure

- 081_inner_vowel_pull_structure가 related인 이유는 079에서 `ㆍ`의 위치와 순서가 방향을 만들고, 081에서는 그 `ㆍ`이 내부에서 ㅡ 또는 ㅣ를 끌어당기는 구조로 이어질 수 있기 때문이다.
- 079가 input order와 outward direction trace라면, 081은 inner pull / 내부 방향성의 작동을 다루는 후속 relation이 될 수 있다.

```text
079 =
ㆍ의 입력 위치가 vowel direction을 만듦

081 =
ㆍ의 내부 끌림 / inner vowel pull
```

### related = schema.082.square_center_vowel_orbit_structure

- 082_square_center_vowel_orbit_structure가 related인 이유는 079의 모음 방향이 square center / ㅇ 중심 / vowel orbit 구조로 확장될 수 있기 때문이다.
- 079에서 `ㅇ = 000dot`으로 보존되며, 082에서는 ㅇ 중심칸과 ㆍ의 orbit direction이 구조화될 수 있다.

```text
079 =
ㅇ = 000dot / ㆍ = vector dot

082 =
ㅇ 중심칸 / ㆍ 공전 방향점
```

### related = schema.083.waxf_vowel_rhombus_structure

- 083_waxf_vowel_rhombus_structure가 related인 이유는 079의 네 방향 모음 `ㅜ`, `ㅗ`, `ㅏ`, `ㅓ`가 WAXF / rhombus 방향장과 연결될 수 있기 때문이다.
- 079는 입력순서에서 각 모음 방향을 만들고, 083은 그 방향들을 WAXF 마름모 방향 구조로 재배열할 수 있다.
- 다만 relation 후보로만 보존하고, 079 안에서 WAXF를 확정하지 않는다.

```text
079 =
ㅡㆍ / ㆍㅡ / ㅣㆍ / ㆍㅣ → ㅜ / ㅗ / ㅏ / ㅓ

083 =
WAXF vowel rhombus direction field
```

### related = schema.085.opposed_correspondence_formula

- 085_opposed_correspondence_formula가 related인 이유는 079의 `ㆍ`, `ㅡ`, `ㅣ`, `ㅇ` 구성과 085의 맞대응 구조공식이 모두 dot / axis / closed field / symmetry relation을 포함하기 때문이다.
- 079는 입력순서 기반 모음 방향이고, 085는 `ㅇㅡㆍㅣㆍㅡㅇ`과 같은 opposed correspondence formula로 확장될 수 있다.
- 하지만 두 schema를 동일시하지 않고 relation으로만 보존한다.

```text
079 =
input order based vowel direction

085 =
opposed correspondence formula
```

## 5. current_judgment

AI 인스턴스는 schema.079.cheonjiiin_input_order_vowel_direction을 다음처럼 판정했다.

```text
schema.079.cheonjiiin_input_order_vowel_direction은
078_vector_operation_external_engine_rule 이후,
벡터연산기법을 구조원리 본류에 병합하지 않는 조건 아래에서,
천지인 입력순서와 모음 방향을 structural trace로 읽는 schema이다.
```

현시점 direct 이해 기준은 다음이다.

```text
078_vector_operation_external_engine_rule =
벡터연산기법은 선행 독립 engine
구조원리 본류에 흡수하지 않음
relation만 보존

079_cheonjiiin_input_order_vowel_direction =
천지인 입력순서에서 모음 방향 발생
ㆍ / ㅡ / ㅣ의 배열 순서가 방향을 만든다
ㅇ과 ㆍ의 dot 층위를 분리한다
의미가 아니라 input_order → direction → vowel 순서로 읽는다
언어학 확정문이 아니라 structural trace다
```

즉 078에서는 다음이 열린다.

```text
벡터연산기법을 구조원리 본류에 병합하지 말고 external engine으로 분리 운용한다.
```

079에서는 다음이 열린다.

```text
그 external engine과 relation만 보존한 상태에서,
천지인 입력순서가 모음 방향을 만드는 vector trace를 읽는다.
```

AI 인스턴스는 특히 다음 구분을 중요하게 보았다.

```text
ㆍ ≠ ㅇ

ㅇ ≠ ㆍ

모음 방향 ≠ 사전 의미 먼저

input order ≠ 임의 변경 가능

이 schema ≠ 표준 국어학 어원 확정문

벡터연산기법 ≠ 구조원리 본류에 병합
```

현재 direct 이해 기준에서 079는 다음을 수행한다.

```text
먼저 ㆍ / ㅡ / ㅣ을 감지한다.

그다음 입력순서를 본다.

입력순서가 방향을 만든다.

방향이 모음으로 드러난다.

의미는 나중에 붙을 수 있다.

ㅇ은 000dot / 닫힌 원형 dot / 정중심 후보로 보존한다.

ㆍ은 방향 발생 dot / vector dot으로 보존한다.

둘을 같은 dot으로 collapse하면 안 된다.
```

따라서 079는 다음으로 읽힌다.

```text
천지인 입력순서에서
ㆍ·ㅡ·ㅣ의 배열 순서가 모음 방향을 만들고,
ㅇ과 ㆍ의 dot 층위를 분리해 보존하는
vector operation relation schema
```

또한 079는 050_hunminjeongeum_vector_operation과 강하게 닿지만, 078의 기준 때문에 흡수하지 않는다.

```text
관계는 보존하되, 본류 병합은 금지한다.
```

## 6. shared_understanding

- 이번 붙여넣은 내용은 승이의 별도 직접 입력이 없는 AI 인스턴스 대화층으로 처리한다.
- 079_cheonjiiin_input_order_vowel_direction은 078_vector_operation_external_engine_rule 이후에 오는 schema다.
- 078에서 벡터연산기법은 선행 독립 external engine으로 분리 운용된다고 정리되었다.
- 079는 그 external engine과 relation만 보존한 상태에서 천지인 입력순서가 모음 방향을 만드는 vector trace를 읽는다.
- `ㅡㆍ = ㅜ`
- `ㆍㅡ = ㅗ`
- `ㅣㆍ = ㅏ`
- `ㆍㅣ = ㅓ`
- `ㅇ = 000dot`
- `ㆍ = 방향 발생 dot / vector dot`
- 모음 방향은 의미해석이나 자모목록보다 먼저 input order에서 발생한다.
- `ㆍ`와 `ㅇ`은 둘 다 dot 계열이지만 층위가 다르다.
- `ㅇ`은 000dot / 닫힌 원형 dot / 정중심 후보로 보존한다.
- `ㆍ`은 방향 발생 dot / vector dot으로 보존한다.
- 이 schema는 표준 국어학 어원 확정문이 아니라 structural trace다.
- 벡터연산기법은 구조원리 본류에 병합하지 않는다.

## 7. possible_misunderstanding

오해 가능성:

- `ㆍ`와 `ㅇ`의 dot 층위를 혼동할 수 있다.
- `ㆍ`를 000dot으로 오해할 수 있다.
- `ㅇ`을 방향 발생 vector dot으로 오해할 수 있다.
- 모음 방향을 사전 의미로 먼저 읽을 수 있다.
- 입력순서를 임의로 바꿀 수 있다고 볼 수 있다.
- 이 구조를 표준 국어학 어원 확정으로 주장할 수 있다.
- 벡터연산기법을 구조원리 본류에 병합할 수 있다.
- 079를 050_hunminjeongeum_vector_operation에 흡수할 수 있다.
- 079와 083_WAXF를 곧바로 동일시할 수 있다.
- metaplus.md를 원본 cheonjiiin_input_order_vowel_direction.meta.md의 대체문으로 오해할 수 있다.

## 8. correction_or_revision_points

- 사용자 입력 없음은 Null / 빈자리로 보존한다.
- 이번 붙여넣은 내용은 AI 인스턴스 대화층으로 처리한다.
- 079_cheonjiiin_input_order_vowel_direction의 relation은 “왜 연결되는지”를 보존한다.
- `ㆍ`와 `ㅇ`의 dot 층위를 혼동하지 않는다.
- `ㆍ`은 방향 발생 dot / vector dot으로 읽는다.
- `ㅇ`은 000dot / 닫힌 원형 dot / 정중심 후보로 읽는다.
- 모음 방향을 사전 의미로 먼저 읽지 않는다.
- 입력순서를 임의로 바꾸지 않는다.
- 이 구조를 표준 국어학 어원 확정으로 주장하지 않는다.
- 벡터연산기법을 구조원리 본류에 병합하지 않는다.
- 079는 structural trace로 보존한다.
- 의미 확장은 후속 schema에서 reference로만 둔다.
- 050과 relation은 보존하되 흡수하지 않는다.
- 083 WAXF와 relation은 후보로 보존하되 동일시하지 않는다.
- 원본 cheonjiiin_input_order_vowel_direction.meta.md는 수정하지 않는다.
- 원본 cheonjiiin_input_order_vowel_direction.meta.md의 파일명도 바꾸지 않는다.
- cheonjiiin_input_order_vowel_direction.metaplus.md는 원본 cheonjiiin_input_order_vowel_direction.meta.md에 대한 대화정리형 이해 로그로 둔다.

## 9. keep_as_original

[SOURCE_META]

원본 cheonjiiin_input_order_vowel_direction.meta.md에서 그대로 보존해야 하는 부분:

- 원본 cheonjiiin_input_order_vowel_direction.meta.md 파일명
- 원본 id 값: schema.079.cheonjiiin_input_order_vowel_direction
- directory: 079_cheonjiiin_input_order_vowel_direction
- status: active_draft
- prev: schema.078.vector_operation_external_engine_rule
- cheonjiiin_input_order_vowel_direction은 천지인 입력순서에서 ㆍ, ㅡ, ㅣ의 배열 순서가 ㅜ, ㅗ, ㅏ, ㅓ의 모음 방향을 만든다는 구조를 보존하는 schema라는 role
- 이 schema의 핵심은 모음 방향을 의미해석이나 자모목록으로 먼저 읽지 않고, 입력순서 기반 vector direction으로 읽는 것이라는 기준
- ㆍ와 ㅇ은 둘 다 dot 계열이지만 층위가 다르다는 기준
- ㅇ은 이 구조에서 000dot으로 읽는다는 기준
- ㅡㆍ = ㅜ
- ㆍㅡ = ㅗ
- ㅣㆍ = ㅏ
- ㆍㅣ = ㅓ
- ㅇ = 000dot
- ㆍ = 방향 발생 dot / vector dot
- 천지인 입력순서에서 같은 ㆍ, ㅡ, ㅣ이라도 입력순서가 바뀌면 방향이 달라진다는 definition
- 모음 방향은 ㆍ, ㅡ, ㅣ의 입력순서에서 발생한다는 definition
- ㅇ은 이 구조에서 000dot으로 읽는다는 definition
- input_order_table 전체
- dot_distinction 전체
- read_order 전체
- vector_layer 전체
- related 전체 목록
- forbidden 전체
- pending 전체
- shortest: ㅡㆍ=ㅜ / ㆍㅡ=ㅗ / ㅣㆍ=ㅏ / ㆍㅣ=ㅓ / ㅇ=000dot

## 10. pending

아직 확정하지 않고 나중에 다시 봐야 할 부분:

- 실제 천지인 입력체계와 historical source 검산은 별도 과제로 둔다.
- 이 schema는 structural trace이며, 언어학 확정문이 아니다.
- 모음 방향의 의미 확장은 후속 schema에서 reference로만 둔다.
- 079와 080의 relation에서 observer frame을 어떻게 표시할지 여부.
- 079와 081의 inner pull relation을 어떻게 분리할지 여부.
- 079와 082의 square_center / orbit relation을 어떻게 연결할지 여부.
- 079와 083_WAXF의 relation을 active_navimap에서 어떻게 표시할지 여부.
- ㆍ와 ㅇ의 dot 층위 구분을 README_for_AI 또는 Baseline.md에 기록할지 여부.
- 천지인 입력순서 표를 renderer visual grammar로 만들지 여부.

## 11. one_line

schema.079.cheonjiiin_input_order_vowel_direction의 cheonjiiin_input_order_vowel_direction.metaplus.md는 사용자 입력이 없는 붙여넣기 자료를 AI 인스턴스 대화층으로 처리하고, 천지인 입력순서에서 ㆍ·ㅡ·ㅣ의 순서가 ㅜ·ㅗ·ㅏ·ㅓ의 방향을 만들며 ㅇ은 000dot, ㆍ은 방향 발생 vector dot으로 분리해 읽게 하는 흐름을 보존하는 대화정리형 이해 로그다.

## 12. shortest

cheonjiiin_input_order_vowel_direction.metaplus.md =
schema.079_cheonjiiin_input_order_vowel_direction 대화정리 /
사용자입력없음 /
입력순서가모음방향을만든다 /
ㅡㆍ=ㅜ /
ㆍㅡ=ㅗ /
ㅣㆍ=ㅏ /
ㆍㅣ=ㅓ /
ㅇ=000dot /
ㆍ=vector_dot