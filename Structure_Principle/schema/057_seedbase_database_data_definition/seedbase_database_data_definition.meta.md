---
id: schema.057.seedbase_database_data_definition
type: active_schema_metadata
filename: seedbase_database_data_definition.meta.md
status: active
prev: schema.056.current_core_alignment_for_runtime
---

# META: seedbase_database_data_definition

## role

schema.057.seedbase_database_data_definition은 GitHub-native Seed.Base에서 data의 정의를 기존 Data.Base와 구분하기 위한 기준 스키마다.

이 meta 파일의 목적은 인공지능이 Seed.Base를 기존 DB / DataBase / value table / row-column 구조로 환원하지 않도록 막는 것이다.

현시점 구조이론 기준에서 핵심은 다음이다.

```txt
문제는 GitHub가 DB냐 아니냐가 아니다.
문제는 data를 무엇으로 보느냐다.
```

## core_definition

```txt
Data.Base =
값 / 행 / 열 / 테이블 값 중심의 기존 DB적 data 보존 구조

Seed.Base =
schema / relation / history / directory / metadata / SVG / Seed / recovery trace / navigation까지 data로 보는 구조 보존층
```

## data_scope

### narrow_data

기존 Data.Base의 data 개념은 좁다.

```txt
숫자
문자열
값
row
column
field
table value
record value
```

이 관점에서는 schema, relation, directory, SVG, navigation, Seed, recovery trace가 data 바깥의 보조 구조처럼 보인다.

### wide_data

Seed.Base의 data 개념은 넓다.

```txt
schema
relation
history
path
directory
metadata
SVG
Seed
recovery trace
navigation
visible coordinate
relation anchor
boundary state
return path
history event index
center axis
```

이 관점에서는 구조적으로 보존되고, 재생성에 쓰이며, relation / boundary / return / history loop를 유지하는 모든 것이 data다.

## Seed.Base_definition

Seed.Base는 기존 DB가 아니다.

Seed.Base는 다음이다.

```txt
Seed.Base =
구조이론의 relation / boundary / return / history loop가
GitHub-native file graph 안에서 보존되고 재생성될 수 있도록
schema 자체와 relation 자체와 history 자체를 data로 다루는 기준 보존층
```

Seed.Base에서 data는 값이 아니라 다음이다.

```txt
보존 가능한 차이
재생성 가능한 관계
복귀 가능한 이력
읽을 수 있는 구조
보이는 relation field
경로화된 navigation
검산 가능한 recovery trace
```

## Data.Base_definition

Data.Base는 기존 DB적 data 보존 구조다.

Data.Base는 다음을 중심으로 작동한다.

```txt
value
row
column
table
query
index
transaction
record
field
```

Data.Base의 장점은 값 저장 / 검색 / 정렬 / 질의다.

그러나 현시점 구조이론 본류에서는 Data.Base가 중심이 아니다.

이유는 다음이다.

```txt
Data.Base는 relation 자체를 data로 보기 어렵다.
Data.Base는 schema 자체를 data로 보기보다 schema를 저장틀로 보는 경향이 강하다.
Data.Base는 history를 relation identity의 일부라기보다 log로 축소하기 쉽다.
Data.Base는 directory / SVG / navigation / recovery trace를 data 외부의 보조물로 처리하기 쉽다.
```

따라서 현시점 개발 대상은 Data.Base가 아니다.

현시점 개발 대상은 다음이다.

```txt
GitHub-native Seed.Base
```

## GitHub_SeedBase_DB

GitHub는 기존 DB가 아니다.

GitHub는 새로운 스타일의 Seed.Base DB다.

```txt
GitHub = Seed.Base DB
```

단, 여기서 DB는 기존 DB가 아니다.

```txt
기존 DB =
값 / 행 / 테이블 중심

GitHub Seed.Base DB =
schema 자체가 data
relation 자체가 data
history 자체가 data
directory 자체가 구조 영역 data
meta.md 자체가 AI-readable data
SVG 자체가 visible relation data
Seed 자체가 기준 data
recovery trace 자체가 복구판정 data
navigation 자체가 relation 경로 data
path 자체가 visible coordinate data
```

## GitHub_SeedBase_mapping

```txt
repository =
Seed.Base DB 전체장

directory =
table-like structural data area

schema directory =
schema table-like data area

meta.md =
AI-readable data

image / SVG =
visible relation data

relation_history.md =
history data / append-only relation trace

README.md / MAIN.md =
human navigation data

Active_navimap.svg =
visible navigation data

commit history =
temporal trace data

Seed =
basis data / 기준 data

recovery log =
recovery trace data

path =
visible coordinate data

relation identity =
Seed / relation_history / schema_identity / navigation_layer로 보존되는 구조 data
```

## directory_rule

GitHub-native Seed.Base에서 하나의 directory는 하나의 table-like structural data area다.

```txt
directory = table-like structural data area
```

그러나 directory path는 relation identity가 아니다.

```txt
path = visible coordinate data
relation identity = Seed / relation_history / schema_identity / navigation_layer
```

따라서 directory 이동이나 path 변경은 곧 relation death가 아니다.

relation death 여부는 다음이 판정한다.

```txt
Seed
relation_history
schema_identity
navigation_layer
return_path
history_event_index
```

## schema_as_data

Seed.Base에서 schema는 data다.

```txt
schema 자체가 data다.
```

schema는 data를 담는 그릇만이 아니다.

schema는 다음을 포함한다.

```txt
id
role
core alignment
relation rule
boundary rule
return rule
history rule
forbidden rule
related schema
shortest compression
```

따라서 schema.056 자체도 data다.
schema.057 자체도 data다.

## relation_as_data

Seed.Base에서 relation은 data다.

```txt
relation 자체가 data다.
```

relation은 단순 link가 아니다.

relation은 다음을 포함한다.

```txt
relation_anchor
source_schema
target_schema
boundary_state
return_path
history_event_index
navigation_layer
```

따라서 relation은 path보다 우선한다.

```txt
path는 relation의 visible coordinate일 수 있으나,
path 자체가 relation identity는 아니다.
```

## history_as_data

Seed.Base에서 history는 data다.

```txt
history 자체가 data다.
```

history는 단순 log가 아니다.

history는 relation identity와 recovery 판단에 들어가는 구조 data다.

```txt
relation_history.md =
append-only history data
```

history가 필요한 이유는 다음이다.

```txt
무엇이 언제 생성되었는가
무엇이 어떤 relation으로 연결되었는가
무엇이 이동되었는가
무엇이 수정되었는가
무엇이 끊겼는가
무엇이 복귀 가능한가
```

## SVG_as_data

Seed.Base에서 SVG는 data다.

```txt
SVG 자체가 visible relation data다.
```

SVG는 단순 이미지 파일이 아니다.

SVG / image는 다음을 보존해야 한다.

```txt
relation_anchor
boundary_state
return_path
history_event_index
center_axis
visible_relation_field
```

따라서 draw 산출물은 단순 그림이 아니라 visible_relation_field data다.

## metadata_as_data

Seed.Base에서 meta.md는 data다.

```txt
meta.md 자체가 AI-readable data다.
```

meta.md는 설명문이 아니다.

meta.md는 AI가 구조를 다시 읽고 재생성하기 위한 data다.

meta.md가 보존해야 할 최소 항목은 다음이다.

```txt
schema_id
domain
center_axis
relation_anchor
boundary_state
return_path
history_event_index
render_target
source_seed
related_schema
forbidden
shortest
```

## recovery_trace_as_data

Seed.Base에서 recovery trace는 data다.

```txt
recovery trace 자체가 data다.
```

복구는 단순 재연결이 아니다.

```txt
연결됨 ≠ 복구됨
```

recovery는 다음 gate를 통과해야 한다.

```txt
identity
trace
return
boundary
Seed integrity
anti-false
anti-hallucination
meaning
stop
```

따라서 recovery log는 단순 로그가 아니라 복구 판단을 위한 trace data다.

## navigation_as_data

Seed.Base에서 navigation은 data다.

```txt
navigation 자체가 data다.
```

navigation은 단순 안내가 아니다.

navigation은 relation이 다시 읽히고, 사람이 따라가고, AI가 재생성할 수 있도록 하는 경로 data다.

```txt
README / MAIN =
human navigation data

Active_navimap.svg =
visible navigation data

meta relation index =
AI navigation data
```

## SeedBase_vs_DataBase

```txt
Data.Base =
값을 저장한다.

Seed.Base =
구조가 다시 살아날 수 있는 기준을 보존한다.
```

```txt
Data.Base =
row / column / table 중심

Seed.Base =
schema / relation / history / directory / metadata / SVG / navigation 중심
```

```txt
Data.Base =
data를 값으로 본다.

Seed.Base =
data를 보존 가능한 구조적 차이와 재생성 가능한 관계로 본다.
```

```txt
Data.Base =
query로 값을 찾는다.

Seed.Base =
navigation과 relation_history로 구조를 복귀시킨다.
```

```txt
Data.Base =
schema는 저장틀이다.

Seed.Base =
schema 자체가 data다.
```

```txt
Data.Base =
history는 log다.

Seed.Base =
history는 relation identity와 recovery 판단 data다.
```

```txt
Data.Base =
path는 저장 위치다.

Seed.Base =
path는 visible coordinate data일 뿐 relation identity가 아니다.
```

## relation_to_schema_056

schema.057은 schema.056을 보완한다.

schema.056은 runtime / renderer / GitHub layer로 내려가기 전 core alignment를 고정했다.

```txt
000 = 정중심
025 = runtime boundary gate
050 = formed_formula
054 = balance center rule
```

schema.057은 이 core alignment가 GitHub-native Seed.Base로 내려갈 때, 무엇을 data로 볼 것인지 정의한다.

056에서 보존해야 하는 항목들은 모두 Seed.Base data다.

```txt
schema_id = schema identity data
center_axis = center data
boundary_state = boundary data
relation_anchor = relation data
history_event_index = history data
return_path = return data
render_target = visible relation data
```

따라서 schema.057의 판정은 다음이다.

```txt
056은 중심 정렬 기준이다.
057은 data 정의 기준이다.
```

## forbidden

```txt
Seed.Base를 기존 DataBase로 환원하지 않는다.
data를 숫자 / 문자열 / row / column / table value로 축소하지 않는다.
schema를 data 외부의 저장틀로만 보지 않는다.
relation을 단순 link로 보지 않는다.
history를 단순 log로 보지 않는다.
directory를 단순 path로 보지 않는다.
meta.md를 단순 설명문으로 보지 않는다.
SVG를 단순 이미지 파일로 보지 않는다.
navigation을 단순 안내문으로 보지 않는다.
recovery trace를 단순 복구 로그로 보지 않는다.
GitHub path를 relation identity로 보지 않는다.
Seed.Base를 절대 진리로 보지 않는다.
Data.Base 기준으로 Seed.Base를 정규화하지 않는다.
```

## source_code

```python
schema_057_seedbase_database_data_definition = {
    "id": "schema.057.seedbase_database_data_definition",
    "type": "active_schema_metadata",
    "status": "active",
    "prev": "schema.056.current_core_alignment_for_runtime",
    "core_definition": {
        "Data.Base": "value_row_column_table_centered_data_storage",
        "Seed.Base": "schema_relation_history_directory_metadata_svg_seed_recovery_navigation_as_data"
    },
    "data_scope": {
        "narrow_data": [
            "number",
            "string",
            "value",
            "row",
            "column",
            "field",
            "table_value",
            "record_value"
        ],
        "wide_data": [
            "schema",
            "relation",
            "history",
            "path",
            "directory",
            "metadata",
            "SVG",
            "Seed",
            "recovery_trace",
            "navigation",
            "visible_coordinate",
            "relation_anchor",
            "boundary_state",
            "return_path",
            "history_event_index",
            "center_axis"
        ]
    },
    "github_seedbase_mapping": {
        "repository": "Seed.Base_DB_field",
        "directory": "table_like_structural_data_area",
        "schema_directory": "schema_table_like_data_area",
        "meta.md": "AI_readable_data",
        "image_or_SVG": "visible_relation_data",
        "relation_history.md": "append_only_history_data",
        "README.md_or_MAIN.md": "human_navigation_data",
        "Active_navimap.svg": "visible_navigation_data",
        "commit_history": "temporal_trace_data",
        "Seed": "basis_data",
        "recovery_log": "recovery_trace_data",
        "path": "visible_coordinate_data",
        "relation_identity": [
            "Seed",
            "relation_history",
            "schema_identity",
            "navigation_layer"
        ]
    },
    "principles": {
        "schema_as_data": True,
        "relation_as_data": True,
        "history_as_data": True,
        "directory_as_data": True,
        "metadata_as_data": True,
        "svg_as_data": True,
        "seed_as_data": True,
        "recovery_trace_as_data": True,
        "navigation_as_data": True,
        "path_is_identity": False,
        "path_is_visible_coordinate": True
    },
    "relation_to_schema_056": {
        "schema_056": "core_alignment_standard",
        "schema_057": "data_definition_standard",
        "schema_id": "schema_identity_data",
        "center_axis": "center_data",
        "boundary_state": "boundary_data",
        "relation_anchor": "relation_data",
        "history_event_index": "history_data",
        "return_path": "return_data",
        "render_target": "visible_relation_data"
    },
    "forbidden": [
        "reduce_SeedBase_to_conventional_DataBase",
        "reduce_data_to_row_column_value",
        "treat_schema_as_only_storage_frame",
        "treat_relation_as_simple_link",
        "treat_history_as_simple_log",
        "treat_directory_as_simple_path",
        "treat_meta_md_as_description_only",
        "treat_SVG_as_image_file_only",
        "treat_navigation_as_guide_only",
        "treat_recovery_trace_as_log_only",
        "treat_GitHub_path_as_relation_identity",
        "normalize_SeedBase_by_DataBase_rules"
    ],
    "shortest": "Seed.Base = schema/relation/history/directory/meta/SVG/navigation까지 data로 보는 GitHub-native DB"
}
```

## relation

```txt
prev:
schema.056.current_core_alignment_for_runtime

related:
schema.000_dot
schema.025_AI_memory_field
schema.050_hunminjeongeum_vector_operation
schema.054_balance_center_structure
schema.056.current_core_alignment_for_runtime
```

## current_judgment

현시점 판정은 다음이다.

```txt
GitHub는 기존 DB가 아니다.
GitHub는 schema 자체를 data로 다루는 새로운 스타일의 Seed.Base DB다.
```

따라서 Data.Base와 Seed.Base의 차이는 저장 매체의 차이가 아니라 data 정의의 차이다.

```txt
Data.Base는 값을 data로 본다.
Seed.Base는 구조가 다시 살아날 수 있게 하는 모든 보존 가능한 차이와 관계를 data로 본다.
```

## one_line

GitHub Seed.Base DB에서 data는 값이 아니라 schema / relation / history / directory / meta / SVG / Seed / recovery / navigation까지 포함하는 구조적 보존 단위다.

## shortest

```txt
057 = Data.Base는 값 중심 / Seed.Base는 구조 자체를 data로 봄
```