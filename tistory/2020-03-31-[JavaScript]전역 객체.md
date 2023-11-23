

## 전역객체

전역객체란 자바스크립트 내에서 가장 최상위에 위치한 유일한 객체를 의미한다.  
- 클라이언트(브라우저) 측면에서는 `window`, 서버(Node.js) 측면에서는 `global` 객체를 의미한다.  
- 자바스크립트 코드 상에서 최상위 객체이므로 루트 객체라고도 한다.  
- 생성자가 없으므로 `new` 키워드를 통해 객체를 생성할 수 없다.  
- document와 같은 하위 객체를 통해 제어할 때 생략이 가능하다.  
- 몇몇 객체(Math, Date 등)를 제외한 모든 객체는 전역 객체의 자손에 속한다.

<br>

### 속성
---


#### Infinity
---

양/음의 무한대를 나타내는 숫자값이다.

```javascript
console.log(Infinity);   // Infinity
console.log(-2 / 0);   // -Infinity
console.log(typeof(Infinity));   // number
```

<br>

### NaN
---

숫자가 아님을 나타내는 숫자값이다.(= Number.NaN)

```javascript
console.log(NaN);   // NaN
console.log(3 / 'yang');   // NaN
console.log(typeof(NaN));   // NaN
```

<br>

### undefined
---

원시타입 undefined를 값으로 갖는다.

```javascript
console.log(undefined);   // undefined
console.log(typeof(undefined));   // undefined
```

<br>

### 함수
---

#### isFinite(x)
---

`x` 값이 정상적인 수인지 확인하여 Boolean으로 반환한다. `x`가 숫자가 아닐 경우 숫자로 변환 후 확인한다.

```javascript
isFinite(Infinity);   // false
isFinite('yang');   // false
isFinite('2');   // true
isFinite(-1);   // true
```
<br>

#### isNaN(x)

`x` 값이 NaN인지 확인하여 Boolean으로 반환한다. `x`가 숫자가 아닐 경우 숫자로 변환 후 확인한다.

```javascript
isNaN(NaN);   // true
isNaN(' ');   // false
isNaN({});   // true
isNaN('yang');   // true
isNaN(3);   // false
```

<br>

### parseFloat(x)
---

문자열 `x`를 부동소수점 숫자로 변환하여 반환한다.

```javascript
parseFloat('3.1415');   // 3.1415
parseFloat('10.0');   // 10
parseFloat(' 60 ');   // 60
```

<br>

### parseInt(x[, y])
---

문자열 `x`를 정수로 변환하여 반환하며 반환값은 10진수이다. `y`는 진법을 의미한다.

```javascript
parseInt(20);   // 20
parseInt(20.55);   // 20
parseInt('30');   // 30
parseInt('40 second')   // 40

// 2진수 110의 값
parseInt('110', 2);   // 3 
```

<br>

### encodeURI(x) / decodeURI(x)
---

`encodeURI()`는 URI 값 `x`를 인코딩, `decodeURI()`는 디코딩한다.

```javascript
var uri = 'https://google.com?name=상길';
var incode = encodeURI(uri);
var decode = decodeURI(incode);

console.log(incode);   // https://google.com?name=%EC%83%81%EA%B8%B8
console.log(decode);   // https://google.com?name=상길
```

<br>

### encodeURIComponent(x) / decodeURIComponent(x)
---

`encodeURIComponent()`는 URI 값 `x`의 구성요소를 인코딩, `decodeURIComponent()`는 디코딩한다. `encodeURI() / decodeURI()` 와 달리 파라미터 구분자(=, ?, &, / 등)를 인/디코딩한다.

```javascript
var uri = 'https://google.com?name=상길';
var incode = encodeURIComponent(uri);
var decode = decodeURIComponent(incode);

console.log(incode);   // https%3A%2F%2Fgoogle.com%3Fname%3D%EC%83%81%EA%B8%B8
console.log(decode);   // https://google.com?name=상길
```

<br>

### alert(x)
---

사용자에게 중요한 내용이나 경고창을 띄워준다.

```javascript
alet('안녕하세요');
```

<br>

### prompt(x)
---

사용자에게 입력값을 받을 수 있는 창을 띄워준다. 입력 받은 값을 문자열로 반환하며 입력 값이 없을 경우 Null 값을 반환한다.

```javascript
var input = prompt('몇살입니까 : ');

console.log(typeof(input));   // string
console.log(input);   // 42
```

<br>

### confirm(x)
---

사용자에게 true('확인') / false('취소') 값을 리턴받을 수 있는 팝업창을 띄워준다.

```javascript
var result = confirm('매일 운동을 하시나요?');

if(result) {
    console.log('잘하셨어요');
}
else {
    console.log('운동하세요');
}
```
