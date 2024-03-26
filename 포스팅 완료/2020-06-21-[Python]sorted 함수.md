
## sorted 함수


`sorted 함수` 는 매개변수로 들어온 반복가능한 자료형의 데이터를 새로운 정렬된 리스트로 반들어서 반환하는 함수이다.

```text
sorted(x)
sorted(x, reverse 파라미터)
sorted(x, key 파라미터)
sorted(x, key 파라미터, reverse 파라미터)
```

- x : 반복 가능한 자료(리스트, 튜플 등)
- key 파라미터 : 어떤 것을 기준으로 정렬할지에 대한 값
- reverse 파라미터 : 오름차순일지 내림차순일지에 대한 구분 값

sort()와 sorted()의 가장 큰 차이는 sort()는 본체의 리스트를 정렬해서 변환 후 반환하는 것이며 sorted()는 본체는 놔두고 정렬한 새로운 리스트를 만들어 반환한다.

<br>

### sorted 함수 예제
---

```python
a = [2, 4, 1, 9, 100, 29, 40, 10]
b = sorted(a)
c = sorted(a, reverse=True)
 
 
print(f'origin                  : {a}')
print(f'sorted(a)               : {b}')
print(f'sorted(a, reverse=True) : {c}')

```
```text
origin                  : [2, 4, 1, 9, 100, 29, 40, 10]
sorted(a)               : [1, 2, 4, 9, 10, 29, 40, 100]
sorted(a, reverse=True) : [100, 40, 29, 10, 9, 4, 2, 1]
```

<br>

```python
text = "python"
sorted_text = sorted(text)
print(text)
```
```text
['h', 'n', 'o', 'p', 't', 'y']
```

<br>

key 파라미터에 일반함수를 넣어 사용할 수 있다.

```python
def sorted_key(x):
    if isinstance(x, str):
        return (True, x)
    else:
        return (False, x)

mixted_list = [3, 'apple', 1, 'banana', 4, 'cherry', 2]
sorted_mixted_list = sorted(mixed_list, key=sorted_key)
print(sorted_mixted_list)
```
```text
[1, 2, 3, 4, 'apple', 'banana', 'cherry']
```

<br>

일반적인 함수뿐만 아니라 람다함수와 함께 사용할 수 있다.

```python
countries = [
  {'code': 'KR', 'name': 'Korea'},
  {'code': 'CA', 'name': 'Canada'},
  {'code': 'US', 'name': 'United States'},
  {'code': 'GB', 'name': 'United Kingdom'},
  {'code': 'CN', 'name': 'China'}
]

print(sorted(countries, key=lambda country: country["code"]))

print(sorted(countries, key=lambda country: country["name"]))
```
```text
[{'code': 'CA', 'name': 'Canada'}, {'code': 'CN', 'name': 'China'}, {'code': 'GB', 'name': 'United Kingdom'}, {'code': 'KR', 'name': 'Korea'}, {'code': 'US', 'name': 'United States'}]

[{'code': 'CA', 'name': 'Canada'}, {'code': 'CN', 'name': 'China'}, {'code': 'KR', 'name': 'Korea'}, {'code': 'GB', 'name': 'United Kingdom'}, {'code': 'US', 'name': 'United States'}]
```

<br>

딕셔너리 key를 이용한 정렬은 다음과 같다.

```python
d = dict()
d['a'] = 66
d['i'] = 20
d['e'] = 30
d['d'] = 33
d['f'] = 50
d['g'] = 60
d['c'] = 22
d['h'] = 80
d['b'] = 11
 
# 1. 딕셔너리 출력
print("\n1. 기본 딕셔너리")
print(d)
 
# 딕셔너리 키 정렬 오름차순(디폴트)
print("\n2. 키 정렬 sorted(d.items())")
f = sorted(d.items())
print(f)
 
# 딕셔너리 키 정렬 내림차순
print("\n3. 키 정렬 sorted(d.items(), reverse=True)")
g = sorted(d.items(), reverse=True)
print(g)
 
# 딕셔너리 키만 정렬 및 출력1
print("\n4. 키만 정렬 sorted(d.keys())")
h = sorted(d.keys())
print(h)
 
# 딕셔너리 키만 정렬 및 출력2
print("\n5. 키만 정렬 sorted(d)")
i = sorted(d)
print(i)
```
```text
1. 기본 딕셔너리
{'a':66, 'i':20, 'e':30, 'd':33, 'f':50, 'g':60, 'c':22, 'h':80, 'b':11}

2. 키 정렬 sorted(d.items())
[('a', 66), ('b', 11), ('c', 22), ('d', 33), ('e', 30), ('f', 50), ('g', 60), ('h', 80), ('i', 20)]

3. 키 정렬 sorted(d.items(), reverse=True)
[('i', 20), ('h', 80), ('g', 60), ('f', 50), ('e', 30), ('d', 33), ('c', 22), ('b', 11), ('a', 66)]

4. 키만 정렬 sorted(d.keys())
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i]

5. 키만 정렬 sorted(d)
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i]
```

<br>

딕셔너리 value를 이용한 정렬은 다음과 같다.

```python
import operator
 
d = {'b': 400, 'f': 300, 'a': 200, 'd': 100, 'c': 500}
 
print('1. 원본 딕셔너리')
print(d.items())

print('\n2. 딕셔너리 정렬 : sorted(d.items())')
f = sorted(d.items())
print(f)
 
print('\n3. 딕셔너리 정렬 : sorted(d.items(), key=operator.itemgetter(1))')
g = sorted(d.items(), key=operator.itemgetter(1))
print(g)
 
print('\n4. 딕셔너리 정렬 : sorted(d.items(), key=operator.itemgetter(1), reverse=True)')
h = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
print(h)
```
```text
1. 원본 딕셔너리
dict_items([('b', 400), ('f', 300), ('a', 200), ('d', 100), ('c', 500)])

2. 딕셔너리 정렬 : sorted(d.items())
[('a', 200), ('b', 400), ('c', 500), ('d', 100), ('f', 300)]

3. 딕셔너리 정렬 : sorted(d.items(), key=operator.itemgetter(1))
[('d', 100), ('a', 200), ('f', 300), ('b', 400), ('c', 500)]

4. 딕셔너리 정렬 : sorted(d.items(), key=operator.itemgetter(1), reverse=True)
[('c', 500), ('b', 400, ('f', 300), ('a', 200), ('d', 100)]
```
