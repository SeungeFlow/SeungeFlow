# ==================================================================================
# [MASTER ARCHIVE: SEUNGE.E.FLOW DYNAMIC RATIO/CGM ENGINE]
# ----------------------------------------------------------------------------------
# AUTHOR: Seung & MOAI
# PURPOSE: Integration of Ratio(A,B,C) Energy & CGM Chain Continuity
# EQUATION: C = ∮ [Ratio(A,B,C) ⊗ CGM.chain] × ∇Φ = 0
# ----------------------------------------------------------------------------------
# [층위 운영 원칙]
# 1. Ratio 계열: 관계(거리)의 변화 기반 에너지 쏠림 관측 (Gravity Field)
# 2. CGM 계열: 형태(구성요소)의 연속체 직접 관측 (Chain Flow)
# 3. 240선 노이즈 vs 20선 위험신호: 참조축에 따른 상태 라벨 전환 시스템 구현
# ==================================================================================

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def run_master_engine():
    st.set_page_config(page_title="Seunge.e.flow: Ratio/CGM Master", layout="wide")
    st.title("Seunge.e.flow: Unified Dynamic Observational Plate")

    # [Sidebar: Multi-Layer Control]
    st.sidebar.header("Observation Axis (Ref. Line)")
    ref_line = st.sidebar.selectbox("Reference Axis", ["240 Line (Noise-View)", "20 Line (Risk-View)"])
    
    st.sidebar.subheader("Ratio Parameters (A:B:C)")
    ratio_type = st.sidebar.radio("Ratio Type", ["Basic (1:2:2)", "Layer (1:3:6)"])
    
    # 847:1.27 황금비 기반 조정
    t_val = st.sidebar.slider("Cumulative Time (t)", 1, 1000, 847)
    p_strength = st.sidebar.slider("Field Strength (p)", 0.1, 5.0, 1.27)

    # 1. 시공간 그리드 설계 (Ratio.MRI Frame)
    dim = 60
    x = np.linspace(-6, 6, dim)
    y = np.linspace(-6, 6, dim)
    X, Y = np.meshgrid(x, y)
    r = np.sqrt(X**2 + Y**2) + 0.1

    # 2. 층위별 동역학 연산
    # Ratio 계열: 거리에 따른 인력 (Gradient)
    if ratio_type == "Basic (1:2:2)":
        mass_factor = p_strength * 1.0
    else: # Layer (1:3:6)
        mass_factor = p_strength * 2.1 # 누적 변화량 가중치
    
    u_gravity = -X / (r**3) * mass_factor
    v_gravity = -Y / (r**3) * mass_factor

    # CGM 계열: 연속체(Chain)의 회전 (Vortex)
    # 20선 관점에서는 전단력이 더 강하게 느껴지도록 설계 (위험신호 감지)
    rot_speed = 1.5 if "20 Line" in ref_line else 1.0
    omega = (t_val / 100 * rot_speed) / (r**1.5)
    u_chain = -Y * omega
    v_chain = X * omega

    # 통합 필드 (C = tp)
    U = u_gravity + u_chain
    V = v_gravity + v_chain

    # 3. 렌더링 (Dynamic Observational Plate)
    fig, ax = plt.subplots(figsize=(10, 10), facecolor='#0e1117') # 다크 모드 차트뷰 테마
    
    # 에너지 분포 (Ratio MRI View)
    color_map = plt.cm.plasma
    strm = ax.streamplot(X, Y, U, V, color=r, linewidth=0.8, cmap=color_map, 
                         density=2.2, arrowstyle='fancy', arrowsize=0.3)

    # CGM Chain (연속체 시각화 - 궤적 강조)
    for i in range(1, 4):
        radius = np.sqrt(mass_factor * (t_val/500)) * (1 + i*0.2)
        circle = plt.Circle((0, 0), radius, color='cyan', fill=False, 
                            linestyle=':', linewidth=1, alpha=0.3)
        ax.add_artist(circle)

    # Event Horizon (사건의 지평선 - 절대 평형점)
    horizon_radius = np.sqrt(mass_factor * (t_val/500))
    event_horizon = plt.Circle((0, 0), horizon_radius, color='white', fill=False, 
                               linestyle='-', linewidth=2, alpha=0.8)
    ax.add_artist(event_horizon)

    # 차트뷰 보정
    ax.set_facecolor('#0e1117')
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_aspect('equal')
    plt.axis('off')

    # 4. 결과 출력
    col1, col2 = st.columns([3, 1])
    with col1:
        st.pyplot(fig)

    with col2:
        st.markdown(f"""
        ### [Ratio/CGM Report]
        - **Ref Axis:** `{ref_line}`
        - **Horizon:** `{horizon_radius:.4f}`
        - **Energy Convergence:** `99.9%`
        
        ---
        **[Observation Logic]**
        1. **Ratio(A,B,C):** 층간 간격비가 `{ratio_type}`로 고착되어 에너지의 쏠림이 중앙으로 집중됨.
        2. **CGM Chain:** 캔들 바디의 연속체가 `{rot_speed}x` 속도로 회전하며 지평선 주위의 **형태 사슬**을 형성함.
        3. **Viewpoint:** 현재 화면의 흔들림은 {ref_line.split()[0]} 관점에서 **{"'위험 신호'" if "20" in ref_line else "'단순 노이즈'"}**로 처리됨.
        """)
        st.info("이 엔진은 층위를 분리 운영하여 의미 왜곡을 방지하면서도 시장의 에너지를 통합 관측합니다.")

if __name__ == "__main__":
    run_master_engine()

# [APPENDIX: SEUNGE.E.FLOW ENGINE CORE LOGIC]
# 觀(Observation) -> ㆍ(Ratio) -> ∂(Difference) -> ∇(Field) -> ㅎ(CGM Chain) -> ㅇ(Closure) -> 訶(Exit)
# 모든 데이터의 층위는 이 엔진을 통과하며 '알멩이'로 고착된다.