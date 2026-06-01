/**
 * rendering v0.4_prototype_run
 * 0001_overlap_volume prototype - Browser Validation & Naming Stabilization
 */

const CONFIG = {
    N: 7,             // N x N x N Grid
    STAGE_SIZE: 300,  // Stage 픽셀 크기
    Z_SPACING: 40     // Z축 레이어 간격
};
CONFIG.CELL_SIZE = CONFIG.STAGE_SIZE / CONFIG.N;

// ==========================================
// CuttableSolidEngine: Operations
// ==========================================

function createCoordinateField(config) {
    const field = [];
    for (let z = 0; z < config.N; z++) {
        const layer = [];
        for (let y = 0; y < config.N; y++) {
            const row = [];
            for (let x = 0; x < config.N; x++) {
                row.push({ x, y, z });
            }
            layer.push(row);
        }
        field.push(layer);
    }
    return field;
}

function assignCellStates(field, config) {
    const center = Math.floor(config.N / 2);
    // 구 형태(Solid)로 밀도 타격
    return field.map(layer =>
        layer.map(row =>
            row.map(cell => {
                const dx = cell.x - center;
                const dy = cell.y - center;
                const dz = cell.z - center;
                const r2 = dx*dx + dy*dy + dz*dz;

                const state = (r2 <= (center * center)) ? 'OCCUPIED_DOT' : 'EMPTY_PRESENT';
                return { ...cell, state };
            })
        )
    );
}

function countCellStates(cellStates) {
    let emptyCount = 0;
    let occupiedCount = 0;

    cellStates.forEach(layer => {
        layer.forEach(row => {
            row.forEach(cell => {
                if (cell.state === 'OCCUPIED_DOT') occupiedCount++;
                if (cell.state === 'EMPTY_PRESENT') emptyCount++;
            });
        });
    });

    return { emptyCount, occupiedCount, layerCount: cellStates.length };
}

// ==========================================
// Renderer Handoff: SVG Film Layer Generation
// ==========================================

function createSvgFilmLayer(layerData, config) {
    const svgNS = "http://www.w3.org/2000/svg";
    const svg = document.createElementNS(svgNS, "svg");
    svg.setAttribute("class", "film-svg");
    svg.setAttribute("viewBox", `0 0 ${config.STAGE_SIZE} ${config.STAGE_SIZE}`);

    layerData.forEach(row => {
        row.forEach(cell => {
            // EMPTY_PRESENT는 데이터 모델에는 존재하나 SVG 요소는 렌더링하지 않음 (투명 보존)
            if (cell.state === 'OCCUPIED_DOT') {
                const rect = document.createElementNS(svgNS, "rect");
                rect.setAttribute("x", cell.x * config.CELL_SIZE);
                rect.setAttribute("y", cell.y * config.CELL_SIZE);
                rect.setAttribute("width", config.CELL_SIZE * 0.9); // 간격을 위한 0.9 배율
                rect.setAttribute("height", config.CELL_SIZE * 0.9);
                rect.setAttribute("class", "occupied-dot");
                svg.appendChild(rect);
            }
        });
    });
    return svg;
}

function renderLayerStack(layersData, stageElement, config) {
    stageElement.innerHTML = ''; // Clear stage
    const centerZ = Math.floor(config.N / 2);

    layersData.forEach((layerData, z) => {
        const layerDiv = document.createElement('div');
        layerDiv.className = 'film-layer';

        // ZOffset Spec 적용
        const zOffset = (z - centerZ) * config.Z_SPACING;
        layerDiv.style.transform = `translateZ(${zOffset}px)`;

        // SVG 주입
        const svgElement = createSvgFilmLayer(layerData, config);
        layerDiv.appendChild(svgElement);

        stageElement.appendChild(layerDiv);
    });
}

// ==========================================
// Display Aid: Info Panel & Observer Controls
// ==========================================

function updateInfoPanel(stats, config, currentView) {
    const content = document.getElementById('stats-content');
    content.textContent = `Run: rendering v0.4_prototype_run
Target: 0001_overlap_volume
Grid: ${config.N} × ${config.N} × ${config.N}
Layer count: ${stats.layerCount}
Occupied dot count: ${stats.occupiedCount}
Empty present count: ${stats.emptyCount}

Current observer view: ${currentView}

Prototype type: SVG Film Layer + CSS 3D LayerStack
Cut Plane: not implemented
Rejoin: not implemented
Move / Rotate Operator: not implemented
Rendering State Machine: not implemented
External engine: none
NASA data: none`;
}

function setActiveObserverButton(viewName) {
    const buttons = document.querySelectorAll('#observer-controls button');
    buttons.forEach(btn => {
        if (btn.getAttribute('data-view') === viewName) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });
}

function setObserverView(viewName, stats, config) {
    const stage = document.getElementById('stage');
    stage.setAttribute('data-view', viewName);
    setActiveObserverButton(viewName);
    updateInfoPanel(stats, config, viewName);
}

function bindObserverControls(stats, config) {
    const buttons = document.querySelectorAll('#observer-controls button');
    buttons.forEach(button => {
        button.addEventListener('click', (e) => {
            const viewName = e.target.getAttribute('data-view');
            setObserverView(viewName, stats, config);
        });
    });
}

// ==========================================
// Prototype Initialization Flow
// ==========================================

function initPrototype() {
    // 1. PLACE_FIELD_DECLARED
    const field = createCoordinateField(CONFIG);

    // 2. CELL_STATES_ASSIGNED
    const states = assignCellStates(field, CONFIG);

    // 3. Stats calculation
    const stats = countCellStates(states);

    // 4. LAYER_STACK_CREATED -> INTERIOR_EXPOSED
    const stage = document.getElementById('stage');
    renderLayerStack(states, stage, CONFIG);

    // 5. Display Aid Binding
    bindObserverControls(stats, CONFIG);
    updateInfoPanel(stats, CONFIG, 'isometric');
    setActiveObserverButton('isometric');
}

// Execute
initPrototype();
