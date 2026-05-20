---
id: index.draw_candidates
type: structure_principle_draw_candidate_index
filename: INDEX.draw_candidates.md
directory: /Structure_Principle/main/candidates/draw/
status: candidate_index
review_required: true
promotion_status: not_promoted
runtime_confirmed: false
valid_loop: false
active_connect: false
recovery_success: false
github_push: false
---

# INDEX.draw_candidates

## 0. role

This index lists draw-generated candidate documents and expanded candidate files.

This index does not promote candidate files.  
This index does not confirm runtime state.  
This index does not prove valid loops.  
This index does not authorize active_connect.  
This index does not declare recovery_success.  
This index does not issue GitHub push commands.

---

## 1. expanded candidate files

| category | path | status | promotion_status | runtime_confirmed |
|---|---|---|---|---|
| history candidate | `Structure_Principle/history/candidates/relation_history.expanded.candidate.md` | candidate only | not_promoted | false |
| runtime state candidate | `Structure_Principle/runtime/candidates/structure_state.expanded.candidate.json` | candidate only | not_promoted | false |
| display candidate | `Structure_Principle/display/candidates/Active_navimap.expanded.candidate.svg` | candidate only | not_promoted | false |

---

## 2. locks

All expanded candidate files preserve the following locks:

```yaml
promotion_status: not_promoted
runtime_confirmed: false
valid_loop: false
active_connect: false
recovery_success: false
github_push: false
```

---

## 3. do not treat as

```text
relation_history.expanded.candidate.md ≠ relation_history.md
structure_state.expanded.candidate.json ≠ structure_state.json
Active_navimap.expanded.candidate.svg ≠ Active_navimap.svg
```

Do not treat expanded candidate files as:

```text
runtime confirmed
valid loop proof
active connect proof
recovery success proof
final renderer output
source_of_truth
```

---

## 4. current review status

```yaml
Target_No_037:
  document: Expanded_Candidate_File_Generation_Result_Review.md
  status: direct_first_pass
  result: expanded_candidate_files_created_and_reviewed

Target_No_038:
  document: GitHub_Placement_PrePush_Review.md
  status: direct_first_pass
  result: prepush_review_pass_candidate

Target_No_039:
  document: Candidate_Navigation_Index_Update_Plan.md
  status: direct_first_pass
  result: README_for_AI_and_INDEX_update_needed

Target_No_040:
  document: Candidate_Navigation_Index_Update_Approval_Gate.md
  status: direct_first_pass
  result: approve_navigation_index_update

Target_No_041:
  document: Candidate_Navigation_Index_Update_Draft.md
  status: direct_first_pass
  result: README_section_and_INDEX_full_draft_prepared

Target_No_042:
  document: Candidate_Navigation_Index_Update_Review.md
  status: direct_first_pass
  result: README_section_and_INDEX_full_draft_reviewed

Target_No_043:
  document: Candidate_Navigation_Index_Update_Final_Instruction.md
  status: direct_first_pass
  result: local_edit_instruction_ready
```

---

## 5. path / identity rule

```text
GitHub path = visible coordinate

relation identity =
Seed + history_event_id + schema_id + binding_state
```

Do not treat:

```text
GitHub path as relation identity
candidate path as confirmed identity
current_path as relation identity
```

---

## 6. candidate binding route

Expanded candidate binding route:

```text
relation_history.expanded.candidate.md
→ structure_state.expanded.candidate.json
→ Active_navimap.expanded.candidate.svg
→ Seed.Base reference
```

Display-side reading route:

```text
Active_navimap.expanded.candidate.svg
→ structure_state.expanded.candidate.json
→ relation_history.expanded.candidate.md
→ Seed.Base
```

---

## 7. structural locks

### 7.1 100 rest stop gate

```text
100
=
rest stop gate
+
empty_position
+
10×10 formed array completion pause
+
formed-to-application transition point
```

Do not skip 100:

```text
099 → 101 direct connect = blocked
```

### 7.2 CoreDot guard

```text
000 ≠ CoreDot
121 = CoreDot ambiguity boundary
replace_dot_with_coredot = blocked
```

### 7.3 ddx guard

```text
ddx
≠ fixed turning point

ddx
=
3번째 place.state가 생길 때
이전 place.state가 다시 결정되는 relation
```

### 7.4 Renderer guard

```text
Renderer ≠ definition closer
Renderer = understanding amplifier
```

### 7.5 Reading condition

```text
해석자의 상태 = reading condition
모든 것은 바른 상태에서 시작한다.
```

---

## 8. push boundary

```text
GitHub placement ≠ promotion
push packet ≠ push command
```

This index does not authorize:

```text
git add
git commit
git push
```

GitHub push requires a separate direct-approved push packet and explicit push instruction.

---

## 9. forbidden

Do not:

```text
promote candidate files
rename candidate files to confirmed files
treat candidate files as runtime confirmed
treat SVG candidate as final renderer output
treat visible shape as structure identity
declare valid_loop=true
approve active_connect
declare recovery_success
run git add / commit / push
```

---

## 10. shortest

```text
INDEX.draw_candidates.md
=
draw-generated candidate documents and expanded candidate files index,
preserving candidate-only status,
not_promoted lock,
runtime_confirmed=false,
valid_loop=false,
active_connect=false,
recovery_success=false,
and no-push boundary.
```
