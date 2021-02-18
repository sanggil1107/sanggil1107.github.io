---
layout: post
title: "[Docker] 4.Docker 명렁어(2)"
category: [Docker]
---
<br>

`Docker 명령어`에 대해 알아보자
<!-- more -->
<hr>

## 컨테이너 생성 및 실행 (docker run)
---
`docker run [옵션] [컨테이너명] 이미지명[:태그명] [인수]`

|옵션|설명|
|---|---|
|--attach, -a|표준 입력, 출력, 오류 출력에 attach 한다.|
|--cidfile|컨테이너 ID를 파일로 출력|
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
다음은 백그라운드에서 컨테이너를 실행하는 방법이다.

|옵션|설명|
|---|---|
|--detach, -d|백그라운드에서 실행|
|--user, -u|사용자명을 지정|
|--restart=`[no | on-failure | on-failure:횟수 | always | unless-stopped]`|명령의 실행 결과에 따라 재시작 옵션|
|--rm|명령 실행 완료 후 컨테이너 자동 삭제|

```
$ docker run -d centos /bin/ping localhost
45cdb13542301f3355e248d902ba299f276f6c35c12555d612336d57e5128a25
```
다음과 같이 컨테이너가 실행 중임을 알 수 있다.
```
$ docker ps
CONTAINER ID   IMAGE     COMMAND                 CREATED          STATUS          PORTS     NAMES
45cdb1354230   centos    "/bin/ping localhost"   17 seconds ago   Up 16 seconds             hungry_wiles
```

다음은 컨테이너의 네트워크를 설정하는 방법이다.
|옵션|설명|
|---|---|
|--add-host 호스트명:IP|컨테이너의 /etc/hosts에 호스트명과 ip를 정의|
|--dns IP주소|컨테이너용 DNS 서버의 IP 지정|
|--expose|지정한 범위의 포트 번호를 할당|
|--mac-address=MAC주소|컨테이너의 MAC 지정|
|--net=`[bridge | none | container:<name | id> | host | NETWORK]`|컨테이너의 네트워크를 지정|
|--hostname, -h|컨테이너 자신의 호스트명 지정|
|--publish, -p 호스트의 포트 번호:컨테이너의 포트 번호|호스트와 컨테이너의 포트 매핑|
|--publish-all, -p|호스트의 임의의 포트를 컨테이너에 할당|
```
$ docker run -d -p 8080:80 nginx

bdf8250879ac608831626240134f331ebb75daec9242298b57bd6ace3fc272a4
```
다음은 컨테이너의 자원을 설정하는 방법이다.
|옵션|설명|
|---|---|
|--cpu-shares, -c|CPU의 사용 배분|
|--memory, -m|사용할 메모리를 제한하여 실행|
|--volume [호스트의 디렉토리]:[컨테이너의 디렉토리], -v|호스트와 컨테이너의 디렉토리 공유|
```
$ docker run -i -t -v /vtest --name volumetest1 centos bin/bash

[root@23d446e9134d /]# ls
bin  dev  etc  home  lib  lib64  lost+found  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var  vtest
```
다음은 컨테이너의 환경변수나 작업 디렉토리를 설정하는 방법이다.
|옵션|설명|
|---|---|
|--env=환경변수, -e|환경변수를 설정|
|--env-file=파일명|환경변수를 파일로부터 설정|
|--read-only=`[true | false]`|컨테이너의 파일 시스템의 읽기 전용 여부 설정|
|--workdir=패스, -w|컨테이너의 작업 디렉토리 지정|
|--user=사용자명, -u|사용자명 또는 UID를 지정|
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


## 컨테이너 목록 (docker ps)
---

작동하는 컨테이너의 가동 상태 확인

`docker ps [옵션]`

|옵션|설명|
|---|---|
|--all, -a|실행 중/정지 중을 포함한 모든 컨테이너 표시|
|--filter, -f|표시할 컨테이너의 필터링|
|--format|표시 포맷을 지정|
|--last, -n|마지막으로 실행된 n건의 컨테이너만 표시|
|--latest, -l|마지막으로 실행된 컨테이너만 표시|
|--no-trunc|정보를 생략하지 않고 표시|
|--quiet, -q|컨테이너 ID만 표시|
|--size, -s|파일 크기 표시|
```
$ docker ps

CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
5fac4b5a8b83   nginx     "/docker-entrypoint.…"   3 seconds ago   Up 2 seconds   0.0.0.0:8080->80/tcp   stupefied_jang
```
```
$ docker ps -a
CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS                      PORTS                  NAMES
5fac4b5a8b83   nginx      "/docker-entrypoint.…"   32 seconds ago   Up 31 seconds               0.0.0.0:8080->80/tcp   stupefied_jang
bdf8250879ac   nginx      "/docker-entrypoint.…"   19 hours ago     Exited (255) 14 hours ago   0.0.0.0:8080->80/tcp   funny_bell
45cdb1354230   centos     "/bin/ping localhost"    19 hours ago     Exited (255) 14 hours ago                          hungry_wiles
2f16a1d56967   centos     "/bin/bash"              19 hours ago     Exited (130) 19 hours ago                          Test1
8fcfc5c36f94   centos     "/bin/cal"               19 hours ago     Exited (0) 19 hours ago                            Test
d898e872e5c2   centos:7   "/bin/bash"              11 days ago      Exited (137) 11 days ago                           cool_mestorf
```
```
$ docker ps -a -f name=Test

CONTAINER ID   IMAGE     COMMAND       CREATED        STATUS                      PORTS     NAMES
2f16a1d56967   centos    "/bin/bash"   19 hours ago   Exited (130) 19 hours ago             Test1
8fcfc5c36f94   centos    "/bin/cal"    19 hours ago   Exited (0) 19 hours ago               Test
```
```
$ docker ps -a -f exited=0

CONTAINER ID   IMAGE     COMMAND      CREATED        STATUS                    PORTS     NAMES
8fcfc5c36f94   centos    "/bin/cal"   19 hours ago   Exited (0) 19 hours ago             Test
```
<br> 
  

## 실행 중인 컨테이너 리소스 사용 정보 (docker stats)
---

작동하는 컨테이너 가동 상태 확인

`docker stats [컨테이너 식별자]`
```
$ docker stats

CONTAINER ID   NAME             CPU %     MEM USAGE / LIMIT    MEM %     NET I/O       BLOCK I/O   PIDS
5fac4b5a8b83   stupefied_jang   0.00%     8.297MiB / 12.4GiB   0.07%     1.31kB / 0B   0B / 0B     2
CONTAINER ID   NAME             CPU %     MEM USAGE / LIMIT    MEM %     NET I/O       BLOCK I/O   PIDS
5fac4b5a8b83   stupefied_jang   0.00%     8.297MiB / 12.4GiB   0.07%     1.31kB / 0B   0B / 0B     2
CONTAINER ID   NAME             CPU %     MEM USAGE / LIMIT    MEM %     NET I/O       BLOCK I/O   PIDS
5fac4b5a8b83   stupefied_jang   0.00%     8.297MiB / 12.4GiB   0.07%     1.31kB / 0B   0B / 0B     2
CONTAINER ID   NAME             CPU %     MEM USAGE / LIMIT    MEM %     NET I/O       BLOCK I/O   PIDS
...
```
<br>


## 컨테이너에서 실행 중인 프로세스 목록 (docker top)
---
`docker top <컨테이너 식별자>`
```
$ docker top 5fac4b5a8b83
UID                 PID                 PPID                C                   STIME               TTY                 TIME                CMD
root                866                 845                 0                   06:11               ?                   00:00:00            nginx: master process nginx -g daemon off;
uuidd               927                 866                 0                   06:11               ?                   00:00:00            nginx: worker process
```
<br>

## 컨테이너 로그 확인
---
`docker logs `
```
$ docker run -d centos /bin/ping localhost
45cdb13542301f3355e248d902ba299f276f6c35c12555d612336d57e5128a25
```
```
$ docker logs 45cdb13542301f3355e248d902ba299f276f6c35c12555d612336d57e5128a25

PING localhost (127.0.0.1) 56(84) bytes of data.
64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.149 ms
64 bytes from localhost (127.0.0.1): icmp_seq=2 ttl=64 time=0.020 ms
64 bytes from localhost (127.0.0.1): icmp_seq=3 ttl=64 time=0.022 ms
64 bytes from localhost (127.0.0.1): icmp_seq=4 ttl=64 time=0.024 ms
64 bytes from localhost (127.0.0.1): icmp_seq=5 ttl=64 time=0.022 ms
64 bytes from localhost (127.0.0.1): icmp_seq=6 ttl=64 time=0.020 ms
64 bytes from localhost (127.0.0.1): icmp_seq=7 ttl=64 time=0.030 ms
64 bytes from localhost (127.0.0.1): icmp_seq=8 ttl=64 time=0.019 ms
...
```
<br>

## 정지된 컨테이너 기동 (docker start)
---
`docker start [옵션] <컨테이너 식별자>`
```
$ docker start 45cdb1354230

45cdb1354230
```
```
$ docker ps

CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
5fac4b5a8b83   nginx     "/docker-entrypoint.…"   16 minutes ago   Up 16 minutes   0.0.0.0:8080->80/tcp   stupefied_jang
45cdb1354230   centos    "/bin/ping localhost"    19 hours ago     Up 16 seconds                          hungry_wiles
```
<br>

## 실행 중인 컨테이너 정지 (docker stop)
---
`docker stop [옵션] <컨테이너 식별자>`
```
$ docker stop 45cdb1354230

45cdb1354230
```
```
$ docker ps

CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
5fac4b5a8b83   nginx     "/docker-entrypoint.…"   19 minutes ago   Up 19 minutes   0.0.0.0:8080->80/tcp   stupefied_jang
```
<br>

## 컨테이너 재기동 (docker restart)
---
`docker restart [옵션] <컨테이너 식별자>`
```
$ docker restart 45cdb1354230

45cdb1354230
```
```
$ docker ps

CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
5fac4b5a8b83   nginx     "/docker-entrypoint.…"   26 minutes ago   Up 26 minutes   0.0.0.0:8080->80/tcp   stupefied_jang
45cdb1354230   centos    "/bin/ping localhost"    19 hours ago     Up 2 seconds                           hungry_wiles
```
<br>

## 정지 중인 컨테이너 삭제 (docker rm)
 ---
`docker rm [옵션] <컨테이너 식별자>`  
```
$ docker ps -a

CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS                      PORTS                  NAMES
5fac4b5a8b83   nginx      "/docker-entrypoint.…"   31 minutes ago   Up 31 minutes               0.0.0.0:8080->80/tcp   stupefied_jang
bdf8250879ac   nginx      "/docker-entrypoint.…"   19 hours ago     Exited (255) 15 hours ago   0.0.0.0:8080->80/tcp   funny_bell
45cdb1354230   centos     "/bin/ping localhost"    20 hours ago     Up 5 minutes                                       hungry_wiles
2f16a1d56967   centos     "/bin/bash"              20 hours ago     Exited (130) 20 hours ago                          Test1
8fcfc5c36f94   centos     "/bin/cal"               20 hours ago     Exited (0) 20 hours ago                            Test
d898e872e5c2   centos:7   "/bin/bash"              11 days ago      Exited (137) 11 days ago                           cool_mestorf
```
```
$ docker rm d898e872e5c2

d898e872e5c2
```
```
$ docker ps -a

CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS                      PORTS                  NAMES
5fac4b5a8b83   nginx     "/docker-entrypoint.…"   32 minutes ago   Up 32 minutes               0.0.0.0:8080->80/tcp   stupefied_jang
bdf8250879ac   nginx     "/docker-entrypoint.…"   19 hours ago     Exited (255) 15 hours ago   0.0.0.0:8080->80/tcp   funny_bell
45cdb1354230   centos    "/bin/ping localhost"    20 hours ago     Up 5 minutes                                       hungry_wiles
2f16a1d56967   centos    "/bin/bash"              20 hours ago     Exited (130) 20 hours ago                          Test1
8fcfc5c36f94   centos    "/bin/cal"               20 hours ago     Exited (0) 20 hours ago                            Test
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
bdf8250879ac608831626240134f331ebb75daec9242298b57bd6ace3fc272a4
2f16a1d569675351c994e5231ae2edba984aea8a08aa9157aa232dcc81431069
8fcfc5c36f94dc8549ade12f2efec7b751b4cda302b74e426b86af94e0734c81

Total reclaimed space: 1.124kB
```
```
$ docker ps -a

CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
5fac4b5a8b83   nginx     "/docker-entrypoint.…"   35 minutes ago   Up 35 minutes   0.0.0.0:8080->80/tcp   stupefied_jang
45cdb1354230   centos    "/bin/ping localhost"    20 hours ago     Up 8 minutes                           hungry_wiles
```
<br>

## 실행 중인 컨테이너(작동 중인 프로세스) 중단 (docker pause)
---
`docker pause <컨테이너 식별자>`  
```
$ docker pause 5fac4b5a8b83

5fac4b5a8b83
```
```
$ docker ps

CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS                   PORTS                  NAMES
5fac4b5a8b83   nginx     "/docker-entrypoint.…"   44 minutes ago   Up 44 minutes (Paused)   0.0.0.0:8080->80/tcp   stupefied_jang
45cdb1354230   centos    "/bin/ping localhost"    20 hours ago     Up 17 minutes                                   hungry_wiles
```
<br>

## 정지 중인 컨테이너 시작 (docker unpause)
---
`docker unpause <컨테이너 식별자>`  
```
$ docker unpause 5fac4b5a8b83

5fac4b5a8b83
```
```
$ docker ps

CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
5fac4b5a8b83   nginx     "/docker-entrypoint.…"   45 minutes ago   Up 45 minutes   0.0.0.0:8080->80/tcp   stupefied_jang
45cdb1354230   centos    "/bin/ping localhost"    20 hours ago     Up 19 minutes                          hungry_wiles
```
<br>

## 실행 중인 컨테이너에 접속(docker attach)
---

실행 중인 컨테이너에 연결 

`docker attach [옵션] <컨테이너 식별자>`  
```
$ docker run -it -d centos /bin/bash

bb8f15806b843fafd11d281e0d85b4f00a43e27d0268d23ad463762fbce605c0
```
```
$ docker ps

CONTAINER ID   IMAGE     COMMAND       CREATED         STATUS         PORTS     NAMES
bb8f15806b84   centos    "/bin/bash"   5 seconds ago   Up 4 seconds             vibrant_ramanujan
```
```
$ docker attach bb8f15806b84

[root@bb8f15806b84 /]# ls
bin  dev  etc  home  lib  lib64  lost+found  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```
<br>

## 실행 중인 컨테이너에서 프로세스 실행(docker exec)
---

실행 중인 컨테이너에서 새로운 프로세스를 실행

`docker exec [옵션] <컨테이너 식별자> <실행할 명령> [인수]`

|옵션|설명|
|---|---|
|--detach, -d|명령을 백그라운드에서 실행|
|--interactive, -i|컨테이너의 표준 입력|
|--tty, -t|단말 디바이스를 사용|
|--user, -u|사용자명을 지정|

```
$ docker ps

CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
a22d39d575b6   nginx     "/docker-entrypoint.…"   37 seconds ago   Up 37 seconds   0.0.0.0:8080->80/tcp   laughing_gauss
```
```
$ docker exec -it a22d39d575b6 /bin/bash

root@a22d39d575b6:/# ls
bin   dev                  docker-entrypoint.sh  home  lib64  mnt  proc  run   srv  tmp  var
boot  docker-entrypoint.d  etc                   lib   media  opt  root  sbin  sys  usr
```
```
$ docker exec -it a22d39d575b6 /bin/echo "hi"

hi
```

`docker attach`로 /bin/bash 에 접속한 후 exit를 통해 나오면 컨테이너가 죽지만,
`docker exec`로 /bin/bash에 접속한 후 exit를 통해 나와도 컨테이너가 죽지 않는다.
`attach`
```
$ docker ps

CONTAINER ID   IMAGE     COMMAND       CREATED         STATUS         PORTS     NAMES
cd21d85bfdae   centos    "/bin/bash"   5 minutes ago   Up 5 minutes             sharp_mclean
```
```
$ docker attach cd21d85bfdae

[root@cd21d85bfdae /]# exit
exit
```
```
$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```
`exec`
```
$ docker ps

CONTAINER ID   IMAGE     COMMAND       CREATED         STATUS        PORTS     NAMES
16f82e5a726c   centos    "/bin/bash"   2 seconds ago   Up 1 second             zealous_rosalind
```
```
$ docker exec -it 16f82e5a726c /bin/bash

[root@16f82e5a726c /]# exit
exit
```
```
$ docker ps

CONTAINER ID   IMAGE     COMMAND       CREATED         STATUS         PORTS     NAMES
16f82e5a726c   centos    "/bin/bash"   2 minutes ago   Up 2 minutes             zealous_rosalind
```
<br>

## 실행 중인 컨테이너의 포트 정보 확인(docker port)
---
`docker port <컨테이너 식별자> [특정 포트]`
```
$ docker ps

CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
809019f71618   nginx     "/docker-entrypoint.…"   3 seconds ago   Up 2 seconds   0.0.0.0:8080->80/tcp   exciting_ganguly
```
```
$ docker port 809019f71618

80/tcp -> 0.0.0.0:8080
```
```
$ docker port 809019f71618 80

0.0.0.0:8080
```
<br>

## 컨테이너 이름 변경(docker rename)
---
`docker rename <변경 전 이름> <변경 후 이름>`
```
$ docker ps

CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
809019f71618   nginx     "/docker-entrypoint.…"   3 minutes ago   Up 3 minutes   0.0.0.0:8080->80/tcp   exciting_ganguly
```
```
$ docker rename exciting_ganguly ysg

$ docker ps

CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
809019f71618   nginx     "/docker-entrypoint.…"   4 minutes ago   Up 4 minutes   0.0.0.0:8080->80/tcp   ysg
```
<br>

## 컨테이너와 호스트간의 파일 복사(docker cp)
---
`docker cp <컨테이너 식별자>:<컨테이너 안의 파일 경로> <호스트의 디렉토리 경로>`
```
$ docker cp 809019f71618:/etc/nginx/nginx.conf ./nginx.conf
```
```
$ ls

nginx.conf
```
`docker cp <호스트 파일> <컨테이너 식별자>:<컨테이너 안의 파일 경로>` 
```
$ ls

nginx.conf  test.txt
```
```
$ docker cp ./test.txt 809019f71618:/tmp/test.txt
```
```
$ docker exec -it 9cd3f115880c /bin/bash

root@809019f71618:/# ls
bin  boot  dev  docker-entrypoint.d  docker-entrypoint.sh  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@809019f71618:/# cd tmp/
root@809019f71618:/tmp# ls
test.txt
```
<br>

## 컨테이너 변경 내역 확인(docker diff)
---
`docker diff <컨테이너 식별자>`
```
$ docker diff 809019f71618
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
C /etc
C /etc/nginx
C /etc/nginx/conf.d
C /etc/nginx/conf.d/default.conf
C /tmp
A /tmp/test.txt
```
<br>

## 컨테이너로부터 이미지 생성(docker commit)
---
`docker commit [옵션] <컨테이너 식별자> [이미지명[:태그명]]`

|옵션|설명|
|---|---|
|--author, -a|작성자를 지정|
|--message, -m|메시지를 지정|
|--change, -c|commit 시 Dockerfile 명령을 지정|
|--pause, -p|컨테이너를 일시 정지하고 commit 실행|

```
$ docker ps

CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
809019f71618   nginx     "/docker-entrypoint.…"   28 minutes ago   Up 28 minutes   0.0.0.0:8080->80/tcp   ysg
```
```
$ docker commit 809019f71618 newimage

sha256:2a0566be6fedfd31d9eae0e245fd35517ce17861b745e3d15d4ac1e17becfcdb
```
```
$ docker images

REPOSITORY             TAG       IMAGE ID       CREATED          SIZE
newimage               latest    2a0566be6fed   13 seconds ago   133MB
```
<br>

## 컨테이너를 파일로 출력(docker export)
---

실행 중인 컨테이너의 디렉토리/파일을 모아 tar로 생성

`docker export <컨테이너 식별자>`
```
$ docker ps

CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
809019f71618   nginx     "/docker-entrypoint.…"   32 minutes ago   Up 32 minutes   0.0.0.0:8080->80/tcp   ysg
```
```
$ docker export 809019f71618 > tartest.tar
```
```
$ ls

tartest.tar
```
<br>

## 파일로부터 이미지 생성(docker import)
---
`docker import <파일 또는 URL> [이미지명[:태그명]]`
```
$ docker import tartest.tar tarimage

sha256:4883995813962e852c8260c9174d497e4e16c649e177c1c0fa75d3565708c937
```
```
$ docker images

REPOSITORY             TAG       IMAGE ID       CREATED         SIZE
tarimage               latest    488399581396   6 seconds ago   131MB
```
<br>

## 이미지를 파일로 저장(docker save)
---
`docker save [옵션] <저장 파일명> [이미지명]`
```
$ docker images

REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
nginx        latest    f6d0b4767a6c   4 weeks ago   133MB
```
```
$ docker save -o nginx.zip nginx
```
```
$ ls

nginx.zip
```
<br>

## 이미지 읽기(docker load)
---
`docker load [옵션] [파일]`
```
$ docker load -i nginx.zip

Loaded image: nginx:latest
```
<br>

## 불필요한 리소스 - 이미지/컨테이너 정리(docker system prune)
---
`docker system prune [옵션]`

|옵션|설명|
|---|---|
|--all, -a|사용하지 않는 리소스를 모두 삭제|
|--force, -f|강제적으로 삭제|

```
$ docker ps -a
CONTAINER ID   IMAGE     COMMAND                  CREATED      STATUS                    PORTS                  NAMES
809019f71618   nginx     "/docker-entrypoint.…"   2 days ago   Up 6 seconds              0.0.0.0:8080->80/tcp   ysg
16f82e5a726c   centos    "/bin/bash"              2 days ago   Exited (255) 2 days ago                          zealous_rosalind
a22d39d575b6   nginx     "/docker-entrypoint.…"   2 days ago   Exited (0) 2 days ago                            laughing_gauss
cd21d85bfdae   centos    "/bin/bash"              2 days ago   Exited (0) 2 days ago                            sharp_mclean
bb8f15806b84   centos    "/bin/bash"              2 days ago   Exited (0) 2 days ago                            vibrant_ramanujan
d46aba680474   centos    "/bin/bash"              2 days ago   Exited (0) 2 days ago                            optimistic_montalcini
be0f97e44094   centos    "/bin/bash"              2 days ago   Exited (0) 2 days ago                            practical_lehmann
e6e0436b2420   centos    "/bin/bash"              2 days ago   Exited (130) 2 days ago                          elegant_beaver
79f2b4d98888   centos    "/bin/bash"              2 days ago   Exited (0) 2 days ago                            relaxed_rosalind
a0380bf99aae   centos    "/bin/bash"              2 days ago   Exited (130) 2 days ago                          festive_bhaskara
641d103ee795   centos    "/bin/bash"              2 days ago   Exited (0) 2 days ago                            keen_pare
701974abc917   centos    "/bin/bash"              2 days ago   Exited (0) 2 days ago                            dreamy_satoshi
5fac4b5a8b83   nginx     "/docker-entrypoint.…"   2 days ago   Exited (0) 2 days ago                            stupefied_jang
45cdb1354230   centos    "/bin/ping localhost"    3 days ago   Exited (0) 2 days ago                            hungry_wiles
```
```
$ docker images

REPOSITORY             TAG       IMAGE ID       CREATED        SIZE
tarimage               latest    488399581396   47 hours ago   131MB
newimage               latest    2a0566be6fed   47 hours ago   133MB
nginx                  latest    f6d0b4767a6c   4 weeks ago    133MB
sanggil1107/ysgnginx   1.0       f6d0b4767a6c   4 weeks ago    133MB
centos                 latest    300e315adb2f   2 months ago   209MB
centos                 7         8652b9f0cb4c   3 months ago   204MB
```
```
$ docker system prune -a
WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all images without at least one container associated to them
  - all build cache

Are you sure you want to continue? [y/N] y
Deleted Containers:
16f82e5a726c685dba4615be5109c27f493de75fc9045ac192d31ac2b18005d4
a22d39d575b6a4e4413b95f209b550d09508ec75a348faae08bbab99dd282e5e
cd21d85bfdae7f3f5b96f0d254025c1cb1cc183e693610c4049c1a57b0ffeae0
bb8f15806b843fafd11d281e0d85b4f00a43e27d0268d23ad463762fbce605c0
d46aba6804748db5df4bce75eec9f6c0eedb765c9ccdfbdee80f2eeadf2418bd
be0f97e44094e140555e74b132599fd02df49c57850745f30115817cd68858ac
e6e0436b24204e41b6e2d04711da00bb171803572723e293ffe10818583b08c8
79f2b4d9888849d10864fe1d9000b411eac7720494dce551bfaff4d80f99f288
a0380bf99aae968e4649255ffece67cd9d0abbf40d43f06af85392d6bcaea9ce
641d103ee7959ff5e03252e7e00acc24fee6be6189846b735b7db7cfb4deee9e
701974abc9179adc130a0fb2349d9a79d972d9f6407c6b403f02321ccfe96724
5fac4b5a8b83dd01ce4372841a5a4dcd8fde959c3d4d7e6036df7f39c09006c3
45cdb13542301f3355e248d902ba299f276f6c35c12555d612336d57e5128a25

Deleted Images:
untagged: centos:latest
untagged: centos@sha256:5528e8b1b1719d34604c87e11dcd1c0a20bedf46e83b5632cdeac91b8c04efc1
deleted: sha256:300e315adb2f96afe5f0b2780b87f28ae95231fe3bdd1e16b9ba606307728f55
deleted: sha256:2653d992f4ef2bfd27f94db643815aa567240c37732cae1405ad1c1309ee9859
untagged: tarimage:latest
deleted: sha256:4883995813962e852c8260c9174d497e4e16c649e177c1c0fa75d3565708c937
deleted: sha256:8bb2e426aa3a81d164c3bdb31b2160945599b2884aa7d0845b32ae8674983bbf
untagged: centos:7
untagged: centos@sha256:0f4ec88e21daf75124b8a9e5ca03c37a5e937e0e108a255d890492430789b60e
deleted: sha256:8652b9f0cb4c0599575e5a003f5906876e10c1ceb2ab9fe1786712dac14a50cf
deleted: sha256:174f5685490326fc0a1c0f5570b8663732189b327007e47ff13d2ca59673db02
untagged: nginx:latest
untagged: nginx@sha256:10b8cc432d56da8b61b070f4c7d2543a9ed17c2b23010b43af434fd40e2ca4aa
untagged: newimage:latest
deleted: sha256:2a0566be6fedfd31d9eae0e245fd35517ce17861b745e3d15d4ac1e17becfcdb
deleted: sha256:ed956f19e85e1aa2ce6471ec960dc52949e4d688a5e6c546c962115fa01d6dc1

Total reclaimed space: 544.6MB
```
```
$ docker ps -a

CONTAINER ID   IMAGE          COMMAND                  CREATED      STATUS         PORTS                  NAMES
809019f71618   f6d0b4767a6c   "/docker-entrypoint.…"   2 days ago   Up 2 minutes   0.0.0.0:8080->80/tcp   ysg
```
```
$ docker images

REPOSITORY             TAG       IMAGE ID       CREATED       SIZE
sanggil1107/ysgnginx   1.0       f6d0b4767a6c   4 weeks ago   133MB
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