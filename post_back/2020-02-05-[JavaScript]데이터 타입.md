---
layout: post
title: "[JavaScript] 데이터 타입과 변수"
category: [JavaScript]

---
<br>

`데이터 타입과 변수`에 대해 알아보자
<!-- more -->

<hr>



# 데이터 타입
---
데이터 타입은 프로그래밍 언어에서 사용할 수 있는 데이터(숫자, 문자열, 불리언 등)의 종류를 말한다. 코드에서 사용되는 모든 데이터는 메모리에 저장되고 참조될 수 있어야 한다.  
자바스크립트에서 사용하는 데이터 타입은 아래와 같다.  
- 원시 타입
   - string
   - number
   - boolean
   - null
   - undefined
   - symbol

- 객체 타입
   - object

## 원시 타입 
---
원시 타입은 변경불가능한 값이며 값에 의한 전달이다.

### string
---
문자열을 만드는 방법은 큰따음표, 작은따음표를 사용하여 만들 수 있다. 또한, 따음표를 출력하고자 하는 경우 `" '' "`, `' "" '` 와 같이 다른 따음표로 표현하면 된다.  
`+` 기호를 이용하여 여러 개의 문자열을 연결할 수 있으며 다른 언어와 달리 문자열을 변경할 수 없다.

```javascript 
var str = "This is \n'javascript'";
console.log(str);
```
```
This is
'javascript'
```

```javascript
var str = "This is" + " " +"javascript";
console.log(str);
```
```
This is javascript
```

### number
---
자바스크립트는 하나의 숫자 타입만 존재하며 모든 수를 하나의 타입으로 표현할 수 있다.
```javascript
var int = 270;
console.log(int);   // 270

var int1 = (5 + 3) * 2);
console.log(int1);   // 16

var double = 3 / 2;
console.log(double);   // 1.5
```

추가적으로 `Infinity`, `-Infinity`, `NaN` 값도 표현할 수 있다.
- `Infinity` : 양의 무한대
- `-Infinity` : 음의 무한대
- `NaN` : 산술 연산 불가

```javascript
var plusInfinity = 10 / 0;
console.log(plusInfinity);   // Infinity

var minusInfinity = 10 / -0;
console.log(minusInfinity);   // -Infinity

var nan = 2 * 'str'
console.log(nan);   // NaN
```


### boolean
---
boolean 값은 참과 거짓을 나타내는 `true`와 `false`이며 `true`는 1, `false`는 0으로 매핑이 된다.  
비교연산자가 여러 개인 경우 왼쪽부터 차례대로 연산한다.
```javascript
var bool1 = true;
var bool2 = false;

var foo1 = 47 > 45;
var foo2 = !true;
var foo3 = 30 > 20 < 10;

console.log(foo1);   // true
console.log(foo2);   // false
console.log(foo3);   // true
```

### undefined
---
변수 선언 이후 값을 할당하지 않은 변수는 `undefined` 값을 가지며 존재하지 않는 객체 프로퍼티에 접근할 때에 `undefined`가 반환된다.

```javascript
var un;
console.log(un);   // undefined
```

### null
---
의도적으로 변수에 값이 없다는 것을 명시할 때 `null`을 사용한다. 또한, 함수가 호출되었으나 유효한 값을 반환할 수 없는 경우에 `null`을 반환한다.

```javascript
var n = 'Yang';
n = null;
```
