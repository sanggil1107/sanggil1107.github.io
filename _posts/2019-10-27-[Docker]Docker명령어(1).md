---
layout: post
title: "[Docker] 3.Docker 명렁어(1)"
category: [Docker]
image: /public/img/알고리즘/삽입정렬3.png
---
<br>
Docker 명령어에 대해 알아보자
<!-- more -->
<hr>

# Docker 명령어

## 이미지 다운로드 (docker pull)
---
`docker image pull [옵션] 이미지명[:태그]`
```
$ docker image pull centos:7

7: Pulling from library/centos
d8d02d457314: Pull complete 
Digest: sha256:307835c385f656ec2e2fec602cf093224173c51119bbebd602c53c3653a3d6eb
Status: Downloaded newer image for centos:7
```
<br>

## 이미지 목록 (docker images)
---
`docker images [옵션] [repository명]`
```
$ docker images

REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
centos              7                   67fa590cfc1c        2 weeks ago         202MB
```
<br>

## 이미지 상세정보 (docker inspect)
---
`docker image inspect 이미지명[:태그]`
```
$ docker image inspect centos:7

[
    {
        "Id": "sha256:67fa590cfc1c207c30b837528373f819f6262c884b7e69118d060a0c04d70ab8",
        "RepoTags": [
            "centos:7"
        ],
        "RepoDigests": [
            "centos@sha256:307835c385f656ec2e2fec602cf093224173c51119bbebd602c53c3653a3d6eb"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2019-08-20T20:21:01.219060918Z",
        "Container": "c77d57543414f78d333710b96b816033f91a246d606e4dd644e75051719a88c3",
        "ContainerConfig": {
            "Hostname": "c77d57543414",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"/bin/bash\"]"
            ],
            "ArgsEscaped": true,
            "Image": "sha256:4c66d610f9092e18227ae1d0de68350d3da2875452762261ccf1c552462dd90d",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {
                "org.label-schema.build-date": "20190801",
                "org.label-schema.license": "GPLv2",
                "org.label-schema.name": "CentOS Base Image",
                "org.label-schema.schema-version": "1.0",
                "org.label-schema.vendor": "CentOS"
            }
        },
        "DockerVersion": "18.06.1-ce",
        "Author": "",
        "Config": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/bash"
            ],
            "ArgsEscaped": true,
            "Image": "sha256:4c66d610f9092e18227ae1d0de68350d3da2875452762261ccf1c552462dd90d",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {
                "org.label-schema.build-date": "20190801",
                "org.label-schema.license": "GPLv2",
                "org.label-schema.name": "CentOS Base Image",
                "org.label-schema.schema-version": "1.0",
                "org.label-schema.vendor": "CentOS"
            }
        },
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 201878234,
        "VirtualSize": 201878234,
        "GraphDriver": {
            "Data": {
                "MergedDir": "/var/lib/docker/overlay2/095871ba6ccbde1ce55f880453cfbba7db253bf8a9fd3a343033ca08197901e7/merged",
                "UpperDir": "/var/lib/docker/overlay2/095871ba6ccbde1ce55f880453cfbba7db253bf8a9fd3a343033ca08197901e7/diff",
                "WorkDir": "/var/lib/docker/overlay2/095871ba6ccbde1ce55f880453cfbba7db253bf8a9fd3a343033ca08197901e7/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:877b494a9f30e74e61b441ed84bb74b14e66fb9cc321d83f3a8a19c60d078654"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]
```
<br>

## 이미지 태그 설정
---
`docker image tag 원본이미지 태그이미지`  
단 docker hub에 push 하기 위해서는 `Docker hub 사용자명/이미지명:[태그명]` 형식으로 태그이미지를 지정해야한다.
```
$ docker image tag centos:7 ysg/ysgcentos:1.0
$ docker images

REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
centos              7                   67fa590cfc1c        2 months ago        202MB
ysg/ysgcentos       1.0                 67fa590cfc1c        2 months ago        202MB
```
<br>

## Docker Hub에서 이미지 검색 (docker search)
---
`docker search [옵션] <검색키워드>`
```
$ docker search nginx

NAME                              DESCRIPTION                                     STARS               OFFICIAL            AUTOMATED
nginx                             Official build of Nginx.                        12109               [OK]                
jwilder/nginx-proxy               Automated Nginx reverse proxy for docker con…   1678                                    [OK]
richarvey/nginx-php-fpm           Container running Nginx + PHP-FPM capable of…   744                                     [OK]
linuxserver/nginx                 An Nginx container, brought to you by LinuxS…   79                                      
bitnami/nginx                     Bitnami nginx Docker Image                      72                                      [OK]
tiangolo/nginx-rtmp               Docker image with Nginx using the nginx-rtmp…   58                                      [OK]
nginxdemos/hello                  NGINX webserver that serves a simple page co…   31                                      [OK]
jlesage/nginx-proxy-manager       Docker container for Nginx Proxy Manager        26                                      [OK]
jc21/nginx-proxy-manager          Docker container for managing Nginx proxy ho…   26                                      
nginx/nginx-ingress               NGINX Ingress Controller for Kubernetes         22                                      
privatebin/nginx-fpm-alpine       PrivateBin running on an Nginx, php-fpm & Al…   18                                      [OK]
schmunk42/nginx-redirect          A very simple container to redirect HTTP tra…   17                                      [OK]
blacklabelops/nginx               Dockerized Nginx Reverse Proxy Server.          12                                      [OK]
centos/nginx-18-centos7           Platform for running nginx 1.8 or building n…   11                                      
centos/nginx-112-centos7          Platform for running nginx 1.12 or building …   10                                      
nginxinc/nginx-unprivileged       Unprivileged NGINX Dockerfiles                  9                                       
nginx/nginx-prometheus-exporter   NGINX Prometheus Exporter                       7                                       
sophos/nginx-vts-exporter         Simple server that scrapes Nginx vts stats a…   5                                       [OK]
1science/nginx                    Nginx Docker images that include Consul Temp…   5                                       [OK]
mailu/nginx                       Mailu nginx frontend                            4                                       [OK]
pebbletech/nginx-proxy            nginx-proxy sets up a container running ngin…   2                                       [OK]
travix/nginx                      NGinx reverse proxy                             2                                       [OK]
ansibleplaybookbundle/nginx-apb   An APB to deploy NGINX                          1                                       [OK]
wodby/nginx                       Generic nginx                                   0                                       [OK]
centos/nginx-110-centos7          Platform for running nginx 1.10 or building …   0                                       
```
<br>

## 이미지 삭제 (docker rmi)
---
`docker rmi [옵션] 이미지명`
```
$ docker rmi centos:7

Untagged: centos:7
Untagged: centos@sha256:307835c385f656ec2e2fec602cf093224173c51119bbebd602c53c3653a3d6eb

$ docker images

REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ysg/ysgcentos       1.0                 67fa590cfc1c        2 months ago        202MB
```
<br>

## Docker Hub 로그인 (docker login)
---
`docker login [옵션] [서버]`
```
$ docker login

Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one.
Username: sanggil1107
Password: 
WARNING! Your password will be stored unencrypted in /home/ysg/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
```

docker hub에 push하기 위해 nginx 이미지 기반으로 태그이미지를 생성한다.

```
$ docker pull nginx

Using default tag: latest
latest: Pulling from library/nginx
8d691f585fa8: Pull complete 
5b07f4e08ad0: Pull complete 
abc291867bca: Pull complete 
Digest: sha256:922c815aa4df050d4df476e92daed4231f466acc8ee90e0e774951b0fd7195a4
Status: Downloaded newer image for nginx:latest
```

```
$ docker image tag nginx sanggil1107/ysgnginx:1.0
$ docker images

REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
nginx                  latest              540a289bab6c        4 days ago          126MB
sanggil1107/ysgnginx   1.0                 540a289bab6c        4 days ago          126MB
ysg/ysgcentos          1.0                 67fa590cfc1c        2 months ago        202MB
```
<br>

## 이미지 업로드 (docker push)
---
`docker push 이미지명[:태그명]`
```
$ docker push sanggil1107/ysgnginx:1.0

The push refers to repository [docker.io/sanggil1107/ysgnginx]
a89b8f05da3a: Pushed 
6eaad811af02: Pushed 
b67d19e65ef6: Pushed 
1.0: digest: sha256:f56b43e9913cef097f246d65119df4eda1d61670f7f2ab720831a01f66f6ff9c size: 948
```
<br>

## Docker hub 로그아웃 (docker logout)
---
`docker logout [서버명]`
```
$ docker logout

Removing login credentials for https://index.docker.io/v1/
```
<br>

## 실행 중인 컨테이너 리소스 사용 정보 (docker stats)
---
`docker stats [컨테이너 식별자]`
```
$ docker stats

CONTAINER ID        NAME                  CPU %               MEM USAGE / LIMIT     MEM %               NET I/O             BLOCK I/O           PIDS
9cd3f115880c        wizardly_mcclintock   0.00%               2.211MiB / 3.852GiB   0.06%               12.5kB / 1.75kB     0B / 0B             2
6becd04e405c        silly_chatterjee      0.01%               968KiB / 3.852GiB     0.02%               11.6kB / 0B         0B / 0B             1
```
<br>


## 컨테이너 목록 (docker ps)
---
`docker ps [옵션]`
```
$ docker ps

CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                  NAMES
9cd3f115880c        nginx               "nginx -g 'daemon of…"   41 minutes ago      Up 41 minutes       0.0.0.0:8080->80/tcp   wizardly_mcclintock
6becd04e405c        centos              "/bin/ping localhost"    About an hour ago   Up About an hour                           silly_chatterjee
```
```
$ docker ps -a

CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                           PORTS                  NAMES
436377e9d58d        centos              "/bin/bash"              21 minutes ago      Exited (0) 21 minutes ago                               fervent_lalande
cc7a7306349a        centos              "/bin/bash"              24 minutes ago      Exited (0) 23 minutes ago                               loving_mcclintock
23d446e9134d        centos              "bin/bash"               28 minutes ago      Exited (0) 28 minutes ago                               volumetest1
9cd3f115880c        nginx               "nginx -g 'daemon of…"   42 minutes ago      Up 42 minutes                    0.0.0.0:8080->80/tcp   wizardly_mcclintock
6becd04e405c        centos              "/bin/ping localhost"    About an hour ago   Up About an hour                                        silly_chatterjee
188a421b227f        centos              "/bin/bash"              About an hour ago   Exited (0) About an hour ago                            Test2
53e652bede18        centos              "/bin/bash"              About an hour ago   Exited (130) About an hour ago                          Test3
608e309487bd        centos              "/bin/cal"               About an hour ago   Exited (0) About an hour ago                            Test
```
```
$ docker ps -a -f name=Test

CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                           PORTS               NAMES
188a421b227f        centos              "/bin/bash"         About an hour ago   Exited (0) About an hour ago                         Test2
53e652bede18        centos              "/bin/bash"         About an hour ago   Exited (130) About an hour ago                       Test3
608e309487bd        centos              "/bin/cal"          About an hour ago   Exited (0) About an hour ago                         Test
```
```
$ docker ps -a -f exited=0

CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                         PORTS               NAMES
436377e9d58d        centos              "/bin/bash"         23 minutes ago      Exited (0) 22 minutes ago                          fervent_lalande
cc7a7306349a        centos              "/bin/bash"         25 minutes ago      Exited (0) 24 minutes ago                          loving_mcclintock
23d446e9134d        centos              "bin/bash"          30 minutes ago      Exited (0) 30 minutes ago                          volumetest1
188a421b227f        centos              "/bin/bash"         About an hour ago   Exited (0) About an hour ago                       Test2
608e309487bd        centos              "/bin/cal"          About an hour ago   Exited (0) About an hour ago                       Test
```
<br>

## 컨테이너에서 실행 중인 프로세스 목록 (docker top)
---
`docker top <컨테이너 식별자>`
```
$ docker top 9cd3f115880c

UID                 PID                 PPID                C                   STIME               TTY                 TIME                CMD
root                6157                6134                0                   10월27               ?                   00:00:00            nginx: master process nginx -g daemon off;
systemd+            6204                6157                0                   10월27               ?                   00:00:00            nginx: worker process
```
