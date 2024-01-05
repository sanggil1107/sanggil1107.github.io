
## 트랜잭션(Transaction)

MySql에서 `트랜잭션(Trnasaction)` 이란 데이터베이스의 상태를 바꾸는 일종의 작업 단위이다.


<br>

### 트랜잭션특징
---

트랜잭션의 특징은 크게 4가지로 구분된다.

- 원자성(Atomicity)
트랜잭션이 데이터베이스에 모두 반영되던가, 아니면 전혀 반영되지 않아야 한다.

- 일관성(Consistency)
트랜잭션의 작업 처리 결과가 항상 일관성이 있어야 한다.
트랜잭션이 진행되는 동안에 데이터베이스가 변경 되더라도 업데이트된 데이터베이스로 트랜잭션이 진행되는것이 아니라, 처음에 트랜잭션을 진행 하기 위해 참조한 데이터베이스로 진행된다.

- 독립성(Isolation)
둘 이상의 트랜잭션이 동시에 실행되고 있는 경우, 어떤 하나의 트랜잭션이라도 다른 트랜잭션의 연산에 끼어들 수 없다.

- 영구성(Durability)
트랜잭션이 성공적으로 완료되었을 경우, 결과는 영구적으로 반영되어야 한다.

<br>

### 트랜잭션 상태
---

그림

트랜잭션의 각 개별 상태에 대한 설명은 다음과 같다.

- 1. 활성(Active)
트랜잭션이 정상적으로 실행중인 상태를 의미

- 2-1. 부분 완료(Partially Committed)
트랜잭션의 마지막까지 실행되었지만, Commit 연산이 실행되기 전 상태

- 2-2. 완료(Committed)
트랜잭션이 성공적으로 종료되어 Commit 연산을 실행한 후의 상태

- 3-1. 실패(Failed)
트랜잭션 실행에 오류가 발생하여 중단된 상태

- 3-2. 철회(Aborted)
트랜잭션이 비정상적으로 종료되어 Rollback(수행 이전의 상태로 되돌림) 연산을 수행한 상태

<br>

### 트랜잭션 문법
---

기본적으로 따로 명시하지 않아도 명령어들은 자동으로 Commit 처리 된다.
아래와 같이 수동으로 명시할 수 있다.

```sql
START TRANSACTION  -- 트랜잭션 시작

SELECT * FROM USER;
INSERT INTO USER VALUES(1, '상길');
SELECT * FROM USER;

COMMIT  -- 트랜잭션 적용

SELECT * FROM USER;  -- 적용된 결과 조회
```

<br>

다음은 롤백의 경우이다.

```sql
START TRANSACTION  -- 트랜잭션 시작

INSERT INTO USER VALUES(1, '상길');
SELECT * FROM USER;

ROLLBACK  -- 트랜잭션을 취소하고 INSERT 전 상태로 롤백

SELECT * FROM USER;  -- 조회
```

<br>

### 예외
---

모든 명령어에 대해 트랜잭션 롤백이 적용되지 않으며 DDL문(CREATE, DROP, RENAME, TRUNCATE)은 롤백 대상이 아니다.