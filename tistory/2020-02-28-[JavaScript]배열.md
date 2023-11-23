---
layout: post
title: "[JavaScript] 배열"
category: [JavaScript]

---
<br>

`배열`에 대해 알아보자
<!-- more -->

<hr>



# 배열
---
배열은 여러 개의 값을 순차적으로 저장할 때 사용한다. 자바스크립트의 배열은 객체이다.
- `대괄호[]`를 사용하여 표현하며 어떤 종류의 자료형도 배열의 요소가 될 수 있다.  
- 배열의 인덱스를 통해 값을 확인할 수 있다.

## 생성
---
배열을 만드는 방법은 다음과 같이 2가지 방법이 있다.
- 배열 리터럴
- Array() 생성자 함수

### 배열 리터럴
---
```javascript
var array = [273, 'String', true, function() {}, {}, [1,2]]

console.log(array[0]);   // 273
console.log(array[1]);   // 'String'
console.log(array[2]);   // true
console.log(array[3]);   // function() { }
console.log(array[4]);   // [object Object]
console.log(array[5]);   // [1, 2]
console.log(array.length);   // 6
```

### Array() 생성자 함수
---
매개변수가 숫자이면서 1개인 경우, 매개변수 값을 length로 하는 빈 배열이 생성된다.  
그 외의 경우는 매개변수로 전달된 값을 요소로 가지는 배열이 생성된다.
```javascript
var arr = new Array('arr1');
console.log(arr);   // ['arr1']

var arr = new Array('arr1', 'arr2', 'arr3');
console.log(arr);   // ['arr1', 'arr2', 'arr3']

var arr = new Array(2);
console.log(arr);   // [,]

var arr = new Array(1,2,3);
console.log(arr);   // [1, 2, 3]
```

## 요소 추가/삭제
---
인덱스를 사용하여 동적으로 요소를 추가할 수 있다. 단, 인덱스 순서에 맞게 추가할 필요 없이 필요한 위치에 값을 할당하여 추가할 수 있다. 배열의 길이는 마지막 인덱스를 기준으로 정해진다.
```javascript
var arr = [];
arr[1] = 1;
arr[4] = 4;

console.loge(arr[0])   // undefined
console.log(arr);   // [, 1, , , 4]
console.log(arr.length);   // 5
```

요소를 삭제할 때에는 `delete` 연산자를 이용한다. 이 때 배열의 length에는 변함이 없다. 요소를 완전히 삭제(length 반영)하기 위해서는 `splice` 메소드를 사용한다.

```javascript
var arr = [1,2,3,4,5];

console.log(arr);   // [1, 2, 3, 4, 5]
console.log(arr.length);   // 5

delete arr[0];
console.log(arr);   // [, 2, 3, 4, 5]
console.log(arr.length);   // 5
```

## 요소 접근
---
인덱스를 통해 배열의 요소 값을 가져올 수 있다.
```javascript
function get_member() {
    return ['yang', 'sang', 'gil'];
}

var member;
member = get_member();

for(i=0; i<member.length; i++) {
    console.log(member[i].toUpperCase());
}
```
```
YANG
SANG
GIl
```

## 배열 프로퍼티
---
기본적으로 제공되는 배열 프로퍼티이다.

### length
---
요소의 개수(배열의 길이)를 의미한다.

```javascript
var array = ['a', 'b', 'c', 'd', 'e'];
console.log(array.length);  // 5
```

## 함수
---
기본적으로 제공되는 배열 함수들이다.

### isArray(x)
---
`x`가 배열이면 `true`, 배열이 아니면 `false`를 반환한다.

```javascript
Array.isArray([]);   // true
Array.isArray(['a', 'b']);   // true

Array.isArray();   // false
Array.isArray({});   // false
Array.isArray('string');   // false
Array.isArray(1);   // false
```

### from(x)
---
반복 가능한 값 `x`(문자열, 배열 등)를 배열로 변환하여 반환한다.

```javascript
console.log(Array.from('hello'));   // ['h', 'e', 'l', 'l', 'o']
console.log(Array.from([1,2,3]));   // [1, 2, 3]
```

### of(x)
---
`x`로 새로운 배열을 생성하여 반환한다.

```javascript
console.log(Array.of('h'));   // ['h']
console.log(Array.of(1,2,3));   // [1, 2, 3]
```

### indexOf(x)
---
`x` 요소에 해당하는 인덱스를 반환한다. 중복되는 요소가 있을 경우 첫 번째 인덱스만 반환하며 해당 요소가 없는 경우 -1을 반환한다.

```javascript
var arr = ['a','b','c','d','d'];

// a 요소의 인덱스(0)
console.log(arr.indexOf('a'));   // 0

// z 요소의 인덱스 => z 요소가 없으므로 -1
console.log(arr.indexOf('z'));   // -1

// d 요소의 인덱스(3)
console.log(arr.indexOf('d'));   // 3
```

### concat(x)
---
`x` 값을 자신의 복사본에 추가하고 반환한다. 원본 배열은 변경되지 않는다.

```javascript
var a = ['a', 'b', 'c'];
var b = a.concat(['d', 'e']);
console.log(b);   // ['a', 'b', 'c', 'd', 'e']

var c = a.concat(['f', 'g']);
console.log(c);   // ['a', 'b', 'c', 'f', 'g']

console.log(a);   // ['a', 'b', 'c']
```

### join(x)
---
배열 요소 사이에 `x`를 연결하여 문자열을 반환한다. `x`는 생략 가능하며 기본자는 `,`이다.

```javascript
var arr = ['a', 'b', 'c', 'd'];
var a = arr.join();
console.log(a);   // 'a,b,c,d'

var b = arr.join('');
console.log(b);   // 'abcd'

var c = arr.join('^');
console.log(C)   // 'a^b^c^d'
```

### push(x)
---
`x` 값을 배열의 마지막 요소로 추가하며 반환값은 새로운 배열의 `length`이다. 원본 배열을 변경한다.

```javascript
var arr = ['a', 'b', 'c', 'd', 'e'];
var ar = [1, 2, 3];

var a = arr.push('f');
console.log(a);   // 6
console.log(arr);   // ['a', 'b', 'c', 'd', 'e', 'f];

var b = arr.push(ar);
console.log(b);   // 7
console.log(arr);   // ['a', 'b', 'c', 'd', 'e', 'f', [1, 2, 3]];
```

### pop()
---
배열에서 마지막 요소를 제거하고 제거한 요소를 반환한다. 빈 배열일 경우 `undefined`를 반환한다. 원본 배열을 변경한다.

```javascript
var arr = ['a', 'b', 'c', 'd', 'e'];

var a = arr.pop();
console.log(arr);   // ['a', 'b', 'c', 'd']
console.log(a);   // 'e'
```

### unshift(x)
---
`x` 값을 배열의 처음 요소로 추가하며 반환값은 새로운 배열의 `length`이다. 원본 배열을 변경한다.

```javascript
var arr = ['a', 'b', 'c', 'd', 'e'];

var a = arr.unshift(1);
console.log(a);   // 6
console.log(arr);   // [1, 'a', 'b', 'c', 'd', 'e']
```

### shift()
---
배열에서 처음 요소를 제거하고 제거한 요소를 반환한다. 빈 배열일 경우 `undefined`를 반환한다. 원본 배열을 변경한다.

```javascript
var arr = ['a', 'b', 'c', 'd', 'e'];

var a = arr.shift();
console.log(arr);   // ['b', 'c', 'd', 'e']
console.log(a);   // 'a'
```

### reverse()
---
배열 요소의 순서를 반대로 변경하며 반환값은 새로운 배열이다. 원본 배열을 변경한다.

```javascript
var a = [1, 2, 3];

var b = a.reverse();
console.log(a);   // [3, 2, 1]
console.log(b);   // [3, 2, 1]
```

### slice(start, end)
---
인수로 지정된 배열의 부분을 복사(배열[start] ~ 배열[end-1])하여 반환하며 인수의 기본값은 `start=0, end=this.length`이다. 원본 배열은 변경되지 않는다. 
- start : 음수인 경우 배열의 끝에서의 인덱스를 의미한다.

```javascript
var arr = ['a', 'b', 'c', 'd', 'e'];

// arr[0]부터 arr[1]까지 반환
var a = arr.slice(0, 2);
console.log(a);   // ['a', 'b']

// arr[2]부터 끝까지 반환
a = arr.slice(2);
console.log(a);   // ['c', 'd', 'e']

// arr[1]부터 arr[2]까지 반환
a = arr.slice(1, 3);
console.log(a);   // ['b', 'c']

// 배열의 끝에서 요소 반환
a = arr.slice(-2);
console.log(a);   // ['d', 'e']

// 모든 요소 반환
a = arr.slice();
console.log(a);   // ['a', 'b', 'c', 'd', 'e']
```

### splice(start, deleteCount, value)
---
기존 배열의 요소를 제거하고 그 위치에 새로운 요소를 추가한다. 또한 배열 중간에 새로운 요소를 추가할때 사용된다. 반환값은 삭제한 요소들을 가진 배열이다. 원본 배열을 변경한다.
- start : 배열의 시작위치이다.(배열[start])
- deleteCount : start부터 제거할 요소의 수이며 0일 경우 요소를 제거하지 않는다.
- value : 삭제한 위치에 추가될 요소이다.

배열의 요소를 삭제하는 경우는 다음과 같다.
```javascript
var arr = [1, 2, 3, 4, 5, 6];

// arr[1]부터 2개 요소 제거 후 반환
var a = arr.splice(1, 2);
console.log(a);   // [2, 3]
console.log(arr);   // [1, 4, 5, 6]

var arr = [1, 2, 3, 4, 5, 6];

// arr[1]부터 모든 요소 제거 후 반환
var a = arr.splice(1);
console.log(a);   // [2, 3, 4, 5, 6]
console.log(arr);   // [1
```

배열의 요소를 삭제한 후 그 위치에 새로운 요소를 추가하는 경우는 다음과 같다.
```javascript
var arr = [1, 2, 3, 4, 5, 6];

// arr[1]부터 1개 요소 제거 후 반환 및 제거 위치에 새로운 요소(10, 11) 추가
var a = arr.splice(1, 1, 10, 11);
console.log(a);   // [2]
console.log(arr);   // [1, 10, 11, 3, 4, 5, 6]
```

배열 중간에 새로운 요소를 추가하는 경우는 다음과 같다.
```javascript
var arr = [1, 2, 3, 4, 5, 6];

// arr[2]부터 0개 제거 후 반환 및 제거 위치에 새로운 요소(100) 추가
// => arr[2] 자리에 새로운 요소 추가 
var a = arr.splice(2, 0, 100);
console.log(a);   // []
console.log(arr);   // [1, 2, 100, 3, 4, 5, 6]
```

### sort()
---
배열의 요소를 정렬하며 반환값은 새로운 배열이다. 원본 배열을 변경한다.

```javascript
var arr = [2, 1, 'b', 3, 4, 'a'];

var a = arr.sort();
console.log(a);   // [1, 2, 3, 4, 'a', 'b']
console.log(arr);   // [1, 2, 3, 4, 'a', 'b']
```


