## Number 객체
---

### 생성
---
Number() 생성자 함수를 통해 생성할 수 있다.

```javascript
var a = new Number(1);
var b = new Number('1');
var c = 1;

console.log(a);   // 1
console.log(b);   // 1

console.log(typeof(a));   // object
console.log(typeof(c));   // number
```

### 속성
---

#### MAX_VALUE
---
사용 가능한 가장 큰 숫자를 반환한다.

```javascript
Number.MAX_VALUE;   // 1.7976931348623157e+308
```

#### MIN_VALUE
---
사용 가능한 가장 작은 양수를 반환한다.

```javascript
Number.MIN_VALUE;   // 5e-324
```

#### POSITIVE_INFINITY
---
양의 무한대(`Infinity`)를 반환한다.

```javascript
Number.POSITIVE_INFINITY;   // Infinity
```

#### NEGATIVE_INFINITY
---
음의 무한대(`-Infinity`)를 반환한다.

```javascript
Number.NEGATIVE_INFINITY;   // -Infinity
```

### 함수
---

#### isFinite(x)
---
`x`값이 정상적인 수인지 확인하여 Boolean으로 반환한다.

```javascript
Number.isFinite('str');   // false
Number.isFinite(123);   // true
```

#### isInteger(x)
---
`x`값이 정수인지 확인하여 Boolean으로 반환한다.

```javascript
Number.isInteger(123);   // true
Number.isInteger('123');   // false
```

#### isNaN(x)
---
`x`값이 NaN인지 확인하여 Boolean으로 반환한다.(숫자가 아닌 경우는 false)

```javascript
Number.isNaN(NaN);   // true
Number.isNaN([]);   // false
Number.isNaN('13');   // false
```

#### toExponential(x)
---
지수 표기법으로 변환하여 문자열로 반환한다.

```javascript
var num = 10;

console.log(num.toExponential(1));   // '1.0e+1'
console.log(num.toExponential(2));   // '1.00e+1'
```

#### toFixed(x)
---
`x`를 소수점자리로 하여 반올림한 후 문자열로 반환한다.

```javascript
var num = 123.45;

// 소수점 이하에서 반올림
console.log(num.toFixed());   // '123'

// 반올림하여 소수점 1자리까지 표시
console.log(num.toFixed(1));   // '123.5'

// 반올림하여 소수점 2자리까지 표시
console.log(num.toFixed(2));   // 123.45
```

### toPrecision(x)
---
`x`로 지정된 전체 자릿수까지 남겨두고 나머지 자릿수를 반올림하여 문자열로 반환한다.
전체 자릿수를 표현할 수 없는 경우 지수 표기법으로 결과를 반환한다.

```javascript
var num = 1234.56;

console.log(num.toPrecision());   // '1234.56'
console.log(num.toPrecision(3));   // '1.23e+3'
console.log(num.toPrecision(5));   // '1234.6'
```

#### toString(x)
---
숫자를 문자열로 변환하여 반환한다. `x`는 진법을 의미한다.

```javascript
var num = 10;

console.log(num.toString());   // '10'
console.log((2).toString());   // '2'
console.log(2 .toString());   // '2'

// 10을 2진법으로 표현
console.log(10 .toString(2));   // 1010
```

#### valueOf()
---
Number 객체의 원시 타입 값을 반환한다.

```javascript
var numObj = new Number(42);
console.log(typeof numObj);   // object

const num = numObj.valueOf();
console.log(num);   // 42
console.log(typeof num);   // number
```
