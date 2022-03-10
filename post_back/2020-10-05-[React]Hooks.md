---
layout: post
title: "[React] Hooks"
category: [React]

---
<br>

`Hooks`에 대해 알아보자
<!-- more -->

<hr>


# hook
## usestate
```jsx
import React from 'react';
import Counter from './component/chap8/Counter';


const App = () => {
  return (
    <Counter/>
  );
};

export default App;
```
```jsx
import React, { useState } from 'react';

const Counter = () => {
  const [value, setValue] = useState(0);

  return (
    <div>
      <p>
        현재 카운터 값은 <b>{value}</b>입니다.
      </p>
      <button onClick={() => setValue(value + 1)}>+1</button>
      <button onClick={() => setValue(value - 1)}>-1</button>
    </div>
  );
};

export default Counter;
```
### useState 여러 개 사용하기
```jsx
import React, { useState } from 'react';

const Info = () => {
  const [name, setName] = useState('');
  const [nickname, setNickname] = useState('');

  const onChangeName = e => {
    setName(e.target.value);
  };

  const onChangeNickname = e => {
    setNickname(e.target.value);
  };

  return (
    <div>
      <div>
        <input value={name} onChange={onChangeName} />
        <input value={nickname} onChange={onChangeNickname} />
      </div>
      <div>
        <div>
          <b>이름 : </b> {name}
        </div>
        <div>
          <b>닉네임: </b> {nickname}
        </div>
      </div>
    </div>

  );
};

export default Info;
```


## useEffect
렌더링될때마다 특정작업을 수행하도록 설정
```jsx
import React, { useEffect, useState } from 'react';

const Info = () => {
  const [name, setName] = useState('');
  const [nickname, setNickname] = useState('');

  useEffect(() => {
    console.log('렌더링 완료');
    console.log({
      name,
      nickname
    });
  });
  const onChangeName = e => {
    setName(e.target.value);
  };

  const onChangeNickname = e => {
    setNickname(e.target.value);
  };

  return (
    <div>
      <div>
        <input value={name} onChange={onChangeName} />
        <input value={nickname} onChange={onChangeNickname} />
      </div>
      <div>
        <div>
          <b>이름 : </b> {name}
        </div>
        <div>
          <b>닉네임: </b> {nickname}
        </div>
      </div>
    </div>

  );
};

export default Info;
```
### 마운트될 때만 실행
화면에 맨 처음 렌더링될 때만 실행, 업데이트 시에는 제외
두 번째 파라미터로 빈 배열
```jsx
import React, { useEffect, useState } from 'react';

const Info = () => {
  const [name, setName] = useState('');
  const [nickname, setNickname] = useState('');

  useEffect(() => {
    console.log('마운트될 때만 실행');
  }, []);
  const onChangeName = e => {
    setName(e.target.value);
  };

  const onChangeNickname = e => {
    setNickname(e.target.value);
  };

  return (
    <div>
      <div>
        <input value={name} onChange={onChangeName} />
        <input value={nickname} onChange={onChangeNickname} />
      </div>
      <div>
        <div>
          <b>이름 : </b> {name}
        </div>
        <div>
          <b>닉네임: </b> {nickname}
        </div>
      </div>
    </div>

  );
};

export default Info;
```

### 특정 값이 업데이트될 때만 실행
특정 값이 변경될 때만 호출
두 번쨰 파라미터에 전달되는 배열 안에 검사하고 싶은 값
```jsx
import React, { useEffect, useState } from 'react';

const Info = () => {
  const [name, setName] = useState('');
  const [nickname, setNickname] = useState('');

  useEffect(() => {
    console.log('name update시에만 실행');
  }, [name]);
  const onChangeName = e => {
    setName(e.target.value);
  };

  const onChangeNickname = e => {
    setNickname(e.target.value);
  };

  return (
    <div>
      <div>
        <input value={name} onChange={onChangeName} />
        <input value={nickname} onChange={onChangeNickname} />
      </div>
      <div>
        <div>
          <b>이름 : </b> {name}
        </div>
        <div>
          <b>닉네임: </b> {nickname}
        </div>
      </div>
    </div>

  );
};

export default Info;
```

### 뒷정리
언마운트되기 전이나 업데이트되기 직전에 수행
```jsx
useEffect(() => {
  console.log('effect');
  console.log('effect : ', name);
  return () => {
    console.log('clean');
    console.log('clean :', name);
  }
});
```
```jsx
import React, { useState } from 'react';
import Counter from './component/chap8/Counter';
import Info from './component/chap8/Info';

const App = () => {
  const [visible, setVisible] = useState(false);
  return (
    <div>
      <button
        onClick={() => {
          setVisible(!visible);
        }}
      >
        {visible ? '숨기기' : '보이기'}
      </button>
      <hr/>
      {visible && <Info/>}
    </div>
  );
};

export default App;
```

렌더링될 떄마다 뒷정리 함수가 계속 호출되며 뒷정리 함수가 호출될 때에는 업데이트됙 직전의 값을 보여준다.

오직 언마운트될 때만 호출하고 싶다면 빈 배열을 넣는다.
```jsx
useEffect(() => {
  console.log('effect');
  console.log('effect : ', name);
  return () => {
    console.log('clean');
    console.log('clean :', name);
  }
}, []);
```
## useReducer

```jsx
import React, { useReducer } from 'react';

function reducer(state, action) {
  switch (action.type) {
    case 'INCREMENT':
      return { value: state.value + 1};
    case 'DECREMENT':
      return { value: state.value - 1};
    default:
      return state;
  }
}

const Counter = () => {
  
  const [state, dispatch] = useReducer(reducer, {value: 0});

  return (
    <div>
      <p>
        현재 카운터 값은 <b>{state.value}</b>입니다.
      </p>
      <button onClick={() => dispatch({type: 'INCREMENT'})}>+1</button>
      <button onClick={() => dispatch({type: 'DECREMENT'})}>-1</button>
    </div>
  );
};

export default Counter;
```
```jsx
import React, { useState } from 'react';
import Counter from './component/chap8/Counter';

const App = () => {
  return (
    <Counter/>
  );
};

export default App;
```

### 인풋 상태 관리
```jsx
import React, { useReducer } from 'react';

function reducer(state, action) {
  return {
    ...state,
    [action.name]: action.value
  };
}

const Info = () => {
  const [state, dispatch] = useReducer(reducer, {
    name: '',
    nickanme: ''
  });

  const {name, nickname} = state;
  const onChange = e => {
    dispatch(e.target);
  };

  return (
    <div>
      <div>
        <input name="name" value={name} onChange={onChange} />
        <input name="nickname" value={nickname} onChange={onChange} />
      </div>
      <div>
        <div>
          <b>이름 : </b> {name}
        </div>
        <div>
          <b>닉네임: </b> {nickname}
        </div>
      </div>
    </div>

  );
};

export default Info;
```

## useMemo
함수형 컴포넌트 내부에서 발생하는 연산을 최적화할 수 있다.

```jsx
import React, { useState } from 'react';

const getAverage = numbers => {
  console.log('평균값 계산 중');
  if (numbers.length === 0 ) return 0;
  const sum = numbers.reduce((a,b) => a + b);
  return sum / numbers.length;
};

const Average = () => {
  const [list, setList] = useState([]);
  const [number, setNumber] = useState('');

  const onChange = e => {
    setNumber(e.target.value);
  };

  const onInsert = e => {
    const nextList = list.concat(parseInt(number));
    setList(nextList);
    setNumber('');
  };

  return (
    <div>
      <input value={number} onChange={onChange} />
      <button onClick={onInsert}>등록</button>
      <ul>
        {list.map((value, index) => (
          <li key={index}>{value}</li>
        ))}
      </ul>
      <div>
        <b>평균값:</b> {getAverage(list)}
      </div>
    </div>
  );
};

export default Average;
```
등록뿐만 아니라 인풋 내용이 수정될 때에도 getAverage 함수가 호출된다.

useMemo를 통해 최적화 할수 있다. 특정 값이 바뀌었을 때만 연산을 실행하고 원하는 값이 바뀌지 않았다면 이전에 연산했던 결과를 다시 사용
```jsx
import React, { useMemo, useState } from 'react';

const getAverage = numbers => {
  console.log('평균값 계산 중');
  if (numbers.length === 0 ) return 0;
  const sum = numbers.reduce((a,b) => a + b);
  return sum / numbers.length;
};

const Average = () => {
  const [list, setList] = useState([]);
  const [number, setNumber] = useState('');

  const onChange = e => {
    setNumber(e.target.value);
  };

  const onInsert = e => {
    const nextList = list.concat(parseInt(number));
    setList(nextList);
    setNumber('');
  };

  const avg = useMemo(() => getAverage(list), [list]);

  return (
    <div>
      <input value={number} onChange={onChange} />
      <button onClick={onInsert}>등록</button>
      <ul>
        {list.map((value, index) => (
          <li key={index}>{value}</li>
        ))}
      </ul>
      <div>
        <b>평균값:</b> {avg}
      </div>
    </div>
  );
};

export default Average;
```

## useCallback
렌더링 성능을 최적화해야 하는 상황에서 사용, 만들어두었던 함수를 재사용 
```jsx
import React, { useCallback, useMemo, useState } from 'react';

const getAverage = numbers => {
  console.log('평균값 계산 중');
  if (numbers.length === 0 ) return 0;
  const sum = numbers.reduce((a,b) => a + b);
  return sum / numbers.length;
};

const Average = () => {
  const [list, setList] = useState([]);
  const [number, setNumber] = useState('');

  const onChange = useCallback(e => {
    setNumber(e.target.value);
  }, []); // 컴포넌트가 처음 렌더링될 때만 함수 생성
 
  const onInsert = useCallback(() => {
    const nextList = list.concat(parseInt(number));
    setList(nextList);
    setNumber('');
  }, [number, list]); // number 혹은 list가 바뀌었을 때만 함수 생성

  const avg = useMemo(() => getAverage(list), [list]);

  return (
    <div>
      <input value={number} onChange={onChange} />
      <button onClick={onInsert}>등록</button>
      <ul>
        {list.map((value, index) => (
          <li key={index}>{value}</li>
        ))}
      </ul>
      <div>
        <b>평균값:</b> {avg}
      </div>
    </div>
  );
};

export default Average;
```

## useRef
??

## 커스텀 Hooks

```jsx
import { useReducer } from 'react';

function reducer(state, action) {
  return {
    ...state,
    [action.name]: action.value
  };
}

export default function useInputs(init) {
  const [state, dispatch] = useReducer(reducer, init);
  const onChange = e => {
    dispatch(e.target);
  };
  return [state, onChange];
}
```
```jsx
import React from 'react';
import useInputs from './userInputs';

const Info = () => {
  const [state, onChange] = useInputs({
    name: '',
    nickanme: ''
  });

  const {name, nickname} = state;
  
  return (
    <div>
      <div>
        <input name="name" value={name} onChange={onChange} />
        <input name="nickname" value={nickname} onChange={onChange} />
      </div>
      <div>
        <div>
          <b>이름 : </b> {name}
        </div>
        <div>
          <b>닉네임: </b> {nickname}
        </div>
      </div>
    </div>

  );
};

export default Info;
```