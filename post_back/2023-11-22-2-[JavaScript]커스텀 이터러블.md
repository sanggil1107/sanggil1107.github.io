## 커스텀 이터러블

일반 객체는 이터레이션 프로토콜을 준수(Symbol.iterator 메소드를 소유)하지 않기 때문에 이터러블이 아니다. 따라서 일반 객체는 for…of 문에서 순회할 수 없으며 Spread 문법의 대상으로 사용할 수도 없다. 하지만 일반 객체도 이터러블 프로토콜을 준수하도록 구현하면 이터러블이 되는데 이를 `커스텀 이터러블` 이라고 한다.

```javascript
const fibonacci = {
  // Symbol.iterator 메소드를 구현하여 이터러블 프로토콜을 준수
  [Symbol.iterator]() {
    let [pre, cur] = [0, 1];
    // 최대값
    const max = 10;

    // Symbol.iterator 메소드는 next 메소드를 소유한 이터레이터를 반환해야 한다.
    // next 메소드는 이터레이터 리절트 객체를 반환
    return {
      // fibonacci 객체를 순회할 때마다 next 메소드가 호출된다.
      next() {
        [pre, cur] = [cur, pre + cur];
        return {
          value: cur,
          done: cur >= max
        };
      }
    };
  }
};

// 이터러블의 최대값을 외부에서 전달할 수 없다.
for (const num of fibonacci) {
  // for...of 내부에서 break는 가능하다.
  // if (num >= 10) break;
  console.log(num);  // 1 2 3 5 8
}
```

<br>

```javascript
// spread 문법과 디스트럭처링을 사용하면 이터러블을 손쉽게 배열로 변환할 수 있다.
// spread 문법
const arr = [...fibonacci];
console.log(arr);  // [ 1, 2, 3, 5, 8 ]

// 디스트럭처링
const [first, second, ...rest] = fibonacci;
console.log(first, second, rest);  // 1 2 [ 3, 5, 8 ]
```

<br>

### 이터러블을 생성하는 함수
---

이터러블을 반환하는 함수는 다음과 같다.

```javascript
// 이터러블을 반환하는 함수
const fibonacciFunc = function (max) {
  let [pre, cur] = [0, 1];

  return {
    // Symbol.iterator 메소드를 구현하여 이터러블 프로토콜을 준수
    [Symbol.iterator]() {
      // Symbol.iterator 메소드는 next 메소드를 소유한 이터레이터를 반환해야 한다.
      // next 메소드는 이터레이터 리절트 객체를 반환
      return {
        // fibonacci 객체를 순회할 때마다 next 메소드가 호출된다.
        next() {
          [pre, cur] = [cur, pre + cur];
          return {
            value: cur,
            done: cur >= max
          };
        }
      };
    }
  };
};

// 이터러블을 반환하는 함수에 이터러블의 최대값을 전달한다.
for (const num of fibonacciFunc(10)) {
  console.log(num);  // 1 2 3 5 8
}
```

<br>

### 이터러블이면서 이터레이터인 객체를 생성하는 함수
---

이터러블이면서 이터레이터인 객체를 생성하면 Symbol.iterator 메소드를 호출하지 않아도 된다.

```javascript
// 이터러블이면서 이터레이터인 객체를 반환하는 함수
const fibonacciFunc = function (max) {
  let [pre, cur] = [0, 1];

  // Symbol.iterator 메소드와 next 메소드를 소유한
  // 이터러블이면서 이터레이터인 객체를 반환
  return {
    // Symbol.iterator 메소드
    [Symbol.iterator]() {
      return this;
    },
    // next 메소드는 이터레이터 리절트 객체를 반환
    next() {
      [pre, cur] = [cur, pre + cur];
      return {
        value: cur,
        done: cur >= max
      };
    }
  };
};

// iter는 이터러블이면서 이터레이터이다.
let iter = fibonacciFunc(10);

// iter는 이터레이터이다.
console.log(iter.next());  // {value: 1, done: false}
console.log(iter.next());  // {value: 2, done: false}
console.log(iter.next());  // {value: 3, done: false}
console.log(iter.next());  // {value: 5, done: false}
console.log(iter.next());  // {value: 8, done: false}
console.log(iter.next());  // {value: 13, done: true}

iter = fibonacciFunc(10);

// iter는 이터러블이다.
for (const num of iter) {
  console.log(num);  // 1 2 3 5 8
}
```