---
layout: post
title: "[React] Component"
category: [React]

---
<br>

`Component`에 대해 알아보자
<!-- more -->

<hr>


# 컴포넌트
## props

### jsx 내부에서 props 렌더링

```jsx
import React from 'react';

const MyComponent = props => {
  return <div>안녕하세요, 제 이름은 {props.name} 입니다.</div>
};

MyComponent.defaultProps = {
  name: '기본'
};

export default MyComponent;
```

### 컴포넌트를 사용할 떄 props 값 지정

```jsx
import React from 'react';
import MyComponent from './component/chap3/MyComponent';

const App = () => {
  return <MyComponent name="react"/>;
};

export default App;
```

### props 기본값 설정: defaultProps

```jsx
import React from 'react';

const MyComponent = props => {
  return <div>안녕하세요, 제 이름은 {props.name} 입니다.</div>
};

MyComponent.defaultProps = {
  name: '기본'
};

export default MyComponent;
```
```jsx
import React from 'react';
import MyComponent from './component/chap3/MyComponent';

const App = () => {
  return <MyComponent/>;
};

export default App;
```

### 태그 사이의 내용을 보여주는 children

```jsx
import React from 'react';
import MyComponent from './component/chap3/MyComponent';

const App = () => {
  return <MyComponent>리액트</MyComponent>;
};

export default App;
```
```jsx
import React from 'react';

const MyComponent = props => {
  return (
    <div>
      안녕하세요, 제 이름은 {props.name} 입니다.<br/>
      children 값은 {props.children} 입니다.
    </div>
  );
};

MyComponent.defaultProps = {
  name: '기본'
};

export default MyComponent;
```

### 비구조화 할당 문법을 통한 props 내부 값 추출

```jsx
import React from 'react';

const MyComponent = ({ name, children }) => {
  
  return (
    <div>
      안녕하세요, 제 이름은 {name} 입니다.<br/>
      children 값은 {children} 입니다.
    </div>
  );
};

MyComponent.defaultProps = {
  name: '기본'
};

export default MyComponent;
```

### propsType를 통한 props검증

```jsx
import React from 'react';
import PropTypes from 'prop-types';

const MyComponent = ({ name, children }) => {
  
  return (
    <div>
      안녕하세요, 제 이름은 {name} 입니다.<br/>
      children 값은 {children} 입니다.
    </div>
  );
};

MyComponent.defaultProps = {
  name: '기본'
};

MyComponent.prototype = {
  name: PropTypes.string
};

export default MyComponent;
```
```jsx
import React from 'react';
import MyComponent from './component/chap3/MyComponent';

const App = () => {
  return <MyComponent name={3}>리액트</MyComponent>;
}

export default App;
```
화면에 표시되지만 경고창 나옴

#### 필수값
```jsx
import React from 'react';
import MyComponent from './component/chap3/MyComponent';

const App = () => {
  return <MyComponent name="react" num={3}>리액트</MyComponent>;
}

export default App;
```
```jsx
import React from 'react';
import PropTypes from 'prop-types';

const MyComponent = ({ name, num, children }) => {
  
  return (
    <div>
      안녕하세요, 제 이름은 {name} 입니다.<br/>
      children 값은 {children} 입니다.<br/>
      숫자는 {num} 입니다.
    </div>
  );
};

MyComponent.defaultProps = {
  name: '기본'
};

MyComponent.propTypes = {
  name: PropTypes.string,
  num: PropTypes.number.isRequired
};

export default MyComponent;
```