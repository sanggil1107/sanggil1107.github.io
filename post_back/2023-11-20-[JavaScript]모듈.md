## 모듈

`모듈` 이란 애플리케이션을 구성하는 개별적 요소로서 재사용 가능한 코드 조각을 말한다. 일반적으로 파일 단위로 분리되어 있으며 명시적으로 `모듈` 을 로드하여 재사용한다. 기능별로 분리되어 작성되므로 코드의 단위를 명확히 분리하여 애플리케이션을 구성할 수 있으며 재사용성이 좋아서 개발 효율성과 유지보수성을 높일 수 있다.

### 모듈 스코프
---

```javascript
// foo.js
var x = 'foo';

// 변수 x는 전역 변수이다.
console.log(window.x); // foo
```

<br>

```javascript
// bar.js
// foo.js에서 선언한 전역 변수 x와 중복된 선언이다.
var x = 'bar';

// 변수 x는 전역 변수이다.
// foo.js에서 선언한 전역 변수 x의 값이 재할당되었다.
console.log(window.x);  // bar
```

<br>

```css
<!DOCTYPE html>
<html>
<body>
  <script src="foo.js"></script>
  <script src="bar.js"></script>
</body>
</html>
```

<br>

### export
---

모듈은 독자적인 스코프를 가지고 있기 때문에 외부에서 다른 모듈들이 참조할 수 있게 하고 싶다면 `export` 키워드를 사용하여 공개하면 된다.

```javascript
// lib.mjs
// 변수의 공개
export const pi = Math.PI;

// 함수의 공개
export function square(x) {
  return x * x;
}

// 클래스의 공개
export class Person {
  constructor(name) {
    this.name = name;
  }
}
```

<br>

```javascript
// lib.mjs
const pi = Math.PI;

function square(x) {
  return x * x;
}

class Person {
  constructor(name) {
    this.name = name;
  }
}

// 변수, 함수 클래스를 하나의 객체로 구성하여 공개
export { pi, square, Person };
```

<br>

### import 
---

모듈에서 export한 대상을 로드하려면 `import` 키워드를 사용한다.

```javascript
// app.mjs
// 같은 폴더 내의 lib.mjs 모듈을 로드.
// lib.mjs 모듈이 export한 식별자로 import한다.
// ES6 모듈의 파일 확장자를 생략할 수 없다.
import { pi, square, Person } from './lib.mjs';

console.log(pi);          // 3.141592653589793
console.log(square(10));  // 100
console.log(new Person('Lee'));  // Person { name: 'Lee' }
```

<br>

모듈이 export한 식별자를 각각 지정하지 않고 하나의 이름으로 한꺼번에 `import` 할 수도 있다. 이때 `import` 되는 식별자는 as 뒤에 지정한 이름의 객체에 프로퍼티로 할당된다. 또한, 이름을 변경하여 `import` 할 수도 있다.

```javascript
// app.mjs
import * as lib from './lib.mjs';

console.log(lib.pi);          // 3.141592653589793
console.log(lib.square(10));  // 100
console.log(new lib.Person('Lee'));  // Person { name: 'Lee' }
```

<br>

```javascript
// app.mjs
import { pi as PI, square as sq, Person as P } from './lib.mjs';

console.log(PI);     // 3.141592653589793
console.log(sq(2));  // 4
console.log(new P('Kim'));  // Person { name: 'Kim' }
```
