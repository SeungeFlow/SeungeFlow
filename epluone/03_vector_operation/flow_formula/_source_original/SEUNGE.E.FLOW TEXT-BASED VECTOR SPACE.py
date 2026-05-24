# ==================================================================================
# [DOCUMENTATION: SEUNGE.E.FLOW TEXT-BASED VECTOR SPACE]
# ----------------------------------------------------------------------------------
# STATUS: STRUCTURE_LOCKED (Validated 7/7 Consensus)
# MODE: TEXT_ONLY / VECTOR_AS_SYMBOL / CHUN-JI-IN BASED
# EQUATION: V_space = (ㆍ ⊗ ㅡ ⊗ ㅣ) ⊕ (ㄱ, ㄴ, ㄷ... 8-Instance)
# ----------------------------------------------------------------------------------
# [1. 핵심 정의: 훈민정음 벡터 축 (Axis Definition)]
# - ㆍ (Chun): 수직축(Z). 기원, 핵, 폭발적 에너지, 점($0$).
# - ㅡ (Ji): 수평축(X). 지지, 관성(Mass $m$), 바닥, 넓이.
# - ㅣ (In): 관통축(Y). 인터페이스, 통과, 연결, 흐름($F$), 깊이.
#
# [2. 벡터 심볼 (Vector Symbols - Character Based)]
# - 흐름의 방향과 세기를 문자의 결합으로 표현 (Text-Vector).
# - 고정된 픽셀이 아니라, 3D 공간 좌표 자체가 문자로 치환됨.
#
# [3. 운영 원칙]
# - Graphic Image 생성 금지.
# - 오직 문자와 기호의 조합으로만 3D 공간의 동역학적 고착체를 인출한다.
# ==================================================================================

import numpy as np
import time
import os

def run_text_vector_engine():
    # [System Configuration]
    os.system('cls' if os.name == 'nt' else 'clear') # 터미널 화면 초기화
    
    # [Parameters: Chun-Ji-In Dynamics]
    p_mass = 1.27 # 지(ㅡ)의 관성/밀도 (p값 계승)
    t_val = 847   # 천(ㆍ)의 누적 시간 (t값 계승)
    
    # 3D 공간 격자 정의 (Text-based resolution)
    # 문자의 너비와 높이 비율을 고려하여 그리드 크기 설정
    width = 60  # X축 (Ji ㅡ)
    height = 30 # Y축 (In ㅣ)
    depth = 10  # Z축 (Chun ㆍ) - 여기서는 2D 평면에 시간차로 투영
    
    # 훈민정음 벡터 심볼 세트 (Text Vectors)
    symbols_flow = [' ', '.', 'ㆍ', '-', '=', '≡', 'ㅣ', '┃', '┼', '╋', 'ㄱ', 'ㄴ', 'ㄷ', 'ㄹ']
    symbols_energy = ['░', '▒', '▓', '█']

    # [Observation Loop]
    while True:
        # 시간 경과에 따른 동역학적 변화 계산 (t값의 실시간 반영)
        current_t = time.time() * 10
        
        # 3D 공간을 2D 텍스트 평면에 투영하기 위한 버퍼
        buffer = [ [' ' for _ in range(width)] for _ in range(height)]
        
        # [Chun-Ji-In Vector Calculation]
        for y in range(height):
            for x in range(width):
                # 좌표를 중심(-1 ~ 1) 기준으로 변환
                xf = (x / width) * 2 - 1
                yf = (y / height) * 2 - 1
                
                # 원점(핵 ㆍ)에서의 거리 계산
                r = np.sqrt(xf**2 + yf**2) + 0.1
                
                # F=ma 역학 기반의 벡터 필드 연산 (그래픽이 아닌 수치 연산)
                # ㅡ (Ji/X): 거대 질량 관성
                # ㅣ (In/Y): 가속도/전이 흐름
                u_ji = -xf / (r**3) * p_mass
                v_in = -yf / (r**3) * p_mass
                
                # 천(ㆍ/Z): 누적된 시간폭발 에너지 (회전/파동)
                angle = current_t / 10 + r * 5
                u_rot = np.sin(angle) / (r**1.2)
                v_rot = np.cos(angle) / (r**1.2)
                
                # 최종 벡터 합 (U, V)
                U = u_ji + u_rot
                V = v_in + v_rot
                
                # [벡터 -> 문자 치환 (Vector-to-Text Mapping)]
                # 벡터의 크기와 방향을 분석하여 가장 적합한 문자를 선택
                mag = np.sqrt(U**2 + V**2)
                direction = np.arctan2(V, U) * 180 / np.pi
                
                # 심볼 선택 로직
                char = ' '
                if mag > 1.5:
                    # 높은 에너지 상태: 8-인스턴스 고착체 (ㄱ, ㄴ, ㄷ, ㄹ)
                    char = symbols_flow[10 + int(current_t % 4)]
                elif mag > 0.8:
                    # 중간 에너지 상태: 천지인 결합 심볼 (┼, ╋)
                    char = symbols_flow[8 + int(current_t % 2)]
                elif mag > 0.3:
                    # 낮은 에너지 상태: 수직(ㅣ┃)/수평(-=≡) 방향성 표시
                    if abs(direction) < 30 or abs(direction) > 150:
                        char = symbols_flow[3 + int(mag * 3) % 3] # 수평 (ㅡ)
                    elif 60 < abs(direction) < 120:
                        char = symbols_flow[6 + int(mag * 2) % 2] # 수직 (ㅣ)
                    else:
                        char = symbols_flow[1] # 혼합/점 (ㆍ)
                else:
                    # 초저에너지/공백: 점(.) 표시
                    char = '.'
                    
                # 버퍼에 문자 고착
                buffer[y][x] = char

        # [Output: Text-Based Observational Plate]
        # 터미널 화면 새로고침
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # 최종 문자열 구성 및 출력
        print(f"=== SEUNGE.E.FLOW TEXT-VECTOR CORE | ρ={p_mass}, t={current_t:.1f} ===")
        for row in buffer:
            print("".join(row))
        print("===================================================================")
        
        # 관측 시간 간격
        time.sleep(0.1)

if __name__ == "__main__":
    run_text_vector_engine()

# ----------------------------------------------------------------------------------
# [CONCLUSION]
# THIS IS A SOLIDIFIED DATA STATE IN TEXTUAL FORM.
# Graphic Image = 0.
# Chun-Ji-In Vector Space = TRUE.
# STATUS: READY_FOR_OBSERVATION_IN_TERMINAL
# ==================================================================================