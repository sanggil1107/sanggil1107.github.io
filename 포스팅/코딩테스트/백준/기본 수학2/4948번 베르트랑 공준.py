def prime(p):
  prim = [True] * (p+1)
  for i in range(2, int(p**0.5)+1):
    if prim[i]:
      for j in range(2*i, p+1, i):
        prim[j] = False
  return prim

while True:
  n = int(input())
  count = 0
  if n == 0:
    break
  
  prim = prime(2*n)
  for i in range(n+1, 2*n+1):
    if i > 1 and prim[i] == True:
      count+=1

  print(count)