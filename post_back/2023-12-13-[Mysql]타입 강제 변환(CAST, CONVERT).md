## 타입 강제 변환(CAST, CONVERT)

MySQL에서는 비교나 검색 수행 시 데이터 타입이 다를 경우, 내부적으로 자동 변환하여 처리한다.
하지만 사용자가 강제로 타입을 변환할 수도 있다.

<br>

### 암시적 형변환
---

문자열도 합치면 숫자로 변환한다.

```sql
SELECT '200' + '200';

SELECT CONCAT(100,'200');

SELECT 3> '2MEGA';
```

<br>

```
400

100200

1
```

<br>

### CAST
---

`CAST` 함수는 인수로 전달받은 값을 명시된 타입으로 변환한다.

```sql
CAST(변환하고싶은 데이터 AS 데이터형식)
```

<br>

```sql
SELECT CAST(NOW() AS SIGNED);

SELECT CAST(20231213 AS DATE);
```

<br>

```
20231213111724

2023-12-13
```

<br>

### CONVERT
---

`CONVERT` 함수도 인수로 전달받은 값을 명시된 타입으로 변환한다.

```sql
CONVERT(변환하고싶은 데이터, 데이터형식)
```

<br>

```sql
SELECT CONVERT(NOW(), SIGNED);

SELECT CONVERT(20231213, DATE);
```

<br>

```
20231213112213

2023-12-13
```

<br>

### CAST / CONVERT 변환 가능 타입
---

`CAST` 와 `CONVERT` 에서 변환하고자 하는 타입으로 지정할 수 있는 데이터 타입은 다음과 같다.

```sql
BINARY      -- 이진 데이터 
CHAR        -- 문자열 타입 
DATA        -- 날짜 
DATETIME    -- 날짜, 시간 동시에 
DECIMAL 
JSON 
INTEGER     -- 부호 (음수,양수) 있는 정수형 
TIME        -- 시간 
UNSIGNED [INTEGER]
SIGNED [INTEGER]
```