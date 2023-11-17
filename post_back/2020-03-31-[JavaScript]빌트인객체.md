## 빌트인 객체

`빌트인 객체` 는 ECMAScript 명세에 정의된 객체를 말하며 애플리케이션 전역의 공통 기능을 제공하며 Object, String, Number, Function, Array. Date, Math 와 같은 객체 생성에 관계가 있는 객체와 메소드로 구성된다.

<br>

### Object
---


```javascript
// Object.keys()
// Object.prototype.toString() -> 모든 객체가 사용할 수 있는 메소드
var arr = ["a", "b", "c"];
document.write('Object.keys(arr) : ', Object.keys(arr), '<br/>');

var o = new Object();
document.write('o.toString() : ', o.toString(), '<br/>');


var a = new Array(1,2,3);
document.write('a.toString() : ', a.toString(), '<br/>');
```

<br>

```
Object.keys(arr) : 0,1,2
o.toString() : [object Object]
a.toString() : 1,2,3
```            


<br>

### Boolean
---

`Boolean` 객체는 boolean 타입을 위한 객체이다.

```javascript
var foo = new Boolean(true);     // true
var foo = new Boolean('false');  // true
var foo = new Boolean(false);   // false
var foo = new Boolean();        // false
```

<br>

### Number
---

`Number` 객체는 아래 포스팅을 참고하자.

<br>

### Math
---

`Math` 객체는 아래 포스팅을 참고하자.

<br>

### Date
---

`Date` 객체는 아래 포스팅을 참고하자.

<br>

### String
---

`String` 객체는 아래 포스팅을 참고하자.

<br>

### Array
---

`Array` 는 아래 포스팅을 참고하자.

<br>

### Error
---

`Error` 생성자는 error 객체를 생성하며 오류 발생 시 throw 된다.

```javascript
try {
    fun();
    throw new Error("ERRRRROR!");
} catch (e) {
    console.log(e.name + ' : ' + e.message);
}
```