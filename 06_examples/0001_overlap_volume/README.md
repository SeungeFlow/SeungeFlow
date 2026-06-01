# 0001 Overlap Volume Prototype

## Purpose
v0.4_prototype_run의 첫 번째 최소 실행 검산.
N × N × N CoordinateFieldModel의 cell state를 Z-axis film layer로 추출하고, LayerStack으로 배치하여 내부가 찬 체적(Volume)을 관측 가능하게 형성한다.

## Prototype Type
This prototype uses SVG film layers inside a CSS 3D LayerStack.

## Display Aid
Observer axis controls are display aids.
They do not implement Cut Plane Operation.
관측축 제어는 현재 체적을 여러 방향에서 보기 위한 표시 보조 수단이며, 구조를 자르지 않는다.

## Structural Implementation
- **CoordinateFieldModel**: N x N x N Grid
- **CellStateModel**: `EMPTY_PRESENT` (0/null, future seat) / `OCCUPIED_DOT` (1/dot, density mark)
- **LayerExtractionRule**: Z축 기준 평면 추출
- **LayerStackModel**: SVG 필름 변환 및 `translateZ`를 이용한 z_offset 구조 재결합

## Browser Validation Checklist
- The page opens in a browser without external libraries.
- The Info Panel displays run, target, grid size, layer count, occupied count, and empty count.
- SVG film layers are visible in the LayerStack.
- Observer view buttons change only the display view.
- Observer view buttons do not create a cut plane.
- EMPTY_PRESENT cells remain in the data model.
- OCCUPIED_DOT cells are rendered as SVG rect elements.
- No NASA data or scientific numeric data is used.
- No Three.js, WebGL, or external rendering engine is used.

## Current Limitations
- 0002_cut_plane is not implemented.
- Rejoin is not implemented.
- MoveRotateOperator is not implemented.
- RenderingStateMachine is not implemented.
- Earth Internal Structure is not implemented.

## Next Entry Condition
Proceed to 0002_cut_plane only after 0001_overlap_volume is stable in browser validation.

## Status
0001_overlap_volume only.
0002_cut_plane is not implemented in this prototype.

## Constraints
- 실제 물리/과학 데이터 투입 금지.
- 외부 렌더링 엔진(Three.js/WebGL) 사용 금지.
- Vanilla HTML/CSS/SVG/JS 구조렌더링 검산 유지.

## Reentry Note
This document belongs to:
rendering v0.4_prototype_run
06_examples/0001_overlap_volume/

It is a saved structure marker for the 0001_overlap_volume stabilized prototype.

## Korean Core Statement
0001_overlap_volume은 브라우저에서 내부 volume이 관측 가능한지 검산하는 첫 프로토타입이다.
0002_cut_plane은 아직 구현하지 않는다.
