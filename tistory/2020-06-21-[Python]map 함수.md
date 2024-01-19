
## map 함수


`map 함수` 는 여러 개의 데이터를 한 번에 다른 형태로 변환할 때 사용한다.

```text
map(function, iterable)
```

- function : 반복 가능한 모든 요소에 대해 호출되는 함수
- iterable : 반복 가능한 자료형(리스트, 튜플 등)

map 함수의 반환 값은 map 객체이기 때문에 해당 자료형을 list나 tuple로 형 변환해야 한다.
동작 방식은 두번째 인자로 들어온 반복 가능한 자료형을 첫번째 인자로 들어온 함수에 하나씩 넣어 수행한다.

<br>

map 함수를 사용하지 않을 때와 사용할 때의 소스를 확인해보자.

- for 문 이용
  
```python
myList = [1, 2, 3, 4, 5]

result = []
for val in myList:
    result.append(val + 1)

print(result)
```
```text
[2, 3, 4, 5, 6]
```

<br>

- map 함수 이용

```python
myList = [1, 2, 3, 4, 5]

def add_one(n):
    return n + 1

result = list(map(add_one, myList))  
print(result)
```
```text
[2, 3, 4, 5, 6]
```

<br>

### map 함수 예제
---

map 함수를 활용하면 코드가 간단해지고 유연해진다.

```python
def to_upper_case(s):
    return s.upper()

directions = ["north", "east", "south", "west"]

directions_upper = list(map(to_upper_case, directions))

print(directions_upper)

```
```text
['NORTH', 'EAST', 'SOUTH', 'WEST']
```

<br>

```python
def multiply(x, y):
  return x * y

a = [1, 4, 6]
b = [2, 3, 5]

result = list(map(multiply, a, b))

print(result)
```
```text
[2, 12, 30]
```

<br>

```python
def func_pow(x):
    return pow(x, 5)  

result = list(map(func_pow, [1, 2, 3, 4, 5]))
print(result)
```
```text
[1, 32, 243, 1024, 3125]
```

<br>

일반적인 함수뿐만 아니라 람다함수와 함께 사용할 수 있다.

```python
result = list(map(lambda x : x * 2, [5, 4, 3, 2, 1]))
print(result2)
```
```text
[10, 8, 6, 4, 2]
```
