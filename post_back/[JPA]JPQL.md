# JPQL
## 문법
1. 쿼리 문법
- 엔터티와 속성은 대소문자 구분
- 키워드 구분 없음
- 엔터티 이름 사용(테이블 이름 X)
- 별칭 필수

2. 집합과 정렬
select
count(m)
sum(m)
~
group by, having

3. TypeQuery, Query
- TypeQuery : 변환 타입이 명확할 때 사용
```
TypeQuery<Member> query = em.createQuery("select m from Member m", Member.class)
TypeQuery<String> query = em.createQuery("select m.username from Member m", String.class)
```
4. 결과조회 API

`TypeQuery<Member> query = em.createQuery("select m from Member m", Member.class)`

1) List resultlist = query.getResultList();
결과가 없으면 빈 컬렉션 반환

2) Member result = query.getSingleResult();
결과가 없으면 : noResultException
결과가 2개 이상이면 : notUniqueException

5. 파라미터 바인딩 - 이름 기준, 위치 기준
```
TypeQuery<Member> query = em.createQuery("select m from Member m where m.username = :username", Member.class)
query.setParameter("username", "member1").getSingleResult()
```

6. 프로젝션 : select 절에 조회할 대상을 지정하는 것
1) 프로젝션
프로젝션 대상 : 엔터티, 임베디드 타입, 스칼라타입(문자, 숫자 등 기본 데이터 타입)
```
select m from Member m
select m.team from member m
select m.address from member m
select m.username, m.age from member m
```

엔터티 프로젝션 : 영속성 컨텍스트로 다 관리 됨
```
List<Member> result = em.createQuery("select m from member m", Member.class).getResultList();
List<Team> result = em.createQuery("select m.team from member m join m.team team", Team.class).getResultList();
List<Address>> result = em.createQuery("select o.address from Order o", Address.class).getResultList();
```
result에 해당하는 결과 값은 모두 영속성 컨텍스트에 관리

2) 프로젝션 - 여러 값 조회
List resultlist = em.createQuery("select m.username, m.age from member m", Member.class).getResultList();

(1). 쿼리타입으로 조회
Object o = resultList.get(0);
Object[] result = (Object[]) 0;

(2). 오브젝트 배열 타입으로 조회
List<Object[]> resultList = em.createQuery("select m.username from member m", Member.class)

(3). new 명령어로 조회
List<Member> result = em.createQuery("select new jpql.Member(m.username, m.age) from member m", Member.class).getResultList();


7. 페이징

8. 조인 : 엔터티를 중심으로 문법
내부조인 : select m from member m [inner] join m.team team
외부조인 : select m from member m left join m.team team