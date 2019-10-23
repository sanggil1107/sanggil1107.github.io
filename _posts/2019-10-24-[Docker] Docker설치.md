---
layout: post
title: [Docker] Docker 설치(feat. ubuntu)
category: [Docker]
---
<br>
Docker 설치해보기
<!-- more -->
<hr>

# Docker 설치

```
$ sudo apt-get update
```
```
$ sudo apt-get install -y apt-transport-https ca-certificates curl 
```

```
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

```
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

```
$ sudo apt-get install docker-ce=18.06.0~ce~3-0~ubuntu
```

```
$sudo usermod -aG docker $USER
```

```
$ docker version
```
> Client:
>  Version:           18.06.0-ce
>  API version:       1.38
>  Go version:        go1.10.3
>  Git commit:        0ffa825
>  Built:             Wed Jul 18 19:11:02 2018
>  OS/Arch:           linux/amd64
>  Experimental:      false
> 
> Server:
>  Engine:
>   Version:          18.06.0-ce
>   API version:      1.38 (minimum version 1.12)
>   Go version:       go1.10.3
>   Git commit:       0ffa825
>   Built:            Wed Jul 18 19:09:05 2018
>   OS/Arch:          linux/amd64
>   Experimental:     false
