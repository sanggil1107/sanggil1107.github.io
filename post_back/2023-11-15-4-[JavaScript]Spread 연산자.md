## Sptread 연산자

`Spread 연산자(Spread Syntax, ...)` 는 대상을 개별 요소로 분리하며 대상은 Iterable 이어야한다.

```javascript
// ...[1, 2, 3]는 [1, 2, 3]을 개별 요소로 분리한다(→ 1, 2, 3)
console.log(...[1, 2, 3]);  // 1, 2, 3

// 문자열은 이터러블이다.
console.log(...'Hello');  // H e l l o

// Map과 Set은 이터러블이다.
console.log(...new Map([['a', '1'], ['b', '2']]));  // [ 'a', '1' ] [ 'b', '2' ]
console.log(...new Set([1, 2, 3]));  // 1 2 3
```

<br>

#### 함수의 인수로 사용

ES6의 Spread 연사자(`…`)을 사용한 배열을 인수로 함수에 전달하면 배열의 요소를 분해하여 순차적으로 파라미터에 할당한다.

```javascript
function foo(x, y, z) {
  console.log(x);  // 1
  console.log(y);  // 2
  console.log(z);  // 3
}

const arr = [1, 2, 3];

// spread 문법에 의해 분리된 배열의 요소는 개별적인 인자로서 각각의 매개변수에 전달된다.
foo(...arr);
```

<br>

```javascript
function bar(x, y, z) {
  console.log(x);  // 1
  console.log(y);  // 2
  console.log(z);  // 3
}

// spread 문법에 의해 분리된 배열의 요소는 개별적인 인자로서 각각의 매개변수에 전달된다.
bar(...[1, 2, 3]);
```

<br>

Rest 파라미터는 반드시 마지막 파라미터이어야 하지만 `Spread 연산자` 를 사용한 인수는 자유롭게 사용할 수 있다.

<br>

```javascript
function foo(v, w, x, y, z) {
  console.log(v);  // 1
  console.log(w);  // 2
  console.log(x);  // 3
  console.log(y);  // 4
  console.log(z);  // 5
}

// ...[2, 3]는 [2, 3]을 개별 요소로 분리한다(→ 2, 3)
foo(1, ...[2, 3], 4, ...[5]);
```

<br>

#### 배열에서 사용하는 경우

- concat

ES5에서 기존 배열의 요소를 새로운 배열 요소의 일부로 만들고 싶은 경우, 배열 리터럴 만으로 해결할 수 없고 concat 메소드를 사용해야 한다.

```javascript
// ES5
var arr = [1, 2, 3];
console.log(arr.concat([4, 5, 6]));  // [ 1, 2, 3, 4, 5, 6 ]
```

<br>

`Spread 연산자` 를 사용하면 배열 리터럴 만으로 기존 배열의 요소를 새로운 배열 요소의 일부로 만들 수 있다.

```javascript
const arr = [1, 2, 3];
const arr1 = [...arr, 4, 5, 6];  // ...arr은 [1, 2, 3]을 개별 요소로 분리한다

console.log(arr1);  // [ 1, 2, 3, 4, 5, 6 ]
```

<br>

- push

ES5에서 기존 배열에 다른 배열의 개별 요소를 각각 push하려면 아래와 같은 방법을 사용한다.

```javascript
// ES5
var arr1 = [1, 2, 3];
var arr2 = [4, 5, 6];

// apply 메소드의 2번째 인자는 배열. 이것은 개별 인자로 push 메소드에 전달된다.
Array.prototype.push.apply(arr1, arr2);

console.log(arr1);  // [ 1, 2, 3, 4, 5, 6 ]
```

<br>

`Spread 연산자` 를 사용하면 아래와 같이 보다 간편하게 표현할 수 있다.

```javascript
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];

// ...arr2는 [4, 5, 6]을 개별 요소로 분리한다
arr1.push(...arr2);  // == arr1.push(4, 5, 6);
console.log(arr1);  // [ 1, 2, 3, 4, 5, 6 ]


const arr3 = [1, 2, 3];
const arr4 = [4, 5, 6];
const arr5 = [...arr3, ...arr4];

console.log(arr5);  // [ 1, 2, 3, 4, 5, 6 ]
```

<br>

- splice

ES5에서 기존 배열에 다른 배열의 개별 요소를 삽입하려면 아래와 같은 방법을 사용한다.

```javascript
// ES5
var arr1 = [1, 2, 3, 6];
var arr2 = [4, 5];

Array.prototype.splice.apply(arr1, [3, 0].concat(arr2));

console.log(arr1);  // [ 1, 2, 3, 4, 5, 6 ]
```

<br>

`Spread 연산자` 를 사용하면 아래와 같이 보다 간편하게 표현할 수 있다.

```javascript
const arr1 = [1, 2, 3, 6];
const arr2 = [4, 5];

// ...arr2는 [4, 5]을 개별 요소로 분리한다
arr1.splice(3, 0, ...arr2);  // == arr1.splice(3, 0, 4, 5);

console.log(arr1);  // [ 1, 2, 3, 4, 5, 6 ]
```

<br>

- copy

ES5에서 기존 배열을 복사하기 위해서는 slice 메소드를 사용한다.

```javascript
// ES5
var arr  = [1, 2, 3];
var copy = arr.slice();

console.log(copy);  // [ 1, 2, 3 ]
```

<br>

`Spread 연산자` 를 사용하면 아래와 같이 보다 간편하게 표현할 수 있다.
이 때 각 요소를 얕은 복사하여 새로운 복사본을 생성한다.

```javascript
const arr = [1, 2, 3];
// ...arr은 [1, 2, 3]을 개별 요소로 분리한다
const copy = [...arr];

console.log(copy);  // [ 1, 2, 3 ]

console.log(arr === copy);  // false
```