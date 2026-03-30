# Navigation Map

## 0. 목적

이 문서는 `myData` 내부의 모든 파일을  
**다른 AI 인스턴스 또는 사람도 동일하게 이해할 수 있도록**  
구조 / 역할 / 연결 / 사용 위치를 정의하는 지도이다.

---

## 1. 전체 구조 정의

```txt
myData/
= 원본 데이터 + 해석 문서 + 구조 기록이 결합된 아카이브

구성 규칙:

ZIP       = 원본 (수정 금지)
README.md = 해석 / 설명 / 연결 기준
2. 핵심 해석 규칙
1. ZIP을 먼저 보지 않는다
2. README부터 읽는다
3. README → ZIP 순서로 접근한다
4. 모든 자료는 “독립”이 아니라 “연결”로 읽는다
3. 구조 계열 (Structure Line)
Structure
파일: Structure.zip
설명: Structure_README.md
역할
구조를 어떻게 볼 것인가를 정의하는 기준 문서
핵심 개념
Safety
OneLoop
Z System
Layer7
모음 구조
4pin 구조
연결
Structure ↔ 모든 문서의 해석 기준
Structure ↔ AI_System
Structure ↔ Ratio
Structure ↔ 4corner_pin
사용 위치
모든 분석의 시작점
4corner_pin
파일: 4corner_pin.zip
설명: 4corner_pin_README.md
역할
구조의 "형태"를 보여주는 문서
핵심 개념
태극
건곤감리
4-Corner Pin
Center 구조
모음 구조
연결
4corner_pin ↔ Structure (구조 언어)
4corner_pin ↔ Ratio (배열 구조)
사용 위치
구조 시각화 / 구조 해석
4. 분석 계열 (Analysis Line)
Ratio
파일: Ratio.zip
설명: Ratio_README.md
역할
현재 상태를 읽는 도구
핵심 개념
간격
배열
교차
시간축
연결
Ratio ↔ Structure (구조 기준)
Ratio ↔ 4corner_pin (배열 형태)
해결 범위
현재 위치
상태 판독
구조 상태 해석
5. AI / 인지 계열 (AI Line)
AI_System
파일: AI_System.zip
설명: AI_System_README.md
역할
AI를 사용하는 방법이 아니라
AI를 "구조 유지 엔진"으로 사용하는 기준
핵심 개념
질문 생성
구조 유지
domain 이동
no delete only add
연결
AI_System ↔ Structure
AI_System ↔ alive-like structure
alive-like structure
파일: alive-like structure of system.zip
설명: alive_like_structure_of_system_README.md
역할
사고가 무너지지 않도록 유지하는 구조
핵심 개념
정의 선행
층위 분리
균형 유지
멈춤 조건
연결
alive-like ↔ AI_System
alive-like ↔ Structure
6. 시스템 / OS 계열 (System Line)
RestoreOS
파일: RestoreOS.zip
설명: RestoreOS_README.md
역할
복구 중심 운영 구조
핵심 개념
Recovery
Snapshot
Builder
반자동 구조
L7OS_for_M7DQ
파일: L7OS_for_M7DQ.zip
설명: L7OS_for_M7DQ_README.md
역할
7대 난제용 시스템 생성기
핵심 개념
7개의 연구 시스템
Linux 기반
연구 루프 자동화
7. 문서 지도 계열 (Map Line)
MyDoc
파일: MyDoc.zip
설명: MyDoc_README.md
역할
전체 문서를 연결하는 내부 지도
핵심 개념
COREMAP
Anchor
Spec
System Map
연결
MyDoc ↔ 모든 문서
vFinal
파일: vFinal.zip
설명: vFinal_README.md
역할
구조 실행 기록 아카이브
특징
순차 기록
버전 흐름
구조 변화 추적
8. 이론 계열 (Theory Line)
MyTheory
파일: MyTheory.zip
설명: MyTheory_README.md
역할
README 기반 이론 흐름 기록
핵심
README_0.1 ~ 0.7
이론 이동 과정
본질 추출
SeungeFinal
파일: SeungeFinal.zip
설명: SeungeFinal_README.md
역할
전체 구조 분석 기록의 통합본
의미
복잡계 → 구조분석 → 시스템화
9. 전체 연결 구조
README.md
= 이론 본체

myData/
= 실행 / 기록 / 확장

navigation_map.md
= 설명 / 연결 / 진입 지도
10. 최종 규칙
1. README.md는 절대 해석하지 않는다
2. navigation_map.md에서만 설명한다
3. ZIP은 수정하지 않는다
4. README는 확장 가능
5. 모든 것은 연결로 읽는다
마지막
이 지도는 문서를 설명하는 것이 아니라

문서를 읽는 방법을 정의한다

---

## 🔥 한 줄

```txt
이제 이건 "설명"이 아니라 "읽기 시스템"이다