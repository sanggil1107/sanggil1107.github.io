
## 변수
---
`var` 키워드를 이용하며 모든 형을 다 담을 수 있다.
```javascript
var pi, radius;
pi = 3.141592;
radius = 10;
console.log(2 * pi * radius);   // 62.83184

var x = y = 100;
console.log(x);   // 100
console.log(y);   // 100

var string = 'String';
var number = 273;
var boolean = true;
var Function = function() {};
var obejct = {};
```

### 호이스팅?
---

### var 키워드의 문제점
---
`var` 키워드로 선언된 변수는 다음과 같은 특징/문제점을 가진다.  
- 함수 레벨 스코프 : 전역변수 남발
- var 키워드 생략 : 의도하지 않은 변수의 전역화
- 중복 선언 : 의도하지 않은 변수 값 변경
- 호이스팅 : 변수 선언하기 전에 참조 가능

이러한 단점을 보완하기 위해 ES6에서는 `let` 과 `const` 키워드가 추가되었다.
