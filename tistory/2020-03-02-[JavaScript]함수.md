---
layout: post
title: "[JavaScript] 함수"
category: [JavaScript]

---
<br>

`함수`에 대해 알아보자
<!-- more -->

<hr>



# 함수
---
함수란 어떤 작을 수행하기 위해 필요한 코드들의 집합을 정의한 코드 블록이다. 필요한 때에 호출하여 실행할 수 있다. 이러한 특징은 코드의 재사용 측명에서 매우 유리하다.  

## 함수 생성
---
자바스크립트에서 함수를 생성하는 방법은 아래와 같이 3가지 방법이 있다.
- 함수 선언식
- 함수 표현식
- Funtion 생성자 함수

### 함수 선언식
---
일반적인 프로그래밍 언어의 선언과 같이 함수명, 매개변수, 내용, 반환값으로 구성되어 있으며 함수 이름으로 함수를 호출한다.
```javascript
function 함수명() {
    로직
}
```
```javascript
function functionmake() {
    console.log('함수 선언');
}
functionmake(); // 함수 선언
```

### 함수 표현식
---
함수 리터럴 방식으로 정의하고 변수에 할당할 수 있다. 아래와 같이 함수명이 생략된 경우를 `익명 함수 표현식이라` 한다. functionmake는 변수이며, function은 익명함수 이고 변수명을 통해 호출한다.(변수명에는 함수명이 아니라 할당된 함수를 가리키는 참조값이 저장된다.)
```javascript
var 함수명 = function() {
    로직
}
```
```javascript
var functionmake = function {
    console.log('함수 표현');
}
functionmake(); // 함수 표현
```

## Function 생성자 함수
---
Function 생성자 함수를 이용하여 함수를 생성한다.
```javascript
var 함수명 = new Function(arg1, arg2, .. ,body);
```
```javascript
var plus = new Function('number', 'return number + number');
console.log(plus(10)); // 20
```

## 호이스팅
---
```javascript
sayHi(); // 'hi'
console.log(hi); // undefined
sayHello() ; // sayHello is not a function


var hi ='hi';
function sayHi(){ console.log('hi') }
var sayHello = function(){ console.log('hello') };
```
위의 예에서 함수 선언문으로 선언된 `sayHi()` 함수는 함수 정의 이전에 호출이 가능하지만 함수 표현식으로 선언된 `sagHello()` 함수는 함수 정의 이전에 호출이 불가능하다. 함수의 선언 위치와 상관없이 코드 어디서든 함수 호출이 가능한데 이것을 호이스팅이라 한다.(자바스크립트는 함수 뿐만 아니라 모든 선언(변수, 함수, 클래스 등)을 호이스팅 한다.)

호이스팅이란 모든 선언문이 Scope의 선두로 옮겨진 것처럼 동작하여 선언문이 선언되기 이전에 참조 가능한 특징을 말한다. 이는 자바스크립트 엔진이 실행될 때 파일을 먼저 읽어 선언된 변수와 함수를 메모리에 저장하기 때문이다.

함수 선언식으로 정의된 함수는 호이스팅될 때 함수 선언, 초기화, 할당이 한 번에 이루어 진다.(함수 호이스팅) 그러므로 선언문 위치에 상관없이 어디서든 호출이 가능하다.

함수 표현식으로 정의된 함수는 호이스팅될 때 변수 생성 및 초기화(undefined) 할당이 분리되어 진행되며(변수 호이스팅) 실제 할당은 선언문에서 진행된다.

변수의 경우도 함수 표현식과 마찬가지로 변수 호이스팅이 되므로 호이스팅 될 때에는 `undefined`로 초기화만 진행된다.(할당 x)

## 매개변수
---
함수 실행을 위해 추가 정보가 필요한 경우 매개변수를 지정하며 매개변수는 함수 내의 변수와 동일하게 메모리 공간을 가진다.
- 선언된 매개변수보다 적은 수의 인수를 전달하면 해당 매개변수는 `undefined`로 초기화된다.  
- 선언된 매개변수보다 많은 수의 인수를 전달하면 초과된 인수는 무시된다.
```javascript
var f = function(p1, p2) {
    console.log(p1, p2);   // 1 undefined
}

f(1);
```

### call-by-value
---
인수가 원시 타입일 경우, `call-by-value(값에 의한 호출)`로 동작한다. 이는 매개변수에 값을 복사하여 전달하는 방식이며 함수 내에서 값이 변경되어도 기존 원시 타입 값은 변경되지 않는다.
```javascript
function func(b) {
    b = 2;
}

var a = 1;
func(a);
console.log(a);   // 1
```

### call-by-reference
---
인수가 객체 타입일 경우, `call-by-reference(참조에 의한 호출)`로 동작한다. 이는 매개변수에 값이 복사되지 않고 객체의 참조값이 매개변수에 저장되는 방식이며 함수 내에서 객체의 값을 변경하면 전달되어진 객체 참조형의 값도 변경된다.
```javascript
// 함수 내에서 매개변수에 새로운 객체의 참조값을 저장하였으므로 a와 b는 서로 다른 객체 참조값을 가지고 있다.
function func(b) {
    b = {
        'id' : 1
    };
    b.id = 2;
}

var a = {
    'id' : 1
};
func(a);   // b = a
console.log(a.id);   // 1
```

```javascript
// a와 b는 서로 같은 객체의 참조값을 가지고 있다.
function func(b) {
    b.id = 2;
}

var a = {
    'id' : 1
};
func(a); // b = a;
console.log(a.id);   // 2
```

## 반환값
---
함수 내에서 수행된 결과를 `return` 키워드를 이용하여 반환할 수 있으며 반환된 값을 반환값이라 한다. 배열 등을 이용하여 한 번에 여러 개의 값을 반환할 수 있다.

```javascript
function sum(s1, s2) {
    var result = s1 + s2;
    return result;
}

console.log(sum(10, 20));  // 30

function mul(m1, m2, m3) {
    var result1 = m1 * m2;
    var result2 = m1 * m2 * m3;
    return [result1, result2];
}

console.log(mul(2,2,4));  // [4, 16]
console.log(mul(2,2,4)[0]);  // 4
console.log(mul(2,2,4)[1]);  // 16
```

## 함수 프로퍼티
---
기본적으로 제공되는 함수 프로퍼티이다.

### arguments
---
arguments 객체는 함수 호출 시에 전달된 인수들의 정보를 가지고 있는 유사 배열 객체이며, 함수 내부에서 지역변수처럼 사용된다.
```javascript
function arg(x) {
    console.log(arguments);
}

console.log(arg());      // {}
console.log(arg(1));     // {'0' : 1}
console.log(arg(1, 2));  // {'0' : 1, '1' : 2}
```

다음과 같이 매개변수의 갯수가 정해져있지 않은 가변 인자 함수를 구현할 때 유용하다.
```javascript
function sumAll() {
    // arguments.length : 함수 호출 시 입력된 매개변수의 갯수
    console.log(typeof(arguments) + ' : ' + arguments.length);
}

sumAll(1,2,3,4,5);  // object : 5
```
```javascript
function sumAll() {
    var output = 0;
    for (var i=0; i<arguments.length; i++) {
        output += arguments[i];
    }
    console.log(output);
}

sumAll(1,2,3,4,5);  // 15
```

### length
---
함수 정의 시 선언된 매개변수의 갯수를 의미한다.
```javascript
function one(arg1) {
    console.log('one.length : ' + one.length);
}

one('var1', 'var2');    // one.length : 1
```

### name
---
함수명을 의미한다. 익명함수의 경우 함수명이 없으므로 변수명을 값으로 한다.

```javascript
var f1 = function sum(a, b) {
    return a + b;
}

var f2 = function(a, b) {
    return a + b;
}

function sum(a, b) {
    return a + b;
}

console.log(f1.name);   // sum
console.log(f2.name);   // f2
console.log(sum.name);  // sum
```

### caller
---
자신을 호출한 함수를 의미한다.

```javascript
function f() {
    f1();
}

function f1() {
    console.log("caller :" + f1.caller);
}

console.log(f());   // caller : function f() { f1(); }
console.log(f1());  // caller : null
```


## 내부함수
---
함수 내부에 정의된 함수를 내부함수라 하며 외부에서 접근할 수 없다.
```javascript
function outter() {
    var title = 'coding everyday';
        
    function inner() {
        console.log(title);
    }
    inner();
}

outter();   // coding everyday
inner();    // inner is not defined
```

## 콜백 함수
---
명시적으로 호출하는 방식이 아닌 특정 시점/이벤트가 발생했을 때 호출되는 함수를 콜백함수라 한다. 또한, 특정 함수의 인자로 넘겨 코드 내부에서 호출되는 함수 역시 콜백 함수가 될 수 있다.
```javascript
function call(a, b, callback) {
    var mul = a * b;
    callback(mul);  // callback 함수 실행
}

var callback = function (mul) {
    console.log(mul)
}

call(2, 3, callback);   // 6
```
callback 함수는 call 함수 내에서 호출되는 시점에 호출되는 콜백 함수이다.

```javascript
function func() {
    function f() {
        console.log("함수 실행");
    }
    return f;
}

var myf = func();   // func() 함수의 리턴 값인 f 함수가 전달된다. 
myf();  // "함수 실행"
```
f 함수는 리턴된 후 myf() 호출 시점에 호출되는 콜백 함수이다.  

```javascript
function call(a, b) {
    var mul = a * b;
    return mul;
}

var callback = function (mul) {
    console.log(mul)
}

callback(call(2, 3));   // 6
```
위와 같이 만약 콜백 함수를 사용하지 않고 순차적으로 함수를 호출한다면 call 함수가 실행 완료된 후에야 callback 함수가 실행되므로 call 함수가 실행 완료될 때까지 기다려야 한다. 만약 웹사이트에서 call 함수의 실행이 길어진다면 웹사이트가 멈춰버릴 수 있다.
