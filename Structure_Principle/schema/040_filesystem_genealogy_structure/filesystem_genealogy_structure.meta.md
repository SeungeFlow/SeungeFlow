# META: filesystem_genealogy_structure

id: schema.040.filesystem_genealogy_structure
type: active_schema_metadata
filename: filesystem_genealogy_structure.meta.md
status: active

## role

filesystem_genealogy_structure는 서버의 디렉토리 구조를 Root 기반의 세대·항렬·관계거리 구조로 해석하는 통합 예시 구조이다.

이 meta 파일은 인공지능이 filesystem을 단순 폴더 트리가 아니라, root에서 분기되는 genealogy 구조로 읽기 위한 규칙이다.

## read_order

1. detect root directory
2. detect child directories
3. detect depth
4. detect sibling nodes
5. detect path length
6. map filesystem path to genealogy relation

## geometry_layer

filesystem_genealogy_structure = root + branch + depth + path

## integer_layer

root_depth = 0
generation_depth = depth
path_length = relation_integer
sibling_layer = same_depth

## vector_layer

root → child
parent → child
node → node through path
direction = hierarchical path flow

## definition

서버의 디렉토리 구조는 단순한 폴더 트리가 아니다.

구조이론에서 filesystem은 root를 기준으로 분기되는 세대·항렬·관계거리 구조로 읽는다.

Root는 조상 기준점이고, depth는 세대이며, sibling은 항렬이고, path length는 촌수이다.

따라서 filesystem은 genealogy 구조로 해석될 수 있다.

## source_code

```python
filesystem_genealogy_structure = {
    "id": "schema.040.filesystem_genealogy_structure",
    "type": "filesystem_genealogy_mapping",
    "relation": {
        "filesystem": "genealogy",
        "root": "ancestor_origin",
        "directory": "descendant_node",
        "depth": "generation",
        "sibling": "hangryeol",
        "path_length": "chon_su",
        "path": "relation_route"
    },
    "mapping": {
        "/root": "0_generation",
        "/root/A": "1_generation",
        "/root/A/B": "2_generation",
        "/root/A/B/C": "3_generation"
    },
    "vector": {
        "root_to_child": "generation_flow",
        "node_to_node": "path_relation_flow",
        "direction": "hierarchical"
    },
    "structural_role": [
        "filesystem_mapping",
        "genealogy_structure",
        "path_length_integer",
        "root_based_relation"
    ]
}
```

## principle

```txt
filesystem = genealogy
root = 조상 기준점
depth = 세대
sibling = 항렬
path length = 촌수
```

```txt
DIR = 경로
genealogy = 거리 해석
filesystem = 실제 구현
```

## example

```txt
/root/A/B/C
=
root → A → B → C
=
0대 → 1대 → 2대 → 3대
```

```txt
A ↔ B = 같은 depth = 같은 항렬
A1 ↔ B1 = 같은 세대 = 같은 층
A1 ↔ A2 = 형제 관계
```

## relation

prev:
- schema.039_genealogy_root_structure

related:
- schema.031_github_as_DB
- schema.038_DIR_structure
- schema.039_genealogy_root_structure

## shortest

path length = 촌수