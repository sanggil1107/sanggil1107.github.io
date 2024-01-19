n = int(input())
a = []
m = 0

for _ in range(n):
  start, end = map(int, input().split())
  a.append([start, end])

a = sorted(a,key=lambda x:x[0]) # 시작 시간을 기준으로 정렬
a = sorted(a,key=lambda x:x[1]) # 끝나는 시간을 기준으로 정렬

last = 0
count = 0

for i, j in a:
  if i >= last:
     count += 1
     last = j

print(count)