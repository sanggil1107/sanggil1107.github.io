---
layout: post
title: "[CSS] Transform"
category: [CSS]

---
<br>

`Transform` 속성에 대해 알아보자
<!-- more -->

<hr>


# transform
---
`transform` 속성은 이동, 회전, 축소 등의 효과를 지정하는 속성이다.

|속성|설명|단위|
|:---:|:---:|:---:|
|translate(x,y)|X축으로 x, Y축으로 y 이동|px, %, em|
|translateX(x)|X축으로 x 이동|px, %, em|
|translateY(y)|Y축으로 y 이동|px, %, em|
|scale(x,y)|X축으로 x배, Y축으로 y배 확대/축소|0, 양수|
|scaleX(x)|X축으로 x배 확대/축소|0, 양수|
|scaleY(y)|Y축으로 y배 확대/축소|0, 양수|
|skew(x, y)|X축으로 x 각도, Y축으로 y 각도 기울임|+, - deg|
|skewX(x)|X축으로 x 각도 기울임|+, - deg|
|skewY(y)|Y축으로 y 각도 기울임|+, - deg|
|rotate(x)|x 만큼 회전|+, - deg|

```html
<html>
    <head>
        <style>
            div {
                width: 110px;
                height: 110px;
                background-color: red;
                text-align: center;
                line-height: 110px;
                margin: 20px;
                margin-bottom: 10px;
                float: left;
                transition: all 1s;
            }
            input:checked ~.translate, .translate:hover {
                transform: translate(8px, 8px);
            }
            input:checked ~.translatex, .translatex:hover {
                transform: translateX(8px);
            }
            input:checked ~.translatey, .translatey:hover {
                transform: translateY(8px);
            }
            input:checked ~.scale, .scale:hover {
                transform: scale(1.2, 1.2);
            }
            input:checked ~.scalex, .scalex:hover {
                transform: scaleX(1.2);
            }
            input:checked ~.scaley, .scaley:hover {
                transform: scaleY(1.2);
            }
            input:checked ~.skew, .skew:hover {
                transform: skew(10deg, 10deg);
            }
            input:checked ~.skewx, .skewx:hover {
                transform: skewX(10deg);
            }
            input:checked ~.skewy, .skewy:hover {
                transform: skewY(10deg);
            }
            input:checked ~.rotate, .rotate:hover {
                transform: rotate(40deg);
            }
        </style>
    </head>
    <body>
        <h1>transform</h1>
        <input type="checkbox">
        <br>
        <div class="translate">translate</div>
        <div class="translatex">translateX</div>
        <div class="translatey">translateY</div>
        <div class="scale">scale</div>
        <div class="scalex">scaleX</div>
        <div class="scaley">scaleY</div>
        <div class="skew">skew</div>
        <div class="skewx">skewX</div>
        <div class="skewy">skewY</div>
        <div class="rotate">rotate</div>
    </body>
</html>
```
<p class="codepen" data-height="550" data-theme-id="default" data-default-tab="result" data-user="omfazpiq" data-slug-hash="eYmoaXO" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="eYmoaXO">
  <span>See the Pen <a href="https://codepen.io/omfazpiq/pen/eYmoaXO">
  eYmoaXO</a> by 양상길 (<a href="https://codepen.io/omfazpiq">@omfazpiq</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

## transform-origin
---
`transform-origin` 속성은 요소의 기준점을 지정한다. 기본값은 중앙(50%, 50%)이다.
- 값으로 %, px, top, left, right, bottom을 사용할 수 있다.
- 0, 0 은 top, left 를 100%, 100% 는 bottom, right와 같다.


```html
<html>
    <head>
        <style>
            div {
                width: 110px;
                height: 110px;
                background-color: red;
                text-align: center;
                line-height: 110px;
                margin: 20px;
                margin-bottom: 10px;
                float: left;
            }
            input:checked ~.translate, .translate:hover {
                transform-origin: 100% 100%;
                transform: translate(8px, 8px);
                transition: transform 1s;
            }
            input:checked ~.scale, .scale:hover {
                transform-origin: 0 0;
                transform: scale(1.2, 1.2);
                transition: transform 1s;
            }
            input:checked ~.skew, .skew:hover {
                transform-origin: 100% 100%;
                transform: skew(10deg, 10deg);
                transition: transform 1s;
            }
            input:checked ~.rotate, .rotate:hover {
                transform-origin: 0 50%;
                transform: rotate(40deg);
                transition: transform 1s;
            }
        </style>
    </head>
    <body>
        <h1>transform-origin</h1>
        <input type="checkbox">
        <br>
        <div class="translate">translate</div>
        <div class="scale">scale</div>
        <div class="skew">skew</div>
        <div class="rotate">rotate</div>
    </body>
</html>
```
<p class="codepen" data-height="400" data-theme-id="default" data-default-tab="result" data-user="omfazpiq" data-slug-hash="XWJebme" style="height: 500px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="XWJebme">
  <span>See the Pen <a href="https://codepen.io/omfazpiq/pen/XWJebme">
  XWJebme</a> by 양상길 (<a href="https://codepen.io/omfazpiq">@omfazpiq</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>