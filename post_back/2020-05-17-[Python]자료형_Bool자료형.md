



# 불(bool) 자료형
---
불(bool) 자료형이란 참(True)과 거짓(False)을 나타내는 자료형이다.  
- True : 참
- False : 거짓
```python
>>> a = True
>>> b = False
>>> type(a)
<class 'bool'>
>>> type(b)
<class 'bool'>

>>> 1 == 1
True
>>> 2 < 1
False
```

## 자료형의 참/거짓
---
자료형에도 참/거짓이 있으며 아래는 자주 사용하는 자료형의 참/거짓이다.  
비어 있는 자료형은 거짓(False)이며 비어 있지 않으면 참(True)이다.
|값|참/거짓|
|---|---|
|'문자열'|True|
|""|False|
|[1,2,3]|True|
|[]|False|
|()|False|
|{}|False|
|1|True|
|0|False|
|None|False|

불(bool) 자료형의 사용 예제는 다음과 같다.
```python
>>> a = [1,2,3,4]
>>> while a:
...     print(a.pop())
...
4
3
2
1

>>> if [] :
...     print("참")
... else:
...     print("거짓")
...
거짓

>>> if [1,2]:
...     print("참")
... else:
...     print("거짓")
...
참
```

## 불(bool) 연산
---
```python
>>> bool("python")
True
>>> bool("")
False
>>> bool(0)
False
>>> bool(1)
True
>>> bool(3)
True
>>> bool([])
False
```
