---
id: main.coremap
type: structure_principle_main_document
filename: Coremap.main.md
directory: /Structure_Principle/main/
status: active_draft
scope:
  target: Structure_Principle
  role: core_relation_map_foundation
  source_range: 000~121
depends_on:
  - main.baseline
  - schema.066.principle_entity_relation_rule
  - schema.067.meta_relation_boundary_bridge
  - schema.099.document_sorting_index
  - schema.120.seedbase_working_schema_memory_asset_structure
  - schema.121.coredot_ambiguity_boundary
---

# Coremap.main

## 0. role

`Coremap.main.md`는 `Structure_Principle/schema/`의 122개 core를 번호순 요약표로 나열하는 문서가 아니다.

이 문서는 각 core의 boundary를 보존한 채, core 사이의 relation을 mapping하기 위한 기초 지도이다.

```text
Coremap.main.md
=
core boundary preserving relation map
```

금지:

```text
coremap ≠ file list
coremap ≠ concept dictionary
coremap ≠ summary table
coremap ≠ merge map
```

정의:

```text
coremap
=
independent core entities
+
boundary-preserving relation edges
+
source / candidate / reference / pending distinction
+
link/connect state
```

## 1. coremap node schema

각 core node는 다음 field를 가진다.

```yaml
core:
  id:
  directory:
  number:
  name:
  phase:
  meta_file:
  metaplus_file:

  core_boundary:
    definition:
    shortest:
    role:
    not:

  metaplus_layer:
    correction:
    guard:
    relation_trace:
    pending:

  relation:
    prev:
    next:
    related:
    source:
    target:
    forbidden:
    pending:

  map_state:
    link:
    connect:
    active:
    reference_only:
```

## 2. relation edge schema

각 edge는 다음 형식을 따른다.

```yaml
edge:
  from:
  to:
  relation:
  meaning:
  type:
  state:
  guard:
```

`state`는 다음 중 하나다.

```text
link_candidate
confirmed_link
active_connect
reference_only
pending
forbidden
```

## 3. global phase map

```text
000~014 = structure validation phase
015~024 = operation-axis validation phase
025~028 = AI-readable active unit formation phase
029~030 = relation-field application examples
031~034 = GitHub-native preservation / support / archive / index phase
035~039 = real-system / orbit / overlap / interval-route / root-relation example phase
040~044 = filesystem genealogy / learning engine / dynamic renderer / SVG forming / angle bridge phase
045~049 = DIR reinforcement / flip transition / shell renderer / sphere-shell distinction / field reveal phase
050~054 = formed_formula / failure-as-Seed / hyper-renderer architecture / definition emergence / movable balance center phase
055~059 = purpose preservation / runtime core alignment / SeedBase data definition / human-side pre-alignment / empty_place-present-dot_anchor alignment phase
060~064 = coherency gate / vector unlock trace / place-domain / boundary requirement / place-overlap phase
065~069 = ⊕ common operator / principle entity boundary / relation bridge / Ctp x-dx-ddx / ddx right-triangle transition phase
070~074 = right-triangle fold-unfold / 3→2 overlap / 2→1 triangle overlap / 73-69 structural triangle / science-based implementation guard phase
075~079 = chemical formula renderer / electron shell visible layer / H2O angle implementation / vector operation external engine separation / Cheonjiin vowel-direction trace phase
080~084 = observer body vector frame / inner vowel pull / square center vowel orbit / WAXF rhombus direction field / BADㆍC orbit reference separation phase
085~089 = opposed correspondence / ani boundary judgment / mat boundary correspondence / vowel-place overlap / Hangul word layer distinction phase
090~094 = Hanja compression reading / structure principle rename / principle hidden layer / SVO-SOV subject anchor / principle-explains-phenomenon phase
095~099 = place source index / vector relation index / science candidate index / reference_only trace index / document sorting gate phase
100~104 = understanding_flow reserved gate / three-dot raw reading / phase boundary distinction / Circle closed return field / boundary contact relation phase
105~109 = center-radius-diagonal-crossing vocabulary / cell-center segment rule / triangle surface-vector distinction / inside-left condition / Ctp structure integer table phase
110~114 = nine-zero return overlap / angle-grid resolution / candle parent-field / OHLC rhombus-to-BADㆍC mapping / Close-to-next-Open transition phase
115~119 = Y branch guard / circle-container inclusion / structural sequence number / pin-dot-Y return / flow-transition self-operation phase
120~121 = SeedBase working memory asset system / CoreDot ambiguity boundary closure phase
```

## 4. primary flow map

```text
000 dot
→ 001 line
→ 002 surface
→ 003 cell
→ 004 boundary
→ 005 position
→ 006 entity
→ 007 safety
→ 008 integer
→ 009 vector
→ 010 sequence
→ 011 swap
→ 012 matrix_product
→ 013 return_preservation
→ 014 structure_judgment
```

Meaning:

```text
minimum place
→ connection
→ closure
→ unit place area
→ separation interface
→ value/state place
→ bounded independent unit
→ boundary preservation
→ count / structure measure
→ directional relation flow
→ repeated relation
→ position exchange
→ matrix operation
→ return / preservation
→ structure validation
```

## 5. operation-axis flow

```text
014 structure_judgment
→ 015 XAWF
→ 016 ABCD_relation
→ 017 diagonal_relation
→ 018 eight_direction
→ 019 center_point
→ 020 crossing_point
→ 021 fold_unfold
→ 022 scale_change
→ 023 reading_protocol
→ 024 operation_axis_judgment
```

Meaning:

```text
structure validation
→ fixed reading coordinate
→ direct / non-direct relation frame
→ diagonal non-direct reading
→ direction field
→ balance center
→ shared relation point
→ layout transformation
→ scale reinterpretation
→ AI reading protocol
→ operation-axis validation
```

## 6. Active unit formation map

```text
024 operation_axis_judgment
→ 025 AI_memory_field
→ 026 dot_dot_system
→ 027 Seed.Base
→ 028 Active.Schema
→ 029 human_relation_structure
→ 030 Naiad_Thalassa_73_69
```

Meaning:

```text
operation axis checkpoint
→ AI memory field
→ image + metadata pair
→ baseline
→ operational schema unit
→ human relation field example
→ orbital / sequence relation example
```

## 7. repository / archive / index map

```text
030 strong relation example
→ 031 GitHub as DB
→ 032 local Linux support
→ 033 archive rule
→ 034 README / MAIN index
```

Meaning:

```text
strong example
→ structure DB
→ support environment
→ separated preservation
→ AI reading route
```

## 8. renderer / orbit / route map

```text
035 connectome
→ 036 orbit
→ 037 disk array torus
→ 038 DIR
→ 039 genealogy root
→ 040 filesystem genealogy
→ 041 dynamic engine
→ 042 dynamic renderer
→ 043 forming SVG renderer
→ 044 angle structure
```

Meaning:

```text
real system mapping
→ repeated path
→ closed overlapping orbit
→ interval route
→ root relation
→ filesystem path mapping
→ learning cycle
→ dynamic renderer
→ SVG forming state
→ planar-to-spatial angle bridge
```

## 9. field reveal / renderer correction map

```text
045 warp_weft_DIR
→ 046 flip_cycle
→ 047 shell_flip_orbit
→ 048 sphere_shell_distinction
→ 049 flip_boundary_spread
→ 050 Hunminjeongeum vector operation
→ 051 failure as Seed
→ 052 HyperRendererCore
→ 053 Structure_Principle flow
→ 054 balance center
```

Meaning:

```text
DIR grid reinforcement
→ transition overlap
→ shell difference
→ sphere/shell distinction
→ field reveal
→ sound/stroke/letter forming reveal
→ unclosed path preservation
→ renderer architecture
→ definition emergence process
→ movable balance center
```

## 10. runtime / SeedBase / place map

```text
055 Active.Schema purpose
→ 056 runtime core alignment
→ 057 SeedBase data definition
→ 058 SeungeFlow Thinking pre-alignment
→ 059 empty_place present understanding
→ 060 coherency
→ 061 vector_unlock
→ 062 place_domain
→ 063 boundary_place_requirement
→ 064 place_overlap
```

Meaning:

```text
purpose preservation
→ runtime alignment
→ data scope definition
→ human-side pre-alignment
→ empty place / present / dot-anchor
→ input-output vector alignment
→ vectorizing unlock trace
→ place as between-domain
→ boundary required for place
→ shared boundary absorption
```

## 11. relation / Ctp / triangle map

```text
064 place_overlap
→ 065 ⊕ common operator
→ 066 principle entity rule
→ 067 relation boundary bridge
→ 068 x dx ddx
→ 069 ddx right triangle
→ 070 right triangle fold/unfold
→ 071 3→2 place overlap
→ 072 2→1 triangle overlap
→ 073 structural triangle 73/69
→ 074 science-based implementation
```

Meaning:

```text
place overlap
→ boundary-preserving combination
→ independent principle entity
→ relation bridge
→ coordinate transition
→ ddx bend point
→ right triangle place occupancy
→ visible/effective count split
→ square cell formation
→ structural triangle relation
→ science-value implementation guard
```

## 12. science / vector external engine / vowel map

```text
074 science implementation
→ 075 chemical formula renderer
→ 076 electron shell
→ 077 H2O angle implementation
→ 078 vector operation external engine rule
→ 079 Cheonjiin vowel direction
→ 080 Sejong body observer frame
→ 081 inner vowel pull
→ 082 square center vowel orbit
→ 083 WAXF vowel rhombus
→ 084 BADㆍC orbit reference
```

Meaning:

```text
science-value implementation
→ chemical formula as structure
→ shell / valence boundary
→ H2O 104.5 condition rendering
→ external vector engine separation
→ input-order vowel direction
→ observer body frame
→ inner pull
→ center orbit
→ rhombus direction field
→ orbit reference separation
```

## 13. language / principle hidden layer map

```text
084 BADㆍC
→ 085 opposed correspondence
→ 086 ani boundary judgment
→ 087 mat boundary correspondence
→ 088 ani/chai vowel overlap
→ 089 Hangul word layer distinction
→ 090 Hanja compression
→ 091 Structure_Principle rename
→ 092 principle hidden layer
→ 093 SVO/SOV subject anchor
→ 094 left principle explains right phenomenon
```

Meaning:

```text
orbit reference
→ center-axis opposed correspondence
→ inner boundary judgment
→ boundary correspondence
→ vowel place overlap
→ word layer distinction
→ compressed meaning direction
→ naming alignment
→ hidden why-layer
→ subject dot-anchor
→ principle explains phenomenon
```

## 14. source / sorting / rebuilt active gate map

```text
094 principle explains phenomenon
→ 095 place source index
→ 096 vector operation relation index
→ 097 science renderer candidate index
→ 098 reference_only trace index
→ 099 document sorting index
→ 100 understanding_flow empty gate
→ 101 three-dot reading mode
```

Meaning:

```text
phenomenon explained by principle
→ source trace preservation
→ external vector relation index
→ science candidate index
→ high-density reference-only buffer
→ sorting gate
→ reserved empty gate
→ rebuilt active opening
```

## 15. rebuilt active chain map

```text
101 three-dot reading
→ 102 phase boundary
→ 103 Circle definition
→ 104 inscribed/circumscribed relation
→ 105 radius/center/diagonal/right-angle/crossing
→ 106 cell-center segment rule
→ 107 triangle/vector/point distinction
→ 108 inside-left condition
→ 109 structure integer property table
→ 110 9-0 transition
→ 111 angle-grid resolution
→ 112 candle subobject orbit
→ 113 BADㆍC-OHLC mapping
→ 114 Close→Next Open
→ 115 Y branch guard
→ 116 circle container inclusion
→ 117 structural sequence integer cell
→ 118 pin-dot-Y return
→ 119 flow transition self-operation
→ 120 SeedBase working memory asset
→ 121 CoreDot ambiguity boundary
```

Meaning:

```text
raw reading
→ phase boundary
→ closed return field
→ contact relation
→ center-axis vocabulary
→ center-to-center segment
→ triangle phase distinction
→ conditional direction/interiority
→ structure integer properties
→ end/start overlap
→ angle resolution
→ candle parent field
→ OHLC rhombus mapping
→ time transition
→ branch guard
→ container boundary
→ structural number sequence
→ pin branch return
→ event flow self-operation
→ working memory asset system
→ terminology ambiguity boundary
```

## 16. critical cross-links

### dot preservation cross-link

```yaml
edge:
  from: schema.000.dot
  to: schema.121.coredot_ambiguity_boundary
  relation: preserved_against_coredot_merge
  meaning: "dot은 000에서 최초 최소 자리로 보존되며, 121은 CoreDot이 dot을 덮어쓰지 못하게 한다."
  state: confirmed_link
```

### empty place cross-link

```yaml
edge:
  from: schema.059.empty_place_present_understanding
  to: schema.000.dot
  relation: retroactive_present_anchor_refinement
  meaning: "059는 dot을 현시점 anchor로 후속 보완하지만 000_dot을 replace하지 않는다."
  state: confirmed_link
```

### relation bridge cross-link

```yaml
edge:
  from: schema.067.meta_relation_boundary_bridge
  to: main.coremap
  relation: defines_coremap_edge_logic
  meaning: "coremap edge는 merge가 아니라 boundary-preserving relation bridge다."
  state: active_connect
```

### source sorting cross-link

```yaml
edge:
  from: schema.099.document_sorting_index
  to: main.coremap
  relation: defines_node_classification
  meaning: "principle_entity / interpretation_layer / applied_example / reference_only / pending 분류는 coremap 생성 기준이 된다."
  state: active_connect
```

### working schema cross-link

```yaml
edge:
  from: schema.120.seedbase_working_schema_memory_asset_structure
  to: main.coremap
  relation: defines_link_connect_distinction
  meaning: "coremap의 link는 relation potential이고, connect는 실제 작동 연결이다."
  state: active_connect
```

## 17. forbidden global edges

```yaml
forbidden_edges:
  - from: schema.121.coredot_ambiguity_boundary
    to: schema.000.dot
    forbidden_relation: replace_dot_with_coredot
    reason: "CoreDot은 ambiguity boundary 대상이며 dot의 본명이 아니다."

  - from: schema.078.vector_operation_external_engine_rule
    to: Structure_Principle.mainline
    forbidden_relation: merge_external_vector_engine_into_mainline
    reason: "벡터연산기법은 external engine relation으로 보존한다."

  - from: schema.098.reference_only_high_density_trace_index
    to: active_schema.mainline
    forbidden_relation: promote_reference_only_to_active_core
    reason: "강한 trace는 폐기하지 않지만 본류에 즉시 승격하지 않는다."

  - from: science_examples
    to: science_proof
    forbidden_relation: treat_visible_relation_field_as_scientific_proof
    reason: "과학 branch는 검증이 아니라 기존 과학값 기반 구현이다."
```

## 18. shortest

```text
Coremap.main.md
=
122개 core의 boundary를 보존하면서
relation / source / candidate / reference / pending / link / connect를 구분하는
Active.Schema relation map
```
