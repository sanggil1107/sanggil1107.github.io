https://namu.wiki/w/%EC%82%BC%EA%B5%AD%EC%A7%80/%EC%A7%80%EB%AA%85
https://namu.wiki/w/%EC%B2%AD%EB%91%90%EC%8B%9C
충칭시 청두시 주나라
인프런 교육 확인


https://cocoelda.tistory.com/entry/%ED%8B%B0%EC%8A%A4%ED%86%A0%EB%A6%AC-%EB%B8%94%EB%A1%9C%EA%B7%B8-%EB%B6%81%ED%81%B4%EB%9F%BD-%EB%89%B4%EB%B6%81-%EB%B6%81%EB%A6%AC%EB%B7%B0-%EC%8D%B8%EB%84%A4%EC%9D%BC-%EC%82%AC%EC%9D%B4%EC%A6%88-%EC%A1%B0%EC%A0%88%ED%95%98%EA%B8%B0


https://melonmilk.tistory.com/?page=2

https://roadtofree.tistory.com/entry/%ED%8B%B0%EC%8A%A4%ED%86%A0%EB%A6%AC-%EB%B6%81%ED%81%B4%EB%9F%BD-%EC%8A%A4%ED%82%A8-%EC%84%A0%ED%83%9D-%ED%9B%84-%ED%95%B4%EC%95%BC%ED%95%A0-13%EA%B0%80%EC%A7%80-2

## 뷰(View)

`뷰(View)` 란 데이터베이스에 존재하는 일종의 가상 테이블을 의미하며 실제 테이블처럼 행과 열을 가지고 있지만 실제로 데이터를 저장하고 있지는 않다.

<br>

### 뷰(View)의 특징
---

- 뷰를 update 할 수 있다.
- 집계함수가 들어가는 뷰는 수정이 불가능하다.
- with check option을 주면 체크조건이 포함된다.
- 특정 사용자에게 테이블 전체가 아닌 필요한 필드만 보여줄 수 있다.
- 복잡한 쿼리를 단순화해서 사용할 수 있다.
- 쿼리를 재사용할 수 있다.
- 한 번 정의된 뷰는 수정할 수 없다.
- 삽입, 삭제, 갱신 작업에 많은 제한 사항을 가진다.
- 자신만의 인덱스를 가질 수 없다.

<br>

### 뷰(View) 생성
---

뷰(View)가 접근할 수 있는 필드를 SELECT 문에 명시하며 뷰(View)는 원본 테이블과 같은 이름을 가질 수 없다.

```sql
CREATE VIEW 뷰이름 AS
  SELECT 필드이름1, 필드이름2, ...
  FROM 테이블이름
  WHERE 조건;
```

<br>

### 뷰(View) 대체
---

`OR REPLACE` 절을 추가하여 기존에 존재하는 뷰(View)를 새로운 뷰로 대체할 수 있다.

```sql
CREATE OR REPLACE VIEW 뷰이름 AS
  SELECT 필드이름1, 필드이름2, ...
  FROM 테이블이름
  WHERE 조건;
```

<br>

만약 기존 뷰(View)가 존재하지 않는다면 신규 생성한다.

<br>

### 뷰(View) 정보
---

```sql
DESCRIBE 뷰이름;
```

<br>


### 뷰(View) 수정
---

alter문을 통해 수정할 수 있다.

```sql
ALTER VIEW 뷰이름 AS
  SELECT 필드이름1, 필드이름2, ...
  FROM 테이블이름
```

<br>

### 뷰(View) 삭제
---

```sql
DROP VIEW 뷰이름
```