## Rest 파라미터

`Rest 파라미터` 는 매개변수 이름 앞에 세개의 점 `...`을 붙여서 정의한 매개변수를 의미한다. `Rest 파라미터` 는 함수에 전달된 인수들의 목록을 배열로 전달받으며 순차적으로 할당된다.

```javascript
function foo(...rest) {
  console.log(Array.isArray(rest));  // true
  console.log(rest);  // [ 1, 2, 3, 4, 5 ]
}

foo(1, 2, 3, 4, 5);
```

<br>

```javascript
function foo(param, ...rest) {
  console.log(param);  // 1
  console.log(rest);   // [ 2, 3, 4, 5 ]
}
foo(1, 2, 3, 4, 5);


function bar(param1, param2, ...rest) {
  console.log(param1);  // 1
  console.log(param2);  // 2
  console.log(rest);    // [ 3, 4, 5 ]
}

bar(1, 2, 3, 4, 5);
```

<br>

또한, `Rest 파라미터` 는 반드시 마지막 파라미터여야 한다.

```javascript
function foo( ...rest, param1, param2) { }

foo(1, 2, 3, 4, 5);
// SyntaxError
```

<br>

`Rest 파라미터` 는 length에 영향을 주지 않는다.

```javascript
function foo(...rest) {}

console.log(foo.length);  // 0
```

<br>

