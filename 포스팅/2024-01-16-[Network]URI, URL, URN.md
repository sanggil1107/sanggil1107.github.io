## URI, URL, URN

`URI`, `URL`, `URN` 에 대해 알아보자

[이미지]

<br>

### URI(Uniform Resource Identifier)
---

- 통합 자원 식별자를 의미한다.
- 인터넷에 있는 자원을 나타내는 유일한 주소를 말한다.
- URI의 존재는 인터넷에서 요구되는 기본조건으로 인터넷 프로토콜에 항상 붙어 다닌다.

<br>

### URL(Uniform Resource Locator)
---

- 프로토콜(스키마)을 포함한 개념이다.
- 네트워크 상에서 자원이 어디에 있는지 알려주기 위한 규약을 말한다.
- 일반적으로 사이트 도메인을 의미한다.
- 웹 상 뿐만 아니라 컴퓨터 네트워크 상의 자원을 모두 나타낼 수 있다.

<br>

### URN(Uniform Resource Name)
---

- 프로토콜(스키마)을 포함하지 않는 개념이다.
- 해당 자원의 이름을 의미한다.
- 자원에 대하여 영속적으로 유일하다.
- 위치에 독립적인 이름을 제공하기 위하여 존재한다.

<br>

### URI, URL, URN 구조
---

```text
scheme://[userinfo@]host[:port][/path][?query][#fragment]
```

`https://www.google.com:443/search?q=hello&hl=ko` 를 통해 구조를 확인해보자.

- <strong>scheme</strong> : `https`
  - 프로토콜을 의미
  - 어떤 방식으로 자원에 접근할지에 대한 규약(https, http, ftp)

- <strong>[userinfo@]</strong> : `해당 없음`
  - 사용자 정보를 의미
  - 거의 사용하지 않음

- <strong>host</strong> : `www.google.com`
  - 호스트명
  - 도메인명 또는 ip 주소 사용 가능

- <strong>[:port]</strong> : `:443`
  - 접속 포트이며 일반적으로 생략

- <strong>[/path]</strong> : `search`
  - 리소스 경로

- <strong>[?query]</strong> : `?q=hello&hl=ko`
  - key = value 형태
  - ?로 시작하며 &로 추가 가능
  - Query Parameter, Query String 으로 불림