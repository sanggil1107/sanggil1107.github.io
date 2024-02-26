
## sum 함수

`sum 함수` 는 인자로 들어온 값의 합을 구하는 함수이다.

```text
sum(x)
sum(x, start)
```

- x : 반복가능한 정수 자료형으로 리스트나 튜플처럼 인덱스 순환 접근이 가능한 자료형
- start : 처음으로 다시 더해줄 숫자
  
sum 함수의 인자 값은 숫자로만 이루어져 있어야하며 두번째 인자(start) 값이 있을 경우에는
첫번째 인자의 합 + 두번째 인자의 합을 반환한다.

<br>

#### sum 함수 예제

```python
result1 = sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(result1)  

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
result2 = sum(a)
print(result2) 

b = []
c = ()
result3 = sum(b)
result4 = sum(c)

print(result3)  # 출력 : 0
print(result4)  # 출력 : 0
```
```text
55
55
0
0
```

<br>

```python
result1 = sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
result2 = sum([])

print(result1)  # 출력 : 55 (리스트) + 0 (start) = 55
print(result2)  # 출력 : 0  (리스트) + 0 (start) = 0


result3 = sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1111)
result4 = sum([], 1111)

print(result3)  # 55 + 1111
print(result4)  # 0 + 1111
```
```text
55
0

1166
1111
```
