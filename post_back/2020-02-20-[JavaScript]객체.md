---
layout: post
title: "[JavaScript] 객체"
category: [JavaScript]

---
<br>

`객체`에 대해 알아보자
<!-- more -->

<hr>




# 객체
---
자바스크립트는 객체 기반의 언어이며, 객체는 키와 값으로 구성된 프로퍼티들의 집합이다.  
객체는 프로퍼티와 메소드로 구성되어 있으며 다음과 같다.
- 프로퍼티 : 키와 값으로 구성되어 있으며 키는 유일해야 하며 문자열이어야 한다.
- 메소드 : 값이 함수일 경우 메소드라 부른다.
  
## 생성
---
객체를 만드는 방법은 다음과 같이 3가지 방법이 있다.
- 객체 리터럴
- Object 생성자 함수
- 생성자 함수

### 객체 리터럴 / Object 생성자 함수
```javascript
var obejct = {};  // 객체 리터럴을 이용한 빈 객체 생성
var obejct = {
    'number' : 273,
    'string' : 'sanggil',
    'boolean' : true,
    'array' : [1,2,3,4],
    'method' : function () {
    }
}  // 객체 리터럴을 이용한 객체 생성
var obejct = new Object();   // Object 생성자 함수를 이용한 객체 생성
```

### 생성자 함수
---
생성자 함수를 이용하면 객체를 생성하기 위한 템플릿처럼 사용할 수 있다.
- javascript에서는 생성자는 함수일 뿐이고 함수 앞에 new 키워드를 붙이면 객체를 만든다.  
- 일반적으로 생성자 함수는 대문자로 시작한다.  
- `this`는 생성자 함수가 생성할 객체를 가리킨다.  
- `this`에 연결되어 있는 프로퍼티와 메소드는 `public`이다.

```javascript
function Person() {};
var p = new Person();
p.name = 'sanggil';
p.introduce = function() {
    return 'My name is ' + this.name;
}

console.log(p.introduce());   // My name is sanggil
```

```javascript
function Person(name) {
    this.name = name;
    this.introduce = function() {
        return 'My name is ' + this.name;
    }
}

var p1 = new Person('sanggil');
console.log(p1.introduce());   // My name is sanggil

var p2 = new Person('haeun');
console.log(p2.introduce());   // My name is haeun
```

## 프로퍼티와 메서드
---
프로퍼티에 접근하는 방법은 `마침표(.)` 표기법과 `대괄호[]` 표기법이 있다.
```javascript
var person = {
    'name' : 'sanggil',
    'age' : 29,
    'address' : ['서울시', '영등포구'],
    'eat' : function(food) {
        console.log(this.name + '이 ' + food + '를 먹는다');
    }
}
console.log(person.name);   // 'sanggil'
console.log(person['name']);   // 'sanggil'
console.log(person.address);   // ['서울시', '영등포구']
console.log(person.eat('고기'));   // 'sanggil이 고기를 먹는다'
```

## 프로퍼티 추가/갱신/제거
---
객체에 존재하지 않는 프로퍼티 키에 값을 할당하면 프로퍼티를 생성한다.  
객체에 존재하는 프로퍼티에 새로운 값을 할당하면 값이 갱신된다.  
프로퍼티를 삭제할 때에는 `delete` 연산자를 이용한다.
```javascript
var student = {};

student.이름 = '상길';
student.취미 = '악기';
student.나이 = 29;
student.특기 = '개발';
student.주소 = ['서울시', '영등포구'];
student.show = function() {
    for(key in this) {
        if(key != 'show') {
            console.log(key + ' : ' + this[key]);
        }
    }
}
console.log(student.show());
student.나이 = 40;
console.log(student.show());
delete(student.나이);
console.log(student.show());
```
```
이름 : 상길
취미 : 악기
나이 : 29
특기 : 개발
주소 : 서울시,영등포구

이름 : 상길
취미 : 악기
나이 : 40
특기 : 개발
주소 : 서울시,영등포구

이름 : 상길
취미 : 악기
특기 : 개발
주소 : 서울시,영등포구
```

## 객체와 반복문
---
```javascript
var grades = {
    'list' : {
        '상길' : 88,
        '민수' : 90,
        '철수' : 87
    },
    'show' : function() {
        for(var name in this.list) {
            console.log(name + ', ' + this.list[name]);
        }
    }
}

grades.show();
```
```
상길, 88
민수, 90
철수, 87
```

```javascript
var grades = {
    'subject' : 'math',
    '상길' : 88,
    '민수' : 90,
    '철수' : 87
}
for(var key in grades) {
    console.log('key : ' + key + ', value : ' + grades[key]);
}

```
```
key : subject, value : math
key : 상길, value : 88
key : 민수, value : 90
key : 철수, value : 87
```


