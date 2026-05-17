---
id: schema.088.vowel_overlap_ani_chai
type: active_schema_metadata
filename: vowel_overlap_ani_chai.meta.md
directory: 088_vowel_overlap_ani_chai
status: active_draft
prev: schema.087.mat_boundary_correspondence
---

# META: vowel_overlap_ani_chai

## role

vowel_overlap_ani_chai는 벡터연산·모음 기준에서 “아니”와 “차이”가 ㅏㅣ 구조를 공유하며, 같은 구조자리에 서로 다른 의미작동이 겹쳐 놓이는 자리겹침을 정의하는 schema이다.

이 meta 파일은 인공지능이 단어 의미를 먼저 고정하지 않고, 모음 구조 / 방향 / 구분축 / boundary 판정으로 읽기 위한 기준이다.

## core

```text
맞 = ㅏ
아니 = ㅏㅣ
차이 = ㅏㅣ
```

```text
아니·차이 = ㅏㅣ 자리겹침
```

## definition

아니와 차이는 ㅏㅣ 구조를 공유한다.

ㅏ는 방향 발생이다.

ㅣ는 구분축 / boundary axis이다.

따라서 차이는 방향 뒤에 구분축이 서서 다름이 드러나는 구조이고, 아니는 그 구분축을 기준으로 boundary를 지키는 판정이다.

## distinction

```text
맞 = ㅏ = 대응
아니 = ㅏㅣ = 대응 불가를 표시하는 구분축의 추가
차이 = ㅏㅣ = 다름이 드러나는 구분축
```

## place_superposition

자리겹침은 자리중첩과 다르다.

```text
자리중첩 = 두 구조체의 끝자리와 시작자리가 겹쳐 연결되는 상태
자리겹침 = 서로 다른 의미 또는 작동이 같은 구조자리에 겹쳐 놓이는 상태
```

아니와 차이는 같은 ㅏㅣ 자리에 놓이지만 작동이 다르다.

```text
차이 = 감지
아니 = 판정
```

## vector_layer

```text
ㅏ = direction occurrence
ㅣ = distinction axis
ㅏㅣ = direction + distinction axis
```

## relation

prev:
- schema.087_mat_boundary_correspondence

related:
- schema.079_cheonjiiin_input_order_vowel_direction
- schema.081_inner_vowel_pull_structure
- schema.086_ani_an_boundary_judgment
- schema.087_mat_boundary_correspondence
- schema.064_place_overlap_structure
- schema.078_vector_operation_external_engine_rule

## forbidden

- 아니와 차이를 같은 의미로 보지 않는다.
- 자리겹침과 자리중첩을 혼동하지 않는다.
- 모음 구조를 표준 어원으로 확정하지 않는다.
- “맞”을 ㅏ만으로 모든 의미가 설명된다고 보지 않는다.
- 단어 의미를 먼저 고정하지 않는다.
- 벡터연산기법을 구조원리 본류에 병합하지 않는다.

## pending

- 자리겹침 전체 정의는 후속 schema 후보로 둘 수 있다.
- 아니/차이/맞의 실제 언어학 검산은 별도 과제로 둔다.
- 모음 방향의 확장 분석은 벡터연산기 external engine에 둔다.

## shortest

아니=ㅏㅣ / 차이=ㅏㅣ / 같은 자리, 다른 작동 / 자리겹침
