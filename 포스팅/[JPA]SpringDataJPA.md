# 스프링 데이터 JPA
스프링 데이터 JPA는 JPA를 더 편리하게 사용할 수 있도록 스프링 프레임워크가 지원하는 프로젝트이다. 데이터 접근 계층을 계발할 때 지루하게 반복되는 CRUD 문제를 해결해준다.

우선 CRUD를 처리하기 위한 공통 인터페이스를 제공한다. 그리고 Repository 개발 시 인터페이스만 작성하면 실행 시점에 스프링 데이터 JPA가 구현 객체를 동적으로 생성해서 주입해준다. 즉, 데이터 접근 계층 개발할 때 구현 클래스 없이 인터페이스 작성만으로 개발을 완료할 수 있다.
일반적인 CRUD 메소드(save, find, delete 등)는 JpaRepositroy 인터페이스만 상속 받아도 공통으로 제공한다. 그리고 findByUsername 처럼 관계에 맞게 메소드 이름을 지어주면 자동으로 스프링 데이터 JPA가 메소드 이름을 분석하여 적절한 JPQL을 실행한다.
```
public interface MemberRepository extends JpaRepository<Member, Long> {
    public List<Member> findByUsername(String username);
}
```
 - 실행되는 JPQL : select m from Member m where username = :username

 ## 공통 인터페이스 기능
 - Generic
    - T : 엔터티 타입
    - ID : 식별자 타입(PK)

JpaRepository를 상속 받으며 제네릭에 회원 엔터티와 회원 엔터티의 식별자 타입을 지정한다. 

## 주요 메소드
 - save(S) : 새로운 엔터티는 저장하고 이미 있는 엔터티는 병합한다.
    - 엔터티에 식별자 값이 없으면 em.persist() 호출
    - 엔터티에 식별자 값이 있으면 em.merge() 호출

 - delete(T) : 엔터티 하나를 삭제한다. 내부에서 em.remove() 호출
 - findById(ID) : 엔터티 하나를 조회한다. 내부에서 em.find() 호출
 - getById(ID) : 엔터티를 프록시로 조회한다. 내부에서 em.getReference() 호출
 - findAll : 모든 엔터티를 조회한다. 정렬이나 페이징 조건을 파라미터로 제공한다.

## 쿼리 메소드
 - 메소드 이름으로 쿼리 생성
 - 메소드 이름으로 JPA NamedQuery 호출
 - @Query 어노테이션을 사용하여 레포지토리 인터페이스에 쿼리 직접 정의

### 메소드 이름으로 쿼리 생성
```
List<Member> findByUsernameAndAge(String username, int age);
```
인터페이스ㅔ 정의한 findByusernameAndAge() 메소드를 실행하면 스프링 데이터 JPA는 메소드 이름을 분석하여 JPQL을 생성하고 실행한다.
 - select m from Member m where m.username = ?1 and m.age = ?2


### 메소드 이름으로 JPA NamedQuery 호출


### @Query 어노테이션을 사용하여 레포지토리 인터페이스에 쿼리 직접 정의