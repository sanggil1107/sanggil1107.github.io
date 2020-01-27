---
layout: post
title: "[CSS] Animation"
category: [CSS]

---
<br>

`Animation`에 대해 알아보자
<!-- more -->

<hr>

# 애니메이션
---
`애니메이션` 효과는 CSS 스타일을 다른 CSS 스타일로부터 자연스럽고 부드럽게 변화시킨다. 애니메이션은 애니메이션을 나타내는 CSS 스타일과 애니메이션의 중간 상태를 나타내는 키프레임들로 이루어져 있다.


## @keyframes
---
`@keyframes` 속성은 CSS 애니메이션에서 구간을 정하고 각 구간별로 어떤 스타일을 적용시킬지 정한다.

```css
@keyframes name {
    0% { ... }
    n% { ... }
    100% { ... }
}
```
```css
@keyframes name {
    from { ... }
    to { ... }
}
```

```html
<html>
    <head>
        <style>
            div {
                position: absolute;
                border: 1px solid black;
                width: 100px;
                height: 100px;
                background-color: chartreuse;
                animation-name: moving;
                animation-duration: 5s;
                animation-iteration-count: infinite;
            }
            @keyframes moving {
                from {
                    left: 20px;
                }
                to {
                    left: 300px;
                }
            }
        </style>
    </head>
    <body>
        <h1>animation</h1>
        <div></div>
    </body>
</html>
```
<p class="codepen" data-height="265" data-theme-id="default" data-default-tab="result" data-user="omfazpiq" data-slug-hash="XWJebme" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="XWJebme">
  <span>See the Pen <a href="https://codepen.io/omfazpiq/pen/XWJebme">
  XWJebme</a> by 양상길 (<a href="https://codepen.io/omfazpiq">@omfazpiq</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

## animation
---
`animation` 속성은 애니메이션에 이름, 지속시간, 속도 등을 설정한다.

|속성|설명|값|
|:---:|:---:|:---:|
|animation-name|`@keyframes 애니메이션 이름을 지정| |
|animation-duration|한 번의 애니메이션에 소요되는 시간(초, 밀리초)|0s|
|animation-timing-function|애니메이션 효과를 위한 함수 지정|ease|
|animation-delay|요소가 로드된 시점과 애니메이션이 실제로 시작하는 사이의 대기시간(초, 밀리초)|0s|
|animation-iteration-count|애니메이션 재생 횟수|1|
|animation-direction|애니메이션 종료 후 반복될 때 진행 방향 지정(역방향, 처음)|normal|
|animation-fill-mode|애니메이션 실행 전/후(미실행 시점) 요소의 스타일 지정| |
|animation-play-state|애니메이션 상태를 지정(재생, 종료)|running|
|animation|모든 애니메이션 속성에 대한 축약 속성| |

## animation-name
---
`animation-name` 속성은 애니메이션에 대한 이름을 지정한다.  
`@keyframes 이름` 에 지정한 이름과 매핑이 되어야 하며 여러 개의 이름을 지정할 수 있다.

```html
<html>
    <head>
        <style>
            div {
                position: absolute;
                border: 1px solid black;
                width: 100px;
                height: 100px;
                background-color: chartreuse;
                animation-name: moving, borderchange, colorchange;
                animation-duration: 5s;
                animation-iteration-count: infinite;
            }
            @keyframes moving {
                from {
                    left: 20px;
                }
                to {
                    left: 300px;
                }
            }
            @keyframes borderchange {
                from {
                    border: 1px solid black;
                }
                to {
                    border-radius: 50%;
                }
            }
            @keyframes colorchange {
                0% {
                    background-color: chartreuse;
                }
                50% {
                    background-color: seagreen;
                }
                100% {
                    background-color: black;
                }
            }
        </style>
    </head>
    <body>
        <h1>animation</h1>
        <div></div>
    </body>
</html>
```
<p class="codepen" data-height="265" data-theme-id="default" data-default-tab="result" data-user="omfazpiq" data-slug-hash="XWJebme" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="XWJebme">
  <span>See the Pen <a href="https://codepen.io/omfazpiq/pen/XWJebme">
  XWJebme</a> by 양상길 (<a href="https://codepen.io/omfazpiq">@omfazpiq</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

## animation-duration
---
`animation-duration` 속성은 한 번의 애니메이션에 소요되는 시간을 지정한다.(초, 밀리 초)

```css
animation-duration: 2s;
animation-duration: 1000ms;
```

## animation-timing-function
`animation-timing-function` 속성은 애니메이션 효과를 위한 함수를 지정한다.


## animation-delay 
`animation-delay` 속성은 요소가 로드된 시점과 애니메이션이 실제로 시작하는 사이의 대기시간을 지정한다.(초, 밀리 초)  
첫 번째 반복에서만 적용된다.

```css
animation-delay: 2s;
animation-delay: 1000ms;
```

## animation-iteration-count
`animation-iteration-count` 속성은 애니메이션 재생 횟수를 지정하며 양수와 `infinite` (무한 반복)만 지정 가능하다.

```css
animation-iteration-count: 4;
animation-iteration-count: infinite;
```

### animation-direction
---
`animation-direction` 속성은 애니메이션의 사이클이 완료될 때, 반대 방향으로 애니메이션을 반복하거나 시작 상태로 재설정하여 애니메이션을 반복할 지 여부를 설정한다.

|값|설명|기본값|
|:---:|:---:|:---:|
|normal|from(0%)에서 to(100%) 방향으로 진행|`normal`|
|reverse|to(100%)에서 from(0%) 방향으로 진행| |
|alternate|홀수번째는 `normal` 로, 짝수번째는 `reverse` 로 진행| |
|alternate-reverse|홀수번째는 `reverse` 로, 짝수번째는 `normal` 로 진행| |

```html
<html>
    <head>
        <style>
            div {
                position: absolute;
                border: 1px solid black;
                width: 100px;
                height: 100px;
                background-color: chartreuse;
                animation-name: change;
                animation-duration: 5s;
                animation-iteration-count: infinite;
                animation-direction: alternate;
            }
            @keyframes change {
                0% {
                    background-color: chartreuse;
                    left: 20px;
                    top: 80px;
                }
                50% {
                    background-color: seagreen;
                    left: 200px;
                    top: 80px;
                }
                75% {
                    background-color: red;
                    left: 200px;
                    top: 200px;
                }
                100% {
                    background-color: black;
                    top: 200px;
                    left: 20px;
                }
            }
        </style>
    </head>
    <body>
        <h1>animation-direction</h1>
        <div></div>
    </body>
</html>
```
<p class="codepen" data-height="500" data-theme-id="default" data-default-tab="result" data-user="omfazpiq" data-slug-hash="XWJebme" style="height: 500px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="XWJebme">
  <span>See the Pen <a href="https://codepen.io/omfazpiq/pen/XWJebme">
  XWJebme</a> by 양상길 (<a href="https://codepen.io/omfazpiq">@omfazpiq</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

### animation-fill-mode
---
`animation-fill-mod` 속성은 애니메이션 실행 전/후(미실행 시점) 요소의 스타일을 지정한다.

|값|상태|설명
|:---:|:---:|:---:|
|none|대기|시작 프레임(from)에 설정한 스타일을 적용하지 않고 대기|
| |종료|애니메이션 실행 전 상태로 값을 되돌리고 종료|
|forwards|대기|시작 프레임(from)에 설정한 스타일을 적용하지 않고 대기|
| |종료|종료 프레임(to)에 설정한 스타일을 적용 후 종료|
|backwards|대기|시작 프레임(from)에 설정한 스타일을 대기|
| |종료|애니메이션 실행 전 상태로 값을 되돌리고 종료|
|both|대기|시작 프레임(from)에 설정한 스타일을 대기|
| |종료|종료 프레임(to)에 설정한 스타일을 적용 후 종료|


```html
<html>
    <head>
        <style>
            div {
                position: absolute;
                border: 1px solid black;
                width: 100px;
                height: 100px;
                background-color: chartreuse;
                animation-delay: 1s;
                animation-duration: 5s;
                animation-iteration-count: 1;
            }
            .none {           
                left: 20px;     
                animation-fill-mode: none;
                animation-name: change;
            }
            .forwards {
                left: 140px;
                animation-name: change1;
                animation-fill-mode: forwards;
            }
            .backwards {
                left: 260px;
                animation-name: change2;
                animation-fill-mode: backwards;
            }
            .both {
                left: 380px;
                animation-name: change3;
                animation-fill-mode: both;
            }
            @keyframes change {
                0% {
                    background-color: blue;
                    left: 20px;
                    top: 70px;
                }
                100% {
                    background-color: green;
                    top: 200px;
                    left: 20px;
                }
            }
            @keyframes change1 {
                0% {
                    background-color: blue;
                    left: 140px;
                    top: 70px;
                }
                100% {
                    background-color: green;
                    top: 200px;
                    left: 140px;
                }
            }
            @keyframes change2 {
                0% {
                    background-color: blue;
                    left: 260px;
                    top: 70px;
                }
                100% {
                    background-color: green;
                    top: 200px;
                    left: 260px;
                }
            }
            @keyframes change3 {
                0% {
                    background-color: blue;
                    left: 380px;
                    top: 70px;
                }
                100% {
                    background-color: green;
                    top: 200px;
                    left: 380px;
                }
            }
        </style>
    </head>
    <body>
        <h1>animation-fill-mode</h1>
        <div class="none">none</div>
        <div class="forwards">forwards</div>
        <div class="backwards">backwards</div>
        <div class="both">both</div>
    </body>
</html>
```
<p class="codepen" data-height="500" data-theme-id="default" data-default-tab="result" data-user="omfazpiq" data-slug-hash="XWJebme" style="height: 500px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="XWJebme">
  <span>See the Pen <a href="https://codepen.io/omfazpiq/pen/XWJebme">
  XWJebme</a> by 양상길 (<a href="https://codepen.io/omfazpiq">@omfazpiq</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

## animation-play-state
---
`animation-play-state` 속성은 애니메이션 재생 상태(재생, 중지)를 지정한다.  

|값|설명|기본값|
|:---:|:---:|:---:|
|running|재생|`running`|
|paused|중지| |

```html
<html>
    <head>
        <style>
            div {
                position: absolute;
                border: 1px solid black;
                width: 100px;
                height: 100px;
                background-color: chartreuse;
                animation-name: change;
                animation-duration: 5s;
                animation-iteration-count: 1;
                animation-iteration-count: infinite;
                animation-play-state: running;
            }
            @keyframes change {
                0% {
                    background-color: blue;
                    left: 20px;
                    top: 100px;
                }
                100% {
                    background-color: green;
                    top: 350px;
                    left: 20px;
                }
            }
            input:checked ~div {
                animation-play-state: paused;
            }
        </style>
    </head>
    <body>
        <h1>animation-play-state</h1>
        <input type="checkbox">paused
        <div></div>
    </body>
</html>
```
<p class="codepen" data-height="500" data-theme-id="default" data-default-tab="result" data-user="omfazpiq" data-slug-hash="XWJebme" style="height: 500px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="XWJebme">
  <span>See the Pen <a href="https://codepen.io/omfazpiq/pen/XWJebme">
  XWJebme</a> by 양상길 (<a href="https://codepen.io/omfazpiq">@omfazpiq</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

## animation
---
`animation` 속성은 모든 애니메이션 속성을 한 번에 지정하기 위한 축약 속성이다. 값을 지정하지 않으면 기본값이 지정되며, `animation-duration` 속성은 필수 값이다.

```css
animation: name duration time-function delay iteration-count direction fill-mode play-state
```