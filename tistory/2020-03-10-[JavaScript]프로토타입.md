---
layout: post
title: "[JavaScript] 프로토타입"
category: [JavaScript]

---
<br>

`프로토타입`에 대해 알아보자
<!-- more -->

<hr>

# 프로토타입 객체
---
다름 객체지향 프로그래밍 언어와 달리 자바스크립트는 프로토타입 기반 객체지향 프로그래밍 언어이다. 모든 객체는 자신의 부모 역할을 담당하는 하는 객체와 연결되어 있으며 이러한 부모 객체를 Prototype (객체)라 한다.

## [[Prototype]] / prototype 프로퍼티
---
모든 객체는 자신의 프로토타입 객체(부모 객체)를 가리키는 [[Prototype]]을 가지며 이는 상속을 위해 사용된다. 함수 객체는 일반 객체와 달리 추가적으로 prototpye 프로퍼티도 가진다.

```javascript
function Parent(name) {
    this.name = name;
}

var child = new Parent('Yang');
```

### [[Prototpye]]
---
모든 객체가 가지고 있는 특징(`__proto__`)이며 자신의 부모 역할을 하는 프로토타입 객체를 가리킨다.

```javascript
console.log(Parent.__proto__ === Function.prototype);   // true
```

### prototype 프로퍼티
---
함수 객체만 가지고 있는 프로퍼티(`prototpye`)이며 함수 객체가 생성자로 사용될 때 이 함수를 통해 생성되는 객체의 부모 역할을 하는 객체를 가리킨다.

```javascript
console.log(Parent.prototype === child.__proto__);   // true
```

### Prototype chain
---
자바스크립트는 [[Prototype]]이 가리키는 부모 객체를 찾아 부모의 프로퍼티나 메소드에 접근할 수 있다. 이를 Prototype chain이라 한다.

#### 객체 리터럴 방식
---
객체 리터럴 방식으로 생성된 객체는 결국 Object() 생성자 함수로 객체를 생성한 것이다.

```javascript
var Parent = {
    name : 'Yang',
    age : 30
}

console.log(Parent.__proto__ === Object.prototype);
console.log(Object.__proto__ === Function.prototype);
console.log(Function.prototype.__proto__ === Object.prototype);
```

#### 생성자 함수 방식
---
생성자 함수 방식으로 생성된 객체는 함수 리터럴 방식이며 이는 Function() 생성자 함수로 함수를 생성한 것이다.

```javascript
function Parent(name, age) {
    this.name = name;
    this.age = age;
}

var child = new Parent('Yang', 30);

console.log(child.__proto__ === Parent.prototype);
console.log(Parent.prototype.__proto__ === Object.prototype);
console.log(Parent.__proto__ === Function.prototype);
console.log(Function.prototype.__proto__ === Object.prototype);
```
### 프로토타입 객체 확장
---
프로토타입 객체도 프로퍼티를 추가/삭제할 수 있으며 이는 prototype chain에 반영된다.

```javascript
function Parent(name) {
    this.name = name;
}

var child = new Parent('Yang');

Parent.prototype.age = 30;

console.log(child.name);   // 'Yang'
console.log(child.age);   // 30
```
Parent.protoype 객체에 age 프로퍼티를 추가하였고 이는 prototype chain에 반영된다. 따라서 생성자 함수 Parent에 의해 생성된 객체 child는 부모 객체인 Parent.prototype의 프로퍼티 age에 접근할 수 있다.

### 원시 타입 확장
---
원시 타입으로 프로퍼티나 메소드를 호출할 때에는 해당 타입의 Wrapper 객체로 일시적 변환되어 프로토타입 객체를 공유한다.

```javascript
var str = 'Yang';

String.prototype.Mystr = function(str) {
    return str;
}

console.log(str.Mystr(str));   // 'Yang'
```
위와 같이 String 객체의 프토로타입 객체(String.prototype)에 메소드를 추가하면 원시 타입에서 해당 메소드에 접근할 수 있다.

### 프로토타입 변경
---
프로토타입 객체는 다른 객체로 변경될 수 있으며 이러한 특징을 이용하여 상속을 구현할 수 있다.

```javascript
function Parent(name) {
    this.name = name;
}

var child1 = new Parent('Yang');

Parent.prototype = { age : 30 };

var child2 = new Parent('Sang');

console.log(child1.age);   // undefined
console.log(child2.age);   // 30
```
