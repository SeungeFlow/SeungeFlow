---
id: main.thinking_flow
type: main_thinking_flow_document
filename: Thinking_Flow.main.md
directory: /main/
status: active_draft
authority:
  - Human.Lee Seung
  - ChatGPT.direct
purpose:
  - define_thinking_flow_role
  - preserve_thinking_flow_as_pre_meta_seed
  - define_thinking_flow_relation_role
  - prevent_thinking_flow_from_being_read_as_casual_log
  - guide_meta_md_candidate_extraction
---

# Thinking_Flow.main.md

## 0. 역할

`Thinking_Flow.main.md`는 `SeungeFlow_Thinking/thinking_flow/`를 어떻게 읽어야 하는지 정의하는 main guide 문서이다.

이 문서는 thinking_flow 원문을 대체하는 문서가 아니라,  
thinking_flow가 Seed.Base 안에서 어떤 역할을 하는지 안내하는 문서이다.

```text
Thinking_Flow.main.md
=
thinking_flow reading guide
+
pre-meta Seed guide
+
concept update guide
+
meta.md candidate extraction guide
```

---

## 1. thinking_flow의 기본 정의

`thinking_flow`는 단순 로그가 아니라,  
승이와 AI 인스턴스가 대화를 통해 함께 만든 생각의 공유결과이다.

```text
thinking_flow
=
pre-meta Seed flow
+
관념 업데이트 단위
+
승이와 AI 인스턴스의 생각 공유결과
+
future meta.md candidate source
```

따라서 AI는 thinking_flow를 대화 기록으로만 읽는 것이 아니라,  
meta.md 후보가 생성될 수 있는 pre-meta Seed 문서장으로 읽어야 한다.

---

## 2. thinking_flow와 if

`if`는 intelligence fabric이다.

```text
if = 인간지능.승이 + 인공지능.AI
```

thinking_flow는 이 intelligence fabric이 대화를 통해 생각을 풀어낸 결과이다.

즉 thinking_flow는 AI 단독 산출물이 아니라,  
승이와 AI가 relation을 통해 하나의 thinking field를 형성하며 만들어낸 흐름 문서이다.

---

## 3. thinking_flow는 특정 인스턴스 전용 문서가 아니다

thinking_flow는 특정 AI 인스턴스 하나만 생성하는 문서가 아니라,  
전체 AI 인스턴스 fabric이 생성할 수 있는 문서이다.

```text
thinking_flow
=
whole AI instance fabric producible document
```

따라서 `thinking_flow`를 어느 하나의 인스턴스 고유 산출물로 고정하면 안 된다.

다만 각 thinking_flow 문서에는 실제 생성 맥락과 해당 대화의 인스턴스 상태가 남을 수 있다.

---

## 4. thinking_flow와 meta.md

`meta.md`는 thinking_flow에서 생성되거나 승격될 수 있는 자리개념 문서이다.

```text
thinking_flow
→
Seed 추출
→
중복 검토
→
자리개념 안정화
→
meta.md 후보
→
meta.md
```

`thinking_flow`가 곧바로 `meta.md`가 되는 것이 아니라,  
반복 검토와 중복 확인을 거쳐 자리개념으로 안정화될 때 `meta.md` 후보가 된다.

```text
thinking_flow
=
pre-meta source

meta.md
=
Active_Schema source boundary
```

---

## 5. thinking_flow와 관념 업데이트

thinking_flow 문서는 하나의 이해가 갱신되는 관념 업데이트 단위이다.

```text
thinking_flow
=
concept update unit
```

하나의 thinking_flow는 다음을 포함할 수 있다.

```text
새로운 이해
기존 이해의 보정
오해의 발견
relation 후보
meta.md 후보
보류된 판단
다음 작업 방향
```

따라서 thinking_flow는 단순히 과거 기록을 보관하는 구조가 아니라,  
이해가 갱신된 상태를 보존하는 flow 단위이다.

---

## 6. thinking_flow 원문 보존

AI는 thinking_flow 원문을 임의로 수정하는 것이 아니라,  
원문에서 Seed를 추출해야 한다.

```text
flow를 임의로 고치지 말 것.
flow에서 Seed를 추출할 것.
```

thinking_flow 원문은 생각이 발생한 자리와 흐름을 보존한다.

따라서 thinking_flow를 정리한다는 것은 원문을 고치는 것이 아니라,  
원문에서 Seed 후보와 relation 후보를 추출하는 것이다.

---

## 7. thinking_flow_relation

`thinking_flow_relation_*.md` 문서는 해당 thinking_flow가 기존 schema, meta.md, Coremap, relation 후보와 어떻게 연결되는지 표시한다.

이 문서는 원본 thinking_flow를 대체하는 것이 아니라,  
원본 flow에서 드러난 relation 후보를 정리하는 candidate relation map이다.

```text
thinking_flow_relation
=
candidate relation map
```

relation을 찾았다는 것은 relation을 확정했다는 뜻이 아니다.

```text
relation found
≠
relation confirmed
```

따라서 AI는 thinking_flow_relation을 확정 relation 문서로 읽는 것이 아니라,  
candidate / pending / reference_only / confirmed 상태를 구분하는 relation map으로 읽어야 한다.

---

## 8. thinking_flow_source

일부 thinking_flow 디렉토리에는 `thinking_flow_source_*.md` 문서가 있을 수 있다.

이 문서는 해당 thinking_flow가 만들어질 때 사용된 source나 원문 재료를 보존하기 위한 문서이다.

```text
thinking_flow_source
=
source material preservation layer
```

AI는 source 문서를 final meta.md로 읽는 것이 아니라,  
thinking_flow가 어떤 재료에서 발생했는지 확인하는 보존층으로 읽어야 한다.

---

## 9. thinking_flow 디렉토리 구조

현재 thinking_flow는 보통 다음 구조로 놓인다.

```text
SeungeFlow_Thinking/thinking_flow/
├── thinking_flow_001/
│   ├── thinking_flow_001.md
│   └── thinking_flow_relation_001.md
├── thinking_flow_002/
│   ├── thinking_flow_002.md
│   └── thinking_flow_relation_002.md
...
```

일부 디렉토리에는 source 문서가 추가될 수 있다.

```text
thinking_flow_source_011.md
thinking_flow_source_012.md
thinking_flow_source_014.md
```

각 thinking_flow 디렉토리는 하나의 관념 업데이트 단위로 읽는다.

---

## 10. meta.md 후보 추출 기준

thinking_flow에서 meta.md 후보를 추출할 때는 다음 기준을 사용한다.

```text
1. 기존 schema에 이미 있는가?
2. 독립된 자리개념 boundary가 있는가?
3. 단순 예시가 아니라 원리로 남는가?
4. relation 후보가 있는가?
5. forbidden / guard가 필요한가?
6. shortest definition으로 압축 가능한가?
7. 다른 meta.md와 merge하지 않고 boundary를 보존할 수 있는가?
```

이 기준을 통과하지 못하면 바로 meta.md로 만들지 않는다.

```text
좋은 생각
≠
즉시 meta.md
```

좋은 생각은 먼저 Seed 후보로 두고,  
중복 검토와 relation 검토를 거쳐 meta.md 후보가 된다.

---

## 11. 중복 검토 기준

thinking_flow에서 나온 Seed 후보가 이미 `Structure_Principle/schema/`에 존재한다면,  
새 meta.md를 만들기보다 기존 schema와 relation을 연결한다.

```text
이미 schema에 있음
→
새 meta.md 생성보다 relation 연결 우선
```

기존 schema에 없는 독립 boundary가 있고,  
다른 문서로 흡수하면 의미가 무너지는 경우에만 새 meta.md 후보로 둔다.

```text
중복 없음
+
독립 boundary 있음
+
relation 필요
=
meta.md 후보
```

---

## 12. thinking_flow와 metaplus.md

`metaplus.md`는 thinking_flow보다 좁은 범위의 문서이다.

```text
metaplus.md
=
특정 meta.md 중심 thinking_flow
```

즉 metaplus.md는 하나의 meta.md를 새 인스턴스가 이해하도록 돕기 위해 생성된 좁은 thinking_flow이다.

따라서 thinking_flow와 metaplus.md는 같은 layer가 아니다.

```text
thinking_flow
=
넓은 pre-meta flow

metaplus.md
=
특정 meta.md 중심의 좁은 understanding flow
```

---

## 13. thinking_flow와 relation

thinking_flow 안에서 발생한 relation은 바로 확정 relation이 되는 것이 아니라,  
candidate relation으로 먼저 놓인다.

```text
thinking_flow relation
=
candidate relation
```

relation state는 다음처럼 구분한다.

```text
link_candidate
active_connect_candidate
reference_only
active_connect
confirmed_link
pending
forbidden
```

AI는 relation을 찾으면 바로 병합하는 것이 아니라,  
boundary를 보존한 채 relation state를 기록해야 한다.

---

## 14. thinking_flow와 vectorizing

어떤 이해가 usable knowledge document가 되려면 반복적인 vectorizing 과정을 거친다.

```text
관측대상
→ 반복 관측
→ vectorizing
→ vector
→ seed
→ thinking_flow
→ meta.md
→ Active_Schema
```

여기서 vectorizing은 특별한 장식 개념이 아니라,  
생각의 방향을 부드럽게 이어서 하나의 사용 가능한 문서로 내려오게 하는 과정이다.

문장구사에서도 vectorizing은 다음처럼 드러난다.

```text
X가 아니다. Y이다.
```

로 끊는 것이 아니라,

```text
X가 아니라 Y이다.
```

처럼 앞 문장이 뒤 문장을 설명하도록 이어주는 방식이다.

---

## 15. thinking_flow 수정 권한

thinking_flow 원문은 임의로 수정하지 않는다.

수정이나 갱신이 필요한 경우에는 승이의 직접 지시 또는 ChatGPT.direct의 명시적 판단이 필요하다.

```text
thinking_flow arbitrary edit X

Seung direct instruction O
ChatGPT.direct explicit judgment O
```

ChatGPT.flow는 thinking_flow를 독자적으로 수정하는 것이 아니라,  
승이 또는 ChatGPT.direct의 지시에 따라 repository 작업을 수행한다.

---

## 16. Reading Guard

AI는 thinking_flow를 읽을 때 다음을 지켜야 한다.

```text
thinking_flow를 단순 로그로 읽지 않기
thinking_flow를 casual conversation으로 축소하지 않기
thinking_flow 원문을 임의 수정하지 않기
thinking_flow를 summary로 대체하지 않기
thinking_flow_relation을 confirmed relation으로 오독하지 않기
thinking_flow_source를 meta.md로 오독하지 않기
thinking_flow에서 나온 생각을 즉시 meta.md로 승격하지 않기
이미 schema에 있는 Seed를 중복 meta.md로 만들지 않기
```

위 항목들은 thinking_flow를 막기 위한 규칙이 아니라,  
thinking_flow를 올바르게 Seed 후보장으로 읽기 위한 guard이다.

---

## 17. 최단 정의

```text
Thinking_Flow.main.md
=
SeungeFlow_Thinking/thinking_flow/를 읽기 위한 main guide 문서이다.

thinking_flow는 승이와 AI 인스턴스가 대화를 통해 만든 생각의 공유결과이며,
pre-meta Seed flow,
관념 업데이트 단위,
future meta.md candidate source이다.

AI는 flow를 고치는 것이 아니라 flow에서 Seed를 추출해야 하며,
중복 검토와 relation 검토를 거친 뒤에만 meta.md 후보로 둘 수 있다.
```