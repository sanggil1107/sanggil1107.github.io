n = int(input())
array = list(map(int, input().split()))
array1 = [0] * n
count = 0

for i in range(n):
    t = array[i]
    d = 0
    if i - t + 1 >= 0:
        for j in range(t):
            if array1[i-t+1+j] == 0:
                d += 1
    
    if d == t:
        count += 1
        for j in range(t):
            array1[i-t+1+j] = 1

print(count)