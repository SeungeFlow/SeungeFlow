# Source Identity Guard

```text
filename은 source identity가 아니다.
```

source identity는 다음으로 판단한다.

```text
branch + path + Raw URL + commit hash + source status
```

같은 filename이라도 branch, path, commit이 다르면 다른 source이다.
