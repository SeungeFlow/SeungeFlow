# META: genealogy_root_structure

id: schema.039.genealogy_root_structure
type: active_schema_metadata
filename: genealogy_root_structure.meta.md
status: active

## role

genealogy_root_structure는 족보의 뿌리구조, 항렬, 대, 촌수를 구조이론의 관계정수로 해석하는 예시 구조이다.

이 meta 파일은 인공지능이 족보를 단순 혈연 기록이 아니라, 세대·항렬·관계거리·정수 읽기 구조로 해석하기 위한 규칙이다.

## read_order

1. detect root ancestor
2. detect generation order
3. detect 항렬 position
4. detect relation distance
5. map 촌수 to integer relation
6. read genealogy as root-relation structure

## geometry_layer

genealogy_root_structure = root + generation layers + relation branches

## integer_layer

root_count = 1
generation_count = variable
relation_distance = 촌수
generation_index = 대

## vector_layer

root → descendant
generation_n → generation_n+1
relation = branch_distance

## definition

족보는 뿌리에서 갈라져 나가는 관계 구조이다.

대는 세대 기준이다.

1대는 기준 세대이고, 2대는 다음 세대이다.

항렬은 같은 세대 또는 같은 관계층에 놓이는 자리 기준이다.

촌수는 관계를 읽어내는 정수이다.

구조이론에서 족보는 뿌리, 세대, 항렬, 관계거리, 정수로 읽는다.

## source_code

```python
genealogy_root_structure = {
    "id": "schema.039.genealogy_root_structure",
    "type": "root_relation_integer_structure",
    "root_count": 1,
    "generation_count": "variable",
    "relation": {
        "root": "ancestor_origin",
        "generation": "대",
        "generation_1": "base_generation",
        "generation_2": "next_generation",
        "hangryeol": "same_generation_position_rule",
        "chon_su": "integer_relation_distance"
    },
    "vector": {
        "flow": "root_to_descendant",
        "generation_flow": "generation_n_to_generation_n_plus_1",
        "relation_flow": "branch_to_branch"
    },
    "structural_role": [
        "root_structure",
        "generation_layer",
        "relation_integer",
        "position_rule",
        "family_tree_mapping"
    ]
}
```

## principle

```txt
족보 = 뿌리구조
항렬 = 같은 관계층의 자리 기준
대 = 세대 기준
촌수 = 관계를 읽어내는 정수
```

```txt
1대 = 기준
2대 = 다음 기준
촌수 = 관계거리
```

## relation

prev:
- schema.038_DIR_structure

related:
- schema.006_entity
- schema.008_integer
- schema.010_sequence_structure
- schema.016_ABCD_relation
- schema.031_github_as_DB

## shortest

촌수 = 관계를 읽어내는 정수