
## String 객체


### 생성
---

String() 생성자 함수를 통해 생성할 수 있다.

```javascript
var a = new String('Yang');
var b = 'Yang';

console.log(a);   // 'Yang'
console.log(b);   // 'Yang'

console.log(typeof(a));   // object
console.log(typeof(b));   // string
```

<br>

### 속성
---

#### length

문자열 내의 문자 갯수를 반환한다.

```javascript
var str = 'Yang';

console.log(str.length);   // 4
```

<br>

### 함수
---

문자열은 변경 불가능한 원시 타입이므로 새로운 문자열을 만들어 반환한다.

#### charAt(x)

`x`로 전달한 index에 해당하는 위치의 문자를 반환한다. 문자열 범위를 벗어난 `x` 값일 경우 빈 문자열을 반환한다.

```javascript
var str = 'Yang';

console.log(str.charAt(0));   // 'Y'
console.log(str.charAt(1));   // 'a'
console.log(str.charAt(2));   // 'n'
console.log(str.charAt(3));   // 'g'
console.log(str.charAt(4));   // ''

for (var i = 0; i < str.lenght; i++) {
    console.log(str[i]);   // 'Y', 'a', 'n', 'g'
}
```

<br>

#### concat(x)

문자열 `x`와 연결하여 새로운 문자열을 반환한다.

```javascript
var str = 'Yang';

console.log(str.concat('Sang'));   // 'YangSang'
console.log(str);   // 'Yang'
```

<br>

#### indexOf(x)

문자 또는 문자열 `x`를 대상 문자열에서 검색하여 처음 위치한 index를 반환한다. 없을 경우 -1을 반환한다.

```javascript
var str = 'Yang Sang Gil';

console.log(str.indexOf('a'));   // 1
console.log(str.indexOf('G'));   // 10
console.log(str.indexOf('tt'));   // -1
```

<br>

#### lastIndexOf(x[, y])

문자 또는 문자열 `x`를 대상 문자열에서 검색하여 마지막에 위치한 index를 반환한다. 없을 경우 -1을 반환한다.  
`y`가 전달되면 검색 시작위치를 `y`로 하여 역방향으로 검색한다.

```javascript
var str = 'Yang Sang Gil';

console.log(str.lastIndexOf('a'));   // 6
console.log(str.lastIndexOf('a', 4));   // 1
console.log(str.lastIndexOf('tt'));   // -1
```

<br>

#### replace(x, y)

문자열 `x`를 대상 문자열에서 찾아 `y`로 대체한다. 검색된 문자열이 여러 개일 경우 처음 검색된 문자열만 대체된다.

```javascript
var str = 'Yang Sang Gil';

console.log(str.replace('Gil', 'Kil'));   // 'Yang Sang Kil'
```

<br>

#### split(x[, y])

문자열 `x`를 대상 문자열에서 검색하여 문자열을 구분한 후 분리된 문자열을 배열로 반환한다.

```javascript
var str = 'Yang Sang Gil';

console.log(str.split());   // ['Yang Sang Gil']
console.log(str.split(' '));   // ['Yang', 'Sang', 'Gil']
console.log(str.split(''));   // ['Y', 'a', 'n', 'g', ' ', 'S', 'a', 'n', 'g', ' ', 'G', 'i', 'l']

// 'a'를 구분자로 하여 반환
console.log(str.split('a'));   // ['Y', 'ng S', 'ng Gil']
```

<br>

#### substring(x[, y])

`x` index부터 `y`-1 index에 해당하는 문자를 모두 반환한다. 음수 값일 경우 전체 문자열을 반환한다.

```javascript
var str = 'Yang Sang Gil';

console.log(str.substring(1, 3));   // 'an'
console.log(str.substring(1));   // 'ang Sang Gil'
console.log(str.substring(-2));   // 'Yang Sang Gil'
```

<br>

#### slice(x[, y])

`substring`과 동일하지만 음수 값을 입력받을 수 있다.

```javascript
var str = 'Yang Sang Gil';

console.log(str.slice(1, 3));   // 'an'
console.log(str.slice(1));   // 'ang Sang Gil'

// 뒤에서 2자리 반환
console.log(str.slice(-2));   // 'il'
```

<br>

#### toLowerCase()

대상 문자열의 모든 문자를 소문자로 변환한다.

```javascript
var str = 'Yang Sang Gil';

console.log(str.toLowerCase());   // 'yang sang gil'
```

<br>

#### toUpperCase()

대상 문자열의 모든 문자를 대문자로 변환한다.

```javascript
var str = 'Yang Sang Gil';

console.log(str.toUpperCase());   // 'YANG SANG GIL'
```

<br>

#### trim() / trimaStart() / trimEnd()

대상 문자열의 공백 문자를 제거하여 반환한다.

```javascript
var str = '   Yang  ';

// 양쪽의 공백 제거
console.log(str.trim());   // 'Yang'

// 왼쪽 공백 제거
console.log(str.trimStart());   // 'Yang  '

// 오른쪽 공백 제거
console.log(str.trimEnd());   // '   Yang'
```

<br>

#### repeat(x)

`x` 만큼 반복하여 연결한 문자열을 반환한다. 0이면 빈 문자열을 반환한다.

```javascript
var str = 'Yang';

console.log(str.repeat(0));   // ''
console.log(str.repeat(1));   // 'Yang'
console.log(str.repeat(2));   // 'YangYang'
```

<br>

#### includes(x)

문자열 `x`가 대상 문자열에 있는지 확인하여 Boolean으로 반환한다.

```javascript
var str = 'Yang Sang Gil';

console.log(str.includes('Yang'));   // true
console.log(str.includes(''));   // true
console.log(str.includes('an'));   // true
console.log(str.includes('t'));   // false
console.log(str.includes());   // false
```