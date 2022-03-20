

# Math 객체
---
Math 객체는 수학을 위한 프로퍼티와 메소드를 제공하는 객체이다.

## 속성
---

### PI
---
pi 값을 반환한다.

```javascript
Math.PI;   // 3.141592653589793
```

## 함수
---

### abs(x)
---
`x`의 절댓값을 반환한다.

```javascript
Math.abs(-1);   // 1
Math.abs('-1');   // 1
Math.abs('');   // 0
Math.abs([]);   // 0
Math.abs();   // NaN
```

### round(x)
---
`x`의 소수점 이하를 반올림하여 정수를 반환한다.

```javascript
Math.round(2.6);   // 3
Math.round(-1.5);   // -1
Math.round();   // NaN
```

### ceil(x)
---
`x`의 소수점 이하를 올림하여 정수를 반환한다.

```javascript
Math.ceil(2.6);   // 3
Math.ceil(-1.5);   // -1
Math.ceil();   // NaN
```
#### floor(x)
---
`x`의 소수점 이하를 내림하여 정수를 반환한다. 음수인 경우, 소수점 이하를 버린 후 -1 한 정수를 반환한다.

```javascript
Math.floor(2.7);   // 2
Math.floor(-3.4);   // -4
Math.floor();   // NaN
```

### sqrt(x)
---
`x`의 제곱근을 반환한다.

```javascript
Math.sqrt(9);   // 3
Math.sqrt(2);   // 1.4142135623730951
Math.sqrt(-4);   // NaN
```

### random()
---
0부터 1미만의 부동 소수점을 반환한다.

```javascript
Math.random();   // 0.590025323429568

var random = Math.floor((Math.random() * 10) + 1);
console.log(random);   // 1 ~ 10 까지의 정수
```

### pow(x, y)
---
`x`의 `y` 승(거듭 제곱)을 반환한다.

```javascript
Math.pow(2, 3);   // 8
```

### max(x)
---
`x` 중에서 가장 큰 수를 반환한다.

```javascript
Math.max(2, 3, -1);   // 3

var arr = [1, 2, 4];   // 4
Math.max(...arr);
```

### min(x)
---
`x` 중에서 가장 작은 수를 반환한다.

```javascript
Math.min(2, 3, -1);   // -1

var arr = [1, 2, 4];   // 1
Math.min(...arr);
```
