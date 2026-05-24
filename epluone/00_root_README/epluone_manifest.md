# epluone manifest

```text
phase = 4/4
document = epluone_manifest.md
role = GitHub 배치용 manifest
```

## 0. 최상위 정의

```text
epluone/
=
Structure_Principle Formation Corpus가 놓이는 장(field)
```

이 manifest는 파일을 하나로 합치기 위한 문서가 아니다.  
이 manifest는 어떤 자료를 어느 디렉토리에 둘지 표시하는 배치표다.

---

## 1. 배치 원칙

```text
원본 우선
해석 별도
요약 보조
삭제 금지
분리 보존
```

```text
압축파일은 가능하면 원형 그대로 보존한다.
압축해제본은 하위 디렉토리에 둔다.
AI 출력과 승이 입력은 가능하면 분리한다.
```

---

## 2. 디렉토리 manifest

| directory | placement target | source type |
|---|---|---|
| 00_root_README | 전체 입구와 지도 | README, relation map, source map, preservation rule, reading order |
| 01_formation_trace | Ctp 이전 형성장 | MyBrain_ThisPoint, Stop/Next/Flow, Break Test, schema formation |
| 02_theory_core | 기반이론 | Ctp_당연한이론, C=tp, c~tp~C, 정수론, 도형론, Flow론 |
| 03_vector_operation | 실행원리 | 훈민정음, 천지인, 자모, 벡터연산, 자동구현프로토콜 |
| 04_vectorizing_tests | 구조테스트 | vectorizing.zip, 반야심경, 금강경, SEUNGE.E.FLOW |
| 05_dynamic_geometry | 동역학 도형 | Cassini, torus, accretion disk, blackhole, vortex, helix, filament |
| 06_ai_cognitive_os | AI 운용 layer | AI인지OS, backdata, 이기종 AI protocol, output protocol |
| 07_the_things_os | 구현 branch | snapshot, restore, drift, alert, heartbeat, fabric navigator, builder relation |
| 08_root_support | 지탱축 | 소호사.향사, 뿌리구조, lineage, ritual, continuity |
| 09_branch_experiments | 분리 archive | PC Branch, 파생 실험, 후보군 |
| 10_capital_market_hints | 미래 응용 힌트 | CFD, OHLC, TradingView, Price.State, Time.State |

---

## 3. 파일 상태 라벨

각 파일 또는 묶음에는 가능하면 다음 중 하나를 붙인다.

```yaml
source_state:
  - original
  - extracted
  - interpreted
  - pending
  - archived
```

## 4. 배치 예시

```text
Ctp_당연한이론.zip
→
epluone/02_theory_core/Ctp_당연한이론/

vectorizing.zip
→
epluone/04_vectorizing_tests/

AI인지OS_백데이터.zip
→
epluone/03_vector_operation/
또는
epluone/06_ai_cognitive_os/AI인지OS_백데이터/

SeungeFlow_blackhole_accretiondisk_*.zip
→
epluone/05_dynamic_geometry/blackhole/
또는
epluone/05_dynamic_geometry/accretion_disk/

the_things_OS 계열
→
epluone/07_the_things_os/

소호사.향사 / 뿌리구조
→
epluone/08_root_support/

CFD / OHLC / TradingView
→
epluone/10_capital_market_hints/
```

---

## 5. 최종 압축

```text
manifest는 배치표다.
manifest는 해석문이 아니다.
manifest는 source가 자기 자리를 잃지 않게 한다.
```
