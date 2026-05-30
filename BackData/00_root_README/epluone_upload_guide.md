# epluone upload guide

```text
phase = 4/4
document = epluone_upload_guide.md
role = GitHub 업로드 가이드
```

## 0. 목적

이 문서는 `github/epluone/`에 파일과 디렉토리를 올릴 때 사용할 작업 순서를 제공한다.

---

## 1. 기본 순서

```text
1. epluone/ 디렉토리 생성
2. mkdir_epluone.sh 실행
3. README 세트 배치
4. relation/source/preservation/reading map 배치
5. source 묶음별 업로드
6. final checklist 확인
7. commit
```

---

## 2. 로컬 생성

```bash
chmod +x mkdir_epluone.sh
./mkdir_epluone.sh epluone
```

---

## 3. 지도 문서 배치

다음 문서는 `epluone/00_root_README/`에 둔다.

```text
epluone_relation_map.md
epluone_relation_map_en.md
epluone_source_map.md
epluone_source_map_en.md
epluone_preservation_rule.md
epluone_preservation_rule_en.md
epluone_reading_order.md
epluone_reading_order_en.md
epluone_manifest.md
epluone_manifest_en.md
epluone_upload_guide.md
epluone_upload_guide_en.md
epluone_final_checklist.md
epluone_final_checklist_en.md
```

---

## 4. 업로드 순서

```text
1차:
00_root_README
01_formation_trace
02_theory_core

2차:
03_vector_operation
04_vectorizing_tests
05_dynamic_geometry

3차:
06_ai_cognitive_os
07_the_things_os

4차:
08_root_support
09_branch_experiments
10_capital_market_hints
```

---

## 5. commit 메시지 예시

```bash
git add epluone
git commit -m "Add epluone formation corpus directory scaffold"
```

source를 실제로 배치한 뒤에는 다음처럼 한다.

```bash
git add epluone
git commit -m "Add epluone source bundles by formation field"
```

---

## 6. 주의

```text
업로드 전 전체를 하나로 합치지 않는다.
대용량 source는 압축파일 원형도 보존한다.
해석문은 source 옆에 두되 source를 대체하지 않는다.
README는 입구 문서일 뿐이다.
```

---

## 7. 최종 압축

```text
GitHub에는 구조를 올린다.
정리본을 올리는 것이 아니다.
```
