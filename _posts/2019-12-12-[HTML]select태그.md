---
layout: post
title: "[HTML] select 태그"
category: [HTML]

---
<br>

`<select>, <option>, <optgroup>` 태그에 대해 알아보자
<!-- more -->

<hr>


# `<select>` 태그
---
`<select>` 태그는 옵션을 선택하고자 할 때 사용한다.

|속성|의미|값|기본값|
|:---:|:---:|:---:|:---:|
|disabled|선택 메뉴를 비활성화|boolean| |
|multiple|다중 선택 여부|boolean| |
|name|선택 메뉴의 이름| | |
|size|한 번에 볼 수 있는 행의 개수|숫자|1|

<br>

# `<option>` 태그
---
`<option>` 태그는 `<select>` 태그에서 옵션을 표시할 때 사용한다.

|속성|의미|값|
|:---:|:---:|:---:|
|disabled|선택 메뉴를 비활성화|boolean|
|selected|옵션이 선택되었음을 표시|boolean|
|value|양식으로 제출될 값| |

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>select 태그</title>
    </head>
    <body>
        <p>색상</p>
        <select name="color1">
            <option value="red">붉은색</option>
            <option value="black">검은색</option>
            <option value="green" selected>초록색</option>
        </select>
        <p>색상 다중선택</p>
        <select name="color2" multiple>
            <option value="red">붉은색</option>
            <option value="black" selected>검은색</option>
            <option value="green">초록색</option>
        </select>
        <p>색상 행 개수</p>
        <select name="color3" size="2">
            <option value="red">붉은색</option>
            <option value="black">검은색</option>
            <option value="green">초록색</option>
        </select>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/html/select.PNG" >

<br>

# `<optgroup>` 태그
---
`<optgroup>` 태그는 `<option>` 태그를 그룹화할 때 사용한다.

|속성|의미|값|
|:---:|:---:|:---:|
|label|옵션 그룹의 이름(필수)| |
|disabled|옵션 그룹을 비활성화|boolean|

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>optgroup 태그</title>
    </head>
    <body>
        <p>신발 사이즈</p>
        <select name="size">
            <optgroup label="남자">
                <option value="260">260mm</option>
                <option value="270">270mm</option>
                <option value="280">280mm</option>
            </optgroup>
            <optgroup label="여자">
                <option value="220">220mm</option>
                <option value="230">230mm</option>
                <option value="240">240mm</option>
            </optgroup>
        </select>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/html/optgroup.png" >
