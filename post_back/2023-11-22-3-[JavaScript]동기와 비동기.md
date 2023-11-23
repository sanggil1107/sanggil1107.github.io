## 동기와 비동기

`동기(synchronous)` 방식은 이전 작업이 완료된 후 차례로 다음 작업을 순차적으로 싱핼하는 방식이며 `비동기(asynchronuous)` 방식은 여러 작업을 동시에 처리하기 위해 특정 작업의 완료를 기다리지 않고 다음 작업을 동시에 수행하는 방식이다.

<br>

### 동기(synchronous) 방식
---

`동기(synchronous)` 방식은 아래와 같은 특징을 가지고 있다.

- 직렬적으로 태스크를 수행하는 방식이다.
- 요청을 보낸 후 응답을 받아야지만 다음 동작이 이루어지는 방식이다. 어떠한 태스크를 처리할 동안 나머지 태스크는 대기한다.
- 실제로 cpu가 느려지는 것은 아니지만 시스템의 전체적인 효율이 저하된다고 할 수 있다.


```javascript
function firstFunc() {
  console.log("first");
}

function second(){
  console.log("second");
}

firstFunc();
second();

console.log("end");
```

<br>

### 비동기(asynchronous) 방식
---

`비동기(asynchronous)` 방식은 아래와 같은 특징을 가지고 있다.

- 병렬적으로 태스크를 수행하는 방식이다.
- 요청을 보낸 후 응답의 수락 여부와는 상관없이 다음 태스크가 동작하는 방식이다. 
- a 태스크가 실행되는 시간 동안 b 태스크를 할 수 있으므로 자원을 효율적으로 사용할 수 있다. 이때, 비동기 요청시 응답 후 처리할 '콜백 함수'를 함께 알려주며 해당 태스크가 완료되었을 때, 콜백 함수가 호출된다.

```javascript
function firstFunc(a,b, inFunc) {
  setTimeout(() => {
    const result = a +b;
    inFunc(result);
  }, 2000);
}

firstFunc(5,5, (res) => console.log(res));
console.log("end");
```

<br>

하지만 비동기 처리를 위해 콜백 패턴을 사용하면 처리 순서를 보장하기 위해 여러 개의 콜백 함수가 중첩되어 복잡도가 높아지는 콜백 지옥(Callback Hell) 이 발생하는 단점이 있다.
콜백 헬은 가독성을 나쁘게 하며 실수를 유발하는 원인이 된다. 아래는 콜백 지옥에 해당하는 예시이다.

```javascript
step1(function(value1) {
  step2(value1, function(value2) {
    step3(value2, function(value3) {
      step4(value3, function(value4) {
        step5(value4, function(value5) {
            // value5를 사용하는 처리
        });
      });
    });
  });
});
```

<br>

콜백 함수, promise, async/await에 대해서는 추후 포스팅을 통해 상세히 다룰 것이며 이번 포스팅에서는 간단하게만 살펴보자.

<br>

#### 비동기와 promise

콜백 함수는 엄연히 말하자면 비동기를 순차적으로 처리하기 위한 일종의 편법 같은 것이지 정식으로 지원하는 비동기 전용 함수가 아니다. 따라서 자바스크립트의 `Promise` 객체는 이러한 한계점을 극복하기 위해 비동기 처리를 위한 전용 객체로서 탄생하였다.

```javascript
function getDB() {
  return new Promise((resolve) => {
    setTimeout(() => {
      const value = 100;
      resolve(value);
    }, 3000);
  });
}

function main() {
  getDB()
    .then((value) => {
      let data = value * 2;
      console.log('data의 값 : ', data);
    })
    .catch((error) => {
      console.error(error);
    });
}

main();
```

<br>

#### 비동기와 async / await

promise도 콜백 함수와 마찬가지로 then 함수를 남용하게 되면 promise hell 이 발생할 수 있고 이렇게 되면 코드가 길어지고 복잡해진다. 그래서 나온 문법이 `async/awiat` 문법이다. async/await는 프로미스를 기반으로 하지만, 마치 동기 코드처럼 작성할 수 있게 해준다.

```javascript
function getDB() {
    return new Promise((resolve, reject) => {
        // 데이터베이스에서 값을 가져오는 3초 걸린다고 가정 (비동기 처리)
        setTimeout(() => {
            const value = 100;
            resolve(value); // Promise 객체 반환
        }, 3000);
    });
}

async function main() {
    let data = await getDB(); // await 키워드로 Promise가 완료될 때까지 기다린다
    data *= 2;
    console.log('data의 값 : ', data);
}
main(); // 메인 스레드 실행
```