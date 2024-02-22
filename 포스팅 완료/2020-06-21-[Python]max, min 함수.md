
## min, max 함수

### min 함수
---

`min 함수` 는 인수로 받은 자료형 내에서 최소값을 찾아서 반환하는 함수이다.

```text
min(x)
min(arg1, arg2, ...)
```

- x : iterabel한 자료형이며 반복 가능한 데이터 타입으로 문자열, 리스트 튜플 등
- arg1, arg2 : 반복 가능한 자료형들로 arg1, arg2 중 작은 매개변수를 반환

문자열의 경우, 알파벳 순서 상 맨 앞에 오는 문자열을 반환한다.

<br>

#### min 함수 예제

```python
a = [1, 2, 3]
print(min(a))  

b = 'BlockDMask'
print(min(b)) 

c = (6, 5, 4, 2)
print(min(c))  

d = 1
print(min(d))  
# error : 'int' object is not iterable

e = [3, 4, 5, 'a', 'b', 'c']
print(min(e))  
# error : str 타입과 int 타입은 비교 불가
```
```text
1
B
2
```

<br>

```python
a = [1, 2, 3]
b = [4, 5, 6]
print(min(a, b))   

c = 'hello'
d = 'world'
print(min(c, d))   

e = [2, 3, 4]
f = [2, 2, 2, 2, 2]
g = [9, 8, 7, 6, 5]
h = [1]
i = [0]
print(min(e, f, g, h, i))   
```
```text
[1, 2, 3]
hello
[0]
```

<br>


### max 함수
---

`max 함수` 는 인수로 받은 자료형 내에서 최대값을 찾아서 반환하는 함수이다.

```text
max(x)
max(arg1, arg2, ...)
```

- x : iterabel한 자료형이며 반복 가능한 데이터 타입으로 문자열, 리스트 튜플 등
- arg1, arg2 : 반복 가능한 자료형들로 arg1, arg2 중 큰 매개변수를 반환

문자열의 경우, 알파벳 순서 상 맨 뒤에 오는 문자열을 반환한다.

<br>

#### max 함수 예제


```python
a = [1, 2, 3]
print(max(a))  

b = 'BlockDMask'
print(max(b)) 

c = (6, 5, 4, 2)
print(max(c))  
```
```text
3
s
6
```

<br>

```python
a = [1, 2, 3]
b = [4, 5, 6]
print(max(a, b))   

c = 'hello'
d = 'world'
print(max(c, d))   

e = [2, 3, 4]
f = [2, 2, 2, 2, 2]
g = [9, 8, 7, 6, 5]
h = [1]
i = [0]
print(max(e, f, g, h, i))   
```
```text
[4, 5, 6]
world
[9, 8, 7, 6, 5]
```