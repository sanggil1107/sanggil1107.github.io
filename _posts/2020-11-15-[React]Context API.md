---
layout: post
title: "[React] Context API"
category: [React]

---
<br>

`Context API`에 대해 알아보자
<!-- more -->
 
<hr>



# Context API
```jsx
import { createContext } from 'react';

const ColorContext = createContext({ color: 'black' });

export default ColorContext;
```
```jsx
import React from 'react';
import ColorBox from './component/chap13/ColorBox';
import ColorContext from './component/chap13/Color';

const App = () => {
  return (
    <div>
      <ColorBox/>
    </div>
  );
};

export default App;
```
```jsx
import React from 'react';
import ColorContext from './Color';

const ColorBox = () => {
  return (
    <ColorContext.Consumer>
      {value => (
        <div 
          style={{
            width: '64px',
            height: '64px',
            background: value.color
          }}
        />
      )}
    </ColorContext.Consumer>
  );
};

export default ColorBox;
```
## Provider
```jsx
import React from 'react';
import ColorBox from './component/chap13/ColorBox';
import ColorContext from './component/chap13/Color';

const App = () => {
  return (
    <ColorContext.Provider value={{ color: 'red' }}>
      <div>
        <ColorBox/>
      </div>
    </ColorContext.Provider>
  );
};

export default App;
```

## 동적 Context
```jsx
import React, { createContext, useState } from 'react';

const ColorContext = createContext({
  state: { color: 'black', subcolor: 'red' },
  actions: {
    setColor: () => {},
    setSubcolor: () => {}
  }
});

const ColorProvider = ({children}) => {
  const [color, setColor] = useState('black');
  const [subcolor, setSubcolor] = useState('red');

  const value = {
    state: { color, subcolor },
    actions: { setColor, setSubcolor }
  };
  return (
    <ColorContext.Provider value={value}>{children}</ColorContext.Provider>
  );
};

// const ColorConsumer = ColorContext.Consumer
const { Consumer: ColorConsumer } = ColorContext;

export { ColorConsumer, ColorProvider };

export default ColorContext;
```
```jsx
import React from 'react';
import ColorBox from './component/chap13/ColorBox';
import { ColorProvider } from './component/chap13/Color';

const App = () => {
  return (
    <ColorProvider>
      <div>
        <ColorBox/>
      </div>
    </ColorProvider>
  );
};

export default App;
```
```jsx
import React from 'react';
import { ColorConsumer } from './Color';

const ColorBox = () => {
  return (
    <ColorConsumer>
      {value => (
        <>
          <div 
            style={{
              width: '64px',
              height: '64px',
              background: value.state.color
            }}
          />
          <div 
            style={{
              width: '32px',
              height: '32px',
              background: value.state.subcolor
            }}
          />
        </>
      )}
    </ColorConsumer>
  );
};

export default ColorBox;
```

## 색상 컴포넌트
```jsx
import React from 'react';

const colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'];

const SelectColors = () => {
  return (
    <div>
      <h2>색상을 선택하세요</h2>
      <div style={{display: 'flex'}}>
        {colors.map(color => (
          <div
            key={color}
            style={{
              background: color,
              width: '24px',
              height: '24px',
              cursor: 'pointer'
            }}
          />
        ))}
      </div>
      <hr/>
    </div>
  );
};

export default SelectColors;
```
