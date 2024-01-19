n, k = map(int, input().split())
items = [int(input()) for _ in range(n)]
count = 0


for i in range(n-1, -1, -1):
  if k >= items[i]:
    count += k // items[i]
    k = k % items[i]



print(count)