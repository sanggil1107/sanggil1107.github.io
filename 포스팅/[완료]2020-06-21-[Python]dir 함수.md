
## dir 함수


`dir 함수` 는 객체가 가지고 있는 속성과 메서드를 나열하는 함수이다.

```text
dir(객체)
```

객체의 내부 구조 및 정보를 확인할 수 있다.

<br>

### dir 함수 예제
---

```python
dir()
```
```text
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
```

<br>

```python
dir((1,2))
```
```text
['count', 'index', ...]
```

<br>

```python
dir({'1':'b'})
```
```text
['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values', ...]
```
