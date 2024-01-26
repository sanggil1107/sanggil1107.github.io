
## all/any 함수

### all 함수
---

`all 함수` 는 인자로 받은 반복 가능한 자료형(iterable)의 모든 요소가 참(True)이면 참(True)을 반환하는 함수이다.

```text
all(iterable)
```

- iterable : 반복 가능한 자료형(리스트, 튜플 등)

all 함수는 인자로 받은 데이터의 모든 요소가 True 일 때 True를 반환한다.
만약 인자로 받은 자료형이 비어있다면 True를 반환한다.

<br>

#### all 함수 예제

```python
arr = [1, 2, 3, 4, 5]
 
if all(i < 10 for i in arr):
    print("성공!")
```
```text
성공!
```

<br>

```python
a = [1,2,3,4,5]
result = all(a)
print(result)

c = []
result = all(c)
print(result)

g = ('b', 2, 0, 'd')
result = all(a)
print(result)
```
```text
True

True

False
```

<br>

```python
print(all([False, True, False]))
print(all([True, True, True]))
```
```text
False
False
```

<br>

### any 함수
---

`any 함수` 는 인자로 받은 반복가능한 자료형(iterable)중 단 하나라도 참(True)이 있으면 참(True)를 반환하는 함수이다.

```text
any(iterable)
```

- iterable : 반복 가능한 자료형(리스트, 튜플 등)

any 함수는 인자로 받은 데이터의 모든 요소가 False 일 때 False를 반환한다.
만약 인자로 받은 자료형이 비어있다면 False 반환한다.

<br>

#### any 함수 예제


```python
arr = [1, 2, 3, 14, 15]
 
if any(i < 10 for i in arr):
    print("성공!")
```
```text
성공!
```

<br>

```python
a = [1,2,3,4,5]
result = any(a)
print(result)

c = []
result = any(c)
print(result)

g = ('b', 2, 0, 'd')
result = any(a)
print(result)
```
```text
True

False

True
```

<br>

```python
print(any([False, False, False]))
print(any([True, True, False]))
```
```text
False
True
```
