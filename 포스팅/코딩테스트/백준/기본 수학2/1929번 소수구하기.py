# 일반적인 소수 판별
import sys

def prime(p):
    if p == 1:
        return False
    for i in range(2, int(p**0.5)+1):
        if p % i == 0:
            return False
    return True # 소수


m,n = map(int, sys.stdin.readline().split())

for i in range(m, n+1):
  if prime(i):
    print(i)


# 에라토스테네스의 체
import sys

def prime(p):
  prim = [True] * (p+1)
  for i in range(2, int(p**0.5)+1):
    if prim[i]:
      for j in range(2*i, p+1, i):
        prim[j] = False
  return prim

m,n = map(int, sys.stdin.readline().split())

prim = prime(n)
for i in range(m, n+1):
  if i > 1 and prim[i] == True:
    print(i)