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

<br>

### LIMIT + OFFSET
---

`OFFSET` 은 `LIMIT` 에서 지정한 시작점부터 몇 개 이후까지 데이터를 보여주는 지정한다. 
`OFFSET` 은 단독으로 사용이 불가능하다.

```sql
LIMIT 행 개수 [,행 개수] OFFSET 시작 행
```

<br>

```sql
SELECT * FROM 테이블명 LIMIT 20 OFFSET 5;
```

<br>

```
6번째 행부터 20개 출력 (6 ~ 25)
```

<br>

### 페이징 처리
---
`LIMIT` 과 `OFFSET` 을 활용하여 웹 사이트 같은 곳에서 페이징을 구현할 수 있다.

```sql
SELECT *
FROM board
WHERE status = 'Y'
ORDER BY seq 
LIMIT 20 OFFSET [변수]
```

<br>

위에 쿼리문에서처럼 `OFFSET` 값 부분을 0부터 변수로 지정하여 페이지를 이동할 때마다 해당 페이지의 `OFFSET` 값을 계산해주면 된다.