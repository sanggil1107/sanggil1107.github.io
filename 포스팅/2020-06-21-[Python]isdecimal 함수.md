
## isdecimal 함수


`isdecimal 함수` 는 문자열이 int 타입으로 변경가능한지 확인하는 함수이다.

```text
"문자열".isdecimal()
```

데이터가 int 타입으로 변환이 가능한 숫자인 경우 True를 반환, 그렇지 않으면 False를 반환한다.

<br>

### isdecimal 함수 예제
---


```python
a = "1"  
print(f"'{a}'.isdecimal() : {a.isdecimal()}")

b = "1.2"    
print(f"'{b}'.isdecimal() : {b.isdecimal()}")

c = "BlockDMask"    
print(f"'{c}'.isdecimal() : {c.isdecimal()}")

d = "12ab"     
print(f"'{d}'.isdecimal() : {d.isdecimal()}")
```
```text
'1'.isdecimal() : True

'1.2'.isdecimal() : False

'BlockDMask'.isdecimal() : False

'12ab'.isdecimal() : False
```
