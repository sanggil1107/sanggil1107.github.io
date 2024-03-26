
## input 함수


`input 함수` 는 사용자로부터 입력을 받는 함수이다.

```text
input()
input('문자열')
```

사용자의 입력을 받고 입력은 엔터가 입력될 때 엔터 전까지 모두 받는다. 반환값으로는 사용자가 입력한 것을 문자열 타입으로 반환한다.

<br>

### input 함수 예제
---


```python
a = input()
print(f'첫번째로 입력 하신 것은 : {a} 입니다.')
 
 
b = input()
print(f'두번째로 입력 하신 것은 : {b} 입니다.')
```
```text
yang
첫번째로 입력 하신 것은 : yang 입니다.

sanggil
첫번째로 입력 하신 것은 : sanggil 입니다.
```

<br>

```python

a = input("사용자 입력 : ")
print(f'입력 하신 것은 : {a} 입니다.')

```
```text
사용자 입력 : 500
입력 하신 것은 : 500 입니다.
```

<br>


```python
i = 0
result = 0
while i < 5:
    a = input("성적 입력 : ")
    result += int(a)
    i += 1
 
print(f'평균 : {result / 5}')
```
```text
성적 입력 : 10
성적 입력 : 30
성적 입력 : 50
성적 입력 : 70
성적 입력 : 100
평균 : 52.0
```
