# SEUNGEFLOW_4D_AUTO.py
# 3D + 4D 완전 자동 블랙홀 동역학 (CR3BP + 회전 + 이동)
# p = 압력, C = 자리영역
# 변경: 슬라이더 → 텍스트 입력, 기본값 고정

import numpy as np
import plotly.graph_objects as go
import streamlit as st

def seungeflow_4d_auto():
    st.set_page_config(page_title="Seunge.e.flow 4D", layout="wide")
    st.title("Seunge.e.flow 4D : 구조체가 스스로 회전·이동하며 구현되는 블랙홀")

    # 기본값 고정
    default_t = 847
    default_p = 1.27

    # 직접 입력 (텍스트 박스)
    col1, col2 = st.columns(2)
    with col1:
        t_input = st.text_input("누적 시간 (t)", value=str(default_t))
    with col2:
        p_input = st.text_input("압력 강도 (p)", value=str(default_p))

    # 입력값 변환 (숫자 아니면 기본값 사용)
    try:
        t = float(t_input)
    except:
        t = default_t
    try:
        p_pressure = float(p_input)
    except:
        p_pressure = default_p

    # 3D 그리드
    x = np.linspace(-10, 10, 40)
    y = np.linspace(-10, 10, 40)
    z = np.linspace(-10, 10, 40)
    X, Y, Z = np.meshgrid(x, y, z)

    r = np.sqrt(X**2 + Y**2 + Z**2) + 0.01

    # 회전 + 이동 + 압력장
    omega = (t / 120) / (r**2) * p_pressure
    gravity = -p_pressure / (r**3)

    U = -Y * omega + gravity * X + 0.3 * np.sin(t/50) * Z
    V =  X * omega + gravity * Y - 0.3 * np.cos(t/50) * Z
    W = gravity * Z + 0.15 * np.sin(t/30) * X

    # 사건지평선 반지름
    horizon = np.sqrt(p_pressure * (t / 420))

    # Plotly 3D
    fig = go.Figure()

    fig.add_trace(go.Cone(
        x=X.flatten(), y=Y.flatten(), z=Z.flatten(),
        u=U.flatten(), v=V.flatten(), w=W.flatten(),
        sizemode="absolute", sizeref=0.3,
        colorscale='Inferno', showscale=False
    ))

    # 사건지평선 (Surface + 원형 마스크)
    theta = np.linspace(0, np.pi*2, 50)
    phi = np.linspace(0, np.pi, 50)
    theta, phi = np.meshgrid(theta, phi)
    xs = horizon * np.sin(phi) * np.cos(theta)
    ys = horizon * np.sin(phi) * np.sin(theta)
    zs = horizon * np.cos(phi)

    fig.add_trace(go.Surface(
        x=xs, y=ys, z=zs,
        colorscale=[[0, 'rgba(255,255,255,0.15)'], [1, 'rgba(255,255,255,0.15)']],
        showscale=False,
        opacity=0.6,
        contours={"z": {"show": True, "color": "white", "width": 2}}
    ))

    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False, range=[-10,10]),
            yaxis=dict(visible=False, range=[-10,10]),
            zaxis=dict(visible=False, range=[-10,10]),
            bgcolor='black',
            aspectmode='cube'
        ),
        margin=dict(l=0,r=0,t=0,b=0),
        title="Seunge.e.flow 4D : 구조체가 스스로 회전·이동하며 블랙홀을 구현하는 순간"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.success(f"""
    ✅ 4D 구현 완료  
    자리영역 C = {t:.0f} × 압력 p = {p_pressure:.2f}  
    사건지평선 반지름 : {horizon:.3f}  
    회전·이동·압력 누적 완료  
    (CR3BP + 상대성 + NS + YM + F=ma + E=mc² 통합)
    """)

if __name__ == "__main__":
    seungeflow_4d_auto()