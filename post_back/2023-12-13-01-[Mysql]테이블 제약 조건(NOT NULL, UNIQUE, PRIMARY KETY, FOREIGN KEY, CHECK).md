## 테이블 제약 조건(NOT NULL, UNIQUE, PRIMARY KETY, FOREIGN KEY, CHECK)

`제약 조건` 이란 데이터의 무결성을 지키기 위해 제한하는 조건으로, 무결성이란 데이터에 결함이 없다는 것을 의미한다.

<br>

### NOT NULL
---

NULL 값을 허용하지 않고 중복값은 허용한다.

```sql
CREATE TABLE 테이블명 (
    컬럼명 컬럼타입 NOT NULL,
    ...
);
```

<br>

ALTER문을 통해 추가할 수도 있다.

```sql
ALTER TABLE 테이블명
ADD 컬럼명 컬럼타입 NOT NULL 
```

<br>

### UNIQUE
---

중복되지 않는 유일한 값이 조건이며 NULL 값이 허용되고 중복값은 허용되지 않는다.
UNIQUE 제약 조건을 설정하면 해당 컬럼은 보조 인덱스로 만들어진다.

```sql
CREATE TABLE 테이블명 (
    컬럼명 컬럼타입 UNIQUE,
    ...
);
```

<br>

```sql
CREATE TABLE 테이블명 (
    컬럼명 컬럼타입,
    ... ,
    [CONSTRAINT 제약조건명] UNIQUE (컬럼명)
);
```

<br>

ALTER문을 통해 추가할 수도 있다.

```sql
ALTER TABLE 테이블명
ADD 컬럼명 컬럼타입 UNIQUE 

ALTER TABLE 테이블명
ADD [CONSTRAINT 제약조건명] UNIQUE (컬럼명)
```

<br>

### PRIMARY KEY
---

데이터를 구분할 수 있는 식별자를 의미하며 중복되거나 NULL일 수 없다. 또한, 테이블 당 한 개만 지정이 가능하다.

```sql
CREATE TABLE 테이블명 (
  컬럼명 컬럼타입 PRIMARY KEY,
  ...
);
```

<br>

```sql
CREATE TABLE 테이블명 (
  컬럼명 컬럼타입,
  ...,
  [CONSTRAINT 제약조건명] PRIMARY KEY (컬럼명)
);
```

<br>

ALTER문을 통해 추가 / 삭제할 수도 있다.

```sql
ALTER TABLE 테이블명
ADD 컬럼명 컬럼타입 PRIMARY KEY
​
ALTER TABLE 테이블명
ADD [CONSTRAINT 제약조건명] PRIMARY KEY (컬럼명)
```

<br>

```sql
ALTER TABLE 테이블명
DROP PRIMARY KEY
```

<br>

### FOREIGN KEY
---

두 테이블 사이의 관계를 연결해주고, 그 결과 데이터의 무결성을 보장해주는 역할을 한다.
FOREIGN KEY 제약 조건을 설정할 때 참조되는 테이블의 필드는 반드시 UNIQUE나 PRIMARY KEY 제약 조건이 설정되어 있어야 한다.

```sql
CREATE TABLE 테이블명 (
  컬럼명 컬럼타입,
  ...,
  [CONSTRAINT 제약조건명] FOREIGN KEY (컬럼명) REFERENCES 부모 테이블명 (컬럼명)
);
```

<br>

ALTER문을 통해 추가 / 삭제할 수도 있다.

```sql
ALTER TABLE 추가할 테이블 명
ADD [CONSTRAINT 제약조건명] FOREIGN KEY (컬럼명) REFERENCES 부모 테이블명 (컬럼명) [ON DELETE CASCADE/ ON UPDATE CASCADE];
```

<br>

```sql
ALTER TABLE 테이블명
DROP FOREIGN KEY 제약조건명
```

<br>

#### ON DELETE / ON UPDATE

FOREIGN KEY 제약 조건에 의해 참조되는 테이블에서 데이터의 수정이나 삭제가 발생하면 참조하고 있는 테이블의 데이터도 같이 영향을 받는데, 이때 참조하고 있는 테이블의 동작은 다음 키워드를 사용하여 FOREIGN KEY 제약 조건에서 미리 설정할 수 있다.

<br>

- <strong>ON DELETE/UPDATE CASCADE</strong> : 참조되는 테이블에서 데이터를 삭제하거나 수정하면, 참조하는 테이블에서도 삭제와 수정이 같이 이루어진다.
- <strong>ON DELETE/UPDATE SET NULL</strong> : 참조되는 테이블에서 데이터를 삭제하거나 수정하면, 참조하는 테이블의 데이터는 NULL로 변경된다.
- <strong>ON DELETE/UPDATE NO ACTION</strong> : 참조되는 테이블에서 데이터를 삭제하거나 수정해도 참조하는 테이블의 데이터는 변경되지 않는다.
- <strong>ON DELETE/UPDATE SET DEFAULT</strong> : 참조되는 테이블에서 데이터를 삭제하거나 수정하면, 참조하는 테이블의 데이터는 컬럼의 기본값으로 설정된다.
- <strong>ON DELETE/UPDATE RESTRICT</strong> : 참조하는 테이블에 데이터가 있으면, 참조되는 테이블의 데이터를 삭제하거나 수정할 수 없다.

<br>

```sql
CREATE TABLE 테이블명2 (
  컬럼명 컬럼타입,
  ... ,
  FOREIGN KEY (컬럼명)
  REFERENCES 부모 테이블명 (컬럼명) ON UPDATE CASCADE ON DELETE RESTRICT
);
```

위의 예제에서 부모 테이블의 컬럼 값이 수정되면 테이블2의 컬럼도 같이 수정이 된다. 그리고 참조되는 부모 테이블의 해당 row는 삭제할 수 없다.

<br>

### DEFAULT
---

해당 컬럼의 기본값을 설정할 수 있게 해준다.

```sql
CREATE TABLE 테이블명 (
  컬럼명 컬럼타입 DEFAULT 기본값,
  ...
);
```

<br>

ALTER문을 통해 추가할 수도 있다.

```sql
ALTER TABLE 테이블명
ADD 컬럼명 컬럼타입 DEFAULT 기본값 

ALTER TABLE 테이블명
MODIFY COLUMN 컬럼명 컬럼타입 DEFAULT 기본값
```

<br>

### CHECK
---

해당 컬럼의 입력 가능한 값의 범위를 지정할 때 사용한다.

```sql
CREATE TABLE 테이블명 (
  컬럼명 컬럼타입 CHECK(조건), 
  ...
);
```

<br>

```sql
CREATE TABLE MEMBER (
  MEM_ID CHAR(8) NOT NULL PRIMARY KEY,
  MEM_NAME VARCHAR(10) NOT NULL,
  HEIGHT TINYINT UNSIGNED NULL CHECK(HEIGHT >= 100),
  PHONE1 CHAR(3) NULL
);
```

<br>

ALTER문을 통해 추가할 수도 있다.

```sql
ALTER TABLE 테이블명 
ADD CONSTRAINT CHECK (조건)
```

<br>

```sql
ALTER TABLE MEMBER
ADD CONSTRAINT
CHECK (PHONE1 IN ('02', '031', '032', '054', '055', '061'));
```