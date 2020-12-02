---
layout: post
title: "[React] Component 반복"
category: [React]

---
<br>

`Component 반복`에 대해 알아보자
<!-- more -->

<hr>


# 컴포넌트 반복

## map
```jsx
import React from 'react';
import Sample from './component/chap6/Sample';

const App = () => {
  return (
    <Sample/>
  );
};

export default App;
```
```jsx
import React from 'react';

const Sample = () => {
  const names = ['눈사람', '얼음', '눈', '바람'];
  const nameList = names.map(name => <li>{name}</li>);
  return <ul>{nameList}</ul>
};

export default Sample;
```

## key
```jsx
import React from 'react';

const Sample = () => {
  const names = ['눈사람', '얼음', '눈', '바람'];
  const nameList = names.map((name, i) => <li key={i}>{name}</li>);
  return <ul>{nameList}</ul>
};

export default Sample;
```

## 응용
### 초기 설정
```jsx
import React, { useState } from 'react';

const Sample = () => {
  const [names, setNames] = useState([
    { id: 1, text: '눈사람' },
    { id: 2, text: '얼음' },
    { id: 3, text: '눈' },
    { id: 4, text: '바람' }
  ]);

  const nameList = names.map(name => <li key={name.i}>{name.text}</li>);
  return <ul>{nameList}</ul>
};

export default Sample;
```

### 데이터 추가
```jsx
import React, { useState } from 'react';

const Sample = () => {
  const [names, setNames] = useState([
    { id: 1, text: '눈사람' },
    { id: 2, text: '얼음' },
    { id: 3, text: '눈' },
    { id: 4, text: '바람' }
  ]);
  const [inputText, setInputText] = useState('');
  const [nextId, setNextId] = useState(5);

  const onChange = e => setInputText(e.target.value);
  const onClick = () => {
    const nextNames = names.concat({
      id: nextId,
      text: inputText
    });
    setNextId(nextId + 1);
    setNames(nextNames);
    setInputText('');
  };

  const nameList = names.map(name => <li key={name.i}>{name.text}</li>);
  return (
    <>
      <input value={inputText} onChange={onChange}/>
      <button onClick={onClick}>추가</button>
      <ul>{nameList}</ul>
    </>
  );
};

export default Sample;
```
배열에 새 항목을 추가할 때 push는 기존 배열 자체를 바꾸지만 concat은 새로운 배열을 만든다.

```jsx
const nextNames = names.concat({
  id: nextId,
  text: inputText
});
```
```jsx
const nextNames = [
  ...names,
  {
    id: nextId,
    text: inputText
  }
];
```

### 데이터 제거
```jsx
import React, { useState } from 'react';

const Sample = () => {
  const [names, setNames] = useState([
    { id: 1, text: '눈사람' },
    { id: 2, text: '얼음' },
    { id: 3, text: '눈' },
    { id: 4, text: '바람' }
  ]);
  const [inputText, setInputText] = useState('');
  const [nextId, setNextId] = useState(5);

  const onChange = e => setInputText(e.target.value);
  const onClick = () => {

    const nextNames = [
      ...names,
      {
        id: nextId,
        text: inputText
      }
    ];

    setNextId(nextId + 1);
    setNames(nextNames);
    setInputText('');
  };

  const onRemove = id => {
    const nextNames = names.filter(name => name.id !== id);
    setNames(nextNames);
  };

  const nameList = names.map(name => (
    <li key={name.i} onDoubleClick={() => onRemove(name.id)}>{name.text}</li>
  ));
  return (
    <> 
      <input value={inputText} onChange={onChange}/>
      <button onClick={onClick}>추가</button>
      <ul>{nameList}</ul>
    </>
  );
};

export default Sample;
```

파라미터가 없을경우 그냥 사용
파라미터가 있을경우 () => 사용