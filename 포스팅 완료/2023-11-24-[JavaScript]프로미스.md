## 프로미스(Promise)

`Promise` 객체는 비동기 작업의 최종 완료 또는 실패를 나타내는 Array나 Object 처럼 독자적인 객체라고 보면 된다. 비동기 작업이 끝날 때까지 결과를 기다리는 것이 아니라, 결과를 제공하겠다는 약속을 반환한다는 의미이다.

<br>

### 프로미스 객체 생성
---

Promise 객체를 생성하기 위해 new 키워드와 생성자 함수를 사용한다. 생성자는 2개의 매개변수를 가진 콜백 함수를 넣게 되는데 첫 번째 인수는 작업이 성공했을 때 성공(resolve)을 알려주는 객체이며 두 번째 인수는 작업이 실패했을 때 실패(reject)임을 알려주는 객체이다.

```javascript
const myPromise = new Promise((resolve, reject) => {
	// 비동기 작업 수행
  const data = fetch('서버로부터 요청할 URL');
    
  if(data)
   	resolve(data);  // 만일 요청이 성공하여 데이터가 있다면
  else
   	reject("Error");  // 만일 요청이 실패하여 데이터가 없다면
})
```

<br>

### 프로미스 후속 처리
---

위처럼 만들어진 Promise 객체는 비동기 작업이 완료된 후 후속 처리 메소드(then, catch)를 통해 성공과 실패에 대한 후속처리를 진행할 수 있다.

- then
then 메소드는 두 개의 콜백 함수를 인자로 전달 받는다. 첫 번째 콜백 함수는 성공(fulfilled, resolve 함수가 호출된 상태) 시 호출되고 두 번째 함수는 실패(rejected, reject 함수가 호출된 상태) 시 호출된다. then 메소드는 Promise를 반환한다.

- catch
예외(비동기 처리에서 발생한 에러와 then 메소드에서 발생한 에러)가 발생하면 호출된다. catch 메소드는 Promise를 반환한다.

```javascript
function myPromise() {
  return new Promise((resolve, reject) => {
    if (/* 성공 조건 */) {
      resolve(/* 결과 값 */);
    } else {
      reject(/* 에러 값 */);
    }
  });
}

// 프로미스 객체를 반환하는 함수 사용
myPromise()
  .then((result) => {
      // 성공 시 실행할 콜백 함수
  })
  .catch((error) => {
      // 실패 시 실행할 콜백 함수
  });
```

<br>

보통 이처럼 Promise 객체를 사용할 경우 함수로 감싸서 사용하며 대부분의 자바스크립트 비동기 라이브러리도 함수 형태로 프로미스 객체를 제공한다. 대표적으로 자바스크립트의 `fetch()` 가 있는데, 메서드 내에서 프로미스 객체를 생성하여 서버로부터 데이터를 가져오면 resolve() 하여 .then() 으로 처리하기 때문이다.

```javascript
// GET 요청 
fetch('https://jsonplaceholder.typicode.com/posts/1')
  .then((response) => response.json())  // 응답 객체에서 JSON 데이터를 추출한다.
  .then((data) => console.log(data));  // JSON 데이터를 콘솔에 출력한다.
```

<br>

### 프로미스 3가지 상태
---

비동기 작업 중 진행, 성공, 실패 상태를 나타내는 것이 프로미스 상태며 일종의 처리 과정이다.

- Pending(대기) : 처리가 완료되지 않은 상태
- Fulfilled(이행) : 성공적으로 처리가 완료된 상태
- Rejected(거부) : 처리가 실패로 끝난 상태

<br>

#### Pending 상태

`Pending` 상태란 말 그대로 아직 비동기 처리 로직이 완료 되지 않은 상태이다(resolve 또는 reject 함수가 아직 호출되지 않은 상태).

```javascript
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
   	resolve("처리 완료")
  }, 5000)
});

console.log(promise);  // Pending (대기) 상태
```

<br>

#### Fulfilled 상태

`Fulfilled` 상태란 성공적으로 처리가 완료된 상태이다(resolve 함수가 호출된 상태). 위의 예제에서 5초 후에 콘솔을 다시 찍어보면 Fulfilled 상태가 된다.

그리고 then() 메소드를 호출하여 결과 값을 받을 수 있다.

```javascript
promise
  .then((data) => {
    console.log("프로미스가 이행 상태가 되면서 처리에 대한 결과를 수행")
  })
```

<br>

#### Rejected 상태

`Rejected` 상태란 실패한 상태이다.(reject 함수가 호출된 상태) reject()를 호출하면 실패 상태가 된다.

```javascript
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
   	reject("처리 실패")
  }, 5000)
});
```

<br>

마찬가지로 catch() 메소드를 호출하여 실패에 대한 후속 처리를 할 수 있다.

```javascript
promise
  .catch((error) => {
   	console.log(error);
    console.log("실패에 대한 후속 조치...")
  })
```

<br>

### 프로미스 체이닝
---

프로미스 체이닝이란 프로미스를 연달아 연결하는 것을 의미한다. 이렇게 하면 여러 개의 비동기 작업을 순차적으로 처리할 수 있다.

```javascript
function doSomething() {
  return new Promise((resolve, reject) => {
    resolve(100)
  });
}

doSomething()
  .then((value1) => {
    const data1 = value1 + 50;
    return data1
  })
  .then((value2) => {
    const data2 = value2 + 50;
    return data2
  })
  .then((value3) => {
    const data3 = value3 + 50;
    return data3
  })
  .then((value4) => {
    console.log(value4);  // 250 출력
  })
```

<br>

```javascript
function doSomething(arg) {
  return new Promise((resolve, reject) => {
    resolve(arg)
  });
}

doSomething('100A')
  .then((value1) => {
    const data1 = value1 + 50; // 숫자에 문자를 연산  
    if (isNaN(data1)) 
      throw new Error('값이 넘버가 아닙니다')
    
    return data1
  })
  .then((value2) => {
    const data2 = value2 + 50;
    return data2
  })
  .catch((err) => {
    console.error(err);
  })
```

<br>

### 프로미스 정적 메소드
---

프로미스(promise) 객체ㅔ는 생성자 함수 외에도 여러 가지 정적 메소드를 제공한다.

<br>

#### Promise.resolve()

```javascript
// 프로미스 객체와 전혀 연관없는 함수
function getRandomNumber() {
  const num = Math.floor(Math.random() * 10); // 0 ~ 9 사이의 정수
  return num;
}

// Promise.resolve() 를 사용하여 프로미스 객체를 반환하는 함수
function getPromiseNumber() {
  const num = getRandomNumber(); // 일반 값
  return Promise.resolve(num); // 프로미스 객체
}

// 핸들러를 이용하여 프로미스 객체의 값을 처리하는 함수
getPromiseNumber()
  .then((value) => {
    console.log(`랜덤 숫자: ${value}`);
  })
  .catch((error) => {
    console.error(error);
  });
```

<br>

#### Promise.reject()

```javascript
// 주어진 사유로 거부되는 프로미스 생성
const p = Promise.reject(new Error('error'));

// 거부 사유를 출력
p.catch(error => console.error(error));  // Error: error
```

<br>

#### Promise.all()

배열, Map, Set에 포함된 여러개의 프로미스 요소들을 한꺼번에 비동기 작업을 처리해야 할때 굉장히 유용한 프로미스 정적 메소드이다.
모든 프로미스 비동기 처리가 이행(fulfilled) 될때까지 기다려서, 모든 프로미스가 완료되면 그때 then 핸들러가 실행된다.

```javascript
const api_1 = fetch("https://jsonplaceholder.typicode.com/users");
const api_2 = fetch("https://jsonplaceholder.typicode.com/users");
const api_3 = fetch("https://jsonplaceholder.typicode.com/users");

const promises = [api_1, api_2, api_3];

// Promise.all() 메서드 인자로 프로미스 배열을 넣어, 모든 프로미스가 이행될 때까지 기다리고, 결과값을 출력
Promise.all(promises)
  .then((results) => {
    // results는 이행된 프로미스들의 값들을 담은 배열.
    // results의 순서는 promises의 순서와 일치.
    console.log(results); // [users1, users2, users3]
  })
  .catch((error) => {
    // 어느 하나라도 프로미스가 거부되면 오류를 출력
    console.error(error);
  });
```

<br>

#### Promise.any()

`Promise.all()` 메소드와는 반대로 모든 프로미스 중 하나라도 완료되면 바로 반환하는 정적 메서드이다.

```javascript
const promise1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    reject("promise1 failed");
  }, 3000);
});

const promise2 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("promise2 succeeded");
  }, 2000);
});

const promise3 = new Promise((resolve, reject) => {
  setTimeout(() => {
    reject("promise3 failed");
  }, 1000);
});

// promise1, promise2, promise3은 각각 3초, 2초, 1초 후에 거부되거나 이행
Promise.any([promise1, promise2, promise3])
  .then((value) => {
    console.log(value);  // "promise2 succeeded" 
  })
  .catch((error) => {
    console.error(error);
  });
```

<br>

### 프로미스 지옥
---

콜백 함수의 콜백 지옥과 마찬가지로 프로미스의 경우도 then() 메소드가 지나치게 많아지면 코드가 길어지고 가독성이 떨어지게 된다.

```javascript
fetch("https://api.github.com/users")
  .then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("Network Error");
    }
  })
  .then((users) => {
    return users.map((user) => user.login);
  })
  .then((logins) => {
    return logins.join(", ");
  })
  .then((result) => {
    console.log(result);
  })
  .catch((error) => {
    console.error(error);
  });
```

<br>

이를 극복하기 위한 문법이 바로 비동기에 대해 마지막으로 다룰 async/await 문법이다.