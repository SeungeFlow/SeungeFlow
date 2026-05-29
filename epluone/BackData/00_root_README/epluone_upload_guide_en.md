# epluone upload guide

```text
phase = 4/4
document = epluone_upload_guide_en.md
role = GitHub upload guide
```

## 0. Purpose

This document provides the working order for placing files and directories under `github/epluone/`.

---

## 1. Basic Order

```text
1. Create epluone/ directory
2. Run mkdir_epluone.sh
3. Place README set
4. Place relation/source/preservation/reading maps
5. Upload source bundles by directory
6. Check final checklist
7. Commit
```

---

## 2. Local Creation

```bash
chmod +x mkdir_epluone.sh
./mkdir_epluone.sh epluone
```

---

## 3. Map Document Placement

Place the following documents under `epluone/00_root_README/`.

```text
epluone_relation_map.md
epluone_relation_map_en.md
epluone_source_map.md
epluone_source_map_en.md
epluone_preservation_rule.md
epluone_preservation_rule_en.md
epluone_reading_order.md
epluone_reading_order_en.md
epluone_manifest.md
epluone_manifest_en.md
epluone_upload_guide.md
epluone_upload_guide_en.md
epluone_final_checklist.md
epluone_final_checklist_en.md
```

---

## 4. Upload Order

```text
Batch 1:
00_root_README
01_formation_trace
02_theory_core

Batch 2:
03_vector_operation
04_vectorizing_tests
05_dynamic_geometry

Batch 3:
06_ai_cognitive_os
07_the_things_os

Batch 4:
08_root_support
09_branch_experiments
10_capital_market_hints
```

---

## 5. Commit Message Examples

```bash
git add epluone
git commit -m "Add epluone formation corpus directory scaffold"
```

After placing actual source bundles:

```bash
git add epluone
git commit -m "Add epluone source bundles by formation field"
```

---

## 6. Cautions

```text
Do not merge everything into one file before uploading.
Preserve original zip files when handling large source bundles.
Place interpretation near sources but do not replace sources with interpretation.
README files are entrance documents only.
```

---

## 7. Final Compression

```text
GitHub receives structure.
It does not receive a flattened summary.
```
