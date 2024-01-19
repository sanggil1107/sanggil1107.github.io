

## 입출력 함수

파이썬 입출력 함수로는 `input` 과 `print` 함수가 있다.

<br>

### input()
---

`input(text)`
- 사용자 입력을 받으며 입력되는 모든 것을 문자열로 취급

```python
a = input()
Sanggil Yang
a

number = input('숫자를 입력하세요: ')
숫자를 입력하세요: 3
number
```

```text
Sanggil Yang

3
```

<br>

### print()
---

`print(x)`
- 입력한 자료형을 출력
- 큰타옴표("")로 둘러싸인 문자열은 + 연산과 동일하다.(띄어쓰기 X)
- 콤마(,)를 사용하여 띄어쓰기를 한다.

```python
print("sanggil" "is" "man")
print("sanggil" + "is" + "man")
print("sanggil", "is", "man")
print(1); print(2)
```
```text
sanggilisman
sanggilisman
sanggil is man
1
2
```

<br>

#### end

`end` 인수를 사용하여 마지막 개행(기본값)에 대해 처리할 수 있다.
  
```python
print("Print end", end=', '); print("test", end='. ')

for i in range(10):
    print(i, end= ' ')
```
```text
Print end, test.

0 1 2 3 4 5 6 7 8 9
```

<br>

#### sep

`sep` 인수를 사용하여 문장과 문장 사이의 공백에 대해 처리할 수 있다.

```python
print("a", "b", sep='%')
print("Print", "sep test", sep='%')
print(1, 2, 3, 4, sep='.')
```
```text
a%b
Print%sep test
1.2.3.4
```

# 파일 읽고 쓰기
---
## 파일 생성
---
```python
f = open("D:/기타/new.txt", 'w')
f.close
```
|파일열기모드|설명|
|:---:|:---:|
|r|읽기모드 - 파일을 읽기만 할 때 사용|
|w|쓰기모드 - 파일에 내용을 쓸 때 사용|
|a|추가모드 - 파일의 마지막에 새로운 내용을 추가할 때 사용|

`w` 쓰기모드의 경우 해당 파일이 이미 존재할 경우 기존 내용은 사라지고, 해당 파일이 존재하지 않으면 새로 생성된다.

```python
# file_write.py
f = open("D:/기타/new.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)

f.close
```
`readline()`

```python
# readline.py
f = open("D:/기타/new.txt", 'r')
line = f.readline()
print(line)
f.close()

python readline.py

1번째 줄입니다.
```

```python
# readline_all.py
f = open("D:/기타/new.txt", 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()

python readline_all.py

1번째 줄입니다.

2번째 줄입니다.

...

9번째 줄입니다.

10번째 줄입니다.
```

`readlines()는 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다.`
```python
# readlines.py
f = open("D:/기타/new.txt", 'r')
lines = f.readlines()
print(lines)
for line in lines:
    print(line)

f.close()

python readlines.py

['1번째 줄입니다.\n', '2번째 줄입니다.\n', '3번째 줄입니다.\n', '4번째 줄입니다.\n', '5번째 줄입니다.\n', '6번째 줄입니다.\n', '7번째 줄입니다.\n', '8번째 줄입니다.\n', '9번째 줄입니다.\n', '10번째 줄입니다.\n']
1번째 줄입니다.

2번째 줄입니다.

...

9번째 줄입니다.

10번째 줄입니다.
```

`read()는 파일의 내용 전체를 문자열로 돌려준다.`
```python
# read.py
f = open("D:/기타/new.txt", 'r')
data = f.read()
print(data)
f.close()

1번째 줄입니다.
2번째 줄입니다.
3번째 줄입니다.
4번째 줄입니다.
5번째 줄입니다.
6번째 줄입니다.
7번째 줄입니다.
8번째 줄입니다.
9번째 줄입니다.
10번째 줄입니다.
```

## 내용 추가
---
```python
f = open("D:/기타/new.txt", 'a')
for i in range(11,20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)

f.close()
```

`with`문을 사용하면 자동으로 close() 한다. 아래 두 예제는 동일한 문장이다.
```python
f = open("foo.txt". 'w')
f.write("Oh My got")
f.close()

with open("foo.txt". 'w') as f:
    f.write("Oh My got")
```

