## 소수점 반올림, 버림(ROUND, TRUNCATE)

MySql에서 소수점을 다루는 경우 `ROUND`, `TRUNCATE` 함수를 사용한다.

<br>

### ROUND
---

소수점을 반올림한다. 자리수를 지정하지 않으면 정수만 출력된다.

```sql
ROUND(숫자, [자리수])
```

<br>

```sql
SELECT ROUND(1234.567);
SELECT ROUND(1234.567, 1);
SELECT ROUND(1234.561, 2);
```

<br>

```
1235
1234.6
1234.56
```


<br>

### TRUNCATE
---

소수점을 버린다. `ROUND` 함수와 달리 자리수를 필수로 지정해야한다.

```sql
TRUNCATE(숫자, 자리수)
```

<br>

```sql
SELECT TRUNCATE(1234.567, 1);
SELECT TRUNCATE(1234.567, 2);
```

<br>

```
1234.5
1234.56
```