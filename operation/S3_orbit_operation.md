# S3_orbit_operation.md

## Formula candidate

```text
S₃(M, m | U, A, P_m)
=
DimSplit_U(
    FieldBoundaryᵢ(M, m, P_m),
    Coord_A(m - ㆍ),
    EscapeCondition(m, FieldBoundaryᵢ, P_m)
)
```

## Role

S₃는 orbit / field boundary / escape condition을 다룬다.

Brake Test 이후 S₃는 물리적 궤도만이 아니라 source-boundary와 interpretation-boundary에도 적용된다.

```text
S₃ = source-boundary + interpretation-boundary + escape-condition
```

## Status

부분 통과.
FieldBoundaryᵢ와 EscapeCondition 정의는 계속 보강해야 한다.
