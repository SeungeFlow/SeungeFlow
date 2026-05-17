# META: flip_cycle_transition_structure

id: schema.046.flip_cycle_transition_structure
type: active_schema_metadata
filename: flip_cycle_transition_structure.meta.md
status: active

## role

flip_cycle_transition_structure는 이분 구조처럼 보이는 주기 구조 안에서, 정면에서는 보이지 않는 중첩 임계구간과 뒤집힘을 읽는 구조이다.

이 meta 파일은 인공지능이 10천간, 12지지, 60갑자를 단순 정수 조합이나 음양구조론으로 읽지 않고, 주기·중첩·임계구간·뒤집힘이 포함된 구조로 읽기 위한 규칙이다.

## read_order

1. detect paired states
2. detect visible opposition
3. detect hidden overlap zone
4. detect dawn-like transition zone
5. detect dusk-like transition zone
6. detect flip condition
7. map cycle to transition structure

## geometry_layer

flip_cycle_transition_structure = paired states + overlap zones + flip cycle

## integer_layer

visible_state_count = 2
overlap_zone_count = 2
cycle_count = 1
flip_state_count = variable

## vector_layer

state_A → overlap_A → state_B → overlap_B → state_A
direction = cyclic
flip = front_view → reverse_view

## definition

flip_cycle_transition_structure는 둘로 나뉘어 보이는 구조가 실제로는 두 개의 중첩 임계구간을 포함하는 주기 구조임을 나타낸다.

정면에서 보면 낮과 밤, 0과 1, 기준점과 활성점, 마이너스와 플러스처럼 둘로 보인다.

그러나 뒤집어 읽으면 박명, 노을, 중첩, 임계, 전이구간이 드러난다.

구조이론에서 이 구조는 음양구조론이 아니라, 이분으로 보이는 주기 안에 숨어 있는 중첩 임계구간을 읽는 flip-cycle 구조이다.

## source_code

```python
flip_cycle_transition_structure = {
    "id": "schema.046.flip_cycle_transition_structure",
    "type": "cycle_transition_with_overlap_and_flip",
    "visible_state_count": 2,
    "overlap_zone_count": 2,
    "cycle_count": 1,
    "relation": {
        "state_A": "night_or_zero_or_minus_or_base",
        "overlap_A": "dawn_twilight_critical_zone",
        "state_B": "day_or_one_or_plus_or_active",
        "overlap_B": "dusk_twilight_critical_zone",
        "cycle": "state_A_to_state_B_to_state_A",
        "flip": "reverse_reading_reveals_overlap"
    },
    "vector": {
        "flow": [
            "state_A",
            "overlap_A",
            "state_B",
            "overlap_B",
            "state_A"
        ],
        "direction": "cyclic",
        "flip": "front_view_to_reverse_view"
    },
    "structural_role": [
        "cycle_transition",
        "overlap_zone_detection",
        "critical_interval_reading",
        "flip_reading",
        "anti_binary_reduction"
    ]
}
```

## principle

```txt
둘로 보이는 구조는 실제로 둘만으로 닫히지 않는다.
```

```txt
state_A
→ overlap_A
→ state_B
→ overlap_B
→ state_A
```

```txt
밤 → 박명 → 낮 → 황혼 → 밤
```

```txt
0 → 중첩구간 A → 1 → 중첩구간 B → 0
```

## structural_note

```txt
10천간
12지지
60갑자
```

이 항목들은 여기서 단순 정수 조합으로 고정하지 않는다.

이 구조에서 중요한 것은 숫자표 자체가 아니라, 반복 주기 안에서 중첩구간과 뒤집힘이 발생한다는 점이다.

```txt
정면 = 상태쌍이 보임
뒤집힘 = 중첩구간이 보임
```

## forbidden

- 음양구조론으로 해석하지 않는다.
- 10천간, 12지지, 60갑자를 전통 상징체계 설명으로 확장하지 않는다.
- 단순한 0/1 이분법으로 축소하지 않는다.
- overlap zone을 오류나 빈칸으로 보지 않는다.
- 뒤집힘 없이 상태 A/B만으로 주기를 닫지 않는다.
- 특정 종교, 점술, 운세 해석으로 연결하지 않는다.

## relation

prev:
- schema.045_warp_weft_DIR_structure

related:
- schema.003_cell
- schema.004_boundary
- schema.010_sequence_structure
- schema.013_return_preservation
- schema.018_eight_direction
- schema.021_fold_unfold
- schema.022_scale_change
- schema.036_orbit_structure
- schema.044_angle_structure

## shortest

둘 사이에는 두 중첩구간이 있고, 뒤집어야 보인다.