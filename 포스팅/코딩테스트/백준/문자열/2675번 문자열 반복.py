t = int(input())
result = []

for _ in range(t):
    r, s = input().split()

    temp = ''
    for i in s:
        temp += int(r) * i
    result.append(temp)

for i in range(t):
    print(result[i])