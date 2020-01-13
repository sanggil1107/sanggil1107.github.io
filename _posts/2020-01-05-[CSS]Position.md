---
layout: post
title: "[CSS] Position"
category: [CSS]

---
<br>

`Position` 속성에 대해 알아보자
<!-- more -->

<hr>


# position
---

## static
---
`static` 은 position 속성의 기본값으로 부모 요소 내에 자식 요소로 존재할 경우 부모 요소의 위치를 기준으로 배치된다.  
좌표 속성(top, bottom, left, right)이 적용되지 않는다.(사용할 경우 무시)

```html
<html>
    <head>
        <style>
            div {
                border: 1px solid tomato;
                width: 150px;
                height: 150px;                
            }
            #parent {
                background-color: gray;
            }
            #me {
                background-color: black;
                color: white;
                position: static;
                left: 100px;
                top: 100px;
            }
        </style>
    </head>
    <body>
        <div id="parent">
            parent
            <div id="me">me</div>
        </div>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/css/static.PNG" >
<br>

me 라는 자식요소에 left, top 값을 지정해주었지만 적용되지 않았다.

## relative
---
`relative` 는 기본 위치(`static`)를 기준으로 좌표 속성(top, bottom, left, right) 만큼 위치한다.  
상대적 위치인 만큼 자식 요소의 경우 부모 위치를 기준(기본 위치)으로 이동한다.

```html
<html>
    <head>
        <style>
            div {
                border: 1px solid tomato;
                width: 150px;
                height: 150px;         
            }
            #parent {
                background-color: gray;
                position: relative;
                left: 50px;
            }
            #me {
                background-color: black;
                color: white;
                position: relative;
                left: 100px;
                top: 100px;
            }
        </style>
    </head>
    <body>
        <div id="parent">
            parent
            <div id="me">me</div>
        </div>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/css/relative.PNG" >
<br>

me 라는 자식 요소에 `position: relative` 값과 left, top 값을 지정한 만큼 이동하였다.

## absolute
---
`absolute` 는 부모 요소나 가장 가까이 있는 조상 요소를 기준으로 좌표 속성(top, bottom, left, right) 만큼 위치한다.  
- 부모 요소나 조상 요소의 position 이 relative, absolute, fixed 로 선언되어 있을 때 부모 요소나 조상 요소를 기준으로 위치한다.
- 부모 요소나 조상 요소의 position 이 static인 경우, html body 요소를 기준으로 위치한다. 
```html
<html>
    <head>
        <style>
            div {
                border: 1px solid tomato;           
            }
            #grand {
                width: 200px;
                height: 200px;
            }
            #parent {
                width: 180px;
                height: 180px;
                background-color: gray;
            }
            #me {
                width: 150px;
                height: 150px;
                background-color: black;
                color: white;
                position: absolute;
                left: 5px;
                top: 5px;
            }
        </style>
    </head>
    <body>
        <div id="grand">
            grand
            <div id="parent">
                parent
                <div id="me">me</div>
            </div>
        </div>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/css/absolute.PNG" >
<br>

me 라는 자식 요소에 `position: absolute` 값과 left, top 값을 지정하였고 이 때, 부모/조상 요소의 `postion` 이 모두 static 이므로 부모 요소 기준이 아닌 html body 요소를 기준으로 위치하게 된다.  

만약 좌표 속성을 지정하지 않는다면 기본 위치(`static`)를 기준으로 위치한다.
```html
<html>
    <head>
        <style>
            div {
                border: 1px solid tomato;           
            }
            #grand {
                width: 200px;
                height: 200px;
            }
            #parent {
                width: 180px;
                height: 180px;
                background-color: gray;
            }
            #me {
                width: 150px;
                height: 150px;
                background-color: black;
                color: white;
                position: absolute;
            }
        </style>
    </head>
    <body>
        <div id="grand">
            grand
            <div id="parent">
                parent
                <div id="me">me</div>
            </div>
        </div>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/css/absolute1.PNG" >
<br>

```html
<html>
    <head>
        <style>
            div {
                border: 1px solid tomato;           
            }
            #grand {
                width: 200px;
                height: 200px;
            }
            #parent {
                width: 180px;
                height: 180px;
                background-color: gray;
                position: relative;
            }
            #me {
                width: 150px;
                height: 150px;
                background-color: black;
                color: white;
                position: absolute;
                left: 20px;
                top: 0;
            }
        </style>
    </head>
    <body>
        <div id="grand">
            grand
            <div id="parent">
                parent
                <div id="me">me</div>
            </div>
        </div>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/css/absolute2.PNG" >
<br>

부모/조상 요소의 position 값이 static이 아닌 relative 이므로 부모 요소인 parent를 기준으로 me 의 위치가 정해진다.  
만약 조상 요소인 grand 에 static이 아닌 position 값이 있고 부모 요소인 parent에 없다면 아래와 같이 조상 요소인 grand를 기준으로 한다.  

<img src="https://sanggil1107.github.io//public/img/css/absolute3.PNG" >
<br>


## fixed
---
`fixed` 는 부모/조상 요소에 관계 없이 html body를 기준으로 좌표 속성(top, bottom, left, right) 만큼 위치한다.  
스크롤이 되더라도 위치에서 사라지지 않고 항상 같은 위치에 고정되어 있다.  
좌표 속성 값이 없다면 기본 위치(`static`)를 기준으로 위치한다.

```html
<html>
    <head>
        <style>
            div {
                border: 1px solid tomato;           
            }
            #grand {
                width: 200px;
                height: 200px;
            }
            #parent {
                width: 180px;
                height: 180px;
                background-color: gray;
                position: relative;
            }
            #me {
                width: 150px;
                height: 150px;
                background-color: black;
                color: white;
                position: fixed;
                left: 100px;
                top: 1px;
            }
        </style>
    </head>
    <body>
        <div id="grand">
            grand
            <div id="parent">
                parent
                <div id="me">me</div>
            </div>
        </div>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/css/fixed.PNG" >
<br>

부모 요소의 position 값에 관계 없이 좌표 속성이 지정되어 있다면 html body 요소를 기준으로 위치하며 항상 고정되어 있다.


# z-index
---
`z-index` 속성은 어느 요소가 앞으로 나오고, 뒤에 나올지 배치 순서를 결정하는 속성이다. static을 제외한 position 속성이 적용된 요소에서만 작동한다.
- 미적용 시 가장 마지막에 작성한 요소가 가장 상위에 배치된다.
- 양수, 음수 입력이 가능하며 값이 클수록 상위에 배치된다.

|속성 값|설명|
|:---:|:---:|
|auto|z-index를 지정하지 않은 값(기본값)|
|number|배치 순서를 결정, 클수록 상위에 배치|
|initial|기본값으로 설정|

코드 상 나중에 입력한 순서대로(z,y,x) 맨 위에 배치된다.
```html
<html>
    <head>
        <style>
            div {
                width: 100px;
                height: 100px;
                position: absolute;
            }
            .x {
                background-color: red;
                top: 20px;
                left: 60px;
            }
            .y {
                background-color: tomato;
                top: 50px;
                left: 20px;
            }
            .z {
                background-color: orange;
                top: 80px;
                left: 50px;
            }
        </style>
    </head>
    <body>
        <div class="x">x</div>
        <div class="y">y</div>
        <div class="z">z</div>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/css/zindex.PNG" >
<br>

x와 z 요소에 `z-index` 값을 지정하며 배치 순서를 변경하였다.
```html
<html>
    <head>
        <style>
            div {
                width: 100px;
                height: 100px;
                position: absolute;
            }
            .x {
                background-color: red;
                top: 20px;
                left: 60px;
                z-index: 10;
            }
            .y {
                background-color: tomato;
                top: 50px;
                left: 20px;
            }
            .z {
                background-color: orange;
                top: 80px;
                left: 50px;
                z-index: -1;
            }
        </style>
    </head>
    <body>
        <div class="x">x</div>
        <div class="y">y</div>
        <div class="z">z</div>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/css/zindex1.PNG" >
<br>

# overflow
---
`overflow` 속성은 자식 요소가 부모 요소의 영역을 벗어났을 때 처리하는 속성이다.

|속성 값|설명|
|:---:|:---:|
|visible|영역을 벗어난 부분을 표시(기본값)|
|hidden|영역을 벗어난 부분을 잘라내어 보이지 않게 함|
|scroll|영역을 벗어난 부분이 없어도 스크롤 표시|
|auto|영역을 벗어난 부분이 있을 때만 스크롤 표시|

```html
<html>
    <head>
        <style>
            div {
                width: 200px;
                height: 170px;
                border: 1px solid black;
                margin: 40px;
                padding: 5px;
                float: left;
            }
            .visible {
                overflow: visible;
            }
            .hidden {
                overflow: hidden;
            }
            .scroll {
                overflow: scroll;
            }
            .auto {
                overflow: auto;
            }
        </style>
    </head>
    <body>
        <h1>overflow</h1>
        <div class="visible"><h3>visible</h3>
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Officiis libero maxime assumenda repellat eaque voluptas amet pariatur ipsum ipsam, dolore soluta! Doloremque?
        </div>
        <div class="hidden"><h3>hidden</h3>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo, esse aliquam ex laboriosam nisi, atque modi eveniet, quae excepturi quaerat inventore voluptatum?
        </div>
        <div class="scroll"><h3>scroll</h3>
            Lorem ipsum dolor sit amet.
        </div>
        <div class="auto"><h3>auto</h3>
           Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fugiat asperiores maiores officiis sunt reiciendis, eaque beatae similique omnis, earum quae enim repellendus!
        </div>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/css/overflow.PNG" >
<br>