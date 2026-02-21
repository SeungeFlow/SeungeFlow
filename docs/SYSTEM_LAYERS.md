SeungeFlow System Layer Definition

이 문서는 SeungeFlow 시스템의 계층 구조를 정의하기 위한 것이다.
이 문서는 기능 설명이 아니라 구조적 위치 정의 문서다.

SeungeFlow는 다음 네 계층으로 구성된다.

1. Manifest Layer

이 계층은 시스템의 존재 이유를 정의한다.
개념, 선언, 철학이 위치한다.
이 계층은 실행되지 않는다. 기준만 제공한다.

2. Runtime Kernel Layer

이 계층은 시스템의 작동 중심이다.
CLI, ingest, query, predict가 여기에 속한다.
이 계층은 관측을 구조로 변환한다.

3. Structural Database Layer

이 계층은 세계 상태를 저장한다.
node, relation, event, pattern이 여기에 존재한다.
이 계층은 시간 속의 기록을 유지한다.

4. Persistence Layer

이 계층은 시간 지속을 보장한다.
systemd 서비스, 로그 흐름, 백업 전략이 여기에 속한다.
이 계층은 시스템이 멈추지 않도록 한다.

이 네 계층은 순환 구조를 이룬다.

Manifest는 Runtime의 기준이 되고,
Runtime은 Database를 갱신하며,
Database는 Persistence 속에서 유지되고,
Persistence는 다시 Manifest를 현실 속에 유지한다.

이 문서는 SeungeFlow의 구조적 위치를 고정한다.
이 정의 이후 계층 추가는 구조 변화로 간주된다.