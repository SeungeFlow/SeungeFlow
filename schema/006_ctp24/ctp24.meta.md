# ctp24.meta.md

## Role

`Ctp24`는 Y_Branch의 1차 구조필터이다.

```text
24 scalar states → 12 symmetric pairs → 3×4 matrix states
```

## Reduced Matrix

```text
[
  [R01, R02, R03, R04],
  [R05, R06, R07, R08],
  [R09, R10, R11, R12]
]
```

## Meaning Matrix

```text
[
  [source-time,     source-place,     source-relation,     source-question],
  [operation-time,  operation-place,  operation-relation,  operation-question],
  [field-time,      field-place,      field-relation,      field-question]
]
```

## C-axis

```text
t-axis: R01, R05, R09
p-axis: R02, R06, R10
m-axis: R03, R07, R11
?-axis: R04, R08, R12
```

## Output Classes

```text
실체
guard
field sample
보류
noise
```

## Guard

Ctp24는 matrix를 억지로 모두 채우는 장치가 아니다.
빈 cell은 실패가 아니라 보류 또는 source boundary 표시일 수 있다.
