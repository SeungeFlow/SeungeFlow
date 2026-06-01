# source_note.md

## 1. 목적

이 문서는 `data_000X`에서 사용하는 원자료와 공개/비공개 경계를 기록한다. 원자료 자체가 아니라 source 기준과 사용 경계를 기록하는 문서다.

## 2. 오감도 원자료 기준

```yaml
source_group: ogamdo
primary_source: user_provided_full_text_in_conversation
secondary_reference:
  - 위키문헌 「오감도」
  - 위키백과 「오감도」
  - 한국민족문화대백과 「오감도」
source_scope:
  - 시제1호 중심
  - 시제1호~시제15호 continuous field reference
```

원칙:

```text
오감도 구조분해의 1차 기준은 사용자가 대화창에 직접 제공한 전문이다.
위키문헌 / 위키백과 / 한국민족문화대백과는 보조 검산 자료로만 사용한다.
오감도 15편 전체는 현재 20회차의 중심이 아니며, 현재 중심은 오감도 시제1호와 비목의 구조 겹침 실험이다.
```

## 3. 비목 원자료 기준

```yaml
source_group: bimok
primary_source: legitimately_purchased_score
score_public_upload: false
analysis_publication: derived_analysis_only
```

원칙:

```text
비목 악보는 사용자가 정당하게 구매한 분석용 원자료다.
분석 단계에서는 음표, 음가, 박, 마디, 코드명, 가사-음표 대응, 자모 구조, 음율 구조를 데이터화할 수 있다.
공개 GitHub에는 구매 악보 PDF 원본, 악보 이미지, 사이트 원본 파일을 올리지 않는다.
공개 가능한 것은 분석용 파생 문서와 구조해석 결과이다.
```

## 4. source_note 최종 한 줄

`data_000X`는 사용자가 제공한 오감도 전문과 정당 구매한 비목 악보를 원자료로 삼되, 공개 GitHub에는 원본 악보 파일을 올리지 않고, 오감도 × 비목 구조 겹침 실험에서 생성된 파생 구조해석 문서만 보관한다.
