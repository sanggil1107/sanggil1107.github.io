---
layout: post
title: "[React] Redux"
category: [React]

---
<br>

`Redux`에 대해 알아보자
<!-- more -->
   
<hr>   
 

# Redux
## 액션
상태에 어떤 변화가 필요하면 액션(action)이란 것이 발생하며 이는 하나의 객체로 표현된다.
```jsx
{
  type: 'TOGGLE'
}
```
액션 객체는 type 필드를 반드시 가지고 있어야 하며, 그 외의 값들은 마음대로 추가해도 된다.

```jsx
{
  type: 'ADD_TODO',
  data: {
    id: 1,
    text: 'Redux'
  }
}
```

## 액션 생성 함
액션 생성 함수는 액션 객체를 만들어 주는 함수이다.

```jsx
const addtodo = data => ({
  type: 'ADD_TODO',
  data
});
```

## 리듀서
리듀서(reducer)는 변화를 일으키는 함수로 액션을 만들어 발생시키면 리듀서가 현재 상태와 전달받은 액션 객체를 파라미터로 받아온다.
두 값을 이용하여 새로운 상태를 만들어 반환한다.

```jsx
const initialState = {
  counter: 1
};

function reducer(state = inittialState, action) {
  switch (action.type) {
    case INCREMENT:
      return {
        counter: state.counter + 1
      };
    default:
      return state;
  }
}
```

## 스토어
프로젝트에 Redux를 적용하기 위해 스토어를 만들며 한 개의 프로젝트는 한개의 스토어만 가질 수 있다. 또한, 스토어 안에는 현재 애플리케이션 상태와 리듀서가 들어가 있다.

## 디스패치
디스패치(dispatch)는 스토어의 내장 함수 중 하나로 액션을 발생시킨다. `dispatch(action)` 과 같은 형태로 액션 객체를 파라미터로 받는다.
디스패치가 호출되면 스토어는 리듀서 함수를 실행하여 새로운 상태를 만든다.

## 구독
구독(subscribe) 역시 스토어의 내장 함수 중 하나로 `subscribe` 함수 안에 리스너 함수를 파라미터로 넣고 호출하면, 리스너 함수가 디스패치되어 상태가 업데이트될 때마다 호출된다.


## 실습
```jsx
import React from 'react';

const Counter = ({number, onIncrease, onDecrease}) => {
  return (
    <div>
      <h1>{number}</h1>
      <div>
        <button onClick={onIncrease}></button>
        <button onClick={onDecrease}></button>
      </div>
    </div>
  );
};

export default Counter;
```

```jsx
import React from 'react';

const TodoItem = ({todo, onToggle, onRemove}) => {
  return (
    <div>
      <input type="checkbox"/>
      <span>예제 텍스트</span>
      <button>삭제</button>
    </div>
  );
};

const Todos = ({input, todos, onChangeInput, onInsert, onToggle, onRemove}) => {
  const onSubmit = e => {
    e.preventDefault();
  };
  return (
    <div>
      <form onSubmit={onSubmit}>
        <input/>
        <button type="submit">등록</button>
      </form>
      <div>
        <TodoItem/>
        <TodoItem/>
        <TodoItem/>
        <TodoItem/>
        <TodoItem/>
      </div>
    </div>
  );
};

export default Todos;
```
```jsx
import React from 'react';
import Counter from './component/chap14/Counter';
import Todos from './component/chap14/Todos';

const App = () => {
  return (
    <div>
      <Counter number={0}/>
      <hr/>
      <Todos/>
    </div>
  );
};

export default App;
```

counter 모듈 작성
```jsx
const INCREASE = 'counter/INCREASE';
const DECREASE = 'counter/DECREASE';

export const increase = () => ({ type: INCREASE });
export const decrease = () => ({ type: DECREASE });

const initialState = {
  number: 0
};

function counter(state = initialState, action) {
  switch (action.type) {
    case INCREASE:
      return {
        number: state.number + 1
      };
    case DECREASE:
      return {
        number: state.number - 1
      };
    default:
      return state;
  }
}

export default counter;
```
todos 모듈
```jsx
const CHANGE_INPUT = 'todos/CHANGE_INPUT';
const INSERT = 'todos/INSERT';
const TOGGLE = 'todos/TOGGLE';
const REMOVE = 'todos/REMOVE';

export const changeInput = input => ({
  type: CHANGE_INPUT,
  input
});

let id = 3;
export const insert = text => ({
  type: INSERT,
  todo: {
    id: id++,
    text,
    done: false
  }
});

export const toggle = id => ({
  type: TOGGLE,
  id
});

export const remove = id => ({
  type: REMOVE,
  id
});

const initialState = {
  input: '',
  todos: [
    {
      id: 1,
      text: 'redux 기초',
      done: true
    },
    {
      id: 2,
      text: 'redux 사용',
      done: false
    }
  ]
};

function todos(state = initialState, action) {
  switch (action.type) {
    case CHANGE_INPUT:
      return {
        ...state,
        input: action.input
      };
    case INSERT:
      return {
        ...state,
        todos: state.todos.concat(action.todo)
      };
    case TOGGLE:
      return {
        ...state,
        todos: state.todos.map(todo => 
          todo.id === action.id ? { ...todo, done: !todo.done } : todo
        )
      };
    case REMOVE:
      return {
        ...state,
        todos: state.todos.filter(todo => todo.id !== action.id)
      }
    default:
      return state;
  }
}

export default todos;
```
루트 리듀서
스토어를 만들 때는 리듀서를 한 개만 사용해야 한다.
```jsx
import { combineReducers } from 'redux';
import counter from './counter';
import todos from './todos';

const rootReducer = combineReducers({
  counter,
  todos
});

export default rootReducer;
```
스토어 생성 및 리덕스 적용
```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { BrowserRouter } from 'react-router-dom';
import { createStore } from 'redux';
import rootReducer from './component/chap14/modules/index';
import { Provider } from 'react-redux';
import { composeWithDevTools } from 'redux-devtools-extension';

const store = createStore(rootReducer, composeWithDevTools());

ReactDOM.render(
  <Provider store={store}>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </Provider>,
  document.getElementById('root')
);

```

CounterContainer
```jsx
import React from 'react';
import Counter from '../Counter';
import { connect } from 'react-redux';
import { decrease, increase } from '../modules/counter';

const CounterContainer = ({number, increase, decrease}) => {
  return (
    <Counter number={number} onIncrease={increase} onDecrease={decrease}/>
  );
};

const mapStateToProps = state => ({
  number: state.counter.number,
});

const mapDispatchToProps = dispatch => ({
  increase: () => {
    console.log('increase');
    dispatch(increase());
  },
  decrease: () => {
    console.log('decrease');
    dispatch(decrease());
  }
});

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(CounterContainer);
```

```jsx
import React from 'react';
import Counter from '../Counter';
import { connect } from 'react-redux';
import { decrease, increase } from '../modules/counter';

const CounterContainer = ({number, increase, decrease}) => {
  return (
    <Counter number={number} onIncrease={increase} onDecrease={decrease}/>
  );
};

export default connect(
  state => ({
    number: state.counter.number,
  }),
  dispatch => ({
    increase: () => dispatch(increase()),
    decrease: () => dispatch(decrease())
  })
  )(CounterContainer);
```

TodosContainer
```jsx
import React from 'react';
import { connect } from 'react-redux';
import { changeInput, insert, toggle, remove } from '../modules/todos';
import Todos from '../Todos';

const TodosContainer = ({input, todos, changeInput, insert, toggle, remove}) => {
  return (
    <Todos input={input} todos={todos} onChangeInput={changeInput} onInsert={insert} onToggle={toggle} onRemove={remove} />
  );
};

export default connect(
  ({todos}) => ({
    input: todos.input,
    todos: todos.todos
  }),
  {
    changeInput,
    insert,
    toggle,
    remove
  }
)(TodosContainer);
```
```jsx

import React from 'react';
import CounterContainer from './component/chap14/containers/CounterContainer';
import TodosContainer from './component/chap14/containers/TodosContainer';

const App = () => {
  return (
    <div>
      <CounterContainer/>
      <hr/>
      <TodosContainer/>
    </div>
  );
};

export default App;
```
Todos.js
```jsx
import React from 'react';

const TodoItem = ({todo, onToggle, onRemove}) => {
  return (
    <div>
      <input 
        type="checkbox"
        onClick={() => onToggle(todo.id)}
        checked={todo.done}
        readOnly={true}
      />
      <span style={{textDecoration: todo.done ? 'line-through' : 'none'}}>
        {todo.text}
      </span>
      <button onClick={() => onRemove(todo.id)}>삭제</button>
    </div>
  );
};

const Todos = ({input, todos, onChangeInput, onInsert, onToggle, onRemove}) => {
  const onSubmit = e => {
    e.preventDefault();
    onInsert(input);
    onChangeInput('');
  };
  const onChange = e => onChangeInput(e.target.value);

  return (
    <div>
      <form onSubmit={onSubmit}>
        <input value={input} onChange={onchange}/>
        <button type="submit">등록</button>
      </form>
      <div>
        {todos.map(todo => (
          <TodoItem todo={todo} key={todo.id} onToggle={onToggle} onRemove={onRemove} />
        ))}
      </div>
    </div>
  );
};

export default Todos;
```
# redux-actions
counter
```jsx
import { createAction, handleActions } from 'redux-actions';

const INCREASE = 'counter/INCREASE';
const DECREASE = 'counter/DECREASE';

export const increase = createAction(INCREASE);
export const decrease = createAction(DECREASE);

const initialState = {
  number: 0
};

const counter = handleActions(
  {
    [INCREASE]: (state, action) => ({ number: state.number + 1}),
    [DECREASE]: (state, action) => ({ number: state.number - 1})
  },
  initialState
);

export default counter; 
```
todos
```jsx
import { createAction, handleActions } from 'redux-actions';

const CHANGE_INPUT = 'todos/CHANGE_INPUT';
const INSERT = 'todos/INSERT';
const TOGGLE = 'todos/TOGGLE';
const REMOVE = 'todos/REMOVE';

export const changeInput = createAction(CHANGE_INPUT, input => input);

let id = 3;
export const insert = createAction(INSERT, text => ({
  id: id++,
  text,
  done: false
}));

export const toggle = createAction(TOGGLE, id => id);
export const remove = createAction(REMOVE, id => id);

const initialState = {
  input: '',
  todos: [
    {
      id: 1,
      text: 'redux 기초',
      done: true
    },
    {
      id: 2,
      text: 'redux 사용',
      done: false
    }
  ]  
};

const todos = handleActions(
  {
    [CHANGE_INPUT]: (state, action) => ({
      ...state,
      input: action.payload
    }),
    [INSERT]: (state, action) => ({
      ...state,
      todos: state.todos.concat(action.payload)
    }),  
    [TOGGLE]: (state, action) => ({
      ...state,
      todos: state.todos.map(todo => 
        todo.id === action.payload ? { ...todo, done: !todo.done } : todo
      )
    }),
    [REMOVE]: (state, action) => ({
      ...state,
      todos: state.todos.filter(todo => todo.id !== action.payload)
    })
  },
  initialState
);

export default todos;
```
```jsx
(...)

const todos = handleActions(
  {
    [CHANGE_INPUT]: (state, { payload: input }) => ({
      ...state,
      input
    }),
    [INSERT]: (state, { payload: todo }) => ({
      ...state,
      todos: state.todos.concat(todo)
    }),
    [TOGGLE]: (state, { payload: id }) => ({
      ...state,
      todos: state.todos.map(todo => 
        todo.id === id ? { ...todo, done: !todo.done } : todo
      )
    }),
    [REMOVE]: (state, { payload: id }) => ({
      ...state,
      todos: state.todos.filter(todo => todo.id !== id)
    })
  },
  initialState
);

export default todos;
```

## useSelector / useDispatch
### useSelector
간단한 예시
### useDispatch
간단한 예시

```jsx
import React, { useCallback } from 'react';
import Counter from '../Counter';
import { useSelector, useDispatch } from 'react-redux';
import { decrease, increase } from '../modules/counter';

const CounterContainer = () => {
  const number = useSelector(state => state.counter.number);
  const dispatch = useDispatch();
  const onIncrease = useCallback(() => dispatch(increase()), [dispatch]);
  const onDecrease = useCallback(() => dispatch(decrease()), [dispatch]);
  return (
    <Counter number={number} onIncrease={onIncrease} onDecrease={onDecrease}/>
  );
};

export default CounterContainer;
```
```jsx
import React, { useCallback } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { changeInput, insert, toggle, remove } from '../modules/todos';
import Todos from '../Todos';

const TodosContainer = () => {
  const { input, todos } = useSelector(({todos}) => ({
    input: todos.input, 
    todos: todos.todos
  }));
  const dispatch = useDispatch();
  const onChangeInput = useCallback(input => dispatch(changeInput(input)), [dispatch]);
  const onInsert = useCallback(text => dispatch(insert(text)), [dispatch]);
  const onToggle = useCallback(id => dispatch(toggle(id)), [dispatch]);
  const onRemove = useCallback(id => dispatch(remove(id)), [dispatch]);
  
  return (
    <Todos input={input} todos={todos} onChangeInput={onChangeInput} onInsert={onInsert} onToggle={onToggle} onRemove={onRemove} />
  );
};

export default TodosContainer;
```