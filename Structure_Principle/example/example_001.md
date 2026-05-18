# example_001.md

```yaml
document_id: example_001
type: structure_principle_example_document
status: active_draft
target_directory: Structure_Principle/example
title: 마름모구조수열의 렌더링 코드화 예시
code_tree_status: deleted
merged_from:
  - code_001
  - codeplus_001
purpose:
  - render_diamond_structure_sequence
  - preserve_python_executable_form
  - preserve_scale_state_correction
  - keep_hangeul_as_primary_reference_language
```

---

# 0. 문서 성격

이 문서는 기존에 분리하려던 `code_001.md`와 `codeplus_001.md`를 합친 문서이다.

이제 `code` 트리는 사용하지 않는다.

```txt
code 트리 = 삭제
code / codeplus 분리 = 보류 또는 폐기
현재 문서 = example_001.md 하나로 통합
```

이 문서는 `Structure_Principle/example/` 디렉토리에 놓일 예시 문서이다.

```txt
C:\github
└── Structure_Principle
    └── example
        ├── example_001.md
        ├── example_002.md
        └── ...
```

---

# 1. 기준 원칙

기준은 한글이다.

```txt
한글 = 기준언어
영어 = 보조언어
# 주석 = 인간의 언어
Python 코드 = 인공지능 / 실행환경의 언어
```

따라서 문서 안에서 사람의 설명은 가능한 한 `#` 주석으로 코드 안에 함께 둔다.

이 방식은 다음 세 가지를 동시에 만족한다.

```txt
1. 사람이 한글로 읽는다.
2. 필요하면 영어 보조 표현을 함께 둔다.
3. 인공지능과 실행환경은 코드를 읽고 실행한다.
```

---

# 2. 마름모구조수열 핵심 해석

마름모구조수열은 다음처럼 읽는다.

```txt
마름모구조수열
=
중심 dot
+ 거리 규칙
+ direction
+ boundary
+ digit_state
+ rendering scale
```

기본 구현은 맨해튼 거리로 한다.

```txt
distance = abs(x - cx) + abs(y - cy)
```

맨해튼 거리가 일정한 점들의 집합은 마름모 boundary를 만든다.

```txt
distance == r
→ radius r의 diamond boundary
```

---

# 3. Python 코드

```python
# 마름모구조수열의 렌더링 코드화 예시
# Diamond Structure Sequence Rendering Code Example
#
# 한글이 기준이다.
# 영어는 보조 설명이다.
# 코드는 인공지능/실행환경이 읽고 실행할 수 있는 언어이다.
#
# 목적:
# - 중심점 dot을 기준으로 마름모 구조수열을 생성한다.
# - 맨해튼 거리로 diamond boundary를 계산한다.
# - rise / fall mode로 숫자상태 digit_state를 렌더링한다.
# - 단일 중심과 다중 중심 구조를 모두 지원한다.
#
# 구조원리식 읽기:
# dot      = 중심 기준점
# line     = 중심에서 boundary로 향하는 거리선
# surface  = 닫힌 마름모 boundary 내부 영역
# vector   = 값이 증가하거나 감소하는 방향 흐름
# digit    = 각 위치에 놓인 숫자 상태


from __future__ import annotations


def diamond_value(
    x: int,
    y: int,
    cx: int,
    cy: int,
    radius: int = 9,
    mode: str = "rise",
) -> int | None:
    # 현재 좌표와 중심점 사이의 맨해튼 거리를 계산한다.
    distance = abs(x - cx) + abs(y - cy)

    # 반지름 바깥은 마름모 구조 외부이다.
    if distance > radius:
        return None

    # rise mode:
    # boundary 0 → center radius
    if mode == "rise":
        return radius - distance

    # fall mode:
    # boundary radius → center 0
    if mode == "fall":
        return distance

    raise ValueError("mode must be 'rise' or 'fall'")


def render_single_diamond(
    radius: int = 9,
    mode: str = "rise",
    spacer: str = "",
) -> str:
    # 단일 중심점 마름모 구조수열을 문자열로 렌더링한다.
    lines: list[str] = []

    for y in range(-radius, radius + 1):
        row: list[str] = []

        for x in range(-radius, radius + 1):
            value = diamond_value(
                x=x,
                y=y,
                cx=0,
                cy=0,
                radius=radius,
                mode=mode,
            )

            if value is None:
                row.append(" ")
            else:
                row.append(str(value % 10))

        lines.append(spacer.join(row).rstrip())

    return "\n".join(lines)


def multi_diamond_value(
    x: int,
    y: int,
    centers: list[tuple[int, int]],
    radius: int = 9,
    mode: str = "rise",
    combine: str = "max",
) -> int | None:
    # 여러 중심점에서 생성된 마름모 값들을 합성한다.
    values: list[int] = []

    for cx, cy in centers:
        value = diamond_value(
            x=x,
            y=y,
            cx=cx,
            cy=cy,
            radius=radius,
            mode=mode,
        )

        if value is not None:
            values.append(value)

    if not values:
        return None

    if combine == "max":
        return max(values)

    if combine == "min":
        return min(values)

    if combine == "first":
        return values[0]

    raise ValueError("combine must be 'max', 'min', or 'first'")


def render_multi_diamond(
    centers: list[tuple[int, int]],
    radius: int = 9,
    mode: str = "rise",
    combine: str = "max",
    spacer: str = "",
) -> str:
    # 다중 중심점 마름모 구조수열을 문자열로 렌더링한다.
    min_x = min(cx - radius for cx, _ in centers)
    max_x = max(cx + radius for cx, _ in centers)
    min_y = min(cy - radius for _, cy in centers)
    max_y = max(cy + radius for _, cy in centers)

    lines: list[str] = []

    for y in range(min_y, max_y + 1):
        row: list[str] = []

        for x in range(min_x, max_x + 1):
            value = multi_diamond_value(
                x=x,
                y=y,
                centers=centers,
                radius=radius,
                mode=mode,
                combine=combine,
            )

            if value is None:
                row.append(" ")
            else:
                row.append(str(value % 10))

        lines.append(spacer.join(row).rstrip())

    return "\n".join(lines)


def example_centers(radius: int = 9) -> list[tuple[int, int]]:
    # 네 방향에 중심 dot을 놓는 예시 중심점 집합이다.
    # top / left / right / bottom 구조로 둔다.
    return [
        (0, -radius),
        (-2 * radius, 0),
        (2 * radius, 0),
        (0, radius),
    ]


def main() -> None:
    # 실행 예시이다.
    radius = 9

    print("=== single rise diamond ===")
    print(render_single_diamond(radius=radius, mode="rise"))

    print("\n=== single fall diamond ===")
    print(render_single_diamond(radius=radius, mode="fall"))

    centers = example_centers(radius=radius)

    print("\n=== multi rise diamond ===")
    print(
        render_multi_diamond(
            centers=centers,
            radius=radius,
            mode="rise",
            combine="max",
        )
    )

    print("\n=== multi fall diamond ===")
    print(
        render_multi_diamond(
            centers=centers,
            radius=radius,
            mode="fall",
            combine="min",
        )
    )


if __name__ == "__main__":
    main()
```

---

# 4. rise / fall 해석

## 4.1 rise

```txt
boundary 0
→ center 9
```

```python
# rise mode:
# value = radius - distance
```

외부 boundary에서 내부 center로 들어오며 값이 증가하는 방향이다.

---

## 4.2 fall

```txt
boundary 9
→ center 0
```

```python
# fall mode:
# value = distance
```

외부 boundary에서 내부 center로 들어오며 값이 감소하는 방향이다.

---

# 5. scale-state 보정

이미지 비교 중 다음 오인이 발생했다.

```txt
첫 이미지:
글자 크기 12
숫자 0~9가 명확히 보임

두 번째 이미지:
글자 크기 1
숫자가 점처럼 보임
```

처음에는 두 이미지가 서로 다른 구조처럼 보였다.

그러나 보정은 다음이다.

```txt
내용은 같다.
글씨 크기만 줄어들었다.
스케일만 달라졌다.
내용이 가지는 속성은 같다.
```

따라서 올바른 판정은 다음이다.

```txt
same_structure
+ different_scale
= same_content_in_different_scale_state
```

---

# 6. 같은 것과 달라진 것

같은 것:

```txt
내용
배열
위치 관계
수열 구조
마름모 boundary
digit_state
구조 속성
```

달라진 것:

```txt
font size
scale
surface rendering state
observer readability
```

따라서 다음을 혼동하지 않는다.

```txt
surface_state difference
≠
structure_property difference
```

---

# 7. example 디렉토리에서의 의미

이 문서는 단순한 코드 예제가 아니다.

```txt
example_001.md
=
구조원리가 실제 표시 방식으로 내려온 첫 예시 문서
```

이 문서에는 다음이 함께 놓인다.

```txt
한글 기준 설명
영어 보조 표현
Python 실행 코드
scale-state correction trace
구조원리식 해석
```

따라서 `example_001.md`는 단순 샘플이 아니라, 앞으로 `Structure_Principle/example/`에 놓일 문서들이 어떤 방식으로 내려올 수 있는지를 보여주는 schema 성격의 예시 문서이다.

---

# 8. 읽는 규칙

```txt
1. 파일명 example에 속지 않는다.
2. 한글을 기준으로 읽는다.
3. 영어는 보조로 읽는다.
4. # 주석은 인간의 언어로 읽는다.
5. Python 코드는 인공지능/실행환경의 언어로 읽는다.
6. scale 변화와 구조 속성 변화를 혼동하지 않는다.
7. 코드와 보조설명은 이 문서 안에서 분리되지 않고 함께 읽는다.
```

---

# 9. one_line

`example_001.md`는 마름모구조수열을 Python 코드로 렌더링하면서, 한글 기준 주석과 실행 코드를 함께 놓고, scale 변화가 구조 속성을 바꾸지 않는다는 보정 trace를 보존하는 통합 예시 문서이다.

---

# 10. shortest

```txt
example_001 = 한글 기준 + Python 코드 + 마름모구조수열 + scale-state 보정
```
