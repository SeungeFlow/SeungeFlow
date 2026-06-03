# source_index

`source_index/`는 Y_Branch에서 사용하는 source identity를 기록하는 디렉토리다.

이 디렉토리는 원자료를 해석하지 않는다.

```text
source_index/ = source fact
```

source identity는 다음으로 판단한다.

```text
branch + path + Raw URL + commit hash + source status
```

filename은 source identity가 아니다.
