# gpt.github handoff — active_schema 문서군 반영 지시문

> 문서번호: `Ctp24_ACTIVE_SCHEMA_HANDOFF_0001`  
> 상태: active_schema 문서군 GitHub 반영 준비  
> 목적: `Ctp24_Active_Schema_Design_Package.zip`을 gpt.github에게 넘겨 active_schema.branch 반영을 준비한다.

---

## 0. 전달 대상

전달할 ZIP:

```text
Ctp24_Active_Schema_Design_Package.zip
```

이 ZIP은 gpt.direct가 작성한 active_schema OS 문서군 후보 패키지다.

```text
성격 =
active_schema.branch 반영 후보
```

---

## 1. 반영 대상 branch

권장 branch:

```text
active_schema
```

이 문서군은 active_schema.branch의 OS 문서군이므로, main이나 epluone에 먼저 반영하지 않는다.

---

## 2. 추천 반영 구조

```text
active_schema branch root
├─ active_schema.md
├─ package_reference.md
├─ runtime_mapping.md
├─ source_mapping.md
├─ current_rules.md
├─ core.meta.md
└─ current_path.md
```

설계 노트:

```text
active_schema_design_0001.md
```

는 root에 두거나, 필요하면 다음처럼 둘 수 있다.

```text
docs/active_schema_design_0001.md
```

---

## 3. 절대 금지

```text
1. main.branch에 바로 반영하지 않는다.
2. seed_base를 덮어쓰지 않는다.
3. first_flow를 삭제하거나 흡수하지 않는다.
4. epluone/Ctp24/GPT_Direct_Structure_Package를 active_schema에 통째로 복사하지 않는다.
5. 렌더링 트랙 epluone/Ctp24_rendering과 섞지 않는다.
```

---

## 4. 반영 전 확인

gpt.github는 먼저 다음을 확인한다.

```text
1. 현재 branch 상태
2. active_schema branch 존재 여부
3. remote origin/active_schema 상태
4. working tree clean 여부
5. 기존 active_schema 파일과 충돌 여부
```

---

## 5. 반영 절차 제안

```text
1. git checkout active_schema
2. 현재 파일 구조 확인
3. ZIP 압축 해제는 임시 디렉토리에 먼저 수행
4. 문서 7개를 active_schema root 후보로 배치
5. active_schema_design_0001.md는 root 또는 docs/에 배치
6. git status 확인
7. 필요 시 기존 파일 backup 또는 diff 확인
8. commit
9. push origin active_schema
10. main branch로 복귀
```

---

## 6. commit message 후보

```text
Add active schema OS document set from GPT Direct design
```

한국어 의미:

```text
gpt.direct 설계 기반 active_schema OS 문서군 추가
```

---

## 7. 반영 후 보고할 것

반영 후 gpt.github는 다음을 보고한다.

```text
branch
commit hash
commit message
changed files count
working tree clean 여부
remote sync 여부
main 복귀 여부
```

---

## 8. 닫힘

이 지시문은 gpt.direct가 작성한 active_schema 문서군을 gpt.github가 안전하게 반영하기 위한 handoff 문서다.

```text
gpt.direct =
active_schema OS 설계

gpt.github =
실제 GitHub 반영
```
