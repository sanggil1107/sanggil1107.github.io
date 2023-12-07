## 콜백 함수(Callback)

`콜백(Callbakc) 함수` 란  매개변수로 함수 객체를 전달해서 호출 함수 내에서 매개변수 함수를 실행하는 것을 말한다. 그리고 파라미터로 일반적인 변수나 값을 전달하는 것이 아닌 함수 자체를 전달하며 일회용으로 사용하기 때문에 함수의 이름이 없는 익명 함수를 형태로 사용한다.

```javascript
function sayHello(name, callback) {
    const words = '이름은 ' + name + ' 입니다.';
    
    callback(words);  // 매개변수의 함수(콜백 함수) 호출
}

sayHello("sanggil", function (name) {
	console.log(name);  // 이름은 sanggil 입니다.
});
```

<br>

ES6에서 도입된 화살표 함수를 사용하여 콜백 함수를 정의할 수도 있다.

```javascript
function sayHello(callback) {
  var name = "Alice";
  callback(name);  // 콜백 함수 호출
}

// 익명 화살표 콜백 함수
sayHello((name) => {
  console.log("Hello, " + name);
});  // Hello, Alice
```

<br>

### 콜백 함수 활용
---

콜백 함수는 다양한 방식으로 사용할 수 있다.

<br>

#### 이벤트 리스너

클릭과 같은 이벤트를 처리하기 위해 등록하는 이벤트 리스너로 콜백함수가 쓰인다.

```javascript
let button = document.getElementById("button"); 

// 버튼에 클릭 이벤트 리스너를 추가
button.addEventListener("click", function () {  // 콜백 함수
  console.log("Button clicked!"); 
});
```

<br>

#### 고차 함수

forEach 메서드의 입력값으로 콜백 함수를 사용할 수 있다.

```javascript 
let numbers = [1, 2, 3, 4, 5]; 
let doubled = []; 

// numbers 배열의 각 요소에 대해 콜백 함수 실행 
numbers.forEach(function (num) { 
    doubled.push(num * 2);  // 콜백 함수로 각 요소를 두 배로 곱해서 doubled 배열에 추가 
}); 

console.log(doubled);  // [2, 4, 6, 8, 10]
```

<br>

#### Ajax

서버와 통신할 때 사용하는 fetch 메서드에서도 사용된다.

```javascript
fetch("https://jsonplaceholder.typicode.com/users")
  .then(function (response) {
    // fetch 메서드가 성공하면 콜백 함수로 response 인자를 받음
    return response.json();  // response 객체의 json 메서드를 호출하여 JSON 데이터를 반환
  })
  .then(function (data) {
    // json 메서드가 성공하면 콜백 함수로 data 인자를 받음
	console.log(data);
  })
```

<br>

#### 타이머 실행 함수

타이머 함수에서 일정 시간마다 스크립트를 실행하는 용도로서 콜백 함수를 이용한다.

```javascript
// 3000 밀리초(3초) 후에 콜백 함수 실행
setTimeout(function () {
  console.log("setTimeout");  // 콜백 함수로 콘솔에 메시지 출력
}, 3000);
```

<br>

#### 애니메이션

jQuery에서 제공하는 애니메이션 메서드들은 애니메이션이 끝난 후에 실행할 콜백 함수를 인자로 받는다.

```javascript
$("#box").slideUp(1000, function () {
  console.log("Animation completed!");  // 콜백 함수로 콘솔에 메시지 출력
});
```

<br>

### 콜백 지옥(Callback Hell)
---

`콜백 지옥` 이란 함수의 매개변수로 넘겨지는 콜백 함수가 반복되어 코드의 들여쓰기 수준이 감당하기 힘들어질 정도로 깊어지는 현상이다.
주로 이벤트 처리나 서버 통신과 같은 비동기 작업을 수행할 때 등장하며 이러한 경우, 코드의 가동성이 떨어지고 수정하기도 매우 어려워진다.

```javascript
step1(function(value1) {
  step2(value1, function(value2) {
    step3(value2, function(value3) {
      step4(value3, function(value4) {
        step5(value4, function(value5) {
          step6(value5, function(value6) {
            // value6를 사용하는 처리
          });
        });
      });
    });
  });
});
```

이를 해결하는 방법으로는 promise와 async/await 가 있다.