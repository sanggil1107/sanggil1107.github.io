
## ord/chr 함수

### ord 함수
---

`ord 함수` 는 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환하는 함수이다.

```text
ord(문자)
```


<br>

#### ord 함수 예제

```python
result1 = ord('a')
result2 = ord('ㄱ')
result3 = hex(ord('b'))

print(result1)
print(result2)
print(result3)
```
```text
97
12593
0x62
```


<br>

### chr 함수
---

`chr 함수` 는 하나의 정수를 인자로 받고 해당 정수에 해당하는 유니코드 문자를 반환하는 함수이다.

```text
chr(정수)
```

chr 함수의 인자(정수) 유효 범위는 0 ~ 1,114,111 (16진수 0x10 FFFF)까지이다.

<br>

#### chr 함수 예제


```python
result1 = chr(97)
result2 = chr(12593)
result3 = chr(0x62)

print(result1)
print(result2)
print(result3)
```
```text
a
ㄱ
b
```

<br>

```python
for i in range(97,123):
    print(chr(i), end=' ')
```
```text
a b c d e f g h i j k l m n o p q r s t u v w x y z
```
