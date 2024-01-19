m = []
for i in range(9):
    a = int(input())
    m.append(a)

print(max(m))
print(m.index(max(m))+1)