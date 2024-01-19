---
layout: post
title: "[HTML] ol, ul, li 태그"
category: [HTML]

---
<br>

`<ol>, <ul>, <li>` 태그에 대해 알아보자
<!-- more -->
<hr>

# `<li>` 태그
---
`<li>` 태그는 list의 약자로 목록을 만들 때 사용한다.  
단독으로 쓰이지 않으면 `<ul>` 혹은 `<ol>` 태그 내부에서 사용한다.

<br>

# `<ul>` 태그
---
`<ul>` 태그는 unordered list의 약자로 순서가 없는 리스트를 작성할 때 사용한다.  
순서가 없기 때문에 글머리 기호를 사용해서 나타낸다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ul 태그</title>
    </head>
    <body>
        <ul>
            <li>Menu1</li>
            <li>Menu2</li>
            <li>Menu3</li>
            <li>Menu4</li>
        </ul>      
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/html/ul.PNG" >

## 속성
---

|속성|의미|값|기본값|
|:---:|:---:|:---:|:---:|
|type|항목에 매겨지는 기호|`circle`, `square`, `disc`|`disc`|

또한, `<ul>` 태그안에 `<ul>` 태그를 사용하여 하위 메뉴 형식으로 작성할 수 있다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ul 태그</title>
    </head>
    <body>
        <ul>
            <li>Menu1</li>
            <li>Menu2</li>
        </ul>  
        <ul type="circle">
            <li>Menu3</li>
            <li>Menu4</li>
            <ul>
                <li>subMenu4-1</li>
                <li>subMenu4-2</li>
            </ul>
        </ul>    
        <ul type="square">
            <li>Menu5</li>
            <li>Menu6</li>
        </ul>        
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/html/ul1.PNG" >

<br>

# `<ol>` 태그
---
`<ol>` 태그는 ordered list의 약자로 순서가 있는 리스트를 작성할 때 사용한다.  

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ol 태그</title>
    </head>
    <body>
        <ol>
            <li>Menu1</li>
            <li>Menu2</li>
            <li>Menu3</li>
            <li>Menu4</li>
        </ol>      
    </body>
</html>
```

<img src="https://sanggil1107.github.io//public/img/html/ol1캡처.PNG" >

## 속성
---

|속성|의미|값|기본값|
|:---:|:---:|:---:|:---:|
|type|항목에 매겨지는 번호 유형|`a`, `A`, `i`, `I`, `1`|`1`|

또한, `<ul>` 태그와 마찬가지로 `<ol>` 태그안에 `<ol>` 태그를 사용하여 하위 메뉴 형식으로 작성할 수 있다.
```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ol 태그</title>
    </head>
    <body>
        <ol>
            <li>Menu1</li>
            <li>Menu2</li>
        </ol>  
        <ol type="a">
            <li>Menu3</li>
            <li>Menu4</li>
            <ol type="i">
                <li>subMenu4-1</li>
                <li>subMenu4-2</li>
            </ol>
        </ol>    
        <ol type="I">
            <li>Menu5</li>
            <li>Menu6</li>
        </ol>        
    </body>
</html>
```
    
<img src="https://sanggil1107.github.io//public/img/html/ol.PNG" >