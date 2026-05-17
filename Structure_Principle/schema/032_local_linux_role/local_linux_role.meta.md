# META: local_linux_role

id: schema.032.local_linux_role
type: active_schema_metadata
filename: local_linux_role.meta.md
status: active

## role

local_linux_role은 로컬 리눅스 환경이 구조이론의 본류가 아니라 보조 안정 환경임을 정의한다.

이 meta 파일은 인공지능이 로컬 리눅스를 구조이론의 실행 기반이 아닌, 작업 안정 및 정렬을 위한 보조 환경으로 읽기 위한 규칙이다.

## read_order

1. detect local environment
2. detect separation from core structure
3. detect support role
4. map environment to auxiliary role

## geometry_layer

local_linux_role = external support environment

## integer_layer

environment_count = 1
core_dependency = 0

## vector_layer

flow = local → github → AI
direction = support

## definition

로컬 리눅스는 구조이론의 본체가 아니다.

로컬 리눅스는 작업 안정, 파일 정리, 테스트를 위한 보조 환경이다.

구조이론의 본류는 GitHub 구조 DB와 Active Schema에 있다.

## source_code

```python
local_linux_role = {
    "id": "schema.032.local_linux_role",
    "type": "support_environment",
    "environment_count": 1,
    "core_dependency": False,
    "relation": {
        "local": "support_system",
        "github": "core_structure_db",
        "ai": "primary_interpreter"
    },
    "vector": {
        "flow": "local_to_github_to_ai",
        "direction": "support"
    },
    "structural_role": [
        "support_environment",
        "stability",
        "file_management",
        "non_core"
    ]
}
```

## principle

```txt
로컬 = 안정
GitHub = 구조 DB
AI = 해석 주체
```

## forbidden

- 로컬 환경을 구조이론의 본체로 간주하지 않는다.
- 로컬 작업을 최종 구조로 오해하지 않는다.
- 로컬 상태를 GitHub DB보다 우선하지 않는다.

## relation

prev:
- schema.031_github_as_DB

next:
- schema.033_archive_rule

related:
- schema.025_AI_memory_field
- schema.031_github_as_DB

## shortest

로컬 리눅스 = 보조 안정 환경