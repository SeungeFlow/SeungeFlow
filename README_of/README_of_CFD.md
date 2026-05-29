---
id: main.readme_of_cfd
type: readme_of_document
filename: README_of_CFD.md
directory: /main/
status: active_draft
authority:
  - Human.Lee Seung
  - ChatGPT.direct
purpose:
  - guide_cfd_reading
  - define_cfd_as_current_body_target_value
  - prevent_cfd_from_being_read_as_epluone_identity
  - connect_cfd_to_epluone_body_slot
  - guide_cfd_backtesting_context
---

# README_of_CFD.md

## 0. 역할

`README_of_CFD.md`는 CFD를 어떻게 읽어야 하는지 안내하는 문서이다.

이 문서는 CFD 자체가 아니라,  
현시점 `epluone`의 `[body]` slot에 놓인 target value인 CFD를 AI가 오독하지 않도록 돕는 guide document이다.

```text
README_of_CFD.md
=
CFD reading guide
+
epluone [body] slot guide
+
current target value guide
+
application target guard
```

---

## 1. CFD의 기본 위치

CFD는 SeungeFlow 전체의 identity가 아니라,  
현시점 `epluone`의 `[body]` slot에 놓인 target value이다.

```text
epluone
=
if+1
=
[body] slot directory

CFD
=
current target value in epluone's [body] slot
```

즉 CFD는 `epluone` 그 자체가 아니라,  
현재 `epluone`의 `[body]` slot에 놓인 응용 target value이다.

---

## 2. if+1 / epluone과 CFD

`if`는 intelligence fabric이다.

```text
if
=
인간지능.승이
+
인공지능.AI
```

`if+1`은 `epluone`이다.

```text
if+1
=
epluone
```

`if+1`은 intelligence fabric이 다음 응용 target에 놓이는 자리이다.

따라서 CFD는 `if+1`의 identity가 아니라,  
현시점 `if+1`의 `[body]` slot에 놓인 적용 대상이다.

```text
if+1
=
application target slot

CFD
=
current application target value
```

---

## 3. CFD와 [body]

SeungeFlow는 어떤 state든 다음 구조로 읽는다.

```text
any([time][place][body])
```

여기서 `[body]`는 응용 target이나 실행 body가 놓이는 자리이다.

```text
[body]
=
application target slot
+
operating body slot
```

CFD는 현시점 `[body]`에 놓인 응용 target value이다.

```text
[body: CFD]
=
현재 응용 target이 CFD로 놓인 상태
```

AI는 CFD를 `[body]` slot의 현재 값으로 읽어야 하며,  
CFD를 Seed.Base 전체나 epluone 전체의 identity로 읽으면 안 된다.

---

## 4. CFD와 Seed.Base

Seed.Base는 특정 파일, 특정 디렉토리, 특정 target 하나에 종속되는 구조가 아니라,  
SeungeFlow 저장소 전체에 놓인 문서, 디렉토리, 관계, map이 함께 만드는 전체 장이다.

```text
Seed.Base
=
존재의 관계 정의
+
장(Field)의 구조원리
```

CFD는 Seed.Base 전체가 아니라,  
Seed.Base가 현시점 응용 대상으로 삼고 있는 `[body]` target value이다.

```text
Seed.Base
≠
CFD

CFD
=
current body target value
```

이 문장은 CFD의 중요성을 낮추는 뜻이 아니라,  
CFD가 놓인 자리를 정확히 구분하기 위한 guard이다.

---

## 5. CFD와 Structure_Principle

`Structure_Principle/`은 `[place]`에 해당한다.

```text
Structure_Principle
=
[place]
```

CFD는 `Structure_Principle/` 내부의 schema identity가 아니라,  
`Structure_Principle`에서 정리된 자리개념과 relation이 적용될 수 있는 현재 `[body]` target value이다.

```text
Structure_Principle
=
place-concept field

CFD
=
current application body target
```

따라서 CFD를 `Structure_Principle/schema/` 내부 core처럼 직접 병합하는 것이 아니라,  
Structure_Principle과 CFD 사이의 application relation으로 읽어야 한다.

---

## 6. CFD와 SeungeFlow_Thinking

`SeungeFlow_Thinking/`은 `[time]`에 해당한다.

```text
SeungeFlow_Thinking
=
[time]
```

CFD에 관한 이해도 thinking_flow를 통해 형성될 수 있다.

```text
CFD 관련 thinking_flow
=
CFD target에 대한 pre-meta Seed flow
```

그러나 CFD 관련 thinking_flow가 곧바로 CFD meta.md가 되는 것은 아니다.

```text
thinking_flow
→
Seed 추출
→
중복 검토
→
relation 검토
→
문서 유형 판단
```

CFD 관련 생각은 먼저 Seed 후보로 두고,  
기존 schema와 중복되는지, 독립 boundary가 있는지, relation이 필요한지 확인해야 한다.

---

## 7. CFD와 main/README_of_CFD.md

`README_of_CFD.md`는 CFD가 놓이는 장소가 아니라,  
CFD를 읽기 위한 guide document이다.

```text
main/README_of_CFD.md
=
CFD reading guide
```

이 문서가 `main/` 안에 놓여 있다는 것은 CFD가 `main/`에 의미적으로 종속된다는 뜻이 아니라,  
CFD를 읽기 위한 guide 문서가 root-level guide layer에 놓여 있다는 뜻이다.

```text
main/
=
root-level guide layer

README_of_CFD.md
=
CFD guide document
```

---

## 8. CFD와 epluone/sample.md

`epluone/sample.md`는 `epluone/` 디렉토리를 GitHub에 유지하기 위한 placeholder 문서이다.

```text
epluone/sample.md
=
placeholder document
```

`sample.md`는 CFD 문서가 아니라,  
`epluone/` 디렉토리가 root 하위에 존재하도록 놓인 최소 파일이다.

따라서 AI는 `sample.md`를 CFD 설명문이나 CFD source로 읽는 것이 아니라,  
epluone directory placeholder로 읽어야 한다.

---

## 9. CFD와 백테스팅

현시점 CFD는 응용 target value이며,  
이후 CFD 백테스팅이나 계산 실험과 연결될 수 있다.

```text
CFD
=
current application target value

CFD backtesting
=
experiment / validation candidate process
```

다만 CFD 백테스팅 결과는 곧바로 proof completion이 아니다.

```text
CFD backtesting result
≠
proof completion
```

CFD 백테스팅 결과는 먼저 experiment trace 또는 candidate validation material로 읽는다.

```text
backtesting result
=
experiment trace
+
candidate validation material
```

---

## 10. CFD와 local Linux / Oracle IDC server

local Linux Ubuntu server는 Oracle IDC server로 가기 전의 staging/test layer이다.

```text
local_linux_ubuntu_server
=
staging
+
test
+
git operation field
```

Oracle IDC server는 장시간 계산과 CFD 백테스팅을 위한 experiment execution layer이다.

```text
oracle_idc_server
=
long-running experiment
+
CFD backtesting field
```

따라서 CFD 작업의 실행 흐름은 다음처럼 읽을 수 있다.

```text
SeungeFlow Seed.Base
→
CFD target value
→
local Linux staging/test
→
Oracle IDC long-running experiment
→
result trace
→
thinking_flow or source candidate
→
meta.md candidate judgment
```

---

## 11. CFD와 relation

CFD와 SeungeFlow의 관계는 identity relation이 아니라,  
current application target relation이다.

```text
CFD
=
current application target relation
```

CFD는 다음과 relation될 수 있다.

```text
epluone
Structure_Principle
SeungeFlow_Thinking
Active_Schema
backtesting result
local Linux server
Oracle IDC server
```

그러나 이 relation은 merge가 아니다.

```text
relation
≠
merge
```

AI는 CFD를 다른 문서나 디렉토리와 병합하는 것이 아니라,  
각 boundary를 보존한 채 application target relation으로 읽어야 한다.

---

## 12. CFD 문서 생성 기준

CFD 관련 새 문서를 만들 때는 먼저 문서 유형을 판단한다.

```text
CFD guide
=
main/README_of_CFD.md

CFD thinking flow
=
SeungeFlow_Thinking/thinking_flow/ 안의 flow 후보

CFD experiment trace
=
source / experiment / candidate layer

CFD meta.md
=
독립된 자리개념 boundary가 확인될 때만 후보
```

좋은 CFD 관련 생각이 나왔다고 해서 바로 meta.md가 되는 것이 아니라,  
기존 schema와 중복 검토를 거쳐 독립 boundary가 확인될 때 meta.md 후보가 된다.

```text
좋은 CFD 생각
≠
즉시 meta.md
```

---

## 13. CFD를 읽을 때의 금지되는 오독

AI는 다음을 하면 안 된다.

```text
CFD를 epluone의 identity로 읽기
CFD를 Seed.Base의 identity로 읽기
CFD를 Structure_Principle/schema/ 내부 core로 직접 병합하기
CFD backtesting result를 proof completion으로 읽기
epluone/sample.md를 CFD source로 읽기
README_of_CFD.md를 CFD 자체로 읽기
CFD relation을 merge로 읽기
```

위 항목은 CFD를 낮추기 위한 금지가 아니라,  
CFD를 정확한 `[body]` target value 자리에 놓기 위한 guard이다.

---

## 14. 최단 정의

```text
README_of_CFD.md
=
현시점 epluone의 [body] slot에 놓인 target value인 CFD를 읽기 위한 guide document이다.

CFD는 epluone의 identity가 아니라 현재 body slot의 target value이며,
Seed.Base 전체의 identity가 아니라 현재 응용 target이다.

CFD 관련 실험과 백테스팅은 proof completion이 아니라,
experiment trace와 candidate validation material로 먼저 읽는다.
```