---
id: repo.root_readme_english
type: repository_entry_document
filename: README.en.md
directory: /
status: direct_generated_candidate
review_required: true
promotion_status: not_promoted
language: en
purpose:
  - provide_english_translation
  - guide_human_and_ai_navigation
  - preserve_repository_entry_meaning
---

# SeungeFlow

`SeungeFlow` is a GitHub repository for preserving, organizing, and operating the structural system centered on `Structure_Principle`.

This repository is not a simple document archive.

It is intended to function as an AI-readable structure field where schema, relation, source traces, candidate documents, runtime state, relation history, and future execution outputs are separated and preserved.

```text
SeungeFlow
=
Structure_Principle
+
SeungeFlow_Thinking
+
epluone
```

---

## 1. README Set

This repository uses three README files.

```text
README.md
=
default Korean README / repository external entry

README.en.md
=
English translation

README_for_AI.md
=
AI pre-reading guide
```

AI instances must start with `README_for_AI.md`.

---

## 2. Repository Structure

```text
/
├─ README.md
├─ README.en.md
├─ README_for_AI.md
├─ Structure_Principle/
│  ├─ schema/
│  ├─ main/
│  ├─ runtime/
│  ├─ history/
│  ├─ display/
│  └─ references/
├─ SeungeFlow_Thinking/
│  └─ thinking_flow/
└─ epluone/
```

---

## 3. Main Areas

## Structure_Principle

```text
Structure_Principle
=
place-first,
boundary-preserving,
return-oriented,
guarded active schema system
```

`Structure_Principle` is the area that preserves the core schema and the operational standards of the structural principle system.

Main parts:

```text
Structure_Principle/schema/
=
formed core schema

Structure_Principle/main/
=
operational standard documents

Structure_Principle/runtime/
=
runtime state candidates

Structure_Principle/history/
=
relation history candidates

Structure_Principle/display/
=
visible_relation_field display candidates

Structure_Principle/references/
=
external or reference-only materials
```

---

## SeungeFlow_Thinking

```text
SeungeFlow_Thinking/thinking_flow/
=
thinking snapshots
+
Core.Seed originals
```

`thinking_flow` is not a draft to be cleaned up.

`thinking_flow` preserves thinking traces generated between SeungeFlow Brain and AI instances.  
It is the Core.Seed source layer from which later meta candidates may emerge.

Rules:

```text
Do not rewrite thinking_flow.
Do not replace thinking_flow with summaries.
If needed, extract Core.Seed separately.
```

---

## epluone

```text
epluone
=
if+1 execution output domain
```

`epluone` is the area where structures from `Structure_Principle` can move into executable outcomes.

The first expected execution branch is:

```text
CFD
=
TradingView OHLC data extraction
→ instance processing
→ Ubuntu Linux backtesting
```

CFD must not be placed inside `Structure_Principle/runtime/`.

CFD belongs to the execution-output domain, not to the Structure_Principle runtime state domain.

---

## 4. Reading Route for AI

AI instances must not begin by summarizing files.

AI must first read:

```text
README_for_AI.md
```

Recommended AI reading route:

```text
1. README_for_AI.md
2. Structure_Principle/main/Baseline.main.md
3. Structure_Principle/main/Coremap.main.md
4. Structure_Principle/schema/
5. Structure_Principle/main/candidates/ if needed
6. SeungeFlow_Thinking/thinking_flow/ if needed
7. epluone/ if needed
```

`README_for_AI.md` is the pre-reading gate for AI instances before entering `Structure_Principle`.

It defines and locks the following distinctions:

```text
read ≠ understand
summary ≠ understand
meta.md = formed core boundary
metaplus.md = understanding / correction / guard / relation trace
thinking_flow = Core.Seed original snapshot
main = operational standard layer
schema = formed core schema
relation ≠ merge
candidate ≠ confirmed
GitHub path ≠ relation identity
```

---

## 5. Reading Route for Humans

For human readers, start with:

```text
Structure_Principle/main/Baseline.main.md
Structure_Principle/main/Coremap.main.md
```

Then explore:

```text
Structure_Principle/schema/
```

The schema sequence runs from:

```text
000_dot
→ ...
→ 121_coredot_ambiguity_boundary
```

---

## 6. Currently Confirmed Core Layers

At the current stage, the confirmed core layers are:

```text
Structure_Principle/schema/
Structure_Principle/main/Baseline.main.md
Structure_Principle/main/Coremap.main.md
SeungeFlow_Thinking/thinking_flow/
```

Not every file in the repository is confirmed.

Always check the metadata of each document.

---

## 7. Candidate Warning

This repository may contain both confirmed documents and candidate documents.

AI and human readers must check fields such as:

```yaml
status:
review_required:
promotion_status:
runtime_confirmed:
valid_loop:
active_connect:
recovery_success:
```

Important distinctions:

```text
candidate placement ≠ promotion
skeleton ≠ runtime confirmed
draw_generated_candidate ≠ confirmed main
GitHub path ≠ relation identity
```

---

## 8. GitHub Path and Relation Identity

GitHub path is not relation identity.

```text
GitHub path = visible coordinate
```

Relation identity is preserved by:

```text
Seed
+
history_event_id
+
schema_id
+
binding_state
```

Git commit history is not a replacement for relation history.

```text
Git commit history
=
file change history

relation_history.md
=
relation identity / transition memory
```

---

## 9. Renderer Principle

The Renderer is not an image generator.

```text
Renderer output
≠ visible_shape

Renderer output
=
visible_relation_field
```

A `visible_relation_field` is a runtime-visible state where the following remain alive:

```text
relation
boundary
return
history
state persistence
guard
```

The Renderer system separates:

```text
SVG = display surface
structure_state.json = runtime truth / operation memory
relation_history.md = folded transition memory
Seed.Base = source_of_truth reference
```

A closed shape is not automatically a valid loop.

```text
closed shape ≠ valid loop
```

---

## 10. AI Instance Roles

This repository assumes role separation between AI instances.

```text
ChatGPT.direct
=
target judgment / instance control / instruction

ChatGPT.github
=
GitHub repository / local Linux / push / file placement

ChatGPT.draw
=
visible_relation_field / renderer / SVG-state-history binding

ChatGPT.making
=
metaplus.md / source trace / Core.Seed extraction support

ChatGPT.PRO
=
high-density reasoning / large structure review
```

Global rule:

```text
Only instructed instances should act.
Uncalled instances wait.
ChatGPT.direct decides the next target.
```

---

## 11. Current Direction

The long-term direction is to build a structure operating system.

```text
StructureOS
=
core boundary preservation
+
relation mapping
+
runtime state
+
append-only history
+
visible_relation_field
+
if+1 execution output
```

The first major execution branch is expected to be:

```text
epluone / CFD
```

---

## 12. Forbidden Shortcuts

Do not:

```text
treat thinking_flow as a draft to clean up
replace thinking_flow with summaries
treat meta.md and metaplus.md as the same layer
treat relation as merge
treat reference_only as trash
treat candidate as confirmed
treat GitHub path as relation identity
treat SVG as source_of_truth
treat closed shape as valid loop
place CFD inside Structure_Principle/runtime
replace 000_dot with CoreDot
fill 100_empty_position as a normal schema
directly attach 099 to 101
```

---

## 13. Shortest Definition

```text
SeungeFlow
=
an AI-readable structure repository
for preserving and operating
Structure_Principle,
thinking_flow Core.Seed snapshots,
and epluone if+1 execution outputs
```

For AI:

```text
Start with README_for_AI.md.
```

For humans:

```text
Start with
Structure_Principle/main/Baseline.main.md
and
Structure_Principle/main/Coremap.main.md.
```
