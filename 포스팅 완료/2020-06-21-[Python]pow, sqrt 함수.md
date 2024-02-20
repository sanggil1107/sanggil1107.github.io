
## pow, sqrt 함수

### pow 함수
---

`pow 함수` 는 인자로 받은 자료형으로 거듭제곱을 반환하는 함수이다.

```text
pow(x, y)
```

- x, y : 실수 자료형

pow 함수는 math 라이브러리를 import 해야하며 반환형은 실수형 타입이다.
x가 음수이면서 y가 실수인 경우에는 Error가 발생한다.


<br>

#### pow 함수 예제

```python
import math
 
result1 = math.pow(2, 4)
result2 = math.pow(1, 5)
result3 = math.pow(9, 0)

print(result1)
print(result2)
print(result3)
```
```text
16.0
1.0
1.0
```

<br>


### sqrt 함수
---

`sqrt 함수` 는 인자의 제곱근을 반환하는 함수이다.

```text
sqrt(x)
```

- x : 실수 자료형

sqrt 함수는 math 라이브러리를 import 해야하며 반환형은 실수형 타입이다.
x가 음수인 경우에는 Error가 발생한다.

<br>

#### sqrt 함수 예제


```python
import math
 
result1 = math.sqrt(4)
result2 = math.sqrt(1)
result3 = math.sqrt(0)

print(result1)
print(result2)
print(result3)
```
```text
2.0
1.0
0.0
```
