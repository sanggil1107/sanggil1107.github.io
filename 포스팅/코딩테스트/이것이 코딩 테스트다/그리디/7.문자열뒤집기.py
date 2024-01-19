a = input()
d = [0, 0]
t = a[0]

for i in range(1, len(a)):
    if  t != a[i]:
        d[int(t)] += 1
        t = a[i]
    else:
        t = a[i]

d[int(t)] += 1

print(min(d[0], d[1]))
