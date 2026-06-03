# validator_loop.md

## Role

Y_Branch는 선형 pipeline이 아니라 Validator Loop를 가진 State Machine이다.

```text
Q.CHECK = 반복 validator
```

## Critical order

```text
B.FIELD → Q.CHECK → O.ORBIT
```

Boundary가 정의되지 않으면 orbit을 호출하지 않는다.
