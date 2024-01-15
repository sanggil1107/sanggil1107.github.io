## TCP(Transmission Control Protocol)

`TCP` 란 전송 계층의 대표적인 연결지향 프로토콜로 신뢰성 있는 애플리케이션 간의 데이터 전송을 하기 위한 프로토콜이다. 하위 계층에서의 (network, datalink 계층) 패킷 손실, 중복 오류 등 모든 전송 문제를 검출하고 해결해주며, IP의  한계인 비연결성과 비신뢰성도 해결해준다.

<br>

### TCP 구조
---

데이터 전달 시에 데이터 앞에 `TCT 헤더` 가 추가되어 전달되며, 데이터 본체와는 별도로 추가되는 정보이며 아래와 같다.

[TCP 헤더 이미지]


- Source Port : 발신지 포트, 패킷을 송신하는 시스템의 포트번호
- Destination Port : 목적지 포트, 패킷을 수신할 시스템의 포트번호
- Sequence Number : 순차 번호, 각 세그먼트의 첫 번째 바이트에 부여되는 고유 번호
- Acknowledge Number : 응답 번호, 수신한 세그먼트의 확인 응답을 위한 필드
- Header Length : 헤더 길이, TCP 헤더 길이를 나타내는 필드
- Reserved : 미래를 위해서 만들어 놓은 예약 필드
- Flags : 세그먼트의 용도와 내용을 결정하는 플래그로 URN(긴급플래그), ACK(응답플래그), PSH(Puch플래그), RST(Reset플래그), SYN(연결요청플래그), FIN(Finish플래그)로 구성
- Window Size : 수신하고자 하는 윈도우의 크기
- Checksum : 오류 검출을 위해 사용되는 필드
- Urgent Point : 긴급 데이터가 시작되는 위치
- Options : TCP 기능을 확장할 때 사용

<br>

### TCP 특징
---

TCP는 다음과 같은 특징을 가지고 있다.

- 연결 지향 : TCP 3 way handshake
- 데이터 전달 보증 : 패킷이 누락되었는지 확인
- 순서 보장

<br>

### TCP 제어 방식
---

- <strong>흐름 제어</strong>
송신측과 수신측 사이의 데이터 처리 속도 차이를 해결
- <strong>오류 제어</strong>
패킷 정보가 손실되거나 분실되는 것을 해결하기 위해 오류나 분실된 패킷을 감지하고 재전송
- <strong>혼잡 제어</strong>
네트워크의 혼잡을 피하기 위해 보내는 데이터의 전송 속도를 제어