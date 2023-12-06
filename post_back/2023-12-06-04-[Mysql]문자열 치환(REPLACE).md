## 문자열 치환(REPLACE)

MySql에서 특정 문자들을 치환하는 경우 `REPLACE` 함수를 사용한다.

<br>

### REPLACE
---

지정된 문자열 값을 특정 문자열로 치환한다.

```sql
REPLACE(문자열/컬럼명, 찾을 문자, 변경할 문자)
```

<br>

```sql
SELECT REPLACE('SANGGIL', 'SANG', 'GIL');
```

<br>

```
GILGIL
```