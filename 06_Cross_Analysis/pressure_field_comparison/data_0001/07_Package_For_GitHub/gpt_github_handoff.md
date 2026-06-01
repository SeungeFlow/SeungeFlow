# gpt_github_handoff.md

## 요청

20회차 종료 후 ZIP으로 전달받은 `data_000X` 패키지를 `music_language` branch의 아래 경로에 배치한다.

```text
music_language/06_Cross_Analysis/pressure_field_comparison/data_000X/
```

## 주의

```text
곡명/작품명을 디렉토리명으로 쓰지 않는다.
구매 악보 원본과 악보 이미지는 포함하지 않는다.
gpt.music 판정문을 수정하지 않는다.
```

## 작업

1. ZIP 압축 해제
2. music_language branch 확인
3. data_000X 번호 확정
4. target path 생성
5. 파일 배치
6. metadata/source_note 검산
7. 원본 악보 파일 포함 여부 검산
8. commit 전 tree 출력
9. 사용자 확인 후 commit 또는 업로드 진행
