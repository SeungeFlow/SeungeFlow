# epluone preservation rule

```text
phase = 3/4
document = epluone_preservation_rule.md
role = 보존 규칙
```

## 0. 최상위 원칙

```text
no delete
only add
```

이 원칙은 파일 보존, 문서 해석, 디렉토리 운영에 모두 적용한다.

---

## 1. 금지

```text
원문 삭제 금지
전체 통합요약 금지
하나의 문서로 합치기 금지
AI 출력만 남기고 승이 입력 삭제 금지
Stop / Next / Flow 삭제 금지
실패 기록 삭제 금지
Break Test 붕괴 기록 삭제 금지
CFD를 core theory로 승격 금지
소호사.향사를 단순 application으로 축소 금지
```

---

## 2. 허용

```text
인덱싱
디렉토리 배치
source map 작성
relation map 작성
README 작성
원문과 해석 분리
후보군 archive
```

---

## 3. 문서 처리 원칙

```text
원문
=
그 자체로 source

해석
=
별도 interpretation file

요약
=
가능하나 source를 대체하지 못함

README
=
입구 문서

relation map
=
지도

manifest
=
배치표
```

---

## 4. AI 출력 처리 원칙

```text
AI 출력은 source가 될 수 있다.
하지만 승이 입력과 구분한다.

AI 출력은 정답이 아니라
해석 trace / response layer / 검증 후보로 둔다.
```

---

## 5. 실패 기록 처리 원칙

```text
실패
=
삭제 대상 아님

붕괴
=
다음 구조의 재료

Stop
=
좌표 충돌 직전 임계 지점

Break Test
=
weak link 발견 장치
```

---

## 6. 압축 금지 원칙

```text
너무 압축하면 의미가 사라진다.
너무 요약하면 구조가 사라진다.
너무 정리하면 흐름이 죽는다.
```

따라서 압축은 다음 목적일 때만 한다.

```text
검색을 위한 index
파일 배치를 위한 manifest
읽기 순서를 위한 guide
```

---

## 7. 최종 압축

```text
epluone에서는
원본이 우선이고,
해석은 다음이며,
요약은 보조이고,
삭제는 없다.
```
