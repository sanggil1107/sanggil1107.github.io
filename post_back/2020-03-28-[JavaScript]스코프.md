
# 스코프
---
스코프(유효 범위)란 참조 대상 식별자를 찾아내기 위한 규칙을 말하며, 식별자는 선언 위치에 따라 해당 스코프를 가지게 된다.

## 구분
---
자바스크립트에서 크게 전역/지역 스코프로 나눌 수 있다.  
- 전역 스코프
: 코드 어디에서든지 참조 가능

- 지역 스코프(함수 레벨 스코프)
: 함수 코드 블록이 만든 스코프로 함수 내부에서만 참조 가능

## 특징
---
자바 스크립트는 함수 레벨 스코프(function-level scope)를 따른다.
- 블록 레벨 스코프(block-level scope)
: 코드 블록({..})내에서 유효한 스코프를 의미한다.

- 함수 레벨 스코프(function-level scope)
: 함수 코드 블록 내에서 유효한 스코프를 의미한다. 즉, 함수 코드 블록 내에서 선언된 변수는 함수 내에서만 유효하고 함수 외부에서는 유효하지 않다.(참조 불가능)

## 전역 스코프
---
전역에 선언된 변수를 `전역변수`라 하며 어디서든 참조할 수 있는 전역 스코프를 가진다. `var` 키워드로 선언한다.

```javascript
var vscope = 'global';

function fscope() {
    console.log(vscope);
}

fscope();   // 'global'
console.log(vscope);   // 'global'
```

아래의 경우, 변수 vscope는 코드 블록({...}) 내에서 선언되었지만 자바스크립트는 함수 레벨 스코프를 따르므로 함수 내부가 아닌 코드 블록내에 선언된 변수도 전역 스코프를 가지게 되는 전역 변수이다. 

```javascript
var vscope = 'global';

{
    var vscope = 'block';
    console.log(vscope);   // 'block'
}

console.log(vscope);   // 'block'
```

if문과 for문 등에서 사용되는 변수는 함수 내부가 아닌 코드 블록내에 선언된 변수이므로 전역 변수이다.

```javascript
function a() {
    var i = 0;   // 지역 변수
}

for(var i=0; i<5; i++) {   // 전역변수
    a();
    console.log(i);   // 0 1 2 3 4
}

console.log(i);   // 5
```

## 지역 스코프
---
함수 내부에 `var`로 선언된 변수는 함수 내부에서만 유효하게 되며 `지역 변수`라 한다.  

```javascript
var vscope = 'global';

function fscope() {
    var vscope = 'local';
    console.log(vscope);
}
fscope();   // 'local'
```

아래의 경우, 함수 내부에서 동일한 이름의 변수를 선언하고 값을 할당했지만(지역 변수) 함수 외부에서 변수를 호출하므로 전역 변수가 호출된다.

```javascript
var vscope = 'global';

function fscope() {
    var vscope = 'local';
}
fscope(); 
console.log(vscope);   // 'global'
```

다음과 같이 함수 내부에서 `var` 키워드를 선언하지 않고 사용하는 변수는 전역 변수가 된다.

```javascript
var vscope = 'global';

function fscope() {
    vscope = 'local';   // var가 없다면 전역변수
    test = 'global test';   // var가 없다면 전역변수
}
fscope();
console.log(vscope);   // 'local'
console.log(test);   // 'global test'
```

따라서 아래의 경우 전역 변수 i 값은 계속 0으로 초기화되므로 무한루프가 된다.

```javascript
function a() {
    i = 0;   // 전역변수
}

for(var i=0; i<5; i++) {   // 전역변수
    a();
    console.log(i);
}
```     

자바스크립트에서는 함수 내에 `var` 키워드로 선언된 변수만 지역 변수가 된다.

## 렉시컬 스코프
---
렉시컬 스코프는 함수 호출 시점이 아닌 선언 시점에 따라 결정된다. 즉, 함수 선언 시점에 상위 스코프가 결정된다. (함수 호출 시점에 따라 결정되는 것을 동적 스코프라 한다.)  

아래 b 함수는 전역에 선언되었으므로 b의 상위 스코프는 전역 스코프이며 따라서, 전역 변수 i의 값을 출력하게 된다.

```javascript
var i = 5;   // 전역변수
            
function a() {
    var i = 10;   // 지역변수
    b();
}

function b() {
    console.log(i);   // 전역 스코프에 함수가 선언되었으므로 전역 변수 i를 출력한다.
}

a();   // 5
b();   // 5
```
