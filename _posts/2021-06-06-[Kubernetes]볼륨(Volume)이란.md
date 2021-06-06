---
layout: post
title: "[Kubernetes] 볼륨(Volume)이란"
category: [Kubernetes]

---
<br>
 
`볼륨(Volume)`에 대해 알아보자
<!-- more -->

<hr>  


# 컨테이너 환경에서의 볼륨

pod의 각 컨테이너에는 고유의 분리된 파일시스템이 있다. 
따라서 pod 또는 각 컨테이너가 다시 시작된다면 이전 컨테이너가 파일시스템에 기록한 내용은 유지되지 않고 삭제된다.
이를 유지하기 위해서는 컨테이너가 외부 디스크 스토리지에 액세스하고 스토리지를 공유해야 한다.

## 볼륨(volume) 소개

볼륨은 pod의 컴포넌트이다. 컨테이너와 마찬가지로 pod의 `spec`에 의해 결정된다.
볼륨은 독립적인 kubernetes 오브젝트가 아니며 스스로 생성하거나 삭제할 수 없다.
pod의 모든 컨테이너에서 볼륨을 사용할 수 있지만 볼륨에 액세스 해야하는 각 컨테이너에 볼륨을 마운트해야한다.

## 사용가능한 볼륨 유형 소개

emptyDir : 일시적인 데이터를 저장하는데 사용되는, 비어 있는 단순한 디렉토리
hostPath : 워커 노드의 파일 시스템에서 pod로 디렉토리를 마운트하는데 사용
gitRepo : 깃 스토리지의 내용을 체크아웃해 초기화된 볼륨
nfs: pod에 마운트된 NFS 공유
cinder,cephfs, iscsi, flocker, gulsterfs, quobyte, rbd, flexvolume, vsphereVolume, photonPersistentDisk, scaleIO: 다른 유형의 네트워크 스토리지를 마운트 하는 데 사용된다.
configMap, secret, downwardAPI : 특정 쿠버네티스 리소스 및 클러스터 정보를 포드에 노출하는 데 사용되는 특수한 유형의 볼륨이다.
persistentVolumeClaim : 사전 또는 동적으로 프로비저닝 영구 스토리지를 사용하는 방법


## volume을 사용한 컨테이너 사이의 데이터 공유

### emptyDir
가장 간단한 볼륨 유형, 포드가 삭제되면 볼륨의 내용이 손실된다.
동일한 포드에서 실행 중인 컨테이너 간에 파일공유에 유용하다.
emptyDir 볼륨은 빈 디렉토리로 시작한다.

- 공유 스토리지가 없는 동일한 포드의 세 개의 컨테이너
!이미지(emptyDir_1)!
    - webserver : /var/htdocs 디렉토리에서 html 페이지를 서비스하지는 웹서버를 실행하고 액세스 로그를 /var/logs에 저장한다.
    - contentAgent : HTML 파일을 생성하고 /var/html에 저장하는 에이전트를 실행한다.
    - LogRotator : /var/log 디렉토리에서 찾은 로그를 처리한다.
==> 각 컨테이너는 파일시스템을 공유하지 않고 서로의 시스템에 엑세스 할수 없기 때문에 세개의 컨테이너로 포드를 만드는 의미가 없음.

- 마운트된 두 개의 volume을 공유하는 컨테이너
!이미지(emptyDir_2)!
    - publicHtml : 해당 Volume은 WebServer가 파일을 제공하는 디렉터리 이므로 /var/htdocs에 있는WebServer 컨테이너에 마운트되고, ContentAgent가 생성한 파일을 쓰기위해 ContentAgent 컨테이너에 /var/html에 마운트 된다.
    - logVol: WebServer 및 LogRotator 컨테이너의 /var/logs에 마운트된다.

### gitRepo
기본적인 구조는 emptyDir과 같지만 volume 최초 생성 시 'git repository'를 복재하여 채워진다. 단 pod에 gitRepo볼륨이 생성된 후에는 참조하는 git repository와 동기화 되지 않는다.
!이미지(gitpath)!

### 워커 노드 파일 시스템에 액세스 하기
대부분의 pod는 호스트 노드를 인식하지 못하므로 노드의 파일 시스템에 액세스 하지 않는다.
단, 특정 시스템 수준 pod는 노드의 파일을 읽거나 노드의 파일 시스템을 통해 노드의 장치에 액세스 해야 한다.

#### hostPath 볼륨
!이미지(hostpath)!
hostPath 볼륨은 노드의 파일 시스템에 있는 특정 파일 또는 디렉토리를 가리킨다.
이전 emptyDir과 달리 hostPath 볼륨의 내용은 pod가 해체될 때 삭제되지 않는다.
단, pod가 재성성될 때 다른 노드에서 실행될 경우 이전의 pod에서 저장한 데이터는 실행되지 않는다.
단일 노드 클러스터에서는 영구 스토리지를 사용하는데 사용할 수 있지만, 다중 노드 클러스터에서는 적절하지 못하다.

### 영구 스토리지 사용
모든 클러스터 노드에서 액세스할 수 있어야 함으로 NAS(Network-Attached Storage) 유형에 저장해야 한다
영구 스토리지를 사용하는 방법으로는 다양한 방법이 있다.
 - 포드 볼륨에서 GCE 영구 디스크 사용
 - 기본 영구 스토리지에서 다른 볼륨의 유형 사용(AWS EC2)
 - NFS 볼륨 사용
 단점 : 이런 유형의 경우 포드 개발자가 클러스터에서 사용할 수 있는 실제 네트워크 스토리지 인프라에 대한 지식을 갖추고 있어야한다.

### 기본 스토리지 기술에서 pod 분리
#### PersistentVolume와 PersistentVolumeClaim
애플리케이션이 인프라 세부 사항을 처리하지 않고도 k8s 클러스터의 스토리지를 요청할 수 있도록 하기 위해 PV(PersistentVolume) 및 PVC(PersistentVolumeClaim) 리소스가 도입
!이미지(pvc)!
#1  클러스터 관리자는 네트워크 스토리지 유형을 설정한다
#2  클러스터 관리자는 PV리소르를 생성해 k8s API 서버에 등록한다 / PV를 생성할 때 지원하는 액세스 모드와 크기를 지정한다
#3  사용자가 PVC를 생성한다
#4  k8s는 적절한 크기 및 액세스 모드의 PV를 찾고 PVC를 PV에 바인딩한다
#5  사용자가 PVC를 참조하는 볼륨으로 포드를 생성한다