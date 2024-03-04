
## isalpha 함수


`isalpha 함수` 는 문자열이 모두 알파벳으로만 이루어져 있는지 확인하는 함수이다.

```text
"문자열".isalpha()
```

문자열이 모두 알파벳으로 이루어져 있으면 True를 반환, 그렇지 않으면 False를 반환한다.

<br>

### isalpha 함수 예제
---


```python
a = "1"  
print(f"'{a}'.isalpha() : {a.isalpha()}")

b = "1.2"    
print(f"'{b}'.isalpha() : {b.isalpha()}")

c = "BlockDMask"    
print(f"'{c}'.isalpha() : {c.isalpha()}")

d = "12ab"     
print(f"'{d}'.isalpha() : {d.isalpha()}")

e = "abc123"     
print(f"'{e}'.isalpha() : {d.isalpha()}")
```
```text
'BlockDMask'.isalpha() : False

'1.2'.isalpha() : False

'BlockDMask'.isalpha() : True

'12ab'.isalpha() : False

'abc123'.isalpha() : False
```
