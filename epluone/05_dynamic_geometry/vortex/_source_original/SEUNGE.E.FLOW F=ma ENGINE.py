# ==================================================================================
# [MASTER ARCHIVE: SEUNGE.E.FLOW F=ma ENGINE]
# ----------------------------------------------------------------------------------
# CORE LOGIC: MA is not 'Moving Average', it is 'Mass x Acceleration'
# EQUATION: F_total = Σ(m_240 * a_local) + Σ(m_20 * a_risk)
# ----------------------------------------------------------------------------------
# [운영 원칙]
# 1. ma_240 (Mass): 거대 관성. 장의 중심 구조 형성.
# 2. ma_20 (Force): 가속도 변화. 지평선 경계의 위험 신호 탐지.
# 3. Ratio Layer: 질량과 가속도 사이의 '거리(관계)' 에너지를 산출함.
# ==================================================================================

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def run_force_engine():
    st.set_page_config(page_title="Seunge.e.flow: F=ma Engine", layout="wide")
    st.title("Seunge.e.flow: F=ma Dynamic Observational Core")

    # [Sidebar: F=ma Control Tower]
    st.sidebar.header("Physics Axis (F=ma)")
    view_mode = st.sidebar.radio("Observation Frame", ["Mass Frame (ma_240)", "Force Frame (ma_20)"])
    
    # t=847, p=1.27 기반의 임계 가속도 설정
    t_val = st.sidebar.slider("Accumulated Inertia (t)", 1, 1000, 847)
    p_mass = st.sidebar.slider("System Mass (p)", 0.1, 5.0, 1.27)

    # 1. 시공간 격자 (Linguistic Physics Fabric)
    dim = 60
    x = np.linspace(-6, 6, dim)
    y = np.linspace(-6, 6, dim)
    X, Y = np.meshgrid(x, y)
    r = np.sqrt(X**2 + Y**2) + 0.1

    # 2. 역학 연산 (F = ma)
    # ma_240에 의한 중심 중력 생성
    m_240 = p_mass * 2.0
    u_gravity = -X / (r**3) * m_240
    v_gravity = -Y / (r**3) * m_240

    # ma_20에 의한 가속도 벡터 (회전력)
    # 20선 관점에서는 가속도의 변화(a)가 더 민감하게 작용하여 위험 신호를 포착
    accel_factor = 2.5 if "ma_20" in view_mode else 1.0
    omega = (t_val / 100 * accel_factor) / (r**1.5)
    u_accel = -Y * omega
    v_accel = X * omega

    # 최종 힘의 벡터 합 (F = m * a)
    U = u_gravity + u_accel
    V = v_gravity + v_accel

    # 3. 렌더링
    fig, ax = plt.subplots(figsize=(10, 10), facecolor='#000000')
    
    # 역학적 흐름 (Force Streamlines)
    color_map = plt.cm.magma 
    ax.streamplot(X, Y, U, V, color=r, linewidth=1, cmap=color_map, 
                  density=2.4, arrowstyle='->', arrowsize=0.5)

    # 사건의 지평선 (Mass-Center Interface)
    horizon_radius = np.sqrt(m_240 * (t_val/500))
    circle = plt.Circle((0, 0), horizon_radius, color='white', fill=False, 
                        linestyle='--', linewidth=2, alpha=0.7)
    ax.add_artist(circle)

    ax.set_facecolor('black')
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_aspect('equal')
    plt.axis('off')

    # 4. 분석 리포트
    col1, col2 = st.columns([3, 1])
    with col1:
        st.pyplot(fig)

    with col2:
        st.info("### [Dynamic Force Report]")
        st.write(f"**Current Frame:** {view_mode}")
        st.write(f"**Horizon Radius:** {horizon_radius:.4f}")
        st.write("---")
        if "ma_240" in view_mode:
            st.success("관측: 거대 관성 상태. 현재의 미세 진동은 '노이즈'로 규정됩니다.")
        else:
            st.warning("관측: 가속도 증폭 상태. 현재의 궤적 이탈은 '위험 신호'로 규정됩니다.")
        
        st.markdown("""
        **[F=ma Logic]**
        1. **Mass (m):** 240선의 데이터 적층 밀도
        2. **Acceleration (a):** 20선의 방향 전단력
        3. **Force (F):** 지평선을 회전시키는 실체적 에너지
        """)

if __name__ == "__main__":
    run_force_engine()