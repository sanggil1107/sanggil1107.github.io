# JSON 이란

JavaScript Object Notation이라는 의미의 축약어로 데이터를 저장하거나 전송할 때 많이 사용되는 경량의 DATA 교환 형식

## 특징

- JavaScript에서 객체를 만들 때 사용하는 표현식
- 데이터 교환 형식 중 하나로 프로그래밍 언어가 아닌 단순히 데이터를 표시하는 표현 방법
- AJAX에서 많이 쓰이며 서버와 클라이언트간의 교류에서 많이 사용
- 특정 언어에 종속되지 않으며 대부분의 프로그래밍 언어에서 JSON 포맷의 데이터를 핸들링 할 수 있는 라이브러리를 제공
- 파일 확장자는 .json


## 구조

- JSON 데이터는 이름(Key)과 값(Value)의 쌍으로 이루어지며 쌍따옴표(")로 감싸준다.
  - {"Key" : "Value"}
- Key 값은 문자열로 구성되며 Value 값에는 아래와 같은 타입이 올 수 있다.
  - 숫자(number), 문자(string), 불리언(boolean), 객체(object), 배열(array), NULL
- JSON 데이터는 쉼표(,)로 나열된다.
- 객체는 중괄호로 표현한다.
- 배열은 대괄호로 표현한다.

```json
{
	"name": "Yang",
	"age": 30,
	"hobby": ["reading", "exercise"]
}
```

```json
{
    "person": [
        {
            "name": "Yang",
	        "age": 30
        },
        {
            "name": "Choi",
	        "age": 28
        }
    ]	
}
```

## 변환

### JSON.stringify()

Javascript 객체나 값을 JSON 문자열로 변환


### JSON.parse()

JSON 문자열을 Javascript 객체로 변환


## 검증

https://jsonlint.com/ 사이트에서 작성한 JSON의 유효성을 검증할 수 있다.