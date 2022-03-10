---
layout: post
title: "[HTML] from, input 태그"
category: [HTML]

---
<br>

`<form>, <input>` 태그에 대해 알아보자
<!-- more -->

<hr>

# `<form>` 태그
---
`form` 태그는 웹사이트에서 다른 페이지로 정보를 보낼 때 사용한다.

|속성|의미|값|기본값|
|---|---|---|---|
|action|전송한 정보를 처리할 웹페이지의 URL|URL| |
|autocomplete|사용자가 이전에 입력한 값으로 자동 완성 기능을 사용할 것인지 여부|`on`, `off`|`on`|
|method|서버로 전송할 HTTP 방식|`GET`, `POST`|`GET`|
|name|고유한 양식의 이름| |
|target|서버로 전송 후 응답받을 방식|`_self`, `_blank`|`_self`|

## method 속성(GET/POST)
---

GET 방식
- URL의 끝에 데이터를 첨부해서 전송한다. 
- 키=값&키=값
- 데이터가 URL에 항상 노출이 되며 전송할 수 있는 정보의 길이가 256자로 제한된다.
  
POST 방식
- URL 상에 정보가 노출되지 않는다.
- 정보가 header의 body에 담겨져 전송된다.
- 전송할 수 있는 정보의 길이 제한이 없다.


```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>form 태그</title>
    </head>
    <body>
        <form action="http:localhost/login.html" method="GET"">
            <p>아이디 : <input type="text" name="id" autofocus></p>
            <p>비밀번호 : <input type="password" name="pwd" placeholder="비밀번호를 입력하세요"></p>
            <p>취미
            개발 : <input type="checkbox" name="hobby"" value="개발">
            잠자기 : <input type="checkbox" name="hobby" value="잠자기" checked>
            독서 : <input type="checkbox" name="hobby" value="독서"></p>
            <input type="submit" value="전송">
            <input type="reset" value="초기화">
            <input type="hidden" name="hidden" value="hidden">
        </form> 
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/html/form1.PNG" >

초기화 버튼 클릭 시 입력 내용이 초기화된다.
<img src="https://sanggil1107.github.io//public/img/html/form3.PNG" >

`method=GET` 일 경우 아래와 같이 URL에 키=값 형식으로 데이터를 확인할 수 있다.
<img src="https://sanggil1107.github.io//public/img/html/form2.PNG" >
<br>

# `<input>` 태그
---
`<input>` 태그는 사용자 입력을 받기 위해 사용한다.

|속성|의미|값|특징|
|:---:|:---:|:---:|:---:|
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
|:---:|:---:|:---:|
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

