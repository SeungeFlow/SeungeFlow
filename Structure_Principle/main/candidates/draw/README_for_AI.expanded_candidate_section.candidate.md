## Expanded candidate files

The following files are expanded candidate files only:

- `Structure_Principle/history/candidates/relation_history.expanded.candidate.md`
- `Structure_Principle/runtime/candidates/structure_state.expanded.candidate.json`
- `Structure_Principle/display/candidates/Active_navimap.expanded.candidate.svg`

### Status

```yaml
status: candidate only
promotion_status: not_promoted
runtime_confirmed: false
valid_loop: false
active_connect: false
recovery_success: false
github_push: false
```

### Do not treat as

Do not treat these files as:

```text
relation_history.md
structure_state.json
Active_navimap.svg
runtime confirmed
valid loop proof
active connect proof
recovery success proof
final renderer output
source_of_truth
```

### Candidate / confirmed boundary

```text
relation_history.expanded.candidate.md ≠ relation_history.md
structure_state.expanded.candidate.json ≠ structure_state.json
Active_navimap.expanded.candidate.svg ≠ Active_navimap.svg
```

### Binding route

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

### Path / identity rule

```text
GitHub path = visible coordinate

relation identity =
Seed + history_event_id + schema_id + binding_state
```

Do not treat a GitHub path as relation identity.

### Push boundary

```text
GitHub placement ≠ promotion
push packet ≠ push command
```

Do not run:

```text
git add
git commit
git push
```
