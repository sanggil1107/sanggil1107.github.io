---
layout: post
title: "[Docker] 2.Docker 설치(feat. ubuntu)"
category: [Docker]
---
<br>
Docker 설치해보기 
<!-- more -->
<hr>

# Docker 설치

## 설치환경
OS : ubuntu 16.04

## 설치
docker 설치에 앞서 패키지 정보 업데이트를 해준다.
```
$ sudo apt-get update
```
<br>

docker 설치에 필요한 패키지를 설치한다.
```
$ sudo apt-get install -y apt-transport-https ca-certificates curl 
```
<br>

docker 공식 GPG KEY를 추가한다.
```
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
<br>

docker 저장소 추가를 추가한다.
```
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```
<br>

docker를 설치한다.(18.06 버전)
```
$ sudo apt-get install docker-ce=18.06.0~ce~3-0~ubuntu
```
<br>

docker group에 현재 유저 권한을 추가해준다.
```
$ sudo usermod -aG docker $USER
```
<br>

docker version을 입력하여 정상적으로 설치되었는지 확인한다.
```
$ docker version

Client:  
 Version:           18.06.0-ce  
 API version:       1.38  
 Go version:        go1.10.3  
 Git commit:        0ffa825  
 Built:             Wed Jul 18 19:11:02 2018  
 OS/Arch:           linux/amd64  
 Experimental:      false  
  
Server:  
 Engine:  
  Version:          18.06.0-ce  
  API version:      1.38 (minimum version 1.12)  
  Go version:       go1.10.3  
  Git commit:       0ffa825  
  Built:            Wed Jul 18 19:09:05 2018  
  OS/Arch:          linux/amd64  
  Experimental:     false  
```

docker 설치 후 명령어 입력 시 아래와 같은 오류가 뜨는 경우가 있는데 이 경우 아래 명령어 실행을 통해 해결할 수 있다.  
`docker가 root 계정으로 설치 되었을때 root 계정이 아닌 계정으로 docker를 실행하고자 하면 제목과 같은 에러가 발생할 때가 있다. Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get http://%2Fvar%2Frun%2Fdocker.sock/v1.40/containers/json: dial unix /var/run/docker.sock: connect: permission denied`
```
$ sudo usermod -aG docker $USER
$ sudo reboot
```