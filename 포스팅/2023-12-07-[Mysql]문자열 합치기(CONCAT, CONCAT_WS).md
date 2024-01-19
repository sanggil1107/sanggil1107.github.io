## 문자열 합치기(CONCAT, CONCAT_WS)

MySql에서 문자열을 하나로 합치는 경우 `CONCAT`, `CONCAT_WS` 함수를 사용한다.

<br>

### CONCAT
---

둘 이상의 문자열을 입력한 순서로 합친다.

```sql
CONCAT(문자열1, 문자열2 ...)
```

<br>

```sql
SELECT CONCAT('안녕', '하세요');
```

<br>

```
안녕하세요
```

<br>

문자열뿐만 아니라 컬럼 데이터도 가능하다.

```sql
SELECT CONCAT(컬럼1, ' + ', 컬럼2) as newcolumn FROM 테이블명;
```

<br>

```
컬럼1값 + 컬럼2값
...
```

<br>

### CONCAT_WS
---

CONCAT 함수와 마찬가지로 둘 이상의 문자열을 입력한 순서로 합치는데 문자열 사이에 설정 구분자를 넣어야한다.

CONCAT 함수와는 다르게 함쳐지는 문자열에 NULL 값이 포함되어 있어도 NULL로 반환하지 않는다.

```sql
CONCAT_WS(구분자, 문자열1, 문자열2 ...)
```

<br>

```sql
SELECT CONCAT_WS(',', '안녕', '하세요');
SELECT CONCAT_WS(',', '안녕', NULL, '하세요');
```

<br>

```
안녕,하세요
안녕,하세요
```