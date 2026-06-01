# music_language

`music_language` branch는 음악과 언어를 하나의 구조장(field)으로 놓고, 악보·가사·시·자모·음율·반복·경계·잔류 구조를 비교하기 위한 SeungeFlow 실험 branch이다.

이 branch의 목적은 특정 곡이나 작품을 소개하는 것이 아니라, 음악과 언어 안에 숨어 있는 구조를 추출하고, 그 구조가 서로 어떻게 겹치고 충돌하고 미끄러지고 잔류하는지 관측하는 것이다.

---

## 1. 기본 목적

이 branch는 다음 질문을 다룬다.

```text
가사와 음율은 어떻게 하나의 field를 이루는가?
시와 악보는 서로 다른 매체이지만 어떤 구조에서 겹칠 수 있는가?
반복, 경계, 수열, 잔류, 결정화는 음악과 언어 안에서 어떻게 나타나는가?
```

현재 핵심 관점은 다음이다.

```text
음악과 언어는 분리된 해석 대상이 아니다.
가사와 음율은 결합된 music-language field이다.
문서의 행, 악보의 음표, 시의 단락, 가사의 음절은 모두 time.state를 끊어 읽는 dot으로 볼 수 있다.
```

---

## 2. 현재 1차 반영 상태

현재 `music_language` branch에는 gpt.music 20회차 1차 마무리 산출물이 반영되어 있다.

```text
06_Cross_Analysis/
└── pressure_field_comparison/
    └── data_0001/
```

`data_0001`은 오감도 × 비목 구조 겹침 실험의 1차 closure package이다.

이 data는 작품명이나 곡명을 디렉토리명으로 쓰지 않고, 중립 data ID 방식으로 보관한다.

---

## 3. data_0001의 중심 실험

`data_0001`의 중심 실험은 다음이다.

```text
오감도 × 비목 구조 겹침 실험
```

이 실험은 두 대상의 의미가 같다고 주장하는 작업이 아니다.

이 실험은 다음 구조를 관측한다.

```text
반복이 강화된 field 안에서
운동과 흐름이 ㄷ형 boundary에 걸리고,
그 결과가 유예·잔류·결정화로 남는 구조
```

gpt.music 20회차 1차 마무리에서 살아남은 중심축은 다음 네 가지다.

```text
1. boundary
2. sequence
3. residue
4. repetition
```

---

## 4. 핵심 구조축

### 4.1 boundary

```text
오감도:
막다른 골목

비목:
깊은 계곡
```

판정:

```text
오감도 = ㄷ 안으로 들어가는 운동
비목 = ㄷ 안에서 남는 결정화
```

---

### 4.2 sequence

```text
오감도:
一人 → 二人 → 二人 → 一人

비목:
1절 / 2절 병렬
```

오감도에서는 수량층이 보존되고 상태층이 반전된다.

비목에서는 같은 음악 구조 위에 1절과 2절의 병렬 언어열이 놓인다.

---

### 4.3 residue

```text
오감도:
질주하지 아니하여도 좋소

비목:
맺힘 / 쌓임
```

판정:

```text
movement / flow
→ boundary
→ residue
→ crystallization
```

---

### 4.4 repetition

```text
오감도:
제1~제13
가 / 도 반복

비목:
깊은 계곡 깊은 계곡
달빛타고 달빛타고
마디마디
알알이
```

한국어에서 반복은 단순 중복이 아니라 강조와 구조 보강으로 작동한다.

---

## 5. source 원칙

이 branch는 원자료를 다음 원칙으로 다룬다.

### 5.1 오감도

오감도는 사용자가 제공한 전문을 1차 원자료로 사용한다.

위키문헌, 위키백과, 한국민족문화대백과 등은 보조 검산 자료로 둔다.

오감도 15편 전체는 continuous field reference로 보관할 수 있으나, 현재 `data_0001`의 중심은 오감도 시제1호와 비목의 구조 겹침 실험이다.

---

### 5.2 비목

비목 악보는 사용자가 정당하게 구매한 분석용 원자료를 사용한다.

분석 단계에서는 다음을 데이터화할 수 있다.

```text
음표
음고
음가
박
마디
코드명
가사-음표 대응
자모 구조
음율 구조
```

단, 공개 GitHub에는 다음을 올리지 않는다.

```text
구매 악보 PDF 원본
악보 이미지 원본
악보 사이트 원본 파일
```

공개 가능한 것은 분석 파생 문서와 구조해석 결과이다.

---

## 6. 공개 / 비공개 경계

공개 가능:

```text
metadata.md
source_note.md
case_manifest.md
work_plan.md
분석용 파생 문서
구조 후보표
state 재분류 문서
겹침 / 충돌 / 미끄러짐 / 잔류 압축문
안정 후보 / 보류 항목 분리문
gpt.music 판정문
gpt.github handoff 문서
```

공개 금지:

```text
구매 악보 PDF 원본
악보 이미지 원본
비공개 원자료 파일
공개하면 안 되는 개인 자료
```

---

## 7. 인스턴스 역할

이 branch의 주요 인스턴스 역할은 다음과 같다.

```text
gpt.music
= 통합 판정 / 겹침·충돌·미끄러짐·잔류 후보 압축

gpt.music.operator
= 원자료 구조 데이터 정렬 / 악보·가사·자모·구조 단위 검산

모아
= 입력 텍스트 순수구조 분해 / 의미 후보 생성

gpt.github
= ZIP 전달 이후 branch 반영 / 파일 배치 / tree 검산
```

역할 원칙:

```text
모아는 operator가 아니다.
operator는 모아가 아니다.
gpt.music은 둘의 산출물을 통합하지만 둘의 역할을 대신하지 않는다.
gpt.github는 gpt.music 판정을 수정하지 않는다.
```

---

## 8. 현재 디렉토리 구조

현재 핵심 data 구조는 다음과 같다.

```text
06_Cross_Analysis/
└── pressure_field_comparison/
    └── data_0001/
        ├── metadata.md
        ├── source_note.md
        ├── case_manifest.md
        ├── work_plan.md
        ├── 00_Source_Reference/
        ├── 01_Extracted_Data/
        ├── 02_Structure_Candidates/
        ├── 03_State_and_Field/
        ├── 04_Overlay_Analysis/
        ├── 05_Filter_and_Hold/
        ├── 06_GptMusic_Judgment/
        ├── 07_Package_For_GitHub/
        └── 99_BackData/
```

---

## 9. data ID 원칙

이 branch에서는 곡명이나 작품명을 디렉토리명으로 사용하지 않는다.

사용 금지 예:

```text
오감도
비목
애국가
그리운_금강산
Bimok
Ogamdo
Aegukga
Geuriun_Geumgangsan
```

사용 방식:

```text
data_0001
data_0002
data_0003
...
```

작품명과 곡명은 `metadata.md`와 `source_note.md` 내부에만 기록한다.

---

## 10. 현재 상태

```text
status:
FIRST_CLOSURE_PERSISTED
```

gpt.music 20회차 1차 마무리 산출물은 `music_language` branch의 `data_0001` place.state에 정상 반영되었다.

현재 판정:

```text
오감도와 비목은 의미가 같아서 만나는 것이 아니라,
반복이 강화된 field 안에서 운동과 흐름이 ㄷ형 boundary에 걸리고,
그 결과가 유예·잔류·결정화로 남는 구조에서 만난다.
```

---

## 11. 후속 후보

다음 작업들은 후속 후보로 남긴다.

```text
오감도 15편 전체 continuous field 확장
비목 전체 음고·음가·박 기반 정밀 대응
애국가 후렴 / 태극기 비교 재개
그리운 금강산 기준 샘플 재비교
화성학 기능 대응
9dot0 공식화
ㅈㅊㅊㅈ 형태 재조립 검산
공명 / 특이점 / 정신세계 잔류 판정
```

이 항목들은 현재 `data_0001`의 1차 closure 안에서는 hold 상태로 둔다.

---

## 12. 최종 한 줄

`music_language` branch는 음악과 언어가 결합된 field 안에서 반복, 경계, 자리수열, 잔류, 결정화 구조를 관측하는 branch이며, 현재 `data_0001`은 오감도 × 비목 구조 겹침 실험의 1차 place.state로 반영되어 있다.
