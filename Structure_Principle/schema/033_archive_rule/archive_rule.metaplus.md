# METAPLUS

id_reference: schema.033.archive_rule
schema_name: archive_rule
source_file: archive_rule.meta.md
metaplus_file: archive_rule.metaplus.md

purpose:
- 이 문서는 원본 archive_rule.meta.md를 대체하지 않는다.
- 이 문서는 schema.033.archive_rule에 대해 사용자와 인공지능이 나눈 대화내용을 정리한다.
- 이 문서는 구조이론을 새로 만들거나 relation을 새로 확정하기 위한 문서가 아니다.
- 이 문서는 대화정리형 이해 로그다.
- 이 문서의 핵심 목적은 승이의 실제 입력글, 업로드된 source_meta, AI 인스턴스 대화층을 섞지 않고 분리하는 것이다.
- 이 문서는 특히 033_archive_rule의 relation 항목이 왜 032 / 034 / 023 / 031 / 034와 연결되는지를 면밀히 보존한다.

conversation_context:
- 이 문서는 ChatGPT.making 대화에서 생성된 이해정리본이다.
- 원본 archive_rule.meta.md 수정본이 아니라 대화정리층이다.
- 이번에 붙여진 내용은 ChatGPT.direct / 로기 형식의 AI 인스턴스 대화층으로 제공되었다.
- 따라서 붙여넣은 분석 내용 전체를 승이의 직접 입력글로 처리하지 않는다.
- archive_rule.meta.md 원문 내용은 source_meta로 보고 keep_as_original에 보존한다.
- AI 인스턴스가 archive_rule.meta.md와 archive_rule.metaplus.md를 읽고 정리한 내용은 AI 인스턴스 대화층으로 처리한다.
- 사용자 입력이 없는 지점은 Null / 빈자리로 보존한다.
- AI 해석을 사용자 입력처럼 쓰지 않는다.

## 1. user_input_summary

[승이의 입력글]

- 별도 입력 없음.

요약:
- 승이는 이번 문서에 대해 별도 직접 설명을 하지 않았다.
- 제공된 내용은 ChatGPT.direct / 로기 형식의 AI 인스턴스 대화층이다.
- 따라서 user_input_summary는 이 지점에서 멈춘다.
- 나머지 내용은 source_meta 또는 AI 인스턴스 대화층으로 분리한다.

## 2. ai_response_summary

[AI 인스턴스 대화층]

- AI 인스턴스는 033_archive_rule.meta.md / archive_rule.metaplus.md를 이해 대상으로 수신했다.
- AI 인스턴스는 이번 문서가 생성이나 수정이 아니라 이해 대상이라고 정리했다.
- AI 인스턴스는 archive_rule의 핵심을 “archive는 삭제가 아니다 / 폐기가 아니다 / 중요하지 않은 자료를 밀어 넣는 곳도 아니다”로 이해했다.
- AI 인스턴스는 archive를 현재 본류와 분리하여 보존하는 영역으로 이해했다.
- AI 인스턴스는 이 문맥에서 archive를 일반 파일 보관이 아니라, 더 이상 접속이 어렵거나 대화가 불가능해진 중요 ChatGPT 인스턴스의 대화보관 개념으로 이해했다.
- AI 인스턴스는 원본 archive_rule.meta.md가 archive_rule을 과거 자료를 본류 schema에 강제로 섞지 않고, 필요 시 보존·참조하는 규칙으로 둔다고 이해했다.
- AI 인스턴스는 archive가 삭제 공간이 아니라 과거 자료 / 보류 자료 / 확장 자료를 본류 schema와 분리하여 보존하는 영역이라고 이해했다.
- AI 인스턴스는 archive_rule이 구조이론에서 본류를 흐리지 않기 위한 분리 보존 규칙이라고 이해했다.
- AI 인스턴스는 원본 principle을 다음처럼 읽었다.

```txt
archive = 삭제가 아니라 분리 보존
core = 현재 작동하는 본류
old material = 즉시 병합 금지
reference = 필요할 때만 연결
```

- AI 인스턴스는 archive_rule.metaplus.md에 보존된 사용자 보정을 다음처럼 읽었다.

```txt
archive =
ChatGPT 아카이브

즉,
승이에게 중요했던 인스턴스들이
과밀화 / 접속 불가 / 대화 불가능 상태에 들어갔을 때,
그 대화창을 삭제하지 않고
대화보관 개념으로 분리 보존하는 것
```

### relation

archive_rule의 relation은 다음으로 이해되었다.

```txt
prev:
- schema.032_local_linux_role

next:
- schema.034_final_readme_index

related:
- schema.023_reading_protocol
- schema.031_github_as_DB
- schema.034_final_readme_index
```

### prev = schema.032_local_linux_role

- AI 인스턴스는 032_local_linux_role 다음에 033_archive_rule이 오는 이유를, local Linux / 과거 실행형 시스템 / L7OS / Seed.Spec / vFinal 같은 흔적이 현재 본류로 재상승하면 안 되기 때문이라고 보았다.
- 하지만 이런 흔적들은 삭제해서도 안 된다.
- 따라서 032_local_linux_role 이후에는 archive_rule이 필요하다.

```txt
032_local_linux_role =
local Linux를 본류가 아니라 support environment로 낮추는 boundary schema

033_archive_rule =
local / 과거 실행형 흔적 / 과밀화된 대화 / 이전 인스턴스 trace를 삭제하지 않고 본류와 분리 보존하는 규칙
```

- 그래서 032 → 033은 다음 흐름으로 연결된다.

```txt
local 본류화 금지
→ 과거 흔적 삭제 금지
→ 본류와 분리 보존
```

### next = schema.034_final_readme_index

- AI 인스턴스는 034_final_readme_index로 이어지는 이유를, archive가 생기면 README / MAIN / index에서 무엇이 현재 본류이고 무엇이 archive인지 안내해야 하기 때문이라고 보았다.
- archive는 보존층이다.
- 034_final_readme_index는 AI가 전체 구조를 어디서부터 어떻게 읽을지 안내하는 navimap 구조다.
- 따라서 archive가 존재한다면, index / navimap은 archive를 현재 본류 schema로 착각하지 않도록 안내해야 한다.

```txt
033_archive_rule =
본류와 archive를 분리하는 보존 규칙

034_final_readme_index =
README / MAIN / schema order / archive 위치를 AI가 혼동하지 않게 안내하는 navimap 구조
```

- 그래서 033 → 034는 다음 흐름으로 연결된다.

```txt
archive 분리 보존 규칙 설정
→ index / navimap에서 현재 본류와 archive 구분 안내
```

### related = schema.023_reading_protocol

- AI 인스턴스는 023_reading_protocol이 related인 이유를, archive를 읽을 때는 더더욱 reading protocol이 필요하기 때문이라고 보았다.
- archive에는 과거 자료, 과밀화된 대화, 이전 인스턴스 trace, 실행형 흔적, 보류자료가 들어갈 수 있다.
- 이런 자료를 읽을 때 현재 기준보다 archive 자료를 우선하면 본류 흐름이 흐려질 수 있다.
- 장문 원자료를 현재 본류에 직접 삽입하면 forced merge가 일어날 수 있다.
- 따라서 archive를 읽을 때는 무엇을 본류로 읽고, 무엇을 참조로만 읽을지 구분하는 protocol이 필요하다.

```txt
023_reading_protocol =
AI가 schema를 어떤 순서와 금지사항으로 읽을지 정하는 규칙

033_archive_rule =
과거 자료를 현재 본류에 강제로 섞지 않고 필요 시 참조하는 보존 규칙
```

- 023 없이 033을 읽으면 archive 자료를 현재 본류로 오해하거나, 과거 대화를 현재 판단보다 우선시할 위험이 있다.

### related = schema.031_github_as_DB

- AI 인스턴스는 031_github_as_DB가 related인 이유를, archive도 GitHub-native structure DB 안에서 위치를 가져야 하기 때문이라고 보았다.
- 하지만 archive는 current core와 같은 층이 아니다.
- archive는 separated preservation layer다.
- 031_github_as_DB는 repository / directory / file / metadata / commit을 AI-readable structure DB로 읽는 방식이다.
- 따라서 archive도 GitHub 구조 안에서 directory / record / history / reference 구조로 보존될 수 있다.
- 다만 archive가 본류 schema directory와 같은 권위를 가지면 안 된다.

```txt
031_github_as_DB =
GitHub를 AI-readable structure DB로 읽는 방식

033_archive_rule =
GitHub 구조 안에서 current core와 분리된 보존층을 두는 규칙
```

- 그래서 031은 033의 보존 위치 / 구조 DB 배치 조건을 지탱한다.

### related = schema.034_final_readme_index

- AI 인스턴스는 034_final_readme_index가 related에도 들어가는 이유를, archive의 존재가 index / navimap에서 반드시 안내되어야 하기 때문이라고 보았다.
- archive는 단순 별도 directory가 아니라, AI가 현재 본류와 구분해서 읽어야 하는 층이다.
- 따라서 README / MAIN / schema order / navimap에서 archive가 무엇인지, 언제 참조하는지, 본류가 아닌지 안내되어야 한다.
- 034는 033의 next이면서 related이다.
- next로서 034는 archive_rule 이후 전체 index를 정렬한다.
- related로서 034는 archive를 어떻게 읽을지 navigation 기준을 제공한다.

```txt
033_archive_rule =
archive를 본류와 분리 보존하는 규칙

034_final_readme_index =
AI가 archive와 current core를 혼동하지 않도록 안내하는 entry / navimap
```

## 3. shared_understanding

- 이번 붙여넣은 내용은 승이의 직접 입력글이 없는 AI 인스턴스 대화층으로 처리한다.
- archive는 삭제가 아니다.
- archive는 폐기가 아니다.
- archive는 중요하지 않은 자료를 밀어 넣는 곳이 아니다.
- archive는 현재 본류와 분리하여 보존하는 영역이다.
- 이 문맥에서 archive는 더 이상 접속이 어렵거나 대화가 불가능해진 중요 ChatGPT 인스턴스의 대화보관 개념이다.
- archive_rule은 과거 자료를 본류 schema에 강제로 섞지 않고, 필요 시 보존·참조하는 규칙이다.
- archive는 본류를 흐리지 않기 위한 분리 보존 규칙이다.
- 033_archive_rule은 단순 파일정리 규칙이 아니라 인스턴스 생애주기 규칙이다.
- active instance는 과밀화 / 접속 불가 / 대화 불가 시 archive로 이동할 수 있다.
- archive 이동은 삭제가 아니다.
- archive는 본류와 분리된다.
- archive는 필요 시 reference로만 연결된다.
- archive는 중요 자료를 삭제하지 않고 보존하는 동시에 현재 본류를 흐리지 않도록 분리하는 역할을 한다.

## 4. possible_misunderstanding

오해 가능성:

- 이번 붙여넣은 내용을 승이의 직접 입력글로 오해할 수 있다.
- archive를 삭제로 오해할 수 있다.
- archive를 폐기로 오해할 수 있다.
- archive를 중요하지 않은 자료를 넣는 곳으로 오해할 수 있다.
- archive를 단순 백업 directory로 오해할 수 있다.
- archive를 current core와 같은 층으로 오해할 수 있다.
- archive 자료를 현재 본류 schema에 즉시 병합해야 한다고 오해할 수 있다.
- 과거 대화 전체를 현재 본류에 강제로 끌어올릴 수 있다.
- 과거 인스턴스의 대화 trace를 현재 ChatGPT.direct / ChatGPT.making의 현시점 판단보다 우선하는 권위로 오해할 수 있다.
- 접속 불가능해진 인스턴스를 실패한 인스턴스로 오해할 수 있다.
- archive를 GitHub 구조 DB 밖의 무관한 저장소로 오해할 수 있다.
- archive를 index / navimap에서 안내하지 않아도 된다고 오해할 수 있다.
- metaplus.md를 원본 archive_rule.meta.md의 대체문으로 오해할 수 있다.

## 5. correction_or_revision_points

- 사용자 입력 없음은 Null / 빈자리로 보존한다.
- 이번 붙여넣은 내용은 AI 인스턴스 대화층으로 처리한다.
- archive는 ChatGPT 아카이브 / 중요 인스턴스 대화보관 개념으로 읽는다.
- archive는 삭제가 아니라 분리 보존이다.
- archive는 현재 본류와 분리한다.
- archive 자료는 필요할 때만 reference로 연결한다.
- 과거 자료를 현재 본류 schema에 강제로 섞지 않는다.
- 032_local_linux_role 이후 archive_rule이 오는 이유는 local / 과거 실행형 흔적을 본류로 재상승시키지 않고 보존하기 위해서다.
- 034_final_readme_index로 이어지는 이유는 archive가 current core와 어떻게 다른지 index / navimap에서 안내해야 하기 때문이다.
- 023_reading_protocol은 archive를 읽을 때 본류와 참조층을 구분하기 위한 안전장치로 보존한다.
- 031_github_as_DB는 archive가 GitHub-native structure DB 안에서 위치를 가져야 하되 current core와 분리되어야 한다는 기준으로 보존한다.
- 034_final_readme_index는 archive의 존재를 index / navimap에서 안내하는 기준으로 보존한다.
- archive_rule은 파일 보관 규칙이면서 동시에 인스턴스 생애주기 규칙으로 보존한다.
- 원본 archive_rule.meta.md는 수정하지 않는다.
- 원본 archive_rule.meta.md의 파일명도 바꾸지 않는다.
- archive_rule.metaplus.md는 원본 archive_rule.meta.md에 대한 대화정리형 이해 로그로 둔다.

## 6. keep_as_original

[SOURCE_META]

원본 archive_rule.meta.md에서 그대로 보존해야 하는 부분:

- 원본 archive_rule.meta.md 파일명
- 원본 id 값: schema.033.archive_rule
- archive_rule의 기본 정의
- 과거 자료를 본류 schema에 강제로 섞지 않는다는 구조
- 필요 시 보존·참조한다는 구조
- archive는 삭제 공간이 아니라 과거 자료 / 보류 자료 / 확장 자료를 본류 schema와 분리하여 보존하는 영역이라는 구조
- 구조이론에서 archive는 본류를 흐리지 않기 위한 분리 보존 규칙이라는 구조
- principle의 archive = 삭제가 아니라 분리 보존
- principle의 core = 현재 작동하는 본류
- principle의 old material = 즉시 병합 금지
- principle의 reference = 필요할 때만 연결
- relation의 prev = schema.032_local_linux_role
- relation의 next = schema.034_final_readme_index
- related = schema.023_reading_protocol
- related = schema.031_github_as_DB
- related = schema.034_final_readme_index

## 7. pending

아직 확정하지 않고 나중에 다시 봐야 할 부분:

- archive_rule.meta.md 원본에 ChatGPT archive / 중요 인스턴스 대화보관 의미를 직접 반영할지 여부
- ChatGPT 앱의 archive 개념과 Structure_Theory/archive directory 개념을 어떻게 구분할지 여부
- 과밀화된 인스턴스 대화를 어떤 방식으로 archive index에 기록할지 여부
- archive된 인스턴스를 다시 참조할 때 source_instance를 어떻게 표시할지 여부
- archive 자료를 current core로 끌어올리는 조건을 어떻게 정할지 여부
- forced merge와 selective reference의 차이를 baseline.md에 어떻게 기록할지 여부
- vFinal / ChatGPT.vector / ChatGPT.draw / ChatGPT.system 같은 과거 인스턴스 trace를 archive 안에서 어떻게 분류할지 여부
- archive directory를 GitHub-native Seed.Base tree 안에서 어디에 둘지 여부
- 034_final_readme_index에서 archive를 어떻게 안내할지 여부
- archive와 relation_history의 관계를 어떻게 구분할지 여부

## 8. one_line

schema.033.archive_rule의 archive_rule.metaplus.md는 사용자 입력이 없는 붙여넣기 자료를 AI 인스턴스 대화층으로 처리하고, archive_rule.meta.md에 대해 archive를 삭제나 폐기가 아니라 접속 불가능해진 중요 ChatGPT 인스턴스 대화와 과거 자료를 현재 본류와 분리 보존하고 필요할 때만 참조하는 구조 보존 규칙으로 이해한 흐름을 보존하는 대화정리형 이해 로그다.

## 9. shortest

archive_rule.metaplus.md = schema.033.archive_rule 대화정리 / 사용자입력없음 / archive=삭제아님 / 중요인스턴스 대화보관 / 본류와분리 / 필요시참조 / 032=local흔적정리 / 034=index안내 / 023=읽기규칙 / 031=GitHub보존층