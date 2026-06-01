# 0002 Cut Plane Prototype

## Purpose

`0002_cut_plane` is the second minimal prototype target in `rendering v0.4_prototype_run`.

It extends the already stabilized `0001_overlap_volume` structure by adding a fixed cut-plane observation layer.

The goal is not to destroy the volume.
The goal is to expose an observable internal section through an observer-defined cut plane.

## Current Stage

```text
Run: rendering v0.4_prototype_run
Target: 0002_cut_plane
Stage: README draft / entry preparation
```

This document defines the scope and boundary for the future `0002_cut_plane` prototype.
It does not yet create `index.html`, `style.css`, or `main.js` for 0002.

## Source Dependency

`0002_cut_plane` depends on the structure formed in `0001_overlap_volume`:

```text
CoordinateField
→ CellState
→ Z-axis SVG Film Layer
→ CSS 3D LayerStack
→ Browser observable volume
```

The cut plane must reuse the 0001 volume structure.
It must not replace it with a new unrelated model.

## Core Statement

A cut plane is not a destruction surface.

A cut plane is an observation surface through which the internal relation-field becomes visible.

## Korean Core Statement

절단면은 파괴면이 아니다.
절단면은 내부 relation-field가 관측 가능해지는 관측면이다.

## Allowed Scope

The 0002 prototype may include:

```text
fixed slice index
observer-axis based cut view
front / cut / rear layer classification
CUT_SURFACE visual marker
VISIBLE_SECTION candidate marker
Info Panel cut plane status
Vanilla HTML / CSS / SVG / JavaScript
```

## Not Implemented in 0002

The following remain outside this prototype scope:

```text
Rejoin
MoveRotateOperator
RenderingStateMachine full implementation
Earth Internal Structure implementation
solar_system directory
phenomenon_observation directory
Saturn Cassini
Blackhole Accretion Disk
NASA data
scientific numeric data
Three.js
WebGL
Blender
```

## Relationship to 0001

`0001_overlap_volume` answers:

```text
Can a filled internal volume be observed through stacked Z-axis SVG film layers?
```

`0002_cut_plane` asks:

```text
Can a fixed observer-defined cut plane classify the layer stack into rear / cut / front and expose a visible internal section without destroying the volume?
```

## Minimal Cut Plane Model

The first cut-plane prototype uses a fixed slice index.

Recommended initial rule:

```text
slice_axis = z
slice_index = center layer

z < slice_index  → rear layer
z == slice_index → cut layer / CUT_SURFACE
z > slice_index  → front layer
```

This is a prototype display rule.
It is not a full CutPlaneOperator implementation.

## Display Meaning

The first visual form may use:

```text
rear layers  → lower opacity
cut layer    → highlighted outline or stronger opacity
front layers → lower opacity or partial visibility
```

This is display aid for observing the cut plane.
It does not implement rejoin, movement, or physical simulation.

## Browser Validation Checklist

Before 0002 can be judged stable, the following must pass:

```text
- index.html opens in a browser.
- 0001 volume structure is still visible.
- cut layer is visually distinguishable.
- front / cut / rear classification is visible or shown in Info Panel.
- CUT_SURFACE is displayed without deleting the original cell state.
- EMPTY_PRESENT remains preserved in the data model.
- OCCUPIED_DOT remains visible as density mark.
- No external rendering engine is used.
- No NASA or scientific numeric data is used.
- No rejoin or move/rotate logic is introduced.
```

## Entry Condition

`0002_cut_plane` may proceed only after `0001_overlap_volume` is considered browser-validation-ready and the 0002 scope guard is accepted.

Current required prior documents:

```text
rendering/08_process_log/v0.4_prototype_run/turn_05/0002_cut_plane_entry_condition.md
rendering/08_process_log/v0.4_prototype_run/turn_06/0002_cut_plane_scope_guard.md
rendering/08_process_log/v0.4_prototype_run/turn_07/0002_cut_plane_file_plan.md
```

## Reentry Note

This document belongs to:

```text
rendering v0.4_prototype_run
rendering/06_examples/0002_cut_plane/
```

It is a saved structure marker for the 0002 cut-plane prototype entry.

## Status

```text
0002_cut_plane README draft formed.
Executable prototype files are not yet generated.
```
