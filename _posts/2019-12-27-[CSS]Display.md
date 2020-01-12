---
layout: post
title: "[CSS] Display"
category: [CSS]

---
<br>

`Display` 속성에 대해 알아보자
<!-- more -->

<hr>

# Display
---
브라우저가 요소를 화면에 나타내는 방법을 제어하는 속성으로 layout 정의에 자주 사용되는 속성이다.

- `block` : block 특성을 가지는 요소
- `inline` : inline 특성을 가지는 요소
- `inline-block` : inline-block 특성을 가지는 요소
- `none` : 요소를 화면에 표시하지 않는다.(공간까지 사라진다.)

## block
---
block 요소는 다음과 같다.
- 항상 새로운 줄에서 시작된다.(줄바꿈 된다.)
- 화면 전체 크기의 가로폭을 차지하며(width:100%) 높이는 콘텐츠 크기만큼 적용된다.
- widht, height, margin, padding 속성 지정이 가능하다.
- block 요소 내에 inline 요소를 포함할 수 있다.
- `div, h1~6, p, ol, ul, li, hr, table, form`

```html
<html>
    <head>
        <style>
            #default {
                /*display: block;  default 속성 */            
                background-color: brown;
            }
            #width {
                /*display: block;  default 속성 */               
                background-color: blue;
                width: 500px;
            }
        </style>
    </head>
    <body>
        <div id="default">
            <p>block 요소</p>
            <p>초기값</p>
        </div>        
        <div id="width">
            <p>block 요소</p>
            <p>넓이 지정</p>  
        </div>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/css/block.PNG" >
<br>

## inline
---
inline 요소는 다음과 같다.
- 줄바꿈을 하지 않는다.
- 가로폭과 높이는 컨텐츠 크기만큼 적용된다.
- width, height, margin-top, margin-bottom 속성 지정이 불가능하다.
- inline 요소는 block 요소 내에 쓰일 수 없다.
- `span, a, strong, img, br, input, select, textarea, button

```html
<html>
    <head>
        <style>
            #box {
                border: 8px solid black;
            }
            #box span {
                width: 500px;
                height: 600px;
                border: 5px solid blue;
            }
            #box a {
                padding: 30px;
                margin: 30px;
                border: 5px solid red;
            }
            #box strong {
                border: 5px solid skyblue;
            }
        </style>
    </head>
    <body>
        <h1>inline 요소</h1>
        <div id="box">
            <span>인라인</span>
            <a>인라인</a>
            <strong>인라인</strong>
        </div>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/css/inline.PNG" >
<br>

## inline-block
---
inline-block 요소는 다음과 같다.
- block과 inline 요소의 특징을 모두 갖는다.
- 줄바꿈을 하지 않으며(inline) width, height, margin, padding 속성 지정이 가능하다.(block) 
- 가로폭은 컨텐츠 크기만큼 적용된다.(inline)

```html
<html>
    <head>
        <style>
            #box, #box1 {
                border: 8px solid black;
            }
            #box span {
                display: inline-block;
                width: 100px;
                height: 100px;
                border: 5px solid blue;
            }
            #box a {
                display: inline-block;
                padding: 30px;
                margin: 30px;
                border: 5px solid red;
            }
            #box strong {
                display: inline-block;
                border: 5px solid skyblue;
            }
            #box1 h3 {
                display: inline-block;
                width: 200px;
                height: 200px;
                border: 5px dotted green;
            }
            #box1 div {
                display: inline-block;
                margin: 20px;
                padding: 20px;
                border: 5px dotted purple;
            }
            #box1 p {
                display: inline-block;
                border: 5px dotted tomato;
            }
        </style>
    </head>
    <body>
        <h1>inline-block 요소</h1>
        <div id="box">
            <span>inline-block(span)</span>
            <a>inline-block(a)</a>
            <strong>inline-block(strong)</strong>
        </div>
        <br><br>
        <div id="box1">
            <h3>inline-block(h3)</h3>
            <div>inline-block(div)</div>
            <p>inline-block(p)</p>        
        </div>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/css/inline-block.PNG" >
<img src="https://sanggil1107.github.io//public/img/css/inline-block1.PNG" >
<br>

# Visibility
---
요소를 보이게 할지 보이지 않게 할지, 요소의 렌더링 여부를 결정하는 속성이다.

- `visible` : 요소를 보이게 한다.
- `hidden` : 요소를 보이지 않게 한다.(공간은 남아 있다.)
- `collapse` : table 요소에 사용하며, 행이나 열을 보이지 않게 한다.

```html
<html>
    <head>
        <style>
            div {
                height: 50px;
                border: 1px solid black;
                margin-bottom: 5px;
            }
            div.visibility {
                visibility: visible;
            }
            div.hidden {
                visibility: hidden;
            }
            .collapse {
                visibility: collapse;
            }
        </style>
    </head>
    <body>
        <h1>visibility 요소</h1>
        <div class="visibility">visibility</div>
        <div class="hidden">hidden</div>
        <table border="1">
            <tr>
                <td>1</td>
                <td class="collapse">2</td>
            </tr>
            <tr>
                <td>3</td>
                <td>4</td>
            </tr>
        </table>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/css/visibility.PNG" >
<br>

# Opacity
---
요소의 투명도를 나타내는 속성이며 0.0(투명) ~ 1.0(불투명) 값을 가진다.

```html
<html>
    <head>
        <style>
            img {
                width: 400px;
                height: 400px;
            }
            .Opacity {
                opacity: 0.4;
            }
            .Opacity1 {
                opacity: 1.0;
            }
        </style>
    </head>
    <body>
        <h1>Opacity 요소</h1>
        <img class="Opacity" src="../HTML/mountain.png">
        <img class="Opacity1" src="../HTML/mountain.png">
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/css/opacity.PNG" >
<br>
