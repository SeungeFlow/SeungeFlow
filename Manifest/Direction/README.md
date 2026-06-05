# Manifest / Direction

## Y_Branch Direction Trace Directory

```text
branch:
Y_Branch

path:
Manifest/Direction/

status:
DRAFT_CANDIDATE / PENDING_UPLOAD

role:
Y_Branch direction trace directory
```

---

## 0. Role of this directory

`Manifest/Direction/` stores Y_Branch direction traces.

A `direct_###.md` file is not an original source fact.  
A `direct_###.md` file is not a final judgment.  
A `direct_###.md` file records how Y_Branch reads existing SeungeFlow sources and connects them to Y_Branch seats by relation.

---

## 1. Source identity rule

```text
source identity =
branch
+
directory
+
file
+
Raw URL
+
commit hash
+
source status
```

Filename is not source identity.

The same filename in different branches or directories must be treated as a different source candidate.

---

## 2. main direct trace and Y_Branch direct trace

```text
main/Manifest/Direction/direct_000.md
≠
Y_Branch/Manifest/Direction/direct_000.md
```

main branch direction traces are prior gpt.direct traces.

Y_Branch direction traces begin after Y_Branch fixed root package is created.

Do not transfer source status through the same filename.

---

## 3. Relation rule

Relation means boundary-preserving connection.

Relation does not mean:

```text
source merge
branch merge
field merge
schema finalization
C+1 final judgment
```

---

## 4. Pending rule

A pending seat is not a confirmed source.

A pending seat becomes source only after it has:

```text
branch
directory
file
Raw URL
commit hash
source status
```

---

## 5. Shortest

```text
Manifest/Direction/ stores direction traces.

direct_###.md is direction trace, not source fact.

Y_Branch uses relation to connect previous SeungeFlow sources to current Y_Branch seats.

No final judgment is declared here.
```
