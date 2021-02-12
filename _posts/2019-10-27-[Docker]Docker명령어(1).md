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

docker hub에서 이미지 다운

---
`docker pull [옵션] 이미지명[:태그]`
```
$ docker pull centos:7

7: Pulling from library/centos
2d473b07cdd5: Pull complete
Digest: sha256:0f4ec88e21daf75124b8a9e5ca03c37a5e937e0e108a255d890492430789b60e
Status: Downloaded newer image for centos:7
docker.io/library/centos:7
```
<br>

## 이미지 목록 (docker images)

docker image 목록 출력

---
`docker images [옵션] [repository명]`

|옵션|설명|
|---|---|
|--all, -a|모든 이미지 표시|
|--digests|다이제스트를 표시할지 말지|
|--no-trunc|결과를 모두 표시|
|--quiet, -q|Docker image ID만 표시|
<br>

```
$ docker images

REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
nginx        latest    f6d0b4767a6c   2 weeks ago    133MB
centos       7         8652b9f0cb4c   2 months ago   204MB
```
```
$ docker images nginx

REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
nginx        latest    f6d0b4767a6c   2 weeks ago   133MB
```
<br>

## 이미지 상세정보 (docker inspect)

image 상세정보

---
`docker inspect 이미지명[:태그]`
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

## 이미지 태그 설정(docker tag)
---
`docker tag 원본이미지 태그이미지`  
단 docker hub에 push 하기 위해서는 `Docker hub 사용자명/이미지명:[태그명]` 형식으로 태그이미지를 지정해야한다.
```
$ docker tag centos:7 ysg:1.0
$ docker images

REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
nginx        latest    f6d0b4767a6c   2 weeks ago    133MB
centos       7         8652b9f0cb4c   2 months ago   204MB
ysg          1.0       8652b9f0cb4c   2 months ago   204MB
```
<br>

## Docker Hub에서 이미지 검색 (docker search)
---
`docker search [옵션] <검색키워드>`
```
$ docker search nginx

NAME                               DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
nginx                              Official build of Nginx.                        14372     [OK]
jwilder/nginx-proxy                Automated Nginx reverse proxy for docker con…   1951                 [OK]
richarvey/nginx-php-fpm            Container running Nginx + PHP-FPM capable of…   804                  [OK]
.... 
wodby/nginx                        Generic nginx                                   1                    [OK]
```
<br>

## 이미지 삭제 (docker rmi / docker image prune)
---
`docker rmi [옵션] 이미지명`

|옵션|설명|
|---|---|
|--force, -f|이미지를 강제로 삭제|

```
$ docker images

REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
nginx        latest    f6d0b4767a6c   2 weeks ago    133MB
centos       7         8652b9f0cb4c   2 months ago   204MB
ysg          1.0       8652b9f0cb4c   2 months ago   204MB
```
```
$ docker rmi ysg:1.0

Untagged: ysg:1.0
```
```
$ docker images

REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
nginx        latest    f6d0b4767a6c   2 weeks ago    133MB
centos       7         8652b9f0cb4c   2 months ago   204MB
```

`docker image prune [옵션]`

사용하지 않는 이미지 삭제

|옵션|설명|
|---|---|
|--force, -f|이미지를 강제로 삭제|
|--all, -a|사용하지 않은 이미지 모두 삭제|
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

REPOSITORY             TAG       IMAGE ID       CREATED        SIZE
sanggil1107/ysgnginx   1.0       f6d0b4767a6c   2 weeks ago    133MB
nginx                  latest    f6d0b4767a6c   2 weeks ago    133MB
centos                 7         8652b9f0cb4c   2 months ago   204MB
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
