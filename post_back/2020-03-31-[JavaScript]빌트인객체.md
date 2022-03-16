
## Object 객체
---
```javascript
// Object.keys()
// Object.prototype.toString() -> 모든 객체가 사용할 수 있는 메소드

var arr = ["a", "b", "c"];
document.write('Object.keys(arr) : ', Object.keys(arr), '<br/>');

var o = new Object();
document.write('o.toString() : ', o.toString(), '<br/>');


var a = new Array(1,2,3);
document.write('a.toString() : ', a.toString(), '<br/>');
            
```
```
Object.keys(arr) : 0,1,2
o.toString() : [object Object]
a.toString() : 1,2,3
```            

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

## String 객체
---

### 생성
---
String() 생성자 함수를 통해 생성할 수 있다.

```javascript
var a = new String('Yang');
var b = 'Yang';

console.log(a);   // 'Yang'
console.log(b);   // 'Yang'

console.log(typeof(a));   // object
console.log(typeof(b));   // string
```

### 속성
---

#### length
---
문자열 내의 문자 갯수를 반환한다.

```javascript
var str = 'Yang';

console.log(str.length);   // 4
```

### 함수
---
문자열은 변경 불가능한 원시 타입이므로 새로운 문자열을 만들어 반환한다.

#### charAt(x)
---
`x`로 전달한 index에 해당하는 위치의 문자를 반환한다. 문자열 범위를 벗어난 `x` 값일 경우 빈 문자열을 반환한다.

```javascript
var str = 'Yang';

console.log(str.charAt(0));   // 'Y'
console.log(str.charAt(1));   // 'a'
console.log(str.charAt(2));   // 'n'
console.log(str.charAt(3));   // 'g'
console.log(str.charAt(4));   // ''

for (var i = 0; i < str.lenght; i++) {
    console.log(str[i]);   // 'Y', 'a', 'n', 'g'
}
```

#### concat(x)
---
문자열 `x`와 연결하여 새로운 문자열을 반환한다.

```javascript
var str = 'Yang';

console.log(str.concat('Sang'));   // 'YangSang'
console.log(str);   // 'Yang'
```

#### indexOf(x)
---
문자 또는 문자열 `x`를 대상 문자열에서 검색하여 처음 위치한 index를 반환한다. 없을 경우 -1을 반환한다.

```javascript
var str = 'Yang Sang Gil';

console.log(str.indexOf('a'));   // 1
console.log(str.indexOf('G'));   // 10
console.log(str.indexOf('tt'));   // -1
```

#### lastIndexOf(x[, y])
---
문자 또는 문자열 `x`를 대상 문자열에서 검색하여 마지막에 위치한 index를 반환한다. 없을 경우 -1을 반환한다.  
`y`가 전달되면 검색 시작위치를 `y`로 하여 역방향으로 검색한다.

```javascript
var str = 'Yang Sang Gil';

console.log(str.lastIndexOf('a'));   // 6
console.log(str.lastIndexOf('a', 4));   // 1
console.log(str.lastIndexOf('tt'));   // -1
```

#### replace(x, y)
---
문자열 `x`를 대상 문자열에서 찾아 `y`로 대체한다. 검색된 문자열이 여러 개일 경우 처음 검색된 문자열만 대체된다.

```javascript
var str = 'Yang Sang Gil';

console.log(str.replace('Gil', 'Kil'));   // 'Yang Sang Kil'
```

#### split(x[, y])
---
문자열 `x`를 대상 문자열에서 검색하여 문자열을 구분한 후 분리된 문자열을 배열로 반환한다.

```javascript
var str = 'Yang Sang Gil';

console.log(str.split());   // ['Yang Sang Gil']
console.log(str.split(' '));   // ['Yang', 'Sang', 'Gil']
console.log(str.split(''));   // ['Y', 'a', 'n', 'g', ' ', 'S', 'a', 'n', 'g', ' ', 'G', 'i', 'l']

// 'a'를 구분자로 하여 반환
console.log(str.split('a'));   // ['Y', 'ng S', 'ng Gil']
```

#### substring(x[, y])
---
`x` index부터 `y`-1 index에 해당하는 문자를 모두 반환한다. 음수 값일 경우 전체 문자열을 반환한다.

```javascript
var str = 'Yang Sang Gil';

console.log(str.substring(1, 3));   // 'an'
console.log(str.substring(1));   // 'ang Sang Gil'
console.log(str.substring(-2));   // 'Yang Sang Gil'
```

#### slice(x[, y])
---
`substring`과 동일하지만 음수 값을 입력받을 수 있다.

```javascript
var str = 'Yang Sang Gil';

console.log(str.slice(1, 3));   // 'an'
console.log(str.slice(1));   // 'ang Sang Gil'

// 뒤에서 2자리 반환
console.log(str.slice(-2));   // 'il'
```

#### toLowerCase()
---
대상 문자열의 모든 문자를 소문자로 변환한다.

```javascript
var str = 'Yang Sang Gil';

console.log(str.toLowerCase());   // 'yang sang gil'
```

#### toUpperCase()
---
대상 문자열의 모든 문자를 대문자로 변환한다.

```javascript
var str = 'Yang Sang Gil';

console.log(str.toUpperCase());   // 'YANG SANG GIL'
```

#### trim() / trimaStart() / trimEnd()
---
대상 문자열의 공백 문자를 제거하여 반환한다.

```javascript
var str = '   Yang  ';

// 양쪽의 공백 제거
console.log(str.trim());   // 'Yang'

// 왼쪽 공백 제거
console.log(str.trimStart());   // 'Yang  '

// 오른쪽 공백 제거
console.log(str.trimEnd());   // '   Yang'
```

#### repeat(x)
---
`x` 만큼 반복하여 연결한 문자열을 반환한다. 0이면 빈 문자열을 반환한다.

```javascript
var str = 'Yang';

console.log(str.repeat(0));   // ''
console.log(str.repeat(1));   // 'Yang'
console.log(str.repeat(2));   // 'YangYang'
```

#### includes(x)
---
문자열 `x`가 대상 문자열에 있는지 확인하여 Boolean으로 반환한다.

```javascript
var str = 'Yang Sang Gil';

console.log(str.includes('Yang'));   // true
console.log(str.includes(''));   // true
console.log(str.includes('an'));   // true
console.log(str.includes('t'));   // false
console.log(str.includes());   // false
```

# Date 객체
---
Date 객체는 날짜와 시간을 위한 메소드를 제공하는 객체이면서 생성자 함수이다.

## 생성자
---

### new Date()
---
인수를 전달하지 않으면 현재 날짜와 시간을 가지는 인스턴스를 반환한다.
```javascript
var date = new Date();
console.log(date);   // Mon Feb 17 2020 19:23:38 GMT+0900 (한국 표준시)
```

### new Date(ms)
---
1970년 1월 1일 00:00(UTC)을 기점으로 `ms`만큼 경과한 날짜와 시간을 가지는 인스턴스를 반환한다.

```javascript
var date = new Date(0);
console.log(date);   // Thu Jan 01 1970 09:00:00 GMT+0900 (한국 표준시)

date = new Date(86400000);
console.log(date);   // Fri Jan 02 1970 09:00:00 GMT+0900 (한국 표준시)
```
### new Date(dateString)
---
날짜와 시간을 가지는 인스턴스를 반환한다.

```javascript
var date = new Date('Jan 20, 2020 22:11:07');
console.log(date);   // Mon Jan 20 2020 22:11:07 GMT+0900 (한국 표준시)

date = new Date('2020/02/17/18:18:18');
console.log(date);   // Mon Feb 17 2020 18:18:18 GMT+0900 (한국 표준시)
```

### new Date(year, month[, day, hour, minute, second, millisecond])
---
지정된 날짜와 시간을 가지는 인스턴스를 반환한다. 

```javascript
var date = new Date(2020, 1);
console.log(date);   // Sat Feb 01 2020 00:00:00 GMT+0900 (한국 표준시)

date = new Date(2020, 1, 17, 20, 20, 20);
console.log(date);   // Mon Feb 17 2020 20:20:20 GMT+0900 (한국 표준시)
```

## 함수
---

### now()
---
1970년 1월 1일 00:00:00(UTC)을 기점으로 현재 시간까지 경과한 밀리초를 숫자로 반환한다.

```javascript
Date.now();   // 1581849549752
```

### getFullYear()
---
년도를 나타내는 4자리 숫자를 반환한다.

```javascript
var today = new Date();
var year = today.getFullYear();

console.log(today);   // Sun Feb 16 2020 19:45:43 GMT+0900 (한국 표준시)
console.log(year);   // 2020
```

### setFullYear(year[, moth[, day]])
---
년도를 나타내는 4자리 숫자를 설정한다. 

```javascript
var today = new Date();

today.setFullYear(2021);

var year = today.getFullYear();

console.log(today);   // Tue Feb 16 2021 19:53:28 GMT+0900 (한국 표준시)
console.log(year);   // 2021

today.setFullYear(2030, 2, 16);

year = today.getFullYear();  

console.log(today);   // Sat Mar 16 2030 19:53:28 GMT+0900 (한국 표준시)
console.log(year);   // 2030
```

### getMonth()
---
월을 나타내는 정수를 반환한다.(0 ~ 11) 1월은 0, 12월은 11을 의미힌다.

```javascript
var today = new Date();
var month = today.getMonth();

console.log(today);   // Sun Feb 16 2020 19:57:45 GMT+0900 (한국 표준시)
console.log(month);   // 1
```

### setMonth(month[, day])
---
월을 나타내는 정수를 설정한다.(0 ~ 11)

```javascript
var today = new Date();

today.setMonth(1);   // 2월
var month = today.getMonth();

console.log(today);   // Sun Feb 16 2020 20:02:43 GMT+0900 (한국 표준시)
console.log(month);   // 1

today.setMonth(10, 7);   // 11월 7일

month = today.getMonth();

console.log(today);   // Sat Nov 07 2020 20:02:43 GMT+0900 (한국 표준시)
console.log(month);   // 10
```

### getDate()
---
날짜를 나타내는 정수를 반환한다.(1 ~ 31)

```javascript
var today = new Date();
var date = today.getDate();

console.log(today);   // Sun Feb 16 2020 20:09:46 GMT+0900 (한국 표준시)
console.log(date);   // 16
```

### setDate()
---
날짜를 나타내는 정수를 설정한다.(1 ~ 31)

```javascript
var today = new Date();

today.setDate(8);

var date = today.getDate();
console.log(today);   // Sat Feb 08 2020 20:14:12 GMT+0900 (한국 표준시)
console.log(date);   // 8
```

### getDay()
---
요일을 나타내는 정수를 반환한다.(0 ~ 6) 0은 일요일, 6은 토요일을 의미한다.

```javascript
var today = new Date();
var day = today.getDay();

console.log(today);   // Sun Feb 16 2020 20:16:33 GMT+0900 (한국 표준시)
console.log(day);   // 0
```

### getHours()
---
시간을 나타내는 정수를 반환한다.(0 ~ 23)

```javascript
var today = new Date();
var hour = today.getHours();

console.log(today);   // Sun Feb 16 2020 20:18:13 GMT+0900 (한국 표준시)
console.log(hour);   // 20
```

### setHours(hour[, minute[, second[, ms]]])
---
시간을 나타내는 정수를 설정한다.(0 ~ 23)

```javascript
var today = new Date();

today.setHours(18);

var hour = today.getHours();
console.log(today);   // Mon Feb 17 2020 18:43:06 GMT+0900 (한국 표준시)
console.log(hour);   // 18

today.setHours(18, 0, 0, 0);

hour = today.getHours();
console.log(today);   // Mon Feb 17 2020 18:00:00 GMT+0900 (한국 표준시)
console.log(hour);   // 18
```

### getMinutes()
---
분을 나타내는 정수를 반환한다.(0 ~ 59)

```javascript
var today = new Date();
var minutes = today.getMinutes();

console.log(today);   // Mon Feb 17 2020 18:47:57 GMT+0900 (한국 표준시)
console.log(minutes);   // 47
```

### setMinutes(minutes[, seconde[, ms]])
---
분을 나타내는 정수를 설정한다.(0 ~ 59)

```javascript
var today = new Date();

today.setMinutes(50);

var minutes = today.getMinutes();
console.log(today);   // Mon Feb 17 2020 18:50:15 GMT+0900 (한국 표준시)
console.log(minutes);   // 50

today.setMinutes(10, 30, 80);

minutes = today.getMinutes();
console.log(today);   // Mon Feb 17 2020 18:10:30 GMT+0900 (한국 표준시)
console.log(minutes);   // 10
```
### getSeconds()
---
초를 나타내는 정수를 반환한다.(0 ~ 59)

```javascript
var today = new Date();
var seconds = today.getSeconds();

console.log(today);   // Mon Feb 17 2020 18:55:53 GMT+0900 (한국 표준시)
console.log(seconds);   // 53
```

### setSeconds(second[, ms])
---
초를 나타내는 정수를 설정한다.(0 ~ 59)

```javascript
var today = new Date();

today.setSeconds(30);
var seconds = today.getSeconds();

console.log(today);   // Mon Feb 17 2020 18:58:30 GMT+0900 (한국 표준시)
console.log(seconds);   // 30

today.setSeconds(30, 50);
seconds = today.getSeconds();

console.log(today);   // Mon Feb 17 2020 18:58:30 GMT+0900 (한국 표준시)
console.log(seconds);   // 30
```

### getMilliseconds()
---
밀리초를 나타내는 정수를 반환한다.(0 ~ 999)

```javascript
var today = new Date();
var ms = today.getMilliseconds();

console.log(today);   // Mon Feb 17 2020 19:01:23 GMT+0900 (한국 표준시)
console.log(ms);   // 696
```

### setMilliseconds(ms);
---
밀리초를 나타내는 정수를 설정한다.(0 ~ 999)

```javascript
var today = new Date();

today.setMilliseconds(458);

var ms = today.getMilliseconds();
console.log(today);   // Mon Feb 17 2020 19:04:20 GMT+0900 (한국 표준시)
console.log(ms);   // 458
```

### getTime()
---
1970년 1월 1일 00:00:00(UTC)를 기점으로 현재 시간까지 경과된 밀리초를 반환한다.

```javascript
var today = new Date();
var time = today.getTime();

console.log(today);   // Mon Feb 17 2020 19:05:51 GMT+0900 (한국 표준시)
console.log(time);   // 1581933951843
```

### setTime(time)
---
1970년 1월 1일 00:00:00(UTC)를 기점으로 현재 시간까지 경과된 밀리초를 설정한다.

```javascript
var toaday = new Date();

today.setTime(86400000);   // 1day

var time = today.getTime();
console.log(today);   // Fri Jan 02 1970 09:00:00 GMT+0900 (한국 표준시)
console.log(time);   // 86400000
```


# Math 객체
---
Math 객체는 수학을 위한 프로퍼티와 메소드를 제공하는 객체이다.

## 속성
---

### PI
---
pi 값을 반환한다.

```javascript
Math.PI;   // 3.141592653589793
```

## 함수
---

### abs(x)
---
`x`의 절댓값을 반환한다.

```javascript
Math.abs(-1);   // 1
Math.abs('-1');   // 1
Math.abs('');   // 0
Math.abs([]);   // 0
Math.abs();   // NaN
```

### round(x)
---
`x`의 소수점 이하를 반올림하여 정수를 반환한다.

```javascript
Math.round(2.6);   // 3
Math.round(-1.5);   // -1
Math.round();   // NaN
```

### ceil(x)
---
`x`의 소수점 이하를 올림하여 정수를 반환한다.

```javascript
Math.ceil(2.6);   // 3
Math.ceil(-1.5);   // -1
Math.ceil();   // NaN
```
#### floor(x)
---
`x`의 소수점 이하를 내림하여 정수를 반환한다. 음수인 경우, 소수점 이하를 버린 후 -1 한 정수를 반환한다.

```javascript
Math.floor(2.7);   // 2
Math.floor(-3.4);   // -4
Math.floor();   // NaN
```

### sqrt(x)
---
`x`의 제곱근을 반환한다.

```javascript
Math.sqrt(9);   // 3
Math.sqrt(2);   // 1.4142135623730951
Math.sqrt(-4);   // NaN
```

### random()
---
0부터 1미만의 부동 소수점을 반환한다.

```javascript
Math.random();   // 0.590025323429568

var random = Math.floor((Math.random() * 10) + 1);
console.log(random);   // 1 ~ 10 까지의 정수
```

### pow(x, y)
---
`x`의 `y` 승(거듭 제곱)을 반환한다.

```javascript
Math.pow(2, 3);   // 8
```

### max(x)
---
`x` 중에서 가장 큰 수를 반환한다.

```javascript
Math.max(2, 3, -1);   // 3

var arr = [1, 2, 4];   // 4
Math.max(...arr);
```

### min(x)
---
`x` 중에서 가장 작은 수를 반환한다.

```javascript
Math.min(2, 3, -1);   // -1

var arr = [1, 2, 4];   // 1
Math.min(...arr);
```
