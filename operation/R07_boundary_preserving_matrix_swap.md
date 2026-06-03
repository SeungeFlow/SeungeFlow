# R07_boundary_preserving_matrix_swap.md

## Definition

```text
R07 = Boundary-Preserving Matrix Swap
```

R07은 서로 다른 field를 병합하지 않고, source boundary를 보존한 채, Ctp24 cell 위치와 구조기능만 교차 비교하는 연산이다.

## Matrix-swap structure vs operation

```text
행렬스왑구조 = 두 구조가 어떻게 놓였는가
행렬스왑연산 = 같은 자리끼리 어떤 연산을 수행하는가
```

수평 비교가 아니다.

```text
A | B  = 수평 펼침 / 나열
A
B     = 수직 겹침 / 같은 자리끼리 연산
```

## Example

```text
  1   5   3
+ 8   4   7
-----------
  9   9   10
```

끝자리 3+7=10에서 carry가 발생해 다음 place-state로 전이한다.

## Guard

```text
의미 등치 금지
상징 병합 금지
source 병합 금지
작품 = 이론 같은 직접대응 금지
```
