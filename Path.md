# Path Rule

## 0. Why Path.md exists

`Path.md`는 Y_Branch 내부에서 path를 어떻게 기록할지 정의한다.

```text
Path는 source가 아니다.
Path는 문서가 놓일 자리다.
```

---

## 1. No local absolute paths

문서 내부에는 local absolute path를 넣지 않는다.

금지 예:

```text
/mnt/data/...
/home/...
C:/Users/...
```

이런 경로는 생성 환경의 runtime path이며, Y_Branch 문서의 장기 source identity가 아니다.

---

## 2. Branch-relative paths

Y_Branch 내부 문서는 branch-relative path를 기본으로 쓴다.

허용 예:

```text
schema/004_ctp/ctp.meta.md
operation/R07_boundary_preserving_matrix_swap.md
field/music_language/README.md
source_index/music_language_sources.md
```

---

## 3. Raw URLs only in source_index/

Raw URL과 commit hash는 본문 곳곳에 반복하지 않는다.

source identity가 필요할 때는 `source_index/`에 기록한다.

```text
source identity = branch + path + Raw URL + commit hash + source status
```

---

## 4. Download filename is not source identity

다운로드된 파일명은 source identity가 아니다.

예:

```text
README(49).md
Ctp_SeungeFlow(29).md
```

이런 이름은 framework duplicate artifact일 수 있다. source identity는 branch, path, Raw URL, commit hash, source status로 판단한다.

---

## 5. GitHub target path

GitHub target path는 다음으로 판단한다.

```text
branch + relative path + filename
```

---

## 6. Runtime path guard

`/mnt/data`, `/home`, `C:/Users` 같은 runtime path는 문서 내부 기준 path로 쓰지 않는다.

runtime path는 생성·검토 중의 임시 위치일 뿐이다.

---

## 7. Shortest

```text
문서 내부에는 local absolute path를 넣지 않는다.
Y_Branch의 문서 path는 branch-relative path로 기록한다.
source identity가 필요할 때만 source_index/에 기록한다.
```
