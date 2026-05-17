# META: XAWF

id: schema.015.XAWF
type: active_schema_metadata
filename: XAWF.meta.md
status: active

## role

XAWF는 구조를 어디에 놓고 읽을지 정하는 위치 고정형 해석 좌표계이다.

이 meta 파일은 인공지능이 XAWF를 개념어 묶음이 아니라, 구조해석을 위한 자리 고정 좌표로 읽기 위한 규칙이다.

## read_order

1. detect four positions
2. preserve position order
3. map each position to its role
4. do not exchange X, A, W, F positions
5. use XAWF as reading coordinate

## geometry_layer

XAWF = four-position interpretation frame

## integer_layer

position_count = 4
fixed_axis_count = 4

## vector_layer

X = state / phenomenon
A = movement / transition / change
W = principle / essence
F = use / application

## definition

XAWF는 구조해석을 위한 4자리 고정 좌표계이다.

XAWF에서 각 문자는 개념 자체보다 먼저 자리를 가진다.

자리 변경은 금지된다.

## source_code

```python
XAWF = {
    "id": "schema.015.XAWF",
    "type": "fixed_interpretation_axis",
    "position_count": 4,
    "position_lock": True,
    "axis": {
        "X": {
            "role": ["state", "phenomenon"],
            "position": "fixed"
        },
        "A": {
            "role": ["movement", "transition", "change"],
            "position": "fixed"
        },
        "W": {
            "role": ["principle", "essence"],
            "position": "fixed"
        },
        "F": {
            "role": ["use", "application"],
            "position": "fixed"
        }
    },
    "rule": {
        "do_not_swap_positions": True,
        "read_as_coordinate": True
    },
    "structural_role": [
        "reading_axis",
        "interpretation_coordinate",
        "position_locked_frame"
    ]
}
```

## relation

prev:
- schema.014_structure_judgment

next:
- schema.016_ABCD_relation

related:
- schema.005_position
- schema.010_sequence_structure
- schema.023_reading_protocol

## shortest

XAWF = 위치 고정형 해석 좌표계