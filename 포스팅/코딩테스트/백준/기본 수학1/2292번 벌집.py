n = int(input())

a = 2
i = 1
if n == 1:
  print(1)
else:
  while True:
    a = a + 6 * i
    if a > n:
      print(i+1)
      break
    i+=1
