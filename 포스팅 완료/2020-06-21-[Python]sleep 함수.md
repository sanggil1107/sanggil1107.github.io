
## sleep 함수


`sleep 함수` 는 인자로 들어온 시간 동안 일시정지하는 함수이다.

```text
time.sleep(x)
```

- x : 숫자 자료형

sleep 함수는 time 모듈을 import 해야한다. 

<br>

### sleep 함수 예제
---

```python
import time
import datetime
 
print('-' * 10)
now = datetime.datetime.now()
print(now.strftime('%H:%M:%S'))  # 현재 시간 출력

time.sleep(5)  # 5 초 딜레이

now = datetime.datetime.now()
print(now.strftime('%H:%M:%S'))

time.sleep(10)  # 10 초 딜레이

print(datetime.datetime.now().strftime('%H:%M:%S'))


print('-' * 10)
print(datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3])

time.sleep(0.5)  # 0.5 초 딜레이

print(datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3])  # 밀리초 3자리까지만 출력

time.sleep(0.06)  # 0.06 초 딜레이

now = datetime.datetime.now()
print(now.strftime('%H:%M:%S.%f')[:-3])
```
```text
----------
10:13:20

10:13:25

10:13:35

----------
10:14:835

10:15:350

10:15:425
```
