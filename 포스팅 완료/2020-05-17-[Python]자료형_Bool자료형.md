

## 불(bool) 자료형

파이썬 불(bool) 자료형이란 참(True)과 거짓(False)을 나타내는 자료형이다.

- True : 참
- False : 거짓
  
```python
a = True
b = False

print(type(a))
print(type(b))
print(1 == 1)
print(2 < 1)
```

```text
<class 'bool'>
<class 'bool'>
True
False
```

<br>

### 자료형의 참/거짓
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
a = [1,2,3,4]
while a:
    print(a.pop())


if [] :
    print("참")
else:
    print("거짓")


if [1,2]:
    print("참")
else:
    print("거짓")

```
```text
4
3
2
1

거짓
참
```

<br>

### 불(bool) 연산
---

```python
print(bool("python"))
print(bool(""))
print(bool(0))
print(bool(1))
print(bool(3))
print(bool([]))
```
```text
True
False
False
True
True
False
```
