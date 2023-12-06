## 공백, 문자 제거(TRIM, LTRIM, RTRIM)

MySql에서 공백, 문자를 제거하는 함수로 `TRIM`, `LTRIM`, `RTRIM` 이 있다.

<br>

### TRIM
---

공백이나 문자를 제거한다.

```sql
TRIM(문자열)
TRIM([BOTH | READING | TRAILING] 문자 FROM 문자열)
```

<br>

#### 좌우 공백 제거

문자열의 공백을 제거한다.

```sql
TRIM(문자열)
TRIM(BOTH FROM 문자열)
```

<br>

```sql
SELECT TRIM(' sanggil ');
```

<br>

```
'sanggil'
```

<br>

#### 좌우 문자 제거(BOTH)

문자열에서 제거할 문자를 좌우로 제거한다.

```sql
TRIM(BOTH 문자 FROM 문자열)
```

<br>

```sql
SELECT TRIM(BOTH 'x' FROM 'xxsanggilxx');
```

<br>

```
'sanggil'
```

<br>

#### 좌측 공백 제거(LEADING)

문자열에서 좌측 공백을 제거한다.

```sql
TRIM(LEADING FROM 문자열)
```

<br>

```sql
SELECT TRIM(LEADING FROM ' sanggil ');
```

<br>

```
'sanggil '
```

<br>

#### 좌측 문자 제거(LEADING)

문자열에서 좌측 문자를 제거한다.

```sql
TRIM(LEADING 문자 FROM 문자열)
```

<br>

```sql
SELECT TRIM(LEADING 's' FROM 'sanggil');
```

<br>

```
'anggil'
```

<br>

#### 우측 공백 제거(TRAILING)

문자열에서 우측 공백을 제거한다.

```sql
TRIM(TRAILING FROM 문자열)
```

<br>

```sql
SELECT TRIM(TRAILING FROM ' sanggil ');
```

<br>

```
' sanggil'
```

<br>

#### 우측 문자 제거(TRAILING)

문자열에서 우측 문자를 제거한다.

```sql
TRIM(LEADING 문자 FROM 문자열)
```

<br>

```sql
SELECT TRIM(LEADING 'l' FROM 'sanggil');
```

<br>

```
'sanggi'
```

<br>

### LTRIM
---

좌측 공백을 제거한다.

```sql
LTRIM(문자열)
```

<br>

```sql
SELECT LTRIM(' sanggil ');
```

<br>

```
'sanggil '
```

<br>

### RTRIM
---

우측 공백을 제거한다.

```sql
RTRIM(문자열)
```

<br>

```sql
SELECT RTRIM(' sanggil ');
```

<br>

```
' sanggil'
```