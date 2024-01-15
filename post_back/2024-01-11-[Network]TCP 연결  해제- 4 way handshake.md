## 4-Way Handshake

`4-Way handshake` 란 상대방 컴퓨터와의 세션을 종료하는 과정을 말한다.(연결 해제)

<br>

### 작동 방식
---

[이미지]

Client와 Server는 연결을 해제하기 위해 4-way handshake를 통해 연결 해제를 하게 된다. 

<strong>[State 정보]</strong>
- CLOSED: 포트가 닫힌 상태
- LISTEN: 포트가 열린 상태로 연결 요청 대기 중
- SYN_RECV: SYNC 요청을 받고 상대방의 응답을 기다리는 중
- ESTABLISHED: 포트 연결 상태
- TIME-WAIT: Server로부터 FIN을 수신하더라도 일정시간(default: 240초) 동안 세션을 남겨놓고 잉여 패킷을 기다리는 과정


<strong>[Flag 정보]</strong>

- <strong>FIN(Finish)</strong>
연결 해제. 세션 연결을 종료시킬 때 사용되며, 더 이상 전송할 데이터가 없음을 의미한다.
- <strong>ACK(Acknowledgement)</strong>
응답 확인. 패킷을 받았다는 것을 의미하는 flag이다.
Acknowledgement Number 필드가 유효한지를 나타낸다.
양단 프로세스가 쉬지 않고 데이터를 전송한다고 가정하면 최초 연결 설정 과정에서 전송되는 첫 번째 세그먼트를 제외한 모든 세그먼트의 ACK 비트는 1로 지정된다고 생각할 수 있다.


<br>

#### Step 1 (FIN(+ACK))

Client는 Server와 커넥션을 해제하기 위해 FIN을 보낸다. [Client -> FIN(+ACK) -> Server]

- 서버와 클라이언트가 연결된 상태에서 클라이언트가 close()를 호출하여 접속을 끊는다
- 클라이언트는 서버에게 연결을 종료한다는 FIN 플래그를 보낸다.
  - 이때 FIN 패킷에는 실질적으로 ACK도 포함되어있다.
- PORT 상태
  - Client : FIN_WAIT_1

#### step 2 (ACK)

Server는 FIN을 받고, 확인했다는 ACK를 Client에게 보내고 자신의 통신이 끝날때까지 기다린다. [Server -> ACK -> Client]

- Server는 ACK Number 필드를 (Sequence Number + 1)로 지정하고, ACK 플래그 비트를 1로 설정한 세그먼트를 전송한다.
- 서버는 클라이언트에게 응답을 보내고 CLOSE_WAIT 상태에 들어가며 아직 남은 데이터가 있다면 마저 전송을 마친 후에 close()를 호출
- Client에서는 Server로부터 ACK를 받은 후에 Server가 남은 데이터 처리를 끝내고 FIN 패킷을 보낼 때까지 기다린다.
- PORT 상태
  - Client : FIN_WAIT_1 -> FIN_WAIT_2
  - Server : CLOSE_WAIT

#### Step 3 (FIN) 

데이터를 모두 보냈다면, Server는 연결이 종료에 합의 한다는 의미로 FIN 패킷을 Client에게 보낸다. [Server -> FIN -> Client]

- PORT 상태
  - Server : LAST_ACK 

#### Step 4 (ACK)

Client는 연결 해제 준비가 되었다는 정상응답인 ACK를 Server에게 보낸다. [Client -> ACK -> Server]

- 클라이언트는 FIN을 받고, 확인했다는 ACK를 서버에게 보낸다.
- 아직 서버로부터 받지 못한 데이터가 있을 수 있으므로 TIME_WAIT을 통해 기다린다. (실질적인 종료과정 CLOSED에 들어가게 된다)
  - 이때 TIME_WAIT 상태는 의도치 않은 에러로 인해 연결이 데드락으로 빠지는 것을 방지
  - 만약 에러로 인해 종료가 지연되다가 타임이 초과되면 CLOSED로 들어간다.
- Server는 ACK를 받은 이후 소켓을 닫는다.
- TIME_WAIT 시간이 끝나면 Client도 닫는다. (Closed)
- PORT 상태
  - Client : FIN_WAIT_2 -> TIME_WAIT -> CLOSED
  - Server : LAST_ACK -> CLOSED