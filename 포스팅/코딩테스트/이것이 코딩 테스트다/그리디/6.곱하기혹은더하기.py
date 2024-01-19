a = input()
total = int(a[0])

for i in range(1, len(a)):
    if total == 0 or total == 1:
        total += int(a[i])
    else:
        if a[i] == 0 or a[i] == 1:
            total += int(a[i])
        else:
            total *= int(a[i])

print(total)