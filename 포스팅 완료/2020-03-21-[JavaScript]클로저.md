

## 클로저

클로저란 외부함수의 변수에 접근할 수 있는 내부 함수를 일컫으며 스코프 체인(scope chain)으로 표현되기도 한다.

```javascript
function outer() {
    var color = 'green';
    function inner() {
        console.log(color);
    }
    return inner;
}

var func = outer();
func();   // 'green'
```

<br>

```javascript
function plus() {
    var cnt = 0;

    function count() {
        cnt++;
        return cnt;
    }
    return count;
}

var add = plus();

console.log(add());   // 1
console.log(add());   // 2
console.log(add());   // 3
```

<br>

### 전역변수 억제
---

아래 예제는 버튼을 클릭한 횟수에 따라 누적된 카운트 값을 보여주는 예이다. 해당 카운트 변수를 전역변수로 사용할 수 있지만 조작할 수 있다는 문제점이 있어 아래와 같이 클로저를 이용하면 전역변수 사용 없이 안정적으로 구현할 수 있다.

```css
<html>
<head>
</head>
<body>
<button id="plus">+</button><p id="cnt">0</p>
<script>
    var plusBtn = document.getElementById('plus');
    var cnt = document.getElementById('cnt');
    var add = (function() {
        var count = 0;

        return function() {
            return ++count;
        }
    }());

    plusBtn.onclick = function() {
        cnt.innerHTML = add();
    }
</script>
</body>
</html>
```

<br>

```css
<html>
<head>
</head>
<body>
<button id="plus">+</button>
<button id="minus">-</button>
<p id="cnt">0</p>
<script>
    var plusBtn = document.getElementById('plus');
    var minusBtn = document.getElementById('minus');
    var cnt = document.getElementById('cnt');
    function counter() {
        var count = 0;

        return function(func) {
            count = func(count);
            return count;
        }
    };

    function addfunc(n) {
        return ++n;
    };

    function minusfunc(n) {
        return --n;
    };

    func = counter();

    plusBtn.onclick = function() {
        cnt.innerHTML = func(addfunc);
    };

    minusBtn.onclick = function() {
        cnt.innerHTML = func(minusfunc);
    };
</script>
</body>
</html>
```

<br>

### 정보은닉
---

아래와 같이 `Counter` 생성자 함수의 count 변수는 외부에서 접근이 불가능하다. 하지만 생성자 함수가 생성한 객체인 `counter`의 메소드 `add`를 통해 count 변수에 접근할 수 있게 되어 count 변수는 `private` 키워드처럼 동작하게 된다.

```javascript
function Counter() {
    var count = 0;

    this.add = function() {
        return ++count;
    };    
}

var counter = new Counter();

console.log(counter.add());   // 1
console.log(counter.add());   // 2
```

<br>

### 자주 발생하는 실수
---

아래 결과에서 0, 1, 2, 3, 4를 예상하지만 for문의 i 변수가 전역변수이므로 전혀 다른 결과가 출력된다.


```javascript
var arr = [];
for(var i = 0; i<5; i++) {
    arr[i] = function() {
        return i;
    }
}  

for(var index in arr) {          
    console.log(arr[index]());   // 5 5 5 5 5
}
```

<br>

다음과 같이 즉시함수를 통해 전역 변수 i의 값을 매개변수에 할당한 후 내부함수를 반환하게 되면 id에는 매개변수에 할당된 값이 유지되어 있으므로 원하는 출력값을 확인할 수 있다.

```javascript
var arr = []
for(var i = 0; i<5; i++) {
    arr[i] = (function(id) {
        return function() {
            return id;
        }
    }(i));
}  
for(var index in arr) {          
    console.log(arr[index]());   // 0 1 2 3 4
}
/*
for(var i = 0; i<5; i++) {
    arr[i] = function(id) {
        return function() {
            return id;
        }
    }(i);
}  
*/
```
