from itertools import combinations

n = int(input())
item = list(map(int, input().split()))
count = sum(item)
d = [0] * count

for i in range(1, len(item)):
    # print(list(map(''.join, combinations(item, i))))
    # print(list(combinations(item, i)))
    for c in combinations(item, i):
        d[sum(c)] = 1

for i in range(1, count):
    if d[i] == 0:
        print(i)
        break