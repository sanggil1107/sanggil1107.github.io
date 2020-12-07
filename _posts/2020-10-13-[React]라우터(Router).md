---
layout: post
title: "[React] 라우터(Router)"
category: [React]

---
<br>

`라우터`에 대해 알아보자
<!-- more -->

<hr>

# Router
## Route 컴포넌트로 특정 주소에 컴포넌트 연결
```jsx
<Route path="주소규칙" component={컴포넌트} />
```
```jsx
import React from 'react';

const Home = () => {
  return (
    <div>
      <h1>홈</h1>
      <p>홈페이지</p>
    </div>
  );
};

export default Home;
```
```jsx
import React from 'react';

const About = () => {

  return (
    <div>
      <h1>소개</h1>
      <p>About me</p>
    </div>
  );
};

export default About;
```
```jsx
import React from 'react';
import { Route } from 'react-router-dom';
import About from './component/chap11/About';
import Home from './component/chap11/Home';

const App = () => {
  return (
    <div>
      <Route path="/" component={Home} exact={true}/>
      <Route path="/about" component={About} />
    </div>
  );
};

export default App;
```

## Link
```jsx
<Link to="주소">내용</Link>
```
```jsx
import React from 'react';
import { Link, Route } from 'react-router-dom';
import About from './component/chap11/About';
import Home from './component/chap11/Home';

const App = () => {
  return (
    <div>
      <ul>
        <li>
          <Link to="/">홈</Link>
        </li>
        <li>
          <Link to="/about">소개</Link>
        </li>
      </ul>
      <hr/>
      <Route path="/" component={Home} exact={true}/>
      <Route path={["/about", "/info"]} component={About} /> 
    </div>
  );
};

export default App;
```

## Switch
여러 Route 중 일치하는 단 하나의 라우트만 렌더링시켜 준다.
```jsx
import React from 'react';
import { Link, Route, Switch } from 'react-router-dom';
import About from './component/chap11/About';
import Home from './component/chap11/Home';

const App = () => {
  return (
    <div>
      <ul>
        <li>
          <Link to="/">홈</Link>
        </li>
        <li>
          <Link to="/about">소개</Link>
        </li>
      </ul>
      <hr/>
      <Switch>
        <Route path="/" component={Home} exact={true}/>
        <Route path={["/about", "/info"]} component={About} />
        <Route render={({location}) => (
          <div>
            <h2>존재하지 않는 페이지 입니다.</h2>
            <p>{location.pathname}</p>
          </div>
        )} />
      </Switch>
    </div>
  );
};

export default App;
```
http://localhost:3000/no 로 접속 시 "존재하지 않는 페이지 입니다." 문구를 확인할 수 있다.

## Route 하나에 여러 개의 path 설정
```jsx
import React from 'react';
import { Link, Route } from 'react-router-dom';
import About from './component/chap11/About';
import Home from './component/chap11/Home';

const App = () => {
  return (
    <div>
      <ul>
        <li>
          <Link to="/">홈</Link>
        </li>
        <li>
          <Link to="/about">소개</Link>
        </li>
      </ul>
      <hr/>
      <Route path="/" component={Home} exact={true}/>
      <Route path={["/about", "/info"]} component={About} />
    </div>
  );
};

export default App;
```
## URL 파라미터와 쿼리

### URL 파라미터
```jsx
import React from 'react';
import { Link, Route } from 'react-router-dom';
import About from './component/chap11/About';
import Home from './component/chap11/Home';
import Profile from './component/chap11/Profile';

const App = () => {
  return (
    <div>
      <ul>
        <li>
          <Link to="/">홈</Link>
        </li>
        <li>
          <Link to="/about">소개</Link>
        </li>
        <li>
          <Link to="/profile/yang">yang 프로필</Link>
        </li>
        <li>
          <Link to="/profile/sanggil">sanggil 프로필</Link>
        </li>
      </ul>
      <hr/>
      <Route path="/" component={Home} exact={true}/>
      <Route path={["/about", "/info"]} component={About} />
      <Route path="/profile/:username" component={Profile} />
    </div>
  );
};

export default App;
```
```jsx
import React from 'react';

const data = {
  yang: {
    name: '양상길',
    description: '리액트 개발자 - yang'
  },
  sanggil: {
    name: '양상길',
    description: '리액트 개발자 - sanggil'
  }
};

const Profile = ({match}) => {
  const {username} = match.params;
  const profile = data[username];
  if (!profile) {
    return <div>존재하지 않는 사용자입니다.</div>
  }
  return (
    <div>
      <h3>
        {username}({profile.name})
      </h3>
      <p>{profile.description}</p>
    </div>
  );
};

export default Profile
```
### URL 쿼리
```jsx
import React from 'react';
import qs from 'qs';

const About = ({location}) => {
  const query = qs.parse(location.search, {
    ignoreQueryPrefix: true
  });
  const showDetail = query.detail === 'true';
  return (
    <div>
      <h1>소개</h1>
      <p>About me</p>
      {showDetail && <p>detail 값을 true로 설정</p>}
    </div>
  );
};
```
export default About;

## 서브 라우트
```jsx
import React from 'react';
import { Link, Route } from 'react-router-dom';
import Profile from './Profile';

const Profiles = () => {
  return (
    <div>
      <h3>사용자 목록:</h3>
      <ul>
        <li>
          <Link to="/profiles/yang">yang</Link>
        </li>
        <li>
          <Link to="/profiles/sanggil">sanggil</Link>
        </li>
      </ul>

      <Route path="/profiles" exact render={() => <div>사용자를 선택하세요</div>} />
      <Route path="/profiles/:username" component={Profile} />
    </div>
  );
};

export default Profiles
```
```jsx
import React from 'react';
import { Link, Route } from 'react-router-dom';
import About from './component/chap11/About';
import Home from './component/chap11/Home';
import Profiles from './component/chap11/Profiles';

const App = () => {
  return (
    <div>
      <ul>
        <li>
          <Link to="/">홈</Link>
        </li>
        <li>
          <Link to="/about">소개</Link>
        </li>
        <li>
          <Link to="/profiles"> 프로필</Link>
        </li>
      </ul>
      <hr/>
      <Route path="/" component={Home} exact={true}/>
      <Route path={["/about", "/info"]} component={About} />
      <Route path="/profiles" component={Profiles} />
    </div>
  );
};

export default App;
```

## 부가 기능
