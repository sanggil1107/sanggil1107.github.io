
# while 문
---
반복해서 문장을 수행하야 할 경우 사용한다.
```
while <조건문>:
    <조건문이 참일 때 수행할 문장>
```

```python
>>> treeHit = 0
>>> while treeHit < 10:
...     treeHit += 1
...     print("나무를 %d번 찍었습니다." % treeHit)
...     if treeHit == 10:
...             print("나무 넘어간다")
...
나무를 1번 찍었습니다.
나무를 2번 찍었습니다.
나무를 3번 찍었습니다.
나무를 4번 찍었습니다.
나무를 5번 찍었습니다.
나무를 6번 찍었습니다.
나무를 7번 찍었습니다.
나무를 8번 찍었습니다.
나무를 9번 찍었습니다.
나무를 10번 찍었습니다.
나무 넘어간다
```

```python
>>> prompt = """
... 1. Add
... 2. Del
... 3. List
... 4. Quit
...
... Endter number: """
>>> number = 0
>>> while number != 4:
...     print(prompt)
...     number = int(input())
...

1. Add
2. Del
3. List
4. Quit

Endter number:
1

1. Add
2. Del
3. List
4. Quit

Endter number:
4
```
## break
---
반복문에서 빠져나오기 위해 사용한다.
```python
>>> coffee = 10
>>> while True:
...    money = int(input("돈을 넣어주세요 : "))
...    if money == 300:
...        print("커피를 줍니다.")
...        coffee -= 1
...        print("남은 커피의 양은 %d개 입니다." % coffee)
...    elif money > 300:
...        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
...        coffee -= 1
...        print("남은 커피의 양은 %d개 입니다." % coffee)
...    else:
...        print("돈이 부족합니다.")
...    if coffee == 0:
...        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
...        break

돈을 넣어주세요 : 400
거스름돈 100를 주고 커피를 줍니다.
남은 커피의 양은 9개 입니다.
돈을 넣어주세요 : 300
커피를 줍니다.
남은 커피의 양은 8개 입니다.
돈을 넣어주세요 : 200
돈이 부족합니다.
돈을 넣어주세요 : 204
돈이 부족합니다.
돈을 넣어주세요 : 600
거스름돈 300를 주고 커피를 줍니다.
남은 커피의 양은 7개 입니다.
돈을 넣어주세요 :
```

## continue 
---
특정 조건일 때에만 수행한 후 다시 조건문으로 돌아가고자 할 때 사용한다.
```python
>>> a = 0
>>> while a < 10:
...    a += 1
...    if a % 2 == 0:
...        continue
...    print(a)

1
3
5
7
9
```

# for문
---
```python
for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2
```
```python
>>> test_list = ['one', 'two', 'three']
>>> for i in test_list:
...     print(i)
...
one
two
three
```
`['one', 'two', 'three']` 리스트의 첫 번째 요소인 one이 먼저 i 번수에 대입된 후 `print(i)` 문장을 수행한다. 그 후 두 번째 요소 two가 i 변수에 대입된후 `print(i)` 문장을 수행하고
리스트 마지막 요소까지 반복한다.

```python
>>> a = [(1,2), (3,4), (4,5)]
>>> for (first, last) in a:
...     print(first, last)
...
1 2
3 4
4 5
```
위 예는 a 리스트의 각 요소값이 튜플이기 때문에 각각의 요소가 (first, last) 변수에 대입된다.(`(first, last) = (1,2)`)

```python
>>> marks = [90, 25, 67, 45, 80]
>>> number = 0
>>> for mark in marks:
...    number = number + 1
...    if mark >= 60:
...        print("%d번 학생은 합격입니다." % number)
...    else:
...        print("%d번 학생은 불합격입니다." % number)

1번 학생은 합격입니다.
2번 학생은 불합격입니다.
3번 학생은 합격입니다.
4번 학생은 불합격입니다.
5번 학생은 합격입니다.
```

for문에서도 continue 문을 사용할 수 있다.
```python
>>> marks = [90, 25, 67, 45, 80]
>>> number = 0
>>> for mark in marks:
...    number = number + 1
...    if mark < 60:
...        continue
...    print("%d번 학생은 합격입니다." % number)

1번 학생은 합격입니다.
3번 학생은 합격입니다.
5번 학생은 합격입니다.
```

## range
---
`range(시작 숫자, 끝 숫자)`  
range는 시작 숫자부터 끝 숫자 미만의 숫자를 포함하는 range 객체를 만들어 준다.  
시작 숫자 생략 시에는 0이 된다.(range(10) = 0 부터 10 미만의 숫자)
```python
>>> a = range(10)
>>> a
range(0, 10)
>>> a = range(1, 11)
>>> a
range(1, 11)
```

### 예시
---
```python
>>> add = 0
>>> for i in range(1, 11):
...     add = add + i
...
>>> print(add)
55
```
```python
>>> marks = [90, 25, 67, 45, 80]
>>> for number in range(len(marks)):
...    if marks[number] < 60:
...        continue
...    print("%d번 항색 축하합니다. 합격입니다." % (number + 1))

1번 항색 축하합니다. 합격입니다.
3번 항색 축하합니다. 합격입니다.
5번 항색 축하합니다. 합격입니다.
```

range() 함수를 사용하면 구구단을 간단하게 구현할 수 있다.
```python
>>> for i in range(2,10):
...     for j in range(1,10):
...             print(i*j, end=" ")
...     print(' ')
...
2 4 6 8 10 12 14 16 18
3 6 9 12 15 18 21 24 27
4 8 12 16 20 24 28 32 36
5 10 15 20 25 30 35 40 45
6 12 18 24 30 36 42 48 54
7 14 21 28 35 42 49 56 63
8 16 24 32 40 48 56 64 72
9 18 27 36 45 54 63 72 81
```

### 리스트 내포
---
```
[표현식 for 항목 in 반복가능객체 (if 조건문)]
```
리스트 안에 for문을 포함하는 것을 의미하며 다중 for문을 사용할 수 있다.
```
[표현식 for 항목1 in 반복가능객체 (if 조건문1)
        for 항목2 in 반복가능객체 (if 조건문2)]
```
```python
>>> a = [1,2,3,4]
>>> result = [num * 3 for num in a]
>>> print(result)
[3, 6, 9, 12]

>>> a = [1,2,3,4]
>>> result = [num * 3 for num in a if num % 2 == 0]
>>> print(result)
[6, 12]
```

아래와 같이 간단하게 구구단을 구현할 수 있다.
```python
>>> result = [x*y for x in range(2,10)
...                     for y in range(1,10)]
>>> print(result)
[2, 4, 6, 8, 10, 12, 14, 16, 18, 3, 6, 9, 12, 15, 18, 21, 24, 27, 4, 8, 12, 16, 20, 24, 28, 32, 36, 5, 10, 15, 20, 25, 30, 35, 40, 45, 6, 12, 18, 24, 30, 36, 42, 48, 54, 7, 14, 21, 28, 35, 42, 49, 56, 63, 8, 16, 24, 32, 40, 48, 56, 64, 72, 9, 18, 27, 36, 45, 54, 63, 72, 81]
```

#### 연습문제
sum = 0
a = 1
while a <= 1000:
    
    if a % 3 == 0:
        sum += a
    a += 1

print(sum)


count = 1
while count < 6:
    print("*" * count)
    count += 1



for a in range(1,101):
    print(a)


a = [70,60,55,75,95,90,80,80,85,100]
score = 0
for score in a:
    score += score

print(score / len(a))



number = [1,2,3,4,5]
result = [n*2 for n in number if n % 2 == 1]
print(result)


a = "Life is too short, you need python"

if "wife" in a:
    print("wife")
elif "python" in a and "you" not in a:
    print("python")
elif "shirt" not in a:
    print("shirt")
elif "need" in a:
    print("need")
else:
    print("none")

