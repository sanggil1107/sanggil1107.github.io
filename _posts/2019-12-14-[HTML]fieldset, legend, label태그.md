---
layout: post
title: "[HTML] fieldset, legend, label 태그"
category: [HTML]

---
<br>

`<fieldset>, <legend>, <label>` 태그에 대해 알아보자
<!-- more -->

<hr>


# `<fieldset>` 태그
---
`<fieldset>` 태그란 같은 목적의 입력요소를 그룹화할 때 사용한다.

|속성|의미|값|
|:---:|:---:|:---:|
|disabled|그룹 내 모든 양식 요소를 비활성화|boolean|
|name|그룹의 이름| |
<br>

# `<legend>` 태그
---
`<legend>` 태그는 `<fieldset>` 태그의 그룹 제목 작성에 사용한다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>fieldset 태그</title>
    </head>
    <body>   
        <fieldset name="cafe">
            <legend>카페 종류</legend>
            <input type="radio">스타벅스
            <input type="radio">이디야
            <input type="radio">파스쿠치
        </fieldset>
        <fieldset name="coffee">
            <legend>커피 종류</legend>
            <input type="radio">아메리카노
            <input type="radio">카페라떼
        </fieldset>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/html/fieldset.PNG" >
<br>

# `<label>` 태그
---
`<label>` 태그는 라벨 가능한 요소를 설명할 때 사용한다.  
라벨 가능한 요소를 컨테츠로 포함하거나 `for` 속성으로 참조할 수 있다.  
라벨 가능한 요소 : `<button>, <input>, <progress>, <select>, <textarea>`

|속성|의미|
|:---:|:---:|
|for|참조 가능한 요소의 id 값|

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>label 태그</title>
    </head>
    <body>   
        <input type="checkbox" id="agree">
        <label for="agree">동의합니다</label>
        
        <label><input type="checkbox">동의하지 않습니다</label>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/html/label.PNG" >

`label` 태그에 의해 라벨 가능한 요소로 포함되어 있기 때문에 checkbox를 누르지 않고 글씨를 눌러 체크할 수 있다.
