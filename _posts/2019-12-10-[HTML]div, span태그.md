---
layout: post
title: "[HTML] div, span 태그"
category: [HTML]

---
<br>

`<div>, <span>` 태그에 대해 알아보자
<!-- more -->

<hr>


# `<div>` 태그
---
`<div>` 태그는 Division의 약자로, 레이아웃을 나누기 위해 사용한다.  
다른 태그와 달리 특별한 기능은 없고 가상의 레이아웃을 설계하는데 사용한다.  
`display` 속성이 `block`이다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>div 태그</title>
    </head>
    <body>
        <div style="background-color: coral;">div1</div>
        <div style="background-color: cyan">div2</div>
    </body>
</div>
```
<img src="https://sanggil1107.github.io//public/img/html/div.PNG" >

# `<span>` 태그
---
`<span>` 태그는 콘텐츠 영역을 설정할 때 사용한다.  
`<div>` 태그와 마찬가지로 특별한 기능을 가지고 있지 않다.  
`display` 속성이 `inline`이다.  

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>span 태그</title>
    </head>
    <body>
        <span style="background-color: purple;">span1</span>
        <span style="background-color: red;">span2</span>
    </body>
</div>
```
<img src="https://sanggil1107.github.io//public/img/html/span.PNG" >

# `<div>` 와 `<span>`의 차이
---
`<div>` 와 `<span>`의 차이를 알아보기 전에 display의 `block`과 `inline` 그리고 `inline-block`에 대해 먼저 확인해보자.  

## `inline, block, inline-block` 속성
---

### `dispaly:inline`
---
context/text 크기만큼만 공간을 점유하고 줄바꿈을 하지 않는다.  
대표적인 태그로 `<span>` 태그가 있다.  
- width/height 적용 불가  
- margin/padding, top/bottom 적용불가  
  
### `dispaly:block`
---
무조건 한 줄을 점유하며 다음 태그는 무조건 줄바꿈이 적용된다.  
대표적인 태그로 `<div>` 태그가 있다.  

### `dispaly:inline-block`
---
`inline` 과 `block` 속성의 특징을 모두 가지고 있다. 기본적인 특징은 `inline` 속성(줄바꿈을 하지 않고 동일 라인에 작성가능)과 비슷하며 추가적으로 width/height 및 margin/padding, top/bottom 적용이 가능하다.

## `<span>, <div>` 
---
`<span>` 태그와 `<html>` 태그는 둘 다 특별한 기능이 없다는 점에서 비슷하지만 `<span>` 태그는 context/text 크기만큼만 공간을 점유하고 줄바꿈 하지 않으며(`inline`), `<div>` 태그는 무조건 한 줄을 점유하며 줄 바꿈이 적용(`block`)된다는 차이점이 있다.  

예를 통해 확인해보자.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>span/div 태그</title>
    </head>
    <body>
        <div style="background-color: sandybrown;" >
            Koreans are in general pessimistic about the socio-economic
            circumstances surrounding them, a survey shows.
            Among different age groups, college students and job
            seekers were most pessimistic, because of the tough
            job market
        </div>
        <span style="background-color: red;">            
            Koreans are in general pessimistic about the socio-economic
            circumstances surrounding them, a survey shows.
            Among different age groups, college students and job
            seekers were most pessimistic, because of the tough
            job market                   
        </span>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/html/divspan.PNG" >

`<div>` 사용 시 색상이 모든 줄에 적용되어 있으나, `<span>` 사용 시 색상이 text 크기만큼에만 적용되어 있다.  
<br>

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>span/div 태그</title>
    </head>
    <body>
        <div style="background-color: skyblue;">div box1</div>
        <div style="background-color: violet;" >div box2</div>
        <div style="background-color: tomato;" >div box3</div>
        <span style="background-color: skyblue;">span box1</span>
        <span style="background-color: violet;">span box2</span>
        <span style="background-color: tomato;">span box3</span>
    </body>
</div>
```
<img src="https://sanggil1107.github.io//public/img/html/divspan2.PNG" >

`<html>` 태그를 사용한 div box 들은 한 줄씩 되어 줄바꿈이 있는 반면, `<span>` 태그를 사용한 span box는 줄바꿈 없이 한 줄에 모두 표현된다.