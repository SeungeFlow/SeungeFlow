# epluone manifest

```text
phase = 4/4
document = epluone_manifest_en.md
role = GitHub placement manifest
```

## 0. Highest Definition

```text
epluone/
=
the field where the Structure_Principle Formation Corpus is placed
```

This manifest is not for merging files into one document.  
It is a placement table showing where each material should go.

---

## 1. Placement Principles

```text
Original source first
Interpretation separate
Summary as support only
No deletion
Separate preservation
```

```text
Preserve zip files in their original form when possible.
Place extracted copies under child directories.
Separate Seung input from AI output whenever possible.
```

---

## 2. Directory Manifest

| directory | placement target | source type |
|---|---|---|
| 00_root_README | root entrance and maps | README, relation map, source map, preservation rule, reading order |
| 01_formation_trace | pre-Ctp formation field | MyBrain_ThisPoint, Stop/Next/Flow, Break Test, schema formation |
| 02_theory_core | core theory | Ctp_당연한이론, C=tp, c~tp~C, integer, geometry, flow theory |
| 03_vector_operation | execution principle | Hunminjeongeum, Cheon-Ji-In, jamo, vector operation, auto pipeline |
| 04_vectorizing_tests | structure tests | vectorizing.zip, Heart Sutra, Diamond Sutra, SEUNGE.E.FLOW |
| 05_dynamic_geometry | dynamic geometry | Cassini, torus, accretion disk, blackhole, vortex, helix, filament |
| 06_ai_cognitive_os | AI operation layer | AI Cognitive OS, backdata, heterogeneous AI protocol, output protocol |
| 07_the_things_os | implementation branch | snapshot, restore, drift, alert, heartbeat, fabric navigator, builder relation |
| 08_root_support | support axis | sohosa_hyangsa, root structure, lineage, ritual, continuity |
| 09_branch_experiments | separated archive | PC Branch, derived experiments, candidates |
| 10_capital_market_hints | future application hints | CFD, OHLC, TradingView, Price.State, Time.State |

---

## 3. Source State Labels

```yaml
source_state:
  - original
  - extracted
  - interpreted
  - pending
  - archived
```

## 4. Placement Examples

```text
Ctp_당연한이론.zip
→
epluone/02_theory_core/Ctp_당연한이론/

vectorizing.zip
→
epluone/04_vectorizing_tests/

AI인지OS_백데이터.zip
→
epluone/03_vector_operation/
or
epluone/06_ai_cognitive_os/AI인지OS_백데이터/

SeungeFlow_blackhole_accretiondisk_*.zip
→
epluone/05_dynamic_geometry/blackhole/
or
epluone/05_dynamic_geometry/accretion_disk/

the_things_OS materials
→
epluone/07_the_things_os/

sohosa_hyangsa / root structure
→
epluone/08_root_support/

CFD / OHLC / TradingView
→
epluone/10_capital_market_hints/
```

---

## 5. Final Compression

```text
A manifest is a placement table.
It is not an interpretation document.
It prevents each source from losing its own place.
```
