## 이터레이션

`이터레이션` 이란 데이터 컬렉션을 순회하기 위한 프로토콜이다. 이터레이션을 준수한 객체는 for of 문으로 순회할 수 이쏘 Spread 문법의 피연산자가 될 수 있다.

<br>

### 이터러블
---

이터러블 프로토콜을 준수한 객체를 `이터러블` 이라 한다. `이터러블` 은 Symbol.iterator 메소드를 구현하거나 프로토타입 체인에 의해 상속한 객체를 말한다. Symbol.iterator 메소드는 이터레이터를 반환한다. `이터러블` 은 for of 문에서 순회할 수 있으며 Spread 문법의 대상으로 사용할 수 있다.

배열은 이터러블 프로토콜을 준수한 이터러블이다.

```javascript
const array = [1, 2, 3];

// 배열은 Symbol.iterator 메소드를 소유한다.
// 따라서 배열은 이터러블 프로토콜을 준수한 이터러블이다.
console.log(Symbol.iterator in array); // true

// 이터러블 프로토콜을 준수한 배열은 for...of 문에서 순회 가능하다.
for (const item of array) {
  console.log(item);
}
```

<br>

일반 객체는 이터러블 프로토콜을 준수한 이터러블이 아니다.

```javascript
const obj = { a: 1, b: 2 };

// 일반 객체는 Symbol.iterator 메소드를 소유하지 않는다.
// 따라서 일반 객체는 이터러블 프로토콜을 준수한 이터러블이 아니다.
console.log(Symbol.iterator in obj);  // false

// 이터러블이 아닌 일반 객체는 for...of 문에서 순회할 수 없다.
// TypeError: obj is not iterable
for (const p of obj) {
  console.log(p);
}
```

<br>

### 이터레이터
---

`이터레이터`  프로토콜은 next 메소드를 소유하며 next 메소드를 호출하면 이터러블을 순회하며 value, done 프로퍼티를 갖는 이터레이터 리절트 객체를 반환하는 것이다. 이 규약을 준수한 객체가 `이터레이터` 이다.

```javascript
// 배열은 이터러블 프로토콜을 준수한 이터러블이다.
const array = [1, 2, 3];

// Symbol.iterator 메소드는 이터레이터를 반환한다.
const iterator = array[Symbol.iterator]();

// 이터레이터 프로토콜을 준수한 이터레이터는 next 메소드를 갖는다.
console.log('next' in iterator);  // true
```

<br>

이터레이터의 next 메소드를 호출하면 value, done 프로퍼티를 갖는 이터레이터 리절트(iterator result) 객체를 반환한다.


```javascript
// 배열은 이터러블 프로토콜을 준수한 이터러블이다.
const array = [1, 2, 3];

// Symbol.iterator 메소드는 이터레이터를 반환한다.
const iterator = array[Symbol.iterator]();

// 이터레이터 프로토콜을 준수한 이터레이터는 next 메소드를 갖는다.
console.log('next' in iterator);  // true

// 이터레이터의 next 메소드를 호출하면 value, done 프로퍼티를 갖는 이터레이터 리절트 객체를 반환한다.
let iteratorResult = iterator.next();
console.log(iteratorResult);  // {value: 1, done: false}
```

<br>

### 빌트인 이터러블
---

`빌트인 이터러블` 이란 이미 제공되는 이터러블로 Array, String, Map, Set 등이 있다.

```javascript
// 배열은 이터러블이다.
const array = [1, 2, 3];

// 이터러블은 Symbol.iterator 메소드를 소유한다.
// Symbol.iterator 메소드는 이터레이터를 반환한다.
let iter = array[Symbol.iterator]();

// 이터레이터는 next 메소드를 소유한다.
// next 메소드는 이터레이터 리절트 객체를 반환한다.
console.log(iter.next());  // {value: 1, done: false}
console.log(iter.next());  // {value: 2, done: false}
console.log(iter.next());  // {value: 3, done: false}
console.log(iter.next());  // {value: undefined, done: true}

// 이터러블은 for...of 문으로 순회 가능하다.
for (const item of array) {
  console.log(item);
}

// 문자열은 이터러블이다.
const string = 'hi';

// 이터러블은 Symbol.iterator 메소드를 소유한다.
// Symbol.iterator 메소드는 이터레이터를 반환한다.
iter = string[Symbol.iterator]();

// 이터레이터는 next 메소드를 소유한다.
// next 메소드는 이터레이터 리절트 객체를 반환한다.
console.log(iter.next());  // {value: "h", done: false}
console.log(iter.next());  // {value: "i", done: false}
console.log(iter.next());  // {value: undefined, done: true}

// 이터러블은 for...of 문으로 순회 가능하다.
for (const letter of string) {
  console.log(letter);
}

// arguments 객체는 이터러블이다.
(function () {
  // 이터러블은 Symbol.iterator 메소드를 소유한다.
  // Symbol.iterator 메소드는 이터레이터를 반환한다.
  iter = arguments[Symbol.iterator]();

  // 이터레이터는 next 메소드를 소유한다.
  // next 메소드는 이터레이터 리절트 객체를 반환한다.
  console.log(iter.next());  // {value: 1, done: false}
  console.log(iter.next());  // {value: 2, done: false}
  console.log(iter.next());  // {value: undefined, done: true}

  // 이터러블은 for...of 문으로 순회 가능하다.
  for (const arg of arguments) {
    console.log(arg);
  }
}(1, 2));
```

<br>

이터레이션 프로토콜은 다양한 데이터 소스가 하나의 순회 방식을 갖도록 규정하여 데이터 소비자가 효율적으로 다양한 데이터 소스를 사용할 수 있도록 데이터 소비자와 데이터 소스를 연결하는 인터페이스의 역할을 한다.