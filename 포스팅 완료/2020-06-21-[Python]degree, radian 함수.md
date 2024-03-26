
## degree, radian 함수


`degree 함수` 는 인자로 받은 라디안 값을 각도 표기법으로 변환하여 반환하는 함수이다.
`radian 함수` 는 인자로 받은 각도 값을 라디안 표기법으로 변환하여 반환하는 함수이다.


```text
degree(x)
radian(x)
```

- x : 라디안 값 or 각도 

각도를 의미하는 degree, radian을 사용하기 위해서는 math 모듈을 import 해야한다.

<br>

### degree, radian 함수 예제
---


```python
import math

a = math.degrees(2 * math.pi) 
b = math.radians(360)  
c = math.pi

print(f"math.degrees(2 * math.pi) : {a}")
print(f"math.radians(360) : {b}")
print(f"math.pi : {c}")
```
```text
math.degrees(2 * math.pi) : 360.0
math.radians(360) : 6.283185307179586
math.pi : 3.141592653589793
```
