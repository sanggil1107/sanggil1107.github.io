a = []
for i in range(10):
    n = int(input())
    k = n % 42
    if k not in a:
        a.append(k)

print(len(a))