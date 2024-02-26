## time
---
시간 관련 모듈

### time()
---
UTC를 사용하여 현재 시간을 실수 형태로 출력
```python
>>> time.time()
1573641965.201
```

### localtime()
---
time.time()이 돌려준 실수 값을 이용하여 연도,월,일, 시, 분, 초의 형태로 출력
```python
>>> time.localtime(time.time())
time.struct_time(tm_year=2019, tm_mon=11, tm_mday=13, tm_hour=19, tm_min=47, tm_sec=21, tm_wday=2, tm_yday=317, tm_isdst=0)
```

### asctime()
---
time.localtime()에 의해 반환된 튜플 값을 이용하여 보기 쉬운 형태로 출력
```python
>>> time.asctime(time.localtime(time.time()))
'Wed Nov 13 19:49:49 2019'
```

### ctime()
---
time.asctime()와 동일
```python
>>> time.ctime()
'Wed Nov 13 19:50:24 2019'
```

### strftime()
---
시간 포맷 형식에 맞춰 출력
`time.strftime('출력할 형식 포맷 코드', time.localtime(time.time()))`
```python
>>> time.strftime('%x', time.localtime(time.time()))
'11/13/19'
```

|포맷코드|설명|예|
|---|---|---|
|%a|요일 줄임말|Mon|
|%A|요일|Monday|
|%b|달 줄임말|jan|
|%B|달|January|
|%c|날짜와 시간|19/12/02 19:22:14|
|%d|날|01~31|
|%H|시간-24시간 형태|00~23|
|%I|시간-12시간 형태|00~12|
|%j|1년 중 누적 날짜|001~366|
|%m|달|01~12|
|%M|분|01~59|
|%p|AM or PM|AM/PM|
|%S|초|00~59|
|%U|1년 중 누적 주-일요일 시작|00~53|
|%w|숫자료된 요일-일요일:0|0~6|
|%W|1년 중 누적 주-월요일 시작|00~53|
|%x|날짜 출력|19/12/02|
|%X|시간 출력|19:08:55|
|%Y|년도|2019|
|%Z|시간대|대한민국 표준시
|%%|문자|%|
|%y|세기부분을 제외한 년도|19|
