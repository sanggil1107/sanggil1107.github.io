N = int(input())
n = 2
while N > 1:
    if N%n == 0:
        N //= n
        print(n)
    else:
        n += 1