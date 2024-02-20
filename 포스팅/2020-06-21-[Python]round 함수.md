
## round 함수


`round 함수` 는 소수점 다음에 정밀도로 반올림한 값을 돌려주는 함수이다.

```text
round(number [, ndigits])
```

- function : 필터링을 적용시킬 함수
- iterable : 반복 가능한 자료(리스트, 튜플 등)

filter 함수의 반환 값은 filter 객체이기 때문에 해당 자료형을 list나 tuple로 형 변환해야 한다.
filter 함수는 iterator에 들어온 값들을 하나하나 function에 넣어서 반환이 true인 값을 필터링해서 다시 리스트로 만들어준다.

<br>

filter 함수를 사용하지 않을 때와 사용할 때의 소스를 확인해보자.

- for 문 이용
  
```python
def is_even(x):
    if x % 2 == 0:
        return True
    return False

arr = []
for val in range(1, 11): 
    if is_even(val):
        arr.append(val)
    
print(arr)
```
```text
[2, 4, 6, 8, 10]
```

<br>

- filter 함수 이용

```python
def is_even(x):
    if x % 2 == 0:
        return True
    return False

arr = list(filter(is_even, range(1,11)))
print(arr)
```
```text
[2, 4, 6, 8, 10]
```

<br>

### filter 함수 예제
---


```python
arr = [1, 10.2, 100.3, 2.3, 20.2, 200.3, 3, 30, 300]

def func1(n):
    if n < 10: 
        return True
    return False

def func2(n):
    if isinstance(n , int):
        return True
    return False

result1 = list(filter(func1 ,arr))
result2 = list(filter(func2 ,arr))

print(result1)
print(result2)
```
```text
[1, 2.3, 3]
[1, 3, 30, 300]
```

<br>

```python
def Fillterfunc(num):
  return num > 40

numlist = [10, 20, 30, 40, 50, 60, 70, 80, 90]

result = list(filter(Fillterfunc, numlist))

print(result)
```
```text
[50, 60, 70, 80, 90]
```


<br>

일반적인 함수뿐만 아니라 람다함수와 함께 사용할 수 있다.

```python
numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = list(map(lambda x : x % 2 == 0, numlist))
print(result2)
```
```text
[2, 4, 6, 8]
```
