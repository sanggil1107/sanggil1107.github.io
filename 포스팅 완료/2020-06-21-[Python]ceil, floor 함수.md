
## ceil/floor 함수

### ceil 함수
---

`ceil 함수` 는 인자로 들어온 x의 올림 값을 반환하는 함수이다.

```text
ceil(x)
```

- x : 실수 타입의 자료형

ceil 함수는 math 라이브러리를 import 해야하며 반환 값은 정수 타입이다. 또한, 음수도 올림이 가능하다.

<br>

#### ceil 함수 예제

```python
import math
 
print("ceil(2.0) : " + str(math.ceil(2.0)))
print("ceil(2.2) : " + str(math.ceil(2.2)))
print("ceil(2.4) : " + str(math.ceil(2.4)))
print("ceil(2.6) : " + str(math.ceil(2.6)))
print("ceil(2.8) : " + str(math.ceil(2.8)))
print("ceil(3.0) : " + str(math.ceil(3.0)))
print("ceil(3.2) : " + str(math.ceil(3.2)))
```
```text

ceil(2.0) : 2
ceil(2.2) : 3
ceil(2.4) : 3
ceil(2.6) : 3
ceil(2.8) : 3
ceil(3.0) : 3
ceil(3.2) : 4
```

<br>

```python
import math

print("ceil(-2.0) : " + str(math.ceil(-2.0)))
print("ceil(-2.2) : " + str(math.ceil(-2.2)))
print("ceil(-2.4) : " + str(math.ceil(-2.4)))
print("ceil(-2.6) : " + str(math.ceil(-2.6)))
print("ceil(-2.8) : " + str(math.ceil(-2.8)))
print("ceil(-3.0) : " + str(math.ceil(-3.0)))
print("ceil(-3.2) : " + str(math.ceil(-3.2)))
```
```text
ceil(-2.0) : -2
ceil(-2.2) : -2
ceil(-2.4) : -2
ceil(-2.6) : -2
ceil(-2.8) : -2
ceil(-3.0) : -3
ceil(-3.2) : -3
```


<br>

### floor 함수
---

`floor 함수` 는 인자로 들어온 x의 내림 값을 반환하는 함수이다.

```text
floor(x)
```

- x : 실수 타입의 자료형

floor 함수는 math 라이브러리를 import 해야하며 반환 값은 정수 타입이다. 또한, 음수도 내림이 가능하다.

<br>

#### floor 함수 예제


```python
import math
 
print("floor(2.0) : " + str(math.floor(2.0)))
print("floor(2.2) : " + str(math.floor(2.2)))
print("floor(2.4) : " + str(math.floor(2.4)))
print("floor(2.6) : " + str(math.floor(2.6)))
print("floor(2.8) : " + str(math.floor(2.8)))
print("floor(3.0) : " + str(math.floor(3.0)))
print("floor(3.2) : " + str(math.floor(3.2)))
```
```text
floor(2.0) : 2
floor(2.2) : 2
floor(2.4) : 2
floor(2.6) : 2
floor(2.8) : 2
floor(3.0) : 3
floor(3.2) : 3
```

<br>

```python
import math

print("floor(-2.0) : " + str(math.floor(-2.0)))
print("floor(-2.2) : " + str(math.floor(-2.2)))
print("floor(-2.4) : " + str(math.floor(-2.4)))
print("floor(-2.6) : " + str(math.floor(-2.6)))
print("floor(-2.8) : " + str(math.floor(-2.8)))
print("floor(-3.0) : " + str(math.floor(-3.0)))
print("floor(-3.2) : " + str(math.floor(-3.2)))
```
```text
floor(-2.0) : -2
floor(-2.2) : -3
floor(-2.4) : -3
floor(-2.6) : -3
floor(-2.8) : -3
floor(-3.0) : -3
floor(-3.2) : -4
```
