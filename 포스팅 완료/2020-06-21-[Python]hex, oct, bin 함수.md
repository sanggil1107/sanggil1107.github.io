
## hex, oct, bin 함수

### hex 함수
---

`hex 함수` 는 매개변수 x에 정수 값을 입력 받아서 16진수로 변환하여, 변환한 값을 반환하는 함수이다.

```text
hex(x)
```

- x : 정수


<br>

#### hex 함수 예제

```python
a = hex(10)
print(f'hex(10) = {a}') 

b = hex(145)
print(f'hex(145) = {b}')
```
```text
hex(10) = 0xa

hex(145) = 0x91
```


<br>

### oct 함수
---

`oct 함수` 는 매개변수 x에 정수 값을 입력 받아서 8진수로 변환하여, 변환한 값을 반환하는 함수이다.

```text
oct(x)
```

- x : 정수


<br>

#### oct 함수 예제


```python
a = oct(10) 
print(f'oct(10) = {a}')

b = oct(233) 
print(f'oct(233) = {b}') 
```
```text
oct(10) = 0o12

oct(233) = 0o351
```

<br>

### bin 함수
---

`bin 함수` 는 매개변수 x에 정수 값을 입력 받아서 2진수로 변환하여, 변환한 값을 반환하는 함수이다.

```text
bin(x)
```

- x : 정수


<br>

#### bin 함수 예제


```python
a = bin(10) 
print(f'bin(10) = {a}') 

b = bin(301) 
print(f'bin(301) = {b}')
```
```text
bin(10) = 0b1010

bin(301) = 0b100101101
```
