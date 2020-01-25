---
layout: post
title: "[CSS] Flexbox"
category: [CSS]

---
<br>

`Flexbox` 속성에 대해 알아보자
<!-- more -->

<hr>

# flexbox
---
`flexbox` 속성은 flexible의 줄임말로 세련된 레이아웃을 위한 속성이다. 이를 활용하면 기존에 레이아웃을 만들기 위해서 사용하던 table 태그나 float 속성의 복잡함 대신 손쉽게 구현할 수 있다. 또한, 요소의 사이즈가 불명확하거나 동적일 때에도 쉽게 구현할 수 있다.

flexbox 레이아웃은 flex item이라는 자식 요소와 flex container라는 부모 요소로 구성된다.


## flex container
---
flex 레이아웃 중 부모 요소에 해당하며 flex item이라는 복수의 자식 요소들을 포함하고 있다.

|속성|설명|
|:---:|:---:|
|display|Flex Container를 정의|
|flex-direction|item의 주 축(수평, 수직)을 설정|
|flex-wrap|item의 여러 줄 묶음(줄바꿈) 설정|
|flex-flow|`flex-direction` 과 `flex-wrap` 의 축약|
|justify-content|수평 방향의 정렬 방법|
|align-content|수직 방향의 정렬 방법(2줄 이상)|
|align-items|수직 방향에서의 item 정렬 방법(1줄)|

### display
---
`display` 속성은 flex 레이아웃을 설정하기 위해 필요한 속성이다. 주의할 점으로 이 속성은 직계 자손에게만 적용된다.

|값|의미|
|:---:|:---:|
|flex|Block 특성의 Container 정의|
|inline-flex|Inline 특성의 Container 정의|

`flex` 로 지정된 Container는 Block 요소와 같은 성향을 가지며 `inline-flex` 로 지정된 Container는 Inline 요소와 같은 성향을 가진다.

```html
<html>
    <head>
        <style>
            .container {
                background-color: skyblue;
                display: flex;
            }
            div {
                background-color: springgreen;
                border: 1px solid black;       
            }
        </style>
    </head>
    <body>
        <h1>flex</h1>
        <div class="container">
            <div class="item1">item1</div>
            <div class="item2">itme2</div>
            <div class="item2">itme3</div>
            <div class="item2">itme4</div>
            <div class="item2">itme5</div>
        </div>
    </body>
</html>
```
<img src="https://sanggil1107.github.io//public/img/css/flexdisplay.PNG" >
<br>

### flex-direction
---
`flex-direction` 속성은 container 안의 item 들의 정렬과 배치 방향을 설정한다.

|값|의미|기본값|
|:---:|:---:|:---:|
|row|item을 왼쪽에서 오른쪽으로 표시|`row`|
|row-reverse|item을 오른쪽에서 왼쪽으로 표시| |
|column|item을 위에서 아래로 표시| |
|column-reverse|item을 아래에서 위로 표시| |

- row  
: 왼쪽에서 오른쪽으로 수평 배치된다.(기본값)

```css
.container {
    display: flex;
    flex-direction: row;
}
```
<img src="https://sanggil1107.github.io//public/img/css/flexdirectionrow.PNG" >
<br>

- row-reverse  
: 오른쪽에서 왼쪽으로 수평 배치된다.

```css
.container {
    display: flex;
    flex-direction: row-reverse;
}
```
<img src="https://sanggil1107.github.io//public/img/css/flexdirectionrowreverse.PNG" >
<br>

- column  
: 위에서 아래로 수직 배치된다.

```css
.container {
    display: flex;
    flex-direction: column;
}
```
<img src="https://sanggil1107.github.io//public/img/css/flexdirectioncolumn.PNG" >
<br>

- column-reverse  
: 아래에서 위로 수직 배치된다.

```css
.container {
    display: flex;
    flex-direction: column-reverse;
}
```
<img src="https://sanggil1107.github.io//public/img/css/flexdirectioncolumnreverse.PNG" >
<br>

### flex-wrap
---
`flex-wrap` 속성은 item들의 너비의 합이 container의 너비를 초과할 때 어떻게 처리할지(한 줄 or 여러 줄) 설정한다.

|값|의미|기본값|
|:---:|:---:|:---:|
|nowrap|모든 item을 한 줄에 표시|`nowrap`|
|wrap|item을 여러 줄로 표시(줄바꿈)| |
|wrap-reverse|item을 `wrap` 의 역방향으로 표시| |

- nowrap  
: item을 개행하지 않고 한 줄로 표현(기본값), item 너비는 최소 크기로 축소된다.

```css
.container {
    display: flex;
    flex-wrap: nowrap;
}
```
<img src="https://sanggil1107.github.io//public/img/css/flexwrapnowrap.PNG" >
<br>

- wrap  
: item들의 너비가 container의 너비보다 큰 경우 개행하여 배치한다.(좌에서 우로, 위에서 아래로)

```css
.container {
    display: flex;
    flex-wrap: wrap;
}
```
<img src="https://sanggil1107.github.io//public/img/css/flexwrapwrap.PNG" >
<br>

- wrap-reverse  
: `wrap` 과 동일하나 아래에서 위로 배치한다.

```css
.container {
    display: flex;
    flex-wrap: wrap-reverse;
}
```
<img src="https://sanggil1107.github.io//public/img/css/flexwrapwrapreverse.PNG" >
<br>

### flex-flow
---
`flex-flow` 속성은 `flex-direction`과 `flex-wrap`을 설정하기 위한 축약 속성이다.

|값|의미|기본값|
|:---:|:---:|:---:|
|flex-direction|item의 주 축(수평, 수직)을 설정|`row`|
|flex-wrap|item의 여러 줄 묶음(줄바꿈) 설정|`nowrap`|

```css
.container {
    display: flex;
    flex-flow: flex-direction || flex-wrap;
}
```
<img src="https://sanggil1107.github.io//public/img/css/flexflow.PNG" >
<br>

### justify-content
---
`justify-content` 속성은 container의 수평방향으로 item들 사이의 여백과 item과 conainer 사이의 여백을 설정한다.

|값|의미|기본값|
|:---:|:---:|:---:|
|flex-start|item을 시작점으로 정렬|`flex-start`|
|flex-end|item을 끝점으로 정렬| |
|center|item을 가운데 정렬| |
|space-between|첫 번째 item은 시작점, 마지막 item은 끝점에 정렬된고 나머지는 고르게 정렬| |
|space-around|item들을 균등한 여백을 포함하여 정렬| |

- flex-start  
: 시작점을 기준으로 정렬한다.

```css
.container {
    display: flex;
    justify-content: flex-start;
}
```
<img src="https://sanggil1107.github.io//public/img/css/justifyflexstart.PNG" >
<br>

- flex-end  
: 끝점을 기준으로 정렬한다.

```css
.container {
    display: flex;
    justify-content: flex-end;
}
```
<img src="https://sanggil1107.github.io//public/img/css/justifyflexend.PNG" >
<br>

- center  
: 수평 방향 기준으로 container 중앙에 정렬한다.

```css
.container {
    display: flex;
    justify-content: center;
}
```
<img src="https://sanggil1107.github.io//public/img/css/justifycenter.PNG" >
<br>

- space-between  
: 첫 번째와 마지막 item은 좌우 측면에 정렬하고 나머지와 균등한 간격으로 정렬한다.

```css
.container {
    display: flex;
    justify-content: space-between;
}
```
<img src="https://sanggil1107.github.io//public/img/css/justifyspacebetween.PNG" >
<br>

- space-around  
: 모든 item을 균등한 간격으로 정렬한다.

```css
.container {
    display: flex;
    justify-content: space-around;
}
```
<img src="https://sanggil1107.github.io//public/img/css/justifyspacearound.PNG" >
<br>

### align-items
---
`align-items` 속성은 container의 수직방향으로 item과 conainer 사이의 여백을 설정한다.  
item이 한 줄로 되어 있을 경우 많이 사용하며 item이 `flex-wrap: wrap;` 을 통해 여러 줄일 경우에는 `align-content` 속성이 우선된다. 따라서 이 속성을 사용하기 위해서는 `align-content` 속성은 기본값(stretch)으로 설정해야 한다.

|값|의미|기본값|
|:---:|:---:|:---:|
|flex-start|item을 시작점으로 정렬| |
|flex-end|item을 끝점으로 정렬| |
|center|item을 가운데 정렬| |
|stretch|Container의 수직방향 축(높이)을 채우기 위해 item을 늘림|`stretch`|
|baseline|item을 문자 기준선에 정렬| |

- flex-start
: 시작점을 기준으로 정렬한다.

```css
.container {
    display: flex;
    align-items: flex-start;
}
```
<img src="https://sanggil1107.github.io//public/img/css/aligntimesflexstart.PNG" >
<br>

- flex-end
: 끝점을 기준으로 정렬한다.

```css
.container {
    display: flex;
    align-items: flex-end;
}
```
<img src="https://sanggil1107.github.io//public/img/css/aligntimesflexend.PNG" >
<br>

- center
: 수직 방향 기준으로 container 중앙에 정렬한다.

```css
.container {
    display: flex;
    align-items: center;
}
```
<img src="https://sanggil1107.github.io//public/img/css/aligntimecenterPNG.PNG" >
<br>

- stretch
: 수직 뱡향으로 container 높이에 꽉찬 높이를 갖는다.(기본값)

```css
.container {
    display: flex;
    align-items: stretch;
}
```
<img src="https://sanggil1107.github.io//public/img/css/aligntimestretch.PNG" >
<br>

- baseline
: container의 문자 기준선을 기준으로 정렬한다.

```css
.container {
    display: flex;
    align-items: baseline;
}
```
<img src="https://sanggil1107.github.io//public/img/css/aligntimesbaseline.PNG" >
<br>

### align-content
---
`align-content` 속성은 container의 수직방향으로 item 들 사이의 여백과 item과 conainer 사이의 여백을 설정한다.  
이 속성은 `flex-wrap: wrap;` 속성이 설정되어 있어야 정상 동작한다.

|값|의미|기본값|
|:---:|:---:|:---:|
|flex-start|item을 시작점으로 정렬| |
|flex-end|item을 끝점으로 정렬| |
|center|item을 가운데 정렬| |
|stretch|container의 수직방향 축(높이)을 채우기 위해 item을 늘림|`stretch`|
|space-between|첫 번째 item은 시작점, 마지막 item은 끝점에 정렬된고 나머지는 고르게 정렬| |
|space-around|item들을 균등한 여백을 포함하여 정렬| |

- flex-start  
: 시작점을 기준으로 정렬한다.

```css
.container {
    display: flex;
    flex-wrap: wrap;
    align-content: flex-start;
}
```
<img src="https://sanggil1107.github.io//public/img/css/aligncontentstart.PNG" >
<br>

- flex-end  
: 끝점을 기준으로 정렬한다.

```css
.container {
    display: flex;
    flex-wrap: wrap;
    align-content: flex-end;
}
```
<img src="https://sanggil1107.github.io//public/img/css/aligncontentend.PNG" >
<br>

- center
: 수직 방향 기준으로 container 중앙에 정렬한다.

```css
.container {
    display: flex;
    flex-wrap: wrap;
    align-content: center;
}
```
<img src="https://sanggil1107.github.io//public/img/css/aligncontentcenter.PNG" >
<br>

- space-between
: 첫 번째와 마지막 item은 좌우 측면에 정렬하고 나머지와 균등한 간격으로 정렬한다.

```css
.container {
    display: flex;
    flex-wrap: wrap;
    align-content: space-between;
}
```
<img src="https://sanggil1107.github.io//public/img/css/aligncontentspacebetween.PNG" >
<br>

- space-around
: 모든 item을 균등한 간격으로 정렬한다.

```css
.container {
    display: flex;
    flex-wrap: wrap;
    align-content: space-around;
}
```
<img src="https://sanggil1107.github.io//public/img/css/aligncontentspacearound.PNG" >
<br>

- stretch
: container 높이를 균등하게 분배한 공간(item 행 만큼)에 모든 item을 정렬하여 배치한다.(기본값)

```css
.container {
    display: flex;
    flex-wrap: wrap;
    align-content: stretch;
}
```
<img src="https://sanggil1107.github.io//public/img/css/aligncontentstretch.PNG" >
<br>


## flex item
---
flex 레이아웃 중 자식 요소에 해당한다.

|속성|설명|
|:---:|:---:|
|order|Flex item 순서 설정|
|flex-grow|item의 증가 너비 비율 설정|
|flex-shrink|item의 감소 너비 비율 설정|
|flex-basis|item의 기본 너비 설정|
|flex|`flex-grow`, `flex-shrink`, `flex-basis` 의 축약|
|align-self|수직 방향에서의 item 정렬 방법|

### order
---
`order` 속성은 item의 배치 순서를 지정하며 값이 작을수록 먼저 배치된다.

|값|의미|기본값|
|:---:|:---:|:---:|
|숫자|item의 순서를 설정|`0`|

```css
.item1 {
    order: 1;
}
.item2 {
    order: -1
}
.item3 {
    order: 5;
}
```
<img src="https://sanggil1107.github.io//public/img/css/flexorder.PNG" >
<br>

### flex-grow
---
`flex-grow` 속성은 item의 너비 비율을 지정한다. 숫자가 클수록 더 큰 너비를 차지하게 되며 브라우저를 늘리면 설정된 비율만큼 증가된다.

|값|의미|기본값|
|:---:|:---:|:---:|
|숫자|item의 증가 너비 비율 설정|`0`|

```css
.item {
    flex-grow: 1;
}
```
모든 item이 동일한 값을 가지면 동일한 너비를 가지게 된다.(총 너비를 5등분하여 차례대로 1/5, 1/5, 1/5, 1/5, 1/5 만큼 차지한다.)
브라우저를 늘리거나 줄이면 동일한 비율로 늘어나거나 줄어든다.

<img src="https://sanggil1107.github.io//public/img/css/flexgrow.PNG" >
<br>
<img src="https://sanggil1107.github.io//public/img/css/flexgrow6.PNG" >
<br>

```css
.item1 {
    flex-grow: 1;
}
```
1 개의 item에만 1의 속성값을 주었을 경우 4개의 item은 최소 너비를 가지게 된다.  
브라우저를 늘리거나 줄이면 flex-grow 속성이 있는 item만 늘어나거나 줄어든다.

<img src="https://sanggil1107.github.io//public/img/css/flexgrow1.PNG" >
<br>
<img src="https://sanggil1107.github.io//public/img/css/flexgrow5.PNG" >
<br>

```css
.item1 { flex-grow: 1; }
.item2 { flex-grow: 2; }
.item3 { flex-grow: 3; }
.item4 { flex-grow: 1; }
.item5 { flex-grow: 1; }
```
모든 item이 설정된 비율의 너비를 가지게 된다.(총 너비를 8등분하여 차례대로 1/8, 2/8, 3/8, 1/8, 1/8 만큼 차지한다.)  
브라우저를 늘리거나 줄이면 설정된 비율로 늘어나거나 줄어든다.

<img src="https://sanggil1107.github.io//public/img/css/flexgrow2.PNG" >
<br>
<img src="https://sanggil1107.github.io//public/img/css/flexgrow4.PNG" >
<br>

### flex-shrink
---
`flex-shrink` 속성은 item의 감소하는 너비 비율을 지정하며 숫자가 클수록 더 많이 감소하게 된다.  
`width`, `flex-basis` 등 요소의 너비에 영향을 받는다.  
요소의 너비가 설정되어 있다면 이를 기준으로 item의 너비가 기준보다 커지면 `flex-grow` 가 동작하고 item의 너비가 기준보다 작아지면 `flex-shrink` 가 동작한다.

|값|의미|기본값|
|:---:|:---:|:---:|
|숫자|item의 감소 너비 비율 설정|`1`|

```css
.item1 { flex-basis: 200px; flex-shrink: 2; }
.item2 { flex-basis: 200px; flex-shrink: 0; }
.item3 { flex-basis: 200px; flex-shrink: 3; }
.item4 { flex-basis: 200px; }
.item5 { flex-basis: 200px; }
```
item들의 너비가 200px인 상황에서 브라우저를 늘려도 item 너비가 늘어나지 않는다.(flex-grow 미지정)  
브라우저를 줄여서 item의 너비인 200px 보다 작아질 때 `flex-shrink` 값의 비율만큼 줄어들게 된다.(모든 item 너비가 동일하므로 감소 비율은 2:0:3:1:1 이며 차례대로 2/7, 0, 3/7, 1/7, 1/7 만큼 감소한다.)  
`flex-shrink` 값이 0인 경우 너비가 줄어들지 않는다.

<img src="https://sanggil1107.github.io//public/img/css/flexshrink.PNG" >
<br>
<img src="https://sanggil1107.github.io//public/img/css/flexshrink1.PNG" >
<br>
<img src="https://sanggil1107.github.io//public/img/css/flexshrink2.PNG" >
<br>

### flex-basis
---
`flex-basis` 속성은 item의 기본 너비(공간 배분 전)를 설정한다.

|값|의미|기본값|
|:---:|:---:|:---:|
|auto|가변 item과 같은 너비|`auto`|
|숫자|item의 증가 너비 비율 설정| |

```css
.item1 { flex-basis: 200px; }
.item2 { flex-basis: 100px; }
.item3 { flex-basis: 300px; }
.item4 { }
.item5 { flex-basis: 50px; }
```
이 속성 지정 시 기본으로 `flex-shrink` 속성이 추가되지만(기본값 : 1) `flex-grow` 속성은 추가되지 않는다. 그래서 브라우저를 줄여보면 동일 비율로 item 너비가 감소하지만 브라우저를 늘리면 item 너비는 `flex-basis` 너비 이상으로 늘어나지 않는다.
<img src="https://sanggil1107.github.io//public/img/css/flexbasis.PNG" >
<br>
<img src="https://sanggil1107.github.io//public/img/css/flexbasis1.PNG" >
<br>
<img src="https://sanggil1107.github.io//public/img/css/flexbasis2.PNG" >
<br>


### flex
---
`flex` 속성은 item의 너비(증가, 감소, 기본)를 설정하는 축약 속성이다.

|값|의미|기본값|
|:---:|:---:|:---:|
|flex-grow|item의 증가 너비 비율 설정|`0`|
|flex-shrink|item의 감소 너비 비율 설정|`1`|
|flex-basis|item의 기본 너비 설정|`auto`|

```css
.item {
    flex: flex-grow flex-shrink flex-basis;
}
```

`flex-shrink`, `flex-basis` 속성은 생략 가능하다.  
`flex-basis` 의 기본값은 auto 이지만 `flex` 속성에서 생략할 경우에는 0으로 적용된다.

### align-self
---
`align-self` 속성은 수직 방향으로 개별 item의 정렬 방법을 지정한다.  
이 속성은 `align-items` 보다 우선된다.

|값|의미|기본값|
|:---:|:---:|:---:|
|auto|Container의 `align-items` 속성을 상속받음|`auto`|
|flex-start|item을 시작점으로 정렬| |
|flex-end|item을 끝점으로 정렬| |
|center|item을 가운데 정렬| |
|stretch|Container의 수직방향 축(높이)을 채우기 위해 item을 늘림| |
|baseline|item을 문자 기준선에 정렬| |

<img src="https://sanggil1107.github.io//public/img/css/alignself.PNG" >
<br>