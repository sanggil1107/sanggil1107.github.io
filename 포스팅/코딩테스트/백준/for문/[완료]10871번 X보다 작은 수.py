n, x = map(int, input().split())

arr = list(map(int, input().split()))

for a in arr:
    if x > a:
        print(a, end=' ')