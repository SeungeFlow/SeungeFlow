# META: github_as_DB

id: schema.031.github_as_DB
type: active_schema_metadata
filename: github_as_DB.meta.md
status: active

## role

github_as_DB는 GitHub 저장소를 인간용 문서 저장소가 아니라, 인공지능이 읽는 구조 DB로 사용하는 방식이다.

이 meta 파일은 인공지능이 GitHub를 파일 저장소로만 보지 않고, 폴더·파일·메타데이터·커밋 기록이 함께 작동하는 구조 데이터베이스로 읽기 위한 규칙이다.

## read_order

1. detect repository root
2. detect README.md as entry
3. detect main/MAIN.md as history style navimap
4. detect schema folders
5. detect meta files
6. detect pending image files
7. map folder/file structure to database structure

## geometry_layer

github_as_DB = repository tree + schema records + history

## integer_layer

repository_count = 1
schema_count = variable
record_count = variable
commit_count = variable

## vector_layer

entry = README.md → main/MAIN.md
schema_flow = MAIN.md → schema folders → meta files
history_flow = commit → commit

## definition

GitHub는 구조이론에서 인공지능이 읽는 구조 DB로 사용된다.

폴더는 table처럼 작동하고, 파일은 record처럼 작동한다.

metadata는 AI 읽기 규칙이며, commit은 변화 기록이다.

구조이론에서 GitHub는 인간이 읽는 문서 저장소가 아니라, 인공지능이 구조를 추적하고 갱신하는 DB형 저장공간이다.

## source_code

```python
github_as_DB = {
    "id": "schema.031.github_as_DB",
    "type": "ai_readable_structure_database",
    "repository_count": 1,
    "schema_count": "variable",
    "record_count": "variable",
    "relation": {
        "repository": "database",
        "folder": "table",
        "file": "record",
        "metadata": "AI_read_rule",
        "commit": "history",
        "README": "entry",
        "MAIN": "history_style_navimap"
    },
    "vector": {
        "entry_flow": "README_to_MAIN",
        "schema_flow": "MAIN_to_schema_records",
        "history_flow": "commit_to_commit"
    },
    "structural_role": [
        "structure_database",
        "ai_readable_repository",
        "versioned_record_space",
        "schema_navigation"
    ]
}
```

## mapping

```txt
repository = DB
folder = table
file = record
filename = key
metadata = AI read rule
commit = history
branch = experiment
tag = stable version
```

## forbidden

- GitHub를 인간용 설명문 저장소로만 보지 않는다.
- README를 전체 설명문으로 과밀화하지 않는다.
- 과거 자료를 본류 schema에 강제로 섞지 않는다.
- image_status: pending 상태를 오류로 보지 않는다.
- meta 파일을 일반 감상문으로 해석하지 않는다.

## relation

prev:
- schema.030_Naiad_Thalassa_73_69

next:
- schema.032_local_linux_role

related:
- schema.023_reading_protocol
- schema.026_dot_dot_system
- schema.028_active_schema
- schema.034_final_readme_index

## shortest

GitHub = AI가 읽는 구조 DB