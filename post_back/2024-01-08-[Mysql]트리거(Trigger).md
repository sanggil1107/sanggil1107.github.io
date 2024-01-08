
## 트리거(Trigger)

MySql에서 트리거란 테이블에서 어떤 이벤트가 발생했을 때 자동으로 실행되는 것을 의미한다. 즉, 어떤 테이블에 특정 이벤트(insert, update, delete)가 발생했을 때, 실행시키고자 하는 쿼리 작업들을 자동으로 수행할 수 잇게 설정하는 것이다.

<br>

### 트리거 종류
---

트리거의 종류로는 `행 트리거`와 `문장 트리거` 가 있다.

<br>

#### 행 트리거

테이블 안의 영향을 받은 행 각각에 대해 실행된다.
변경 전 또는 변경 후의 행은 OLD, NEW라는 가상 줄 변수를 사용하여 읽을 수 있다.

<br>

#### 문장 트리거

INSERT, UPDATE, DELETE 문에 대해 한 번만 실행된다.
삽입, 갱신 또는 삭제되는 행 수에 상관없이 각 트랜잭션에 대해 트리거가 한 번 실행된다.

<br>

### 트리거 사용법
---

#### 트리거 생성

```sql
DELIMITER $$

CREATE TRIGGER update_item
AFTER UPDATE  -- {BEFORE | AFTER} {INSERT | UPDATE| DELETE } 중 언제 어떤 작업을 할지 정한다
ON sale_table -- 트리거를 부착할 테이블
FOR EACH ROW -- 아래 나올 조건에 해당하는 모든 row에 적용한다는 뜻

BEGIN
  -- 트리거시 실행되는 코드
  IF NEW.discount_rate != OLD.discount_rate THEN -- update 트리거는 old와 new 값이 존재한다.
    UPDATE item_table SET discount_rate = NEW.discount_rate WHERE discount_rate = OLD.discount_rate;
  END IF;
END $$

DELIMITER ;
```

<br>

BEGIN ~ END 사이에 조건문과 실행문을 작성한다.
IF 조건을 만족하는 row는 UPDATE 쿼리문을 실행하게 된다.

<br>

#### 트리거 실행

sale_table에 update 발생 시 실행된다.

```sql
UPDATE sale_table
SET ...
WHERE ...;
```

<br>

#### 트리거 확인

```sql
SHOW TRIGGERS;
```

<br>

#### 트리거 삭제

```sql
DELETE triggers;
```