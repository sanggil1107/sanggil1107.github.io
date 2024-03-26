
## print 함수


`print 함수` 는 출력하고 싶은 문자열을 출력하는 함수이다.

```text
print('문자열')
print('문자열', seq, end)
```

- seq : 기본값은 공백(띄어쓰기)이며 출력 시 출력 값들 사이에 넣어줄 구분자
- end : 기본값은 개행(중바꿈)이며 마지막 문자열을 출력하고 그 다음에 출력할 문자


<br>

### print 함수 예제
---


```python
a = 2
b = 10
 
print("a + b : ", a + b)
print(123)
print("Yang")
print("Sanggil")

arr = [1, 2, "yangpang", 3, 4, 'z']
for v in arr:
    print(f"value : {v}")
```
```text
a + b : 12
123
Yang
Sanggil

value : 1
value : 2
value : yangpang
value : 3
value : 4
value : z
```

<br>

```python
s1 = "Fisrt"
s2 = "Second"

print(s1, s2)
```
```text
Fisrt Second
```

<br>

#### end 옵션 예제

```python
print('', end="_")
print('Yang', end="_")
print('Sang', end="%")
print('Gil', end="*")
```
```text
_Yang_Sang%Gil*
```

<br>

#### seq 옵션 예제


```python
print("a", "b", "c", "d")
print("a", "b", "c", "d", sep="*")
print("a", "b", "c", "d", sep="_")
print("a", "b", "c", "d", sep="____")
```
```text
a b c d
a*b*c*d
a_b_c_d
a___b___c___D
```
