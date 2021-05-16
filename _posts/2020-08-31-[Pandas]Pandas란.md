---
layout: post
title: "[Pandas] Pandas란"
category: [데이터분석]

---
<br>

`Pandas`에 대해 알아보자
<!-- more -->

<hr>
     
>>> import pandas as pd
>>> pan = pd.Series([4,7,-5,3])
>>> pan
0    4
1    7
2   -5
3    3
dtype: int64

>>> pan.values
array([ 4,  7, -5,  3], dtype=int64)

>>> pan.index
RangeIndex(start=0, stop=4, step=1)

>>> pan.dtypes
dtype('int64')

>>> pan = pd.Series([4,7,-5,3], index=['a','b','c','d'])
>>> pan
a    4
b    7
c   -5
d    3
dtype: int64

>>> data = {'Yang' : 35000, 'Choi' : 50000, 'Sang' : 14000, 'Ha' : 62000}
>>> pan = pd.Series(data)
>>> pan
Yang    35000
Choi    50000
Sang    14000
Ha      62000
dtype: int64

>>> pan.name = 'Salary'
>>> pan.index.name = 'Name'
>>> pan
Name
Yang    35000
Choi    50000
Sang    14000
Ha      62000
Name: Salary, dtype: int64

>>> pan.index = ['1','2','3','4']
>>> pan
1    35000
2    50000
3    14000
4    62000
Name: Salary, dtype: int64

Dataframe

>>> data = {'name' : ['Yang', 'Choi', 'Sang', 'Ha'], 'year' : [2017, 2018, 2019,2020], 'age' 
: [20, 30, 40,50]}
>>> df = pd.DataFrame(data)
>>> df
   name  year  age
0  Yang  2017   20
1  Choi  2018   30
2  Sang  2019   40
3    Ha  2020   50

>>> df.index
RangeIndex(start=0, stop=4, step=1)

>>> df.columns
Index(['name', 'year', 'age'], dtype='object')
>>> df.values
array([['Yang', 2017, 20],
       ['Choi', 2018, 30],
       ['Sang', 2019, 40],
       ['Ha', 2020, 50]], dtype=object)

>>> df.index.name = 'Num'
>>> df.columns.name = 'Info'
>>> df
Info  name  year  age
Num
0     Yang  2017   20
1     Choi  2018   30
2     Sang  2019   40
3       Ha  2020   50       

>>> df1 = pd.DataFrame(data, columns=['year', 'name', 'age', 'point'], index=['A','B','C','D'])
>>> df1
   year  name  age point
A  2017  Yang   20   NaN
B  2018  Choi   30   NaN
C  2019  Sang   40   NaN
D  2020    Ha   50   NaN

>>> df1.describe()
              year        age
count     4.000000   4.000000
mean   2018.500000  35.000000
std       1.290994  12.909944
min    2017.000000  20.000000
25%    2017.750000  27.500000
50%    2018.500000  35.000000
75%    2019.250000  42.500000
max    2020.000000  50.000000

>>> df1
   year  name  age point
A  2017  Yang   20   NaN
B  2018  Choi   30   NaN
C  2019  Sang   40   NaN
D  2020    Ha   50   NaN

>>> df1['year'] // df.year
A    2017
B    2018
C    2019
D    2020
Name: year, dtype: int64

>>> df1[['year', 'age']]
   year  age
A  2017   20
B  2018   30
C  2019   40
D  2020   50

>>> df1.point = 50
>>> df1
   year  name  age  point
A  2017  Yang   20     50
B  2018  Choi   30     50
C  2019  Sang   40     50
D  2020    Ha   50     50

>>> df1.point = [10,20,30,40]
>>> df1
   year  name  age  point
A  2017  Yang   20     10
B  2018  Choi   30     20
C  2019  Sang   40     30
D  2020    Ha   50     40

>>> df1['new'] = np.arange(4)
>>> df1
   year  name  age  point  new
A  2017  Yang   20     10    0
B  2018  Choi   30     20    1
C  2019  Sang   40     30    2
D  2020    Ha   50     40    3

>>> df1['mul'] = df1['point'] * df1['new']
>>> df1
   year  name  age  point  new  mul
A  2017  Yang   20     10    0    0
B  2018  Choi   30     20    1   20
C  2019  Sang   40     30    2   60
D  2020    Ha   50     40    3  120

>>> df1['bool'] = df1['point'] > 20
>>> df1
   year  name  age  point  new  mul   bool
A  2017  Yang   20     10    0    0  False
B  2018  Choi   30     20    1   20  False
C  2019  Sang   40     30    2   60   True
D  2020    Ha   50     40    3  120   True


>>> del df1['bool']
>>> df1
   year  name  age  point  new  mul
A  2017  Yang   20     10    0    0
B  2018  Choi   30     20    1   20
C  2019  Sang   40     30    2   60
D  2020    Ha   50     40    3  120

>>> df1.index.name = 'Order'
>>> df1.columns.name = 'Info'
>>> df1
Info   year  name  age  point  new  mul
Order
A      2017  Yang   20     10    0    0
B      2018  Choi   30     20    1   20
C      2019  Sang   40     30    2   60
D      2020    Ha   50     40    3  120

>>> df1[0:2]
Info   year  name  age  point  new  mul
Order
A      2017  Yang   20     10    0    0
B      2018  Choi   30     20    1   20

>>> df1.loc['A']
Info
year     2017
name     Yang
age        20
point      10
new         0
mul         0
Name: A, dtype: object

>>> df1.loc['A':'C']
Info   year  name  age  point  new  mul
Order
A      2017  Yang   20     10    0    0
B      2018  Choi   30     20    1   20
C      2019  Sang   40     30    2   60

>>> df1.loc['A':'C', 'name']
Order
A    Yang
B    Choi
C    Sang
Name: name, dtype: object

>>> df1.loc[:,'age']
Order
A    20
B    30
C    40
D    50
Name: age, dtype: int64

>>> df1.loc['A':'C', 'year':'point']
Info   year  name  age  point
Order
A      2017  Yang   20     10
B      2018  Choi   30     20
C      2019  Sang   40     30

>>> df1.loc['E', :] = [2021, 'Gil', 60, 50, 4, 200]
>>> df1
Info     year  name   age  point  new    mul
Order
A      2017.0  Yang  20.0   10.0  0.0    0.0
B      2018.0  Choi  30.0   20.0  1.0   20.0
C      2019.0  Sang  40.0   30.0  2.0   60.0
D      2020.0    Ha  50.0   40.0  3.0  120.0
E      2021.0   Gil  60.0   50.0  4.0  200.0

>>> df1.iloc[1]
Info
year     2018
name     Choi
age        30
point      20
new         1
mul        20
Name: B, dtype: object

>>> df1.iloc[0:3, 0:3]
Info     year  name   age
Order
A      2017.0  Yang  20.0
B      2018.0  Choi  30.0
C      2019.0  Sang  40.0

>>> df1.iloc[[0,1,3], [1,2]]
Info   name   age
Order
A      Yang  20.0
B      Choi  30.0
D        Ha  50.0

>>> df1.iloc[1,1]
'Choi'