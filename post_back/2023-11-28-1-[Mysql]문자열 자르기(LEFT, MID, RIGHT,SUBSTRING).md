## 문자열 추출

MySql에서 문자열을 추출하는 함수로는 `SUBSTRING`, `LEFT`, `MID`, `RIGHT` 가 있다.

<br>

### SUBSTRING
---

시작위치부터 길이만큼 추출한다.

```sql
SUBSTRING(문자열, 시작 위치, 길이)
```

- 문자열 : 원하는 문자열
- 시작 위치 : 시작 위치
- 길이 : 추출할 길이

<br>

```sql
SELECT SUBSTRING('test@gmail.com', 1, 3);
SELECT SUBSTRING('test@gmail.com', 1, 5);
SELECT SUBSTRING('test@gmail.com', 3, 6);
```

<br>

```
tes
test@
st@gma
```

<br>

### LEFT
---

문자열 맨 처음부터 길이만큼 추출한다.

```sql
LEFT(문자열, 길이)
```

- 문자열 : 원하는 문자열
- 길이 : 추출할 길이


<br>

```sql
SELECT LEFT('test@gmail.com', 4);
SELECT LEFT('test@gmail.com', 8);
SELECT LEFT('test@gmail.com', 12);
```

<br>

```
test
test@gma
test@gmail.c
```

### MID
---

시작위치부터 길이만큼 추출하며 `SUBSTRING` 함수와 동일하다.

```sql
MID(문자열, 시작 위치, 길이)
```

- 문자열 : 원하는 문자열
- 시작 위치 : 시작 위치
- 길이 : 추출할 길이

<br>

```sql
SELECT MID('test@gmail.com', 1, 3);
SELECT MID('test@gmail.com', 1, 5);
SELECT MID('test@gmail.com', 3, 6);
```

<br>

```
tes
test@
st@gma
```

<br>

### RIGHT
---

문자열 맨 마지막부터 길이만큼 추출한다.

```sql
RIGHT(문자열, 길이)
```

- 문자열 : 원하는 문자열
- 길이 : 추출할 길이


<br>

```sql
SELECT RIGHT('test@gmail.com', 4);
SELECT RIGHT('test@gmail.com', 8);
SELECT RIGHT('test@gmail.com', 12);
```

<br>

```
.com
mail.com
st@gmail.com
```