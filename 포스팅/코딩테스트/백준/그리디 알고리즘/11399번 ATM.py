n = int(input())
p = list(map(int, input().split()))

total = [0] * n
temp = 0

p.sort()

for i in range(n):
  temp += p[i]
  total[i] = temp

print(sum(total))