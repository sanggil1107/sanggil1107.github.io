
## Date 객체

Date 객체는 날짜와 시간을 위한 메소드를 제공하는 객체이면서 생성자 함수이다.

<br>

### 생성자
---

#### new Date()

인수를 전달하지 않으면 현재 날짜와 시간을 가지는 인스턴스를 반환한다.

```javascript
var date = new Date();
console.log(date);   // Mon Feb 17 2020 19:23:38 GMT+0900 (한국 표준시)
```

<br>

#### new Date(ms)

1970년 1월 1일 00:00(UTC)을 기점으로 `ms`만큼 경과한 날짜와 시간을 가지는 인스턴스를 반환한다.

```javascript
var date = new Date(0);
console.log(date);   // Thu Jan 01 1970 09:00:00 GMT+0900 (한국 표준시)

date = new Date(86400000);
console.log(date);   // Fri Jan 02 1970 09:00:00 GMT+0900 (한국 표준시)
```

<br>

#### new Date(dateString)

날짜와 시간을 가지는 인스턴스를 반환한다.

```javascript
var date = new Date('Jan 20, 2020 22:11:07');
console.log(date);   // Mon Jan 20 2020 22:11:07 GMT+0900 (한국 표준시)

date = new Date('2020/02/17/18:18:18');
console.log(date);   // Mon Feb 17 2020 18:18:18 GMT+0900 (한국 표준시)
```

<br>

#### new Date(year, month[, day, hour, minute, second, millisecond])

지정된 날짜와 시간을 가지는 인스턴스를 반환한다. 

```javascript
var date = new Date(2020, 1);
console.log(date);   // Sat Feb 01 2020 00:00:00 GMT+0900 (한국 표준시)

date = new Date(2020, 1, 17, 20, 20, 20);
console.log(date);   // Mon Feb 17 2020 20:20:20 GMT+0900 (한국 표준시)
```

<br>

### 함수
---

#### now()

1970년 1월 1일 00:00:00(UTC)을 기점으로 현재 시간까지 경과한 밀리초를 숫자로 반환한다.

```javascript
Date.now();   // 1581849549752
```

<br>

#### getFullYear()

년도를 나타내는 4자리 숫자를 반환한다.

```javascript
var today = new Date();
var year = today.getFullYear();

console.log(today);   // Sun Feb 16 2020 19:45:43 GMT+0900 (한국 표준시)
console.log(year);   // 2020
```

<br>

#### setFullYear(year[, moth[, day]])

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

<br>

#### getMonth()

월을 나타내는 정수를 반환한다.(0 ~ 11) 1월은 0, 12월은 11을 의미힌다.

```javascript
var today = new Date();
var month = today.getMonth();

console.log(today);   // Sun Feb 16 2020 19:57:45 GMT+0900 (한국 표준시)
console.log(month);   // 1
```

<br>

#### setMonth(month[, day])

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

<br>

#### getDate()

날짜를 나타내는 정수를 반환한다.(1 ~ 31)

```javascript
var today = new Date();
var date = today.getDate();

console.log(today);   // Sun Feb 16 2020 20:09:46 GMT+0900 (한국 표준시)
console.log(date);   // 16
```

<br>

#### setDate()

날짜를 나타내는 정수를 설정한다.(1 ~ 31)

```javascript
var today = new Date();

today.setDate(8);

var date = today.getDate();
console.log(today);   // Sat Feb 08 2020 20:14:12 GMT+0900 (한국 표준시)
console.log(date);   // 8
```

<br>

#### getDay()

요일을 나타내는 정수를 반환한다.(0 ~ 6) 0은 일요일, 6은 토요일을 의미한다.

```javascript
var today = new Date();
var day = today.getDay();

console.log(today);   // Sun Feb 16 2020 20:16:33 GMT+0900 (한국 표준시)
console.log(day);   // 0
```

<br>

#### getHours()

시간을 나타내는 정수를 반환한다.(0 ~ 23)

```javascript
var today = new Date();
var hour = today.getHours();

console.log(today);   // Sun Feb 16 2020 20:18:13 GMT+0900 (한국 표준시)
console.log(hour);   // 20
```

<br>

#### setHours(hour[, minute[, second[, ms]]])

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

<br>

#### getMinutes()

분을 나타내는 정수를 반환한다.(0 ~ 59)

```javascript
var today = new Date();
var minutes = today.getMinutes();

console.log(today);   // Mon Feb 17 2020 18:47:57 GMT+0900 (한국 표준시)
console.log(minutes);   // 47
```

<br>

#### setMinutes(minutes[, seconde[, ms]])

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

<br>

#### getSeconds()

초를 나타내는 정수를 반환한다.(0 ~ 59)

```javascript
var today = new Date();
var seconds = today.getSeconds();

console.log(today);   // Mon Feb 17 2020 18:55:53 GMT+0900 (한국 표준시)
console.log(seconds);   // 53
```

<br>

#### setSeconds(second[, ms])

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

<br>

#### getMilliseconds()

밀리초를 나타내는 정수를 반환한다.(0 ~ 999)

```javascript
var today = new Date();
var ms = today.getMilliseconds();

console.log(today);   // Mon Feb 17 2020 19:01:23 GMT+0900 (한국 표준시)
console.log(ms);   // 696
```

<br>

#### setMilliseconds(ms);

밀리초를 나타내는 정수를 설정한다.(0 ~ 999)

```javascript
var today = new Date();

today.setMilliseconds(458);

var ms = today.getMilliseconds();
console.log(today);   // Mon Feb 17 2020 19:04:20 GMT+0900 (한국 표준시)
console.log(ms);   // 458
```

<br>

#### getTime()

1970년 1월 1일 00:00:00(UTC)를 기점으로 현재 시간까지 경과된 밀리초를 반환한다.

```javascript
var today = new Date();
var time = today.getTime();

console.log(today);   // Mon Feb 17 2020 19:05:51 GMT+0900 (한국 표준시)
console.log(time);   // 1581933951843
```

<br>

#### setTime(time)

1970년 1월 1일 00:00:00(UTC)를 기점으로 현재 시간까지 경과된 밀리초를 설정한다.

```javascript
var toaday = new Date();

today.setTime(86400000);   // 1day

var time = today.getTime();
console.log(today);   // Fri Jan 02 1970 09:00:00 GMT+0900 (한국 표준시)
console.log(time);   // 86400000
```