---
layout: post
title: "[HTML] textarea, datalist 태그"
category: [HTML]

---
<br>

`<textarea>, <datalist>` 태그에 대해 알아보자
<!-- more -->

<hr>

# `<textarea>` 태그
---
`<textarea>` 태그는 여러 줄의 텍스트 양식을 입력받을 때 사용한다.

|속성|의미|값|
|:---:|:---:|:---:|
|autocomplete|사용자가 이전에 입력한 값으로 자동 완성 기능을 사용할 것인지 여부|`on`, `off`|
|autofocus|페이지가 로드될 떄 자동으로 포커스|boolean|
|disabled|양식을 비활성화|boolean|
|maxlength|입력 가능한 최대 문자 수|숫자|
|name|양식의 이름| |
|placeholder|사용자가 입력할 값의 힌트| |
|readonly|수정 불가한 읽기 전용| |
|rows|높이(양식의 줄 수)|숫자|
|cols|너비(한 줄의 글자 수)|숫자|

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>textarea 태그</title>
    </head>
    <body>   
        <p>textarea1 : <textarea name="textarea1" placeholder="textarea" disabled></textarea></p>
        <p>textarea2 : <textarea name="textarea2" rows="5" cols="5"></textarea></p>
        <p>textarea3 : <textarea name="textarea3" readonly>readonly</textarea></p>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/html/textarea.PNG" >
<br>


# `<datalist>` 태그
---
`<datalist>` 태그는 `<input>` 태그에 미리 정의된 옵션을 지정하여 자동완성 기능을 제공하는데 사용한다.

|속성|의미|값|
|:---:|:---:|:---:|
|id|list 대상|`<input>` 태그의 `list` 속성|

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>datalist 태그</title>
    </head>
    <body>   
       <input name="datalist" list="browser">
       <datalist id="browser">
           <option value="IE"></option>
           <option value="Chrome"></option>
           <option value="Fire Fox"></option>
           <option value="Safari"></option>
       </datalist>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/html/datalist.png" >
