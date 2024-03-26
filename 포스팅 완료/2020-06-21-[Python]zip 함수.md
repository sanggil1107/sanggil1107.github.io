
## zip 함수

`zip 함수` 는 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 튜플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환하는 함수이다.

```text
zip(iterable1, iterable2)
```

- iterable : 반복 가능한 자료형(리스트, 튜플 등)

<br>

### zip 함수 예제
---

```python
numbers = [1, 2, 3]
letters = ["A", "B", "C"]
for pair in zip(numbers, letters):
    print(pair)
```
```text
(1, 'A')
(2, 'B')
(3, 'C')
```

<br>

```python
for number, upper, lower in zip("12345", "ABCDE", "abcde"):
    print(number, upper, lower)
```
```text
1 A a
2 B b
3 C c
4 D d
5 E e
```

<br>

```python
keys = [1, 2, 3]
values = ["A", "B", "C"]

print(dict(zip(keys, values)))
```
```text
{1: 'A', 2: 'B', 3: 'C'}
```

<br>

### zip 해체(unzip)
---

인자에 * 연산자를 붙이면 `zip()` 함수를 통해 엮어 놓은 데이터를 다시 해체(unzip)할 수 있다.


```python
numbers = (1, 2, 3)
letters = ("A", "B", "C")
pairs = list(zip(numbers, letters))

numbers, letters = zip(*pairs)

print(numbers)
print(letters)
```
```text
(1, 2, 3)
('A', 'B', 'C')
```
