## async / await

`async / await` 는 ES2017에서 도입된 문법으로 Promise 로직을 더 쉽고 간결하게 사용할 수 있게 해준다. 하지만 완전히 Promise를 대체하기 위한 기능은 아니다.
사용법은 function 키워드 앞에 `async` 를, 비동기 처리되는 부분 앞에 `await` 키워드만 작성해주면 된다.

```javascript
// 기존 Promise.then() 형식
function main() {
  delay(1000)
      .then(() => {
        return delay(2000);
      })
      .then(() => {
        return Promise.resolve('끝');
      })
      .then(result => {
        console.log(result);
      });
}

main();  // 메인 함수 호출
```

<br>

```javascript
// async/await 방식
async function main() {
  await delay(1000);
  await delay(2000);
  const result = await Promise.resolve('끝');
  console.log(result);
}

main();  // 메인 함수 호출
```

<br>

### async 키워드
---

`async` 키워드는 await를 사용하기 위한 선언문에 해당한다. 즉, fucntion 앞에 `async` 를 붙여줌으로써 해당 함수 내에 await 키워드를 사용할 수 있게 되는 것이다.

```javascript
// 함수 선언식
async function func1() {
    const res = await fetch(url);  // 요청을 기다림
    const data = await res.json();  // 응답을 JSON으로 파싱
}
func1();

// 함수 표현식
const func2 = async () => {
    const res = await fetch(url);  // 요청을 기다림
    const data = await res.json();  // 응답을 JSON으로 파싱
}
func2();
```

<br>

async 키워드를 붙인 함수의 리턴값은 프로미스 객체로 감싸져서 반환된다.

```javascript
async function func1() {
  return 1;
}

const data = func1();
console.log(data);  // 프로미스 객체가 반환된다
```

<br>

### await 키워드
---

`await` 키워드는 promise.then() 보다 좀 더 세련되게 비동기 처리의 결과를 얻을 수 있도록 해준다. 

```javascript
// await 방식
async function func() {
    const res = await fetch(url);  // 요청을 기다림
    const data = await res.json();  // 응답을 JSON으로 파싱
    // data 처리
    console.log(data);
}
func();
```

<br>

`await` 키워드는 비동기 처리가 완료될 때까지 코드 실행을 중지하고 wait 한다. 
아래 예제를 보면 getData() async 함수 내에서 fetch() 비동기 함수를 호출하고, 반환된 Promise를 await 키워드로 처리한다. 이로 인해 함수 내 코드 실행이 일시 중지되고, fetch() 함수가 완료될 때까지 기다리게 된다. 서버로부터 리소스를 성공적으로 가져와 fetch() 함수가 완료되면, 바로 다음 response.json() 함수를 호출하여 반환된 Promise를 다시 await로 처리한다. 다시 데이터를 가져오는 동안 코드 실행이 일시 중지되고, 데이터가 성공적으로 가져와지면 최종 결과 값을 반환한다

```javascript
async function getData() {
  const response = await fetch('https://jsonplaceholder.typicode.com/users/1');
  const data = await response.json();
  console.log(data):
}
```

<br>

async/await 에서도 try/catch로 에러를 처리할 수 있다.

```javascript
// async/await 방식
async function func() {

    try {
        const res = await fetch(url);  // 요청을 기다림
        const data = await res.json();  // 응답을 JSON으로 파싱
        // data 처리
        console.log(data);
    } catch (err) {
        // 에러 처리
        console.error(err);
    }

}
func();
```