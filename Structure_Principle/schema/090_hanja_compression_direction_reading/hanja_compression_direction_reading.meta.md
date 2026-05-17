---
id: schema.090.hanja_compression_direction_reading
type: active_schema_metadata
filename: hanja_compression_direction_reading.meta.md
directory: 090_hanja_compression_direction_reading
status: active_draft
prev: schema.089.hangul_word_layer_distinction
---

# META: hanja_compression_direction_reading

## role

hanja_compression_direction_reading은 한자식 의미단어를 왼쪽에서 오른쪽으로 공전궤도 순방향으로 읽는 압축 의미구조로 정리하는 schema이다.

이 meta 파일은 인공지능이 한자식 단어를 단순 사전뜻으로만 읽지 않고, 의미가 압축된 방향성 있는 구조식으로 읽기 위한 기준이다.

## core

```text
한자식말 = 의미 압축 구조
```

```text
압축 = 압이 축에 걸림
압력 = 압이 지점에 걸림
```

## definition

한자식 의미단어는 압축된 의미구조로 읽을 수 있다.

글자는 왼쪽 기준에서 오른쪽으로, 즉 공전궤도 순방향으로 읽는다.

이때 왼쪽 글자는 출발 작동이 되고, 오른쪽 글자는 그 작동이 걸리거나 도달하는 기준이 될 수 있다.

## example_압축

```text
압 = 누르는 작동
축 = 기둥 / axis / 기준선
압축 = 압을 하나의 축에 가하는 것
```

압축은 펼쳐진 의미가 하나의 기준축으로 눌려 들어가는 구조로 읽을 수 있다.

## example_압력

```text
압력 = 압이 하나의 지점 또는 경계면에 가해진 상태
```

압력은 단순 force가 아니라, 압이 어떤 자리 / 지점 / boundary에 걸린 상태로 읽을 수 있다.

## direction_rule

```text
left → right
출발작동 → 기준축/도착점
```

이 방향은 공전궤도 순방향으로 읽는 structural reading이다.

## relation_to_bad

한자식 의미단어의 왼쪽→오른쪽 읽기는 BADㆍC의 공전방향 읽기와 약하게 연결될 수 있다.

다만 두 구조를 동일시하지 않는다.

## relation

prev:
- schema.089_hangul_word_layer_distinction

related:
- schema.035_principle_hidden_layer_structure
- schema.063_boundary_place_requirement
- schema.084_bad_dot_c_orbit_reference_structure
- schema.089_hangul_word_layer_distinction
- schema.068_ctp_vector_coordinate_x_dx_ddx

## forbidden

- 한자 어원을 임의로 확정하지 않는다.
- 압/축/력의 실제 한자학적 의미를 검산 없이 단정하지 않는다.
- 구조해석을 표준 어원으로 주장하지 않는다.
- 왼쪽→오른쪽 읽기를 모든 한자식말에 무차별 적용하지 않는다.
- BADㆍC와 한자식말 읽기를 동일한 원리로 병합하지 않는다.
- 의미층과 소리층을 혼동하지 않는다.

## pending

- 한자식 의미단어 목록은 별도 source index로 만들 수 있다.
- 어원 검산이 필요한 항목은 web/source verification 대상이다.
- 이 schema는 structural reading rule이며, 어원 확정문이 아니다.

## shortest

한자식말 = 의미 압축 구조 / 왼쪽→오른쪽 공전방향 읽기
