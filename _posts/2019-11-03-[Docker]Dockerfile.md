---
layout: post
title: "[Docker] 5.Dockerfile"
category: [Docker]
image: /public/img/알고리즘/삽입정렬3.png
---
<br>
Dockerfile 에 대해 알아보자
<!-- more -->
<hr>

# Dockerfile
---
Docker 상에서 작동시킬 컨테이너의 이미지를 생성하기 위한 설정 파일이며, `docker build` 명령을 통해 Dockerfile에 기술된 설정 정보를 바탕으로 이미지를 생성할 수 있다.

## FROM
---
어떤 이미지로부터 새로운 이미지를 생성할지를 나타내는 베이스 이미지
```
FROM centos:centos7
```
```
$ docker build -t dockerfile .

Sending build context to Docker daemon  2.048kB
Step 1/1 : FROM centos
 ---> 0f3e07c0138f
Successfully built 0f3e07c0138f
Successfully tagged dockerfile:latest
```
```
$ docker images
REPOSITORY             TAG                 IMAGE ID            CREATED             SIZE
dockerfile             latest              0f3e07c0138f        4 weeks ago         220MB
```

## RUN
---
이미지를 생성하는 과정에서 실행될 명령
```
FROM ubuntu:16.04

RUN mkdir /test
RUN apt-get update
RUN apt-get install -y nginx
RUN echo "hello docker"
```
```
$ docker build -t dockerfile1 .

Sending build context to Docker daemon  2.048kB
Step 1/5 : FROM ubuntu:16.04
 ---> 5f2bf26e3524
Step 2/5 : RUN mkdir /test
 ---> Using cache
 ---> 315fa275f252
Step 3/5 : RUN apt-get update
 ---> Running in 83d0f70d1074
Get:1 http://archive.ubuntu.com/ubuntu xenial InRelease [247 kB]
Get:2 http://security.ubuntu.com/ubuntu xenial-security InRelease [109 kB]
...
Reading package lists...
Removing intermediate container 83d0f70d1074
 ---> 82891da53879
Step 4/5 : RUN apt-get install -y nginx
 ---> Running in 1783722f3948
Reading package lists...
Building dependency tree...
Reading state information...
...
Processing triggers for systemd (229-4ubuntu21.22) ...
Removing intermediate container 1783722f3948
 ---> 7db54b9f0832
Step 5/5 : RUN echo "hello docker"
 ---> Running in 99c53e230659
hello docker
Removing intermediate container 99c53e230659
 ---> 29b06a231dab
Successfully built 29b06a231dab
Successfully tagged dockerfile1:latest
```
```
$ docker images

REPOSITORY             TAG                 IMAGE ID            CREATED             SIZE
dockerfile1            latest              29b06a231dab        2 minutes ago       205MB
ubuntu                 16.04               5f2bf26e3524        2 days ago          123MB
```
```
$ docker run -it dockerfile1

root@2d5230899d57:/# ls -al
total 76
drwxr-xr-x   1 root root 4096 Nov  3 08:59 .
drwxr-xr-x   1 root root 4096 Nov  3 08:59 ..
drwxr-xr-x   2 root root 4096 Nov  3 08:48 test

```
```
root@2d5230899d57:/etc# ls -al
total 360
drwxr-xr-x 1 root root    4096 Nov  3 08:59 .
drwxr-xr-x 1 root root    4096 Nov  3 08:59 ..
drwxr-xr-x 6 root root    4096 Nov  3 08:56 nginx
```

## CMD
---
이미지를 바탕으로 생성된 컨테이너 안에서 실행될 명령  
Dockerfile에는 하나의 CMD 명령만 기술 가능  
container 실행 시 run을 통해 명령어 및 인자값을 전달하면 CMD에 명시된 인자 값은 무시
```
FROM ubuntu:16.04

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install nginx

EXPOSE 80

CMD nginx -g 'damon off;'
```
```
$ docker build -t dockerfile2 .
Sending build context to Docker daemon  2.048kB
Step 1/5 : FROM ubuntu:16.04
 ---> 5f2bf26e3524
Step 2/5 : RUN apt-get -y update && apt-get -y upgrade
 ---> Running in 7b68cb919c2f
Get:1 http://archive.ubuntu.com/ubuntu xenial InRelease [247 kB]
...
Removing intermediate container 7b68cb919c2f
 ---> a9bc7e4fe027
Step 3/5 : RUN apt-get -y install nginx
 ---> Running in 9bd2ad70033d
Reading package lists...
Building dependency tree...
...
Processing triggers for systemd (229-4ubuntu21.22) ...
Removing intermediate container 9bd2ad70033d
 ---> 751624ca203c
Step 4/5 : EXPOSE 80
 ---> Running in 2d79da4cbdd7
Removing intermediate container 2d79da4cbdd7
 ---> 684a0a59a7e3
Step 5/5 : CMD nginx -g 'damon off;'
 ---> Running in e3b5d3dc203b
Removing intermediate container e3b5d3dc203b
 ---> 5612afcbc523
Successfully built 5612afcbc523
Successfully tagged dockerfile2:latest
```
```
$ docker images

REPOSITORY             TAG                 IMAGE ID            CREATED              SIZE
dockerfile2            latest              5612afcbc523        About a minute ago   205MB
```
```
$ docker run -d -p 8082:80 dockerfile2

de432b250dcafe0b6de7e0e31108eca059195995f0d22a1c117fbc1862d327ac
```
```
$ docker ps

CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                  NAMES
de432b250dca        dockerfile2         "nginx -g 'daemon of…"   2 seconds ago       Up 1 second         0.0.0.0:8082->80/tcp   festive_pare
```
```
FROM ubuntu:16.04

CMD ["echo", "Hello CMD"]
```
```
$ docker build -t dockerfile3 .

Sending build context to Docker daemon  2.048kB
Step 1/2 : FROM ubuntu:16.04
 ---> 5f2bf26e3524
Step 2/2 : CMD ["echo", "Hello CMD"]
 ---> Running in 68daca9db5d6
Removing intermediate container 68daca9db5d6
 ---> 04721077a911
Successfully built 04721077a911
Successfully tagged dockerfile3:latest
```
```
$ docker run -it dockerfile3

Hello CMD
```
```
$ docker run -it dockerfile3 test

$ docker run -it dockerfile3 "/bin/echo" "HI"

HI
```

## ENTRYPOINT
---
이미지를 바탕으로 생성된 컨테이너 안에서 실행될 명령   
CMD와 달리 container 실행 시 run을 통해 명령어 및 인자값을 전달해도 기존의 명령이 실행
```
FROM ubuntu:16.04

ENTRYPOINT ["echo", "Hello ENTRYPOINT"]
```
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
```
$ docker run -it dockerfile4

Hello ENTRYPOINT
```
```
$ docker run -it dockerfile4 test

Hello ENTRYPOINT test
```

## ENV
---
환경변수 설정
```
FROM ubuntu:16.04

ENV PATH /home
CMD echo $PATH
```
```
$ docker build -t dockerfile5 .

Sending build context to Docker daemon  2.048kB
Step 1/3 : FROM ubuntu:16.04
 ---> 5f2bf26e3524
Step 2/3 : ENV PATH /home
 ---> Using cache
 ---> 79678e5170f7
Step 3/3 : CMD echo $PATH
 ---> Using cache
 ---> 5b6301b6d7f9
Successfully built 5b6301b6d7f9
Successfully tagged dockerfile5:latest
```
```
$ docker run -it dockerfile5

/home
```

## WORKDIR
---
생성할 컨테이너 내의 현재경로 지정
```
FROM ubuntu:16.04

WORKDIR home
WORKDIR DIR

CMD ["/bin/bash", "-c",  "pwd"]
```
```
$ docker build -t dockerfile6 .

Sending build context to Docker daemon  2.048kB
Step 1/4 : FROM ubuntu:16.04
 ---> 5f2bf26e3524
Step 2/4 : WORKDIR home
 ---> Using cache
 ---> 814f2aff4e46
Step 3/4 : WORKDIR DIR
 ---> Using cache
 ---> b5c1d8c8cac6
Step 4/4 : CMD ["/bin/bash", "-c", "pwd"]
 ---> Using cache
 ---> 3246ae187202
Successfully built 3246ae187202
Successfully tagged dockerfile6:latest
```
```
$ docker run -it dockerfile6

/home/DIR
```

```
FROM ubuntu:16.04

WORKDIR home
WORKDIR DIR
```
```
$ docker build -t dockerfile6 .

Sending build context to Docker daemon  2.048kB
Step 1/3 : FROM ubuntu:16.04
 ---> 5f2bf26e3524
Step 2/3 : WORKDIR home
 ---> Using cache
 ---> 814f2aff4e46
Step 3/3 : WORKDIR DIR
 ---> Using cache
 ---> b5c1d8c8cac6
Successfully built b5c1d8c8cac6
Successfully tagged dockerfile6:latest
```
```
$ docker run -it dockerfile6

root@18007ff9830f:/home/DIR#
```

## EXPOSE
---
컨테이너의 공개 포트 번호 지정
```
FROM ubuntu:16.04

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install nginx

EXPOSE 80

CMD nginx -g 'damon off;'
```

## ADD
---
`ADD <복사할 파일 경로> <이미지에서 파일이 위치할 경로>`  
이미지에 호스트상의 파일이나 디렉토리를 추가  
```
FROM ubuntu:16.04

ADD host.html /docker.html 
ADD test /docker_dir 
ADD hos* /docker_dir/ 
ADD hos?.html /docker_dir/ 
ADD test.tar.gz /
ADD https://www.wings.msn.to/index.php /docker_dir/web/
```
- `복사할 파일 경로`는 컨텍스트 아래를 기준으로 하며 컨텍스트 바깥의 파일, 디렉토리나 절대경로는 사용할 수 없다. 
- `복사할 파일 경로`에는 파일뿐만 아니라 디렉토리도 설정할 수 있으며 디렉토리 지정 시 디렉토리의 모든 파일을 복사한다. 또한, 와일드 카드를 사용하여 특정 파일만 복사할 수 있다. 
- `복사할 파일 경로`에 인터넷이 있는 파일의 URL을 설정할 수 있다. 
- `복사할 파일 경로`의 압축파일이 있는 경우, 압축을 해제하고 tar를 풀어서 추가된다. 단, 인터넷에 있는 파일 URL은 압축만 해제한 뒤 tar 파일이 그대로 추가된다. 
- `<이미지에서 파일이 위치할 경로>`의 마지막에 /가 있으면 디렉토리가 생성되고 그 아래 파일이 복사된다. 
- `<이미지에서 파일이 위치할 경로>`은 항상 절대 경로로 설정해야 한다.
- `ADD A.txt B.txt` 형식인 경우 A.txt가 B.txt 이름으로 복사된다. 


```
FROM ubuntu:16.04

ADD host.html /docker_dir/
```
```
$ docker build -t dockerfile7 .

Sending build context to Docker daemon  3.072kB
Step 1/2 : FROM ubuntu:16.04
 ---> 5f2bf26e3524
Step 2/2 : ADD host.html /docker_dir/
 ---> 66555d611940
Successfully built 66555d611940
Successfully tagged dockerfile7:latest
```
```
$ docker run -it dockerfile7

root@6f5bc56088cc:/# ls -al
total 76
drwxr-xr-x   1 root root 4096 Nov  3 13:26 .
drwxr-xr-x   1 root root 4096 Nov  3 13:26 ..
drwxr-xr-x   2 root root 4096 Nov  3 13:26 docker_dir

root@6f5bc56088cc:/docker_dir# ls -al
total 12
drwxr-xr-x 2 root root 4096 Nov  3 13:26 .
drwxr-xr-x 1 root root 4096 Nov  3 13:26 ..
-rw-rw-r-- 1 root root   45 Nov  3 13:25 host.html
```

## COPY
---
이미지에 호스트상의 파일이나 디렉토리를 추가  
`ADD` 명령어와 달리 압축 파일을 추가할 때 압축을 해제하지 않으며, 파일 URL도 사용할 수 없다.
`COPY <복사할 파일 경로> <이미지에서 파일이 위치할 경로>`  
```
FROM ubuntu:16.04

COPY host.html /docker.html 
COPY test /docker_dir
COPY hos* /docker_dir/ 
COPY hos?.html /docker_dir/ 
```
- `복사할 파일 경로`는 컨텍스트 아래를 기준으로 하며 컨텍스트 바깥의 파일, 디렉토리나 절대경로는 사용할 수 없다.
- `복사할 파일 경로`에는 파일뿐만 아니라 디렉토리도 설정할 수 있으며 디렉토리 지정 시 디렉토리의 모든 파일을 복사한다. 또한, 와일드 카드를 사용하여 특정 파일만 복사할 수 있다. 
- `복사할 파일 경로`의 압축파일이 있는 경우, 압축을 해제하지 않고 복사한다.
- `<이미지에서 파일이 위치할 경로>`의 마지막에 /가 있으면 디렉토리가 생성되고 그 아래 파일이 복사된다. 
- `<이미지에서 파일이 위치할 경로>`은 항상 절대 경로로 설정해야 한다.
- `COPY A.txt B.txt` 형식인 경우 A.txt가 B.txt 이름으로 복사된다. 

```
FROM ubuntu:16.04

WORKDIR /docker_idr
COPY test docker_dir_sub
```
```
$ docker build -t dockerfile8 .

Sending build context to Docker daemon  4.608kB
Step 1/3 : FROM ubuntu:16.04
 ---> 5f2bf26e3524
Step 2/3 : WORKDIR /docker_idr
 ---> Running in 322fa8ddf935
Removing intermediate container 322fa8ddf935
 ---> 9eb4c931b670
Step 3/3 : COPY test docker_dir_sub
 ---> 2335c08e48e8
Successfully built 2335c08e48e8
Successfully tagged dockerfile8:latest
```
```
$ docker run -it dockerfile8

root@b6dde00fc6e9:/docker_idr# ls
docker_dir_sub
root@b6dde00fc6e9:/docker_idr/docker_dir_sub# ls
addtest.txt
```