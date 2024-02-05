
## reduce 함수


`reduce 함수` 는 반복 가능한 객체(iterable object) 내 각 요소를 연산한 뒤 이전 연산 결과들과 누적해서 반환해 주는 함수이다.

```text
from functolls import reduce

reduce(function, iterable)
```

- function : 연산을 적용시킬 함수
- iterable : 반복 가능한 자료(리스트, 튜플 등)

파이썬3부터는 reduce가 내장 함수가 아니기 때문에 functools 모듈에서 reduce 함수를 불러와야 한다.

<br>

reduce 함수를 사용하지 않을 때와 사용할 때의 소스를 확인해보자.

- for 문 이용
  
```python
def SumFunction(x, y):
    return x + y

target = list(range(1, 21))
result = 0
for value in target:
    result = SumFunction(result, value)
print(result) 
```
```text
210
```

<br>

- reduce 함수 이용

```python
from functools import reduce

def SumFunction(x, y):
    return x + y
    
target = list(range(1, 21))
print(reduce(SumFunction, target)) 
```
```text
210
```

<br>

### reduce 함수 예제
---

```python
from functools import reduce

def get_larger_value(a, b):    
    if a > b:        
        return a    
    else:        
        return b 

result = reduce(get_larger_value, [1,6,3,0])
print(result)
```
```text
6
```


<br>

일반적인 함수뿐만 아니라 람다함수와 함께 사용할 수 있다.

```python
from functools import reduce

target = list(range(1, 21))
print(reduce(lambda x, y: x + y, target))
```
```text
210
```

<br>

```python
from functools import reduce

f = lambda x, y: 3*x+2*y

result = reduce(f, [1,2,3])
print(result)
```
```text
27
```
