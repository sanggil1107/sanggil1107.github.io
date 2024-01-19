t = int(input())

for _ in range(t):
  h, w, n = map(int, input().split())
  x = n % h
  y = n // h + 1
  if n % h == 0:
    x = h
    y = n // h

  print(x * 100+y)
  