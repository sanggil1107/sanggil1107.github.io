## 디스트럭처링

`디스트럭처링(Destructuring)` 은 구조화된 배열 또는 객체를 Destructuring(비구조화, 파괴)하여 개별적인 변수에 할당하는 것이다. 배열 또는 객체 리터럴에서 필요한 값만을 추출하여 변수에 할당한다.

<br>

### 배열 디스트럭처링
---

배열의 각 요소를 추출하여 변수 리스트에 할당하며 배열의 인덱스를 기준으로 한다.

```javascript
const arar = [1, 2, 3];

const [num1, num2, num3] = arr;

console.long(num1, num2, num3);  // 1 2 3
```

<br>

```javascript
const [a, b] = [1];
console.log(a, b)  // 1 undefined

const [a, b] = [1, 2, 3];
console.log(a, b);  // 1 2

const [a, b= 10, c =3] = [1,2];
console.log(a, b, c);  // 1 2 3
```

<br>

### 객체 디스트럭처링
---

객체의 각 프로퍼티를 추출하여 변수 리스트에 할당하며 프로퍼티 이름(키)을 기준으로 한다.

```javascript
const name = { first: 'Sanggil', last: 'Yang' };

const { first, last } = name;

console.log(first, last);  // Sanggil Yang
```

<br>

```javascript
const { first = 'Sanggil', last } = { last: 'Yang' };
console.log(first, last);  // Sanggil Yang

const { first: fn = 'Sanggil', last: ln } = { last: 'Yang' };
console.log(fn, ln);  // Sanggil Yang

const { prop1, prop2 } = { prop1: 'a', prop2: 'b' };
console.log({ prop1, prop2 });  // { prop1: 'a', prop2: 'b' }
```

<br>

또한, 키로 값을 추출할 수 있다.

```javascript
const todo = { id: 1, content: 'HTML', completed: true };

// todo 객체로부터 id 프로퍼티만 추출한다.
const { id } = todo;

console.log(id);  // 1
```

<br>

중첩 객체는 아래와 같이 사용한다.

```javascript
const person = {
  name: 'Lee',
  address: {
    zipCode: '03068',
    city: 'Seoul'
  }
};

// address 프로퍼티 키로 객체를 추출하고 이 객체의 city 프로퍼티 키로 값을 추출한다.
const { address: { city } } = person;
console.log(city);  // 'Seoul'
```