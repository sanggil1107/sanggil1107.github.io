h, m = map(int, input().split())

m = m - 45

if m < 0:
    m = 60 + m
    if h == 0:
        h = 23
    else:
        h -= 1

print(h, m, end = ' ')