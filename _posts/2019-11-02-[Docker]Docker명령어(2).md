---
layout: post
title: "[Docker] 4.Docker 명렁어(2)"
category: [Docker]
image: /public/img/알고리즘/삽입정렬3.png
---
<br>

`Docker 명령어`에 대해 알아보자
<!-- more -->
<hr>

## 컨테이너 실행 (docker run)
---
`docker run [옵션] [컨테이너명] 이미지명[:태그명] [인수]`

|옵션|설명|
|---|---|
|--attach, -a|표준 입력, 출력, 오류 출력에 attach 한다.|
|--cidfile|컨테이너 ID를 파일로 출력|
|--detach, -d|컨테이너를 생성하고 백그라운드에서 실행|
|--interactive, -i|컨테이너의 표준 입력|
|--tty, -t|단말기 디바이스 사용|

```
$ docker run -it --name "Test" centos /bin/cal

   September 2019   
Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30
```
```
$ docker run -it --name "Test3" centos /bin/bash

[root@ca8fd2f4982a /]# ls
anaconda-post.log  bin  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```
```
$ docker run -d -p 8080:80 nginx

9cd3f115880c4da7885f706bd83f63131c4e0e8b2543321a5560138f01f0b0c1
```
```
$ ls

Desktop  Documents  Downloads  examples.desktop  Music  Pictures  Public  Templates  Videos  vtest

$ docker run -i -t -v /vtest --name volumetest1 centos bin/bash

[root@23d446e9134d /]# ls
bin  dev  etc  home  lib  lib64  lost+found  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var  vtest
```
```
$ docker run -it -e foo=bar centos /bin/bash

[root@cc7a7306349a /]# set
BASH=/bin/bash
BASHRCSOURCED=Y
BASH_ALIASES=()
BASH_ARGC=()
...
foo=bar
```
```
$ cat env_list 
yang=sanggil

$ docker run -it --env-file=env_list centos /bin/bash

[root@436377e9d58d /]# set
BASH=/bin/bash
BASHRCSOURCED=Y
BASH_ALIASES=()
BASH_ARGC=()
...
yang=sanggil
```
<br>

## 컨테이너 로그 확인
---
`docker logs `
```
$ docker run -d centos /bin/ping localhost

6becd04e405cabfc1e627ef6b3f573212762101f6419c157ef22246b1dce57c9
```
```
$ docker logs 6becd04e405cabfc1e627ef6b3f573212762101f6419c157ef22246b1dce57c9

PING localhost (127.0.0.1) 56(84) bytes of data.
64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.149 ms
64 bytes from localhost (127.0.0.1): icmp_seq=2 ttl=64 time=0.020 ms
64 bytes from localhost (127.0.0.1): icmp_seq=3 ttl=64 time=0.022 ms
64 bytes from localhost (127.0.0.1): icmp_seq=4 ttl=64 time=0.024 ms
64 bytes from localhost (127.0.0.1): icmp_seq=5 ttl=64 time=0.022 ms
64 bytes from localhost (127.0.0.1): icmp_seq=6 ttl=64 time=0.020 ms
64 bytes from localhost (127.0.0.1): icmp_seq=7 ttl=64 time=0.030 ms
64 bytes from localhost (127.0.0.1): icmp_seq=8 ttl=64 time=0.019 ms
```
<br>

## 정지된 컨테이너 기동 (docker start)
---
`docker start [옵션] <컨테이너 식별자>`
```
$ docker start 53e652bede18

53e652bede18
```
```
$ docker ps

CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                  NAMES
9cd3f115880c        nginx               "nginx -g 'daemon of…"   About an hour ago   Up About an hour    0.0.0.0:8080->80/tcp   wizardly_mcclintock
6becd04e405c        centos              "/bin/ping localhost"    About an hour ago   Up About an hour                           silly_chatterjee
53e652bede18        centos              "/bin/bash"              About an hour ago   Up 5 seconds                               Test3
```
<br>

## 실행 중인 컨테이너 정지 (docker stop)
---
`docker stop [옵션] <컨테이너 식별자>`
```
$ docker stop 53e652bede18

53e652bede18
```
```
$ docker ps

CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                  NAMES
9cd3f115880c        nginx               "nginx -g 'daemon of…"   About an hour ago   Up About an hour    0.0.0.0:8080->80/tcp   wizardly_mcclintock
6becd04e405c        centos              "/bin/ping localhost"    About an hour ago   Up About an hour                           silly_chatterjee
```
<br>

## 컨테이너 재기동 (docker restart)
---
`docker restart [옵션] <컨테이너 식별자>`
```
$ docker restart 53e652bede18

53e652bede18
```
```
$ docker ps

CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                  NAMES
9cd3f115880c        nginx               "nginx -g 'daemon of…"   About an hour ago   Up About an hour    0.0.0.0:8080->80/tcp   wizardly_mcclintock
6becd04e405c        centos              "/bin/ping localhost"    About an hour ago   Up About an hour                           silly_chatterjee
53e652bede18        centos              "/bin/bash"              About an hour ago   Up 1 second                                Test3
```
<br>
 
## 정지 중인 컨테이너 삭제 (docker rm)
 ---
`docker rm [옵션] <컨테이너 식별자>`  
```
$ docker ps -a

CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                         PORTS                  NAMES
436377e9d58d        centos              "/bin/bash"              About an hour ago   Exited (0) About an hour ago                          fervent_lalande
cc7a7306349a        centos              "/bin/bash"              About an hour ago   Exited (0) About an hour ago                          loving_mcclintock
23d446e9134d        centos              "bin/bash"               About an hour ago   Exited (0) About an hour ago                          volumetest1
9cd3f115880c        nginx               "nginx -g 'daemon of…"   About an hour ago   Up About an hour               0.0.0.0:8080->80/tcp   wizardly_mcclintock
6becd04e405c        centos              "/bin/ping localhost"    About an hour ago   Up About an hour                                      silly_chatterjee
188a421b227f        centos              "/bin/bash"              About an hour ago   Exited (0) About an hour ago                          Test2
53e652bede18        centos              "/bin/bash"              2 hours ago         Up 2 minutes                                          Test3
608e309487bd        centos              "/bin/cal"               2 hours ago         Exited (0) 6 minutes ago                              Test
```
```
$ docker rm 436377e9d58d

436377e9d58d
```
```
$ docker ps -a

CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                         PORTS                  NAMES
cc7a7306349a        centos              "/bin/bash"              About an hour ago   Exited (0) About an hour ago                          loving_mcclintock
23d446e9134d        centos              "bin/bash"               About an hour ago   Exited (0) About an hour ago                          volumetest1
9cd3f115880c        nginx               "nginx -g 'daemon of…"   About an hour ago   Up About an hour               0.0.0.0:8080->80/tcp   wizardly_mcclintock
6becd04e405c        centos              "/bin/ping localhost"    About an hour ago   Up About an hour                                      silly_chatterjee
188a421b227f        centos              "/bin/bash"              About an hour ago   Exited (0) About an hour ago                          Test2
53e652bede18        centos              "/bin/bash"              2 hours ago         Up 3 minutes                                          Test3
608e309487bd        centos              "/bin/cal"               2 hours ago         Exited (0) 7 minutes ago                              Test
```
<br>

## 정지 중인 모든 컨테이너 삭제 (docker container prune)
---
`docker container prune [옵션]`  
```
$ docker container prune

WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
cc7a7306349aa7bffa40780ff30b31b6644dfa5894820e1f71327ea5934df78b
23d446e9134d3e302509b869629f2b6d1b8f3842724d4b09d258ede4a72777f0
188a421b227fc4ba7b2d8341082624d8a4424faf97ac9e7ab5f1af4043c6f30c
608e309487bd21a979de80637ef0ec27d24d331e6e8848dc1fd07fbcf0e3f4d3

Total reclaimed space: 43B
```
```
$ docker ps -a

CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                  NAMES
9cd3f115880c        nginx               "nginx -g 'daemon of…"   25 hours ago        Up 25 hours         0.0.0.0:8080->80/tcp   wizardly_mcclintock
6becd04e405c        centos              "/bin/ping localhost"    25 hours ago        Up 25 hours                                silly_chatterjee
53e652bede18        centos              "/bin/bash"              25 hours ago        Up 24 hours                                Test3
```
<br>

## 실행 중인 컨테이너(작동 중인 프로세스) 정지 (docker pause)
---
`docker pause <컨테이너 식별자>`  
```
$ docker pause 9cd3f115880c

9cd3f115880c
```
```
$ docker ps

CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                 PORTS                  NAMES
9cd3f115880c        nginx               "nginx -g 'daemon of…"   25 hours ago        Up 25 hours (Paused)   0.0.0.0:8080->80/tcp   wizardly_mcclintock
6becd04e405c        centos              "/bin/ping localhost"    25 hours ago        Up 25 hours                                   silly_chatterjee
53e652bede18        centos              "/bin/bash"              25 hours ago        Up 24 hours                                   Test3
```
<br>

## 정지 중인 컨테이너 시작 (docker unpause)
---
`docker unpause <컨테이너 식별자>`  
```
$ docker unpause 9cd3f115880c

9cd3f115880c
```
```
$ docker ps

CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                  NAMES
9cd3f115880c        nginx               "nginx -g 'daemon of…"   25 hours ago        Up 25 hours         0.0.0.0:8080->80/tcp   wizardly_mcclintock
6becd04e405c        centos              "/bin/ping localhost"    25 hours ago        Up 25 hours                                silly_chatterjee
53e652bede18        centos              "/bin/bash"              25 hours ago        Up 24 hours                                Test3
```
<br>

## 실행 중인 컨테이너에 접속(docker attach)
---
`docker attach [옵션] <컨테이너 식별자>`  
```
$ docker run -it -d centos /bin/bash

1c9750acdca25f179a7bbb9216ebb92a7887149f7ad582c6ae05c4dadaca6f28
```
```
$ docker ps

CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                  NAMES
1c9750acdca2        centos              "/bin/bash"              2 seconds ago       Up 2 seconds                               nostalgic_gates
9cd3f115880c        nginx               "nginx -g 'daemon of…"   5 days ago          Up 4 days           0.0.0.0:8080->80/tcp   wizardly_mcclintock
6becd04e405c        centos              "/bin/ping localhost"    5 days ago          Up 5 days                                  silly_chatterjee
53e652bede18        centos              "/bin/bash"              5 days ago          Up 4 days                                  Test3
```
```
$ docker attach 1c9750acdca2

[root@1c9750acdca2 /]# ls
bin  dev  etc  home  lib  lib64  lost+found  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```
```
$ docker attach 9cd3f115880c

```
<br>

## 실행 중인 컨테이너에서 프로세스 실행(docker exec)
---
`docker exex [옵션] <컨테이너 식별자> <실행할 명령> [인수]`
```
$ docker ps

CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                  NAMES
9cd3f115880c        nginx               "nginx -g 'daemon of…"   5 days ago          Up 4 days           0.0.0.0:8080->80/tcp   wizardly_mcclintock
6becd04e405c        centos              "/bin/ping localhost"    5 days ago          Up 5 days                                  silly_chatterjee
53e652bede18        centos              "/bin/bash"              5 days ago          Up 4 days                                  Test3
```
```
$ docker exec -it 9cd3f115880c /bin/bash

root@9cd3f115880c:/# ls
bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@9cd3f115880c:/# 
```
```
$ docker exec -it 9cd3f115880c /bin/echo "hello"

hello
```
<br>

## 실행 중인 컨테이너의 포트 정보 확인(docker port)
---
`docker port <컨테이너 식별자> [특정 포트]`
```
$ docker ps

CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                  NAMES
9cd3f115880c        nginx               "nginx -g 'daemon of…"   5 days ago          Up 2 minutes        0.0.0.0:8080->80/tcp   wizardly_mcclintock
6becd04e405c        centos              "/bin/ping localhost"    5 days ago          Up 5 days                                  silly_chatterjee
53e652bede18        centos              "/bin/bash"              5 days ago          Up 4 days                                  Test3
```
```
$ docker port 9cd3f115880c

80/tcp -> 0.0.0.0:8080
```
```
$ docker port 9cd3f115880c 80

0.0.0.0:8080
```
<br>

## 컨테이너 이름 변경(docker rename)
---
`docker rename <변경 전 이름> <변경 후 이름>`
```
$ docker ps

CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                  NAMES
9cd3f115880c        nginx               "nginx -g 'daemon of…"   5 days ago          Up 2 minutes        0.0.0.0:8080->80/tcp   wizardly_mcclintock
6becd04e405c        centos              "/bin/ping localhost"    5 days ago          Up 5 days                                  silly_chatterjee
53e652bede18        centos              "/bin/bash"              5 days ago          Up 4 days                                  Test3
```
```
$ docker rename wizardly_mcclintock nginx

$ docker ps

CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                  NAMES
9cd3f115880c        nginx               "nginx -g 'daemon of…"   5 days ago          Up 10 minutes       0.0.0.0:8080->80/tcp   nginx
6becd04e405c        centos              "/bin/ping localhost"    5 days ago          Up 5 days                                  silly_chatterjee
53e652bede18        centos              "/bin/bash"              5 days ago          Up 4 days                                  Test3
```
<br>

## 컨테이너와 호스트간의 파일 복사(docker cp)
---
`docker cp <컨테이너 식별자>:<컨테이너 안의 파일 경로> <호스트의 디렉토리 경로>`
```
$ docker cp 9cd3f115880c:/etc/nginx/nginx.conf ./nginx.conf
```
```
$ ls

Desktop  Documents  Downloads  env_list  examples.desktop  Music  nginx.conf  Pictures  Public  Templates  Videos  vtest
```
`docker cp <호스트 파일> <컨테이너 식별자>:<컨테이너 안의 파일 경로>` 
```
$ ls

Desktop  Documents  Downloads  env_list  examples.desktop  local.txt  Music  nginx.conf  Pictures  Public  Templates  Videos  vtest
```
```
$ docker cp ./local.txt 9cd3f115880c:/tmp/local.txt
```
```
$ docker exec -it 9cd3f115880c /bin/bash

root@9cd3f115880c:/# ls
bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@9cd3f115880c:/# cd /tmp/
root@9cd3f115880c:/tmp# ls
local.txt
```
<br>

## 컨테이너 변경 내역 확인(docker diff)
`docker diff <컨테이너 식별자>`
```
$ docker diff 9cd3f115880c

C /tmp
A /tmp/local.txt
C /root
A /root/.bash_history
C /run
A /run/nginx.pid
C /var
C /var/cache
C /var/cache/nginx
A /var/cache/nginx/fastcgi_temp
A /var/cache/nginx/proxy_temp
A /var/cache/nginx/scgi_temp
A /var/cache/nginx/uwsgi_temp
A /var/cache/nginx/client_temp
```
<br>

## 컨테이너로부터의 이미지 생성(docker commit)
`docker commit [옵션] <컨테이너 식별자> [이미지명[:태그명]]`
```
$ docker ps

CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                  NAMES
9cd3f115880c        nginx               "nginx -g 'daemon of…"   5 days ago          Up 38 minutes       0.0.0.0:8080->80/tcp   nginx
6becd04e405c        centos              "/bin/ping localhost"    5 days ago          Up 5 days                                  silly_chatterjee
53e652bede18        centos              "/bin/bash"              5 days ago          Up 4 days                                  Test3
```
```
$ docker commit 9cd3f115880c ysg/newnaginx:1.1

sha256:ed64139f3913a9fd33afff4632b6af1cf3e1096a93cc6e5bd7f51ef92417ee20
```
```
$ docker images

REPOSITORY             TAG                 IMAGE ID            CREATED             SIZE
ysg/newnaginx          1.1                 ed64139f3913        2 seconds ago       126MB
nginx                  latest              540a289bab6c        10 days ago         126MB
sanggil1107/ysgnginx   1.0                 540a289bab6c        10 days ago         126MB
centos                 latest              0f3e07c0138f        4 weeks ago         220MB
ysg/ysgcentos          1.0                 67fa590cfc1c        2 months ago        202MB
```
<br>

## 컨테이너를 파일로 출력(docker export)
---
`docker export <컨테이너 식별자>`
```
$ docker ps

CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                  NAMES
9cd3f115880c        nginx               "nginx -g 'daemon of…"   5 days ago          Up 45 minutes       0.0.0.0:8080->80/tcp   nginx
6becd04e405c        centos              "/bin/ping localhost"    5 days ago          Up 5 days                                  silly_chatterjee
53e652bede18        centos              "/bin/bash"              5 days ago          Up 4 days                                  Test3
```
```
$ docker exprort 9cd3f115880c > nginx.tar
```
```
$ ls -al

total 125464
drwxr-xr-x 19 ysg  ysg       4096 11월  2 13:25 .
drwxr-xr-x  3 root root      4096  8월 29 01:23 ..
-rw-rw-r--  1 ysg  ysg  128327680 11월  2 13:25 nginx.tar
```
<br>

## 파일로부터 이미지 생성(docker import)
---
`docker import <파일 또는 URL> [이미지명[:태그명]]`
```
$ docker import nginx.tar new:1.1

sha256:c1cbed9183aeb68827dfda66f2f4efb4b05400462174d429b0a1ef929cd76d06
```
```
$ docker images

REPOSITORY             TAG                 IMAGE ID            CREATED              SIZE
new                    1.1                 c1cbed9183ae        About a minute ago   125MB
```
<br>

## 이미지를 파일로 저장(docker save)
---
`docker save [옵션] <저장 파일명> [이미지명]`
```
$ docker images

REPOSITORY             TAG                 IMAGE ID            CREATED             SIZE
new                    1.1                 c1cbed9183ae        5 minutes ago       125MB
ysg/newnaginx          1.1                 ed64139f3913        18 minutes ago      126MB
nginx                  latest              540a289bab6c        10 days ago         126MB
sanggil1107/ysgnginx   1.0                 540a289bab6c        10 days ago         126MB
centos                 latest              0f3e07c0138f        4 weeks ago         220MB
ysg/ysgcentos          1.0                 67fa590cfc1c        2 months ago        202MB
```
```
$ docker save -o new.zip new
```
```
$ ls -al

total 250792
drwxr-xr-x 19 ysg  ysg       4096 11월  2 13:40 .
drwxr-xr-x  3 root root      4096  8월 29 01:23 ..
-rw-------  1 ysg  ysg  128335872 11월  2 13:40 new.zip
```
<br>

## 이미지 읽기(docker load)
---
`docker load [옵션] [파일]`
```
$ docker load -i new.zip

Loaded image: new:1.1
```
<br>

## 불필요한 리소스 - 이미지/컨테이너 정리(docker system prune)
---
`docker system prune [옵션]`
```
$ docker system prune -a
WARNING! This will remove:
        - all stopped containers
        - all networks not used by at least one container
        - all images without at least one container associated to them
        - all build cache
Are you sure you want to continue? [y/N] y
Deleted Containers:
1c9750acdca25f179a7bbb9216ebb92a7887149f7ad582c6ae05c4dadaca6f28
53fdaf5ad92ea050a08c1f1b5e15ec8fce56e3b553325a48de373487c549c563
57593f9eeedca92f191120f59296fcd75dba41a9266e26972a13688891eb7708
9a28ba890e81716b4fe1e5bb135032df12cfdc0d0b9b39b4f51f87bcf67e35d4

Deleted Images:
untagged: nginx:latest
untagged: nginx@sha256:922c815aa4df050d4df476e92daed4231f466acc8ee90e0e774951b0fd7195a4
untagged: ysg/newnaginx:1.1
deleted: sha256:ed64139f3913a9fd33afff4632b6af1cf3e1096a93cc6e5bd7f51ef92417ee20
deleted: sha256:7290db1730e6adac29da378c94178ae107454640e582e96b524032006a3e44b9
untagged: new:1.1
deleted: sha256:c1cbed9183aeb68827dfda66f2f4efb4b05400462174d429b0a1ef929cd76d06
deleted: sha256:56fca39b276e62f00fd4be15ff94962defb88d27605b6021775a2665aa5d0b0a
untagged: ysg/ysgcentos:1.0
deleted: sha256:67fa590cfc1c207c30b837528373f819f6262c884b7e69118d060a0c04d70ab8
deleted: sha256:877b494a9f30e74e61b441ed84bb74b14e66fb9cc321d83f3a8a19c60d078654

Total reclaimed space: 326.4MB
```
```
$ docker ps -a

CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                  NAMES
9cd3f115880c        540a289bab6c        "nginx -g 'daemon of…"   5 days ago          Up About an hour    0.0.0.0:8080->80/tcp   nginx
6becd04e405c        centos              "/bin/ping localhost"    5 days ago          Up 5 days                                  silly_chatterjee
53e652bede18        centos              "/bin/bash"              5 days ago          Up 4 days                                  Test3
```
```
$ docker images

REPOSITORY             TAG                 IMAGE ID            CREATED             SIZE
sanggil1107/ysgnginx   1.0                 540a289bab6c        10 days ago         126MB
centos                 latest              0f3e07c0138f        4 weeks ago         220MB
```
<br>

## 이미지 생성(docker build)
---
Dockerfile로부터 이미지를 생성
`docker build [옵션] <dockerfile 경로>`
```
$ docker build -t dockerfile4 .

Sending build context to Docker daemon  2.048kB
Step 1/2 : FROM ubuntu:16.04
 ---> 5f2bf26e3524
Step 2/2 : ENTRYPOINT ["echo", "Hello ENTRYPOINT"]
 ---> Running in 059f7f22e938
Removing intermediate container 059f7f22e938
 ---> b8e3559cdd3d
Successfully built b8e3559cdd3d
Successfully tagged dockerfile4:latest
```