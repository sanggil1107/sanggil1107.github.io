## 3-Way Handshake

`3-Way handshake` 란 TCP/IP 프로토콜을 이용해서 통신을 하는 응용프로그램이 데이터를 전송하기 전에 먼저 정확한 전송을 보장하기 위해 상대방 컴퓨터와 사전에 세션을 수립하는 과정을 말한다.

<br>

### 작동 방식
---

[이미지]

Client는 Server와 연결하기 위해 3-way handshake를 통해 연결 요청을 하게 된다. 이는 양 쪽 모두 데이터를 전송할 준비가 되어있다는 것을 보장하고, 실제로 데이터 전달이 시작하기 전에 다른 한쪽이 준비되었다는 것을 알 수 있도록 한다.

<strong>[State 정보]</strong>
- CLOSED: 포트가 닫힌 상태
- LISTEN: 포트가 열린 상태로 연결 요청 대기 중
- SYN_RECV: SYNC 요청을 받고 상대방의 응답을 기다리는 중
- ESTABLISHED: 포트 연결 상태
- TIME-WAIT: Server로부터 FIN을 수신하더라도 일정시간(default: 240초) 동안 세션을 남겨놓고 잉여 패킷을 기다리는 과정


<strong>[Flag 정보]</strong>

- <strong>SYN(Synchronize Sequence Number)</strong>
연결 설정. Sequence Number를 랜덤으로 설정하여 세션을 연결하는 데 사용하며, 초기에 Sequence Number를 전송한다.
따라서, Connection을 생성할때 사용하는 flag이다.
- <strong>ACK(Acknowledgement)</strong>
응답 확인. 패킷을 받았다는 것을 의미하는 flag이다.
Acknowledgement Number 필드가 유효한지를 나타낸다.
양단 프로세스가 쉬지 않고 데이터를 전송한다고 가정하면 최초 연결 설정 과정에서 전송되는 첫 번째 세그먼트를 제외한 모든 세그먼트의 ACK 비트는 1로 지정된다고 생각할 수 있다.


<br>

#### Step 1 (SYN)

Client는 Server와 커넥션을 연결하기 위해 SYN을 보낸다. [Client -> SYN -> Server]

- 송신자가 최초로 데이터를 전송할 때 Sequence Number를 임의의 랜덤 숫자로 지정하고, SYN 플래그 비트를 1로 설정한 세그먼트를 전송한다.
- PORT 상태
  - Client : CLOSED -> SYN_SENT
  - Server : LISTEN

#### step 2 (SYN + ACK)

Server가 SYN을 받고, Clenet로 받았다는 신호인 ACK와 SYN 패킷을 보낸다. [Server -> SYN + ACK -> Client]

- 접속 요청을 받은 Server가 요청을 수락했으며, 접속 요청 프로세스인 Client도 포트를 열어달라는 메세지를 전송 
- ACK Number필드를 Sequence Number + 1 로 지정하고 SYN과 ACK 플래그 비트를 1로 설정한 새그먼트 전송
- PORT 상태
  - Client : CLOSED
  - Server : SYN_RCV

#### Step 3 (ACK) 

클라이언트는 서버의 응답은 ACK와 SYN 패킷을 받고, ACK를 서버로 보낸다. [Client -> ACK -> Server]

- 마지막으로 접속 요청 프로세스 P가 수락 확인을 보내 연결을 맺음 (ACK)
- 이때, 전송할 데이터가 있으면 이 단계에서 데이터를 전송할 수 있다.
- PORT 상태
  - Client : ESTABLISED
  - Server : SYN_RCV -> ACK -> ESTABLISED
