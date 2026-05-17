---
id: schema.089.hangul_word_layer_distinction
type: active_schema_metadata
filename: hangul_word_layer_distinction.meta.md
directory: 089_hangul_word_layer_distinction
status: active_draft
prev: schema.088.vowel_overlap_ani_chai
---

# META: hangul_word_layer_distinction

## role

hangul_word_layer_distinction은 한국인이 사용하는 한글 단어를 한글 표기 하나로만 읽지 않고, 소리층 / 순우리말 감각층 / 한자식 의미층 / 과학개념층 / 구조원리 해석층으로 분리해 읽기 위한 schema이다.

이 meta 파일은 인공지능이 한글로 적힌 모든 단어를 같은 방식으로 해석하여 의미혼용을 일으키지 않도록 막는 기준이다.

## core

```text
한글표기 하나
내부층 여럿
```

```text
순우리말 = 소리·몸감각
한자식말 = 의미·개념압축
```

## definition

한국인이 쓰는 한글단어는 겉으로 모두 한글 표기이지만, 내부적으로는 여러 층이 섞여 있다.

순우리말은 대체로 소리, 몸감각, 생활감각이 강하다.

한자식말은 대체로 의미 단위, 개념 압축, 정의어의 성격이 강하다.

따라서 단어를 읽기 전에 먼저 층위를 분리해야 한다.

## layer_structure

```text
한글 표기층
소리층
순우리말 감각층
한자 의미층
과학 개념층
구조원리 해석층
```

## examples

순우리말 감각층 예:

```text
오르다
구르다
가르다
버리다
자리
안
밖
사이
```

한자식 의미층 예:

```text
원리
본질
개념
정의
현상
상태
활용
응용
관계
경계
공간
시간
```

## reading_rule

같은 한글 표기라도 다음을 먼저 묻는다.

```text
순우리말 감각이 강한가?
한자식 의미구조가 강한가?
둘 다 작동하는가?
어느 층을 먼저 읽어야 의미혼용이 줄어드는가?
```

## relation

prev:
- schema.088_vowel_overlap_ani_chai

related:
- schema.078_vector_operation_external_engine_rule
- schema.079_cheonjiiin_input_order_vowel_direction
- schema.086_ani_an_boundary_judgment
- schema.090_hanja_compression_direction_reading
- schema.035_principle_hidden_layer_structure
- schema.067_meta_relation_boundary_bridge

## forbidden

- 한글 표기만 같다고 같은 층위로 보지 않는다.
- 순우리말과 한자식말을 무조건 동일하게 분석하지 않는다.
- 한자식 의미구조를 무시하지 않는다.
- 소리층을 의미층으로 바로 환원하지 않는다.
- 구조원리 해석을 표준 국어학 결론으로 주장하지 않는다.
- 의미혼용 상태에서 relation을 생성하지 않는다.

## pending

- 순우리말 감각층의 별도 index를 만들 수 있다.
- 한자식 의미단어 해석은 schema.090에서 분리한다.
- 과학개념층은 science implementation 계열과 relation으로만 둔다.

## shortest

한글표기 하나 / 내부층 여럿 / 순우리말=소리·몸감각 / 한자식말=의미·개념압축
