
## enumerate 함수


`enumerate 함수` 는 반복 가능한 객체를 인자로 받아서 해당 객체의 요소들을 순회하면서, 각 요소의 인덱스와 값을 순서쌍으로 반환하는 함수이다.

```text
enumerate(iterable)
enumerate(iterable, start)
```

- iterable : 반복 가능한(iterable) 자로형
- start : 인덱스의 시작값, 기본값은 0

파이썬의 반올림은 반올림 하려는 수가 올림, 내림했을 때 동일하게 차이가 나는 경우에는 짝수 값으로 반올림한다.

<br>

### enumerate 함수 예제
---


```python
for entry in enumerate(['A', 'B', 'C']):
    print(entry)
```
```text
(0, 'A')
(1, 'B')
(2, 'C')
```

<br>

```python
for index, fruit in enumerate_fruits:
    print(index, fruit)
```
```text
0 apple
1 banana
2 cherry
```

<br>

```python
print(list(enumerate(['A', 'B', 'C'])))
```
```text
[(0, 'A'), (1, 'B'), (2, 'C')]
```

<br>

다음과 같이 2차원 리스트에서 사용할 수 있다.

```python
matrix = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]

for r, row in enumerate(matrix):
    for c, letter in enumerate(row):
        print(r, c, letter)
```
```text
0 0 A
0 1 B
0 2 C
1 0 D
1 1 E
1 2 F
2 0 G
2 1 H
2 2 I
```

#### 시작 인덱스 변경

```python
for i, letter in enumerate(['A', 'B', 'C'], start=100):
    print(i, letter)
```
```text
100 A
101 B
102 C
```
