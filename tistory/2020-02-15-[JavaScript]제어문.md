---
layout: post
title: "[JavaScript] 제어문"
category: [JavaScript]

---
<br>

`제어문`에 대해 알아보자
<!-- more -->

<hr>


# 조건문
---

## if 문
---
```javascript
if (조건식1) {
   조건식1이 참이면 이 코드 블록이 실행된다.
} 
else if (조건식2) {
   조건식2이 참이면 이 코드 블록이 실행된다.
} 
else {
   조건식1과 조건식2가 모두 거짓이면 이 코드 블록이 실행된다.
}
```
```javascript
var date = new Date();
var hour = date.getHours();

if (hour < 11) {
    console.log('아침입니다.');
}

else if (hour < 15) {
    console.log('점심입니다.');
}

else {
    console.log('저녁입니다.');
}
```
```
저녁입니다.
```

## switch 문
---
```javascript
switch (표현식) {
  case 표현식1:
    switch 문의 표현식과 표현식1이 일치하면 실행될 문;
    break;
  case 표현식2:
    switch 문의 표현식과 표현식2가 일치하면 실행될 문;
    break;
  default:
    switch 문의 표현식과 일치하는 표현식을 갖는 case 문이 없을 때 실행될 문;
}
```
```javascript
var input = Number(prompt('숫자를 입력하세요'));

switch(input % 2) {
    case 0:
        console.log('짝수');
        break;
    case 1:
        console.log('홀수');
}
```

### 삼항 연산자
---
`(불표현식) ? (참일 때 실행) : (거짓일 때 실행)` 형식으로 간단하게 비교 표현 가능하다.
```javascript
var input = Number(prompt('숫자를 입력하세요'));

(input > 0 ) ? console.log('자연수') : console.log('음수');
```


# 반복문
---
## while문
---
```javascript
while (불 표현식) {
    문장
}
```
```javascript
var value = 0;

while (value < 4) {
    console.log(value + '번째');
    value++;
}
```
```
0번째 1번째 2번째 3번째
```

## do while문
---
조건을 먼저 검사하고 반복을 실행, 즉 최소 한 번은 무조건 실행된다.
```javascript
do {
  문장
} while(불 표현식)
```
```javascript 
var value = 0;

do {
    console.log(value + '번째');
    value++;
} while(value < 2)
```
```
0번째1번째
```

## for문
---
```javascript
for (초기식; 조건식; 종결식) {
  문장
}
```
```javascript
var array = ['포도', '사과', '바나나', '망고'];

for (i=0; i<array.length; i++) {
    console.log(array[i]);
}
```
```
'포도사과바나나망고'
```

## for in 문
---
```javascript
for (변수 in 객체/배열)
```
```javascript
var array = ['포도', '사과', '바나나', '망고'];

for (i in array) {
    console.log(array[i]);
}
```
```
'포도사과바나나망고'
```

## 중첩 반복문
---
```javascript
var output = '';

for (i=1; i<10; i++) {
    for (j=1; j<=i; j++) {
        output += '*';
    }
    output += '<br/>';
}

document.write(output);
```
```
*
**
***
****
*****
******
*******
********
*********
```

## break
---
break문은 코드 블록을 탈출한다.
```javascript
for (var i = 0; true; i++) {
    console.log(i + '번째 반복문입니다.' + '<br/>');
    
    if(i == 3) {
        break;
    }
}
```            
```
0번째 반복문입니다. 
1번째 반복문입니다. 
2번째 반복문입니다. 
3번째 반복문입니다.
```

## continue
---
continue문은 코드 블록의 실행 시점을 현 시점에서 중단하고 반복문으로 이동한다.
```javascript
var output = 0;
for (var i = 0; i <= 10; i++) {
    if(i % 2 == 1) {
        continue;
    }
    output += i;
}

console.log(output); // 1부터 10까지 수 중에서 짝수들의 합
```
```
30
```