def prime(p):
    if p == 1:
        return False
    for i in range(2, p-1):
        if p % i == 0:
            return False
    return True # 소수

m = int(input())
n = int(input())
total = 0
mi = n+1

for i in range(m, n+1):
  if prime(i):
    total+=i
    if mi > i:
      mi = i

if total == 0:
  print(-1)
else:
  print(total, mi, sep='\n')