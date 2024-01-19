## NULL 처리(IFNULL)

MySql에서 NULL 처리하는 경우 `IFNULL` 함수를 사용한다.

<br>

### IFNULL
---

해당 값이 NULL일 때 다른 값을 출력할 수 있도록 하는 함수이다.

```sql
IFNULL(컬럼명, NULL일 경우 대체 값)
```

<br>

```sql
SELECT IFNULL(AGE, -1) FROM 테이블명;
```

<br>

```
AGE 컬럼 값이 NULL일 경우 -1 반환
```