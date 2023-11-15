## ECMAScript

ECMA스크립트란, ECMA International이 ECMA-262 기술 규격에 따라 정의하고 있는 표준화된 스크립트 프로그래밍 언어를 말한다.

ES6(ECMAScript 2015)에서 추가된 사항에 대해 알아보고자 한다.


<br>

### let
---

기존에는 변수를 선언하기 위해 `var` 키워드를 사용하였으나 블록 레벨 스코프를 따르는 변수를 선언하기 위해 `let` 키워드를 제공한다.

- 함수 레벨 스코프
함수 내에서 선언된 변수는 함수 내에서만 유효하며 함수 외부에서는 참조할 수 없다. 즉, 함수 내부에서 선언한 변수는 지역 변수이며 함수 외부에서 선언한 변수는 모두 전역 변수이다.

- 블록 레벨 스코프
모든 코드 블록(함수, if 문, for 문, while 문, try/catch 문 등) 내에서 선언된 변수는 코드 블록 내에서만 유효하며 코드 블록 외부에서는 참조할 수 없다. 즉, 코드 블록 내부에서 선언한 변수는 지역 변수이다.

```javascript
function fruit() {
  if (true) {
    var pear = 1;
    let apple = 2;
  }

  console.log(pear);  // 출력 1
  console.log(apple);  // if 문 안에서만 접근 가능하므로 reference 에러 발생
}
```

<br>

또한, `var` 키워드는 중복 선언이 가능했으나 `let` 키워드는 중복 선언이 불가능하다.

```javascript
var foo = 123;
var foo = 456;  // 중복 선언 허용

let bar = 123;
let bar = 456;  // Uncaught SyntaxError
```

<br>

### const
---

`const` 는 상수(변하지 않는 값)를 선언하기 위해 사용하며 블록 레벨 스코프를 갖는다.

```javascript
function fruit() {
  if (true) {
    var pear = 1;
    const apple = 2;
  }

  console.log(pear);  // 출력 1
  console.log(apple);  // if 문 안에서만 접근 가능하므로 reference 에러 발생
}
```

<br>

또한, 재할당이 불가능하며 선언과 동시에 할당이 이루어져야한다.

```javascript
const FOO = 123;

FOO = 456;  // TypeError: Assignment to constant variable.
```

<br>

```javascript
const FOO;  // SyntaxError
```

