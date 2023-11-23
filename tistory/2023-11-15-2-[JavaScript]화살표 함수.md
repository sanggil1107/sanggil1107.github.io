## 화살표 함수

`화살표 함수(Arrow function)` 는 function 키워드 대신 화살표(=>)를 사용하여 보다 간략한 방법으로 함수를 선언할 수 있다. 하지만 모든 경우 화살표 함수를 사용할 수 있는 것은 아니며 화살표 함수의 기본 문법은 아래와 같다.


```javascript
// 매개변수 지정 방법
    () => { ... }  // 매개변수가 없을 경우
     x => { ... }  // 매개변수가 한 개인 경우, 소괄호를 생략할 수 있다.
(x, y) => { ... }  // 매개변수가 여러 개인 경우, 소괄호를 생략할 수 없다.

// 함수 몸체 지정 방법
x => { return x * x }  // single line block
x => x * x             // 함수 몸체가 한줄의 구문이라면 중괄호를 생략할 수 있으며 암묵적으로 return된다. 위 표현과 동일하다.

() => { return { a: 1 }; }
() => ({ a: 1 })  // 위 표현과 동일하다. 객체 반환시 소괄호를 사용한다.

() => {           // multi line block.
  const x = 10;
  return x * x;
};
```

<br>

### 화살표 함수 호출
---

`화살표 함수` 는 익명 함수로만 사용할 수 있다.

```javascript
// ES5
var pow = function (x) { return x * x; };
console.log(pow(10));  // 100


// ES6
const pow = x => x * x;
console.log(pow(10));  // 100
```

<br>

```javascript
// ES5
var fruit = function (apple, pear) {
  var cart = apple * pear;
  return cart;
};
console.log(fruit(10, 20));  // 200


// ES6
let fruit = (apple, pear) => {
  return apple * pear;
};
console.log(fruit(10, 20));  // 200
```

<br>

### 화살표 함수의 this
---

`화살표 함수` 는 함수를 선언할 때 this에 바인딩할 객체가 정적으로 결정된다. 동적으로 결정되는 일반 함수와는 달리 화살표 함수의 this 언제나 상위 스코프의 this를 가리킨다. 

```javascript
function Prefixer(prefix) {
  this.prefix = prefix;
}

Prefixer.prototype.prefixArray = function (arr) {
    // this는 상위 스코프인 prefixArray 메소드 내의 this를 가리킨다.
    return arr.map(x => `${this.prefix}  ${x}`);
};

const pre = new Prefixer('Hi');
console.log(pre.prefixArray(['Lee', 'Kim']));
```

<br>

### 화살표 함수를 사용해서는 안되는 경우
---

#### 메소드

메소드로 정의한 화살표 함수 내부의 this는 메소드를 소유한 객체, 즉 메소드를 호출한 객체를 가리키지 않고 상위 컨택스트인 전역 객체 window를 가리킨다. 따라서 `화살표 함수` 로 메소드를 정의하는 것은 바람직하지 않다.

```javascript
const person = {
  name: 'Lee',
  sayHi: () => console.log(`Hi ${this.name}`)
};

person.sayHi();  // Hi undefined
```

<br>

#### 생성자 함수

`화살표 함수` 는 생성자 함수로 사용할 수 없다. 생성자 함수는 prototype 프로퍼티를 가지며 prototype 프로퍼티가 가리키는 프로토타입 객체의 constructor를 사용한다. 하지만 화살표 함수는 prototype 프로퍼티를 가지고 있지 않다.

```javascript
const Foo = () => {};

// 화살표 함수는 prototype 프로퍼티가 없다
console.log(Foo.hasOwnProperty('prototype'));  // false

const foo = new Foo();  // TypeError=
```