## 파티션(Partition)

`파티션(Partition)` 이란 대량의 데이터를 테이블에 저장할 때, 물리적으로 별도의 테이블로 분리해서 저장하는 기법을 말한다.
단, 내부적으로 분리되어 처리되기 때문에 사용자 입장에서는 하나의 테이블로 보이게 된다.

파티션이 필요한 경우는 다음과 같다.
- 하나의 테이블이 너무 커서 인덱스의 크기가 물리적 메모리를 초과할 경우
- 데이터 특성상 주기적인 삭제 작업이 필요한 경우

<br>

### 파티션 특징
---

파티션의 주요 특징은 다음과 같다.

- 파티션 테이블에는 외래 키를 설정할 수 없다.
- Primary Key, Unique Key가 존재하는 테이블에서는 반드시 파티션에서 사용되는 열도 PK, UK 중 한 가지로 사용해야 한다.
- 스토어드 프로시저, 스토어드 함수, 사용자 변수 등을 파티션 식에 사용할 수 없다.
- 임시 테이블은 파티션을 사용할 수 없다.
- MAXVALUE 파티션이 있다면 새로운 파티션을 추가 할 수 없습니다.(파티션 분리로 진행)
- MySQL은 파티션 개수는 최대 1,024개까지 지원한다.


<br>

### 파티션 종류
---

MySql에서 파티션은 4가지 종류가 있다.

- <strong>Range 파티션</strong> 
- <strong>List 파티션</strong> 
- <strong>Hash 파티션</strong> 
- <strong>Key 파티션</strong> 

<br>

#### Range 파티션

파티션 키의 연속된 범위로 파티션을 정의하는 방식이며 범위(날짜 등)를 기반으로 파티션을 나눈다. (가장 흔히 사용)

<br>

##### 파티션 생성

```sql
CREATE TABLE TB_RANGE_TABLE (
  USERID CHAR(8) NOT NULL,
  NAME VARCHAR(10) NOT NULL,
  BIRTHYEAR INT NOT NULL, -- 생일날짜가 파티션 범위 대로 정렬된다.
  ADDR CHAR(2) NOT NULL
)

PARTITION BY RANGE(BIRTHYEAR) ( -- 출생년도를 기준으로 분할한다.
  PARTITION part1 VALUES LESS THAN (1970), -- 1970년 이하
  PARTITION part2 VALUES LESS THAN (1980), -- 1971 ~ 1980
  PARTITION part999 VALUES LESS THAN MAXVALUE -- 1980 ~
);
```

<br>

##### 파티션 확인

```sql
SELECT TABLE_SCHEMA, TABLE_NAME, PARTITION_NAME, PARTITION_ORDINAL_POSITION, TABLE_ROWS
FROM INFORMATION_SCHEMA.PARTITIONS
WHERE TABLE_NAME = 'TB_RANGE_TABLE';
```

<br>

##### 파티션 추가

MAXVALUE 파티션이 있다면 새로운 파티션을 추가할 수 없고 분리해야 한다.

```sql
ALTER TABLE TB_RANGE_TABLE ADD PARTITION
(PARTITION part3 VALUES LESS THAN(1990)  -- 1981 ~ 1990
);  

OPTIMIZE TABLE TB_RANGE_TABLE; -- 파티션 작업된 테이블 적용
```

<br>

##### 파티션 분리

```sql
ALTER TABLE TB_RANGE_TABLE
REORGANIZE PARTITION PART3 INTO (
  PARTITION PART3 VALUES LESS THAN (1995), -- 파티션3을 더 쪼갰다.
  PARTITION PART999 VALUES LESS THAN MAXVALUE
);

OPTIMIZE TABLE TB_RANGE_TABLE; -- 파티션 작업된 테이블 적용
```

<br>

##### 파티션 병합

```sql
ALTER TABLE TB_RANGE_TABLE
REORGANIZE PARTITION part2,part3 INTO (
PARTITION part3 VALUES LESS THAN (1995) 
);

OPTIMIZE TABLE TB_RANGE_TABLE; -- 파티션 작업된 테이블 적용
```

<br>

##### 파티션 삭제

```sql
ALTER TABLE TB_RANGE_TABLE DROP PARTITION part3;
```

<br>

#### List 파티션

파티션 키 값 하나하나 리스트로 나열해야하며 코드나 카테고리 등 특정 값을 기반으로 파티션을 나눈다.

<br>

##### 파티션 생성

```sql
CREATE TABLE TB_LIST_TABLE (
ID INT NOT NULL AUTO_INCREMENT ,
NAME VARCHAR(10),
DEPT_NO INT NOT NULL,
PRIMARY KEY(ID,DEPT_NO)
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4
PARTITION BY LIST(DEPT_NO) (
PARTITION P_ACCOUNTING VALUES IN(1),
PARTITION P_RESEARCH VALUES IN(2),
PARTITION P_SALES VALUES IN(3),
PARTITION P_OPERATIONS VALUES IN(4,NULL) );
```

<br>

##### 파티션 추가

```sql
ALTER TABLE TB_LIST_TABLE 
ADD PARTITION (PARTITION P_MARKETING VALUES IN(5));

OPTIMIZE TABLE ALTER TABLE TB_LIST_TABLE; -- 파티션 작업된 테이블 적용
```

<br>

##### 파티션 삭제

```sql
ALTER TABLE TB_LIST_TABLE DROP PARTITION P_MARKETING;

OPTIMIZE TABLE ALTER TABLE TB_LIST_TABLE; -- 파티션 작업된 테이블 적용
```

<br>

#### Hash 파티션

해시 함수에 의해 레코드가 저장될 파티션이 결정되는 방식이며 설정한 HASH 함수를 기반으로 파티션을 나눈다.

<br>

##### 파티션 생성

```sql
CREATE TABLE TB_HASH_TABLE (
ID INT NOT NULL,
NAME VARCHAR(10),
DEPT_NO INT NOT NULL
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4
PARTITION BY HASH(ID)
PARTITIONS 4 (
PARTITION P1,
PARTITION P2,
PARTITION P3,
PARTITION P4
);
```

<br>

##### 파티션 추가

```sql
ALTER TABLE TB_HASH_TABLE ADD PARTITION(PARTITION P5);

OPTIMIZE TABLE ALTER TABLE TB_HASH_TABLE; -- 파티션 작업된 테이블 적용
```

<br>

##### 파티션 삭제

```sql
ALTER TABLE TB_HASH_TABLE COALESCE PARTITION 1; -- 1개 축소

OPTIMIZE TABLE ALTER TABLE TB_HASH_TABLE; -- 파티션 작업된 테이블 적용
```

<br>

#### Key 파티션

MD5() 함수를 이용한 HASH 값을 기반으로 파티션을 나눈다.

<br>

##### 파티션 생성 

```sql
CREATE TABLE `TB_KEY_TABLE` (
ID INT NOT NULL,
NAME VARCHAR(10),
DEPT_NO INT NOT NULL,
PRIMARY KEY (ID,NAME)
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4
PARTITION BY KEY(ID)
PARTITIONS 4;
```