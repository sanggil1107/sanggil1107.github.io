---
layout: post
title: "[Docker] 4.Docker 명렁어(3)"
category: [Docker]
---
<br>

`Docker 명령어`에 대해 알아보자
<!-- more -->
<hr>



## 네트워크 목록 (docker network ls)
---
`docker network ls [옵션]`

|옵션|설명|
|---|---|
|--filter=[], -f|출력을 필터링|
|--no-trunc|상세 정보를 출력|
|--quiet, -q|네트워크 ID만 표시|

```
$ docker network ls

NETWORK ID     NAME      DRIVER    SCOPE
76d167d53944   bridge    bridge    local
bbcee6515c54   host      host      local
0afffbf8a0f2   none      null      local
```