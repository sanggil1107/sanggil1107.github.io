
# this
--
함수를 호출할 때 함수가 어떻게 호출되었는지에 따라 `this`에 바인딩할 객체가 동적으로 결정된다.  
자바스크립트에서 함수를 호출하는 방식은 다음과 같다.
- 함수호출
- 메소드 호출
- 생성자 함수 호출
- apply / call / bind 호출

## 함수호출
---
일반 함수 호출 시 기본적으로 `this`는 전역객체에 바인딩된다. 뿐만 아니라 내부함수의 경우에도 내부함수를 호출하는 외부함수가 아닌 전역객체에 바인딩된다.

```javascript
function func() {
    console.log('func this : ', this);   // window
    function inner() {
        console.log('inner this : ', this);   // window
    }
    inner();
}

func();
```

또한, 메소드의 내부함수일 경우에도 `this`는 전역객체에 바인딩된다.

```javascript
var name = 'Y';

var obj = {
    name : 'Yang',
    func : function() {
        console.log('func this : ', this);   // obj
        console.log('func this.name : ', this.name);   // 'Yang'
        function inner() {
            console.log('inner this : ', this);   // window
            console.log('inner this.name : ', this.name);   // 'Y'
        }

        inner();
    }
}

obj.func();
```

## 메소드 호출
---
함수가 객체의 프로퍼티 값이면 메소드로서 호출된다. 이 때, 메소드 내부의 `this`는 해당 메소드를 호출한 객체에 바인딩된다.

```javascript
var obj = {
    name : 'Yang',
    getThis : function() {
        console.log(this);
    }
}

obj.say = function() {
    console.log(this.name);
}

var obj1 = {
    name : 'Sang'
}

obj1.say = obj.say;

obj.say();   // 'Yang'
obj.getThis();   // obj
obj1.say();   // 'Sang'
```

### 생성자 함수 호출
---
생성자 함수 호출의 경우 `this`는 새로 생성하는 객체에 바인딩되며, new 연산자와 함께 생성자 함수를 호출하면 아래와 같이 동작한다.
1. 빈 객체 생성 및 this 바인딩
   - 코드 실행 전 빈 객체가 우선 생성되며, 이 빈 객체는 생성자 함수가 새로 생성하는 객체가 된다. 이후, `this`는 이 객체에 바인딩된다.
2. this를 이용한 프로퍼티/메소드 추가
   - 생성자 함수 내에 `this`를 사용하여 프로퍼티나 메소드를 생성할 시, `this`는 새로 생성된 객체를 의미하므로 `this`로 추가된 프로퍼티나 메소드는 새로 생성된 객체에 추가된다.
3. 객체 반환
   - 반환문이 없는 경우, `this`에 바인딩된 새로운 객체가 반환된다.


```javascript
function Person(name) {
    this.name = name;
}

Person.prototype.getName = function() {
    console.log(this.name);
}

var my = new Person('Yang');
my.getName();   // 'Yang'

Person.prototype.name = 'Sang';
console.log(Person.prototype.getName());   // 'Sang'

var m = new Person('Gil');
m.getName();   // 'Gil'
```

생성자 함수를 new 연산자 없이 그냥 호출할 경우(일반 함수 호출), `this`에는 전역객체가 바인딩된다.

```javascript
function Person(name) {
    this.name = name;
    this.say = function() {
        console.log(this);
    }
}

var me = Person('Yang');

console.log(me);   // undefined
console.log(name);   // 'Yang'
say();   // window
```

```javascript
var funcThis = null;

function Obj(name) {
    this.name = name;
    funcThis = this;
}

var o1 = Obj('Yang');
console.log(funcThis);   // window

var o2 = new Obj('Sang');
console.log(funcThis);   // Obj
```

```javascript
var o = {};
var p = {};
function func() {
    switch(this) {
        case o:
            document.write('o <br/>');
            break;
        case p:
            document.write('p <br/>');
            break;
        case window:
            document.write('window <br/>');
            break;
    }
}
func();
func.apply(o);
func.apply(p);
```
```
window
o
p
```
