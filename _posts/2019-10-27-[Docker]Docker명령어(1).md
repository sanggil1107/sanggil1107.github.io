---
layout: post
title: "[Docker] 3.Docker 명렁어(1)"
category: [Docker]
---
<br>
Docker 명령어에 대해 알아보자
<!-- more -->
<hr>

```cs
#docker image pull [옵션] 이미지명[:태그]
```

```
$ docker image pull centos:7

7: Pulling from library/centos
d8d02d457314: Pull complete 
Digest: sha256:307835c385f656ec2e2fec602cf093224173c51119bbebd602c53c3653a3d6eb
Status: Downloaded newer image for centos:7
```

```docker images [옵션] [repository명]```
```
$ docker images

REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
centos              7                   67fa590cfc1c        2 weeks ago         202MB
```

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

`docker image tag 원본이미지 태그이미지`  
단 docker hub에 push 하기 위해서는 `Docker hub 사용자명/이미지명:[태그명]` 형식으로 태그이미지를 지정해야한다.
```
$ docker image tag centos:7 ysg/ysgcentos:1.0
$ docker images

REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
centos              7                   67fa590cfc1c        2 months ago        202MB
ysg/ysgcentos       1.0                 67fa590cfc1c        2 months ago        202MB
```

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

`docker image rm [옵션] 이미지명`
```
$ docker image rm centos:7

Untagged: centos:7
Untagged: centos@sha256:307835c385f656ec2e2fec602cf093224173c51119bbebd602c53c3653a3d6eb

$ docker images

REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ysg/ysgcentos       1.0                 67fa590cfc1c        2 months ago        202MB
```



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

`docker push 이미지명[:태그명]`
```
$ docker push sanggil1107/ysgnginx:1.0

The push refers to repository [docker.io/sanggil1107/ysgnginx]
a89b8f05da3a: Pushed 
6eaad811af02: Pushed 
b67d19e65ef6: Pushed 
1.0: digest: sha256:f56b43e9913cef097f246d65119df4eda1d61670f7f2ab720831a01f66f6ff9c size: 948
```

`docker logout [서버명]`
```
$ docker logout
Removing login credentials for https://index.docker.io/v1/
```

`docker run [옵션] 이미지명[:태그명] [인수]`
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
$ docker run -d centos /bin/ping localhost

6becd04e405cabfc1e627ef6b3f573212762101f6419c157ef22246b1dce57c9
```

`docker logs `
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

`docker stats [컨테이너 식별자]`
```
$ docker stats

CONTAINER ID        NAME                  CPU %               MEM USAGE / LIMIT     MEM %               NET I/O             BLOCK I/O           PIDS
9cd3f115880c        wizardly_mcclintock   0.00%               2.211MiB / 3.852GiB   0.06%               12.5kB / 1.75kB     0B / 0B             2
6becd04e405c        silly_chatterjee      0.01%               968KiB / 3.852GiB     0.02%               11.6kB / 0B         0B / 0B             1
```

`docker top 컨테이너 식별자`
```
$ docker top 9cd3f115880c

UID                 PID                 PPID                C                   STIME               TTY                 TIME                CMD
root                6157                6134                0                   10월27               ?                   00:00:00            nginx: master process nginx -g daemon off;
systemd+            6204                6157                0                   10월27               ?                   00:00:00            nginx: worker process
```