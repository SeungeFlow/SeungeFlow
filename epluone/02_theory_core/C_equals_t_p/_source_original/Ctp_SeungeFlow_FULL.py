# Ctp_SeungeFlow_FULL.py
# -*- coding: utf-8 -*-

"""
Ctp_SeungeFlow FULL ENGINE

전체 구조:
ㆍ → T₁ → C → TORUS → R → I → D → Closure
"""

# ============================================================
# [1] Seed → T1 (1단)
# ============================================================

T1 = ["ㆍ", 1,2,3,4,5,6,7,8,9,0, "ㆍ"]

def is_closed(flow):
    return flow[0] == flow[-1]


# ============================================================
# [2] 7 적층 → C
# ============================================================

def build_C(T1, n=7):
    return [list(T1) for _ in range(n)]


# ============================================================
# [3] TORUS 판정
# ============================================================

def is_torus(C):
    return len(C) == 7 and all(is_closed(layer) for layer in C)


# ============================================================
# [4] Ring (R)
# ============================================================

def build_R(C):
    return {
        "type": "R",
        "layers": len(C),
        "mass": [1.0]*len(C)
    }


# ============================================================
# [5] Cassini = I
# ============================================================

KEY_SEQUENCE = ["ㆁ","ㆆ","ㆅ"]

def interface_I():
    return {
        "axis": "ㅣ",
        "key": KEY_SEQUENCE[-1]
    }


def cassini_condition(rho, dr, chi, sigma):
    return (
        rho >= 1.0 and
        dr <= 1.0 and
        chi >= 1.0 and
        sigma < 1.0
    )


# ============================================================
# [6] R → D 전이
# ============================================================

def R_to_D(R, rho, dr, chi, sigma):
    if cassini_condition(rho, dr, chi, sigma):
        return {
            "state": "D",
            "interface": interface_I(),
            "key_sequence": KEY_SEQUENCE,
            "transition": True
        }
    return {
        "state": "R",
        "transition": False
    }


# ============================================================
# [7] Closure (최종)
# ============================================================

def closure(state):
    return state == "D"


# ============================================================
# [8] 전체 실행
# ============================================================

def run():
    print("=== Ctp FULL ENGINE ===")

    # 1. Seed → T1
    print("T1 Closed:", is_closed(T1))

    # 2. C
    C = build_C(T1)
    print("C Layers:", len(C))

    # 3. Torus
    print("TORUS:", is_torus(C))

    # 4. R
    R = build_R(C)
    print("R Built")

    # 5. Transition
    result = R_to_D(R, rho=2.0, dr=0.3, chi=2.0, sigma=0.2)
    print("Transition:", result)

    # 6. Closure
    print("Closure:", closure(result["state"]))


if __name__ == "__main__":
    run()