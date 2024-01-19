# 이진 탐색
def bs(array, start, end, target):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return 1
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return 0

n = int(input())
narray = list(map(int, input().split()))
m = int(input())
marray = list(map(int, input().split()))

narray.sort()

for i in range(m):
  result = bs(narray, 0, n-1, marray[i])

  if result == 1:
    print("yes", end=' ')
  else:
    print("no", end=' ')



# 계수 정렬 사용 
n = int(input())
array = [0] * 1000000

for i in input().split():
  array[int(i)] = 1

m = int(input())
marray = list(map(int, input().split()))

for i in range(m):
  if array[marray[i]] == 1:
    print("yes", end=' ')
  else:
    print("no", end=' ')
'''
for i in marray:
  if array[i] == 1:
    print("yes", end=' ')
  else:
    print("no", end=' ')
'''