n = int(input())
sum = 0
a = list(map(int, input().split()))
m = max(a)

for i in range(n):
    sum += a[i]/m * 100

print(sum / n)