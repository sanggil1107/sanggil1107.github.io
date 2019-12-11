---
layout: post
title: "[HTML] table 태그"
category: [HTML]

---
<br>

`<table>` 태그에 대해 알아보자
<!-- more -->

<hr>

# `<table>` 태그
---
`<table>` 태그는 표를 만들 때 사용한다.
- `<tr>` 태그는 표의 열을 나타낸다.
- `<td>` 태그는 표의 행을 나타내며, `<tr>` 태그 하위에 위치한다.
- `<th>` 태그는 머리글 행을 나타내며, `<tr>` 태그 하위에 위치한다.
 
```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>table 태그</title>
    </head>
    <body>
        <table>
            <tr>
                <th>이름</th><th>성별</th><th>주소</th><th>회비</th>
            </tr>
            <tr>
                <td>양상길</td><td>남</td><td>서울</td><td>1000</td>
            </tr>
            <tr>
                <td>김철수</td><td>남</td><td>서울</td><td>500</td>
            </tr>
            </table>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/html/table1.PNG" >

일반적인 표는 제목 줄을 가지고 있는 경우가 많으며 다음 태그를 사용하여 구현한다.
`<thead>` 태그는 표의 제목 영역을 나타낸다.(머리글)
`<tbody>` 태그는 표의 본문 영역을 나타낸다.(본문)
`<tfoot>` 태그는 표의 바닥 영역을 나타낸다.(바닥글)

아래 결과와 같이 테이블의 레이아웃에 영향을 주지 않는다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>table 태그</title>
    </head>
    <body>
        <table>
            <thead>
                <tr>
                    <th>이름</th><th>성별</th><th>주소</th><th>회비</th>
                </tr>
            </thead>
            <tbody>      
                <tr>
                    <td>양상길</td><td>남</td><td>서울</td><td>1000</td>
                </tr>
                <tr>
                    <td>김철수</td><td>남</td><td>서울</td><td>500</td>
                </tr>
            </tbody>
            <tfoot>
                <tr>
                    <td>합계</td><td></td><td></td><td>1500</td>
                </tr>
            </tfoot>
            </table>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/html/table_theadbodyfoot.PNG" >

<br>

## 속성
---

### `<table>` 속성
---
|속성|의미|값|
|---|---|---|
|border|테이블 테두리 두께|두께|
|bordercolor|테이블 테두리 색상|색값|
|bgcolor|배경 색상|색값|
|cellspacing|셀과 셀과의 간격|간격
|cellpadding|셀 안의 내용과의 여백|여백
|width|테두리 가로 너비|크기, 비율|
|height|테두리 세로 너비|크기, 비율|

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>table 태그</title>
    </head>
    <body>
        <table border="2" bordercolor="skyblue" bgcolor="pink" width="300" height="200" cellspacing="10" cellpadding="10">
            <tr>
                <th>이름</th><th>성별</th><th>주소</th><th>회비</th>
            </tr>
            <tr>
                <td>양상길</td><td>남</td><td>서울</td><td>1000</td>
            </tr>
            <tr>
                <td>김철수</td><td>남</td><td>서울</td><td>500</td>
            </tr>
        </table>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/html/table2.PNG" >
<br>

### `<tr> <td> <th>` 속성
---
|속성|의미|값|
|---|---|---|
|bgcolor|배경 색상|색값|
|align|정렬|`left`, `right`, `center`|
|colspan|확장하려는(병합) 열의 수|열의 수|
|rowspan|확장하려는(병합) 행의 수|행의 수|

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>table 태그</title>
    </head>
    <body>
        <table border="2">
            <tr bgcolor="red">
                <th>이름</th><th>성별</th><th>주소</th><th>회비</th>
            </tr>
            <tr>
                <td>양상길</td><td>남</td><td rowspan="2">서울</td><td>1000</td>
            </tr>
            <tr>
                <td>김철수</td><td>남</td><td>500</td>
            </tr>
            <tr>
                <td align="center" bgcolor="green" colspan="3">합계</td><td>1500</td>
            </tr>
        </table>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/html/table3.PNG" >
<br>

# `<caption>` 태그
---
`<caption>` 태그는 표의 제목을 설정한다.  
table 당 하나의 `<caption>`만 사용 가능하다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>table 태그</title>
    </head>
    <body>
        <table border="2">
            <caption>html caption 태그</caption>
            <thead>
                <tr bgcolor="red">
                    <th>이름</th><th>성별</th><th>주소</th><th>회비</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>양상길</td><td>남</td><td rowspan="2">서울</td><td>1000</td>
                </tr>
                <tr>
                    <td>김철수</td><td>남</td><td>500</td>
                </tr>
            </tbody>
            <tfoot>
                <tr>
                    <td align="center" bgcolor="green" colspan="3">합계</td><td>1500</td>
                </tr>
            </tfoot>
        </table>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/html/caption.PNG" >