---
layout: post
title: "[HTML] textarea, input 태그"
category: [HTML]

---
<br>

`<textarea>, <input>` 태그에 대해 알아보자
<!-- more -->

<hr>


# `<textarea>` 태그
---
`<textarea>` 태그는 여러 줄의 텍스트 양식을 입력받을 때 사용한다.

|속성|의미|값|
|:---:|---|:---:|
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

# `<input>` 태그
---
`<input>` 태그는 사용자 입력을 받기 위해 사용한다.

|속성|의미|값|특징|
|:---:|---|:---:|:---:|
|autocomplete|사용자가 이전에 입력한 값으로 자동 완성 기능을 사용할 것인지 여부|`on`, `off`| |
|autofocus|페이지가 로드될 떄 자동으로 포커스|boolean| |
|checked|양식이 선택되었음을 표시|boolean|`type` 속성이 `radio`. `checkbox`일 때|
|disabled|양식을 비활성화|boolean| |
|max|지정 가능한 최대 값|숫자| |
|min|지정 가능한 최소 값|숫자| |
|maxlength|입력 가능한 최대 문자 수|숫자|`type` 속성이 `text`. `email`, `password`, `tel`. `url`일 때|
|name|양식의 이름| | |
|placeholder|사용자가 입력할 값의 힌트| | |
|readonly|수정 불가한 읽기 전용| | |
|type|입력 받을 데이터의 종류|별도 정리| |
|value|양식의 초기 값| | |
|required|필수 값| | |
|list|참조할 `<datalist>`의 id 속성 값| | |


## type 속성
---

|속성|의미|특징|
|:---:|---|:---:|
|text|일반 텍스트| |
|password|비밀번호|가려짐|
|button|일반 버튼| |
|submit|제출 버튼|`form` 태그 내에서 사용|
|reset|초기화|`form` 태그 내에서 사용|
|email|이메일| |
|search|검색| |
|tel|전화번호| |
|number|숫자| |
|url|절대 URL| |
|file|파일| |
|hidden|보이지 않지만 전송할 양식|`value` 속성으로 값을 지정|
|range|범위 컨트롤|`min`,`max`,`step`,`value` 속성 사용|
|radio|라디오 버튼|같은 `name` 속성 그룹 내 하나만 선택 가능|
|checkbox|체크박스| |

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>input 태그</title>
    </head>
    <body>
        <p>text : <input type="text" name="textvalue" autofocus></p>
        <p>password : <input type="password" name="passwordvalue" placeholder="비밀번호를 입력하세요"></p>
        <p>button : <input type="button" name="buttonvalue" value="버튼"></p>
        <p>submit : <input type="submit" name="submitvalue" value="전송"></p>
        <p>reset : <input type="reset" name="resetvalue" value="초기화"></p>
        <p>email : <input type="email" name="emailvalue" disabled></p>
        <p>serach : <input type="search" name="searchvalue" value="search" readonly></p>
        <p>tel : <input type="tel" name="telvalue"></p>
        <p>number : <input type="number" name="numbervalue"></p>
        <p>url : <input type="url" name="urlvalue"></p>
        <p>file : <input type="file" name="filevalue"></p>
        <p>hidden : <input type="hidden" name="hidden" value="hidden"></p>
        <p>range : <input type="range" name="rangevalue" min="0" max="10" ></p>
        <p>
            radio(단일선택)<br>
            붉은색 : <input type="radio" name="color" value="red">
            검은색 : <input type="radio" name="color" value="black" checked>
            초록색 : <input type="radio" name="color" value="green">
        </p>
        <p>
            checkbox(다중선택)<br>
            95 : <input type="checkbox" name="size" value="95" checked>
            100 : <input type="checkbox" name="size" value="100" checked>
            105 : <input type="checkbox" name="size" value="105">
        </p>   
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/html/input.PNG" >

- text : 자동으로 포커싱(`autofocus`)
- password : 필수값(`required`), 기본 안내글(`placeholder`)
- email : 비활성화(`disabled`)
- search : 수정불가능(`readonly`)
- tel : 최대 4자리(`maxlength`)
- range : 범위 0 ~ 10(`min`, `max`)
- radio, checkbox : 자동 체크(`checked`)

