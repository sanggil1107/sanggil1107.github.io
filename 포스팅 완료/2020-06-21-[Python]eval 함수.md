
## eval 함수


`eval 함수` 는 매개변수로 받은 식(expression)을 무자열로 받아서 실행하는 함수이다.

```text
eval(expression)
```

- expression : 값, 연산자, 변수 등 파이썬에서 사용하여 무언가를 표현할 수 있는 것들로 하나 이상의 값으로 표현될 수 있는 코드

eval 함수는 문자열로 들어온 expression을 실행해서 결과값을 리턴한다. 이는 사용자 마음대로 프로그램을 조종할 수 있다(프로그램에 명령을 입력)는 의미이고 즉, 프로그램을 상처입히거나 해킹을 하거나 할 수 있다는 뜻과 동일하다.

<br>

### eval 함수 예제
---


```python
result1 = eval('"BlockDMask" + "blog"')
result2 = eval("100 + 32")
result3 = eval("abs(-56)")
result4 = eval("len([1,2,3,4])")
result5 = eval("round(1.5)")

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
```
```text
BlockDMaskblog
132
56
4
2
```
