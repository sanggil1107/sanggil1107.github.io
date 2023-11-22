## for of 문

`for of 문` 은 내부적으로 이터레이터의 next 메소드를 호출하여 이터러블을 순회하며 next 메소드가 반환한 이터레이터 리절트 객체의 value 프로퍼티 값을 `for of 문` 의 변수에 할당한다. 
그리고 이터레이터 리절트 객체의 done 프로퍼티 값이 false이면 이터러블의 순회를 계속하고 true이면 이터러블의 순회를 중단한다.

```javascript
// 배열
for (const item of ['a', 'b', 'c']) {
  console.log(item);
}

// 문자열
for (const letter of 'abc') {
  console.log(letter);
}

// Map
for (const [key, value] of new Map([['a', '1'], ['b', '2'], ['c', '3']])) {
  console.log(`key : ${key} value : ${value}`);  // key : a value : 1 ...
}

// Set
for (const val of new Set([1, 2, 3])) {
  console.log(val);
}
```

<br>

`for of 문` 이 내부적으로 동작하는 것을 for 문으로 표현하면 다음과 같다.

```javascript
// 이터러블
const iterable = [1, 2, 3];

// 이터레이터
const iterator = iterable[Symbol.iterator]();

for (;;) {
  // 이터레이터의 next 메소드를 호출하여 이터러블을 순회한다.
  const res = iterator.next();

  // next 메소드가 반환하는 이터레이터 리절트 객체의 done 프로퍼티가 true가 될 때까지 반복한다.
  if (res.done) break;

  console.log(res);
}
```