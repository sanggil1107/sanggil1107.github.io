n = int(input())

for _ in range(n):
    st = input()

    sum = 0
    i = 1
    for s in st:
        if s == 'O':
            sum += i
            i += 1
        else:
            i = 1

    print(sum)