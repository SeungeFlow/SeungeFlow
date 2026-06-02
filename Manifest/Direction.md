# Direction.md

## SeungeFlow gpt.direct 48회차 방향문 — 04회차 반영

```text
file target:
main/Manifest/Direction.md

document role:
direction document from gpt.direct to all instances
+
48-session route plan
+
Session 04 branch-role direction update

compass anchor:
main/Manifest/README_for_AI.md

primary instance:
gpt.direct

current session:
04 / 48

observed branch:
main

observed path:
Manifest/Branch.md

observed Raw URL:
https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/main/Manifest/Branch.md

fixed-revision Raw URL:
https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/0335ce3/Manifest/Branch.md
```

---

## 0. 이 문서의 역할

`Direction.md`는 gpt.direct가 모든 인스턴스에게 방향을 제시하는 문서다.

04회차 이후 이 문서는 특히 다음 방향을 추가한다.

```text
각 인스턴스는
자기 branch를 읽기 전
그 branch의 role-bearing structure field를 먼저 확인한다.
```

`README_for_AI.md`는 중심기준이다.

`Direction.md`는 그 중심기준에 따라 어느 지점을 어떻게 볼지 알려주는 route 문서다.

---

## 1. 04회차 관측 지점

```text
[SeungeFlow 표시문]

branch:
main

path:
Manifest/Branch.md

observed Raw URL:
https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/main/Manifest/Branch.md

fixed-revision Raw URL:
https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/0335ce3/Manifest/Branch.md

source status:
verified branch Raw URL
+
verified fixed-revision Raw URL at commit 0335ce3

observed point:
Branch.md는 main.branch Manifest 안에서 branch.structure의 대표 정의와 역할 mapping을 고정하는 문서다.

source fact:
Branch.md는 branch가 단순 Git branch가 아니라 role-bearing structure field라고 둔다.
main, seed_base, active_schema, epluone, first_flow는 서로 다른 구조역할을 가진다.

structure interpretation:
각 인스턴스는 자기 branch를 읽을 때 branch 이름보다 먼저 branch 역할과 place.state를 확인해야 한다.

comparison point:
다른 인스턴스는 위 Raw URL에 접근해 자기 branch가 SeungeFlow 전체 branch map 안에서 어떤 역할을 갖는지 비교해야 한다.

guard:
branch 역할을 섞지 않는다.
main을 DB로 만들지 않는다.
seed_base를 runtime output으로 덮지 않는다.
active_schema를 archive로 만들지 않는다.
epluone을 representative root로 만들지 않는다.
first_flow를 삭제하지 않는다.
```

---

## 2. 04회차가 모든 인스턴스에게 제시하는 방향

각 인스턴스는 다음 순서로 자기 branch를 읽는다.

```text
1. README_for_AI.md로 gpt.direct 중심기준 확인
2. Direction.md로 회차 방향 확인
3. Branch.md로 branch role map 확인
4. 자기 branch의 role-bearing structure field 확인
5. 자기 output이 놓일 branch / path / place.state 확인
6. source fact와 structure interpretation 분리
7. gpt.direct 이해와 자기 자가해석 비교
```

---

## 3. branch role map

```text
main =
visible root
+
representative entry
+
compass

seed_base =
source memory
+
Seed.Base

active_schema =
current operating structure
+
OS

epluone =
runtime factory
+
output production field
+
workshop

first_flow =
origin preservation
+
first flow
+
proto path field
```

---

## 4. branch flow direction

기본 flow:

```text
first_flow
→ seed_base
→ active_schema
→ epluone
→ outputs/meta
→ seed_base
```

active_schema 중심 flow:

```text
seed_base source
+
epluone package output
+
first_flow origin reference
→
active_schema OS
→
Core / Path / Rule / Mapping
→
main candidate
+
epluone next task
```

이 flow는 복사흐름이 아니다.

```text
copy flow X
interpretation flow O
```

---

## 5. 이후 회차에 반영할 방향

05회차부터 main.branch의 다른 Manifest 문서를 볼 때도 다음 기준을 유지한다.

```text
branch role first
path second
Raw URL third
source fact fourth
structure interpretation fifth
```

인스턴스가 어느 파일을 보든, 그 파일이 어느 branch role 안에 놓여 있는지를 먼저 본다.

---

## 6. 48회차 흐름 안에서 04회차의 위치

```text
01 =
README_for_AI.md / Direction.md 역할 분리

02 =
main README / visible root 확인

03 =
README_for_SeungLee.md / SeungLee-side principle 확인

04 =
Branch.md / branch.structure representative map 확인
```

04회차는 main.branch compass block 안에서 branch 역할지도를 고정하는 회차다.

이후 회차에서 Core, Path, Rule을 읽을 때도 branch role guard를 유지한다.

---

## 7. 다음 회차

```text
next session:
05 / 48

next branch:
main

next path:
Manifest/Rule.md

next observed Raw URL:
https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/main/Manifest/Rule.md

next purpose:
main.branch 기준의 기본 규칙 / 금지사항 확인
```

---

## 8. Direction.md 닫힘문

```text
04회차 이후 Direction.md는
각 인스턴스가 branch를 단순 Git branch가 아니라
role-bearing structure field와 place.state로 읽도록 방향을 제시한다.

Branch.md는 branch.structure representative map이며,
모든 인스턴스는 자기 branch 작업에 들어가기 전
branch 역할과 place.state를 먼저 확인해야 한다.
```
