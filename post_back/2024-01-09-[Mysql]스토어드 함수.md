
## 스토어드 함수

스토어드 함수란 필요에 따라 직접 만들어서 사용하는 함수를 의미한다.

<br>

### 스토어드 함수 vs 스토어드 프로시저
---

(스토어드 프로시저 링크)

스토어드 함수와 스토어드 프로시저는 비슷해보이지만 다음과 같은 차이점이 있다.

- 프로시저의 파라미터 `IN`, `OUT` 을 스토어드 함수에서는 사용할 수 없다.
- 스토어드 함수 파라미터는 모두 입력 파라미터로 사용된다.
- 스토어드 함수는 return문으로 반환 할 값의 데이터 타입을 지정하고, 본문 안에서 return문으로 하나의 값을 반환해야 한다.
- 프로시저는 `call` 로 호출되지만, 스토어드 함수는 `select` 로 호출된다.
- 프로시저 안에서는 select 문을 사용할 수 있지만, 스토어드 함수 안에서는 집합 결과를 반환하는 select 문을 사용할 수 없다.

<br>

### 스토어드 함수 사용법
---

#### 스토어드 함수 생성

```sql
DROP FUNCTION IF EXISTS getAge;

DELIMITER $$
	CREATE FUNCTION getAgeFunc(birthYear INT) -- 입력 파라미터 지정
	RETURNS INT -- 반환 타입 지정
    
BEGIN
	DECLARE age INT
	SET age = YEAR(CURDATE()) - bYear;

	RETURN age; -- 값 반환
END $$
DELIMITER ;
```

<br>

#### 스토어드 함수 실행

```sql
SELECT getAgeFunc(1979);
​
SELECT userName, getAgeFunc(birthYear) AS '나이' FROM userTable;
```

<br>

#### 스토어드 함수 조회 / 삭제

```sql
SHOW CREATE FUNCTION 스토어드 함수명;
​
DROP FUNCTION 스토어드 함수명;
```
