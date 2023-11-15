## 템플릿 문자열

템플릿 문자열(Template String)은 문자열을 생성하는 새롭게 도입된 리터럴이다. 문자열을 설정하기 위해 따옴표(`)를 사용한다. 

```javascript
const template = `템플릿 리터럴은 '작은따옴표(single quotes)'과 "큰따옴표(double quotes)"를 혼용할 수 있다.`;

console.log(template);
```

<br>

줄바꿈은 허용되지 않으며 공백을 표현하기 위해서는 백슬래시(\)로 시작하는 이스케이프 시퀀스(Escape Sequence)를 사용하여야 한다. ES6 템플릿 리터럴은 일반적인 문자열과 달리 여러 줄에 걸쳐 문자열을 작성할 수 있으며 템플릿 리터럴 내의 모든 white-space는 있는 그대로 적용된다.

```javascript
const template = `<ul class="nav-items">
  <li><a href="#home">Home</a></li>
  <li><a href="#news">News</a></li>
  <li><a href="#contact">Contact</a></li>
  <li><a href="#about">About</a></li>
</ul>`;

console.log(template);
```

<br>

또한 + 연산자를 사용하지 않아도 간단하게 새로운 문자열을 삽입할 수 있다.

```javascript
const first = 'Ung-mo';
const last = 'Lee';

// ES5: 문자열 연결
console.log('My name is ' + first + ' ' + last + '.');
// "My name is Ung-mo Lee."

// ES6: 템플릿 문자열
console.log(`My name is ${first} ${last}.`);
// "My name is Ung-mo Lee."
```