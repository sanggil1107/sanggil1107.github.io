## 문자열 길이(LENGTH, CHAR_LENGTH)

MySql에서 문자열 길이를 구하는 경우 `LENGTH`, `CHAR_LENGTH` 함수를 사용한다.

<br>

### LENGTH
---

문자열의 길이를 Byte로 반환한다.(영어는 1byte, 한글은 3byte)

```sql
LENGTH(문자열)
```

<br>

```sql
SELECT LENGTH('Hello');
SELECT LENGTH('안녕');
```

<br>

```
5
6
```

<br>

### CHAR_LENGTH
---

문자열의 길이를 계산할 때 byte 수로 계산하지 않고 문자가 몇개 있는지를 기준으로 길이를 계산한다. 

<br>

```sql
CHAR_LENGTH(문자열)
```

<br>

```sql
SELECT CHAR_LENGTH('Hello');
SELECT CHAR_LENGTH('안녕');
```

<br>

```
5
2
```