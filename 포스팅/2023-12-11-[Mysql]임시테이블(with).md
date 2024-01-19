## 임시 테이블(with)

SQL을 통해 빅데이터를 처리하면서 새로운 결과를 저장하고 관리할 때마다 테이블에 저장할 수 없으며 이 경우 `임시 테이블`을 사용하여 처리한다.

<br>

### 임시테이블 생성
---

```sql
WITH 임시테이블명 as
(
    SELECT 컬럼
    FROM 테이블명
    WHERE 조건
)
SELECT 컬럼
FROM 임시테이블명
WHERE 조건
```

<br>

```sql
WITH ADULT AS 
(
    SELECT gender
         , name
         , age
      FROM MEMBER
     WHERE age > 19
)
SELECT gender
     , name
     , age
FROM ADULT
```

위의 쿼리문을 통해 실제 테이블을 만들지 않고 ADULT라는 임시 테이블을 만들어 저장했다.

with 절을 사용한 임시 테이블의 장점은 장시간 걸리는 쿼리의 결과를 저장해놓고 저장해놓은 데이터를 엑세스하기 때문에 성능이 좋다는 것이다.

<br>

### 옵션
---

임시 테이블의 성능을 높이기 위한 옵션은 다음과 같다.

<br>

#### materialize

기본 with 절 사용 시 자동으로 적용되며 temp(임시 테이블)를 사용한다.

<br>

#### inline

materialize 와 달리 temp 테이블을 생성하지 않고 inline view로 수행한다.

```sql
WITH EEE AS (
  SELECT /*+INLINE */ JOB, SUM(SAL) AS TOTAL 
  FROM EMP 
  GROUP BY JOB
)
SELECT JOB, TOTAL 
FROM EEE 
WHERE TOTAL > (SELECT AVG(TOTAL) FROM EEE);
```
