## Symbol

`Symbol`은 ES6에서 새롭게 추가된 7번 째 타입으로 변경 불가능한 원시 타입이다. 주로 이름의 충돌 위험이 없는 유일한 객체의 프로퍼티 키를 만들기 위해 사용한다.

<br>

### Symbol 생성
---

`Symbol` 은 Symbol() 함수로 생성하며 new 연산자를 사용하지 않는다.

```javascript
let mySymbol = Symbol();

console.log(mySymbol);         // Symbol()
console.log(typeof mySymbol);  // symbol
```

<br>

### Symbol 사용
---

객체의 프로퍼티 키로 사용할 수 있으며 Symbol 값을 키로 갖는 프로퍼티는 다른 어떤 프로퍼티와 충돌하지 않는다.

```javascript
const obj = {};

const mySymbol = Symbol('mySymbol');
obj[mySymbol] = 123;

console.log(obj);  // { [Symbol(mySymbol)]: 123 }
console.log(obj[mySymbol]);  // 123
```

<br>

### Symbol 객체
---

Symbol() 함수로 Symbol 값을 생성할 수 있었으며 이는 Symbol이 함수 객체라는 것을 의미한다. Symbol 객체는 다양한 프로퍼티와 메소드를 가지고 있다.

<br>

#### Symbol.iterator

```javascript
// 배열에는 Array.prototype[Symbol.iterator] 메소드가 구현되어 있다.
const iterable = ['a', 'b', 'c'];

// 이터러블의 Symbol.iterator를 프로퍼티 key로 사용한 메소드는 이터레이터를 반환한다.
const iterator = iterable[Symbol.iterator]();

// 이터레이터는 순회 가능한 자료 구조인 이터러블의 요소를 탐색하기 위한 포인터로서 value, done 프로퍼티를 갖는 객체를 반환하는 next() 함수를 메소드로 갖는 객체이다. 이터레이터의 next() 메소드를 통해 이터러블 객체를 순회할 수 있다.
console.log(iterator.next());  // { value: 'a', done: false }
console.log(iterator.next());  // { value: 'b', done: false }
console.log(iterator.next());  // { value: 'c', done: false }
console.log(iterator.next());  // { value: undefined, done: true }
```

<br>

#### Symbol.for

`Symbol.for` 메소드는 인자로 전달받은 문자열을 키로 사용하여 Symbol 값들이 저장되어 있는 레지스트리에서 해당 키와 일치하는 Symbol 값을 검색한다.
만약 값이 있다면 Symbol 값을 반환하고 없다면 새로운 Symbol 값을 생성하고 레지스트리에 저장한 후 Symbol 값을 반환한다.

```javascript
// 전역 Symbol 레지스트리에 foo라는 키로 저장된 Symbol이 없으면 새로운 Symbol 생성
const s1 = Symbol.for('foo');

// 전역 Symbol 레지스트리에 foo라는 키로 저장된 Symbol이 있으면 해당 Symbol을 반환
const s2 = Symbol.for('foo');

console.log(s1 === s2);  // true
```

<br>

`Symbol.for` 메소드를 통해 생성된 Symbol 값은 반드시 키를 갖지만 Symbol 함수를 통해 생성된 Symbol 값은 키가 없다.

```javascript
const shareSymbol = Symbol.for('myKey');
const key1 = Symbol.keyFor(shareSymbol);
console.log(key1);  // myKey

const unsharedSymbol = Symbol('myKey');
const key2 = Symbol.keyFor(unsharedSymbol);
console.log(key2);  // undefined
```