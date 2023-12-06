## 대문자 / 소문자 변경(UPPER, LOWER)

MySql에서 대문자 / 소문자를 변경하는 경우 `UPPER`, `LOWER` 함수를 사용한다.

<br>

### UPPER
---

대문자로 변경한다.

```sql
UPPER(문자열)
```

<br>

```sql
SELECT UPPER('Sanggil');
```

<br>

```
SANGGIL
```

<br>

### LOWER
---

소문자로 변경한다.

```sql
LOWER(문자열)
```

<br>

```sql
SELECT LOWER('SANGGIL');
```

<br>

```
sanggil
```