/**
 * rendering v0.4_prototype_run
 * 0002_cut_plane prototype - fixed center Z cut plane
 *
 * This is a minimal cut-plane display prototype.
 * It is not Rejoin, MoveRotateOperator, Earth model, or full RenderingStateMachine implementation.
 */

const CONFIG = {
    N: 7,
    STAGE_SIZE: 300,
    Z_SPACING: 40,
    SLICE_AXIS: 'z'
};
CONFIG.CELL_SIZE = CONFIG.STAGE_SIZE / CONFIG.N;
CONFIG.SLICE_INDEX = Math.floor(CONFIG.N / 2);

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
    return field.map(layer =>
        layer.map(row =>
            row.map(cell => {
                const dx = cell.x - center;
                const dy = cell.y - center;
                const dz = cell.z - center;
                const r2 = dx * dx + dy * dy + dz * dz;
                const state = (r2 <= (center * center)) ? 'OCCUPIED_DOT' : 'EMPTY_PRESENT';
                return { ...cell, state };
            })
        )
    );
}

function classifyLayer(z, config) {
    if (z < config.SLICE_INDEX) return 'rear';
    if (z === config.SLICE_INDEX) return 'cut';
    return 'front';
}

function countCellStates(cellStates, config) {
    let emptyCount = 0;
    let occupiedCount = 0;
    let cutSurfaceCount = 0;
    const layerCounts = { rear: 0, cut: 0, front: 0 };

    cellStates.forEach((layer, z) => {
        const classification = classifyLayer(z, config);
        layerCounts[classification] += 1;

        layer.forEach(row => {
            row.forEach(cell => {
                if (cell.state === 'OCCUPIED_DOT') {
                    occupiedCount += 1;
                    if (classification === 'cut') cutSurfaceCount += 1;
                }
                if (cell.state === 'EMPTY_PRESENT') emptyCount += 1;
            });
        });
    });

    return {
        emptyCount,
        occupiedCount,
        cutSurfaceCount,
        layerCount: cellStates.length,
        rearLayerCount: layerCounts.rear,
        cutLayerCount: layerCounts.cut,
        frontLayerCount: layerCounts.front
    };
}

function createSvgFilmLayer(layerData, z, config) {
    const svgNS = 'http://www.w3.org/2000/svg';
    const svg = document.createElementNS(svgNS, 'svg');
    const classification = classifyLayer(z, config);

    svg.setAttribute('class', 'film-svg');
    svg.setAttribute('viewBox', `0 0 ${config.STAGE_SIZE} ${config.STAGE_SIZE}`);
    svg.setAttribute('data-layer-classification', classification);

    if (classification === 'cut') {
        const frame = document.createElementNS(svgNS, 'rect');
        frame.setAttribute('x', 1);
        frame.setAttribute('y', 1);
        frame.setAttribute('width', config.STAGE_SIZE - 2);
        frame.setAttribute('height', config.STAGE_SIZE - 2);
        frame.setAttribute('class', 'visible-section-frame');
        svg.appendChild(frame);
    }

    layerData.forEach(row => {
        row.forEach(cell => {
            // EMPTY_PRESENT remains in the data model and is not drawn by default.
            if (cell.state === 'OCCUPIED_DOT') {
                const rect = document.createElementNS(svgNS, 'rect');
                rect.setAttribute('x', cell.x * config.CELL_SIZE);
                rect.setAttribute('y', cell.y * config.CELL_SIZE);
                rect.setAttribute('width', config.CELL_SIZE * 0.9);
                rect.setAttribute('height', config.CELL_SIZE * 0.9);
                rect.setAttribute('class', classification === 'cut' ? 'occupied-dot cut-surface' : 'occupied-dot');
                rect.setAttribute('data-cell-state', cell.state);
                if (classification === 'cut') {
                    rect.setAttribute('data-cut-role', 'CUT_SURFACE');
                }
                svg.appendChild(rect);
            }
        });
    });

    return svg;
}

function renderLayerStack(cellStates, stageElement, config) {
    stageElement.innerHTML = '';
    const centerZ = Math.floor(config.N / 2);

    cellStates.forEach((layerData, z) => {
        const classification = classifyLayer(z, config);
        const layerDiv = document.createElement('div');
        layerDiv.className = `film-layer layer-${classification}`;
        layerDiv.setAttribute('data-z-index', String(z));
        layerDiv.setAttribute('data-layer-classification', classification);

        const zOffset = (z - centerZ) * config.Z_SPACING;
        layerDiv.style.transform = `translateZ(${zOffset}px)`;

        const svgElement = createSvgFilmLayer(layerData, z, config);
        layerDiv.appendChild(svgElement);
        stageElement.appendChild(layerDiv);
    });
}

function updateInfoPanel(stats, config, currentView) {
    const content = document.getElementById('stats-content');
    content.textContent = `Run: rendering v0.4_prototype_run
Target: 0002_cut_plane
Grid: ${config.N} × ${config.N} × ${config.N}
Layer count: ${stats.layerCount}
Occupied dot count: ${stats.occupiedCount}
Empty present count: ${stats.emptyCount}

Cut Plane:
axis: ${config.SLICE_AXIS}
slice index: ${config.SLICE_INDEX}
rear layers: ${stats.rearLayerCount}
cut layers: ${stats.cutLayerCount}
front layers: ${stats.frontLayerCount}
CUT_SURFACE count: ${stats.cutSurfaceCount}

Current observer view: ${currentView}
Prototype type: Fixed Z Cut Plane + SVG Film Layer + CSS 3D LayerStack
Rejoin: not implemented
Move / Rotate Operator: not implemented
Rendering State Machine: not implemented
Earth Internal Structure: not implemented
External engine: none
NASA data: none`;
}

function setActiveObserverButton(viewName) {
    const buttons = document.querySelectorAll('#observer-controls button');
    buttons.forEach(button => {
        const active = button.getAttribute('data-view') === viewName;
        button.classList.toggle('active', active);
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
        button.addEventListener('click', event => {
            const viewName = event.currentTarget.getAttribute('data-view');
            setObserverView(viewName, stats, config);
        });
    });
}

function initPrototype() {
    const field = createCoordinateField(CONFIG);
    const states = assignCellStates(field, CONFIG);
    const stats = countCellStates(states, CONFIG);
    const stage = document.getElementById('stage');

    renderLayerStack(states, stage, CONFIG);
    bindObserverControls(stats, CONFIG);
    updateInfoPanel(stats, CONFIG, 'isometric');
    setActiveObserverButton('isometric');
}

initPrototype();
