---
layout: post
title: "[CSS] Background"
category: [CSS]

---
<br>

`Background` 속성에 대해 알아보자
<!-- more -->

<hr>

# Background
---
요소의 배경의 색상, 이미지, 위칰, 반복 등의 설정을 위한 속성이다.

|속성|설명|기본값|
|:---:|:---:|:---:|
|background-color|배경색을 설정|`transparent`|
|background-image|요소의 배경 이미지 설정|`none`|
|background-repeat|배경의 반복 여부|`repeat`|
|background-position|배경이 요소 배경 안에 표시되어야 하는 위치 설정|`left top`|
|background-attachment|내용이 스크롤될 때 요소의 배경 동작 설정|`scroll`|
|background-size|배경 이미지의 크기를 동적으로 설정|`auto`|
|background|background 속성의 축약 속성| |
|background-clip|배경 이미지를 클리핑(오려내기) 하는 영역 설정|`border-box`|
|background-origin|배경 이미지의 시작 위치를 특정 영역으로 설정|`padding-box`|


## background-color
---
`background-color` 속성은 배경의 색상을 지정한다.
- 문서 안에 있는 거의 모든 요소에 배경색 지정 가능
- 상속되지 않으며 기본값은 투명(transparent)이다.

```html
<html>
    <head>
        <style>
            div {
                height: 300px;
                border: 5px solid gray;

                background-color: tomato; 
            }
        </style>
    </head>
    <body>
        <div>
            <h1>background-image</h1>    
        </div>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/css/bgcolor.PNG" >
<br>

## background-image
---
`background-image` 속성은 배경 이미지를 지정한다.
- 이미지 경로를 `url('')` 에 작성하면 해동 경로의 이미지가 표시된다.
- 요소 박스가 이미지보다 크다면 이미지는 반복되어 표시된다.

```html
<html>
    <head>
        <style>
            div {
                height: 300px;
                border: 5px solid gray;

                background-image: url('mountain.jpg');
            }
        </style>
    </head>
    <body>
        <div>
            <h1>background-image</h1>    
        </div>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/css/bgimage.PNG" >
<br>

## background-repeat
---
`background-repeat` 속성은 이미지의 반복 여부를 지정한다.

|속성|설명|
|:---:|:---:|
|repeat|기본값, 수직/수평 모두 반복|
|repeat-x|수평(좌우)으로 반복|
|repeat-y|수직(상하)으로 반복|
|no-repeat|반복하지 않고 한 번만 표시|

```html
<html>
    <head>
        <style>
            div {
                margin-bottom: 5px;
                height: 155px;
                border: 5px solid gray;
                
                background-image: url('mountain.jpg');
            }
            .repeat {
                background-repeat: repeat;
            }
            .repeatx {
                background-repeat: repeat-x;
            }
            .repeaty {
                background-repeat: repeat-y;
            }
            .no {
                background-repeat: no-repeat;
            }
        </style>
    </head>
    <body>
        <div class="repeat">
            <h1>background-repeat</h1>    
        </div>
        <div class="repeatx">
            <h1>background-repeat repeat-x</h1>
        </div>
        <div class="repeaty">
            <h1>background-repeat repeat-y</h1>
        </div>
        <div class="no">
            <h1>background-repeat no-repeat</h1>
        </div>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/css/bgrepeat.PNG" >
<br>

## background-position
---
`background-position` 속성은 이미지의 위치를 지정한다.  
기본값은 좌측 상단(0% 0% / 0 0)이며 `x, y좌표` 를 지정하여 사용할 수 있다.(좌표 값으로 px, %, 기준좌표를 혼용해서 사용 가능)

- x, y 좌표 : 요소 안쪽은 +, 요소 바깥쪽은 -
- 기준 좌표 : left, right, center, top, bottom

```html
<html>
    <head>
        <style>
            div {
                margin-bottom: 5px;
                height: 130px;
                border: 5px solid gray;
                
                background-image: url('mountain.jpg');
                background-repeat: no-repeat;
            }
            .ex1 {
                background-position: 20px 30px;
            }
            .ex2 {
                background-position: -30px 10%;
            }
            .ex3 {
                background-position: 20px center;
            }
            .ex4 {
                background-position: right;
            }
        </style>
    </head>
    <body>
        <div class="ex1">
            <h1>background-position</h1>    
        </div>
        <div class="ex2">
            <h1>background-position</h1>   
        </div>
        <div class="ex3">
            <h1>background-position</h1>   
        </div>
        <div class="ex4">
            <h1>background-position</h1>   
        </div>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/css/bgposition.PNG" >
<br>

## background-attachment
---
`background-attachment` 속성은 페이지 스크롤에 따른 배경이미지의 화면 고정 유무를 지정한다.

|속성|값|
|:---:|:---:|
|scroll|기본값, 배경이미지가 화면에 따라 스크롤 되도록 한다.|
|fixed|화면을 스크롤해도 배경이미지는 스크롤 되지 않고 고정위치에 있다.|

```html
<html>
    <head>
        <style>
            div {
                height: 400px;
                border: 5px solid gray;
                background: tomato url('mountain.jpg');
                background-attachment : fixed;               
            }
        </style>
    </head>
    <body>
        <div>
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Tenetur non debitis quia voluptate delectus ad, eos similique voluptatibus, earum officiis, nesciunt accusantium! Aut quod rerum doloremque cupiditate facere quo nesciunt. Officia ea qui sapiente dignissimos dolorem, molestiae blanditiis consectetur aliquid quidem non voluptate. Officiis consequuntur ea voluptatum omnis quisquam, vitae nostrum odio! Blanditiis nesciunt aliquid dicta quas aliquam asperiores aut debitis doloribus similique saepe quidem et quia aperiam explicabo quaerat doloremque, autem laboriosam libero eius eveniet. Neque voluptatibus porro aliquam nostrum aliquid non ducimus, sed quo voluptatum quam facere sequi labore perspiciatis error dolore blanditiis sint eius reprehenderit dolorum? Commodi culpa, pariatur repudiandae exercitationem quibusdam, tempore eius molestias eligendi, 
        </div>
    </body>
</html>
```

결과는 코드펜

## background-size
---
`background-size` 속성은 배경 이미지의 사이즈를 지정한다.

- 첫 번째 값은 width, 두 번째 값은 height를 의미한다.
- 값은 1개만 지정한 경우, 지정 값은 width를 의미하며 height는 auto로 지정된다.

|속성|설명|
|:---:|:---:|
|auto|기본값으로 배경 이미지 원래의 width, height를 표시한다.|
|px|배경이미지 크기가 지정된 px값 그대로 표시한다.|
|%|부모 요소에 비례한 % 값으로 표시한다.|  
|contain|배경 이미지의 크기 비율을 유지한 상태에서 배경 요소에 배경 이미지 전체가 들어갈 수 있도록 한다.(요소 크기에 의해 이미지가 잘릴 수 있으며 빈공간이 생길 수 있다.)|  
|cover|배경 이미지의 크기 비율을 유지한 상태로 배경 요소를 가득 채운다.(요소 크기에 의해 이미지가 잘릴 수 있다.)|

```html
<html>
    <head>
        <style>
            div {
                margin-bottom: 5px;
                height: 200px;
                border: 5px solid gray;
                background-image: url('mountain.jpg');
                background-repeat: no-repeat;  
            }
            .cover {
                background-size: cover;
            }
            .contain {
                background-size: contain;
            }
        </style>
    </head>
    <body>
        <div class="no">
            <h2>background-size</h2>
        </div>
        <div class="cover">
            <h2>background-size cover</h2>
        </div>
        <div class="contain">
            <h2>background-size contain</h2>
        </div>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/css/bgsize.PNG" >
<br>

## background
---
`background` 속성은 배경 속성들을 한 번에 정의하기 위한 축약 속성이다.

```
background: background-color background-image background-repeat background-attachment background-position
```
```css
div {
    background: red url('mountain.jpg') no-repeat fixed center;
}