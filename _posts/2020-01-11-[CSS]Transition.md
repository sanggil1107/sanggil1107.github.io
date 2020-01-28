---
layout: post
title: "[CSS] Transition"
category: [CSS]

---
<br>

`Transition` 속성에 대해 알아보자
<!-- more -->

<hr>

# transition
---
`transition` 속성은 CSS 속성이 변화할 때 서서히 변화시키는 속성이다.

|속성|설명|기본값|
|:---:|:---:|:---:|
|transition-property|transition이 적용될 속성 지정|all|
|transition-duration|transition이 일어나는 지속시간(초, 밀리초)|0s|
|transition-delay|속성이 변화한 시점과 transition이 실제시작하는 사이에 대기 시간(초, 밀리초)|0s|
|transition-timing-function|transition 효과를 위한 함수 지정|ease|
|transition|transition 축약형| |

## transition-property
---
`transition-property` 속성은 transition이 적용될 CSS 속성을 지정한다.

|속성|설명|
|:---:|:---:|
|none|속성을 지정하지 않음|
|all|모든 속성에 적용|
|property|속성 지정, 여러 개의 경우 콤마(,)로 구분|
|inherit|부모 요소의 속성 값을 상속|

```html
<html>
    <head>
        <style>
            div {
                width: 200px;
                height: 200px;
                margin: 2px;
                background-color: red;
            }
            .property {
                transition-property: background-color;
                transition-duration: 3s;
            }
            .property1 {
                transition-property: width;
                transition-duration: 3s;
            }
            .all {
                transition-property: all;
                transition-duration: 3s;
            }
            input:checked ~div, div:hover {
                background-color: blue;
                width: 300px;
            } 
        </style>
    </head>
    <body>
        <h1>transition-property</h1>
        <input type="checkbox">
        <div class="property">background-color</div>
        <div class="property1">width</div>
        <div class="all">all</div>
    </body>
</html>
```
<p class="codepen" data-height="1000" data-theme-id="default" data-default-tab="result" data-user="omfazpiq" data-slug-hash="gObyJyv" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="gObyJyv">
  <span>See the Pen <a href="https://codepen.io/omfazpiq/pen/gObyJyv">
  gObyJyv</a> by 양상길 (<a href="https://codepen.io/omfazpiq">@omfazpiq</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

## transition-duration
---
`transition-duration` 속성은 transition이 일어나는 지속시간을 지정한다.(s, ms)  
transition-duration 속성은 transition-property 속성과 1:1로 대응한다.

```html
<html>
    <head>
        <style>
            div {
                width: 200px;
                height: 200px;
                margin: 2px;
                background-color: red;
            }
            .property {
                transition-property: background-color, width;
                transition-duration: 3s, 1s;
                box-sizing: border-box;
            }
            .property1 {
                transition-property: background-color, width, border;
                transition-duration: 4s, 2s, 0.5s;
                box-sizing: border-box;
            }
            .property2 {
                transition-property: background-color, width, border;
                transition-duration: 3s;
                box-sizing: border-box;
            }
            input:checked ~div, div:hover {
                background-color: blue;
                width: 300px;
                border: 8px dotted white;
            } 
        </style>
    </head>
    <body>
        <h1>transition-duration</h1>
        <input type="checkbox">
        <div class="property">3s, 1s</div>
        <div class="property1">4s, 2s, 0.5s</div>
        <div class="property2">3s</div>
    </body>
</html>
```
<p class="codepen" data-height="810" data-theme-id="default" data-default-tab="result" data-user="omfazpiq" data-slug-hash="zYxXQQG" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="zYxXQQG">
  <span>See the Pen <a href="https://codepen.io/omfazpiq/pen/zYxXQQG">
  zYxXQQG</a> by 양상길 (<a href="https://codepen.io/omfazpiq">@omfazpiq</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

## transition-timing-function
---
`transition-timing-function` 속성은 transition 효과를 지정한다.

|속성|설명|
|:---:|:---:|
|ease|느리게 시작하여 점점 빨라졌다가 느리게 종료(기본값)|
|linear|일정한 속도|
|ease-in|느리게 시작하여 특정 속도에 도달하면 일정하게 유지|
|ease-out|일정한 속도로 시작하다가 느려지면서 종료|
|ease-in-out|느리게 시작하여 점점 느려지면서 종료|

```html
<html>
    <head>
        <style>
            div {
                width: 100px;
                height: 100px;
                margin: 10px;
                background-color: red;
                transition-property: all;
                transition-duration: 1s;
            }
            .function {
                transition-timing-function: ease;
            }
            .function1 {
                transition-timing-function: linear;
            }
            .function2 {
                transition-timing-function: ease-in;
            }
            .function3 {
                transition-timing-function: ease-out;
            }
            .function4 {
                transition-timing-function: ease-in-out;
            }
            input:checked ~div, div:hover {
                background-color: blue;
                width: 300px;
            } 
        </style>
    </head>
    <body>
        <h1>transition-timing-function</h1>
        <input type="checkbox">
        <div class="function"">ease</div>
        <div class="function1">linear</div>
        <div class="function2">ease-in</div>
        <div class="function3">ease-out</div>
        <div class="function4">ease-in-out</div>
    </body>
</html>
```
<p class="codepen" data-height="780" data-theme-id="default" data-default-tab="result" data-user="omfazpiq" data-slug-hash="NWPmVVO" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="NWPmVVO">
  <span>See the Pen <a href="https://codepen.io/omfazpiq/pen/NWPmVVO">
  NWPmVVO</a> by 양상길 (<a href="https://codepen.io/omfazpiq">@omfazpiq</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

## transition-delay
---
`transition-delay` 속성은 속성이 변화한 시점과 transition이 실제 시작하는 사이에 대기 시간을 지정한다.(s, ms)

```html
<html>
    <head>
        <style>
            div {
                width: 200px;
                height: 200px;
                margin: 2px;
                background-color: red;
                transition-property: all;
                transition-duration: 1s;
            }
            .delay {
                transition-delay: 0.5s;
            }
            .delay1 {
                transition-delay: 1s;
            }
            .delay2 {
                transition-delay: 2s;
            }
            input:checked ~div, div:hover {
                background-color: blue;
                width: 300px;
            } 
        </style>
    </head>
    <body>
        <h1>transition-delay</h1>
        <input type="checkbox">
        <div class="delay">0.5s</div>
        <div class="delay1">1s</div>
        <div class="delay2">2s</div>
    </body>
</html>
```
<p class="codepen" data-height="810" data-theme-id="default" data-default-tab="result" data-user="omfazpiq" data-slug-hash="YzPMbox" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="YzPMbox">
  <span>See the Pen <a href="https://codepen.io/omfazpiq/pen/YzPMbox">
  YzPMbox</a> by 양상길 (<a href="https://codepen.io/omfazpiq">@omfazpiq</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

## transition
---
`transition` 속성은 transition 속성을 한 번에 지정할 수 있는 축약형이다.

```css
    transition: property duration function delay
```

```html
<html>
    <head>
        <style>
            div {
                width: 400px;
                height: 100px;
                margin: 2px;
                background-color: red;
            }
            .transition {
                transition: 1s;
            }
            .transition1 {
                transition: all 2s;
            }
            .transition2 {
                transition: width 1s 1s;
            }
            .transition3 {
                transition: 1s ease-in 0.5s;
            }
            .transition4 {
                transition: all 1s ease 1s;
            }
            input:checked ~div, div:hover {
                background-color: blue;
                width: 600px;
            } 
        </style>
    </head>
    <body>
        <h1>transition</h1>
        <input type="checkbox">
        <div class="transition">duration(1s)</div>
        <div class="transition1">property(all) duration(2s)</div>
        <div class="transition2">property(width) duration(1s) delay(1s)</div>
        <div class="transition3">duration(1s) function(ease-in) delay(0.5s)</div>
        <div class="transition4">property(all) duration(1s) function(ease) delay(1s)</div>
    </body>
</html>
```
<p class="codepen" data-height="750" data-theme-id="default" data-default-tab="result" data-user="omfazpiq" data-slug-hash="ZEYZNgz" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="ZEYZNgz">
  <span>See the Pen <a href="https://codepen.io/omfazpiq/pen/ZEYZNgz">
  ZEYZNgz</a> by 양상길 (<a href="https://codepen.io/omfazpiq">@omfazpiq</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>