

# 문서 객체 모델(Document Object Model, DOM)
---

getElementById(id)
: id 속성 값으로 요소 노드를 한 개 선택한다. 복수 개인 경우, 첫 번째 요소만 반환한다.
```html
<html>
<head>
</head>
<body>
    <h1>getElementById</h1>
    <p id="getid">getElementById</p>
    <button onclick="changeColor('blue');">blue</button>
    <button onclick="changeColor('red');">red</button>
    <script>
        function changeColor(color) {
            var element = document.getElementById('getid');
            element.style.color = color;
        }
    </script>
</body>
</html>
```

querySelector(selector)
: CSS 선택자를 사용하여 요소 노드를 한 개 선택한다. 복수 개인 경우, 첫 번째 요소만 반환한다.
```html
<html>
<head>
</head>
<body>
    <h1>querySelector</h1>
    <div>querySelector</div>
    <p id="get1">querySelector</p>
    <p class="get2">querySelector</p>
    <script>
        document.querySelector('div').style.color = 'blue';
        document.querySelector('p').style.color = 'red';
        document.querySelector('.get2').style.color = 'green';
    </script>
</body>
</html>
```

querySelectorAll(selector)
: 지정된 CSS 선택자를 이용하여 요소 노드를 모두 선택한다.
```html
<html>
<head>
</head>
<body>
    <h1>querySelectorAll</h1>
    <p class="get">querySelectorAll</p>
    <p class="get">querySelectorAll</p>
    <p class="get">querySelectorAll</p>
    <script>
        var all = document.querySelectorAll('p');
        all[1].style.color = 'red';
    </script>
</body>
</html>
```
```html
<html>
<head>
</head>
<body>
    <h1>querySelectorAll</h1>
    <p class="get">querySelectorAll</p>
    <p class="get">querySelectorAll</p>
    <p class="get">querySelectorAll</p>
    <script>
        var all = document.querySelectorAll('.get');
        for(var i = 0; i < all.length; i++) {
            all[i].style.color = 'blue';
        }
    </script>
</body>
</html>
```
```html
<html>
<head>
</head>
<body>
    <h1>querySelectorAll</h1>
    <p class="get1">querySelectorAll</p>
    <p class="get2">querySelectorAll</p>
    <p class="get3">querySelectorAll</p>
    <script>
        var all = document.querySelectorAll('.get1, .get3');
        for(var i = 0; i < all.length; i++) {
            all[i].style.color = 'orange';
        }
    </script>
</body>
</html>
```

getElementsByTagName
: 지정된 태그를 가진 모든 요소를 선택한다.
```html
<html>
<head>
</head>
<body>
    <h1>getElementsByTagName</h1>
    <ul>
        <li>사과</li>
        <li>딸기</li>
        <li>수박</li>
    </ul>
    <script>
        var tag = document.getElementsByTagName('li');
        document.write("총 " + tag.length + " 개의 li 요수 <br>");

        for(var i = 0; i < tag.length; i++) {
            document.write(tag[i].nodeName + " : " + tag[i].childNodes[0].nodeValue + "<br>");
        }
    </script>
</body>
</html>
```

getElementsByName
: 지정된 name 값에 해당하는 모든 요소를 탐색한다.
```html
<html>
<head>
</head>
<body>
    <h1>getElementsByName</h1>
    <ul>
        <li name="red">빨간색</li>
        <li name="red">빨간색1</li>
        <li name="blue">파란색</li>
    </ul>
    <script>
        var red = document.getElementsByName('red');
        red[0].style.color = "red";
        red[1].style.color = "red";
    </script>
</body>
</html>
```

getElementsByClassName
: 지정된 class 명에 해당하는 모든 요소를 탐색한다.
```html
<html>
<head>
</head>
<body>
    <h1>getElementsByClassName</h1>
    <div class="getclassname">first</div>
    <p class="getclassname">second</p>
    <ul>
        <li class="getclassname">third</li>
        <li>fourth</li>
    </ul>
    <script>
        var classname = document.getElementsByClassName('getclassname');
        for(var i = 0; i < classname.length; i++) {
            classname[i].style.fontWeight = 'bold';
        }
    </script>
</body>
</html>
```

createElement/createTextNode/appendChild
---
createElement(tagName)
: 태그 이름을 인자로 전달하여 요소를 생성한다.

createTextNode(text)
: 텍스트를 인자로 전달하여 텍스트 노드를 생성한다.

appendChild(Node)
: 인자로 전달한 노드를 DOM 트리에 마지막 자식 요소로 추가한다.
```html
<html>
<head>
</head>
<body>
    <h1>createElement/createTextNode/appendChild</h1>
    <script>
        window.onload = function() {
            var header = document.createElement('h3');
            var textNode = document.createTextNode('HI DOM');
    
            header.appendChild(textNode);
            document.body.appendChild(header);
        };
    </script>
</body>
</html>
```

hasAttribute/setAttribute/getAttribute/removeAttribute
---
hasAttribute(attribute)
: 지정한 속성을 가지고 있는지 검사한다.

getAttribute(attribute)
: 속성의 값을 취득한다.

setAttribute(attribute, value)
: 속성과 속성 값을 설정한다.

removeAttribute(attribute)
: 지정한 속성을 제거한다.

```html
<html>
<head>
</head>
<body>
    <h1>attribute</h1>
    <script>
        var a = document.createElement('a');
        var textNode = document.createTextNode('google');

        a.appendChild(textNode);
        if(!a.hasAttribute('href')) {
            a.setAttribute('href', 'http://www.google.com');    
        }
        
        document.write('attribute : ' + a.getAttribute('href') + '<br>');
        document.body.appendChild(a);
    </script>
</body>
</html>
```

innerHTML
: 해당 요소의 모든 자식 요소를 포함하는 모든 콘텐츠를 하나의 문자열로 취득한다.
```html
<html>
<head>
</head>
<body>
    <h1>innerHTML</h1>
    <div id="inner"></div>
    <script>
        window.onload = function() {
            var inner = document.getElementById('inner');
            var output ='';
            output += '<ul>';
            output += ' <li>HTML</li>';
            output += ' <li>Javascript</li>';
            output += '</ul>';

            inner.innerHTML = output;

            inner.innerHTML += '<p>CSS</p>';
        };
    </script>
</body>
</html>
```

parentNode/firstChild/lastChild/next
---
firstChild/lastChild
: 텍스트 요소를 포함한 첫 번째/마지막 자식 노드를 탐색한다.

firstElementChild/lastElementChild
: Element 요소만을 가진 첫 번째/마지막 자식 노드를 탐색한다.

nextSibling/previousSibling
: 텍스트 요소를 포함한 이전/이후 형제 노드를 탐색한다.

nextElementSibling/previousElementSibling
: Element 요소만을 가진 이전/이후 형제 노드를 탐색한다.

parentNode
: 텍스트 요소를 포함한 부모 요소를 탐색한다.

parentElement
: Element 요소만을 가진 부모 요소를 탐색한다.

hasChildNodes/childNodes/children
---
hasChildNodes
: 자식 노드가 있는지 확인하고 Boolean을 반환한다.

childNodes
: 텍스트 요소를 포함한 모든 자식 요소를 탐색한다.

children
: Element 요소만을 가진 모든 자식 요소를 탐색한다.

```html
<html>
<head>
</head>
<body>
    <h1>hasChildNodes/childNodes/children</h1>
    <div id="div01">
        <p>first</p>
        <p>second</p>
        <p>third</p>
    </div>
    
    <script>
        var p1 = document.getElementById('div01');

        if(p1.hasChildNodes()) {
            document.write('<br>' + '<strong>childNodes</strong>' + '<br>');
            for(var i=0; i < p1.childNodes.length; i++) {
                document.write(i + ' ' + p1.childNodes[i].textContent + '<br>');
            }
            document.write('<br>' + '<strong>children</strong>' + '<br>');
            for(var i=0; i < p1.children.length; i++) {
                document.write(i + ' ' + p1.children[i].textContent + '<br>');
            }
        }
    </script>
</body>
</html>
```
