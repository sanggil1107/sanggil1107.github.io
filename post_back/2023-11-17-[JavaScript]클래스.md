## 클래스

자바스크립트는 프로토타입 기반 객체지향 언어로 클래스가 필요없는(class-free) 객체지향 프로그래밍 스타일로 프로토타입 체인과 클로저 등으로 객체 지향 언어의 상속, 캡슐화(정보 은닉) 등의 개념을 구현할 수 있었다. 

하지만 ES6에서는 클래스에 대한 새로운 문법을 다음과 같이 제시한다.

<br>

### 클래스 정의
---

ES6 클래스는 `class` 키워드를 사용한다.

```javascript
// 클래스 선언문
class Person {
  // constructor(생성자)
  constructor(name) {
    this._name = name;
  }

  say() {
    console.log(`Hi! ${this._name}`);
  }
}

// 인스턴스 생성
const me = new Person('Lee');
me.say();  // Hi! Lee

console.log(me instanceof Person);  // true
```

<br>

### 인스턴스 생성
---

`new` 키워드를 사용한다.

```javascript
class Foo {}

const foo = new Foo();
```

<br>

### 생성자(constructor)
---

`생성자` 는 인스턴스를 생성하고 클래스 필드(클래스 내부의 변수)를 초기화하기 위한 메소드이다.

```javascript
// 클래스 선언문
class Person {
  // constructor(생성자). 이름을 바꿀 수 없다.
  constructor(name) {
    // this는 클래스가 생성할 인스턴스를 가리킨다.
    // _name은 클래스 필드이다.
    this._name = name;
  }
}

// 인스턴스 생성
const me = new Person('Lee');
console.log(me);  // Person {_name: "Lee"}
```

<br>

생성자는 클래스 내에서 한개만 존재할 수 있으며 생략도 가능하다. 생략하면 `constructor() {}` 를 호출한 것과 동일하며 빈 객체를 생성한다. 만약 프로퍼티를 추가하려면 인스턴스를 생성한 이후 동적으로 추가해야 한다.

```javascript
class Foo { }

const foo = new Foo();
console.log(foo);  // Foo {}

// 프로퍼티 동적 할당 및 초기화
foo.num = 1;
console.log(foo);  // Foo&nbsp;{ num: 1 }
```

<br>

```javascript
class Foo {
  // constructor는 인스턴스의 생성과 동시에 클래스 필드의 생성과 초기화를 실행한다.
  constructor(num) {
    this.num = num;
  }
}

const foo = new Foo(1);

console.log(foo);  // Foo { num: 1 }
```

<br>

### 클래스 필드
---

클래스 필드(멤버 변수)의 선언과 초기화는 생성자 내부에서 해야한다.

```javascript
class Foo {
  constructor(name = '') {
    this.name = name;  // 클래스 필드의 선언과 초기화
  }
}
const foo = new Foo('Lee');

console.log(foo);  // Foo { name: 'Lee' }
console.log(foo.name);  // Lee
```

<br>

### getter, setter
---

#### getter

`getter` 는 클래스 필드에 접근할 때마다 클래스 필드의 값을 조작하는 행위가 필요할 때 사용하며 메소드 이름 앞에 get 키워드를 사용해 정의한다.

```javascript
class Foo {
  constructor(arr = []) {
    this._arr = arr;
  }

  // getter: get 키워드 뒤에 오는 메소드 이름 firstElem은 클래스 필드 이름처럼 사용된다.
  get firstElem() {

    return this._arr.length ? this._arr[0] : null;
  }
}

const foo = new Foo([1, 2]);
// 필드 firstElem에 접근하면 getter가 호출된다.
console.log(foo.firstElem);  // 1
```

<br>

#### setter

`setter` 는 클래스 필드에 값을 할당할 때마다 클래스 필드의 값을 조작하는 행위가 필요할 때 사용하며 메소드 이름 앞에 set 키워드를 사용해 정의한다.

```javascript
class Foo {
  constructor(arr = []) {
    this._arr = arr;
  }

  // getter: get 키워드 뒤에 오는 메소드 이름 firstElem은 클래스 필드 이름처럼 사용된다.
  get firstElem() {
    // getter는 반드시 무언가를 반환하여야 한다.
    return this._arr.length ? this._arr[0] : null;
  }

  // setter: set 키워드 뒤에 오는 메소드 이름 firstElem은 클래스 필드 이름처럼 사용된다.
  set firstElem(elem) {

    this._arr = [elem, ...this._arr];
  }
}

const foo = new Foo([1, 2]);

// 클래스 필드 lastElem에 값을 할당하면 setter가 호출된다.
foo.firstElem = 100;

console.log(foo.firstElem);  // 100
```

<br>

### 정적 메소드
---

`static` 키워드를 사용하여 정적 메소드를 정의한다. 정적 메소드는 클래스의 인스턴스가 아닌 클래스 이름으로 호출하며 this를 사용할 수 없다.

```javascript
class Foo {
  constructor(prop) {
    this.prop = prop;
  }

  static staticMethod() {
    /*
    정적 메소드는 this를 사용할 수 없다.
    정적 메소드 내부에서 this는 클래스의 인스턴스가 아닌 클래스 자신을 가리킨다.
    */
    return 'staticMethod';
  }

  prototypeMethod() {
    return this.prop;
  }
}

// 정적 메소드는 클래스 이름으로 호출한다.
console.log(Foo.staticMethod());

const foo = new Foo(123);

// 정적 메소드는 인스턴스로 호출할 수 없다.
console.log(foo.staticMethod()); // Uncaught TypeError
```

<br>

### 클래스 상속
---

부모 클래스를 상속받는 자식 클래스를 정의할 때 `extends` 키워드를 사용한다.

- 오버라이딩(Overriding)
상위 클래스가 가지고 있는 메소드를 하위 클래스가 재정의하여 사용하는 방식이다.

- 오버로딩(Overloading)
매개변수의 타입 또는 갯수가 다른, 같은 이름의 메소드를 구현하고 매개변수에 의해 메소드를 구별하여 호출하는 방식이다.

```javascript
// 부모 클래스
class Circle {
  constructor(radius) {
    this.radius = radius; 
  }

  getDiameter() {
    return 2 * this.radius;
  }

  getPerimeter() {
    return 2 * Math.PI * this.radius;
  }

  getArea() {
    return Math.PI * Math.pow(this.radius, 2);
  }
}

// 자식 클래스
class Cylinder extends Circle {
  constructor(radius, height) {
    super(radius);
    this.height = height;
  }

  // 원통의 넓이: 부모 클래스의 getArea 메소드를 오버라이딩하였다.
  getArea() {
    return (this.height * super.getPerimeter()) + (2 * super.getArea());
  }

  getVolume() {
    return super.getArea() * this.height;
  }
}

// 반지름이 2, 높이가 10인 원통
const cylinder = new Cylinder(2, 10);

// 원의 지름
console.log(cylinder.getDiameter());   // 4
// 원의 둘레
console.log(cylinder.getPerimeter());  // 12.566370614359172
// 원통의 넓이
console.log(cylinder.getArea());       // 150.79644737231007
// 원통의 부피
console.log(cylinder.getVolume());     // 125.66370614359172

// cylinder는 Cylinder 클래스의 인스턴스이다.
console.log(cylinder instanceof Cylinder);  // true
// cylinder는 Circle 클래스의 인스턴스이다.
console.log(cylinder instanceof Circle);    // true
```

<br>

#### super

`super` 키워드는 부모 클래스를 참조(Reference)할 때 또는 부모 클래스의 생성자를 호출할 때 사용한다.

```javascript
// 부모 클래스
class Circle {
  constructor(radius) {
    this.radius = radius; 
  }

  getDiameter() {
    return 2 * this.radius;
  }

  getPerimeter() {
    return 2 * Math.PI * this.radius;
  }

  getArea() {
    return Math.PI * Math.pow(this.radius, 2);
  }
}

class Cylinder extends Circle {
  constructor(radius, height) {
    
    // super 메소드는 부모 클래스의 constructor를 호출하면서 인수를 전달한다.
    super(radius);
    this.height = height;
  }

  getArea() {

    // super 키워드는 부모 클래스(Base Class)에 대한 참조
    return (this.height * super.getPerimeter()) + (2 * super.getArea());
  }

  getVolume() {

    // super 키워드는 부모 클래스(Base Class)에 대한 참조
    return super.getArea() * this.height;
  }
}

// 반지름이 2, 높이가 10인 원통
const cylinder = new Cylinder(2, 10);
```