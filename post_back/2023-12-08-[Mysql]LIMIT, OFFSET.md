## LIMIT, OFFSET

MySql에서 출력되는 행의 레코드 수를 지정하거나 페이징 처리를 하기 위해 `LIMIT`, `OFFSET` 명령어를 사용한다.

<br>

### LIMIT
---

`LIMIT` 는 처음부터 몇 개까지의 데이터를 가져올지 지정한다.

```sql
LIMIT 행 개수 [,행 개수]
```

<br>

```sql
SELECT * FROM 테이블명 LIMIT 20;

SELECT * FROM 테이블명 LIMIT 10, 30;
```

<br>

```
처음부터 20개 출력 (1 ~ 20)
11번째부터 30개 출력 (11 ~ 40)
```

https://inpa.tistory.com/entry/MYSQL-%F0%9F%93%9A-LIMIT-OFFSET

https://ssd0908.tistory.com/entry/MYSQL-LIMIT-OFFSET%EC%82%AC%EC%9A%A9%EB%B2%95-%EC%B4%9D%EC%A0%95%EB%A6%AC

https://zzang9ha.tistory.com/295

https://greensky0026.tistory.com/126