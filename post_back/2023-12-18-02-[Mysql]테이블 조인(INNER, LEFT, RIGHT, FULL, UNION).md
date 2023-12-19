
## 테이블 조인

`JOIN` 은 데이터베이스 내의 여러 테이블에서 가져온 레코드를 조합하여 하나의 테이블이나 결과 집합으로 표현할 수 있게 도와준다.


<br>

### (INNER) JOIN
---

- 조인하는 테이블의 ON 절의 조건이 일치하는 결과만 출력한다.

```sql
SELECT A.USERID, NAME 
FROM USERTBL AS A
INNER JOIN BUYTBL AS B 
ON A.USERID=B.USERID 
WHERE A.USERID="YANG";
```

<br>

다음과 같이 `INNER JOIN` 을 생략해서 사용할 수 있다.

```sql
SELECT A.USERID, NAME 
FROM USERTBL A, BUYTBL B 
ON A.USERID=B.USERID 
WHERE A.USERID="YANG";
```

<br>

### LEFT OUTER JOIN
---

- 두 테이블을 조인할 때 왼쪽을 기준으로 왼쪽 테이블의 데이터는 모두 출력이 된다.
- 왼쪽 테이블을 기준으로 오른쪽 테이블을 조합해서 출력한다.

```sql
SELECT STUDENT.NAME, PROFESSOR.NAME 
FROM STUDENT LEFT OUTER JOIN PROFESSOR 
ON STUDENT.PID = PROFESSOR.ID 
WHERE GRADE = 1
```

<br>

위의 쿼리문의 경우 STUDENT 테이블의 데이터는 ON 조건을 만족하지 않는 데이터라도 전부 출력된다.

<br>

### RIGHT OUTER JOIN
---

- 두 테이블을 조인할 때 오른쪽을 기준으로 오른쪽 테이블의 데이터는 모두 출력이 된다.
- 오른쪽 테이블을 기준으로 왼쪽 테이블을 조합해서 출력한다.

```sql
SELECT STUDENT.NAME, PROFESSOR.NAME 
FROM STUDENT RIGHT OUTER JOIN PROFESSOR 
ON STUDENT.PID = PROFESSOR.ID 
WHERE GRADE = 1
```

<br>

위의 쿼리문의 경우 PROFESSOR 테이블의 데이터는 ON 조건을 만족하지 않는 데이터라도 전부 출력된다.

<br>

### UNION
---

- `UNION` 은 여러 개의 SELECT 문의 결과를 하나의 테이블이나 집합으로 표현할 때 사용한다.
- 이 때 각 SELECT 문의 컬럼 개수와 타입은 모두 같아야 하며, 컬럼 순서 또한 동일해야 한다.
- 중복제거(DISTINCT)가 자동 포함되어 수행된다.

```sql
SELECT S1.NAME, S1.GRADE FROM STUDENT S1
UNION
SELECT S2.NAME, S2.GRADE FROM STUDENT S2
```

<br>

### UNION ALL
---

- `UNION` 과 마찬가지로 여러 개의 SELECT 문의 결과를 하나의 테이블이나 집합으로 표현할 때 사용한다.
- 각 SELECT 문의 컬럼 개수와 타입은 모두 같아야 하며, 컬럼 순서 또한 동일해야 한다.
- `UNION` 과 달리 <strong>중복되는 행까지 모두 출력한다.</strong>
  
```sql
SELECT S1.NAME, S1.GRADE FROM STUDENT S1
UNION ALL
SELECT S2.NAME, S2.GRADE FROM STUDENT S2
```

<br>

### DISTINCT
---

- `DISTINCT` 는 중복되는 행을 제거하고 출력한다.
- 행의 수가 많을 수록 성능이 느리다.

```sql
SELECT DISTINCT P.ID, P.NAME, J.JOB_NAME 
FROM PERSON P, JOB J
ON P.NAME = J.PERSON_NAME;
```

<br>

JOIN 문에 사용할 테이블의 중복을 제거하거자 하는 경우 JOIN 수행 전에 미리 중복을 제거하는 것이 성능상 좋다.

```sql
SELECT P.ID, P.NAME
FROM PERSON P
LEFT JOIN (SELECT DISTINCT J.JOM_NAME, J.PERSON_NAME FROM JOB J) AS A
ON P.NAME = A.PERSON_NAME;
```