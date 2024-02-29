
## isdigit 함수


`isdigit 함수` 는 문자열이 숫자로만 이루어져있는지 확인하는 함수이다.

```text
str.isdigit("문자열")
"문자열".isdigit()
```


문자가 단 하나라도 있다면 False를 반환하고 모든 문자가 숫자로만 이루어져 있으면 True를 반환한다. 또한, 음수를 뜻하는 '-'와 소수점을 뜻하는 '.'는 문자로 판단한다.

<br>

### isdigit 함수 예제
---


```python
a = "BlockDMask"  
print(f"str.isdigit('{a}') : {str.isdigit(a)}")
print(f"'{a}'.isdigit() : {a.isdigit()}")

b = "1234Blog"    
print(f"str.isdigit('{b}') : {str.isdigit(b)}")
print(f"'{b}'.isdigit() : {b.isdigit()}")

c = "131231"    
print(f"str.isdigit('{c}') : {str.isdigit(c)}")
print(f"'{c}'.isdigit() : {c.isdigit()}")

d = "-234"     
print(f"str.isdigit('{d}') : {str.isdigit(d)}")
print(f"'{d}'.isdigit() : {d.isdigit()}")

e = "1.23"        
print(f"str.isdigit('{e}') : {str.isdigit(e)}")
print(f"'{e}'.isdigit() : {e.isdigit()}")

f = "3²"          
print(f"str.isdigit('{f}') : {str.isdigit(f)}")
print(f"'{f}'.isdigit() : {f.isdigit()}")

g = "⅔"           
print(f"str.isdigit('{g}') : {str.isdigit(g)}")
print(f"'{g}'.isdigit() : {g.isdigit()}")

h = "0"           
print(f"str.isdigit('{h}') : {str.isdigit(h)}")
print(f"'{h}'.isdigit() : {h.isdigit()}")

i = "0123"        
print(f"str.isdigit('{i}') : {str.isdigit(i)}")
print(f"'{i}'.isdigit() : {i.isdigit()}")
```
```text
str.isdigit('BlockDMask') : False
'BlockDMask'.isdigit() : False

str.isdigit('1234Blog') : False
'1234Blog'.isdigit() : False

str.isdigit('131231') : True
'131231'.isdigit() : true

str.isdigit('-234') : False
'-234'.isdigit() : False

str.isdigit('1.23') : False
'1.23'.isdigit() : False

str.isdigit('3²') : True
'3²'.isdigit() : True

str.isdigit('⅔') : False
'⅔'.isdigit() : False

str.isdigit('0') : True
'0'.isdigit() : True

str.isdigit('0123') : True
'0123'.isdigit() : True
```
