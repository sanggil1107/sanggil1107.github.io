
## round 함수


`round 함수` 는 소수점 다음에 정밀도로 반올림한 값을 돌려주는 함수이다.

```text
round(number [, ndigits])
```

- function : 반올림하고자 하는 숫자 자료형
- ndigits : 정밀도(자릿수)

파이썬의 반올림은 반올림 하려는 수가 올림, 내림했을 때 동일하게 차이가 나는 경우에는 짝수 값으로 반올림한다.

<br>

### round 함수 예제
---


```python
print('round(0.5) : {0}'.format(round(0.5)))
print('round(1.5) : {0}'.format(round(1.5)))
print('round(2.5) : {0}'.format(round(2.5)))
print('round(3.5) : {0}'.format(round(3.5)))
print('round(4.5) : {0}'.format(round(4.5)))
print('round(5.5) : {0}'.format(round(5.5)))
print('round(6.5) : {0}'.format(round(6.5)))
```
```text
round(0.5) : 0 
round(1.5) : 2
round(2.5) : 2 
round(3.5) : 4    
round(4.5) : 4 
round(5.5) : 6
round(6.5) : 6 
```

<br>

```python
print('round(-6.5) : {0}'.format(round(-6.5)))
print('round(-5.5) : {0}'.format(round(-5.5)))
print('round(-4.5) : {0}'.format(round(-4.5)))
print('round(-3.5) : {0}'.format(round(-3.5)))
print('round(-2.5) : {0}'.format(round(-2.5)))
print('round(-1.5) : {0}'.format(round(-1.5)))
print('round(-0.5) : {0}'.format(round(-0.5)))
```
```text
round(-6.5) : -6
round(-5.5) : -6
round(-4.5) : -4
round(-3.5) : -4
round(-2.5) : -2
round(-1.5) : -2
round(-0.5) : 0
```

<br>


```python
a = 0.0
while a < 2.1:
    result = round(a)
    print('round({0}) => {1}'.format(a, result))
    a += 0.1
```
```text
round(0.0) => 0
round(0.1) => 0
round(0.2) => 0
round(0.30000000000000004) => 0
round(0.4) => 0
round(0.5) => 0 
round(0.6) => 1
round(0.7) => 1
round(0.7999999999999999) => 1
round(0.8999999999999999) => 1
round(0.9999999999999999) => 1
round(1.0999999999999999) => 1
round(1.2) => 1
round(1.3) => 1
round(1.4000000000000001) => 1
round(1.5000000000000002) => 2 
round(1.6000000000000003) => 2
round(1.7000000000000004) => 2
round(1.8000000000000005) => 2
round(1.9000000000000006) => 2
round(2.0000000000000004) => 2
round(2.1000000000000005) => 2
round(2.2000000000000006) => 2
round(2.3000000000000007) => 2
round(2.400000000000001) => 2
round(2.500000000000001) => 3 
round(2.600000000000001) => 3
round(2.700000000000001) => 3
round(2.800000000000001) => 3
round(2.9000000000000012) => 3
round(3.0000000000000013) => 3
```
