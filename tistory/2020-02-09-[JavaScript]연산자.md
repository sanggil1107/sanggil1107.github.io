---
layout: post
title: "[JavaScript] 연산자"
category: [JavaScript]

---
<br>

`연산자`에 대해 알아보자
<!-- more -->

<hr>


# 연산자
---
연산자는 하나 이상의 표현식을 대상으로 산술, 할당, 비교, 논리, 타입 연산 등을 수행한다.

## 산술 연산자
---
산술 연산자는 수학적 계산을 수행하여 새로운 값을 만든다.

### 이항 산술 연산자
---
2개의 피연산자를 대상으로 연산한다.

|연산자|의미|
|:---:|:---:|
|+|덧셈|
|-|뺄셈|
|*|곱셈|
|/|나눗셈|
|%|나머지|

```javascript
5 + 3
5 - 3
5 * 3
5 / 3
5 % 3
```

### 단항 산술 연산자
---
1개의 피연산자를 대상으로 연산한다.

|연산자|의미|
|:---:|:---:|
|++|증가|
|--|감소|

피연산자 앞에 위치할 경우 먼저 증가/감소한 후에 수행하며, 뒤에 위치할 경우 연산을 수행한 후에 증가/감소시킨다.

```javascript
var number = 10;

console.log(number++);   // 10
console.log(++number);   // 12
console.log(number--);   // 12
console.log(--number);   // 10
```

### 문자열 연결 연산자
---
`+` 연산자는 문자열 연결 연산자로써 피연산자 중 하나 이상이 문자열인 경우 동작한다.

```javascript
'1' + '2'
'1' + 2
```

## 할당 연산자
---
할당 연산자는 오른쪽의 피연산자의 결과를 왼쪽의 변수에 할당한다.

|연산자|예|동일 표현|
|:---:|:---:|:---:|
|=||a = b|a = b|
|+=|a += b|a = a + b|
|-=|a -= b|a = a - b|
|*=|a *= b|a = a * b|
|/=|a /= b|a = a / b|
|%=|a %= b|a = a % b|

```javascript
var x;

x = 10;
console.log(x);   // 10

x += 5; 
console.log(x);   // 15  

x -= 3;
console.log(x);   // 12

x *= 2;
console.log(x);   // 24

x /= 2; 
console.log(x);   // 12

x %= 2;
console.log(x);   // 0 
```

## 비교 연산자
---
비교 연산자는 왼쪽과 오른쪽 피연산자를 비교하여 boolean 값을 반환한다.

### 동등 / 일치 비교 연산자
---

|연산자|의미|예|설명|
|:---:|:---:|:---:|:---:|
|==|동등 비교|x == y|x와 y의 값이 같음|
|===|일치 비교|x === y|x와 y의 값과 타입이 같음|
|!=|부등 비교|x != y|x와 y의 값이 다름|
|!==|불일치 비교|x !== y|x와 y의 값과 타입이 다름|

동등 비교(==) 연산자는 왼쪽과 오른쪽의 피연산자를 비교할 때 암묵적 타입 변환을 통해 타입을 일치시킨 후 같은 값을 갖는지 비교한다. 따라서 동등 비교(==) 연산자는 양쪽의 피연산자가 타입은 다르더라도 암묵적 타입 변환 후에 같은 값을 수 있으면 true를 반환한다.

```javascript
5 == 5   // true
5 == '5'   // true

5 === 5   // true
5 === '5'   // false
```
```javascript
1 == "1"   // true
"one" == "one"   // true

'' == false   // true
'' == 0    // true
false == 0   // true
null == undefined   // true
```
```javascript
1 === "1"   // false
'' === false   // false
'' === 0   // false
'' === 0   // false
0 === -0   // true
NaN === NaN   // false
```

### 대소 관계 비교 연산자
---
피연산자의 크기를 비교하여 boolean 값을 반환한다.

|연산자|예|설명|
|:---:|:---:|:---:|
|>|x > y|x가 y보다 크다|
|<|x > y|x가 y보다 작다|
|>=|x >= y|x가 y보다 같거나 크다|
|<=|x <= y|x가 y보다 같거나 작다|

```javascript
6 > 0
6 > 9

6 < 0
6 < 9

6 >= 0
6 >= 6

6 <= 0
6 <= 6
```

## 삼항 연산자
---
삼항 연산자는 조건식의 평가 결과에 따라 반환할 값을 결정한다.

```
조건식 ? true일 때 : false 일 때
```

```javascript
var x = 2;

var result = x % 2 ? '홀수' : '짝수';

console.log(result)   // '짝수'
```

## 논리 연산자
---

|연산자|설명|
|:---:|:---:|
||||논리합(or)|
|&&|논리곱(and)|
|!|부정(not)|

```javascript
true || true
true || false
false || true
false || false

true && true
true && false
false && true
false && false

!true
!false
```

## 자료형 검사
---
자바스크립트에서 자료형을 검사하기 위한 방법과 같다.
- `typeof()`
- `Object.prototype.toString.call()`
  
### typeof()
---
피연산자의 데이터 타입을 문자열로 반환한다.
```javascript
typeof('String');           // string
typeof(245);                // number
typeof(true);               // boolean
typeof(function() {});      // function
typeof({});                 // object
typeof([]);                 // object
typeof(NaN);                // number
typeof(null);               // object
typeof(new String());       // ojbect
```
`typeof` 연산자의 경우, 원시 타입을 타입을 제외한 객체의 경우, 모두 object를 반환(함수의 경우 function)하여 정확히 구분하는데 문제가 있다.

### Object.prototype.toString.call()
---
`Object.prototype.toString` 메소드는 객체를 나타내는 문자열을 반환하며 `call` 메소드를 이용하면 값의 타입을 알 수 있다.

```javascript
Object.prototype.toString.call('');             // [object String]
Object.prototype.toString.call(new String());   // [object String]
Object.prototype.toString.call(1);              // [object Number]
Object.prototype.toString.call(new Number());   // [object Number]
Object.prototype.toString.call(NaN);            // [object Number]
Object.prototype.toString.call(Infinity);       // [object Number]
Object.prototype.toString.call(true);           // [object Boolean]
Object.prototype.toString.call();               // [object Undefined]
Object.prototype.toString.call(null);           // [object Null]
Object.prototype.toString.call([]);             // [object Array]
Object.prototype.toString.call({});             // [object Object]
Object.prototype.toString.call(new Date());     // [object Date]
Object.prototype.toString.call(Math);           // [object Math]
Object.prototype.toString.call(function () {}); // [object Function]
Object.prototype.toString.call(document);       // [object HTMLDocument]
Object.prototype.toString.call(undefined);      // [object Undefined]
```

이를 이용하여 타입을 반환하는 함수를 구현할 수 있다.
```javascript
function getType(type) {
    return Object.prototype.toString.call(type).slice(8, -1);
}

getType(1);  // Number
```

## 입력
---
`prompt()` 함수를 사용하면 입력을 받을 수 있는 입력창이 나타나며 사용자가 입력한 값을 return 한다.  
입력하지 않고 취소를 누르면 null 값을 반환한다.  
`confrim()` 함수를 사용하면 확인을 요구하는 창이 나타난다. (확인 - true or 취소 - false)
```javascript
var input = prompt('Message');
alert(input);
```
```javascript
var input = prompt('Message', 'str');
alert(input);
```
```javascript
var input = confirm('수락하시겠습니까?');
alert(input);
```

# 타입 변환
---
자바스크립트의 모든 값에는 문자열, 숫자 등의 타입이 있으며 이를 변활할 수 있는데 의도적으로 타입을 변환하는 것을 `명시적 타입 변환`이라고 하며, 개발자의 의도와 상관없이 암묵적으로 자동으로 타입이 변환되는 것을 `암묵적 타입 변환`이라고 한다.

## 암묵적 타입 변환
---
개발자의 의도와 상관없이 암묵적으로 타입이 변경된다.

### 문자열 타입으로 변환
---
`+` 연산자는 피연산자 중 하나 이상이 문자열이면 문자열 연결 연산자로 동작한다.

```javascript
52 + '2'   // '522'
0 + ''   // '0'
-2 + '3'   // '-23'
NaN + ''   // NaN
```

### 숫자 타입으로 변환
---
`+` 연산자를 제외한 산술 연산자는 피연산자 중 숫자 타입이 아닌 피연산자를 숫자 타입으로 암묵적 타입 변환한다. 이 때, 피연사자를 숫자 타입으로 변환할 수 없으면 NaN을 반환한다.
단, 단항 `+` 연산자는 피연산자가 숫자 타입이 아니면 숫자 타입으로 암묵적 타입 변환한다.
```javascript
52 * '2'   // 104
1 - '2'   // -1
5 / '2'   // 2.5

+''   // 0
+'0'   // 0
+'Number'   // NaN
+true   // 1
+false   // 0
+null   // 0
```

### boolean 타입으로 변환
---
if문이나 for문의 제어문에서 조건식을 boolean 타입으로 암묵적 타입 변환한다.  
아래 값들은 `false`로 변환되는 값들이다.
- false
- undefined
- null
- 0, -0
- NaN
- 빈문자열

## 명시적 타입 변환
---
개발자의 의도에 의해 명시적으로 타입을 변경한다.

### 문자열 타입으로 변환
---
문자열 타입으로 변환하는 방법은 다음과 같다.
- String() 생성자 함수
```javascript
String(1);   // '1'
String(true);   // 'true'
```

- toString() 함수
```javascript
(10).toString();   // '10'
(NaN).toString();   // 'NaN'
(false).toString();   // 'false' 
```

### 숫자 타입으로 변환
---
숫자 타입으로 변환하는 방법은 다음과 같다.
- Number() 생성자 함수
```javascript
Number('5555');   // 5555
Number(true);   // 1
```

- parseInt, parseFloat 함수(문자열만 변환 가능)
```javascript
parseInt('22');   // 22
parseFloat('10.2');   // 10.2
```

### boolean 타입으로 변환
---
boolean 타입으로 변환하는 방법은 다음과 같다.
- Boolean() 생성자 함수
```javascript
Boolean(0);   // false
Boolean(1);   // true
Boolean(NaN);  // false
Boolean('');   // false
Boolean(null);   // false
Boolean(undefined);   // false
Boolean("bool");   // true
```

- 부정 논리 연산자(!) 두 번 사용
```javascript
!!0  // false     
!!1  // true
!!NaN   // false
!!''   // false
!!null   // false
!!undefined   // false
!!"bool"   // true
```