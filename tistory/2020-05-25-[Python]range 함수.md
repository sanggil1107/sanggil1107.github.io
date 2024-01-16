

## range

파이썬에서 range() 함수는 연속된 숫자들을 만들어내는 내장함수이며 주로 for 반복문과 함께 사용되는 경우가 많으며 아래 3가지 구문이 있다.

```text
range(stop)
range(start, stop)
range(start, stop, step)
```

<br>

### range(stop)
---

```python
range(stop)
```

- stop : 생성할 숫자 범위의 끝(이 값은 범위에 포함되지 않는다.)


<br>

`range(stop)` 는 0 부터 stop 이전까지의 숫자들을 포함하는 range 객체를 만들어 준다. 즉, range(0)는 해당하는 숫자 범위가 없기 때문에 empty가 리턴된다.

- range를 리스트로 변환하려면 list(range()) 처럼 리스트 생성자를 이용하여 변환

```python
result = list(range(5))
print(result)

for i in range(5):     
    print(i) 
```
```text
[0, 1, 2, 3, 4]

0, 1, 2, 3, 4
```

<br>

### range(start, stop)
---

```python
range(start, stop)
```

- start : 시작하는 숫자
- stop : 생성할 숫자 범위의 끝(이 값은 범위에 포함되지 않는다.)

<br>

`range(start, stop)` 는 start 부터 stop 이전까지의 숫자들을 포함하는 range 객체를 만들어 준다.

```python
result= list(range(2, 8)) 
print(result)

for i in range(2, 8):     
    print(i) 
```

```text
[2, 3, 4, 5, 6, 7]

2, 3, 4, 5, 6, 7
```

<br>

### range(start, stop, step)
---

```python
range(start, stop, step)
```

- start : 시작하는 숫자
- stop : 생성할 숫자 범위의 끝(이 값은 범위에 포함되지 않는다.)
- step : 각 숫자들 사이의 간격

<br>

`range(start, stop, step)` 는 start 부터 stop 이전까지의 숫자들 중 step 간격에 포함되는 range 객체를 만들어 준다.

```python
numbers = list(range(2, 15, 3)) 
print(numbers)  

for i in range(2, 15, 3):     
    print(i)
```

```text
[2, 5, 8, 11, 14]

2, 5, 8, 11, 14
```

<br>

### 활용
---

다음은 for 문에서 range를 사용하는 방법이다.

```python
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 항색 축하합니다. 합격입니다." % (number + 1))
```
```text
1번 항색 축하합니다. 합격입니다.
3번 항색 축하합니다. 합격입니다.
5번 항색 축하합니다. 합격입니다.
```

<br>

range() 함수를 사용하면 구구단을 간단하게 구현할 수 있다.

```python
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print(' ')
```
```text
2 4 6 8 10 12 14 16 18
3 6 9 12 15 18 21 24 27
4 8 12 16 20 24 28 32 36
5 10 15 20 25 30 35 40 45
6 12 18 24 30 36 42 48 54
7 14 21 28 35 42 49 56 63
8 16 24 32 40 48 56 64 72
9 18 27 36 45 54 63 72 81
```
