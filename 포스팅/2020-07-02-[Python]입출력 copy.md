


## 파일 읽기, 파일쓰기

### 파일 생성(open, close)
---

`open` 함수는 파일을 생성할 때 사용하는 함수이며 `close` 함수는 오픈한 파일을 닫을 때 사용하는 함수이다.

```python
open(file, mode)
close()
```

- file : 생성할 파일 경로
- mode : 파일이 열리는 옵션, 모드

|파일열기모드|설명|
|:---:|:---:|
|r|읽기모드 - 파일을 읽기만 할 때 사용|
|w|쓰기모드 - 파일에 내용을 쓸 때 사용|
|a|추가모드 - 파일의 마지막에 새로운 내용을 추가할 때 사용|

`w` 쓰기모드의 경우 해당 파일이 이미 존재할 경우 기존 내용은 사라지고, 해당 파일이 존재하지 않으면 새로 생성된다.

<br>

#### 파일 생성 예제

```python
f = open('D:/기타/new.txt', 'w')

f.write('yangpang')
f.write('\npython open func') 

f.close()
```
```text
yangpang
python open func
```

<br>

### 파일 쓰기(write, writelines)
---

`write`, `writelines` 함수는 파일에 내용을 쓸 때 사용하는 함수이다.

```python
write('문자열')
writelines(리스트)
```

<br>

#### 파일 쓰기 예제

```python
f = open('D:/기타/new.txt', 'w')

f.write('write write write\n')
f.write('파이썬 파일 입출력 포스팅\n') 

f.close()
```
```text
write write write
파이썬 파일 입출력 포스팅
```

<br>

```python
f = open('D:/기타/new.txt', 'a')

f.writelines(['a', 'b', '123', '456', 'abcdefg', '\n'])
f.writelines('\n'.join(['yangapng', 'python', 'blog'])) 
f.close() 
```
```text
write write write
파이썬 파일 입출력 포스팅
ab123456abcdefg
yangpang
python
blog
```

<br>

### 파일 읽기(read, readline, readlines)
---

`read`, `readline`, `readlines` 함수는 파일 내용을 읽을 때 사용하는 함수이다.

```python
read
```

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

