
## gcd, lcm 함수

### gcd 함수
---

`gcd 함수` 는 인자로 들어온 숫자들의 최대 공약수(정수)를 반환하는 함수이다.

```text
gcd(x)
```

- x : 숫자, 인자는 0개부터 N개까지 가능

gcd 함수는 math 라이브러리를 import 해야한다. 

<br>

#### gcd 함수 예제

```python
import math
 
a = math.gcd()
b = math.gcd(0, 2, 4)
c = math.gcd(10, 5, 100)

print(a)
print(b)
print(c)
```
```text
0
2
5
```

<br>

```python
import math

a = math.gcd(0)
b = math.gcd(0, 0)
c = math.gcd(0, 0, 0, 0)

print(a)
print(b)
print(c)
```
```text
0
0
0
```

<br>

```python
import math

a = math.gcd(3)
b = math.gcd(3, 6, 3, 3, 3, 3)
c = math.gcd(66, 22, 11, 33, 44)

print(a)
print(b)
print(c)
```
```text
3
3
11
```

<br>

### lcm 함수
---

`lcm 함수` 는 인자로 들어온 숫자들의 최소 공배수를 반환하는 함수이다.

```text
lcm(x)
```

- x : 숫자, 인자는 0개부터 N개까지 가능

lcm 함수는 math 라이브러리를 import 해야한다.

<br>

#### lcm 함수 예제


```python
import math
 
a = math.lcm()
b = math.lcm(0, 2, 4)
c = math.lcm(10, 5, 100)

print(a)
print(b)
print(c)
```
```text
1
0
100
```

<br>

```python
import math

a = math.lcm(0)
b = math.lcm(0, 0)
c = math.lcm(0, 0, 0, 0)

print(a)
print(b)
print(c)
```
```text
0
0
0
```

<br>

```python
import math

a = math.lcm(0)
b = math.lcm(3, 6, 1, 3, 3, 3)
c = math.lcm(66, 22, 11, 33, 44)

print(a)
print(b)
print(c)
```
```text
0
6
132
```
